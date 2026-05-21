"""MCP server: expose ``kb_search`` (tool) and ``kb_read`` (Resource) for
the Team Olimpo Knowledge Base.

The server provides read-only access to ``Library/Wiki/`` and
``Library/documents/`` via:

- **``kb_search``** — grep-based search across the knowledge base,
  returning structured JSON results with snippet and frontmatter.
- **``kb_read``** — MCP Resource with URI scheme ``wiki://{path}`` that
  returns the full Markdown content of a page.

Usage
-----
    uv run python -m tools.knowledge_base.server

Registrazione in opencode.json::

    "knowledge_base": {
      "type": "local",
      "command": ["uv", "run", "python", "-m", "tools.knowledge_base.server"],
      "enabled": true
    }
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from loguru import logger

from tools.knowledge_base.grep_engine import (
    MAX_CONTEXT_LINES,
    MAX_RESULTS_LIMIT,
    VALID_SCOPES,
    clear_caches,
    get_grep_engine,
    parse_search_output,
    resolve_search_paths,
    run_grep,
    DEFAULT_CONTEXT_LINES,
    DEFAULT_MAX_RESULTS,
    DEFAULT_TIMEOUT,
    MAX_QUERY_LENGTH,
)

# ---------------------------------------------------------------------------
# MCP SDK — graceful fallback if missing
# ---------------------------------------------------------------------------

try:
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("knowledge_base")
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False

# ---------------------------------------------------------------------------
# Project root & config
# ---------------------------------------------------------------------------

_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

_config: dict[str, Any] | None = None


def _load_config() -> dict[str, Any]:
    """Load ``tools/config.yaml`` and cache it."""
    global _config
    if _config is not None:
        return _config

    config_path = _PROJECT_ROOT / "tools" / "config.yaml"
    if not config_path.exists():
        logger.warning("tools/config.yaml not found — using defaults")
        _config = {}
        return _config

    try:
        with open(config_path, "r") as f:
            _config = yaml.safe_load(f) or {}
    except Exception as exc:
        logger.error(f"Failed to parse tools/config.yaml: {exc}")
        _config = {}
    return _config


def _get_kb_config() -> dict[str, Any]:
    """Return the ``knowledge_base`` section from config."""
    cfg = _load_config()
    return cfg.get("knowledge_base", {})


# ---------------------------------------------------------------------------
# Resource base helpers
# ---------------------------------------------------------------------------

_LIBRARY_BASE = _PROJECT_ROOT / "Library"


def _resolve_and_read(library_rel: str, page_path_orig: str = "") -> str:
    """Resolve a path relative to ``Library/`` and return its content.

    Steps:

    1. Security — path traversal guard (must stay under ``Library/``).
    2. If the target is a ``.md`` file, return its content.
    3. If the target is a directory, return a listing of ``*.md`` files.
    4. Otherwise → ``Resource not found``.

    Parameters
    ----------
    library_rel : str
        Path relative to ``Library/`` (e.g. ``"Wiki/index"`` or
        ``"documents/some-doc.md"``).
    page_path_orig : str
        Original URI path for error messages.
    """
    # ---- Security: path traversal guard ----
    candidate = (_LIBRARY_BASE / library_rel).resolve()
    if not str(candidate).startswith(str(_LIBRARY_BASE.resolve())):
        logger.warning(f"Path traversal blocked: {library_rel} → {candidate}")
        return "Error: Path traversal blocked."

    # ---- Try exact path (if already has an extension) ----
    if library_rel.endswith(".md") and candidate.is_file():
        try:
            return candidate.read_text(encoding="utf-8")
        except OSError as e:
            logger.error(f"Failed to read {candidate}: {e}")
            return f"Error: Failed to read file — {e}"

    # ---- Try with .md appended ----
    md_candidate = (_LIBRARY_BASE / f"{library_rel}.md").resolve()
    if str(md_candidate).startswith(str(_LIBRARY_BASE.resolve())) and md_candidate.is_file():
        try:
            return md_candidate.read_text(encoding="utf-8")
        except OSError as e:
            logger.error(f"Failed to read {md_candidate}: {e}")
            return f"Error: Failed to read file — {e}"

    # ---- Try as directory ----
    if candidate.is_dir():
        md_files = sorted(candidate.glob("*.md"))
        if not md_files:
            return f"# Directory: {library_rel}\n\n*(empty)*"
        listing_lines = "\n".join(
            str(f.relative_to(candidate)) for f in md_files
        )
        return f"# Directory: {library_rel}\n\n{listing_lines}"

    # ---- Not found ----
    uri_path = page_path_orig or library_rel
    return f"Resource not found: wiki://{uri_path}"


def _read_wiki_page(page_name: str) -> str:
    """Read a page under ``Library/Wiki/``, optionally with ``.md``."""
    return _resolve_and_read(f"Wiki/{page_name}", page_name)


def _read_document(doc_name: str) -> str:
    """Read a document under ``Library/documents/``."""
    return _resolve_and_read(f"documents/{doc_name}", f"documents/{doc_name}")


# ---------------------------------------------------------------------------
# MCP Tool: kb_search
# ---------------------------------------------------------------------------


@mcp.tool()
def kb_search(
    query: str,
    scope: str = "wiki+docs",
    max_results: int = DEFAULT_MAX_RESULTS,
    context_lines: int = DEFAULT_CONTEXT_LINES,
    no_frontmatter: bool = False,
) -> str:
    """Cerca nella knowledge base usando grep.

    Esegue grep (o ripgrep, se disponibile) su Library/Wiki/ e Library/documents/.
    Ritorna risultati strutturati con path, linea, snippet e frontmatter parsato.

    Parameters
    ----------
    query : str
        Termine di ricerca. Plain text — grep cerca la stringa letterale.
        Per regex, usare caratteri regex validi per grep -E.
    scope : str
        Ambito della ricerca:
        - ``"wiki"`` → solo Library/Wiki/
        - ``"docs"`` → solo Library/documents/
        - ``"wiki+docs"`` → Wiki + Documents (default)
        - ``"all"`` → Library/ completa
    max_results : int
        Numero massimo di risultati (default 15, max 50).
    context_lines : int
        Righe di contesto prima e dopo ogni match (default 3).
        Usare 0 per solo la riga matchata.
    no_frontmatter : bool
        Se True, filtra i match che cadono dentro il blocco YAML frontmatter
        (tra i delimiter ``---``). Default False.

    Returns
    -------
    str
        JSON array di risultati. Ogni risultato ha:
        - path: path relativo del file
        - line: numero di riga del match
        - snippet: testo del match con contesto
        - frontmatter: dict con title, date, tags (se presenti)

    Edge cases
    ----------
    - query vuota → ``{"error": "Query parameter is required."}``
    - scope non valido → ``{"error": "Invalid scope. ..."}``
    - nessun match → ``[]``
    - timeout (10s) → ``{"error": "Search timed out after 10s."}``
    """
    # ---- Validate query ----
    if not query or not query.strip():
        return json.dumps({"error": "Query parameter is required."})

    # Truncate overly long queries
    if len(query) > MAX_QUERY_LENGTH:
        logger.warning(f"Query truncated from {len(query)} to {MAX_QUERY_LENGTH} chars")
        query = query[:MAX_QUERY_LENGTH]

    # ---- Validate scope ----
    if scope not in VALID_SCOPES:
        return json.dumps({
            "error": f"Invalid scope '{scope}'. "
            f"Use one of: {', '.join(sorted(VALID_SCOPES))}."
        })

    # ---- Clamp parameters ----
    if max_results > MAX_RESULTS_LIMIT:
        logger.warning(f"max_results clamped from {max_results} to {MAX_RESULTS_LIMIT}")
        max_results = MAX_RESULTS_LIMIT
    if max_results < 1:
        max_results = 1
    if context_lines > MAX_CONTEXT_LINES:
        logger.warning(
            f"context_lines clamped from {context_lines} to {MAX_CONTEXT_LINES}"
        )
        context_lines = MAX_CONTEXT_LINES
    if context_lines < 0:
        context_lines = 0

    # ---- Resolve paths ----
    try:
        search_paths = resolve_search_paths(_PROJECT_ROOT, scope)
    except ValueError as e:
        return json.dumps({"error": str(e)})

    if not search_paths:
        return json.dumps({"error": "No valid search paths found for the given scope."})

    # ---- Get grep engine ----
    try:
        engine_name, engine_path = get_grep_engine()
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

    # ---- Read timeout from config ----
    kb_cfg = _get_kb_config()
    timeout = kb_cfg.get("timeout", DEFAULT_TIMEOUT)

    # ---- Config defaults override (if config explicitly set) ----
    cfg_defaults = kb_cfg.get("defaults", {})
    if max_results == DEFAULT_MAX_RESULTS and cfg_defaults.get("max_results") is not None:
        pass  # user could have passed explicit, don't override
    # (the config defaults are for the tool defaults, but the user can still
    #  override them via explicit parameters — handled by Python's default args)

    logger.info(
        f"kb_search called: query='{query[:80]}', "
        f"scope={scope}, max_results={max_results}, "
        f"context_lines={context_lines}, no_frontmatter={no_frontmatter}, "
        f"engine={engine_name}"
    )

    # Clear caches between searches to avoid stale frontmatter
    clear_caches()

    # ---- Run grep ----
    try:
        raw_output = run_grep(
            query, search_paths, engine_path, engine_name, _PROJECT_ROOT, timeout
        )
    except TimeoutError as e:
        logger.error(f"Search timed out: {e}")
        return json.dumps({"error": str(e)})
    except RuntimeError as e:
        logger.error(f"Search failed: {e}")
        return json.dumps({"error": str(e)})
    except ValueError as e:
        return json.dumps({"error": str(e)})

    # ---- Parse output ----
    try:
        return parse_search_output(
            raw_output,
            _PROJECT_ROOT,
            max_results,
            context_lines,
            no_frontmatter,
        )
    except Exception as e:
        logger.exception("Failed to parse grep output")
        return json.dumps({"error": f"Failed to parse results: {e}"})


# ---------------------------------------------------------------------------
# MCP Resources: kb_read (wiki:// URI scheme)
#
# Multiple templates are needed because the MCP SDK (v1.27.1) uses
# ``{param}`` → ``(?P<param>[^/]+)`` which only captures single path
# segments.  We register templates at the depths we know exist.
# ---------------------------------------------------------------------------


@mcp.resource("wiki://")
def kb_read_root() -> str:
    """Legge la pagina index della knowledge base.

    ``wiki://`` → ``Library/Wiki/index.md``
    """
    return _read_wiki_page("index")


@mcp.resource("wiki://{page_name}")
def kb_read_page(page_name: str) -> str:
    """Legge una pagina wiki di primo livello.

    URI esempi::

        wiki://index        → Library/Wiki/index.md
        wiki://log          → Library/Wiki/log.md
    """
    return _read_wiki_page(page_name)


@mcp.resource("wiki://documents/{doc_name}")
def kb_read_document(doc_name: str) -> str:
    """Legge un documento da Library/documents/.

    URI esempi::

        wiki://documents/mcp-roadmap-pythagoras-research-report
        wiki://documents/knowledge-retrieval-patterns-grep-first-mcp
        wiki://documents/                          → directory listing
    """
    return _read_document(doc_name)


@mcp.resource("wiki://concepts/{year}/{month}/{slug}")
def kb_read_concept(year: str, month: str, slug: str) -> str:
    """Legge una concept page da ``Library/Wiki/concepts/{year}/{month}/``.

    URI esempio::

        wiki://concepts/2026/05/kb-mcp-design
    """
    return _read_wiki_page(f"concepts/{year}/{month}/{slug}")


@mcp.resource("wiki://decisions/{year}/{month}/{slug}")
def kb_read_decision(year: str, month: str, slug: str) -> str:
    """Legge una decision page da ``Library/Wiki/decisions/{year}/{month}/``."""
    return _read_wiki_page(f"decisions/{year}/{month}/{slug}")


@mcp.resource("wiki://research/{year}/{month}/{slug}")
def kb_read_research(year: str, month: str, slug: str) -> str:
    """Legge una research page da ``Library/Wiki/research/{year}/{month}/``."""
    return _read_wiki_page(f"research/{year}/{month}/{slug}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main_server() -> None:
    """Start the knowledge_base MCP server on stdio transport."""
    if not MCP_AVAILABLE:
        logger.error("MCP SDK not installed. Run: uv add mcp")
        raise SystemExit(1)

    # Warm up: check grep engine availability
    try:
        engine_name, engine_path = get_grep_engine()
        logger.info(f"Grep engine detected: {engine_name} ({engine_path})")
    except RuntimeError as e:
        logger.error(f"No grep engine available: {e}")
        raise SystemExit(1)

    # Log config
    kb_cfg = _get_kb_config()
    search_paths = kb_cfg.get("search_paths", ["Library/Wiki/", "Library/documents/"])
    timeout = kb_cfg.get("timeout", DEFAULT_TIMEOUT)
    defaults = kb_cfg.get("defaults", {})
    logger.info(
        f"Knowledge base config: paths={search_paths}, "
        f"timeout={timeout}s, defaults={defaults}"
    )

    logger.info("Starting knowledge_base MCP server on stdio...")
    mcp.run()


if __name__ == "__main__":
    main_server()
