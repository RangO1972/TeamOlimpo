---
title: "Handoff — Agent Output Specification & Procedure"
aliases: [handoff-guide, handoff]
tags: [sops, handoff, workflow]
---

# Handoff — Agent Output Specification & Procedure

## Rule

Every agent invocation **must** end by writing one handoff file before returning control to Hermes. No exceptions.

---

## How to Create a Handoff

Use the `handoff_create` MCP tool with these parameters:

| Parameter | Required | Notes |
|-----------|----------|-------|
| `type` | ✅ | See [Valid types](#valid-types) |
| `title` | ✅ | Max 60 characters |
| `body` | ✅ | Free Markdown content |
| `agent` | ✅ | Lowercase agent name (e.g. `efesto`, `proteo`) |
| `task_id` | — | Assigned by Hermes at task start (e.g. `T-042`) |
| `completion_notes` | — | What was done, deviations, operational notes |
| `status` | — | `completed` or `blocked`. Default: `completed` |
| `priority` | — | `high` / `medium` / `low`. Default: `medium` |
| `output_refs` | — | File paths to artifacts produced |
| `deviation` | — | See [Deviation block](#deviation-block) |

**Do not set**: `date`, `timestamp`, `agent` in the body — the tool adds these automatically.

---

## Valid Types

| Type | Content |
|------|---------|
| `report` | Completed operation results, statistics |
| `profile` | Competency profile for a role or AI agent |
| `spec` | Technical specification, design decision |
| `test` | Test scenarios, acceptance criteria |
| `analysis` | Research output, strategic analysis |
| `note` | Non-actionable information, announcements |
| `bug` | Bug detected during execution — routes to Efesto |
| `feedback` | Non-bug quality signal: limitation, degradation |

---

## Valid Statuses

| Status | Who | When |
|--------|-----|------|
| `completed` | Agent | Invocation finished with usable output |
| `blocked` | Agent | Unresolvable blocker — output absent or partial |
| `cancelled` | **Hermes only** | Never write this yourself |

**Rules:**
- `status: blocked` → `next_action` is **required**
- `deviation.outcome == 'open'` → `status` must be `blocked`

---

## `next_action`

One sentence addressed to Hermes. Required when `status: blocked`.

```yaml
# Route to specialist
next_action: "Hermes: suggest delegating encoding fix to Efesto before resuming T-042"

# Return to user
next_action: "Output ready for user. No further action needed."

# Blocked with recovery hint
next_action: "Hermes: blocked on missing loguru — requires Efesto fix before T-038 can resume"
```

---

## `quality_score`

Self-assessed by the producing agent.

| Score | Meaning |
|-------|---------|
| 1 | Unusable output |
| 2 | Partial or significantly flawed |
| 3 | Functional but improvable |
| 4 | Meets expectations |
| 5 | Exceeds expectations |

---

## `deviation` Block

Include when execution hit a blocker, error, or incomplete output.

```yaml
deviation:
  type: "tool_failure | output_incomplete | missing_input | other"
  description: "brief description"
  cause: "identified cause"
  corrective_action: "what was done to resolve"
  outcome: "resolved | workaround | open"
  user_impact: false
```

If `outcome: open` → `status: blocked` is mandatory.

---

## Examples

### A — Standard completed report (MCP tool)

```yaml
# handoff_create call:
type: report
title: "Fixed loguru import in pdf_converter"
body: "47/50 files converted. 3 skipped: encoding issue in nk-2400-*.md."
agent: efesto
task_id: T-042
completion_notes: "Added loguru to pyproject.toml, all tests pass"
```

### B — Blocked with bug (MCP tool)

```yaml
# handoff_create call:
type: bug
title: "ModuleNotFoundError: loguru in pdf_converter"
body: "See deviation block for details."
agent: clio
status: blocked
priority: high
next_action: "Hermes: blocked on missing dependency — delegate fix to Efesto before T-038 resumes"
deviation:
  type: "tool_failure"
  description: "ModuleNotFoundError: No module named 'loguru'"
  cause: "Missing dependency in requirements.txt"
  corrective_action: "None — operation halted, requires Efesto"
  outcome: "open"
  user_impact: true
```



## Tool Reference

Full CLI usage (`list`, filters, `--json`, `--paths`): `Library/Meta/tools/handoff/guide.md`
