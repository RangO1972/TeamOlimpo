---
data: '2026-05-21'
timestamp: '2026-05-21T00:24:46'
agent: proteo
invocation: 21
type: analysis
status: completed
priority: high
title: Euterpe gap analysis — test nuovo protocollo
---

# Euterpe Gap Analysis — Test Nuovo Protocollo

**Date:** 2026-05-21  
**Analyzer:** Proteo (Senior Researcher)  
**Scope:** Read-only conformance audit of Euterpe agent files against Team Olimpo SOPs.

---

## File 1: `.opencode/agents/euterpe.md` — Operational Profile

Checklist against `Library/SOPs/agent-design-methodology.md` (sections: Agent file structure, Description field, Permission, Prompt Minimal Standard, Common anti-patterns) and `Library/SOPs/agent-creation-flow.md` (checklist).

### 1.1 `description:` present, operational, ~150-200 chars, English, no agent names

**Result: FAIL** ❌

| Sub-check | Status | Detail |
|-----------|--------|--------|
| Present | ✅ | Yes |
| ~150-200 chars | ✅ | ~197 chars — within range |
| English | ✅ | Yes |
| No agent names | ✅ | No agent names |
| **Operational with "Use when..." trigger** | **❌** | **Missing entirely.** SOP requires: *"Contains role AND usage trigger ('Use when...')"* and *"Operational, not poetic"*. Current text is purely descriptive: *"Italian school essay and theme writer for middle and high school students. Composes themes, essays, and argumentative texts. Receives assignment and sources from the orchestrator, produces clear Italian texts."* |

**What to change:** Rewrite to include a usage trigger. Example:
```yaml
description: "Italian essay writer for school assignments. Use when a student needs a theme, saggio breve, or argumentative text in Italian. Receives traccia + sources from orchestrator, returns structured composition."
```

---

### 1.2 `mode:` present

**Result: PASS** ✅

`mode: subagent` — present and valid.

---

### 1.3 `model:` present and valid

**Result: PASS** ✅

`model: opencode/big-pickle` — matches the default specified in agent-design-methodology.md ("Default: `opencode/big-pickle`").

---

### 1.4 `permission:` present with appropriate permissions

**Result: PASS** ✅

Present. Scope is appropriate for a file-writing agent (read + targeted edit paths). Note: `write` is not explicitly listed (only `edit`), but this is a minor semantic point — functionally acceptable for an agent that writes Markdown files.

---

### 1.5 NO custom frontmatter fields

**Result: PASS** ✅

Only standard fields (`description`, `mode`, `model`, `permission`) present in frontmatter. No custom fields.

---

### 1.6 Header comment: 2-3 lines, who/does/doesn't

**Result: PASS** ✅

Lines 15-18:
```
# Euterpe — Italian School Essay & Theme Writer

Italian school essay and theme writer. Produces structured compositions (temi, saggi brevi) in Italian.
Does not conduct research, write code, or interact with the user.
```

Covers who (Italian school essay writer), does (structured compositions), doesn't (research, code, user interaction).

---

### 1.7 Operative instructions in body

**Result: PASS** ✅

Lines 20-111 contain Identity, Core Rules, Competencies, Operational Process, Limitations, Output Format, Guiding Principles.

---

### 1.8 Prompt Minimal Standard — no decorative lines, self-reviewed

**Result: FAIL** ❌

| Issue | Line(s) | Current text | Problem |
|-------|---------|--------------|---------|
| Missing mandatory section | — | No dedicated `## Communication style` section | SOP mandates it (Section 4 in agent-design-methodology.md). Tone info is partially embedded in Identity ("Clear, orderly, didactic...") but not a dedicated block. |
| Missing mandatory section | — | No dedicated `## Interactions` section | SOP mandates Section 8: *"direction (receive/produce) and format. No agent names — Hermes manages routing."* Current file has no Interactions section. |
| Missing mandatory section | — | No dedicated `## References` section | SOP mandates Section 10: external docs (methodology, vault conventions, handoff guide). Currently only mentioned inline (line 104) and not as a structured section. |
| Decorative adjective | Line 22 | *"polished Italian text"* | "Polished" is decorative filler per Prompt Minimal Standard. Remove or replace with operational description. |
| Overlap / bloat | Lines 31, 106-111 | Core Rules (items 3,5,6) overlap with Guiding Principles (items 1,2,4,5) | Content duplication. "Rigid structure" (rule 3) ≈ "Structure" (principle 2). "Output language: Italian" (rule 6) is redundant with Identity. Guiding Principles section could be folded into Core Rules or removed. |
| Typo / formatting error | Line 24 | `**Always write in Italian in your output.***` | Double asterisk at start, triple at end. Should be `**Always write in Italian in your output.**` |

---

### 1.9 Additional structural gaps against agent-design-methodology.md

| Section (per SOP order) | Status | Detail |
|-------------------------|--------|--------|
| 1. Frontmatter | ✅ | OK |
| 2. Header comment | ✅ | Lines 15-18 |
| 3. Identity | ✅ | Lines 20-22 |
| **4. Communication style** | **❌ MISSING** | **No dedicated section.** SOP: *"tone, rhythm, language rule"* |
| 5. Operating rules | ✅ | "Core Rules" — lines 26-32 |
| 6. Competencies | ✅ | Lines 34-72 |
| 7. Workflows | ✅ | "Operational Process" — lines 74-81 |
| **8. Interactions** | **❌ MISSING** | **No dedicated section.** SOP: *"direction (receive/produce) and format"* |
| 9. Limitations | ✅ | Lines 83-86 |
| **10. References** | **❌ MISSING** | **No dedicated section.** SOP: *"external docs (methodology, vault conventions, handoff guide)"* |

**3 mandatory sections missing** from the structural template (communication style, interactions, references).

---

### 1.10 Anti-pattern check (agent-design-methodology.md)

| Anti-pattern | Result | Detail |
|--------------|--------|--------|
| Decorative personality | ⚠️ Partial | Identity describes tone but no dedicated Communication style section to operationalize it |
| Vague limitations | ✅ OK | Explicit list (lines 84-86) |
| Process without steps | ✅ OK | Numbered steps (lines 76-81) |
| Competency list | ✅ OK | Competencies include context ("when/how to use") |
| Custom frontmatter | ✅ OK | None |
| Member name references | ✅ OK | No agent names in this file |

---

## File 2: `Team/Members/euterpe.md` — Identity File

Checklist against `Library/SOPs/agent-design-methodology.md` (Member identity file section) and `Library/SOPs/agent-creation-flow.md` (checklist).

### 2.1 Frontmatter: `type: member`

**Result: FAIL** ❌

**Line 2:** `type: soul`

Must be `type: member` per SOP: *"Frontmatter — `type: member`, `agent: <name>`, `role: <role>` (all lowercase, hyphenated)."*

---

### 2.2 Frontmatter: `agent: <name>` (lowercase)

**Result: PASS** ✅

**Line 3:** `agent: euterpe` — correct.

---

### 2.3 Frontmatter: `role: <role>` (lowercase, hyphenated)

**Result: PASS** ✅

**Line 4:** `role: essay-writer` — correct format.

---

### 2.4 Title: `# <Name> — Team Olimpo`

**Result: FAIL** ❌

**Line 7:** `# SOUL — Euterpe`

Must be `# Euterpe — Team Olimpo` per SOP: *"Title: `# <Name> — Team Olimpo`"*.

---

### 2.5 Sections: `## Identity`, `## Values`, `## Boundaries`, `## Dependencies`

**Result: PASS** ✅

All 4 required sections are present:
- Line 9: `## Identity`
- Line 12: `## Values`
- Line 19: `## Boundaries`
- Line 26: `## Dependencies`

---

### 2.6 Written in English

**Result: FAIL** ❌

The ENTIRE body (lines 10-28) is in Italian. SOP explicitly states: **"English only"**.

| Line | Current (Italian) |
|------|-------------------|
| 10 | `Musa della poesia lirica, reimmaginata come scrittrice di temi e saggi brevi per Team Olimpo. Produco composizioni scolastiche chiare e ben strutturate per studenti di scuola media e superiore. Ricevo la traccia e le fonti dall'orchestratore, restituisco un testo italiano pronto all'uso.` |
| 13-17 | All values in Italian (`Semplicità`, `Struttura rigida`, `Fedeltà alle fonti`, `Rispetto del livello`, `Revisione obbligatoria`) |
| 20-24 | All boundaries in Italian (`Non valuta`, `Non fa ricerca originale`, etc.) |
| 27-28 | Dependencies in Italian |

---

### 2.7 Dependencies list tools/SOPs/data sources — never other agents by name

**Result: FAIL** ❌

**Lines 27-28:**
```
## Dependencies
- Hermes (traccia + fonti)
- Pythagoras (ricerca accademica come fonte)
```

Two violations:
1. **Lists agents by name (Hermes, Pythagoras)** — SOP explicitly prohibits: *"Never list other agents by name. The orchestrator handles routing; agents do not know each other."*
2. **Should list tools, data paths, SOPs** — Current content is agent names + Italian descriptions. Should be something like: `- Library/SOPs/obsidian-vault-conventions.md`, `- Library/SOPs/handoff-guide.md`, `- Team/Inbox/ (assignment intake path)`.

---

### 2.8 One file per agent

**Result: PASS** ✅

Only one `Team/Members/euterpe.md` file exists for this agent.

---

## File 3: `Team/Members/Registro.md`

### 3.1 Euterpe has an individual registry row

**Result: MINOR CONCERN** ⚠️

The registry contains a batch entry for `Tutti | SOUL v1` covering all 11 agents, but **no individual row for Euterpe**. Per the SOP checklist: *"`Team/Members/Registro.md` updated with new row (Date, Agent, Version, Notes)."* While the batch entry technically acknowledges Euterpe's existence, individual rows are preferable for version tracking and audit trail.

---

## Summary of Gaps

| ID | File | Check | Severity |
|----|------|-------|----------|
| G1 | `.opencode/agents/euterpe.md` | `description:` missing "Use when..." trigger | **High** |
| G2 | `.opencode/agents/euterpe.md` | Missing mandatory `## Communication style` section | **High** |
| G3 | `.opencode/agents/euterpe.md` | Missing mandatory `## Interactions` section | **High** |
| G4 | `.opencode/agents/euterpe.md` | Missing mandatory `## References` section | **Medium** |
| G5 | `.opencode/agents/euterpe.md` | Decorative adjective "polished" (line 22) | **Low** |
| G6 | `.opencode/agents/euterpe.md` | Core Rules / Guiding Principles content overlap | **Low** |
| G7 | `.opencode/agents/euterpe.md` | Typo: triple asterisk `***` on line 24 | **Low** |
| G8 | `Team/Members/euterpe.md` | `type: soul` instead of `type: member` (line 2) | **High** |
| G9 | `Team/Members/euterpe.md` | Title `# SOUL — Euterpe` instead of `# Euterpe — Team Olimpo` (line 7) | **High** |
| G10 | `Team/Members/euterpe.md` | Entire body in Italian — must be English | **High** |
| G11 | `Team/Members/euterpe.md` | Dependencies list agent names (Hermes, Pythagoras) — must list tools/SOPs | **High** |
| G12 | `Team/Members/Registro.md` | No individual Euterpe row (only batch "Tutti" entry) | **Low** |

### Gap count

| Severity | Count |
|----------|-------|
| **High** | 8 |
| **Medium** | 1 |
| **Low** | 3 |
| **Total** | **12** |

### Key findings

1. **Identity file is the most non-conformant**: Italian text, wrong frontmatter type, wrong title, agent names in Dependencies — 4 high-severity issues in one file.
2. **Operational profile is structurally incomplete**: 3 mandatory sections (Communication style, Interactions, References) are missing from the agent-design-methodology 10-section template.
3. **Description is descriptive, not operational**: Missing the "Use when..." usage trigger that makes the field an agent selection tool.
4. **Prompt Minimal Standard partially violated**: Decorative adjectives, content duplication, formatting typo.
