"""MCP server: expose ``handoff_create`` and ``handoff_list`` tools for
Team Olimpo handoff management.

Usage
-----
    uv run python -m tools.handoff.server

The server listens on stdio (MCP stdio transport). An MCP client (e.g.
opencode.json's ``mcp`` section) connects to it and calls the
``handoff_create`` and ``handoff_list`` tools.
"""

from __future__ import annotations

import contextlib
import io
import json as json_lib
import re
import sys
from datetime import date as date_type
from datetime import datetime
from pathlib import Path
from typing import Optional

import yaml
from loguru import logger

from tools.handoff.cli import (
    _collect_handoffs,
    _find_project_root,
    _get_scan_dirs,
    _title_to_slug,
    main as handoff_main,
)

# ---------------------------------------------------------------------------
# MCP SDK — optional; server reports a clear error if missing
# ---------------------------------------------------------------------------

try:
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("handoff")
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Config path relative to project root
_CONFIG_PATH = Path("tools") / "config.yaml"


def _get_handoff_root(project_root: Path) -> Path:
    """Read ``handoff_root`` from ``tools/config.yaml``.

    Raises ``RuntimeError`` if the config is missing or malformed.
    """
    config_file = project_root / _CONFIG_PATH
    if not config_file.is_file():
        raise RuntimeError(f"Config file not found: {config_file}")

    try:
        raw = config_file.read_text(encoding="utf-8")
        config: dict = yaml.safe_load(raw) or {}
    except Exception as exc:
        raise RuntimeError(f"Failed to parse {config_file}: {exc}") from exc

    handoff_cfg = config.get("handoff")
    if not isinstance(handoff_cfg, dict):
        raise RuntimeError("Missing 'handoff' section in tools/config.yaml")

    handoff_rel = handoff_cfg.get("handoff_root")
    if not handoff_rel:
        raise RuntimeError("Missing 'handoff_root' in tools/config.yaml [handoff]")

    return project_root / handoff_rel


def _reconstruct_handoff_path(
    project_root: Path, agent: str, hf_type: str, title: str
) -> Path:
    """Reconstruct the handoff file path that ``main()`` will produce.

    The derivation mirrors the identical logic inside ``cli.main()`` so the
    caller can verify the output file exists without parsing ``typer.echo``.
    """
    handoff_root = _get_handoff_root(project_root)
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H%M")
    slug = _title_to_slug(title)
    output_dir = handoff_root / now.strftime("%Y") / now.strftime("%m")
    filename = f"{date_str}_{time_str}_{agent}_{hf_type}_{slug}.md"
    return output_dir / filename


# ---------------------------------------------------------------------------
# Tool
# ---------------------------------------------------------------------------


@mcp.tool()
def create(
    type: str,
    title: str,
    body: str,
    agent: str,
    task_id: Optional[str] = None,
    completion_notes: Optional[str] = None,
    status: Optional[str] = "completed",
    priority: Optional[str] = "medium",
    output_refs: Optional[str] = None,
    deviation: Optional[str] = None,
) -> str:
    """Create a Team Olimpo handoff file.

    Builds a temporary body file with YAML frontmatter, delegates to the
    existing handoff CLI (``tools.handoff.cli.main``), and returns the
    **relative** path of the newly created handoff file (e.g.
    ``Library/Handoff/2026/05/2026-05-20_1430_efesto_report_my-slug.md``).

    Parameters
    ----------
    type : str
        Handoff type: ``report``, ``analysis``, ``profile``, ``spec``,
        ``test``, ``note``, ``bug``, ``feedback``.
    title : str
        Human-readable title (max 60 characters recommended).
    body : str
        Markdown body content.
    agent : str
        Agent name (lowercase, e.g. ``efesto``, ``proteo``).
    task_id : str | None
        Optional task identifier (e.g. ``T-042``).
    completion_notes : str | None
        Optional completion notes.
    status : str | None
        Status (default ``"completed"``).
    priority : str | None
        Priority (default ``"medium"``).
    output_refs : str | None
        Optional output references file.
    deviation : str | None
        Optional deviation block (JSON or YAML inline string).
    """
    # ------------------------------------------------------------------
    # 1. Validate required parameters
    # ------------------------------------------------------------------
    if not type or not title or not body or not agent:
        return (
            "Error: 'type', 'title', 'body', and 'agent' are required parameters."
        )

    if len(title) > 60:
        logger.warning(f"Title exceeds 60 characters ({len(title)} chars).")

    # ------------------------------------------------------------------
    # 2. Build YAML frontmatter dict
    # ------------------------------------------------------------------
    frontmatter: dict[str, object] = {
        "type": type,
        "title": title,
    }

    if task_id:
        frontmatter["task_id"] = task_id
    if completion_notes:
        frontmatter["completion_notes"] = completion_notes
    if status:
        frontmatter["status"] = status
    if priority:
        frontmatter["priority"] = priority
    if output_refs:
        frontmatter["output_refs"] = output_refs
    if deviation:
        frontmatter["deviation"] = deviation

    # ------------------------------------------------------------------
    # 3. Locate project root
    # ------------------------------------------------------------------
    try:
        project_root = _find_project_root()
    except FileNotFoundError as e:
        logger.error(f"Project root not found: {e}")
        return f"Error: {e}"

    # ------------------------------------------------------------------
    # 4. Write temporary body file at Team/<agent>/hf.md
    # ------------------------------------------------------------------
    agent_dir = project_root / "Team" / agent
    agent_dir.mkdir(parents=True, exist_ok=True)

    # When task_id is present, embed it in the filename so the existing
    # _extract_task_id_from_filename helper can pick it up.
    body_filename = f"hf-{task_id}.md" if task_id else "hf.md"
    body_path = agent_dir / body_filename

    yaml_block = yaml.dump(
        frontmatter,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
    ).strip()
    file_content = f"---\n{yaml_block}\n---\n\n{body}"
    body_path.write_text(file_content, encoding="utf-8")
    logger.debug(f"Body file written: {body_path}")

    # ------------------------------------------------------------------
    # 5. Pre-compute the expected handoff path (before main() deletes body)
    # ------------------------------------------------------------------
    try:
        handoff_path = _reconstruct_handoff_path(
            project_root, agent, type, title
        )
    except RuntimeError as e:
        logger.error(str(e))
        return f"Error: {e}"

    # ------------------------------------------------------------------
    # 6. Delegate to the existing main() function
    # ------------------------------------------------------------------
    logger.debug(f"Delegating to main() with body={body_path}")
    try:
        # Suppress stdout/stderr from main() (it calls typer.echo).
        # We capture stderr only for error detection.
        stderr_capture = io.StringIO()
        with (
            contextlib.redirect_stdout(io.StringIO()),
            contextlib.redirect_stderr(stderr_capture),
        ):
            handoff_main(body=body_path, verbose=False)
        stderr_text = stderr_capture.getvalue()
        if stderr_text:
            logger.debug(f"main() stderr output: {stderr_text.strip()}")
    except SystemExit as e:
        if e.code != 0:
            logger.error(f"Handoff creation failed (exit code {e.code})")
            return f"Error: handoff creation failed (exit code {e.code})"
    except Exception as e:
        logger.error(f"Unexpected exception from main(): {e}")
        return f"Error: unexpected error — {e}"

    # ------------------------------------------------------------------
    # 7. Verify the handoff file exists and return its relative path
    # ------------------------------------------------------------------
    if not handoff_path.is_file():
        logger.error(f"Expected handoff file not found: {handoff_path}")
        return (
            f"Error: handoff file was not created at the expected path "
            f"({handoff_path}). The CLI may have failed silently."
        )

    relative_path = handoff_path.relative_to(project_root)
    logger.info(f"Handoff created: {relative_path}")
    return str(relative_path)


# ---------------------------------------------------------------------------
# Tool — list
# ---------------------------------------------------------------------------


@mcp.tool()
def list(  # noqa: A001
    agent: Optional[str] = None,
    type: Optional[str] = None,  # noqa: A002
    task_id: Optional[str] = None,
    search: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
    limit: Optional[int] = None,
    paths: bool = False,
    json_output: bool = False,
    year: Optional[int] = None,
    month: Optional[int] = None,
    day: Optional[int] = None,
) -> str:
    """List and filter existing Team Olimpo handoff files.

    Searches the handoff archive (Library/Handoff/YYYY/MM/) for handoff files
    matching the given filters. Results are sorted newest-first.

    Parameters
    ----------
    agent : str | None
        Filter by agent name (lowercase, e.g. ``efesto``, ``proteo``).
    type : str | None
        Filter by handoff type (e.g. ``report``, ``analysis``, ``profile``).
    task_id : str | None
        Filter by task identifier (e.g. ``T-042``).
    search : str | None
        Text search in title or body content (case-insensitive).
    since : str | None
        Start date (inclusive, YYYY-MM-DD).
    until : str | None
        End date (inclusive, YYYY-MM-DD).
    limit : int | None
        Maximum number of results to return.
    paths : bool
        If ``True``, output only relative file paths (one per line).
    json_output : bool
        If ``True``, output as a JSON array of objects.
    year : int | None
        Filter by year (e.g. 2026).
    month : int | None
        Filter by month (1-12).
    day : int | None
        Filter by day (1-31).
    """
    # ------------------------------------------------------------------
    # 1. Parse optional date filters
    # ------------------------------------------------------------------
    since_date: Optional[date_type] = None
    until_date: Optional[date_type] = None

    if since:
        try:
            since_date = date_type.fromisoformat(since)
        except ValueError:
            return f"Error: invalid --since date: '{since}'. Use YYYY-MM-DD format."

    if until:
        try:
            until_date = date_type.fromisoformat(until)
        except ValueError:
            return f"Error: invalid --until date: '{until}'. Use YYYY-MM-DD format."

    # ------------------------------------------------------------------
    # 2. Locate project root
    # ------------------------------------------------------------------
    try:
        project_root = _find_project_root()
    except FileNotFoundError as e:
        logger.error(f"Project root not found: {e}")
        return f"Error: {e}"

    # ------------------------------------------------------------------
    # 3. Load config and resolve handoff root
    # ------------------------------------------------------------------
    try:
        handoff_root = _get_handoff_root(project_root)
    except RuntimeError as e:
        logger.error(str(e))
        return f"Error: {e}"

    # ------------------------------------------------------------------
    # 4. Determine which year/month directories to scan
    # ------------------------------------------------------------------
    scan_dirs = _get_scan_dirs(
        handoff_root, since_date, until_date, year, month, day
    )

    if not scan_dirs:
        return "[]" if json_output else "No handoff directories found."

    # ------------------------------------------------------------------
    # 5. Collect and filter handoff records
    # ------------------------------------------------------------------
    records = _collect_handoffs(
        handoff_root,
        scan_dirs,
        project_root,
        agent_filter=agent if agent else None,
        type_filter=type if type else None,
        task_filter=task_id if task_id else None,
        search_text=search if search else None,
        since_date=since_date,
        until_date=until_date,
    )

    total = len(records)

    if total == 0:
        return "[]" if json_output else "No handoff files match the given filters."

    # Apply limit
    if limit is not None and limit > 0:
        records = records[:limit]

    # ------------------------------------------------------------------
    # 6. Format output
    # ------------------------------------------------------------------
    if json_output:
        output_list: list[dict[str, object]] = []
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
        return json_lib.dumps(output_list, indent=2, ensure_ascii=False)

    if paths:
        lines: list[str] = []
        for rec in records:
            lines.append(str(rec.path.relative_to(project_root)))
        return "\n".join(lines)

    # Default: human-readable text table
    lines = ["Date       Time   Agent       Type        Title                                              Path"]
    lines.append("-" * 120)
    for rec in records:
        rel_str = str(rec.path.relative_to(project_root))
        lines.append(
            f"{rec.date.isoformat()} {rec.time or '----'}  "
            f"{rec.agent:<10} {rec.type:<10} "
            f"{rec.title[:55]:<55} {rel_str}"
        )
    result = "\n".join(lines)
    if limit is not None and total > len(records):
        result += f"\n\nShowing {len(records)} of {total} results"
    return result


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main_server() -> None:
    """Start the MCP server on stdio transport."""
    if not MCP_AVAILABLE:
        logger.error(
            "MCP SDK not installed. Run: uv add mcp"
        )
        sys.exit(1)

    logger.info("Starting handoff MCP server on stdio...")
    mcp.run()


if __name__ == "__main__":
    main_server()
