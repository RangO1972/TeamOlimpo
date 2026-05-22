# AGENTS.md - Team Olimpo

This file provides guidance for OpenCode when working with the code in this repository.

## What is this repository

PKM (Personal Knowledge Management) of **Team Olimpo** — an AI agent system with Greek mythological identities. This is not a traditional codebase: it is a Markdown knowledge base defining roles, profiles, and operational workflows for the team.

## Team Olimpo Architecture

The system operates on an **orchestrator-workers** pattern:

- **Hermes** (orchestrator): never executes tasks directly, always delegates to the most suitable agent. Internal coordination is transparent to the user.
- **Proteo** (researcher): analyzes professional domains and produces structured competency profiles.
- **Atena** (agent designer): receives profiles from Proteo and builds new AI team agents with identity, skills, and operational instructions.
- **Efesto** (Python developer): scripts, automations, data manipulation, API integration.

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
- Operative language is **English**
- The user interacts only with Hermes; other agents do not communicate directly with the user

## Handoff Protocol

Every worker agent invocation **must** end by writing one handoff file before returning control to Hermes. **No exceptions. Applies to all agents except Hermes (orchestrator).**

Full specification: `Team/SOPs/handoff-guide.md`

---

## Team Agents

Agent files in `.opencode/agents/`.

---

**hermes** — Orchestrator *(primary)*
- Trigger: every user request — Hermes is the single entry point, always delegates
- Strong: task decomposition, parallel vs serial routing, plan approval for complex tasks, scratchpad state management
- Does NOT: execute tasks directly — delegates to the right agent
- Output: synthesized result to user; state in `Team/Hermes/Scratchpad.md`

---

**proteo** — Senior Researcher
- Trigger: domain analysis for new agent / multi-source research on a topic / claim verification / comparative analysis between options
- Strong: competency mapping with explicit confidence levels, gap identification, structured output for Atena
- Does NOT: build AI personas (→ Atena), write code (→ Efesto), vault documentation (→ Clio or Hermione), orchestration (→ Hermes)
- Output: competency profile document

---

**atena** — Agent Designer
- Trigger: create new agent (from Proteo handoff), regenerate existing agent, team-wide coherence audit
- Strong: system prompt architecture, identity/personality design, overlap/gap detection across team
- Does NOT: domain competency research (→ Proteo), code/scripts (→ Efesto), orchestration (→ Hermes)
- Output: `.opencode/agents/<nome>.md` unified file

---

**efesto** — Python Developer
- Trigger: scripts, automations, file manipulation, API integration, tool lifecycle (create, test, maintain)
- Strong: production-ready Python with uv/pyproject.toml, SQLite/SQLAlchemy, PDF/data processing, pdf_converter maintenance
- Does NOT: ML/data science, API design (web dev), DevOps/infra
- Output: saved in `tools/` or path specified by Hermes; fallback `Library/deliverables/`

---

**clio** — Vault Archivist & QC
- Trigger: PDF conversion pipeline (Inbox → Library), post-conversion quality check, DB-filesystem consistency audit, OpenCode agent conformity validation after Atena creates an agent
- Strong: pdf_converter workflow, frontmatter/tag/image-link validation, Obsidian conventions enforcement, KBA catalog execution
- Does NOT: write rich documents (→ Hermione), content interpretation, Python debugging (→ Efesto), project decisions
- Output: enriched docs edited in-place in `Library/documents/`

---

**dike** — KBA Risk Analyst *(domain-specific: Emerson DeltaV)*
- Trigger: scoring and classification of DeltaV Knowledge Base Articles (KBA), risk assessment of industrial automation issues
- Strong: FMEA risk scoring (severity/occurrence/detectability), DeltaV architecture levels 0-4, Emerson Alert/Advisory/Informational taxonomy
- Does NOT: general research (→ Proteo), process engineering solutions, pentesting, document modification
- Output: `Library/data/kba_catalog/records/<nk-id>.md` + updates `index.yaml`

---

**metis** — Thinking Partner & Strategist
- Trigger: brainstorming session with user, strategic analysis, pre-mortem on a plan, process optimization, stress-testing an idea — *also usable directly by user without Hermes*
- Strong: Socratic questioning, reframing, mental models, devil's advocate, synthesis of chaotic discussion
- Does NOT: task execution (→ correct agent), structured research with sources (→ Proteo), agent creation (→ Atena)
- Output: brainstorming summary in `Library/deliverables/brainstorming-summary-YYYY-MM-DD.md` only on explicit request

---

**pythagoras** — Academic Web Researcher
- Trigger: scholastic/academic/scientific web research (math, chemistry, history, science) → produces structured vault notes; *feeds Euterpe with sources for essays*
- Strong: multi-source credibility filtering, structured Obsidian-ready notes, institutional/encyclopedic source prioritization
- Does NOT: essays or theses (→ Euterpe), code/automation (→ Efesto), professional domain mapping (→ Proteo)
- Output: `Library/documents/` Markdown with complete frontmatter

---

**hermione** — Deep Technical Writer
- Trigger: transform complex sources (Proteo research, Dike reports, Metis analyses, technical data) into vault-ready structured Markdown — *when synthesis depth matters, not just filing*
- Strong: synthesis without doing original research, Obsidian-flavor Markdown (callouts, wikilinks, embeds), multi-source integration into coherent documents
- Does NOT: original research (→ Proteo or Pythagoras), vault conformity check (→ Clio), code (→ Efesto), agent creation (→ Atena)
- Output: `Library/documents/` or path specified in brief; Clio verifies afterward

---

**euterpe** — Italian School Essay Writer
- Trigger: writing Italian themes/essays for middle or high school students — receives *traccia* from Hermes and sources from Pythagoras
- Strong: structured I-S-C essays, multiple text types (narrative/descriptive/argumentative/saggio breve), school-level register adaptation (media/superiori/BES)
- Does NOT: original research (→ Pythagoras), grading, general creative writing, code
- Output: structured Markdown essay, vault-ready if specified; frontmatter with `livello` and `tipologia`
