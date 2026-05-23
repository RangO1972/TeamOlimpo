# AGENTS.md - Team Olimpo

This file provides guidance for OpenCode when working with the code in this repository.

## What is this repository

PKM (Personal Knowledge Management) of **Team Olimpo** — an AI agent system with Greek mythological identities. This is not a traditional codebase: it is a Markdown knowledge base defining roles, profiles, and operational workflows for the team.

## Team Olimpo Architecture

The system operates on an **orchestrator-workers** pattern: Hermes routes every request to the best-suited agent using a fixed routing table (IntentGate).

Flow to create a new agent: Hermes → Proteo (domain analysis) → Hermes → Atena (persona construction) → metadata integration in `.opencode/agents/<name>.md`.

## PUBLIC/PRIVATE Split

This repo has two tiers:

- **PUBLIC** (`TeamOlimpo/` → GitHub): templates, skills, configs, tool code, SOPs
- **PRIVATE** (`Library/` → symlink → local git, no remote): all sensitive data — handoff diaries, system state, wiki, emails, deliverables

`Library/` is gitignored from this repo. It's a symlink to a separate local git repository that never pushes to GitHub.

## Folder Structure — PUBLIC

| Path | Content |
|------|---------|
| `.opencode/agents/` | Agent system prompt files (OpenCode format) |
| `Team/Members/` | Identity files (SOUL.md) for team agents |
| `Team/SOPs/` | Standard operating procedures |
| `Team/Meta/` | System documentation, tool guides, conventions |
| `Team/Prompts/` | Prompt library |
| `Team/Fucina/` | Team working files (gitignored — cloned repos, temp analyses, KBA working data) |
| `Inbox/` | User PDFs waiting for conversion |
| `tools/` | Python tools (handoff, taskmanager, knowledge_base, email_processor, pdf_converter, session_memory) |
| `scripts/` | Utility scripts |
| `opencode.json` | Main OpenCode agent configuration |
| `AGENTS.md` | This file |

## Folder Structure — PRIVATE (`Library/`)

| Path | Content |
|------|---------|
| `Handoff/YYYY/MM/` | Agent output handoff files. Every worker invocation writes one file here. Includes `type: spec` and `type: plan`. See `Team/SOPs/handoff-guide.md` for full spec. |
| `System/Hermes/` | Hermes scratchpad and operational state (`state.yaml`, scratchpad `.md` files). Task manager state is here. |
| `Quarantine/` | Files put aside for review or recovery |
| `documents/` | Markdown files converted from PDFs |
| `assets/images/` | Images extracted from PDFs, organized by document slug |
| `data/` | SQLite databases, converter logs, KBA catalog |
| `Wiki/` | **Team Olimpo Knowledge Wiki** (LLM Wiki pattern). Concepts, decisions, research. Chronological `YYYY/MM/`. |
| `emails/` | Email vault |
| `deliverables/` | Final outputs destined for the user |

## Conventions

- Each agent profile in `.opencode/agents/` uses standard OpenCode frontmatter
- Agent names are Greek mythological figures

## Handoff Protocol

Every worker agent invocation **must** end by writing one handoff file before returning control to Hermes. **No exceptions. Applies to all agents except Hermes (orchestrator).**

Full specification: `Team/SOPs/handoff-guide.md`

## Using TeamOlimpo with Claude Code

This repository is compatible with **both OpenCode and Claude Code**.

### Architecture Differences

- **OpenCode**: Hermes is primary agent; routing is automatic via `mode: primary`
- **Claude Code**: All custom agents are subagents; routing must be manual (via `@` mention)

### How to Use with Claude Code

Claude Code starts with **Hermes as the main agent** (configured in `.claude/settings.json`). Hermes automatically:
1. Receives all your requests
2. Routes them to the best specialist (Atena for design, Efesto for Python, Proteo for research, etc.)
3. Tracks state and synthesizes results

**MCP servers** are configured in `.mcp.json` (project scope, shared with team) and auto-connect to all 5 backend services (handoff, email_processor, taskmanager, knowledge_base, session_memory)

### Generated Artifacts

Agent files are auto-generated from OpenCode sources:
- **Source**: `.opencode/agents/*.md` (canonical, edit these)
- **Generated**: `.claude/agents/*.md` (auto-synced, do not edit manually)
- **Sync script**: `tools/sync_agents.py` — run after modifying any OpenCode agent file

To sync after agent edits:
```bash
uv run python tools/sync_agents.py
```

### Testing MCP Servers

Inside Claude Code, run:
```
/mcp
```

Shows connection status and tool count per server. If a server shows "disconnected", debug by running:
```bash
uv run python -m tools.session_memory.server  # example
```

Check stderr for errors.

### Limitations

- Claude Code does not support the automatic `mode: primary` routing that OpenCode provides — you must invoke `@hermes` explicitly
- Permission rules are less granular in Claude Code; the sync script does a best-effort conversion
- `opencode/big-pickle` model is mapped to `sonnet` in Claude Code
- MCP configuration **must** be in `.mcp.json` (not `.claude/settings.json`), which is committed to git and shared
