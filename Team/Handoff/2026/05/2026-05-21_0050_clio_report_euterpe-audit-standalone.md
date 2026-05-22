---
data: '2026-05-21'
timestamp: '2026-05-21T00:50:54'
agent: clio
invocation: 3
type: report
status: completed
priority: high
title: Euterpe audit — standalone
output_refs: .opencode/agents/euterpe.md, Team/Members/euterpe.md, Team/Members/Registro.md
---

## Summary

**Verdict: FAIL**
**Total gaps found: 1**

One blocking criterion fails (missing References section in `.opencode/agents/euterpe.md`). Two non-blocking notes attached.

---

## Per-file results

### `.opencode/agents/euterpe.md`

| # | Criterion | Result | Detail |
|---|-----------|--------|--------|
| 1 | `description:` present, operational, ~150-200 chars, English, no agent names | ✅ PASS | 221 chars (slightly above ~150-200, acceptable per ~). English, operational, no agent names. |
| 2 | `mode:` present | ✅ PASS | `mode: subagent` |
| 3 | `model:` present and valid | ✅ PASS | `model: opencode/big-pickle` |
| 4 | `permission:` present, proportional to role | ✅ PASS | read:allow + edit scoped to Library/deliverables/**, Library/documents/**, Team/Euterpe/** |
| 5 | NO custom frontmatter fields | ✅ PASS | Only standard fields: description, mode, model, permission |
| 6 | Header comment: 2-3 lines, who/does/doesn't | ✅ PASS | Lines 15-18: "Italian school essay and theme writer. Produces structured compositions… Does not conduct research, write code, or interact with the user." |
| 7 | Operative instructions in body | ✅ PASS | Identity through Output Format provide full operative instructions |
| 8 | Prompt Minimal Standard — no decorative lines, self-reviewed | ✅ PASS | No decorative dividers or banners. Clean formatting. |
| 9 | Sections per 10-point template | ❌ **FAIL** | **References section missing.** The template requires 10 sections: frontmatter, header, identity, comm style, rules, competencies, workflows, interactions, limitations, references. All present except the final `## References` section. SOP references exist inline (obsidian-vault-conventions.md at rule 5 and line 112) but not as a dedicated section. |
| 10 | No agent names referenced in body | ✅ PASS | "orchestrator" is a role, not an agent name. No other agent names found. |

### `Team/Members/euterpe.md`

| # | Criterion | Result | Detail |
|---|-----------|--------|--------|
| 1 | Frontmatter: type/agent/role, lowercase, hyphenated | ✅ PASS | `type: member`, `agent: euterpe`, `role: essay-writer` |
| 2 | Title: `# <Name> — Team Olimpo` | ✅ PASS | `# Euterpe — Team Olimpo` |
| 3 | Sections: Identity, Values, Boundaries, Dependencies | ✅ PASS | All four present |
| 4 | Written in English | ✅ PASS | Entirely in English |
| 5 | Dependencies list tools/SOPs/data — no agent names | ✅ PASS | References "orchestrator" (role), Library/deliverables/, SOP paths. No agent names. |
| 6 | One file per agent | ✅ PASS | Single file |

### `Team/Members/Registro.md`

| # | Criterion | Result | Detail |
|---|-----------|--------|--------|
| 1 | Row present with Date, Agent, Version, Notes | ✅ PASS | Row: `2026-05-20 | Euterpe | v2 | Revisione post-Chimera: …` |
| 2 | Notes describe what changed | ✅ PASS | "Revisione post-Chimera: inglese, dipendenze agente rimosse, Prompt Minimal Standard" — clear change summary |

### Cross-checks

| # | Criterion | Result | Detail |
|---|-----------|--------|--------|
| 1 | No overlap between Core Rules and Guiding Principles | ⚠️ NOTE | Core Rules 2/3/4 (Simple first, Rigid structure, Source use) overlap thematically with Guiding Principles 1/2/3 (Simplicity, Structure, Documentary truth). Framed differently (operational vs. aspirational) so not a strict fail, but duplication exists. |
| 2 | No decorative adjectives | ✅ PASS | No forbidden adjectives (comprehensive, accurate, professional, seamless, polished, etc.) found. |
| 3 | YAML frontmatter parses correctly | ✅ PASS | Both files parse cleanly in isolation. |
| 4 | Language: English throughout | ✅ PASS | English throughout. Domain-specific Italian terms (tema, saggio breve, traccia, scuola media/superiore) in the output format section are acceptable per spec. |

---

## Notes

1. **Description length**: 221 characters — slightly above the ~150-200 guideline. This is a non-blocking observation since the spec uses "~" (approximately). The content is complete and operational.
2. **Core Rules / Guiding Principles overlap**: Rules 2-4 and Principles 1-3 cover the same concepts from different angles (operational directives vs. declarative values). Not a fail, but a minor consistency touchpoint if Atena wishes to tighten it.
3. **Dedicated References section**: The missing `## References` section is the sole blocking issue. The file already references `Library/SOPs/obsidian-vault-conventions.md` inline (rule 5, line 112). A dedicated section would typically list: `Library/SOPs/obsidian-vault-conventions.md`, `Library/SOPs/handoff-guide.md`, and potentially `Library/SOPs/agent-design-methodology.md`.

---

## Action required

**FAIL** — route back to Atena for the missing `## References` section. All other criteria pass or carry only non-blocking notes.
