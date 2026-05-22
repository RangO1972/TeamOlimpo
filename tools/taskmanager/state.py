"""state.yaml backing store with file locking for the Task Manager.

Exports:
    StateStore — thread-safe YAML backing store with fcntl locking
    _find_project_root — locate project root from CWD or file location
"""

from __future__ import annotations

import fcntl
import os
import shutil
import tempfile
from pathlib import Path
from typing import Any

import yaml
from loguru import logger

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_STATE: dict[str, Any] = {
    "version": 1,
    "last_updated": "",
    "counter": {},
    "tasks": {},
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _find_project_root() -> Path:
    """Locate the Team Olimpo project root directory.

    Strategy (in order):
    1. Walk up from CWD looking for ``tools/config.yaml``.
    2. Fall back to ``pyproject.toml`` in parent directories.
    3. Fall back to ``Path(__file__)`` based resolution.

    Returns:
        Absolute path to the project root.

    Raises:
        FileNotFoundError: If no project root can be determined.
    """
    cwd = Path.cwd().resolve()
    for candidate in [cwd, *cwd.parents]:
        if (candidate / "tools" / "config.yaml").is_file():
            logger.debug(f"Project root found via tools/config.yaml: {candidate}")
            return candidate
    for candidate in [cwd, *cwd.parents]:
        if (candidate / "pyproject.toml").is_file():
            logger.debug(f"Project root found via pyproject.toml: {candidate}")
            return candidate

    # Fallback: from this file's location: tools/taskmanager/state.py → tools/ → root
    file_based = Path(__file__).resolve().parent.parent.parent
    if (file_based / "tools" / "config.yaml").is_file():
        logger.debug(f"Project root found via file location: {file_based}")
        return file_based

    raise FileNotFoundError(
        "Could not locate Team Olimpo project root. "
        "Run from within the project directory."
    )


# ---------------------------------------------------------------------------
# StateStore
# ---------------------------------------------------------------------------


class StateStore:
    """Thread-safe state.yaml backing store with fcntl file locking.

    Usage::

        store = StateStore()
        data = store.load()
        data["tasks"]["T-MY-001"] = task_dict
        store.save()

    The store caches data in memory; call ``reload()`` to force a disk read.
    File locking with ``fcntl.flock`` prevents concurrent writes from
    external processes.
    """

    def __init__(self, path: Path | None = None) -> None:
        """Initialize the store.

        Args:
            path: Explicit path to state.yaml. If ``None``, auto-detect
                  from ``Library/System/Hermes/state.yaml`` relative to project root.
        """
        if path is not None:
            self._path = path.resolve()
        else:
            project_root = _find_project_root()
            self._path = (project_root / "Library" / "System" / "Hermes" / "state.yaml").resolve()
        self._lock_path = self._path.with_name(f".{self._path.name}.lock")
        self._data: dict[str, Any] | None = None
        self._lock_fd: int | None = None

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def path(self) -> Path:
        """Return the path to state.yaml."""
        return self._path

    # ------------------------------------------------------------------
    # File locking
    # ------------------------------------------------------------------

    def _acquire_lock(self) -> None:
        """Acquire an exclusive file lock (fcntl.flock)."""
        self._lock_path.parent.mkdir(parents=True, exist_ok=True)
        if not self._lock_path.exists():
            self._lock_path.touch()
        fd = os.open(str(self._lock_path), os.O_RDONLY)
        fcntl.flock(fd, fcntl.LOCK_EX)
        self._lock_fd = fd
        logger.debug(f"Lock acquired on {self._lock_path}")

    def _release_lock(self) -> None:
        """Release the file lock."""
        if self._lock_fd is not None:
            fcntl.flock(self._lock_fd, fcntl.LOCK_UN)
            os.close(self._lock_fd)
            self._lock_fd = None
            logger.debug("Lock released")

    # ------------------------------------------------------------------
    # Read / Write
    # ------------------------------------------------------------------

    def load(self) -> dict[str, Any]:
        """Load state from disk into memory.

        Returns the in-memory data dict. On first call (or after
        ``reload()``), reads from the YAML file. If the file does not
        exist, creates a default empty state.

        Returns:
            The state dict with keys ``version``, ``last_updated``,
            ``counter``, ``tasks``.

        Raises:
            ValueError: If the YAML file is malformed.
        """
        if self._data is not None:
            return self._data

        if not self._path.exists():
            logger.info(f"state.yaml not found at {self._path}, creating default")
            self._data = dict(DEFAULT_STATE)
            # Write default to disk immediately so the file exists
            self._save_raw()
            return self._data

        try:
            raw = self._path.read_text(encoding="utf-8")
            parsed = yaml.safe_load(raw)
        except yaml.YAMLError as exc:
            raise ValueError(
                f"state.yaml malformed at {self._path}: {exc}. "
                "File non modificato."
            ) from exc

        if not isinstance(parsed, dict):
            raise ValueError(
                f"state.yaml at {self._path} must be a YAML dictionary, "
                f"got {type(parsed).__name__}. File non modificato."
            )

        # Ensure all top-level keys exist
        for key, default_val in DEFAULT_STATE.items():
            if key not in parsed:
                parsed[key] = default_val

        self._data = parsed
        logger.debug(f"State loaded from {self._path} ({len(parsed.get('tasks', {}))} tasks)")
        return self._data

    def _save_raw(self) -> None:
        """Atomically write ``self._data`` to the YAML file.

        Uses a temporary file + ``shutil.move`` for atomic write.
        """
        self._path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp_path = tempfile.mkstemp(
            suffix=".yaml",
            prefix=f".{self._path.name}.",
            dir=self._path.parent,
        )
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                yaml.dump(
                    self._data,
                    f,
                    default_flow_style=False,
                    allow_unicode=True,
                    sort_keys=False,
                    indent=2,
                )
            shutil.move(tmp_path, str(self._path))
        except Exception:
            # Clean up temp file on failure
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
            raise

    def save(self) -> None:
        """Write the current in-memory state to the YAML file with locking.

        The ``last_updated`` field is automatically set to the current
        UTC timestamp before writing.
        """
        if self._data is None:
            logger.warning("save() called with no data loaded — loading first")
            self.load()
            return

        self._acquire_lock()
        try:
            # Update timestamp
            from tools.taskmanager.models import now_iso

            self._data["last_updated"] = now_iso()
            self._save_raw()
            logger.debug(f"State saved to {self._path}")
        finally:
            self._release_lock()

    def reload(self) -> dict[str, Any]:
        """Force a full reload from disk, discarding the in-memory cache.

        Returns:
            The reloaded state dict.
        """
        self._data = None
        return self.load()

    # ------------------------------------------------------------------
    # Task-specific helpers
    # ------------------------------------------------------------------

    def get_tasks(self) -> dict[str, dict[str, Any]]:
        """Return the ``tasks`` dict (id → task dict)."""
        return self.load().setdefault("tasks", {})

    def get_task(self, task_id: str) -> dict[str, Any] | None:
        """Return a single task dict, or ``None`` if not found."""
        return self.get_tasks().get(task_id)

    def get_counter(self) -> dict[str, int]:
        """Return the area counter dict."""
        return self.load().setdefault("counter", {})

    def _ensure_loaded_for_write(self) -> dict[str, Any]:
        """Ensure data is loaded and return it for modification.

        Caller **must** call ``save()`` after modifications.
        """
        if self._data is None:
            self.load()
        return self._data  # type: ignore[return-value]

    def next_task_id(self, area: str) -> str:
        """Generate the next task ID for an *area* and increment the counter.

        Called before adding a task. Example::

            task_id = store.next_task_id("MCP")
            # Returns "T-MCP-003" if counter was at 2
            # Counter is incremented to 3

        Note:
            The counter increment is persisted when ``save()`` is called.
        """
        data = self._ensure_loaded_for_write()
        counter: dict[str, int] = data.setdefault("counter", {})
        tasks: dict[str, Any] = data.setdefault("tasks", {})
        current = counter.get(area, 0) + 1
        # Increment until we find an ID that doesn't collide with existing tasks
        # (handles explicit IDs that were set manually, e.g. T-PARENT-001)
        while f"T-{area}-{current:03d}" in tasks:
            current += 1
        counter[area] = current
        return f"T-{area}-{current:03d}"
