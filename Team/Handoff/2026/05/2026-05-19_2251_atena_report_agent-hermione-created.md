---
data: 2026-05-19
timestamp: 2026-05-19T22:51:00
agent: atena
task_id: T-NNN
invocation: 1
type: report
status: completed
priority: medium
title: "Hermione agent file created — English version"
completion_notes: "Step 9 of member-creation-flow.md completed. File written to .opencode/agents/hermione.md overwriting Italian original. Registro updated. All checklist items passed."
output_refs:
  - .opencode/agents/hermione.md
  - Team/Members/Registro.md
quality_score: 5
external_review: false
next_action: "Hermes: activate member, update Scratchpad per Step 10."
---

# Hermione Agent File Created — English Version

**Agent**: Hermione — Deep Technical Writer
**File**: `.opencode/agents/hermione.md`
**Design source**: `Library/Handoff/2026/05/2026-05-19_2246_atena_profile_design-hermione.md`

## Checklist Results

| # | Criterion | Result |
|---|-----------|--------|
| 1 | `description:` present, operational, ~150-200 chars, in English, no member name references | **PASS** |
| 2 | `mode:` present | **PASS** — `mode: subagent` |
| 3 | `model:` present and valid | **PASS** — `model: opencode/big-pickle` |
| 4 | `permission:` present with appropriate permissions | **PASS** — bash: deny, edit: allow, read: allow, task: deny |
| 5 | NO custom frontmatter fields | **PASS** — only standard fields used |
| 6 | Header comment present (2-3 lines for humans: who, does, doesn't do) | **PASS** — 2 lines after title |
| 7 | Complete operative instructions in the body | **PASS** — Identity, Communication Style, Core Rules, Competencies, Workflow (6 steps), Limitations, Output Format, Guiding Principles |
| 8 | Register updated in `Team/Members/Registro.md` | **PASS** |

All 8 checklist items **PASS**.

## Summary of Changes (Italian original → English version)

| Change | Detail |
|--------|--------|
| **Language** | Italian → English throughout |
| **Lines** | 174 → ~210 (structural expansion, not bloat) |
| **Interactions section** | REMOVED (was 11-line table with 7 member names) |
| **Member name references** | 26 occurrences → 0 |
| **"Figlia di Hermes" lore** | REMOVED from Identity |
| **Identity** | Rewritten — no team context, no mythology |
| **Communication Style** | "Ripercorri il lavoro di altri membri" → "work with the material as presented" |
| **Language directive** | `Rispondi sempre in italiano` → `Always reply in English` |
| **Workflow Step 6** | "segnala ad Hermes" / "verifica di Clio" → "Confirm completion. File ready for downstream use." |
| **Limitations** | All 6 rewritten — no "compito di X" patterns |
| **Competencies** | All source references generalized (no member names) |
| **Output Format** | Template comments translated to English |
| **Path fix** | `obsidian-vault.md` → `obsidian-vault-conventions.md` |
| **Header comment** | Added (2 lines: who, does, doesn't do) |
| **Frontmatter description** | Rewritten ~190 chars, operational, EN, no member names |

## Design Decisions Applied

1. **Pure subagent model**: Hermione has no knowledge of team structure, other members, or routing. Her mental model is: receive source files → produce documents.
2. **No Interactions section**: removed per user directive. The orchestrator manages all routing.
3. **Boundary-clean limitations**: each limitation defines what Hermione does not do, without naming who does it.
4. **Depth calibration**: profile depth matches role complexity — full 6-step workflow, 4 competency areas, guiding principles, output template.

## Registro Update

Added to `Team/Members/Registro.md` Notes section:
> "Hermione v2 (2026-05-19): Traduzione EN completa, rimozione sezione Interazioni, allineamento subagente puro, zero nomi membri."
