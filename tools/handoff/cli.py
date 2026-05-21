"""CLI: generate and list handoff files for Team Olimpo.

Commands:
    main (default)  — Generate a formatted handoff file from a body file.
    list            — Query/filter existing handoff files.

Write usage:
    uv run python -m tools.handoff main --body Team/<agent>/hf.md
    uv run python -m tools.handoff main --body Team/<agent>/hf-T-042.md -v

List usage:
    uv run python -m tools.handoff list
    uv run python -m tools.handoff list --agent efesto --type report
    uv run python -m tools.handoff list --since 2026-05-01 --until 2026-05-15 --paths

See ``list --help`` for full filter options.
"""

from __future__ import annotations

import json as json_lib
import re
import sys
from dataclasses import dataclass
from datetime import date as date_type
from datetime import datetime
from pathlib import Path
from typing import Optional

import typer
import yaml
from loguru import logger
from rich.console import Console
from rich.table import Table

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VALID_TYPES = {
    "report",
    "profile",
    "spec",
    "test",
    "analysis",
    "note",
    "bug",
    "feedback",
}

SLUG_MAX_CHARS = 50
SLUG_MAX_WORDS = 5

# Filename regexps — tried in order for best-effort metadata extraction
# Canonical:   YYYY-MM-DD_HHMM_agent_type_slug.md
# Extended:    YYYY-MM-DD_agent_type_slug.md   (no HHMM)
# Basic:       YYYY-MM-DD_slug.md              (no agent/type in name)
_CANONICAL_FN_RE = re.compile(
    r"^(\d{4}-\d{2}-\d{2})_(\d{4})_([a-z][a-z0-9-]+)_([a-z][a-z0-9-]+)_(.+)\.md$"
)
_EXTENDED_FN_RE = re.compile(
    r"^(\d{4}-\d{2}-\d{2})_([a-z][a-z0-9-]+)_([a-z][a-z0-9-]+)_(.+)\.md$"
)
_BASIC_FN_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})_(.+)\.md$")
_DATE_PREFIX_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")

# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------

app = typer.Typer(
    name="handoff",
    help="Generate and list handoff files for Team Olimpo.",
    no_args_is_help=True,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _setup_logging(verbose: bool) -> None:
    """Configure loguru: WARNING by default, DEBUG with --verbose."""
    logger.remove()
    level = "DEBUG" if verbose else "WARNING"
    logger.add(sys.stderr, level=level, format="<level>{level}</level>: {message}")


def _find_project_root() -> Path:
    """Locate the project root directory.

    Strategy (in order):
    1. Walk up from CWD looking for ``tools/config.yaml``.
    2. Fall back to ``Path(__file__)`` based resolution (parent of ``tools/``).
    3. If not found, raise ``FileNotFoundError``.
    """
    cwd = Path.cwd()
    for candidate in [cwd, *cwd.parents]:
        if (candidate / "tools" / "config.yaml").is_file():
            return candidate

    # Fallback: from this file's location: tools/handoff/cli.py → tools/ → root
    file_based = Path(__file__).resolve().parent.parent.parent
    if (file_based / "tools" / "config.yaml").is_file():
        return file_based

    raise FileNotFoundError(
        "Could not locate project root: no tools/config.yaml found from CWD or file location."
    )


def _load_config(project_root: Path) -> dict:
    """Load and validate ``tools/config.yaml``.

    Returns the parsed config dict. Exits with code 1 on error.
    """
    config_path = project_root / "tools" / "config.yaml"
    if not config_path.is_file():
        logger.error(f"Config file not found: {config_path}")
        raise typer.Exit(code=1)

    with open(config_path, encoding="utf-8") as f:
        config: dict = yaml.safe_load(f) or {}

    if "handoff" not in config:
        logger.error("Missing 'handoff' section in tools/config.yaml")
        raise typer.Exit(code=1)

    return config


def _parse_frontmatter(path: Path) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from a Markdown file.

    Returns a ``(frontmatter_dict, body_string)`` tuple. If no valid
    frontmatter is found the dict will be empty and ``body_string`` will
    contain the whole file content.
    """
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    frontmatter_str = parts[1]
    body = parts[2].strip() + "\n"

    try:
        frontmatter: dict = yaml.safe_load(frontmatter_str) or {}
    except yaml.YAMLError as exc:
        logger.warning(f"Failed to parse YAML frontmatter: {exc}")
        return {}, body

    return frontmatter, body


def _title_to_slug(title: str) -> str:
    """Convert a human-readable title to a kebab-case slug.

    Steps:
    - Lowercase
    - Strip non-alphanumeric characters (preserving spaces and hyphens)
    - Replace whitespace/hyphen runs with a single hyphen
    - Strip leading/trailing hyphens
    - Truncate to ``SLUG_MAX_CHARS`` (break on word boundary)
    - Limit to ``SLUG_MAX_WORDS`` hyphen-separated tokens
    """
    slug = title.lower()
    # Keep letters, digits, spaces, and hyphens
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    # Collapse whitespace/hyphen runs into single hyphen
    slug = re.sub(r"[\s-]+", "-", slug)
    # Strip leading/trailing hyphens
    slug = slug.strip("-")

    # Truncate at word boundary
    if len(slug) > SLUG_MAX_CHARS:
        slug = slug[:SLUG_MAX_CHARS].rstrip("-")

    # Limit words
    words = slug.split("-")
    if len(words) > SLUG_MAX_WORDS:
        slug = "-".join(words[:SLUG_MAX_WORDS])

    return slug


def _extract_task_id_from_filename(name: str) -> str:
    """Try to extract a ``task_id`` from a body filename like ``hf-T-042.md``.

    Returns the extracted string, or an empty string if the pattern doesn't
    match.
    """
    m = re.match(r"hf-(.+)\.md$", name, re.IGNORECASE)
    return m.group(1) if m else ""


# ---------------------------------------------------------------------------
# List command — helpers
# ---------------------------------------------------------------------------


@dataclass
class HandoffRecord:
    """A single handoff file with parsed metadata for display/filtering."""

    path: Path
    date: date_type
    time: str
    agent: str
    type: str
    title: str
    task_id: str
    status: str
    priority: str


def _parse_handoff_filename(name: str) -> dict[str, Optional[str]]:
    """Extract metadata from a handoff filename (best-effort).

    Tries three patterns in order:
    1. Canonical: ``YYYY-MM-DD_HHMM_agent_type_slug.md``
    2. Extended:  ``YYYY-MM-DD_agent_type_slug.md``  (no HHMM)
    3. Basic:     ``YYYY-MM-DD_slug.md``

    Returns a dict with keys: ``date``, ``time``, ``agent``, ``type``, ``slug``.
    Missing fields are ``None``.
    """
    m = _CANONICAL_FN_RE.match(name)
    if m:
        return {
            "date": m.group(1),
            "time": m.group(2),
            "agent": m.group(3),
            "type": m.group(4),
            "slug": m.group(5),
        }
    m = _EXTENDED_FN_RE.match(name)
    if m:
        return {
            "date": m.group(1),
            "time": None,
            "agent": m.group(2),
            "type": m.group(3),
            "slug": m.group(4),
        }
    m = _BASIC_FN_RE.match(name)
    if m:
        return {
            "date": m.group(1),
            "time": None,
            "agent": None,
            "type": None,
            "slug": m.group(2),
        }
    return {"date": None, "time": None, "agent": None, "type": None, "slug": None}


def _extract_frontmatter_field(fm: dict, *keys: str) -> Optional[str]:
    """Return the first non-empty string value from *fm* for any of *keys*."""
    for key in keys:
        val = fm.get(key)
        if val and isinstance(val, str):
            return val
    return None


def _filename_date_in_range(
    name: str,
    since_date: Optional[date_type],
    until_date: Optional[date_type],
) -> Optional[bool]:
    """Quick date-range check using the ``YYYY-MM-DD`` prefix of *name*.

    Returns ``None`` when the filename doesn't have a parseable prefix
    (→ file should be included for further frontmatter-based checking).
    """
    m = _DATE_PREFIX_RE.match(name)
    if not m:
        return None
    try:
        file_date = date_type.fromisoformat(m.group(1))
    except ValueError:
        return None
    if since_date and file_date < since_date:
        return False
    if until_date and file_date > until_date:
        return False
    return True


def _get_scan_dirs(
    handoff_root: Path,
    since_date: Optional[date_type],
    until_date: Optional[date_type],
    year: Optional[int],
    month: Optional[int],
    day: Optional[int],
) -> list[tuple[int, int]]:
    """Determine which ``(year, month)`` directories to scan.

    Date resolution order:
    1. ``--since`` / ``--until`` define the range when present.
    2. Otherwise ``--year`` / ``--month`` / ``--day`` with cascading defaults
       (if ``--day`` → infer month + year from today, etc.).
    3. No date filter → scan all existing year/month directories.
    """
    today = date_type.today()

    # Collect existing year directories
    year_dirs: list[int] = []
    try:
        for d in handoff_root.iterdir():
            if d.is_dir() and d.name.isdigit() and len(d.name) == 4:
                year_dirs.append(int(d.name))
    except OSError:
        return []

    year_dirs.sort()
    if not year_dirs:
        return []

    # --since / --until override year/month/day
    if since_date is not None or until_date is not None:
        min_needed = since_date.year if since_date else min(year_dirs)
        max_needed = until_date.year if until_date else max(year_dirs)
        result: list[tuple[int, int]] = []
        for y in year_dirs:
            if y < min_needed or y > max_needed:
                continue
            y_path = handoff_root / str(y)
            months: list[int] = []
            try:
                for d in y_path.iterdir():
                    if d.is_dir() and d.name.isdigit():
                        m_int = int(d.name)
                        if 1 <= m_int <= 12:
                            months.append(m_int)
            except OSError:
                continue
            months.sort()
            for m in months:
                if since_date is not None and y == since_date.year and m < since_date.month:
                    continue
                if until_date is not None and y == until_date.year and m > until_date.month:
                    continue
                result.append((y, m))
        return result

    # No since/until → use year/month/day with cascading defaults
    if day is not None:
        y = year or today.year
        m = month or today.month
        return [(y, m)] if y in year_dirs else []
    if month is not None:
        y = year or today.year
        return [(y, month)] if y in year_dirs else []
    if year is not None:
        if year not in year_dirs:
            return []
        y_path = handoff_root / str(year)
        months = sorted(
            int(d.name)
            for d in y_path.iterdir()
            if d.is_dir() and d.name.isdigit() and 1 <= int(d.name) <= 12
        )
        return [(year, m) for m in months]

    # No date filter → all years and months
    result = []
    for y in year_dirs:
        y_path = handoff_root / str(y)
        months = sorted(
            int(d.name)
            for d in y_path.iterdir()
            if d.is_dir() and d.name.isdigit() and 1 <= int(d.name) <= 12
        )
        for m in months:
            result.append((y, m))
    return result


def _collect_handoffs(
    handoff_root: Path,
    scan_dirs: list[tuple[int, int]],
    project_root: Path,  # noqa: ARG001 — used for relative path resolution if needed
    agent_filter: Optional[str],
    type_filter: Optional[str],
    task_filter: Optional[str],
    search_text: Optional[str],
    since_date: Optional[date_type],
    until_date: Optional[date_type],
) -> list[HandoffRecord]:
    """Walk scan directories, parse files, apply filters, return matches."""
    results: list[HandoffRecord] = []

    for y, m in scan_dirs:
        dir_path = handoff_root / str(y) / f"{m:02d}"
        if not dir_path.is_dir():
            continue

        # List files newest-first (lexicographic reverse on filename)
        try:
            files = sorted(dir_path.glob("*.md"), reverse=True)
        except OSError:
            continue

        for fpath in files:
            fname = fpath.name

            # Skip known non-handoff files
            if fname in ("Registro.md",):
                continue

            # ── Filename-level pre-filters (avoid opening files when possible) ──
            date_check = _filename_date_in_range(fname, since_date, until_date)
            if date_check is False:
                continue

            fn_info = _parse_handoff_filename(fname)
            fn_agent = fn_info.get("agent")
            fn_type = fn_info.get("type")
            fn_date_str = fn_info.get("date")

            if agent_filter and fn_agent and fn_agent != agent_filter:
                continue
            if type_filter and fn_type and fn_type != type_filter:
                continue

            # ── Open file and parse frontmatter ──
            try:
                fm, body = _parse_frontmatter(fpath)
            except Exception:
                logger.warning(f"Failed to read {fpath}")
                continue

            # Extract fields (frontmatter first, filename as fallback)
            rec_date_str = (
                _extract_frontmatter_field(fm, "data", "date") or fn_date_str or ""
            )
            rec_agent = (
                _extract_frontmatter_field(fm, "agent", "mittente", "autore")
                or fn_agent
                or "unknown"
            )
            rec_type = (
                _extract_frontmatter_field(fm, "type", "tipo")
                or fn_type
                or "unknown"
            )
            rec_title = (
                _extract_frontmatter_field(fm, "title", "titolo") or "Untitled"
            )

            # Time from frontmatter ``timestamp`` field or filename
            rec_time: str = fn_info.get("time") or ""
            if not rec_time:
                ts_val = fm.get("timestamp", "")
                if ts_val and isinstance(ts_val, str):
                    tm = re.search(r"T(\d{2}):(\d{2})", ts_val)
                    if tm:
                        rec_time = tm.group(1) + tm.group(2)
                # Fallback: try to extract HHMM from filename via canonical match
                if not rec_time:
                    cm = _CANONICAL_FN_RE.match(fname)
                    if cm:
                        rec_time = cm.group(2)

            # Parse date
            rec_date: date_type
            try:
                rec_date = date_type.fromisoformat(rec_date_str) if rec_date_str else date_type.today()
            except ValueError:
                rec_date = date_type.today()

            # Task ID
            rec_task: str = (
                _extract_frontmatter_field(fm, "task_id", "task") or ""
            )

            # Status & priority (from frontmatter with sensible defaults)
            rec_status: str = (
                _extract_frontmatter_field(fm, "status") or "completed"
            )
            rec_priority: str = (
                _extract_frontmatter_field(fm, "priority") or "medium"
            )

            # ── Full-content filters ──

            # Agent filter (re-check against parsed FM value)
            if agent_filter and rec_agent.lower() != agent_filter.lower():
                continue

            # Type filter
            if type_filter and rec_type.lower() != type_filter.lower():
                continue

            # Task ID filter (substring match)
            if task_filter:
                if not rec_task or task_filter.lower() not in rec_task.lower():
                    continue

            # Date range (re-check against parsed date for accuracy)
            if since_date is not None and rec_date < since_date:
                continue
            if until_date is not None and rec_date > until_date:
                continue

            # Full-text search (case-insensitive in title + body)
            if search_text:
                sl = search_text.lower()
                if sl not in rec_title.lower() and sl not in body.lower():
                    continue

            results.append(
                HandoffRecord(
                    path=fpath,
                    date=rec_date,
                    time=rec_time,
                    agent=rec_agent,
                    type=rec_type,
                    title=rec_title,
                    task_id=rec_task,
                    status=rec_status,
                    priority=rec_priority,
                )
            )

    # Newest first (reverse chronological by date, then time)
    results.sort(key=lambda r: (r.date, r.time or "0000"), reverse=True)
    return results


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------


@app.command(name="list")
def list_handoffs(  # noqa: PLR0913 — function name avoids shadowing built-in list()
    agent: Optional[str] = typer.Option(
        None, "--agent", help="Filter by agent name (lowercase, e.g., efesto, proteo)."
    ),
    year: Optional[int] = typer.Option(
        None, "--year", help="Filter by year (e.g., 2026)."
    ),
    month: Optional[int] = typer.Option(
        None, "--month", help="Filter by month (1-12)."
    ),
    day: Optional[int] = typer.Option(
        None, "--day", help="Filter by day (1-31)."
    ),
    type: Optional[str] = typer.Option(  # noqa: A002
        None, "--type", help="Filter by handoff type (e.g., report, analysis, profile)."
    ),
    task: Optional[str] = typer.Option(
        None, "--task", help="Filter by task_id (e.g., T-042)."
    ),
    search: Optional[str] = typer.Option(
        None,
        "--search",
        help="Text search in title or body content (case-insensitive).",
    ),
    since: Optional[str] = typer.Option(
        None, "--since", help="Start date (inclusive, YYYY-MM-DD)."
    ),
    until: Optional[str] = typer.Option(
        None, "--until", help="End date (inclusive, YYYY-MM-DD)."
    ),
    limit: Optional[int] = typer.Option(
        None, "--limit", help="Maximum number of results to show."
    ),
    paths: bool = typer.Option(
        False,
        "--paths",
        help="Output only relative file paths (one per line), useful for piping.",
    ),
    json: bool = typer.Option(
        False,
        "--json",
        help="Output as JSON array (one object per handoff).",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable DEBUG-level logging to stderr.",
    ),
) -> None:
    """List and filter handoff files from Team/Handoff/YYYY/MM/.

    Supports filtering by agent, date range, type, task_id, and full-text
    search. Results are sorted newest-first. Use ``--paths`` to get a
    pipe-friendly list of relative file paths.
    """
    _setup_logging(verbose)

    # ── Parse date filters ──
    since_date: Optional[date_type] = None
    until_date: Optional[date_type] = None

    if since:
        try:
            since_date = date_type.fromisoformat(since)
        except ValueError:
            logger.error(f"Invalid --since date: '{since}'. Use YYYY-MM-DD format.")
            raise typer.Exit(code=2)

    if until:
        try:
            until_date = date_type.fromisoformat(until)
        except ValueError:
            logger.error(f"Invalid --until date: '{until}'. Use YYYY-MM-DD format.")
            raise typer.Exit(code=2)

    logger.debug(f"Date range: since={since_date}, until={until_date}")
    logger.debug(
        f"Filters: agent={agent}, year={year}, month={month}, day={day}, "
        f"type={type}, task={task}, search={search}"
    )

    # ── Locate project root & load config ──
    try:
        project_root = _find_project_root()
    except FileNotFoundError as e:
        logger.error(str(e))
        raise typer.Exit(code=1)

    try:
        config = _load_config(project_root)
    except typer.Exit:
        raise

    handoff_root = (project_root / config["handoff"]["handoff_root"]).resolve()
    logger.debug(f"Handoff root: {handoff_root}")

    # ── Determine scan directories ──
    scan_dirs = _get_scan_dirs(
        handoff_root, since_date, until_date, year, month, day
    )
    logger.debug(f"Scan directories: {len(scan_dirs)} year/month pairs")

    if not scan_dirs:
        typer.echo("No handoff directories found.")
        raise typer.Exit(code=0)

    # ── Collect & filter ──
    records = _collect_handoffs(
        handoff_root,
        scan_dirs,
        project_root,
        agent_filter=agent,
        type_filter=type,
        task_filter=task,
        search_text=search,
        since_date=since_date,
        until_date=until_date,
    )

    total = len(records)

    if total == 0:
        if json:
            typer.echo("[]")
        else:
            typer.echo("No handoff files match the given filters.")
        raise typer.Exit(code=0)

    # Apply limit
    if limit is not None and limit > 0:
        records = records[:limit]

    # ── Output ──
    if json:
        output_list: list[dict] = []
        for rec in records:
            rel_path = str(rec.path.relative_to(project_root))
            output_list.append(
                {
                    "date": rec.date.isoformat(),
                    "time": rec.time,
                    "agent": rec.agent,
                    "type": rec.type,
                    "title": rec.title,
                    "task_id": rec.task_id,
                    "status": rec.status,
                    "priority": rec.priority,
                    "path": rel_path,
                }
            )
        typer.echo(json_lib.dumps(output_list, indent=2, ensure_ascii=False))
    elif paths:
        for rec in records:
            rel_path = rec.path.relative_to(project_root)
            typer.echo(str(rel_path))
    else:
        console = Console()
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Date", min_width=5)
        table.add_column("Time", min_width=4)
        table.add_column("Agent", no_wrap=True)
        table.add_column("Type", no_wrap=True)
        table.add_column("Title", ratio=2)
        table.add_column("Path", ratio=3)

        for rec in records:
            rel_str = str(rec.path.relative_to(project_root))
            # Rich handles column sizing via ratio;
            # we just pass the raw (possibly long) values.
            table.add_row(
                rec.date.strftime("%m-%d"),
                rec.time or "",
                rec.agent,
                rec.type,
                rec.title,
                rel_str,
            )

        console.print(table)

        if limit is not None and total > limit:
            typer.echo(f"Showing {limit} of {total} results")


@app.command()
def main(
    body: Path = typer.Option(
        ...,
        "--body",
        "-b",
        help="Path to body file (Markdown with YAML frontmatter).",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable DEBUG-level logging to stderr.",
    ),
) -> None:
    """Read a body file, derive metadata, and write a canonical handoff file.

    The body file **must** be a Markdown file with YAML frontmatter containing
    at minimum ``type`` and ``title`` fields. See the module docstring for a
    complete description of the flow.
    """
    _setup_logging(verbose)
    logger.debug(f"Body file argument resolved to: {body}")

    # ------------------------------------------------------------------
    # 1. Locate project root & load config
    # ------------------------------------------------------------------
    try:
        project_root = _find_project_root()
    except FileNotFoundError as e:
        logger.error(str(e))
        raise typer.Exit(code=1)

    logger.debug(f"Project root: {project_root}")

    try:
        config = _load_config(project_root)
    except typer.Exit:
        raise  # already logged

    handoff_root = (project_root / config["handoff"]["handoff_root"]).resolve()
    logger.debug(f"Handoff root: {handoff_root}")

    # ------------------------------------------------------------------
    # 2. Parse body frontmatter
    # ------------------------------------------------------------------
    frontmatter, body_content = _parse_frontmatter(body)

    # Validate required fields
    required_fields = ("type", "title")
    missing = [f for f in required_fields if not frontmatter.get(f)]
    if missing:
        logger.error(
            f"Missing required frontmatter field(s): {', '.join(missing)}"
        )
        raise typer.Exit(code=1)

    hf_type: str = frontmatter["type"]
    title: str = frontmatter["title"]

    # Warn on invalid type but still proceed
    if hf_type not in VALID_TYPES:
        logger.warning(
            f"Type '{hf_type}' is not in the standard set "
            f"{sorted(VALID_TYPES)} — using as-is."
        )

    # Warn on long title (max 60 chars per spec)
    if len(title) > 60:
        logger.warning(f"Title exceeds 60 characters ({len(title)} chars). Truncation may occur in slug.")

    # ------------------------------------------------------------------
    # 3. Derive agent name from the body file's parent folder
    # ------------------------------------------------------------------
    agent = body.parent.name.lower()
    logger.debug(f"Derived agent: '{agent}' from folder: {body.parent.name}")

    # ------------------------------------------------------------------
    # 4. Timestamp
    # ------------------------------------------------------------------
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    timestamp_str = now.strftime("%Y-%m-%dT%H:%M:%S")
    time_str = now.strftime("%H%M")

    # ------------------------------------------------------------------
    # 5. Slug from title
    # ------------------------------------------------------------------
    slug = _title_to_slug(title)
    if not slug:
        logger.error("Slug is empty after processing title — check the title value.")
        raise typer.Exit(code=1)
    logger.debug(f"Slug: '{slug}'")

    # ------------------------------------------------------------------
    # 6. Task ID
    # ------------------------------------------------------------------
    task_id: str = frontmatter.get("task_id", "")
    if not task_id:
        task_id = _extract_task_id_from_filename(body.name)
    if task_id:
        logger.debug(f"Task ID: {task_id}")

    # ------------------------------------------------------------------
    # 7. Output directory
    # ------------------------------------------------------------------
    output_dir = handoff_root / now.strftime("%Y") / now.strftime("%m")
    output_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # 8. Count existing handoffs for this agent → invocation number
    # ------------------------------------------------------------------
    pattern = f"*_{agent}_*.md"
    existing = list(output_dir.glob(pattern))
    agent_handoffs = [f for f in existing if f.is_file()]
    invocation = len(agent_handoffs) + 1
    logger.debug(
        f"Found {len(agent_handoffs)} existing handoffs for "
        f"'{agent}' in {output_dir}; invocation = {invocation}"
    )

    # ------------------------------------------------------------------
    # 9. Build output filename & path
    # ------------------------------------------------------------------
    filename = f"{date_str}_{time_str}_{agent}_{hf_type}_{slug}.md"
    output_path = output_dir / filename

    logger.debug(f"Output filename: {filename}")

    # ------------------------------------------------------------------
    # 10. Build handoff frontmatter
    # ------------------------------------------------------------------
    handoff_fm: dict[str, object] = {
        "data": date_str,
        "timestamp": timestamp_str,
        "agent": agent,
        "invocation": invocation,
        "type": hf_type,
        "status": frontmatter.get("status", "completed"),
        "priority": frontmatter.get("priority", "medium"),
        "title": title,
    }

    if task_id:
        handoff_fm["task_id"] = task_id

    # Carry over any extra frontmatter fields from the body (e.g.
    # next_action, completion_notes, output_refs, deviation, etc.)
    # but never override the derived/direct fields above.
    reserved = {
        "data", "timestamp", "agent", "invocation", "type",
        "status", "priority", "title", "task_id",
    }
    for key, value in frontmatter.items():
        if key not in reserved:
            handoff_fm[key] = value

    # ------------------------------------------------------------------
    # 11. Serialize and write
    # ------------------------------------------------------------------
    yaml_block = yaml.dump(
        handoff_fm,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
    ).strip()

    handoff_content = f"---\n{yaml_block}\n---\n\n{body_content}"
    output_path.write_text(handoff_content, encoding="utf-8")

    logger.info(f"Handoff written: {output_path}")

    # ------------------------------------------------------------------
    # 12. Clean up body file
    # ------------------------------------------------------------------
    try:
        body.unlink()
        logger.debug(f"Body file removed: {body}")
    except OSError as exc:
        logger.error(f"Failed to remove body file {body}: {exc}")

    # ------------------------------------------------------------------
    # 13. Done
    # ------------------------------------------------------------------
    typer.echo(f"Handoff file created: {output_path}")
