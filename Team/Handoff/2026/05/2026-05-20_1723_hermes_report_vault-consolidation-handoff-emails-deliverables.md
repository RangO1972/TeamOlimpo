---
data: '2026-05-20'
timestamp: '2026-05-20T17:23:08'
agent: hermes
invocation: 6
type: report
status: completed
priority: medium
title: 'Vault consolidation: Handoff, emails, deliverables moved into Library/'
task_id: T-CONSOLIDAR-001
---

## Summary

Consolidated three external directories into the Library/ Obsidian vault to enable wikilinks across all content.

## Moves executed

| Old path | New path | Files |
|----------|----------|-------|
| `Team/Handoff/` | `Library/Handoff/` | 342 handoff files |
| `vaults/email/` | `Library/emails/` | 2025 email notes |
| `Owner's Inbox/` | `Library/deliverables/` | 95 deliverables |

## Config & tool updates

- `tools/config.yaml` — Updated `handoff_root`, `vault_root`, added `search_paths` for all new dirs
- 9 Python tools updated (config.py constants in kba indexer/merger/reporter + gen_fermata, automation_video_ia, preflight_check)
- AGENTS.md, 3 agent profiles (efesto, metis, euterpe), Hermes scratchpad
- ~200 .md references batch-updated across Library/Meta/, Prompts/, paper/, projects/

## Wiki fixes

- Fixed wikilink in `agent-qualification-framework.md`: `[[Team/Handoff/...]]` -> `[[Handoff/...]]`

## Obsidian config

- `Library/.obsidian/app.json` set to exclude `Handoff/Legacy`, `emails/Inbox`, `emails/_review`
- Removed nested `.obsidian/` from `Library/emails/` (leftover from former separate vault)

## Verification

- `handoff list --limit 3` -> OK, shows correct `Library/Handoff/...` paths
- Knowledge base search -> OK
- Zero old references to `Owner's Inbox`, `Team/Handoff`, `vaults/email` remain
- `Team/Inbox/` left untouched (raw input folder, 45 MB)
