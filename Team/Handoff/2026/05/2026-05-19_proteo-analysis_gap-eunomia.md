---
title: "Gap Analysis — Eunomia Profile vs Agent Design Methodology"
type: analysis
slug: gap-eunomia
from: Proteo
to: Hermes
date: 2026-05-19
---

# Gap Analysis: Eunomia Profile vs Agent Design Methodology

## Summary

**Overall verdict: 4 major gaps, 2 minor gaps, 1 anti-pattern violation.** The profile is structurally strong (9 of 10 sections present) and well-detailed, but has three critical issues: (1) the `description` field is 93 chars over the limit and lacks the required "Use when..." trigger phrase, (2) the References section is entirely missing, and (3) member name references to Hermes, Efesto, and Clio appear 7 times across the body — a direct anti-pattern per the methodology. Permission configuration also has a discrepancy (`bash: ask` for a non-coding agent, missing `write` for an agent that creates files). **Priority:** fix member name references and missing References section first, then address the description length/trigger phrase.

---

## A. Frontmatter

- [x] **description**: **FAIL** — 3 issues detected:
  1. **Length**: 293 characters, exceeds the 150–200 char range by 93 chars.
  2. **Missing trigger phrase**: The methodology requires a "Use when..." or equivalent usage trigger so the system knows when to invoke this agent. The current description is purely declarative (no invocation condition).
  3. Contains "Team Olimpo" (acceptable — team name, not a member name).

- [ ] **mode/model/permission**: **PASS with 2 notes**
  - `mode: subagent` ✅ valid
  - `model: opencode/big-pickle` ✅ valid (matches default)
  - `permission`:
    - `bash: ask` — methodology says "bash = code execution — don't grant unless needed." The agent's own limitations say "Do not write Python code" and "Do not use external APIs." Having bash:ask is unnecessary and contradictory.
    - `write` permission is **missing** — the agent creates new files (`Review/summaries/YYYY/MM/DD.md`, `Review/actions.md`). `edit: allow` alone may not cover creation of new files.
    - `read: allow` ✅
    - `edit: allow` ✅

- [ ] **Custom frontmatter fields**: **PASS** — No custom fields detected. Only `description`, `mode`, `model`, `permission`.

---

## B. Structure (10-section model)

Mandatory sections (8) per methodology: frontmatter, header comment, identity, communication style, operating rules, competencies, workflows, limitations.

| # | Section | Status | Notes |
|---|---------|--------|-------|
| 1 | Frontmatter | ✅ Present | Lines 1–9 |
| 2 | Header comment | ⚠️ Incomplete | Lines 10–20 (`## Who I Am`) serve the *function* of a header (who/does/doesn't do) but are formatted as markdown content, not as a comment block. No HTML comment (`<!-- -->`) found. |
| 3 | Identity | ✅ Present | Lines 21–23 (`## Identity`) — subheading appears after the header, which duplicates the function of `## Who I Am` |
| 4 | Communication style | ✅ Present | Lines 25–31 (`## Personality and Communication Style`) |
| 5 | Operating rules | ✅ Present | Lines 33–43 (`## Operating Rules`) — 9 numbered rules |
| 6 | Competencies | ✅ Present | Lines 45–67 — 4 sub-domains organized with context |
| 7 | Workflows | ✅ Present | Lines 69–150 — numbered steps with input/output per step |
| 8 | Interactions | ✅ Present | Lines 222–228 (`## Team Interactions` table) — **but contains member names (anti-pattern)** |
| 9 | Limitations | ✅ Present | Lines 230–237 — 7 specific bullet points |
| 10 | References | ❌ **Missing** | No `## References` section anywhere in the file |

**Extra sections** (not in the 10-model, not necessarily bad but add length):
- `## Who I Am` (line 13) — functionally duplicates the header comment and identity
- `## Eunomia Output` (line 152) — detailed output templates
- `## Email Vault Structure` (line 201) — directory tree
- `## Guiding Principles` (line 239) — values/principles

**Redundancy**: `## Who I Am` (line 13) and `## Identity` (line 21) overlap significantly. Both describe mission and role.

---

## C. Quality per section

### Identity (lines 21–23)
- **Verdict: ✅ PASS**
- Mission is clear ("bring order to communications, connect every email to its context")
- ~5 sentences, within the 2-4 sentence guideline (borderline)
- Uses member name "Eunomia" (self-reference is acceptable; rule only forbids referencing *other* members)

### Communication Style (lines 25–31)
- **Verdict: ✅ PASS**
- Tone described: "analytical, curious, precise" — and operative instructions reflect this (methodical 8-step workflow, precise input/output definitions)
- Anti-pattern test: tone IS reflected in the instructions. No decorative personality detected.

### Operating Rules (lines 33–43)
- **Verdict: ✅ PASS**
- 9 numbered, non-negotiable rules
- Sequenced in logical operational order (read → thread → identify → search → enrich → report)
- Clear and specific — each rule is verifiable

### Competencies (lines 45–67)
- **Verdict: ✅ PASS**
- Organized by 4 domains with headings: Contextual Email Analysis, Vault Search and Linking, Email Note Enrichment, Reporting
- Each competency includes context for what it involves (e.g., "Reading YAML frontmatter: message_id, references, date...")
- Not a flat list — usage context provided ✅

### Workflows (lines 69–150)
- **Verdict: ✅ PASS** (exemplary)
- 8 numbered steps (SCAN → READ → FOLLOW THREAD → IDENTIFY SENDER → SEARCH WIKI → SEARCH PROJECTS → ENRICH NOTE → REPORT)
- Each step has explicit **Input** and **Output**
- Includes sub-workflows for note enrichment detail and signal file format
- This is the strongest section — meets methodology requirements precisely

### Limitations (lines 230–237)
- **Verdict: ✅ PASS**
- 7 specific limitations, all concrete and actionable
- Examples: "Do not write Python code — that's Efesto's job", "Do not modify files outside `vaults/email/`", "Do not force links"
- **Note: line 232 references Efesto by name** (see anti-patterns)

### References
- **Verdict: ❌ MISSING**
- No `## References` section
- Methodology requires references to external docs: methodology, vault conventions, handoff guide
- `Library/SOPs/obsidian-vault-conventions.md` is mentioned in the interactions table (line 228) but not in a formal References section

---

## D. Anti-patterns detected

### 1. Member name references ❌ ANTI-PATTERN (7 occurrences)
The methodology states: *"Never mention specific team member names"* (description rule) and *"No member names — Hermes manages routing"* (interactions rule).

| Line | Text | Member |
|------|------|--------|
| 31 | "Communication with **Hermes**: synthetic, results-oriented" | Hermes |
| 43 | "Produce a report at the end of each session for **Hermes**" | Hermes |
| 154 | "### Report to **Hermes**" (heading) | Hermes |
| 226 | "**Hermes** — Receives / Returns" | Hermes |
| 227 | "**Efesto** — Tool output" | Efesto |
| 228 | "**Clio** — Consultation" | Clio |
| 232 | "Do not write Python code — that's **Efesto**'s job. If the `email_processor` tool does not exist, report to **Hermes**." | Efesto + Hermes |

### 2. Description lacks trigger phrase ❌ ANTI-PATTERN
The methodology requires: *"Contains role AND usage trigger ('Use when...')"*. The current description is purely descriptive — it says what the agent *is* and *does*, but not when the system should invoke it. Example pattern: "Contextual analyst for the email vault. Use when emails need to be read, threaded, and enriched with context from the vault."

### 3. Decorative personality? ✅ NOT DETECTED
Tone description (analytical, curious, precise) is consistently reflected in the methodical step-by-step workflows and explicit operating rules.

### 4. Vague limitations? ✅ NOT DETECTED
All 7 limitations are specific and actionable.

### 5. Process without steps? ✅ NOT DETECTED
The main workflow is a model of step-by-step clarity with input/output.

### 6. Competency list without context? ✅ NOT DETECTED
Competencies are domain-organized with context.

### 7. Custom frontmatter fields? ✅ NOT DETECTED
Only standard fields present.

---

## E. Additional observations

### Section ordering mismatch
The 10-section methodology expects: frontmatter → header → identity → communication → rules → competencies → workflows → interactions → limitations → references. The current file order is: frontmatter → header/identity → communication → rules → competencies → workflows → output examples → vault structure → interactions → limitations → guiding principles. This doesn't match the canonical order. The "Interactions" section appears after "Email Vault Structure" instead of before "Limitations."

### Redundant sections
- `## Who I Am` (line 13) and `## Identity` (line 21) cover the same ground. The methodology expects a single header comment (2-3 lines) followed by a 2-4 sentence Identity block. The current file has three overlapping blocks: lines 10-12 (title), lines 13-19 (Who I Am), lines 21-23 (Identity).
- `## Guiding Principles` (line 239) is a bonus section not in the methodology. Not necessarily harmful but adds length.

### Permission mismatch
- Agent has `bash: ask` but limitations say "Do not write Python code" and "Do not use external APIs"
- Agent creates files (Review/summaries/, Review/actions.md) but lacks `write` permission (only `edit: allow`)
- Methodology recommends `read`, `write`, `websearch`, `webfetch` for research/analysis roles — none of these are fully present

---

## Priority Recommendations

| Priority | Issue | Severity | Action required |
|----------|-------|----------|-----------------|
| **P1** | Member name references (7 occurrences) | **Critical** — explicit anti-pattern | Rewrite interactions table without member names (e.g., "Orchestrator" instead of "Hermes", "Tool pipeline" instead of "Efesto"). Replace references in limitations and communication style with role-based descriptions. |
| **P1** | Missing References section | **High** — mandatory per methodology | Add `## References` section listing: Library/SOPs/agent-design-methodology.md, Library/SOPs/handoff-guide.md, Library/SOPs/obsidian-vault-conventions.md |
| **P2** | Description: 293 chars (over limit) + missing trigger phrase | **High** — affects system invocation | Rewrite to ~150-200 chars. Add "Use when" trigger. Maintain operational specificity. |
| **P2** | Permission mismatch (`bash:ask` not needed, `write` missing) | **Medium** — operational correctness | Remove `bash: ask`. Add `write: allow`. Consider adding `websearch`/`webfetch` if the role could benefit from external lookups (currently says "no external APIs" so likely intentional omission). |
| **P3** | Section ordering and redundancy (`Who I Am` vs `Identity`) | **Low** — style/consistency | Merge `## Who I Am` into a proper header comment block. Keep `## Identity` as the mission statement. |
| **P3** | Header not in comment format | **Low** — deviation from methodology | Consider wrapping the header block in an HTML comment (`<!-- ... -->`) for human readability as specified. |
