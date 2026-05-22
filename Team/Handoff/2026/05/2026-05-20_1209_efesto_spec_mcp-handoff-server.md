---
data: 2026-05-20
timestamp: 2026-05-20T12:09:00
agent: efesto
invocation: 1
type: spec
status: completed
priority: high
title: MCP handoff server + deps/config
task_id: T-042
completion_notes: All four steps completed. Server verified imports and starts correctly.
---

## Summary

Created an MCP server exposing `handoff_create` tool, installed `mcp` dependency, updated `opencode.json`, and added `main.py` for backward compatibility.

## Files created/modified

| File | Size | Lines | Action |
|------|------|-------|--------|
| `tools/handoff/server.py` | 9483 bytes | 275 | Created |
| `tools/handoff/main.py` | 210 bytes | 9 | Created |
| `opencode.json` | 236 bytes | 10 | Modified |
| `pyproject.toml` | — | — | Modified (mcp dep added) |

## Steps completed

1. **`tools/handoff/server.py`** — MCP server using `FastMCP`. Exposes `handoff_create` tool with all required parameters. Writes a temporary body file at `Team/<agent>/hf.md` (or `hf-<task_id>.md`), calls the existing `main()` from `cli.py`, reconstructs the handoff path, returns the relative path. Handles `SystemExit` and exceptions gracefully.

2. **`uv add mcp`** — Succeeded. `mcp==1.27.1` added to `pyproject.toml` dependencies (line 58), locked in `uv.lock`, 12 packages installed.

3. **`opencode.json`** — Updated with MCP section:
   ```json
   "mcp": {
     "handoff": {
       "type": "local",
       "command": ["uv", "run", "python", "-m", "tools.handoff.server"],
       "enabled": true
     }
   }
   ```

4. **`tools/handoff/main.py`** — Created (9 lines). Alias for `__main__.py`, imports `app` from `cli.py` and calls `app()`. Both `python -m tools.handoff` and `python -m tools.handoff.main` work.

## Verification results

- `uv run python -c "import tools.handoff.server"` → imports OK
- `uv run python -m tools.handoff.main --help` → CLI help displays correctly
- `timeout 3 uv run python -m tools.handoff.server` → logs "Starting handoff MCP server on stdio..." and listens (transport: stdio)

## Limits / notes

- The server uses `FastMCP` from the `mcp` SDK. The stdio transport is the default for local MCP servers.
- Temporary body files are created under `Team/<agent>/` and deleted by `main()` after processing.
- The `handoff_create` tool returns a **relative** path string (relative to project root). For absolute path, concatenate with project root.
- All error cases from `main()` (missing config, invalid frontmatter, slug generation failure) are caught and returned as error strings.
- `opencode.json` already references the server; no restart should be needed for OpenCode to pick it up.
