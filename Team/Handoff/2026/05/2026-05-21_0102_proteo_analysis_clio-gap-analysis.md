---
data: '2026-05-21'
timestamp: '2026-05-21T01:02:04'
agent: proteo
invocation: 22
type: analysis
status: completed
priority: medium
title: Clio gap analysis
---

## Summary

**Verdict: FAIL** — 6 blocking failures found.

| File | Failures | Notes |
|------|----------|-------|
| `.opencode/agents/clio.md` | 1 | `bash: ask` permission not proportional |
| `Team/Members/clio.md` | 4 | Frontmatter, title, language, dependencies |
| `Team/Members/Registro.md` | 1 | Missing Clio-specific row |
| Cross-checks | 0 | Pass |

**Total gaps: 6 blocking, 2 non-blocking observations**

---

## Per-file results

### `.opencode/agents/clio.md`

- ✅ `description:` present, operational (196 chars), English, no agent names
- ✅ `mode:` present (`subagent`)
- ✅ `model:` present and valid (`opencode/big-pickle`)
- ❌ **`permission:` — `bash: ask` not proportional to role.** Clio is a vault archivist and QC specialist. Its workflows are: conversion pipeline monitoring, Markdown/YAML validation, DB-filesystem coherence checks, handoff reports. None require shell execution. Per `agent-design-methodology.md` (§Permission/tool selection): *"bash = code execution — don't grant unless needed"*. Clio's permissions should be `read`, `write`, `edit` (for in-place document enrichment) and the `handoff_create` MCP tool. `bash: ask` on line 8 should be removed.
- ✅ No custom frontmatter fields
- ✅ Header comment: 2-3 lines, who/does/doesn't (lines 16-18)
- ✅ Operative instructions in body
- ✅ Prompt Minimal Standard — no decorative lines, self-reviewed
- ⚠️ *Non-blocking:* No explicit `## Identity` section per the 10-point template. The header comment (lines 16-18) serves as identity — it states who, does, doesn't — but the methodology template requires a dedicated `## Identity` section as point 3. The design-methodology.md says "Mandatory: frontmatter, header comment, identity..." — identity is listed independently.
- ✅ Sections present: frontmatter, header, comm style, rules, competencies, workflows, interactions, limitations, references (9 of 10)
- ✅ No agent names referenced in body

**1 failure, 1 observation.**

### `Team/Members/clio.md`

- ❌ **Frontmatter `type:` — expected `member`, got `soul`.** SOP (`agent-design-methodology.md` §Member identity file) specifies `type: member`. The team has adopted a `type: soul` convention across all member files (documented in Registro.md "SOUL v1 — SOUL files created" line). This is a systematic deviation from the SOP — either the SOP needs updating or all files need correction.
- ✅ `agent: clio` — correct
- ✅ `role: vault-archivist` — correct, lowercase hyphenated
- ❌ **Title: `# SOUL — Clio` — expected `# Clio — Team Olimpo`.** Same systematic deviation as above. The SOP template requires `# <Name> — Team Olimpo`.
- ✅ `## Identity` present
- ✅ `## Values` present
- ✅ `## Boundaries` present
- ❌ **`## Dependencies` — contains agent names.** Lists "Hermes" and "Efesto" by name. SOP explicitly forbids this: *"Never list other agents by name. The orchestrator handles routing; agents do not know each other."* Should reference tools/SOPs only (e.g., `Library/Meta/pdf-converter-guida.md` is a valid reference).
- ❌ **Language: Italian, not English.** The entire file is in Italian. SOP §Member identity file states: *"English only."* Domain-specific terms in Italian are acceptable, but the full text (Identity, Values, Boundaries, Dependencies) is in Italian.
- ✅ One file per agent

**4 failures.**

### `Team/Members/Registro.md`

- ❌ **No Clio-specific row.** The registry has rows for Atena (v2), Tutti (SOUL v1 bulk creation), Euterpe (v2, v3). The "Tutti" entry covers Clio as part of the mass SOUL creation, but there is no individual row with Date, Agent, Clio, Version, Notes describing Clio-specific changes.
- ⚠️ *Non-blocking:* The "Tutti" entry of 2026-05-20 covers all 11 agents' SOUL file creation. If the team considers this sufficient, the Registro SOP spec may need alignment.

**1 failure, 1 observation.**

---

### Cross-checks

- ✅ No overlap between Core Rules and Guiding Principles — only a single `## Operating Rules` section exists
- ✅ No decorative adjectives (comprehensive, accurate, professional, etc.)
- ✅ YAML frontmatter parses correctly in all files
- ✅ Language: `.opencode/agents/clio.md` is in English ✅; `Team/Members/clio.md` is in Italian ❌ (already counted above)

**Pass with 1 pre-counted failure.**

---

## Notes

1. **The `type: soul` / `# SOUL — Name` / Italian-language pattern is consistent across all 11 SOUL files** (checked atena.md, efesto.md). This is a deliberate team convention introduced 2026-05-20. The gap analysis flags it as non-compliant with the current SOP — resolution path: either update `agent-design-methodology.md` to recognize the SOUL format, or convert all member files to the `type: member` / English standard.

2. **`bash: ask` is the highest-priority fix** — it's a genuine security/permissions concern. Clio has no operational need for shell execution.

3. **The `## Identity` section in `.opencode/agents/clio.md`** is semantically present in the header comment but structurally missing as a labeled section. The methodology lists it as mandatory. This is a minor structural gap.

4. **Modification flow limit**: per `agent-review-flow.md`, max 2 FAIL cycles per gap analysis. This first report counts as cycle 1.
