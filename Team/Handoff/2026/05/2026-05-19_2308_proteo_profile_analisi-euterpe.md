---
data: 2026-05-19
timestamp: 2026-05-19T23:08:00
agent: proteo
task_id: T-UNASSIGNED
invocation: 1
type: profile
status: completed
priority: high
title: "Domain analysis Euterpe — structural profile for EN translation"
completion_notes: >
  Full structural mapping of `.opencode/agents/euterpe.md` (168 lines).
  All IT content identified. Member references counted. Complexity estimated.
  Ready for Hermes to delegate translation/update to Atena.
output_refs:
  - .opencode/agents/euterpe.md
quality_score: 5
external_review: false
next_action: "Hermes: delegate EN translation + role update of Euterpe profile to Atena, with this analysis as input"
---

# Profile analysis: Euterpe — Structural Domain Mapping

## 1. File metadata

| Field | Value |
|-------|-------|
| Path | `.opencode/agents/euterpe.md` |
| Total lines | 168 |
| Current language | 100% Italian (profile instructions) |
| Output language | Italian (temi/saggi per scuole) |
| Current role title | "Scrittrice di Temi Italiano" |
| Target role title | "Essay & Theme Writer (Italian School)" |
| Model | `opencode/big-pickle` |
| Mode | `subagent` |

---

## 2. Complete structural map

```
┌─ YAML Frontmatter (lines 1-10)
│   ├─ description       → IT ✓ (needs EN translation + role update)
│   ├─ mode              → EN ✓
│   ├─ model             → EN ✓
│   └─ permission        → EN ✓
│
├─ H1 # Euterpe — Scrittrice di Temi Italiano (line 12)
│   → Needs EN: "Euterpe — Essay & Theme Writer (Italian School)"
│
├─ ## Identità (lines 14-16)
│   → Full IT. Describes Euterpe as Muse of lyric poetry turned essay writer.
│     Must be translated to EN while preserving the mythological identity.
│
├─ ## Personalità e stile di comunicazione (lines 18-24)
│   → Full IT. 5 bullet points (tone, rhythm, attitude, language, + line 24).
│   → Line 24: "Rispondi sempre in italiano." ← CRITICAL: this is profile
│     language instruction for OUTPUT. Must be preserved in EN version.
│
├─ ## Regole operative fondamentali (lines 26-33)
│   → Full IT. 6 numbered rules.
│   → Rule 6 (line 33): "Lingua operativa: italiano in ogni output prodotto."
│     ← CRITICAL: explicit output language constraint. Must stay in EN version.
│
├─ ## Competenze (lines 35-68)
│   → Full IT. 6 competency blocks:
│   │
│   ├─ 1. Scrittura nella lingua italiana (lines 37-40)
│   │     → grammar, lexicon, punctuation
│   ├─ 2. Strutturazione del testo / Architettura tematica (lines 42-45)
│   │     → intro, development, conclusion
│   ├─ 3. Tipologie testuali (lines 47-52)
│   │     → narrative, descriptive, expository, argumentative, saggio breve
│   ├─ 4. Elaborazione fonti documentali (lines 54-58)
│   │     → source analysis, quotations, concept maps
│   ├─ 5. Adattamento scolastico (lines 60-63)
│   │     → middle school (11-14), high school (14-19), BES/DSA
│   └─ 6. Revisione e auto-correzione (lines 65-68)
│       → proofreading, reverse reading, length check
│
├─ ## Processo operativo (lines 70-105)
│   → Full IT. 6 steps with sub-actions:
│   │
│   ├─ Step 1: Ricezione e analisi della traccia (lines 74-77)
│   ├─ Step 2: Analisi delle fonti (lines 79-82)
│   ├─ Step 3: Pianificazione / scaletta (lines 84-87)
│   ├─ Step 4: Stesura in brutta copia (lines 89-92)
│   ├─ Step 5: Revisione (lines 94-100)
│   └─ Step 6: Bella copia / output finale (lines 102-105)
│
├─ ## Interazioni con il team (lines 107-116)
│   → Full IT. Table with 4 members (Hermes, Pythàgoras, Clio, Atena).
│   → + Note "Non interagisci mai direttamente con l'utente" (line 116)
│
├─ ## Limitazioni (lines 118-126)
│   → Full IT. 7 limitations (numbered list)
│
├─ ## Formato di output (lines 128-160)
│   → Full IT. Markdown template with Italian frontmatter keys.
│   → IMPORTANT: frontmatter keys are in IT (titolo, data, livello, tipologia, fonti)
│     — these should STAY in IT since output is in Italian.
│
└─ ## Principi guida (lines 162-168)
    → Full IT. 5 guiding principles.
```

---

## 3. Content to translate (IT → EN): full inventory

| Section | Lines | Content type | Translation complexity |
|---------|-------|-------------|----------------------|
| YAML `description` | 2-3 | Single paragraph | Low — concise, technical |
| H1 Title | 12 | Single line | Low — role title |
| Identità | 14-16 | 1 paragraph | Medium — mythological reference |
| Personalità e stile | 18-24 | 5 bullets + 1 instruction | Medium — stylistic nuance |
| Regole operative | 26-33 | 6 numbered rules | Low — procedural |
| Competenza 1 | 37-40 | 3 sub-bullets | Medium — grammar terminology |
| Competenza 2 | 42-45 | 3 sub-bullets | Medium — structural terms |
| Competenza 3 | 47-52 | 5 sub-bullets | Medium — text typology terms |
| Competenza 4 | 54-58 | 4 sub-bullets | Low — procedural |
| Competenza 5 | 60-63 | 3 sub-bullets | Low — school level descriptors |
| Competenza 6 | 65-68 | 3 sub-bullets | Low — revision workflow |
| Processo Step 1 | 74-77 | 3 sub-bullets | Low |
| Processo Step 2 | 79-82 | 3 sub-bullets | Low |
| Processo Step 3 | 84-87 | 3 sub-bullets | Low |
| Processo Step 4 | 89-92 | 3 sub-bullets | Low |
| Processo Step 5 | 94-100 | 3 sub-bullets + sub-list | Low |
| Processo Step 6 | 102-105 | 3 sub-bullets | Low |
| Team interactions | 109-116 | Table + 1 note | Medium — table restructuring |
| Limitazioni | 119-126 | 7 bullets | Low — standard limitations |
| Formato output | 130-160 | Template + notes | **High** — IT frontmatter keys must stay IT |
| Principi guida | 163-168 | 5 bullets | Medium — idiomatic principles |

---

## 4. Critical language instructions (MUST PRESERVE semantics in EN)

These are the explicit directives about the **output language** (Italian). They must be translated into English for the profile, but their operational meaning must remain unchanged: **Euterpe always produces output in Italian**.

### 4a. From "Personalità e stile di comunicazione" (line 24)
```markdown
**Original IT:** "Rispondi sempre in italiano."
**EN translation:** "Always respond in Italian."
```
→ This governs Euterpe's interaction/output language. Must be preserved in EN profile.

### 4b. From "Regole operative fondamentali" (line 33)
```markdown
**Original IT:** "6. **Lingua operativa**: italiano in ogni output prodotto."
**EN translation:** "6. **Operating language**: Italian in every output produced."
```
→ Same semantics. Must be preserved.

### 4c. From "Formato di output" (lines 133-139)
Italian frontmatter keys in the output template:
```yaml
titolo, data, livello, tipologia, fonti
```
→ These must **remain in Italian** in the output template, since Euterpe's output is in Italian. The template example should stay IT.

**Recommendation**: In the EN profile, add an explicit note like:
> *"Output language: Italian. The profile instructions are in English, but every essay/theme produced by Euterpe must be written in Italian."*

---

## 5. Member name references inventory

| Member | Count | Lines | Context | Should generalize? |
|--------|-------|-------|---------|-------------------|
| **Hermes** | **5** | 16, 72, 75, 111, 123 | Orchestrator; sends titles/tracce, receives output | No — keep as team role reference |
| **Pythàgoras** | **7** | 16, 31, 55, 74, 79, 112, 121 | Academic researcher; provides sources | No — keep as team role reference |
| **Clio** | **1** | 113 | Vault archivist; consulted for Obsidian compliance | No — keep |
| **Atena** | **1** | 114 | HR manager; may send profile updates | No — keep |
| **Efesto** | **1** | 125 | Developer; mentioned in limitations | No — keep |
| **Total** | **15** | — | All valid team interaction patterns | **No generalization needed** |

**Assessment**: All 15 member references reflect real interaction protocols described in `AGENTS.md`. They should be preserved in translation, not generalized. No references to non-team Olimpo members.

---

## 6. Role title update: from "Scrittrice di Temi" to "Essay & Theme Writer"

### Current state
- H1 (line 12): `# Euterpe — Scrittrice di Temi Italiano`
- Frontmatter description (line 2): starts with "Scrittrice di temi italiano scolastici."
- Competency 3 (lines 47-52): covers "Saggio breve" as one of 5 text types

### Required changes
1. **H1**: `# Euterpe — Essay & Theme Writer (Italian School)`
2. **Frontmatter description**: must explicitly mention both "essays" (saggi) and "themes" (temi)
3. **Competency 3 — "Saggio breve"**: this is already covered, but its description should be slightly more prominent alongside "theme" types
4. **Process steps**: update Step 1 language to mention both "theme" and "essay"

### Suggested frontmatter description (EN)
```yaml
description: >
  Italian school essay and theme writer. Use when composing themes, short essays,
  or argumentative texts for middle and high school students. Receives title from
  Hermes and sources from Pythagoras, produces simple, readable Italian texts
  structured in introduction-body-conclusion.
```

---

## 7. Output format template analysis

The current markdown template (lines 132-158) has Italian frontmatter keys:

```yaml
titolo: "[Titolo del tema]"
data: [Data di produzione]
livello: [Scuola media / Scuola superiore]
tipologia: [Narrativo / Descrittivo / Espositivo / Argomentativo / Saggio breve]
fonti: [Elenco fonti fornite da Pythàgoras, se presenti]
```

**Decision**: These keys should **remain in Italian** because Euterpe's output is in Italian and targets Italian students. The section heading in the EN profile should be updated to something like:

```
## Output Format (Italian)
```

And an explicit note added:
> *"The frontmatter keys below are in Italian because they are part of the Italian-language output. Do not translate them."*

---

## 8. Sections needing structural rework (not just translation)

| # | Section | Issue | Recommended action |
|---|---------|-------|-------------------|
| 1 | YAML `description` | Single-line string too long; current has embedded logic | Rewrite as multi-line YAML with `>` or `\|` for readability |
| 2 | `## Personalità e stile di comunicazione` | Name should become `## Personality & Communication Style` | Translation + cultural adaptation of register descriptors |
| 3 | `## Regole operative fondamentali` | → `## Core Operating Rules` | Straightforward translation |
| 4 | `## Competenze` → `## Competencies` | Competency 3 "Tipologie testuali" should emphasize "saggio breve" more given role update | Minor restructuring |
| 5 | `## Processo operativo` → `## Operational Process` | Step names need idiomatic EN | Straightforward after right terminology |
| 6 | `## Interazioni con il team` → `## Team Interactions` | Table header translation: Direzione → Direction | Table translation + keep member names |
| 7 | `## Formato di output` → `## Output Format (Italian)` | + note about IT keys staying IT | Structural note needed |
| 8 | `## Principi guida` → `## Guiding Principles` | 5 principles; idiomatic EN needed | Moderate — principle 1 has a "proverb" quality |

---

## 9. Complexity estimation

| Factor | Rating | Notes |
|--------|--------|-------|
| Total lines | 168 | Moderate file size |
| % in Italian | 100% | Every content line needs translation |
| % that must stay IT | ~8% | Output template frontmatter keys, some examples |
| Role change impact | Medium | "Saggio breve" already partially covered; mainly title + description |
| Terminology domain | Low-Medium | School-level Italian, no specialized jargon |
| Cultural adaptation | Medium | Italian school system references (scuola media/superiore, BES/DSA, foglio protocollo) — need EN explanation |
| Structural changes | Low | No section reordering needed |
| Member references | 15 | All valid, no generalization needed |

### Overall: **MEDIUM** (6/10)

Breakdown:
- Pure translation work: ~3/10 (straightforward procedural text)
- Cultural adaptation (school system, BES/DSA): requires care — 7/10
- Output template IT/EN boundary management: non-trivial — 6/10
- Maintaining mythological identity (Musa della poesia lirica) in EN: 4/10
- Role update integration (essay + theme): 4/10

---

## 10. Specific edge cases and recommendations

### Edge case 1 — BES/DSA reference (line 63)
```markdown
Original: "BES/DSA: usi font ad alta leggibilità (se formattato), testi semplificati, strutture ridondanti."
```
**Issue**: BES (Bisogni Educativi Speciali) and DSA (Disturbi Specifici dell'Apprendimento) are Italian-specific educational categories.
**Recommendation**: Translate as "Special Educational Needs / Specific Learning Disorders (BES/DSA)" with a brief explanation, or reframe as "Students with special educational needs or learning disorders."

### Edge case 2 — "foglio protocollo" reference (line 68)
```markdown
Original: "Verifichi la lunghezza: 3-5 colonne di foglio protocollo per il saggio breve."
```
**Issue**: "foglio protocollo" (A4 grid paper) is a culturally specific Italian school reference.
**Recommendation**: Translate as "3-5 notebook pages" or "approximately 600-1000 words" — provide a word count equivalent rather than the physical paper format.

### Edge case 3 — "scaletta" (lines 84-87)
```markdown
Original: "Stesura scaletta (Introduzione → Sviluppo con 2-4 paragrafi → Conclusione)"
```
**Recommendation**: Translate as "outline" or "structured draft outline" — avoid literal "little ladder" translation.

### Edge case 4 — "brutta copia / bella copia" (Steps 4 & 6)
```markdown
Original: "Stesura in brutta copia" / "Bella copia (output finale)"
```
**Recommendation**: Translate as "Rough draft" / "Final copy (clean version)" — these are standard Italian school concepts.

### Edge case 5 — "Muse of lyric poetry" identity (line 16)
```markdown
Original: "Sei Euterpe, Musa della poesia lirica trasformata in scrittrice di temi italiano per il Team Olimpo."
```
**Recommendation**: Preserve the mythological reference. Translate as: "You are Euterpe, Muse of lyric poetry, reimagined as an Italian essay and theme writer for Team Olimpo." Keep the poetic identity as it provides role character.

---

## 11. Summary for Atena (translation brief)

| Item | Instruction |
|------|-------------|
| **Role title** | Change to "Essay & Theme Writer (Italian School)" |
| **Profile language** | English (all section headings, instructions, rules) |
| **Output language** | Italian (must remain Italian — add explicit EN instruction) |
| **Output template frontmatter** | Keep Italian keys (`titolo`, `data`, `livello`, `tipologia`, `fonti`) |
| **Member names** | Keep Hermes, Pythagoras, Clio, Athena, Hephaestus (⚠️ note: names in EN profile should use English versions: Pythagoras, Athena, Hephaestus) |
| **Cultural items** | Explain BES/DSA, replace "foglio protocollo" with word count |
| **Competency 3** | Keep "saggio breve" as sub-type; ensure description covers both essay and theme |
| **Section structure** | Maintain same 10 sections; names in English |
| **Mythological identity** | Preserve "Muse of lyric poetry" reference |
| **No emojis** | As per Team Olimpo conventions |
