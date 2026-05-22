---
data: '2026-05-21'
timestamp: '2026-05-21T01:14:42'
agent: proteo
invocation: 24
type: analysis
status: completed
priority: medium
title: Gap analysis batch — 9 agenti
task_id: T-REVISIONE-024
---

# Gap Analysis — 9 Agenti (Proteo)

**Methodology**: `Library/SOPs/agent-review-flow.md` full checklist × `Library/SOPs/agent-design-methodology.md`
**Date**: 2026-05-21
**Analyzed by**: Proteo

---

## Summary

**Verdict**: FAIL
**Total gaps found**: 76 (spread across all 9 agents)

Every agent fails. All 9 `Team/Members/*.md` files share 4 systematic defects (`type: soul` instead of `type: member`, wrong title, Italian language, agent names in dependencies). Registro lacks individual rows for 8/9 agents. `.opencode/agents/` files vary widely in section completeness.

Hermione has the most structural issues in `.opencode/` (overlapping Core Rules/Guiding Principles, agent name reference). Pythagoras deviates most from the 10-point template. Proteo and Hermes have the most missing mandatory sections.

| Agent | .opencode gaps | Member gaps | Registro gaps | **Total** |
|-------|:---:|:---:|:---:|:---:|
| Proteo | 7 | 4 | 1 | **12** |
| Hermes | 6 | 4 | 1 | **11** |
| Pythagoras | 6 | 4 | 1 | **11** |
| Hermione | 5 | 4 | 1 | **10** |
| Efesto | 3 | 4 | 1 | **8** |
| Eunomia | 2 | 4 | 1 | **7** |
| Metis | 1 | 4 | 1 | **6** |
| Dike | 1 | 4 | 1 | **6** |
| Atena | 1 | 4 | 0 | **5** |
| **Total** | **32** | **36** | **8** | **76** |

---

## Per-agent results

---

### 1. Proteo

#### `.opencode/agents/proteo.md`

- ❌ **description length** — 139 chars, expected ~150–200. Line 2.
- ✅ `mode: subagent` present.
- ✅ `model: opencode/big-pickle` present and valid.
- ✅ `permission:` present, proportional to research role.
- ✅ No custom frontmatter fields.
- ❌ **Header comment** — missing. No 2-3 line who/does/doesn't block between frontmatter and identity. Expected after line 11.
- ✅ Operative instructions in body (Workflows section).
- ❌ **Decorative adjective in description** — "Professional" in "Professional domain analysis" is on the banned list (`agent-design-methodology.md` line 109). Lines 2–3.
- ❌ **Sections per 10-point template** — 5 gaps:
  - ❌ **Header comment** (mandatory, point 2) — missing
  - ❌ **Communication style** (mandatory, point 4) — missing; no `## Communication Style` section
  - ❌ **Competencies** (mandatory, point 6) — missing; no `## Competencies` section (only Workflows)
  - ❌ **Interactions** (point 8) — missing; no receive/produce section
  - ❌ **Limitations** (mandatory, point 9) — missing; no explicit `## Limitations` section ("Operating Constraints" partially overlaps but is not a formal Limitations block)
- ✅ No agent names referenced in body.
- ✅ Prompt Minimal Standard — no decorative lines, self-review pass (aside from "Professional").

**Subtotal**: 7 gaps

#### `Team/Members/proteo.md`

- ❌ **Frontmatter `type:`** — `type: soul`, expected `type: member`. Line 2.
- ✅ `agent: proteo` correct.
- ✅ `role: senior-researcher` correct (lowercase, hyphenated).
- ❌ **Title** — `# SOUL — Proteo`, expected `# Proteo — Team Olimpo`. Line 7.
- ✅ Sections present: `## Identity`, `## Values`, `## Boundaries`, `## Dependencies`.
- ❌ **Language** — entire file is in Italian. Expected English.
- ❌ **Dependencies references agent name** — `Hermes (briefing)` references another agent by name. Line 25–26.
- ✅ One file per agent.

**Subtotal**: 4 gaps

#### `Team/Members/Registro.md`

- ❌ **No individual row for Proteo** — only a bulk "Tutti" entry (2026-05-20) covers all SOUL file creations. Lacks dedicated per-agent version tracking.
- ✅ "Tutti" bulk entry exists with notes.

**Subtotal**: 1 gap

**Proteo total**: 12 gaps

---

### 2. Atena

#### `.opencode/agents/atena.md`

- ✅ `description:` present (167 chars), operational ("Use when..."), English, no agent names.
- ✅ `mode: subagent` present.
- ✅ `model: opencode/big-pickle` present and valid.
- ✅ `permission:` present, proportional to designer role.
- ✅ No custom frontmatter fields.
- ✅ Header comment present (line 14: "Agent architect. Designs, regenerates, and audits...").
- ✅ Operative instructions in body.
- ✅ Prompt Minimal Standard pass.
- ❌ **Missing dedicated `## Identity` section** — the header comment functions as an identity statement but there is no formal `## Identity` section per the 10-point template (mandatory, point 3). Content exists but section header is absent.
- ✅ `## Communication Style` present.
- ✅ `## Operating Rules` present.
- ✅ `## Competencies` present.
- ✅ `## Workflows` present.
- ✅ `## Interactions & Limits` present (combines interactions and limitations).
- ✅ No agent names referenced in body.

**Subtotal**: 1 gap

#### `Team/Members/atena.md`

- ❌ **Frontmatter `type:`** — `type: soul`, expected `type: member`. Line 2.
- ✅ `agent: atena` correct.
- ✅ `role: agent-designer` correct.
- ❌ **Title** — `# SOUL — Atena`, expected `# Atena — Team Olimpo`. Line 7.
- ✅ Sections present.
- ❌ **Language** — entire file is in Italian. Expected English.
- ❌ **Dependencies reference agent names** — Lists `Proteo (profili di competenza)` and `Hermes (brief di design)`. Lines 26–27.
- ✅ One file per agent.

**Subtotal**: 4 gaps

#### `Team/Members/Registro.md`

- ✅ Dedicated row present: `2026-05-20 | Atena | v2 | Full structural revision…`
- ✅ "Tutti" bulk entry also covers SOUL v1.

**Subtotal**: 0 gaps

**Atena total**: 5 gaps

---

### 3. Efesto

#### `.opencode/agents/efesto.md`

- ✅ `description:` present (154 chars), operational, English, no agent names.
- ✅ `mode: subagent` present.
- ✅ `model: opencode/big-pickle` present.
- ✅ `permission:` present, proportional (code writer: read, edit, bash).
- ✅ No custom frontmatter fields.
- ✅ Header comment present (line 15: "Python developer and tool builder...").
- ✅ Operative instructions in body.
- ✅ Prompt Minimal Standard pass.
- ❌ **Missing dedicated `## Identity` section** — the header comment partially covers identity but no formal `## Identity` section (mandatory, point 3).
- ✅ `## Style` (Communication style) present.
- ✅ `## Rules` (Operating rules) present.
- ✅ `## Skills` (Competencies) present.
- ✅ `## Workflow` present.
- ❌ **Missing `## Interactions` section** (point 8) — no receive/produce section. The "## Limits" section at the end is purely limitations.
- ✅ `## Limits` (Limitations) present.
- ❌ **Missing `## References` section** (point 10) — no references to SOPs or methodology documents.
- ✅ No agent names in body.

**Subtotal**: 3 gaps

#### `Team/Members/efesto.md`

- ❌ **Frontmatter `type:`** — `type: soul`, expected `type: member`.
- ✅ `agent: efesto`, `role: python-developer` correct.
- ❌ **Title** — `# SOUL — Efesto`, expected `# Efesto — Team Olimpo`.
- ✅ Sections present.
- ❌ **Language** — Italian.
- ❌ **Dependencies** — Lists `Hermes (brief di specifica)` and `Team Olimpo (test e feedback)` — agent names.
- ✅ One file per agent.

**Subtotal**: 4 gaps

#### `Team/Members/Registro.md`

- ❌ No individual row for Efesto. Only covered under bulk "Tutti" entry.

**Subtotal**: 1 gap

**Efesto total**: 8 gaps

---

### 4. Hermes

#### `.opencode/agents/hermes.md`

- ❌ **description length** — 130 chars, expected ~150–200. Line 2.
- ✅ `mode: primary` present.
- ✅ `model: opencode/big-pickle` present.
- ❌ **`permission:` potentially disproportionate** — has `bash: allow`. The methodology table assigns `bash` to "Writes code/files", not to "Delegates to other agents" (`read, write, edit, task`). Hermes is an orchestrator, not a code writer. While this may be intentional, it deviates from the recommended permission profile. Lines 5–9.
- ✅ No custom frontmatter fields.
- ❌ **Header comment** — missing. No who/does/doesn't block after frontmatter. Goes directly from title to `## State Management ← NON OPTIONAL`.
- ✅ Operative instructions in body (very detailed).
- ✅ Prompt Minimal Standard — mostly clean. "Expert PM" borderline but not on the explicit banned list.
- ❌ **Sections per 10-point template** — 4 gaps:
  - ❌ **Header comment** (mandatory, point 2) — missing
  - ❌ **Competencies** (mandatory, point 6) — missing; no dedicated competencies section
  - ❌ **Interactions** (point 8) — missing; no receive/produce section
  - ❌ **Limitations** (mandatory, point 9) — missing; no formal `## Limitations` section (some limits implied in Operating Rules but not explicit)
- ✅ `## Identity` present.
- ✅ `## Communication Style` present.
- ✅ `## Operating Rules` present.
- ✅ `## Workflows` present.
- ✅ `## Reference Documents` present.
- ❌ **Agent names in body** — Lines 111–112: `Proteo (domain analysis) → Atena (profile). Serial — Atena depends on Proteo.` and `Research/analysis: Proteo → return result.` Reference other agents by name, violating `agent-design-methodology.md` line 79.

**Subtotal**: 6 gaps

#### `Team/Members/hermes.md`

- ❌ **Frontmatter `type:`** — `type: soul`, expected `type: member`.
- ✅ `agent: hermes`, `role: orchestrator` correct.
- ❌ **Title** — `# SOUL — Hermes`, expected `# Hermes — Team Olimpo`.
- ✅ Sections present.
- ❌ **Language** — Italian.
- ❌ **Dependencies** — Lists all 10 other agents by name: `Tutti gli agenti Team Olimpo (Proteo, Atena, Efesto, Clio, Dike, Metis, Pythagoras, Hermione, Euterpe, Eunomia)`. The methodology explicitly forbids referencing other agents (line 94: "Never list other agents by name").
- ✅ One file per agent.

**Subtotal**: 4 gaps

#### `Team/Members/Registro.md`

- ❌ No individual row for Hermes. Only bulk "Tutti" entry.

**Subtotal**: 1 gap

**Hermes total**: 11 gaps

---

### 5. Hermione

#### `.opencode/agents/hermione.md`

- ❌ **description length** — 217 chars, expected ~150–200 (8.5% over the upper bound). Lines 2–4.
- ✅ `mode: subagent` present.
- ✅ `model: opencode/big-pickle` present.
- ✅ `permission:` present, proportional.
- ✅ No custom frontmatter fields.
- ✅ Header comment present (lines 16–17).
- ✅ Operative instructions in body.
- ❌ **Prompt Minimal Standard — Overlap between Core Rules and Guiding Principles:**
  - `## Core Operating Rules` rules 2 (Source fidelity) / 4 (Critical synthesis) / 3 (Obsidian conventions) / 5 (Source transparency) overlap substantially with `## Guiding Principles` rules 2 (Fidelity) / 1 (Depth) / 4 (Conventions) / 3 (Structure is not overlap). This duplicates guidance and violates the "no overlap" cross-check. Lines 27–31 vs lines 93–96.
- ❌ **Sections per 10-point template** — 3 gaps:
  - ❌ **Communication style** (mandatory, point 4) — missing; no `## Communication Style` section. "Always reply in English" is embedded in Identity but not a dedicated section.
  - ❌ **Interactions** (point 8) — missing; no formal receive/produce `## Interactions` section. `## Limitations` touches on it but is not structured as Interactions.
  - ❌ **References** (point 10) — missing; no `## References` section linking to SOPs.
- ✅ `## Identity` present.
- ✅ `## Core Operating Rules` present.
- ✅ `## Competencies` present.
- ✅ `## Operational Process` (Workflows) present.
- ✅ `## Limitations` present.
- ❌ **Agent name in body** — `## Limitations` line 68: `(you apply conventions, Clio verifies).` References "Clio" by name.

**Subtotal**: 5 gaps

#### `Team/Members/hermione.md`

- ❌ **Frontmatter `type:`** — `type: soul`, expected `type: member`.
- ✅ `agent: hermione`, `role: technical-writer` correct.
- ❌ **Title** — `# SOUL — Hermione`, expected `# Hermione — Team Olimpo`.
- ✅ Sections present.
- ❌ **Language** — Italian.
- ❌ **Dependencies** — Lists `Hermes (sorgenti e brief)` and `Clio (verifica conformità post-produzione)`.
- ✅ One file per agent.

**Subtotal**: 4 gaps

#### `Team/Members/Registro.md`

- ❌ No individual row for Hermione. Only bulk "Tutti" entry.

**Subtotal**: 1 gap

**Hermione total**: 10 gaps

---

### 6. Metis

#### `.opencode/agents/metis.md`

- ✅ `description:` present (183 chars), operational, English, no agent names.
- ✅ `mode: all` present (valid for dual-role agent).
- ✅ `model: opencode/big-pickle` present.
- ✅ `permission:` present, proportional.
- ✅ No custom frontmatter fields.
- ✅ Header comment present (lines 14–15).
- ✅ Operative instructions in body (detailed workflows).
- ✅ Prompt Minimal Standard pass.
- ❌ **Sections per 10-point template** — 1 gap:
  - ❌ **Communication style** (mandatory, point 4) — missing formal `## Communication Style` section. Tone/register is described within `## Identity` but not as a dedicated section.
- ✅ `## Identity` present.
- ✅ `## Operating Rules` present.
- ✅ `## Competencies` present.
- ✅ `## Workflows` present (detailed with 0. Agent creation flow + 1–5 Thinking partner flow).
- ✅ `## Interactions` present.
- ✅ `## Limitations` present.
- ✅ `## References` present.
- ✅ No agent names referenced in body.

**Subtotal**: 1 gap

#### `Team/Members/metis.md`

- ❌ **Frontmatter `type:`** — `type: soul`, expected `type: member`.
- ✅ `agent: metis`, `role: thinking-partner` correct.
- ❌ **Title** — `# SOUL — Metis`, expected `# Metis — Team Olimpo`.
- ✅ Sections present.
- ❌ **Language** — Italian.
- ❌ **Dependencies** — Lists `Hermes (delegation per review)` — agent name.
- ✅ One file per agent.

**Subtotal**: 4 gaps

#### `Team/Members/Registro.md`

- ❌ No individual row for Metis. Only bulk "Tutti" entry.

**Subtotal**: 1 gap

**Metis total**: 6 gaps

---

### 7. Dike

#### `.opencode/agents/dike.md`

- ✅ `description:` present (196 chars), operational ("Use for..."), English, no agent names.
- ✅ `mode: subagent` present.
- ✅ `model: opencode/big-pickle` present.
- ✅ `permission:` present, proportional.
- ✅ No custom frontmatter fields.
- ✅ Header comment present (lines 14–15).
- ✅ Operative instructions in body (very detailed operational workflow).
- ✅ Prompt Minimal Standard pass.
- ❌ **Sections per 10-point template** — 1 gap:
  - ❌ **Communication style** (mandatory, point 4) — missing dedicated `## Communication Style` section. Tone embedded in `## Identity` but not a separate section.
- ✅ `## Identity` present.
- ✅ `## Operating Rules` present.
- ✅ `## Competency Domain: Industrial Automation` (Competencies) present.
- ✅ `## Operational Workflow` (Workflows) present.
- ✅ `## Interactions & Limitations` present (combines interactions and limitations).
- ✅ `## References` present.
- ✅ No agent names in body.

**Subtotal**: 1 gap

#### `Team/Members/dike.md`

- ❌ **Frontmatter `type:`** — `type: soul`, expected `type: member`.
- ✅ `agent: dike`, `role: kba-risk-analyst` correct.
- ❌ **Title** — `# SOUL — Dike`, expected `# Dike — Team Olimpo`.
- ✅ Sections present.
- ❌ **Language** — Italian.
- ❌ **Dependencies** — Lists `Clio (documenti KBA convertiti in Library/documents/)` and `Hermes (richieste di analisi)` — agent names.
- ✅ One file per agent.

**Subtotal**: 4 gaps

#### `Team/Members/Registro.md`

- ❌ No individual row for Dike. Only bulk "Tutti" entry.

**Subtotal**: 1 gap

**Dike total**: 6 gaps

---

### 8. Eunomia

#### `.opencode/agents/eunomia.md`

- ✅ `description:` present (194 chars), operational ("Use when..."), English, no agent names.
- ✅ `mode: subagent` present.
- ✅ `model: opencode/big-pickle` present.
- ✅ `permission:` present, proportional.
- ✅ No custom frontmatter fields.
- ❌ **Header comment** — missing. Goes directly from title (`# Eunomia — Contextual Analyst`) to `## Identity`. No 2-3 line who/does/doesn't block.
- ✅ Operative instructions in body.
- ✅ Prompt Minimal Standard pass.
- ❌ **Sections per 10-point template** — 2 gaps:
  - ❌ **Header comment** (mandatory, point 2) — missing
  - ❌ **Communication style** (mandatory, point 4) — missing dedicated `## Communication Style` section
- ✅ `## Identity` present.
- ✅ `## Operating Rules` + `## Decision Heuristics` present.
- ✅ `## Competencies` present.
- ✅ `## Workflows` present.
- ✅ `## Interactions & Limits` present (combines interactions and limitations).
- ✅ `## References` present.
- ✅ No agent names in body.

**Subtotal**: 2 gaps

#### `Team/Members/eunomia.md`

- ❌ **Frontmatter `type:`** — `type: soul`, expected `type: member`.
- ✅ `agent: eunomia`, `role: contextual-analyst` correct.
- ❌ **Title** — `# SOUL — Eunomia`, expected `# Eunomia — Team Olimpo`.
- ✅ Sections present.
- ❌ **Language** — Italian.
- ❌ **Dependencies** — Lists `Hermes (richieste di analisi)` — agent name.
- ✅ One file per agent.

**Subtotal**: 4 gaps

#### `Team/Members/Registro.md`

- ❌ No individual row for Eunomia. Only bulk "Tutti" entry.

**Subtotal**: 1 gap

**Eunomia total**: 7 gaps

---

### 9. Pythagoras

#### `.opencode/agents/pythagoras.md`

- ✅ `description:` present (191 chars), operational ("Use for..."), English, no agent names.
- ✅ `mode: subagent` present.
- ✅ `model: opencode/big-pickle` present.
- ✅ `permission:` present, proportional (research: read, edit, websearch, webfetch).
- ✅ No custom frontmatter fields.
- ✅ Header comment present (lines 16–17: "Academic web researcher covering all scholastic and academic disciplines. Does NOT write essays, develop code, or perform professional domain analysis.").
- ✅ Operative instructions in body (`## Operational Instructions`).
- ✅ Prompt Minimal Standard — some redundancy between "What You Do", "What You Don't Do", and "Interaction Guidelines" but no decorative adjectives.
- ❌ **Sections per 10-point template** — 6 gaps (the most deviant structure among all agents):
  - ❌ **Communication style** (mandatory, point 4) — missing dedicated section. "Always reply in English" is buried in `## Interaction Guidelines` (line 72).
  - ❌ **Operating rules** (mandatory, point 5) — missing formal `## Operating Rules` section. Content is scattered across `## What You Do`, `## What You Don't Do`, and `## Operational Instructions` without a unified rules section.
  - ❌ **Workflows** (mandatory, point 7) — `## Operational Instructions` has steps but they are not numbered with I/O per step as required by methodology (point 7: "numbered steps with input/output per step").
  - ❌ **Interactions** (point 8) — `## Interaction Guidelines` is present but generic, lacking the structured receive/produce format.
  - ❌ **Limitations** (mandatory, point 9) — no formal `## Limitations` section. `## What You Don't Do` is close but not a formal limitations block.
  - ❌ **References** (point 10) — missing references section linking to SOPs.
- ✅ `## Identity` present.
- ✅ `## Skills and Competencies` present.
- ✅ No agent names in body (no explicit names; "the developer" and "the requester" are generic).

**Subtotal**: 6 gaps

#### `Team/Members/pythagoras.md`

- ❌ **Frontmatter `type:`** — `type: soul`, expected `type: member`.
- ✅ `agent: pythagoras`, `role: academic-researcher` correct.
- ❌ **Title** — `# SOUL — Pythagoras`, expected `# Pythagoras — Team Olimpo`.
- ✅ Sections present.
- ❌ **Language** — Italian.
- ❌ **Dependencies** — Lists `Hermes (brief di ricerca)` and `Euterpe (destinatario di fonti per temi scolastici)` — agent names.
- ✅ One file per agent.

**Subtotal**: 4 gaps

#### `Team/Members/Registro.md`

- ❌ No individual row for Pythagoras. Only bulk "Tutti" entry.

**Subtotal**: 1 gap

**Pythagoras total**: 11 gaps

---

## Cross-checks (all agents)

| Check | Result | Details |
|-------|--------|---------|
| No overlap Core Rules / Guiding Principles | ❌ | Hermione: `## Core Operating Rules` (rules 2,3,4,5) overlap with `## Guiding Principles` (principles 1,2,4). Other agents: N/A (no such sections). |
| No decorative adjectives | ❌ | Proteo description: "Professional" (explicitly banned in `agent-design-methodology.md` line 109). Others clean. |
| YAML frontmatter parses correctly | ✅ | All 9 `.opencode/agents/` and all 9 `Team/Members/` files parse as valid YAML. |
| Language: English throughout | ❌ | **All 9 `Team/Members/*.md` files are in Italian.** `.opencode/agents/*.md` files are in English (pass). Domain-specific Italian terms like "DeltaV" are acceptable but full Italian prose is not. |

---

## Systematic defects (all agents)

### Defect A — `Team/Members/*.md` frontmatter: `type: soul` (9/9 agents)
The methodology (`agent-design-methodology.md` line 89) specifies `type: member`. Every file uses `type: soul` instead.

### Defect B — `Team/Members/*.md` title: `# SOUL — <Name>` (9/9 agents)
Expected format: `# <Name> — Team Olimpo`. Every file uses `# SOUL — <Name>`.

### Defect C — `Team/Members/*.md` language: Italian (9/9 agents)
All membership identity files are written entirely in Italian. The methodology (line 97) requires English throughout.

### Defect D — `Team/Members/*.md` Dependencies: agent names (9/9 agents)
Every Dependencies section lists one or more other agents by name (e.g., "Hermes", "Proteo", "Clio", "Euterpe"). The methodology (line 94) explicitly states: "Never list other agents by name. The orchestrator handles routing; agents do not know each other."

### Defect E — `Team/Members/Registro.md`: missing individual rows (8/9 agents)
Only Atena has a dedicated row. The bulk "Tutti" (2026-05-20) entry documents SOUL file creation for all agents collectively but does not provide per-agent version tracking.

### Defect F — Missing `## Communication Style` section (5/9 agents)
Proteo, Hermione, Metis, Dike, Eunomia, Pythagoras all lack a dedicated Communication Style section. Atena, Efesto, and Hermes have one.

---

## Handoff path
This handoff is located at the path returned by `handoff_create`.
