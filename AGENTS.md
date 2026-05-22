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
| `tools/` | Python tools (handoff, taskmanager, knowledge_base, email_processor, pdf_converter) |
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
