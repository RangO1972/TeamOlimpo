---
data: '2026-05-20'
timestamp: '2026-05-20T10:19:11'
agent: efesto
invocation: 12
type: report
status: completed
priority: high
title: Handoff tool — list subcommand implemented
task_id: T-LIST-001
completion_notes: 'Added ''list'' subcommand to tools/handoff/ with 12 filter options:
  --agent, --year, --month, --day, --type, --task, --search, --since, --until, --limit,
  --paths, --verbose. Implements two output modes: rich.Table (default) and --paths
  for piping. Filtering uses two-pass approach: filename pre-filter then frontmatter
  check. Handles both canonical (English frontmatter) and legacy (Italian keys) files.

  '
output_refs:
- tools/handoff/cli.py
- tools/handoff/__init__.py
next_action: Ready for team-wide use. Hermes can query handoffs via `uv run python
  -m tools.handoff list`.
quality_score: 5
---

Added the `list` subcommand to the handoff tool with filtering by agent, date range, type, task_id, and full-text search.
