---
data: 2026-05-19
timestamp: 2026-05-19T22:53:30
agent: proteo
task_id: T-NNN
invocation: 1
type: profile
status: completed
priority: medium
title: "Structural domain analysis — Dike profile translation prep"
quality_score: 5
external_review: false
next_action: "Hermes: analysis ready. The Dike profile requires HIGH complexity translation with 70+ elements to localize, 2 member-name references to generalize, and one critical frontmatter inconsistency (description describes wrong role) to resolve."
completion_notes: "Full structural mapping of dike.md (383 lines). Every translatable element inventoried by section. Member name references flagged. Frontmatter discrepancy detected: description field describes a 'process and workflow analyst' role while the body defines a 'KBA Risk Analyst for Emerson DeltaV' role — requires rewrite from scratch, not translation."
output_refs:
  - .opencode/agents/dike.md
  - Library/SOPs/member-creation-flow.md
  - Library/SOPs/agent-design-methodology.md
  - Library/SOPs/handoff-guide.md
  - AGENTS.md
---

# Structural Domain Analysis — Dike Agent Profile (Translation Preparation)

**Source**: `.opencode/agents/dike.md` (383 lines)
**Target**: Translation Italian → English per team-wide profile migration
**Reference SOP**: `Library/SOPs/member-creation-flow.md` (step 3, handoff type: profile)

---

## 0. Critical Pre-Analysis Findings

### ⚠️ FINDING 1: Frontmatter Description — Role Mismatch

The `description` field (lines 2–4) describes a **different role** from the actual profile body:

| Element | Described Role | Verdict |
|---------|---------------|---------|
| `description` frontmatter (l.2–4) | *"Analista di processi e workflow per il Team Olimpo. Monitora l'evoluzione del sistema, documenta decisionsi chiave, garantisce trasparenza operativa e traccia la provenienza delle modifiche."* | ❌ **MISMATCH** — describes a process/workflow auditor role |
| H1 title (l.13) | *"Dike — Analista KBA del Team Olimpo"* | ✅ Matches body |
| AGENTS.md description | *"KBA Risk Analyst (domain-specific: Emerson DeltaV)"* — scoring/classification of KBA, FMEA risk scoring, DeltaV architecture | ✅ Consistent with body |
| Body (l.17) | *"analista tecnico [...] specializzata nella classificazione e valutazione del rischio delle Knowledge Base Articles (KBA) per sistemi di automazione industriale Emerson DeltaV"* | ✅ Clear mission |

**Impact**: The frontmatter description must be **rewritten from scratch** in English to describe the KBA Risk Analyst role, not translated from the current text. This is a correction, not a translation task.

**Recommended EN description** (~150-200 chars, operational, no member names):

```yaml
description: KBA Risk Analyst for Team Olimpo's Emerson DeltaV domain. Use for scoring and classifying DeltaV Knowledge Base Articles using FMEA-based risk methodology, and maintaining the KBA catalog index.
```

(184 chars — within limit. Includes trigger: "Use for scoring and classifying...")

---

### ⚠️ FINDING 2: Missing Header Comment (SOP Violation)

Per `Library/SOPs/agent-design-methodology.md` (line 16) and `member-creation-flow.md` (checklist step 9), every agent file MUST have a header comment of 2-3 lines after the title H1.

Dike currently has **no header comment**. The first content after the title is `## Identita'`.

**Recommended header comment**:

```
KBA Risk Analyst for Team Olimpo's DeltaV knowledge base.
Scores and classifies Knowledge Base Articles using FMEA-based risk methodology.
Does NOT design process solutions, validate vulnerabilities, or modify source documents.
```

---

### ⚠️ FINDING 3: No Explicit Operating Rules Section

Per the standard structure (agent-design-methodology.md line 19): *"Operating rules — non-negotiable constraints, protocols"*

The current Dike profile has:
- `## Personalita' e stile di comunicazione` (Communication Style) — line 21, with the language directive embedded in the last bullet (line 27)
- But NO dedicated `## Operating Rules` section

The language directive `- **Rispondi sempre in italiano.**` is currently nested inside Communication Style as bullet 5. **This should be extracted into its own Operating Rules section** (as done in Clio, Metis, Calliope profiles) with the language rule as the first item.

**Recommendation**: Add `## Operating Rules` section after Communication Style, move the language directive there, and add any other non-negotiable rules (e.g., "Do not modify source documents", "Always document confidence", etc. — many are scattered in the body).

---

## 1. Current Profile Map — Complete Section Inventory

| # | Section | Subsection | Lines | Language | Notes |
|---|---------|-----------|-------|----------|-------|
| 1 | **Frontmatter** | `description` | 2–4 | IT | ⚠️ **Wrong role** (process analyst, not KBA analyst) |
| 2 | **Frontmatter** | `mode` | 5 | EN | `subagent` — no change |
| 3 | **Frontmatter** | `model` | 6 | EN | `opencode/big-pickle` — no change |
| 4 | **Frontmatter** | `permission` | 7–9 | EN | `edit: allow, read: allow` — no change |
| 5 | **Title** | `# Dike — Analista KBA del Team Olimpo` | 13 | IT | H1 with role |
| — | *(missing)* | **Header comment** | — | — | ❌ **MISSING** per SOP — 2-3 lines needed |
| 6 | **Identity** | Section title | 15 | IT | `## Identita'` |
| 7 | **Identity** | Paragraph — mythological identity (3 sentences) | 17–19 | IT | Dike, figlia di Temi, mission statement |
| 8 | **Personality & Communication Style** | Section title | 21 | IT | `## Personalita' e stile di comunicazione` |
| 9 | **Personality & Communication Style** | Bullet: Tono | 23 | IT | Tone: measured, analytical, precise |
| 10 | **Personality & Communication Style** | Bullet: Atteggiamento | 24 | IT | Attitude: neither alarmist nor dismissive |
| 11 | **Personality & Communication Style** | Bullet: Linguaggio | 25 | IT | Language: technical, clear, structured |
| 12 | **Personality & Communication Style** | Bullet: Ritmo | 26 | IT | Rhythm: methodical, consistent |
| 13 | **Personality & Communication Style** | Bullet: **Language directive** | 27 | IT | `- **Rispondi sempre in italiano.**` ⚠️ |
| 14 | **Competency Domain** | Section title | 29 | IT | `## Dominio di competenza — Automazione industriale` |
| 15 | **Competency 1** | Subtitle: DCS Architecture | 31 | IT | `### Architettura DCS (Distributed Control System)` |
| 16 | **Competency 1** | 5 level bullets (Level 0–4) | 33–38 | IT | Infrastructure levels, IT descriptions |
| 17 | **Competency 2** | Subtitle: DeltaV Components | 40 | IT | `### Componenti DeltaV` |
| 18 | **Competency 2** | 5 bullets (workstation, controller, I/O, software, infrastructure) | 42–47 | IT | Technical terms mostly EN, descriptions IT |
| 19 | **Competency 3** | Subtitle: Key Concepts | 49 | IT | `### Concetti chiave` |
| 20 | **Competency 3** | 4 bullets (control loops, SIS, firmware, Purdue model) | 51–54 | IT | |
| 21 | **Risk Scoring Framework** | Section title | 56 | IT | `## Framework di scoring del rischio` |
| 22 | **Scoring: Level 1** | Subtitle: Composite Risk Score | 58 | IT | `### Livello 1 — Risk Score composito (1.0-10.0)` — mixed IT/EN |
| 23 | **Scoring: Level 1** | Formula (code block) | 62–64 | EN/IT | Formula in EN, labels in IT |
| 24 | **Scoring: Level 1** | Severity explanation (1–10 scale) | 66–71 | IT | Detailed scale with examples |
| 25 | **Scoring: Level 1** | Occurrence explanation (1–10 scale) | 72–75 | IT | Detailed scale with examples |
| 26 | **Scoring: Level 1** | Detectability explanation (1–10 scale) | 76–79 | IT | Detailed scale with examples |
| 27 | **Scoring: Level 1** | Weight rationale paragraph | 81 | IT | Why severity is weighted at 50% |
| 28 | **Scoring: Level 2** | Subtitle: Qualitative Categorization | 83 | IT | `### Livello 2 — Categorizzazione qualitativa` |
| 29 | **Scoring: Level 2** | **Table**: 5-level classification | 85–91 | IT/EN | Labels EN (Negligible→Critical), descriptions IT |
| 30 | **Scoring: Modifiers** | Subtitle: Multipliers & Modifiers | 93 | IT | `### Moltiplicatori e modificatori` |
| 31 | **Scoring: Modifiers** | **Table**: 9 impact factors | 97–107 | IT | Factor descriptions in IT |
| 32 | **Scoring: Emerson Taxonomy** | Subtitle: Emerson Native Taxonomy | 109 | IT | `### Tassonomia Emerson nativa (riferimento)` |
| 33 | **Scoring: Emerson Taxonomy** | **Table**: 3 categories (Alert/Advisory/Informational) | 111–115 | IT/EN | Labels EN, descriptions IT |
| 34 | **Scoring: Emerson Taxonomy** | Usage note paragraph | 117 | IT | Guidance on when to diverge |
| 35 | **Problem Classification** | Section title | 119 | IT | `## Classificazione dei problemi` |
| 36 | **Problem Classification** | Subtitle: By problem type | 121 | IT | `### Per tipo di problema` |
| 37 | **Problem Classification** | 6 code-label + description bullets | 122–127 | IT/EN | Labels are EN code-style (`bug_software`, etc.), descriptions IT |
| 38 | **Problem Classification** | Subtitle: By impact domain | 129 | IT | `### Per dominio d'impatto` |
| 39 | **Problem Classification** | 4 bullets (safety, availability, integrity, confidentiality) | 130–133 | IT | |
| 40 | **Severity Indicators** | Section title | 135 | IT | `## Indicatori di severita'` |
| 41 | **Severity: High** | Subtitle + Linguistic patterns (7 items) | 137–145 | IT/EN | Mixed — phrases like "loss of control", "shutdown inatteso" |
| 42 | **Severity: High** | Structural indicators (6 items) | 147–153 | IT/EN | Mixed |
| 43 | **Severity: Medium** | Subtitle + Linguistic patterns (5 items) | 155–160 | IT/EN | Mixed |
| 44 | **Severity: Medium** | Structural indicators (4 items) | 162–166 | IT/EN | Mixed |
| 45 | **Severity: Low** | Subtitle + Linguistic patterns (5 items) | 168–173 | IT/EN | Mixed |
| 46 | **Severity: Low** | Structural indicators (4 items) | 175–179 | IT/EN | Mixed |
| 47 | **Operating Process** | Section title | 181 | IT | `## Processo operativo — Analisi di una KBA` |
| 48 | **Process: Step 1** | Rapid scan — numbered step | 183–184 | IT | |
| 49 | **Process: Step 2** | Overview analysis — numbered step | 186–191 | IT | |
| 50 | **Process: Step 3** | Impact mapping — numbered step | 193–197 | IT | |
| 51 | **Process: Step 4** | Mitigation assessment — numbered step | 199–203 | IT | |
| 52 | **Process: Step 5** | Composite scoring — numbered step | 205–211 | IT | 7 sub-steps |
| 53 | **Process: Ambiguity** | Subtitle: Ambiguity Signals | 213 | IT | `### Segnali di ambiguita'` |
| 54 | **Process: Ambiguity** | 4 bullet items | 214–217 | IT | |
| 55 | **Process: Confidence** | Subtitle: Confidence Criteria | 219 | IT | `### Confidence — criteri di assegnazione` |
| 56 | **Process: Confidence** | **Table**: 3 confidence levels | 223–227 | IT/EN | Labels EN (high/medium/low), conditions IT |
| 57 | **Process: Confidence** | Rule paragraph | 229 | IT | `confidence_note` required for medium/low |
| 58 | **Output Format** | Section title | 231 | IT | `## Formato di output — Record strutturato per singola KBA` |
| 59 | **Output Format** | Intro line | 233 | IT | Path: `Library/data/kba_catalog/records/` |
| 60 | **Output Format** | YAML frontmatter **code block** (~20 fields) | 237–284 | EN/IT | Field names EN, comments IT |
| 61 | **Output Format** | Body Markdown template | 288–316 | IT | `## Sintesi`, `## Analisi del rischio`, etc. |
| 62 | **Catalog Structure** | Section title | 318 | IT | `## Struttura del catalogo` |
| 63 | **Catalog Structure** | Directory tree **code block** | 320–327 | EN | Paths only — preserve as-is |
| 64 | **Catalog Structure** | Index (index.yaml) **code block** | 329–347 | EN | YAML template — mostly EN |
| 65 | **Catalog Structure** | Update instruction | 349 | IT | |
| 66 | **Batch Workflow** | Section title | 351 | IT | `## Workflow batch — Analisi multipla` |
| 67 | **Batch Workflow** | 5 numbered steps (Inventario, Triage, Analisi, Consolidamento, Report) | 353–358 | IT | |
| 68 | **Team Interactions** | Section title | 360 | IT | `## Interazioni con il team` |
| 69 | **Team Interactions** | **Table**: Hermes (l.364), Clio (l.365) | 362–366 | IT | ⚠️ Contains member names |
| 70 | **Team Interactions** | No direct user interaction note | 367 | IT | `Non interagisci mai direttamente con l'utente` |
| 71 | **Limitations** | Section title | 369 | IT | `## Limitazioni` |
| 72 | **Limitations** | 5 bullet points | 371–375 | IT | No member names — generic descriptions |
| 73 | **Guiding Principles** | Section title | 377 | IT | `## Principi guida` |
| 74 | **Guiding Principles** | 5 numbered principles | 379–383 | IT | |

**Total line items to modify**: ~70–80 (majority of the file)
**Lines that stay unchanged**: ~30 (paths, code blocks with EN-only content, permission, mode, model)

---

## 2. Elementi da Tradurre — Per Sezione

### 2.1 Frontmatter — `description:` (righe 2–4)

- **Testo attuale (IT)**: `Analista di processi e workflow per il Team Olimpo. Monitora l'evoluzione del sistema, documenta decisionsi chiave, garantisce trasparenza operativa e traccia la provenienza delle modifiche.`
- **Problema**: ❌ **Non corrisponde al ruolo descritto nel corpo del file**. Parla di analista di processi/workflow, non di KBA Risk Analyst per Emerson DeltaV.
- **Cosa fare**: **Riscrivere da zero** in EN (~150-200 char, operativa, senza nomi membri). Non tradurre il testo attuale.
- **Raccomandazione**: La descrizione deve rispondere a "When should Hermes invoke Dike?" → When a DeltaV KBA needs scoring, classification, and catalog update.
- **Complessità**: Alta — richiede riscrittura creativa, non traduzione.

### 2.2 Section Titles (da tradurre)

| Current IT | Proposed EN | Note |
|------------|-------------|------|
| `# Dike — Analista KBA del Team Olimpo` | `# Dike — KBA Risk Analyst, Team Olimpo` | Allineare a formato `# <Nome> — <Ruolo EN>, Team Olimpo` |
| `## Identita'` | `## Identity` | Standard |
| `## Personalita' e stile di comunicazione` | `## Communication Style` | Standard |
| *(nuovo)* | `## Operating Rules` | **DA AGGIUNGERE** — mancante, estrarre da Communication Style |
| `## Dominio di competenza — Automazione industriale` | `## Competency Domain: Industrial Automation` | Oppure suddividere in singole Competency subsection |
| `### Architettura DCS (Distributed Control System)` | `### DCS Architecture (Distributed Control System)` | Preserve EN acronym |
| `### Componenti DeltaV` | `### DeltaV Components` | |
| `### Concetti chiave` | `### Key Concepts` | |
| `## Framework di scoring del rischio` | `## Risk Scoring Framework` | |
| `### Livello 1 — Risk Score composito (1.0-10.0)` | `### Level 1 — Composite Risk Score (1.0-10.0)` | |
| `### Livello 2 — Categorizzazione qualitativa` | `### Level 2 — Qualitative Categorization` | |
| `### Moltiplicatori e modificatori` | `### Multipliers & Modifiers` | |
| `### Tassonomia Emerson nativa (riferimento)` | `### Emerson Native Taxonomy (Reference)` | |
| `## Classificazione dei problemi` | `## Problem Classification` | |
| `### Per tipo di problema` | `### By Problem Type` | |
| `### Per dominio d'impatto` | `### By Impact Domain` | |
| `## Indicatori di severita'` | `## Severity Indicators` | |
| `## Processo operativo — Analisi di una KBA` | `## Operational Process: KBA Analysis` | |
| `### Segnali di ambiguita'` | `### Ambiguity Signals` | |
| `### Confidence — criteri di assegnazione` | `### Confidence Assignment Criteria` | |
| `## Formato di output — Record strutturato per singola KBA` | `## Output Format: Single KBA Record` | |
| `## Struttura del catalogo` | `## Catalog Structure` | |
| `## Workflow batch — Analisi multipla` | `## Batch Workflow: Multi-KBA Analysis` | |
| `## Interazioni con il team` | `## Team Interactions` | |
| `## Limitazioni` | `## Limitations` | Standard |
| `## Principi guida` | `## Guiding Principles` | |

Totale titoli da tradurre: **~24**

### 2.3 Identity (righe 15–19)

- **Testo attuale**: Paragrafo di 3 frasi. Identità mitologica (Dike, dea della giustizia, figlia di Temi) + missione tecnica.
- Elementi da preservare: riferimento a Dike come dea della giustizia applicata, relazione con Themis, missione di classificazione KBA.
- **⚠️ Nota culturale**: `Dike, dea della giustizia applicata, figlia di Temi` → `Dike, goddess of applied justice, daughter of Themis`. Themis è invariato in EN. "Giustizia applicata" è un concetto che funziona in EN.
- Raccomandazione: dopo l'H1, aggiungere **header comment** di 2-3 righe (standard SOP). Poi tradurre il paragrafo Identity.

### 2.4 Communication Style (righe 21–27)

- Tradurre interamente: 5 bullet point con label in grassetto.
- **Tono** → **Tone** (measured, analytical, precise)
- **Atteggiamento** → **Approach** (neither alarmist nor minimizing)
- **Linguaggio** → **Language** (technical, clear, structured)
- **Ritmo** → **Rhythm** (methodical, consistent)
- ⚠️ **Riga 27 — DIRETTIVA LINGUA**: `- **Rispondi sempre in italiano.**` → **DEVE diventare** `- **Always reply in English.**`
  - **Raccomandazione**: Estrarre dalla sezione Communication Style e creare una nuova sezione `## Operating Rules` subito dopo, con questa come prima regola (standard Metis/Clio/Calliope).

### 2.5 Competency Domain: Industrial Automation (righe 29–54)

- **Titolo sezione**: Tradurre.
- **Sottosezione 1 — DCS Architecture (righe 31–38)**: Tradurre 5 livello descrizioni. I termini tecnici (S-series, M-series, HMI, DCS, ERP) sono già in EN o invariati.
- **Sottosezione 2 — DeltaV Components (righe 40–47)**: Tradurre 5 bullet. Nomi propri (DeltaV Explorer, Operate, Diagnostics, Batch) vanno preservati invariati.
- **Sottosezione 3 — Key Concepts (righe 49–54)**: Tradurre 4 bullet. "Safety Instrumented Systems (SIS)" → preservare acronimo. "Modello Purdue (IEC 62264)" → "Purdue Model (IEC 62264)".
- **Volume**: ~24 righe di testo tecnico denso.
- **Nessun nome membro** in questa sezione.

### 2.6 Risk Scoring Framework (righe 56–117) — SEZIONE CRITICA

Questa è la sezione più lunga e complessa del profilo (~62 righe). Contiene:

#### 2.6.1 Level 1 — Composite Risk Score (righe 58–81)

- **Formula (codice)**: `Risk Score = (Severita' x 0.5) + (Probabilita' x 0.3) + (Rilevabilita_inversa x 0.2)`
  - Tradurre i nomi dei fattori: `Severita'` → `Severity`, `Probabilita'` → `Occurrence`, `Rilevabilita_inversa` → `Inverse Detectability`
  - La formula in sé è un'operazione matematica — tradurre solo i nomi delle variabili.
- **Descrizioni scale Severità/Occurrence/Detectability**: Tradurre interamente. Attenzione ai termini tecnici come `plant shutdown`, `workaround`, `cosmetico`.
- **Paragrafo pesi (riga 81)**: Tradurre — contiene la logica del 50% peso severità.

#### 2.6.2 Level 2 — Qualitative Categorization (righe 83–91)

- **Tabella**: 5 righe di classificazione.
  - Label di livello: già in EN (`Negligible`, `Informational`, `Advisory`, `Warning`, `Critical`) — **preservare invariati**.
  - Colonna "Significato operativo": tradurre le descrizioni IT.
  - Headers tabella: `Livello` → `Level`, `Score` (già EN), `Label` (già EN), `Significato operativo` → `Operative Meaning`.

#### 2.6.3 Multipliers & Modifiers (righe 93–107)

- **Tabella**: 9 fattori con effetto.
  - Colonna "Fattore" → "Factor" — tradurre descrizioni IT.
  - Colonna "Effetto" → "Effect" — già numerico, preservare.
- **Attenzione**: termini come `Workaround banale`, `Safety-related (SIS)`, `CVE associato con exploit noto` — tecnici ma traducibili direttamente.

#### 2.6.4 Emerson Native Taxonomy (righe 109–117)

- **Tabella**: 3 categorie Emerson.
  - Labels `Alert`, `Advisory`, `Informational` — **preservare** (sono nomenclature Emerson ufficiali).
  - Descrizioni e score indicativi: tradurre.
- **Paragrafo nota (riga 117)**: Tradurre — importante per la metodologia ("puoi divergere ma documenta").

### 2.7 Problem Classification (righe 119–133)

- **Titolo sezione**: Tradurre.
- **Sottosezione "Per tipo di problema" (righe 121–127)**:
  - 6 label in formato codice (`bug_software`, `security_vulnerability`, ecc.) — **preservare invariati** (sono identificatori interni).
  - Descrizioni brevi dopo i `:` — tradurre.
- **Sottosezione "Per dominio d'impatto" (righe 129–133)**:
  - 4 label (`safety`, `availability`, `integrity`, `confidentiality`) — **preservare** (sono categorie standard ISO/inglese).
  - Descrizioni: tradurre.

### 2.8 Severity Indicators (righe 135–179) — SEZIONE CRITICA

Questa sezione è un prontuario di pattern linguistici bilingue (IT/EN). Richiede attenzione:

- **Righe 137–145 (High severity)**:
  - Pattern linguistici misti IT/EN: es. `"could result in loss of control", "perdita di controllo"`.
  - ⚠️ **Strategia**: Normalizzare tutto in EN. Rimuovere i pattern italiani (sono duplicati dei pattern EN o versioni italiane). Tenere solo i pattern EN o tradurre quelli IT.
  - **Raccomandazione**: Poiché il profilo sarà in EN, i pattern linguistici dovrebbero essere TUTTI in EN. Rimuovere le versioni italiane o tradurle.
- **Righe 147–153 (High — Structural indicators)**: Tradurre descrizioni IT.
- **Righe 155–160 (Medium — Linguistic patterns)**: Già prevalentemente in EN — normalizzare.
- **Righe 162–166 (Medium — Structural indicators)**: Tradurre.
- **Righe 168–173 (Low — Linguistic patterns)**: Già prevalentemente in EN.
- **Righe 175–179 (Low — Structural indicators)**: Tradurre.

### 2.9 Operating Process (righe 181–229)

- **Titolo sezione**: Tradurre.
- **Passi 1–5 (righe 183–211)**: Tradurre interamente. I titoli dei passi (Scansione rapida, Analisi dell'overview, ecc.) e le descrizioni.
- **Sottosezione "Segnali di ambiguita'" (righe 213–217)**: Tradurre 4 bullet.
- **Sottosezione "Confidence — criteri" (righe 219–229)**: Tradurre.
  - **Tabella confidence**: Labels `high`, `medium`, `low` — già EN. Condizioni IT — tradurre.
  - **Regola (riga 229)**: `confidence_note` obbligatoria — tradurre, preservare il nome del campo `confidence_note` (è un campo dati).

### 2.10 Output Format (righe 231–316) — SEZIONE CODICE

- **Titolo sezione**: Tradurre.
- **Intro (riga 233)**: Tradurre. Path `Library/data/kba_catalog/records/` → preservare.
- **YAML frontmatter code block (righe 237–284)**:
  - **Nomi dei campi YAML**: Già in EN (`kba_id`, `title`, `risk_score`, ecc.) — **preservare invariati**.
  - **Commenti/caption IT** (es. `# Identificazione`, `# Classificazione`, `# Scoring dettagliato`): Tradurre in EN.
  - I valori enum (`"Alert"`, `"Advisory"`, ecc.) sono già in EN.
  - Le descrizioni nei commenti (es. `# 1-10 (10 = difficile da rilevare)`) — tradurre.
- **Body Markdown template (righe 288–316)**:
  - Header sezioni (`## Sintesi`, `## Analisi del rischio`, ecc.) — tradurre.
  - Placeholder `[score]/10`, `[Calcolo esplicito...]` — tradurre il testo interno.
  - **Raccomandazione**: Creare una versione EN del template completa e coerente.

### 2.11 Catalog Structure (righe 318–349)

- **Titolo sezione**: Tradurre.
- **Directory tree (righe 320–327)**: Path puri — **preservare invariati**.
- **YAML index template (righe 329–347)**: Già in EN — **preservare invariato**.
- **Istruzione finale (riga 349)**: Tradurre ("Aggiorna l'indice ogni volta...").

### 2.12 Batch Workflow (righe 351–358)

- **Titolo sezione**: Tradurre.
- **5 step**: Tradurre titoli e descrizioni. Nessun nome membro.

### 2.13 Team Interactions (righe 360–367)

- **Titolo sezione**: Tradurre.
- **Tabella**: 2 righe (Hermes, Clio).
  - ⚠️ **Riga 364 — Hermes**: `Ricevi indicazione di KBA da analizzare. Restituisci score + record strutturato + alert per rischi critici.`
  - ⚠️ **Riga 365 — Clio**: `Dipendenza a monte: Clio converte i PDF e li deposita in Library/documents/. Lavori sul Markdown già convertito.`
- **Riga 367**: `Non interagisci mai direttamente con l'utente (protocollo Team Olimpo).`
- **Raccomandazione**: Ristrutturare in formato **Receive / Produce** (come Metis/Clio profili EN). Rimuovere nomi membri:
  ```
  ## Interactions
  
  **Receive:**
  - KBA analysis requests from the orchestrator (which KBAs to process, batch or single)
  
  **Produce:**
  - Structured risk score records (saved to `Library/data/kba_catalog/records/<nk-id>.md`)
  - Updated catalog index (`Library/data/kba_catalog/index.yaml`)
  - Critical risk alerts for scores > 8.0
  
  **Upstream dependency:**
  - Works on Markdown files already converted by the vault archivist from PDFs in `Library/documents/`
  
  **Protocol:**
  - Never interacts directly with the user.
  ```

### 2.14 Limitations (righe 369–375)

- **Titolo sezione**: Tradurre.
- **5 bullet**: Tradurre interamente.
- **Nessun nome membro** in questa sezione — le descrizioni sono già generiche ("Non sei un ingegnere di processo", "Non sei un penetration tester", ecc.).
- Traduzione diretta, nessuna riscrittura necessaria.

### 2.15 Guiding Principles (righe 377–383)

- **Titolo sezione**: Tradurre.
- **5 principi numerati**: Tradurre interamente.
- Nessun nome membro, nessun riferimento culturale problematico.

---

## 3. Riferimenti a Nomi di Membri — Inventory Completo

Secondo la SOP `agent-design-methodology.md` (riga 46): *"Never mention specific team member names."*

| # | Riga | Nome Membro | Contesto | Azione Raccomandata |
|---|------|-------------|----------|---------------------|
| 1 | 364 | Hermes | Interazioni — mittente delle richieste KBA | Sostituire con "orchestrator" |
| 2 | 365 | Clio | Interazioni — dipendenza upstream per conversione PDF | Generalizzare in "vault archivist" |

**Totale**: **2 occorrenze** di nomi membri da rimuovere/generalizzare.

**Note**: 
- Il nome `Dike` nel titolo e nell'Identity (righe 13, 17) è il nome dell'agente stesso — **non modificare**.
- `Temi` (Themis, riga 17) è la madre mitologica di Dike — **preservare** (è mitologia, non un membro del team).
- `Emerson` (righe 17, 113, 117, 148) è il vendor del sistema DeltaV — **preservare**.
- `DeltaV` è il nome del prodotto — **preservare**.

**Verdetto**: Dike è il profilo con **meno riferimenti** a nomi membri tra tutti quelli analizzati finora. Solo 2 occorrenze, entrambe nella sezione Interazioni.

---

## 4. Direttiva Lingua Esplicita

**Trovata alla riga 27** (all'interno di Communication Style):

```
- **Rispondi sempre in italiano.**
```

Obbligatorio cambiarla in:

```
- **Always reply in English.**
```

**Raccomandazione strutturale**: Estrarre dalla sezione Communication Style e creare una sezione `## Operating Rules` dedicata (seguendo lo standard Metis/Clio/Calliope). La regola della lingua deve essere la prima delle Operating Rules.

---

## 5. Riferimenti Culturali e Linguistici Specifici

| Elemento | Rischio | Raccomandazione |
|----------|---------|-----------------|
| `Dike, dea della giustizia applicata, figlia di Temi` | Nome mitologico e relazione — invariante in EN | `Dike, goddess of applied justice, daughter of Themis` |
| `Temi` / `Themis` | Traslitterazione italiana vs. greca | Usare `Themis` (forma greca standard in EN) |
| Termini tecnici DeltaV (`S-series`, `M-series`, `HMI`, `historian`) | Sono nomi propri di prodotto — invariati | Preservare invariati |
| `Modello Purdue (IEC 62264)` | Standard internazionale — nomenclatura fissa | `Purdue Model (IEC 62264)` |
| `CVE`, `CVSS`, `FMEA`, `SIS` | Acronimi internazionali | Preservare invariati |
| `plant shutdown`, `loss of control`, `workaround` | Termini già EN nel testo IT | Preservare come sono |
| Pattern linguistici bilingui (IT/EN) nelle Severity Indicators | Mix di lingue — decidere strategia | **Normalizzare tutto in EN**. Rimuovere duplicati IT. |
| `bug_software`, `security_vulnerability` | Label codice in formato snake_case | Preservare invariati (sono identificatori) |
| `cosmetico`, `degradazione prestazioni`, `shutdown inatteso` | Termini tecnici IT | Tradurre: cosmetic, performance degradation, unexpected shutdown |
| `Score composito` / `Composite Risk Score` | Termine metodologico | Usare "Composite Risk Score" o "Risk Score" |
| `Rilevabilita' inversa` / `Inverse Detectability` | Termine FMEA | In FMEA standard è "Detectability" (inversa è implicita nel punteggio 1-10) |
| `Rispondi sempre in italiano` → `Always reply in English` | Cambio lingua dell'agente | **Critico** — la direttiva cambia da IT a EN |
| `workaround banale` vs `workaround complesso` | Gradazione qualitativa | `trivial workaround` vs `complex workaround` |

**Nessun gioco di parole intraducibile, dialetto, o riferimento culturale strettamente italiano** che blocchi la traduzione. Il dominio (automazione industriale Emerson DeltaV) è intrinsecamente internazionale con terminologia prevalentemente inglese.

---

## 6. Raccomandazioni per Miglioramento Strutturale

### 6.1 Problema Principale: Sezionamento e Aggregazione

L'attuale struttura ha **13 sezioni di primo livello** — è molto frammentata. La struttura standard (SOP) prevede al massimo 10. Diverse sezioni correnti possono essere accorpate:

| Situazione Attuale | Raccomandazione |
|-------------------|-----------------|
| Dominio di competenza → DCS Architettura + Componenti + Concetti chiave | **Accorpare** in un'unica sezione `## Competencies` con 3 sottosezioni (standard SOP) |
| Framework di scoring → 4 sottosezioni (Livello 1, Livello 2, Modificatori, Emerson) | **Mantenere** come sezione unica — è il cuore metodologico del profilo |
| Classificazione problemi + Severity Indicators | **Unire** in `## Classification & Scoring Criteria` (sono correlate) |
| Processo operativo → 5 passi + Ambiguity + Confidence | **Mantenere** come `## Operational Workflow` con 3 sottosezioni |
| Output Format + Catalog Structure | **Unire** in `## Output & Catalog Maintenance` (sono entrambi formato output) |
| Batch Workflow | **Fondere** dentro Operational Workflow come workflow alternativo |
| Guiding Principles | **Spostare** dopo Limitations o **fondere** in Communication Style |

### 6.2 Sequenza Raccomandata (allineata a SOP)

```
1. Frontmatter                    → (invariato)
2. [Header comment]               → DA AGGIUNGERE (2-3 righe)
3. Title + Identity               → tradurre
4. Communication Style            → tradurre, rimuovere lingua directive
5. Operating Rules                → DA CREARE (con lingua directive come prima regola)
6. Competencies                   → rinominare, accorpare dominio + componenti + concetti
7. Risk Scoring Framework         → mantenere come cuore metodologico
8. Classification & Criteria      → unire Problem Classification + Severity Indicators
9. Operational Workflow           → unire Processo + Batch + Ambiguity + Confidence
10. Output & Catalog              → unire Output Format + Catalog Structure
11. Interactions                  → riscrivere in Receive/Produce, rimuovere nomi membri
12. Limitations                   → tradurre
13. Guiding Principles            → mantenere come chiusura
```

### 6.3 Aggiunte Necessarie

1. **Header comment** (2-3 righe dopo H1) — obbligatorio per SOP
2. **Operating Rules section** — mancante, creare con lingua directive e altre regole non negoziabili
3. **Confidence section** — già presente ma potrebbe essere spostata nel workflow

### 6.4 Elementi da Preservare ASSOLUTAMENTE

1. **Sequenza logica** del processo di scoring (non alterare l'ordine dei passi 1-5)
2. **Formula FMEA** e pesi (50/30/20) — è il cuore del metodo
3. **Tabelle** di categorizzazione (5 livelli, 9 modificatori, 3 categorie Emerson, 3 confidence)
4. **Template YAML** del record di output (20+ campi)
5. **Path filesystem**: `Library/data/kba_catalog/`, `Library/documents/`
6. **Nomenclature tecniche**: Emerson Alert/Advisory/Informational, S-series/M-series, DeltaV Explorer/Operate
7. **Permission block**: `edit: allow, read: allow`
8. **Numero di limitazioni**: 5 punti
9. **Numero di principi guida**: 5 punti

### 6.5 Path e Comandi da NON Tradurre (preservare invariati)

| Riga | Elemento | Tipo |
|------|----------|------|
| 233 | `Library/data/kba_catalog/records/` | Path template |
| 237–284 | Campi YAML (`kba_id:`, `title:`, `risk_score:`, ecc.) | Nomi campo |
| 288–316 | Struttura body Markdown (solo template) | Struttura |
| 320–327 | Directory tree (`Library/`, `data/`, `kba_catalog/`, ecc.) | Path |
| 329–347 | YAML index template (`catalog_updated:`, `total_entries:`, ecc.) | Nomi campo |
| 7–9 | `permission:` block | Frontmatter |

---

## 7. Stima Complessità

| Fattore | Valutazione |
|---------|-------------|
| **Volume totale** | 383 righe — **il più lungo finora** (Clio: 170, Calliope: 111) |
| **Elementi da tradurre** | ~70-80 (titoli, descrizioni, bullet, tabelle, note) |
| **Elementi da preservare invariati** | ~30 (path, campi YAML, permission, mode, model, acronimi tecnici) |
| **Nomi membri da rimuovere** | 2 occorrenze — **minimo storico** |
| **Riscritture strutturali necessarie** | 3 (frontmatter description da zero, header comment, Operating Rules section) |
| **Inconsistenze da risolvere** | 1 (frontmatter description non corrisponde al corpo) |
| **Sezioni da modificare** | ~14 su 14 sezioni |
| **Tabelle da tradurre** | 5 (qualitative categorization, modifiers, Emerson taxonomy, interactions, confidence) |
| **Code block da modificare parzialmente** | 3 (formula, YAML template, Markdown template) |
| **Giochi di parole italiani** | 0 |
| **Riferimenti culturali problematici** | 0 |
| **Pattern linguistici bilingui da normalizzare** | ~20 (sezione Severity Indicators) |
| **Decisioni di traduzione aperte** | 1 (pattern bilingui: normalizzare in EN) |

### Verdetto: COMPLESSITÀ ALTA

**Motivazione**:

1. **Volume**: 383 righe è più del doppio di Clio (170) e più del triplo di Calliope (111). È un profilo estremamente corposo.
2. **Densità tecnica**: Il dominio Emerson DeltaV ha terminologia specializzata che deve essere tradotta con precisione (FMEA, Purdue model, safety instrumented systems, ecc.).
3. **Pattern bilingui**: La sezione Severity Indicators contiene pattern linguistici misti IT/EN che richiedono normalizzazione strategica — non è una semplice traduzione.
4. **Riscritture strutturali**: 3 interventi strutturali (frontmatter, header comment, operating rules) si aggiungono alla traduzione pura.
5. **Tabelle multiple**: 5 tabelle con contenuto misto richiedono attenzione per preservare allineamento e struttura.
6. **Template YAML**: 20+ campi con commenti IT da tradurre senza rompere la sintassi YAML.

**Tempo stimato per la traduzione**: 45-60 minuti per un traduttore esperto del dominio tecnico (tempo raddoppiato rispetto a Clio/Calliope per via del volume e della densità tecnica).

**Sezioni a maggiore sforzo**:
1. **Risk Scoring Framework** (righe 56-117) — 62 righe, 4 sottosezioni, 3 tabelle, la formula, logica di peso
2. **Output Format** (righe 231-316) — 86 righe, template YAML + Markdown, attenzione alla sintassi
3. **Severity Indicators** (righe 135-179) — 45 righe, pattern bilingui da normalizzare
4. **Operating Process** (righe 181-229) — 49 righe, 5 passi, 2 sottosezioni, 1 tabella

**Sezioni a minore sforzo**:
1. **Interactions** (righe 360-367) — 8 righe, 2 nomi membri da generalizzare
2. **Limitations** (righe 369-375) — 7 righe, traduzione diretta
3. **Guiding Principles** (righe 377-383) — 7 righe, traduzione diretta
4. **Catalog Structure** (righe 318-349) — 32 righe ma quasi tutto path/code invariato

---

## 8. Checklist Pre-Traduzione (da consegnare a chi traduce)

- [ ] **Frontmatter `description:`** → Riscrivere da zero in EN (~150-200 char, ruolo corretto: KBA Risk Analyst per DeltaV). NON tradurre il testo attuale.
- [ ] **Aggiungere header comment** di 2-3 righe dopo il titolo H1 (obbligatorio SOP).
- [ ] **Aggiungere sezione `## Operating Rules`** — estrarre lingua directive da Communication Style, aggiungere altre regole.
- [ ] **Tradurre titolo H1** → `# Dike — KBA Risk Analyst, Team Olimpo`
- [ ] **Identity** → Tradurre, preservare Dike/Themis mitologia
- [ ] **Communication Style** → Tradurre 4 bullet (Tono/Atteggiamento/Linguaggio/Ritmo), RIMUOVERE la lingua directive (spostata in Operating Rules)
- [ ] **Competency: DCS Architecture** → Tradurre 5 livello descrizioni
- [ ] **Competency: DeltaV Components** → Tradurre 5 bullet, preservare nomi prodotto
- [ ] **Competency: Key Concepts** → Tradurre 4 bullet
- [ ] **Risk Scoring: Level 1** → Tradurre formula (nomi variabili), scale Severità/Occurrence/Detectability, paragrafo pesi
- [ ] **Risk Scoring: Level 2** → Tradurre tabelle, preservare label EN (Negligible→Critical)
- [ ] **Risk Scoring: Modifiers** → Tradurre tabella 9 fattori
- [ ] **Risk Scoring: Emerson Taxonomy** → Tradurre tabella, preservare Alert/Advisory/Informational
- [ ] **Problem Classification** → Tradurre descrizioni, preservare label codice (`bug_software`, ecc.)
- [ ] **Severity Indicators** → **Normalizzare in EN**: rimuovere pattern italiani, tenere solo pattern EN o tradurre quelli IT. Tradurre indicatori strutturali.
- [ ] **Operational Process: Steps 1-5** → Tradurre titoli e descrizioni
- [ ] **Operational Process: Ambiguity Signals** → Tradurre 4 bullet
- [ ] **Operational Process: Confidence** → Tradurre tabella 3 livelli + regola
- [ ] **Output Format: YAML template** → Tradurre commenti IT nel codice YAML, preservare campi EN
- [ ] **Output Format: Markdown template** → Tradurre header sezioni e placeholder
- [ ] **Catalog Structure** → Tradurre solo titolo sezione, preservare path e YAML index
- [ ] **Batch Workflow** → Tradurre 5 step
- [ ] **Interactions** → Riscrivere in formato Receive/Produce, rimuovere Hermes e Clio
- [ ] **Limitations** → Tradurre 5 bullet (traduzione diretta)
- [ ] **Guiding Principles** → Tradurre 5 principi (traduzione diretta)
- [ ] **Verificare**: nessun path tradotto, nessun campo YAML modificato
- [ ] **Verificare**: nessun nome membro nel file finale
- [ ] **Verificare**: direttiva `Always reply in English.` presente come prima regola in Operating Rules
- [ ] **Verificare**: pattern linguistici in Severity Indicators tutti in EN (nessun residuo IT)
- [ ] **Verificare**: i 5 livelli di classificazione (Negligible/Critical) preservati invariati
