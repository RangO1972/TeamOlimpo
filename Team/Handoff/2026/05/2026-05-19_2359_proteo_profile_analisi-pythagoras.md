---
data: 2026-05-19
timestamp: 2026-05-19T23:59:00
agent: proteo
task_id: T-UNASSIGNED
invocation: 1
type: profile
status: completed
priority: high
title: "Domain analysis Pythagoras — structural profile for EN translation"
completion_notes: >
  Full structural mapping of `.opencode/agents/pythagoras.md` (80 lines).
  Body is already 100% EN — only frontmatter description and H1 title are in IT.
  One critical finding: Calliope referenced at line 29 is NOT in AGENTS.md (outdated reference).
  Language directive line 71 says "Use Italian" → must become "Always reply in English".
  Role expansion from STEM to ALL disciplines identified in 3 key locations.
  Ready for Hermes to delegate translation/update to Atena.
output_refs:
  - .opencode/agents/pythagoras.md
  - AGENTS.md
  - Library/SOPs/agent-design-methodology.md
quality_score: 5
external_review: false
next_action: "Hermes: low-complexity task. Pythagoras body already in EN. Delegate EN frontmatter fix + role expansion + member name generalization to Atena with this analysis as input."
---

# Profile analysis: Pythagoras — Structural Domain Mapping

## 1. File metadata

| Field | Value |
|-------|-------|
| Path | `.opencode/agents/pythagoras.md` |
| Total lines | 80 |
| Body language | **100% English** (lines 14–80) |
| Italian content | Frontmatter `description` (line 2) + H1 title (line 12) |
| Current role title | "Ricercatore Web Scolastico" |
| Current role scope | STEM-only (math, chemistry, history, science) |
| Target scope | **ALL disciplines** (sciences, humanities, economics, philosophy, etc.) |
| Model | `opencode/big-pickle` |
| Mode | `subagent` |

---

## 2. Complete structural map

```
┌─ YAML Frontmatter (lines 1-10)
│   ├─ description       → IT ✓ (line 2: "Ricercatore Web Scolastico specializzato...")
│   ├─ mode              → EN ✓ (subagent)
│   ├─ model             → EN ✓ (opencode/big-pickle)
│   └─ permission        → EN ✓ (read, webfetch, websearch, write)
│
├─ H1 # Pythagoras — Ricercatore Web Scolastico (line 12)
│   → IT → EN: "Pythagoras — Academic Web Researcher, Team Olimpo"
│
├─ ## Core Identity (lines 14-20)
│   → EN ✓ (already in English)
│   → Line 18: "Role: Web Research Specialist focused on scholastic and academic topics"
│     — currently broad enough, but may need ALL-discipline emphasis
│
├─ ## What You Do (lines 22-26)
│   → EN ✓
│   → Line 23: contains STEM-limited examples: "mathematics, chemistry, history"
│     ★ NEEDS UPDATE: expand to include ALL disciplines
│
├─ ## What You Don't Do (lines 28-32)
│   → EN ✓
│   → Line 29: "delegate to Calliope" ★ CALLIOPE is NOT in AGENTS.md — outdated reference
│   → Line 30: "delegate to Efesto or the requester" — mentions member name
│   → Line 32: "operate on delegation from Hermes" — mentions member name
│
├─ ## Skills and Competencies (lines 34-38)
│   → EN ✓ — 4 skills, no discipline limitation
│
├─ ## Operational Instructions (lines 40-52)
│   → EN ✓
│   → Line 41: "request clarification from Hermes" — member name
│   → Line 44: "authoritative sources (universities, research institutes, Wikipedia, digital libraries)"
│     — good general sources, could add humanities-specific sources
│   → Line 52: "ready for review by Clio or delivery to the user" — member name
│
├─ ## Output Format (lines 54-65)
│   → EN ✓ — Markdown template with EN frontmatter keys
│   → No Italian keys — unlike Euterpe, this output is already EN-formatted
│
├─ ## Interaction Guidelines (lines 67-71)
│   → EN ✓
│   → Line 71: "Use Italian for all communications, as per team standards."
│     ★ LANGUAGE DIRECTIVE — must change to "Always reply in English."
│
└─ ## Available Tools (lines 73-80)
    → EN ✓ — tools list, no changes needed
```

---

## 3. Content to translate (IT → EN): full inventory

**Key finding: Only 2 elements need translation from Italian.**

| Section | Lines | Current IT | Current length | Complexity |
|---------|-------|------------|----------------|------------|
| YAML `description` | 2 | `Ricercatore Web Scolastico specializzato in ricerca accademica e scientifica. Trasforma informazioni web in note strutturate per il vault Obsidian.` | ~160 char | Low — concise, technical |
| H1 Title | 12 | `# Pythagoras — Ricercatore Web Scolastico` | 1 line | Low — role title |

**Everything else (lines 14–80) is already in English.** This profile is 97.5% English already.

---

## 4. Critical language instruction (MUST change semantics)

### 4a. Current directive (line 71)
```markdown
**Original:** "Use Italian for all communications, as per team standards."
```
→ **Must become:** "Always reply in English."
→ Reason: After translation, Pythagoras's operating language should be English (like Metis, Clio, and all other EN profiles).

⚠️ **Note**: Unlike Euterpe (whose output must remain in Italian because she writes Italian school essays), Pythagoras produces structured research notes in English for the vault. The language directive change is straightforward.

---

## 5. Role expansion: STEM → ALL disciplines

### 5a. AGENTS.md (line 118-122)
Current:
```
**pythagoras** — Academic Web Researcher
- Trigger: scholastic/academic/scientific web research (math, chemistry, history, science)
  → produces structured vault notes; *feeds Euterpe with sources for essays*
```
**Change needed:** Expand trigger examples to cover ALL disciplines:
```
- Trigger: scholastic/academic web research across all disciplines (sciences, 
  humanities, economics, philosophy, history, literature, arts) → produces 
  structured vault notes; feeds Euterpe with sources for essays
```

### 5b. Profile — "What You Do" (line 23)
Current:
```
Conduct targeted web research on scholastic, academic, and scientific topics 
(e.g., mathematics, chemistry, history).
```
**Change needed:** Broaden examples:
```
Conduct targeted web research on scholastic and academic topics across all 
disciplines (e.g., mathematics, literature, chemistry, philosophy, history, 
economics, biology, arts).
```

### 5c. Profile — Role title (line 18)
Current:
```
Role: Web Research Specialist focused on scholastic and academic topics
```
**Assessment:** This is already broad enough. Optional: add "across all disciplines" for emphasis.

### 5d. Profile — Source types (line 44)
Current:
```
authoritative sources (universities, research institutes, Wikipedia, digital libraries)
```
**Consider adding:**
```
authoritative sources (universities, research institutes, Wikipedia, digital libraries, 
academic databases, archives, institutional repositories)
```
→ Humanities and social sciences rely on different source types (archives, databases like JSTOR/Scopus, institutional repositories).

### 5e. AGENTS.md — "Strong" and "NON lui" sections (lines 120-121)
Current:
```
- Strong: multi-source credibility filtering, structured Obsidian-ready notes, 
  institutional/encyclopedic source prioritization
- NON lui: essays or theses (→ Euterpe), code/automation (→ Efesto), 
  professional domain mapping (→ Proteo)
```
**Assessment:** Both are already discipline-agnostic. The "Strong" section describes methodology, not domain. The "NON lui" section correctly delegates to other members. No changes needed.

---

## 6. Member name references inventory

| # | Line | Member | Context | SOP says generalize? | Action |
|---|------|--------|---------|---------------------|--------|
| 1 | 29 | **Calliope** 🚩 | "delegate to Calliope" — for essays/theses | **N/A — NOT in AGENTS.md** | **CRITICAL OUTDATED REFERENCE.** Calliope is not a current AGENTS.md member. The current flow (AGENTS.md line 121) says essays → Euterpe. **Recommendation:** generalize to "delegate to the essay writer" or update to Euterpe if keeping specific names, but SOP says no names. |
| 2 | 30 | **Efesto** | "delegate to Efesto or the requester" — for code | Should generalize | Replace with "delegate to the developer" |
| 3 | 32 | **Hermes** | "operate on delegation from Hermes" | Should generalize | Replace with "operate on delegation from the orchestrator" |
| 4 | 41 | **Hermes** | "request clarification from Hermes" | Should generalize | Replace with "request clarification from the orchestrator" |
| 5 | 52 | **Clio** | "ready for review by Clio or delivery to the user" | Should generalize | Replace with "ready for QC review or delivery to the user" |

**Total: 5 references · 4 unique members · 1 outdated (Calliope)**

**SOP compliance note:** `agent-design-methodology.md` lines 45–46 and 79 state: *"Never mention specific team member names"* and *"agent files must not reference other team members by name."*

**Recommendation:** Generalize ALL 5 references. No member names should appear in the EN profile.

---

## 7. Output format template analysis

The current Markdown template (lines 54–65) uses **English frontmatter keys**:
```yaml
---
title: "[Topic]"
date: YYYY-MM-DD
tags: [school, research, pythagoras]
source: "Web Research"
---
```

✅ **No Italian keys to preserve.** This is a clean EN template. No changes needed, unlike Euterpe where Italian keys had to stay.

**Minor recommendation:** Update the `tags` to include discipline-specific tags, e.g., `[research, pythagoras, sciences]` or `[research, pythagoras, humanities]` — but this can be handled as part of the role expansion.

---

## 8. Sections needing structural rework (not just translation)

| # | Section | Issue | Recommended action |
|---|---------|-------|-------------------|
| 1 | YAML `description` (line 2) | In Italian, ~160 char, STEM-specific | Rewrite in EN (~150-200 char) covering ALL disciplines, operational trigger |
| 2 | H1 Title (line 12) | "Ricercatore Web Scolastico" → narrow | "Pythagoras — Academic Web Researcher, Team Olimpo" |
| 3 | `## What You Do` (line 23) | STEM-only examples | Expand examples to cover ALL disciplines |
| 4 | `## What You Don't Do` (line 29) | Calliope reference outdated | Generalize: remove Calliope, delegate to "essay writer" |
| 5 | `## Interaction Guidelines` (line 71) | Language directive says "Use Italian" | Change to "Always reply in English." |
| 6 | All sections with member names | 5 member references to generalize | Replace with role descriptors (orchestrator, developer, QC) |
| 7 | Missing header comment | Profile has no 2-3 line header after H1 | Add per SOP `agent-design-methodology.md` (standard: 2 lines: who + what NOT) |

### 8a. Missing header comment

Following the Metis and SOP standard, add a header comment after the H1 title:

```markdown
Academic web researcher covering all school and university disciplines.
Does NOT write essays, develop code, or perform professional domain analysis.
```

---

## 9. Recommended frontmatter description (EN)

Following `agent-design-methodology.md` rules:
- Contains role AND usage trigger ("Use when...")
- Operational, not poetic
- ~150-200 chars
- Uniquely distinguishes from all other agents
- No member names

**Proposed:**
```yaml
description: >
  Academic web researcher for all school and university disciplines. Use when 
  structured, source-based research is needed across sciences, humanities, 
  or social sciences. Produces Obsidian-ready Markdown notes with verified sources.
```

**Character count:** 196 — within the ~150-200 target.
**Trigger is implicit:** "Use when structured, source-based research is needed" clearly signals invocation.
**Distinct from Proteo:** Proteo does "professional domain mapping" and "competency analysis" — Pythagoras does "school/university discipline research with verified sources."

---

## 10. Complexity estimation

| Factor | Rating | Notes |
|--------|--------|-------|
| Total lines | 80 | Small file — smallest profile in team after Proteo (76) |
| % in Italian | ~2.5% | Only frontmatter description + H1 title |
| % that must stay unchanged | ~90% | Body is already EN, paths are EN, template is EN |
| Translation work | **Very Low** | 2 elements to translate (description + title) |
| Role expansion impact | **Medium** | 3 locations to update (AGENTS.md, profile line 23, line 44) |
| Member references to generalize | 5 | Including 1 outdated (Calliope → not in AGENTS.md) |
| Language directive change | 1 | Line 71: "Use Italian" → "Always reply in English" |
| Structural changes | Low | Add header comment (2 lines after H1) |
| Cultural adaptation | **None** | No Italian-specific cultural references |

### Overall: **LOW** (3/10)

Breakdown:
- Pure translation work: 1/10 (2 elements, ~20 words total)
- Role expansion integration: 4/10 (requires judgment on where ALL disciplines appear)
- Calliope resolution: 3/10 (just generalize, no structural impact)
- Member name generalization: 2/10 (5 substitutions)
- Language directive change: 1/10 (single line)
- Missing header comment: 1/10 (add 2 lines)

**Estimated time for Atena:** 10–15 minutes. This is the fastest profile update in the team.

---

## 11. Specific edge cases and recommendations

### Edge case 1 — Calliope reference (line 29)
```
Original: "Do not write complex essays or theses: your task is data collection and 
structuring, not creative composition (delegate to Calliope)."
```
**Issue:** Calliope is NOT listed in AGENTS.md as a current team member. The current delegation flow (AGENTS.md line 121) routes essays/theses to **Euterpe**.

**Three options:**
| Option | Action | Risk |
|--------|--------|------|
| **A — Generalize (RECOMMENDED)** | Replace with "delegate to the essay writer" | Aligns with SOP (no member names), avoids stale references |
| **B — Update to Euterpe** | Replace Calliope with Euterpe | Creates a member name reference (violates SOP); also Euterpe might change in future |
| **C — Remove entirely** | Just say "your task is data collection and structuring, not creative composition" | Cleanest but loses routing signal for Hermes |

**Recommendation: Option A** — generalize. The section title "What You Don't Do" is about capability boundaries, not routing instructions. Hermes handles routing.

### Edge case 2 — Discipline breadth in "Strong" vs "Trigger"
The AGENTS.md entry for Pythagoras has a strong STEM bias ("math, chemistry, history, science") but in practice Pythagoras should handle ALL subjects. The `Strong` field in AGENTS.md (line 120) mentions methodology (credibility filtering, note structuring) — already discipline-agnostic. The fix is **only** in the `Trigger` line (119).

### Edge case 3 — Profile body already in EN
Unlike Euterpe (100% IT), Clio (~90% IT), and Dike (~90% IT), Pythagoras's profile body is already in fluent English. This is likely because Pythagoras was created or updated after the team started transitioning to EN. **No risk of inconsistent voice.**

### Edge case 4 — Tool list (lines 73-80)
The "Available Tools" section lists `grep` but NOT `glob`, `edit`, or `skill`. This is fine for a research subagent, but worth noting for completeness. The Metis profile only lists `read` and `write` — so tool lists are already minimal and role-appropriate.

**Recommendation:** No change needed. The tool set matches Pythagoras's research-only role.

### Edge case 5 — Output format `tags` (line 61)
Current tags: `[school, research, pythagoras]`

For the expanded role, consider whether the tags should remain generic (`school, research, pythagoras`) or adopt discipline-specific tags dynamically. Since Pythagoras produces documents for the vault, discipline tags would make content more findable.

**Recommendation:** Keep `tags` dynamic per document. The template is fine as-is — tags are populated per research topic, not hardcoded.

---

## 12. Summary for Atena (translation brief)

| Item | Instruction |
|------|-------------|
| **Role title** | Change from "Ricercatore Web Scolastico" to "Academic Web Researcher" |
| **Role scope** | Expand from STEM-only to ALL school/university disciplines |
| **Profile language** | Frontmatter description → EN. Body is already EN. |
| **H1 title** | `# Pythagoras — Academic Web Researcher, Team Olimpo` |
| **Header comment** | Add 2 lines after H1 (who + what NOT) per SOP standard |
| **Language directive** | Line 71: change "Use Italian" → "Always reply in English." |
| **Output language** | English (already the default in the template) |
| **Output template** | No changes needed — already EN keys |
| **Member names** | Generalize ALL 5 references: Calliope → "essay writer", Efesto → "developer", Hermes → "orchestrator" (×2), Clio → "QC reviewer" |
| **Calliope reference** | **CRITICAL OUTDATED REFERENCE.** Current delegation flow is to Euterpe, not Calliope (not in AGENTS.md). Generalize. |
| **Section about sources** | Line 44: consider adding humanities-specific sources (academic databases, archives) |
| **Discipline examples** | Line 23: expand beyond "math, chemistry, history" to include literature, philosophy, economics, arts, etc. |
| **Section structure** | Maintain same sections. Add header comment. No reordering needed. |
| **Mythological identity** | Preserve "philosopher of measure and order" and Pythagorean archetype — both are already in English (lines 14-19) |
| **No emojis** | As per Team Olimpo conventions |

---

## 13. Quick-reference: before / after table

| Element | Before (IT) | After (EN) |
|---------|------------|------------|
| Frontmatter `description` | `Ricercatore Web Scolastico specializzato in ricerca accademica e scientifica...` | `Academic web researcher for all school and university disciplines...` |
| H1 title | `# Pythagoras — Ricercatore Web Scolastico` | `# Pythagoras — Academic Web Researcher, Team Olimpo` |
| Header comment | ❌ Missing | ✅ Add: "Academic web researcher covering all disciplines. Does NOT write essays, develop code, or perform professional domain analysis." |
| Role scope (line 23) | STEM: "mathematics, chemistry, history" | ALL: "mathematics, literature, chemistry, philosophy, history, economics, biology, arts" |
| Language directive (line 71) | "Use Italian for all communications" | "Always reply in English." |
| Member names | Hermes (×2), Efesto, Clio, Calliope | All generalized to roles |
| Calliope (line 29) | "delegate to Calliope" | "delegate to the essay writer" |
| Source types (line 44) | "universities, research institutes, Wikipedia, digital libraries" | Same + "academic databases, archives, institutional repositories" |
| AGENTS.md trigger | "math, chemistry, history, science" | All disciplines listed generically |
| Output template | EN keys ✅ (no change) | EN keys ✅ (no change) |
| Tools section | webfetch, grep, write, read | ✅ No change |
