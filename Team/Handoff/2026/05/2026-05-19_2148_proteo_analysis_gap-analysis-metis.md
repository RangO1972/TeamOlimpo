---
date: 2026-05-19
timestamp: 2026-05-19T21:48:16
agent: proteo
task_id: T-000
invocation: 1
type: analysis
status: completed
priority: high
title: "Gap analysis — Metis profile vs agent design methodology"
quality_score: 4
next_action: "Hermes: pass to Atena for Metis profile redesign following the recommendations below"
---

# Gap Analysis: Metis Profile

## Synthetic Verdict

**Substantial revision needed** — the profile is functionally rich and operationally sound, but structurally incomplete against the agent design methodology: it is missing 3 of 10 sections (header comment, interactions, references), has member name references in the description and identity, an inappropriate `task` permission, and incorrect section ordering.

---

## Structure Check

### Methodology Reference (10 sections)

| # | Section | Methodology status | Metis status | Lines |
|---|---------|-------------------|--------------|-------|
| 1 | Frontmatter | Mandatory | ✅ Present (description, mode, model, permission) | 1-9 |
| 2 | Header comment | Mandatory | ❌ **Missing** | — |
| 3 | Identity | Mandatory | ✅ Present as `## Identity` | 13-17 |
| 4 | Communication style | Mandatory | ✅ Present as `## Style` | 21-26 |
| 5 | Operating rules | Mandatory | ✅ Present as `## Rules` | 30-46 |
| 6 | Competencies | Mandatory | ✅ Present as `## Skills` (should be "Competencies") | 50-58 |
| 7 | Workflows | Mandatory | ✅ Present as `## Workflow` | 62-88 |
| 8 | Interactions | Optional (good practice) | ❌ **Missing** | — |
| 9 | Limitations | Mandatory | ✅ Present as `## Limits` | 92-98 |
| 10 | References | Optional | ❌ **Missing** (handoff guide mentioned inline but no dedicated section) | 78 mentions handoff guide inline |

**6 mandatory sections present**: 5 ✅ — **header comment missing** ❌

### Section Order Comparison

| Methodological order | Current Metis order |
|---------------------|-------------------|
| Frontmatter | ✅ Frontmatter |
| Header comment | ❌ Missing |
| Identity | ✅ Identity |
| Communication style | ✅ Style |
| Operating rules | ✅ Rules |
| Competencies | ✅ Skills |
| Workflows | ✅ Workflow |
| Interactions | ❌ Missing |
| Limitations | ✅ Limits |
| References | ❌ Missing |
| — | Extra: Summary format (lines 102-128) |

---

## Issues Found (priority order)

### Issue 1 — Header comment missing (High severity)
**Location**: after frontmatter (line 9), before `## Identity` (line 13)
**Detail**: The methodology mandates a 2-3 line header comment as section 2 — a human-readable statement of who the agent is, what they do, and what they don't do. The profile jumps directly from frontmatter into `## Identity`.
**Recommendation**: Add a header comment block between line 9 and line 13, e.g.:
```
# Metis — Thinking Partner & Strategist

Thinking partner for brainstorming, strategic reflection, and complex problem-solving.
Does NOT execute tasks, write code, or produce generic documents.
```

---

### Issue 2 — Member name reference in `description` field (High severity)
**Location**: Line 2, frontmatter `description`
**Current text**: `"Thinking partner for strategic brainstorming and flow optimization. Use for critical thinking sessions with the user or as a subagent delegated by Hermes. Creates Markdown summaries on request."`
**Problem**: The methodology explicitly states: *"Never mention specific team member names"* in the description field. "Hermes" appears here.
**Recommendation**: Rewrite description without member names:
> `Thinking partner for strategic brainstorming and flow optimization. Use for critical thinking sessions with the user or as a delegated subagent. Creates Markdown summaries on request.`
(This also keeps it within ~150-200 chars.)

---

### Issue 3 — Inappropriate `task` permission (High severity)
**Location**: Line 8, frontmatter `permission`
**Current**: `task: allow`
**Problem**: Per the methodology permission table, `task` = agent delegation — only for orchestrators or collaborators. Metis is neither. Metis receives task delegations (from Hermes) but does not delegate to other agents. Granting `task` could allow Metis to spawn subagents, which is outside its role.
**Recommendation**: Remove `task: allow`. The correct permission set based on Metis's role (thinking partner / strategic analyst) is `read: allow`, `write: allow` (for summaries and handoffs). Research tools (`websearch`, `webfetch`) are not needed unless the brief specifies otherwise, since Metis works from internal knowledge and conversation.

---

### Issue 4 — Member name references in Identity section (Medium severity)
**Location**: Line 15, `## Identity`
**Current text**: `"...specialized subagent Hermes delegates for internal process optimization and member creation reviews."`
**Problem**: The methodology's anti-pattern 6 states: *"agent files must not reference other team members by name. The orchestrator manages routing."* Identity mentions Hermes explicitly.
**Recommendation**: Reframe without naming:
> `"...specialized subagent for internal process optimization and member creation reviews."`
The routing mechanism (who delegates to whom) is Hermes's concern, not encoded in the profile.

---

### Issue 5 — Member name references in Workflows (Medium severity)
**Location**: Lines 66, 68, 73
**Current text**:
- Line 66: `"When Hermes delegates a review..."`
- Line 68: `"Hermes passes path of a type:profile handoff from Proteo."`
- Line 73: `"Hermes passes path of a type:profile handoff from Atena."`
**Problem**: Same anti-pattern — member names in agent file.
**Recommendation**: Replace "Hermes" with "The orchestrator" or "Delegation" or simply describe the input ("When a review is delegated..."). Example:
- `"When delegated a member creation review, operate as independent evaluator — not thinking partner."`
- `"Receive a type:profile handoff."`

---

### Issue 6 — Missing Interactions section (Medium severity)
**Location**: Missing entirely (between Workflows and Limitations)
**Detail**: The methodology includes an optional but recommended "Interactions" section (section 8): direction (receive/produce) and format. While the workflows implicitly describe interactions, a dedicated section would clarify I/O patterns.
**Recommendation**: Add an `## Interactions` section:
```markdown
## Interactions

**Receive:**
- Brainstorming requests from user (free-form conversation)
- Delegated reviews from orchestrator (handoff file path)

**Produce:**
- Brainstorming summaries → `Library/deliverables/brainstorming-summary-YYYY-MM-DD.md`
- Analysis handoffs → `Library/Handoff/YYYY/MM/<filename>.md`
```

---

### Issue 7 — Missing References section (Medium severity)
**Location**: Missing entirely (end of file)
**Detail**: Section 10 of the methodology. Line 78 references `Library/SOPs/handoff-guide.md` inline but there is no dedicated `## References` section at the end.
**Recommendation**: Add at the end:
```markdown
## References

- `Library/SOPs/handoff-guide.md` — Handoff file format
- `Library/SOPs/agent-design-methodology.md` — Agent profile design standard
- `Library/SOPs/obsidian-vault-conventions.md` — Vault conventions
```

---

### Issue 8 — Section naming: "Skills" vs "Competencies" (Low severity)
**Location**: Line 50, `## Skills`
**Problem**: The methodology names section 6 "Competencies". The current profile uses "Skills." This is a minor naming inconsistency.
**Recommendation**: Rename `## Skills` → `## Competencies` to match the standard.

---

### Issue 9 — Thinking Partner Workflow Step 2 is abstract (Low severity)
**Location**: Lines 85-86, step 2 of the thinking partner flow
**Current text**: `"Facilitate thinking — apply inquiry design and structural listening. Cycle: Welcome → Explore → Challenge → Structure → Activate."`
**Problem**: While not a full anti-pattern (the workflow has numbered steps), step 2 lacks explicit input/output definition. The methodology requires: *"Each step needs input, action, output."*
**Recommendation**: Make the I/O explicit:
> 2. **Facilitate thinking** — Input: user's current problem/status. Action: apply inquiry design and structural listening through cycle (Welcome → Explore → Challenge → Structure → Activate). Output: clarified problem space, decisions, or session notes.

---

### Issue 10 — "Summary format" is an extra section outside the 10-section template (Low severity)
**Location**: Lines 102-128, `## Summary format`
**Problem**: This is useful content but doesn't map to any of the 10 sections. If kept, it should be integrated into a reference or into the interactions section.
**Recommendation**: Move the summary format template into a `## References` section or into the `## Interactions` section as a specification of the output format. Alternatively, keep it but rename to match an allowed section.

---

## Strengths

What works well and should be preserved:

1. **Description is operational and unique** — "Thinking partner for strategic brainstorming and flow optimization" clearly distinguishes Metis from all other team members. Only the member name reference needs fixing.

2. **Style section is well-calibrated** — tone, rhythm, language, and length rules are specific and actionable. Not decorative, since the Rules section backs them up with concrete operating principles.

3. **Rules section is excellent** — "What you are / What you are not / Operating principles" is a clear tripartite structure with non-negotiable constraints. Each principle has an operational consequence.

4. **Competencies have rich context** — each skill (inquiry design, structural listening, reframing, etc.) comes with a description of *how* it is applied and *when*. Not a flat list.

5. **Limitations are specific** — explicit boundaries on file creation, artifact types, encyclopedic responses, and premature structure. No vague "don't do things outside your scope."

6. **Workflow 0 (member creation flow) is well-structured** — clear input (path), action (evaluate with guide questions), and output (handoff with specific structure).

7. **No decorative personality** — the tone descriptions in Style are supported by concrete rules and principles.

---

## Recommendations for Atena

### Mandatory (blocking redesign):

| # | Action | Rationale |
|---|--------|-----------|
| R1 | **Add header comment** between frontmatter and Identity | Section 2 of the methodology, mandatory. 2-3 lines. |
| R2 | **Remove "Hermes" from description** field (line 2) | Methodology rule: no member names in description. |
| R3 | **Remove `task: allow`** from permissions (line 8) | Metis does not delegate to other agents. |
| R4 | **Remove "Hermes" from Identity** (line 15) | Anti-pattern 6: no member names in agent files. |
| R5 | **Remove "Hermes" (and "Proteo", "Atena") from Workflows** (lines 66, 68, 73) | Same anti-pattern. Replace with "orchestrator" or "delegation source." |

### Recommended (structural completeness):

| # | Action | Rationale |
|---|--------|-----------|
| R6 | **Add `## Interactions` section** after Workflows | Recommended section 8. Clarifies receive/produce patterns. |
| R7 | **Add `## References` section** at end of file | Section 10. List SOPs and methodology docs. |
| R8 | **Rename `## Skills` → `## Competencies`** | Align with methodology naming (section 6). |
| R9 | **Make thinking partner flow Step 2 I/O explicit** | Each workflow step needs input, action, output per methodology. |

### Optional (polish):

| # | Action | Rationale |
|---|--------|-----------|
| R10 | **Reintegrate Summary format** into Interactions or References | It's useful content that doesn't fit the 10-section model as a standalone section. |
| R11 | **Reorder sections** to match methodology order | Cosmetic but reduces friction for future audits. Order: Frontmatter → Header → Identity → Style → Rules → Competencies → Workflows → Interactions → Limitations → References. |

---

## Anti-patterns Detected

| Anti-pattern | Status | Detail |
|---|---|---|
| Decorative personality | ✅ **Clean** | Style descriptions backed by concrete Rules |
| Vague limitations | ✅ **Clean** | Limits are explicit and specific |
| Process without steps | ✅ **Clean** (minor) | Workflows have numbered steps with I/O. Only Step 2 of thinking partner flow could be more explicit. |
| Competency list without context | ✅ **Clean** | Each skill has operational description |
| Custom frontmatter fields | ✅ **Clean** | Only standard fields (description, mode, model, permission) |
| **Member name references** | ❌ **PRESENT** | Lines 2, 15, 66, 68, 73 — "Hermes" appears in description, identity, and workflow sections. Line 68 mentions "Proteo", line 73 mentions "Atena". |

**Total anti-patterns: 1 active** (member name references).

---

## Information Gaps

- The methodology does not explicitly forbid member name references in workflow steps when describing delegation flow. The anti-pattern says "agent files must not reference other team members by name." I have interpreted this broadly. Atena should confirm whether workflow-level references to orchestrator are acceptable or must be fully abstracted.
- The `summary format` section (lines 102-128) is not accounted for in the 10-section model. It may be intentionally preserved as a "bonus" section or absorbed elsewhere.
