# AGENTS.md - Team Olimpo

This file provides guidance for OpenCode when working with the code in this repository.

## What is this repository

PKM (Personal Knowledge Management) of **Team Olimpo** — an AI agent system with Greek mythological identities. This is not a traditional codebase: it is a Markdown knowledge base defining roles, profiles, and operational workflows for the team.

## Team Olimpo Architecture

The system operates on an **orchestrator-workers** pattern: Hermes routes every request to the best-suited agent using a fixed routing table (IntentGate).

Flow to create a new agent: Hermes → Proteo (domain analysis) → Hermes → Atena (persona construction) → metadata integration in `.opencode/agents/<name>.md`.

## Folder Structure

- AI agent profiles are integrated in files under `.opencode/agents/` with additional metadata.
- `Team/Handoff/YYYY/MM/` — Agent output files (handoff). Every agent invocation writes one file here. See `Team/SOPs/handoff-guide.md` for full spec.
- `Team/Fucina/` — Team working files (repo clonati, analisi temporanee, working data). **Gitignorato.**
  - `Team/Fucina/repos/` — Repository clonati per analisi e reference
  - `Team/Fucina/analyses/` — Note di analisi temporanee
  - `Team/Fucina/KBA/` — Working file del processo KBA
- `Team/Hermes/` — Hermes scratchpad e stato operativo.
- `Team/Members/` — Identity files for team agents
- `Team/Meta/` — System documentation: tool guides, conventions
- `Team/Prompts/` — Prompt library
- `Team/SOPs/` — Standard operating procedures
- `Inbox/` — User PDFs to convert (input for pdf_converter)
- `Library/deliverables/` — Final outputs destined for the user
- `Library/` — **Team Obsidian Vault** (see `Team/SOPs/obsidian-vault-conventions.md` for conventions). Symlink to private git repo with backup.
  - `Library/documents/` — Markdown files converted from PDFs
  - `Library/assets/images/` — Images extracted from PDFs, organized by document slug
  - `Library/data/` — SQLite database (`pdf_index.db`), converter logs, KBA catalog
  - `Library/Wiki/` — **Team Olimpo Knowledge Wiki** (LLM Wiki pattern). Compiled and interconnected knowledge: concepts, decisions, research. Chronological structure YYYY/MM/.
    - `index.md` — Navigable semantic index
    - `log.md` — Chronological wiki operations log
    - `concepts/YYYY/MM/` — Persistent conceptual pages
    - `decisions/YYYY/MM/` — Architectural decisions
    - `research/YYYY/MM/` — Completed research summaries
  - `Library/emails/` — Email vault
- `tools/pdf_converter/` — Python module for PDF → Markdown conversion (guide: `Team/Meta/pdf-converter-guida.md`)
- `opencode.json` (root) — Main OpenCode agent configuration
- `.opencode/agents/` — Individual agent system prompt files

## Conventions

- Each agent profile in `.opencode/agents/` uses standard OpenCode frontmatter
- Agent names are Greek mythological figures

## Handoff Protocol

Every worker agent invocation **must** end by writing one handoff file before returning control to Hermes. **No exceptions. Applies to all agents except Hermes (orchestrator).**

Full specification: `Team/SOPs/handoff-guide.md`
