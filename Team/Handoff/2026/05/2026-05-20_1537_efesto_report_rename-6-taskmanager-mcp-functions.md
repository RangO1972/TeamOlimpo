---
data: '2026-05-20'
timestamp: '2026-05-20T15:37:48'
agent: efesto
invocation: 16
type: report
status: completed
priority: high
title: Rename 6 taskmanager MCP functions — remove taskmanager_ prefix
task_id: T-TOOLS-007
---

## Summary

Renamed 6 MCP tool functions in `server.py` to remove the `taskmanager_` prefix, fixing the double namespace issue (MCP server is named `"taskmanager"` so tools appeared as `taskmanager_taskmanager_task_*` in OpenCode).

## Changes

### File: `tools/taskmanager/server.py`

| Old name | New name |
|---|---|
| `taskmanager_task_create` | `task_create` |
| `taskmanager_task_update_status` | `task_update_status` |
| `taskmanager_task_query` | `task_query` |
| `taskmanager_task_summary` | `task_summary` |
| `taskmanager_task_log_event` | `task_log_event` |
| `taskmanager_task_export` | `task_export` |

Updated in all locations:
- Function definitions (`def` + `@mcp.tool()`)
- Comment headers (`# Tool N: ...`)
- Module docstring (lines 1-19, both description and tools table)
- `logger.info` / `logger.debug` string messages
- `# ---------------------------------------------------------------------------` section separators preserved

### File: `tools/taskmanager/__init__.py`
- Docstring listing of the 6 tools updated to new names

### Not changed (per instructions)
- `FastMCP("taskmanager")` server name (line ~55) — unchanged
- Function parameters, logic, internal behavior — untouched
- Documentation files (agent profiles, handoff records, wiki) — out of scope

## Verification

- `grep 'taskmanager_task_' tools/taskmanager/` → **0 matches** (code fully clean)
- `uv run python -m tools.taskmanager.server` → starts cleanly, logs:
  ```
  Starting taskmanager MCP server on stdio...
  State loaded from .../state.yaml (265 tasks)
  ```
- Exits gracefully on SIGTERM (exit 0)

## Operational Notes

The 69 remaining `taskmanager_task_*` references in documentation files (`hermes.md`, handoff records, wiki) do not affect functionality — the MCP client resolves tools by the function name registered with `@mcp.tool()`, which is now `task_*`. These docs can be updated separately if desired.

## Dependencies
No changes — existing `pyproject.toml` remains valid.
