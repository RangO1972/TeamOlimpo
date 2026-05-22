---
title: "Design — Eunomia v3 Profile"
type: profile
slug: design-eunomia-v3
from: Atena
to: Hermes
date: 2026-05-19
---

# Design Summary: Eunomia v3

## Changes from v2

### P1 — Critical (5 items)

| # | Issue | Change | Rationale |
|---|-------|--------|-----------|
| 1 | Member name references (7 occ.) | Replaced all with role descriptions: "orchestrator" for Hermes, "tool pipeline" for Efesto, "vault conventions" for Clio. | Explicit anti-pattern per methodology: agent files must not reference other members by name. |
| 2 | Missing `write` permission | Added `write: allow` to frontmatter. | The agent creates `Review/summaries/YYYY/MM/DD.md` and `Review/actions.md` — its primary output artifacts. Without `write` these cannot be created. Metis correctly upgraded this to P1. |
| 3 | Unnecessary `bash: ask` | Removed from frontmatter. | The agent's own limitations say "Do not write Python code" and "Do not use external APIs." Granting bash is contradictory and unnecessary. |
| 4 | Missing `## References` section | Added section referencing 3 SOPs: agent-design-methodology.md, handoff-guide.md, obsidian-vault-conventions.md. | Mandatory per methodology (section 10 of 10). |
| 5 | Search tool permissions | Verified: `read: allow` covers `glob` and `grep` operations needed for file/content search in the workflow (steps 1, 5, 6). No additional permissions required. | Cross-checked against other agents (Proteo, Clio) — none have explicit `glob`/`grep` permissions. `read: allow` is sufficient. |

### P2 — Important (2 items)

| # | Issue | Change | Rationale |
|---|-------|--------|-----------|
| 6 | Description: 293 chars, no trigger | Rewritten to 194 chars with "Use when..." trigger phrase. | Per methodology: description must contain role AND usage trigger, 150-200 chars, operational not poetic. |
| 7 | Unverified `email_processor` dependency | Clarified as existing dependency in interactions and signal file sections. Noted but not removed. | Metis flagged this as P1 architectural risk. The dependency exists in the v2 design. It is documented clearly as an existing tool — if it does not exist, this is an Efesto deliverable, not an Atena design issue. |

### P3 — Polish (4 items)

| # | Issue | Change | Rationale |
|---|-------|--------|-----------|
| 8 | Redundant `## Who I Am` / `## Identity` | Merged into single `## Identity` section (4 sentences: mission + do + don't do). | Both covered the same ground. Proteo flagged the duplication. |
| 9 | Section order non-canonical | Reordered to: frontmatter → header comment → identity → communication style → operating rules → competencies → workflows → interactions → limitations → references. | Methodology specifies this exact order. v2 had interactions after vault structure, guiding principles at the end. |
| 10 | Guiding Principles (bonus section) | Preserved as `### Decision Heuristics` under Operating Rules. | Metis noted these are valuable decision guardrails. Integrated rather than removed. |
| 11 | Output templates too verbose (~100 lines) | Condensed: kept note enrichment detail (essential for daily work), kept report format (one terse example). Dropped vault structure tree and actions.md template. | Depth calibration: narrow procedural domain should be concise. Templates for every possible output are over-specification. |

### What was PRESERVED (unchanged)

- The 8-step workflow with explicit Input/Output per step — Proteo called it "exemplary," Metis agreed
- Competency structure organized by 4 domains with usage context
- Operating rules (9 rules, renumbered to keep 1-9)
- Limitations (6 items, member name references removed)
- Overall operational logic: read status:new → follow threads → cross-reference vault → enrich notes → produce reports

## Key Design Decisions

### 1. Identity structure: merged with clear separation

v2 had three overlapping blocks: title line (`# Eunomia v2 — Contextual Analyst`), `## Who I Am` (mission + do/don't), and `## Identity` (mythological role). v3 collapses into:
- Header comment (HTML `<!-- -->`): 3 lines, who/does/doesn't — for human skimming
- `## Identity`: mission statement + what I do / what I don't do — for operational clarity

The mythological framing ("goddess of order") is removed. The identity is now purely functional. The methodology requires identity-behavior coherence, not decorative lore.

### 2. Guiding Principles → Decision Heuristics

Rather than deleting the principles or keeping them as an orphan section at the end, I nested them under Operating Rules as `### Decision Heuristics`. This follows the methodology's guidance for operating rules: "non-negotiable constraints, protocols." The heuristics are exactly that — non-negotiable decision guardrails for edge cases.

### 3. Interactions table: role-based, not name-based

| v2 (names) | v3 (roles) |
|-------------|------------|
| "Hermes" | "Orchestrator" |
| "Efesto — Tool output" | "Tool pipeline — Consumes output" |
| "Clio — Consultation" | "Vault conventions — Reference" |

The row structure is preserved but names are replaced with role descriptions. The orchestrator manages routing; the agent only needs to know the direction (receive/produce/consume).

### 4. `email_processor` dependency: documented but unchanged

I considered two options:
- **(a)** Remove all references and design Eunomia to scan the inbox directly → this would change the operational model and create overlap with the tool pipeline
- **(b)** Keep the dependency but document it clearly → chosen

The `email_processor` is referenced in the Interactions table (as "Tool pipeline"), in the signal file section, and in the limitations (as "if the tool is not producing notes, report to the orchestrator"). This makes the dependency explicit without implying it might not exist. If the tool is missing, it is an Efesto deliverable, not a Eunomia design gap.

### 5. Permission model: minimal and sufficient

```
permission:
  edit: allow    # modify email notes in-place
  read: allow    # read all vault files + implicitly covers glob/grep for search
  write: allow   # create Review/summaries/ and Review/actions.md
```

No `bash`, no `websearch`/`webfetch` (agent does not use external APIs), no `task` (agent does not delegate). This matches the methodology's Research and Analysis pattern but scoped down to file-only operations.

## Verification

### Correctness checks

- [x] No member names — all replaced with role descriptions
- [x] `write: allow` present in frontmatter
- [x] `bash` removed from frontmatter
- [x] `## References` section present with 3 SOPs
- [x] Description is 194 chars (150-200 range) with "Use when..." trigger
- [x] `## Who I Am` and `## Identity` merged into single `## Identity`
- [x] Sections in canonical order (10-section model)
- [x] Guiding Principles preserved as `### Decision Heuristics` under Operating Rules
- [x] Output templates condensed — enrichment detail kept, vault tree dropped, actions format dropped
- [x] 8-step workflow with Input/Output preserved
- [x] Competency structure (4 domains) preserved
- [x] No Italian text remaining
- [x] No "v2" or "v3" in agent file
- [x] Valid YAML frontmatter (no custom fields)
- [x] Header comment in HTML comment format
- [x] Limitations are specific and actionable
- [x] `email_processor` referenced as existing dependency (not "if it exists")

### Structural diff (line count)

| Metric | v2 | v3 |
|--------|----|----|
| Total lines | 245 | ~185 |
| Member name refs | 7 | 0 |
| Sections | 12 (extra: Who I Am, Output, Vault Structure, Guiding Principles) | 10 (canonical) |
| Output templates | 3 full formats ~100 lines | 2 condensed ~30 lines |

### Suggested Hermes actions

1. **Verify `email_processor` tool exists** before routing work to Eunomia. If missing, delegate to Efesto.
2. **Update Registro** to reflect Eunomia v3 is deployed.
3. **No further Atena changes needed** — v3 is structurally complete.
