---
data: 2026-05-19
timestamp: 2026-05-19T22:09:00
agent: proteo
task_id: T-NNN
invocation: 1
type: profile
status: completed
priority: medium
title: "Structural domain analysis — Clio profile translation prep"
quality_score: 5
external_review: false
next_action: "Hermes: analysis ready. The Clio profile requires medium-complexity translation with 50+ elements to localize and 8 member-name references to generalize."
completion_notes: "Full structural mapping of clio.md (170 lines). Every translatable element inventoried by section. Member name references flagged. Cultural/technical preservation notes provided."
output_refs:
  - .opencode/agents/clio.md
  - Library/SOPs/member-creation-flow.md
  - Library/SOPs/agent-design-methodology.md
  - Library/SOPs/handoff-guide.md
---

# Structural Domain Analysis — Clio Agent Profile

**Source**: `.opencode/agents/clio.md` (170 lines)
**Target**: Translation Italian → English per team-wide profile migration
**Reference SOP**: `Library/SOPs/member-creation-flow.md` (step 3, handoff type: profile)

---

## 1. Current Profile Map — Complete Section Inventory

| # | Section | Subsection | Lines | Language | Notes |
|---|---------|-----------|-------|----------|-------|
| 1 | Frontmatter | description | 2–4 | IT | Multi-line YAML, 2 sentences |
| 2 | Frontmatter | mode | 5 | EN | `subagent` — no change |
| 3 | Frontmatter | model | 6 | EN | `opencode/big-pickle` — no change |
| 4 | Frontmatter | permission | 7–10 | EN | `bash: ask, edit: allow, read: allow` — no change |
| 5 | Title | `# Clio — Archivista Digitale del Team Olimpo` | 14 | IT | H1 heading |
| 6 | Identity | Paragraph (3 sentences) | 16–17 | IT | Core identity statement |
| 7 | Communication Style | Section title | 19 | IT | `Personalita' e stile di comunicazione` |
| 8 | Communication Style | Tone bullet | 20 | IT | `Tono` |
| 9 | Communication Style | Approach bullet | 21 | IT | `Approccio` |
| 10 | Communication Style | Transparency bullet | 22 | IT | `Trasparenza` |
| 11 | Communication Style | Detail attention bullet | 23 | IT | `Attenzione al dettaglio` |
| 12 | Communication Style | Adaptive comms bullet | 24 | IT | `Comunicazione adattiva` — contains member names |
| 13 | Operating Rules | Section title | 26 | IT | `Regole operative` |
| 14 | Operating Rules | Rule 1 | 27 | IT | **Language directive**: `Rispondi sempre in italiano.` |
| 15 | Operating Rules | Rule 2 | 28 | IT | No code — contains member ref (Efesto) |
| 16 | Operating Rules | Rule 3 | 29 | IT | No content interpretation |
| 17 | Operating Rules | Rule 4 | 30 | IT | Follow Hermes — contains member ref |
| 18 | Operating Rules | Rule 5 | 31 | IT | Verify before declaring done |
| 19 | Operating Rules | Rule 6 | 32 | IT | Document decisions |
| 20 | Competencies | Section title | 34 | IT | `Competenze` |
| 21 | Competencies | Subtitle: Document Management | 36 | IT | `Gestione documentale e catalogazione` |
| 22 | Competencies | Metadata bullet | 37 | IT | |
| 23 | Competencies | Controlled vocabularies | 38 | IT | |
| 24 | Competencies | Naming conventions | 39 | IT | |
| 25 | Competencies | Deduplication | 40 | IT | |
| 26 | Competencies | Taxonomy | 41 | IT | |
| 27 | Competencies | Document relations | 42 | IT | |
| 28 | Competencies | Subtitle: Conversion Workflow | 44 | IT | `Esecuzione workflow di conversione` |
| 29 | Competencies | Pipeline description | 45 | IT | Paths in code font: `Team/Inbox/` etc. |
| 30 | Competencies | Commands block (code) | 46–54 | EN/IT | Code = EN preserve; desc = IT translate |
| 31 | Competencies | Idempotence | 54 | IT | |
| 32 | Competencies | Subtitle: Post-conversion QC | 56 | IT | `Quality control post-conversione` |
| 33 | Competencies | Frontmatter verification | 57 | IT | |
| 34 | Competencies | Markdown structure | 58 | IT | |
| 35 | Competencies | Images check | 59 | IT | `![[...]]` syntax — preserve |
| 36 | Competencies | Integrity check | 60 | IT | |
| 37 | Competencies | DB-filesystem alignment | 61 | IT | |
| 38 | Competencies | Subtitle: Database management | 63 | IT | `Gestione database e indice` |
| 39 | Competencies | Querying bullets | 64–67 | IT | Paths to preserve: `Library/data/pdf_index.db`, `Library/data/pdf_converter.log` |
| 40 | Competencies | Subtitle: Formats and standards | 69 | IT | `Formati e standard` |
| 41 | Competencies | Markdown/YAML/Obsidian/PDF/OpenCode | 70–74 | IT | Obsidian syntax preserve |
| 42 | Competencies | Subtitle: OpenCode compliance | 76 | IT | `Verifica conformità OpenCode` |
| 43 | Competencies | Frontmatter/permission/changelog/recognition | 77–80 | IT | |
| 44 | Workflows | Section title | 82 | IT | `Flussi di lavoro` |
| 45 | Workflows | Workflow 1: Conversion pipeline | 84–96 | IT | Title + numbered steps |
| 46 | Workflows | Workflow 2: Periodic maintenance | 98–104 | IT | Title + numbered steps |
| 47 | Workflows | Workflow 3: OpenCode conformity | 106–115 | IT | Title + numbered steps |
| 48 | Workflows | Failure output note | 117 | IT | Path `Library/Handoff/verifica-conformita-...` |
| 49 | Workflows | Workflow 4: Feedback to Efesto | 119–144 | IT | Member name ref in title; template in code block |
| 50 | Interactions | Section title | 146 | IT | `Interazioni con il team` |
| 51 | Interactions | Hermes description | 147 | IT | Member name ×3 |
| 52 | Interactions | Atena description | 148 | IT | Member name ×2 |
| 53 | Interactions | Efesto description | 149 | IT | Member name |
| 54 | Interactions | User description | 150 | IT | |
| 55 | Limitations | Section title | 152 | IT | `Limitazioni` |
| 56 | Limitations | Not a developer | 153 | IT | Efesto ref |
| 57 | Limitations | Not an analyst | 154 | IT | |
| 58 | Limitations | Not a PM | 155 | IT | Hermes ref |
| 59 | Limitations | No infrastructure | 156 | IT | |
| 60 | Folder Structure | Section title | 158 | IT | `Struttura delle cartelle di riferimento` |
| 61 | Folder Structure | Path block (code) | 159–165 | EN | Paths only — preserve as-is |
| 62 | Output | Section title | 167 | EN | `Output` (same in both languages) |
| 63 | Output | Status reports | 168 | IT | Hermes ref |
| 64 | Output | Feedback files | 169 | IT | Efesto ref, `Library/Handoff/` path |
| 65 | Output | Enriched documents | 170 | IT | `Library/documents/` path |

**Total line items to modify: ~55–60** (majority of the file)
**Lines that stay unchanged: ~20** (paths, code blocks, frontmatter technical fields, permission block)

---

## 2. Elementi da Tradurre — Per Sezione

### 2.1 Frontmatter — `description:` (righe 2–4)
- **Testo attuale (IT)**: `Esperta di documentazione e verifica conformità per il vault Obsidian del Team Olimpo. Conosce tutte le convenzioni del vault e verifica la qualità dell'output destinato all'utente.`
- **Cosa fare**: Riscrivere in EN, ~150–200 char, operativa (cosa fa + quando invocarla), senza nomi membri.
- **Raccomandazione**: Allineare a standard Metis/Efesto. Includere trigger: "Use for PDF conversion, vault QC, and OpenCode agent conformity checks."
- **Linee guida SOP**: `description` deve essere in inglese, senza nomi di altri membri (checklist step 9, member-creation-flow.md).
- **Complessità**: Media — richiede riscrittura creativa, non traduzione letterale.

### 2.2 Section Titles (da tradurre)
| Current IT | Proposed EN | Note |
|------------|-------------|------|
| `# Clio — Archivista Digitale del Team Olimpo` | `# Clio — Vault Archivist & QC, Team Olimpo` | Allineare a formato `# <Nome> — <Ruolo EN>, Team Olimpo` |
| `## Identita'` | `## Identity` | Standard |
| `## Personalita' e stile di comunicazione` | `## Communication Style` | Standard Metis |
| `## Regole operative` | `## Operating Rules` | Standard |
| `## Competenze` | `## Competencies` | Standard |
| `### Gestione documentale e catalogazione` | `### Document Management & Cataloging` | |
| `### Esecuzione workflow di conversione` | `### Conversion Workflow Execution` | |
| `### Quality control post-conversione` | `### Post-Conversion Quality Control` | Already partly EN |
| `### Gestione database e indice` | `### Database & Index Management` | |
| `### Formati e standard` | `### Formats & Standards` | |
| `### Verifica conformità OpenCode` | `### OpenCode Conformity Checks` | |
| `## Flussi di lavoro` | `## Workflows` | Standard |
| `## Interazioni con il team` | `## Interactions` | Standard — omettere "con il team" |
| `## Limitazioni` | `## Limitations` | Standard |
| `## Struttura delle cartelle di riferimento` | `## Reference Folder Structure` | |
| `## Output` | `## Output` | Same in EN |

### 2.3 Identity (righe 16–17)
- Testo attuale: paragrafo che definisce Clio come "Musa della storia" / "archivista digitale"
- Preservare il riferimento mitologico ("Muse of History" → "Clio, Muse of History. Digital archivist...")
- **Attenzione**: non usare "custodisci" (custodian) letteralmente — meglio terminologia archivistica
- Raccomandazione: dividere in identity + header comment (2-3 righe human-readable), come da standard `.opencode/agents/metis.md` (linee 12-13)

### 2.4 Communication Style (righe 19–24)
- Tradurre interamente
- **Riga 24** contiene riferimenti a Hermes e Efesto: `con Hermes sei sintetica... nei report per Efesto sei dettagliata...`
  - ⚠️ **Da generalizzare**: rimuovere nomi membri, usare "with the orchestrator" / "in technical reports for the developer" o simile

### 2.5 Operating Rules (righe 26–32)
- **Riga 27 — DIRETTIVA LINGUA**: `Rispondi sempre in italiano.` → **DEVE diventare** `Always reply in English.`
  - Questo è il punto più critico della traduzione: cambiare la regola esplicita sulla lingua da IT a EN
- **Riga 28**: `Non modificare mai codice Python o script. Se uno strumento non funziona, produci un report di feedback.`
  - Menciona implicitamente Efesto (destinatario del feedback) → generalizzare
- **Riga 30**: `Ricevi istruzioni da Hermes.` → generalizzare: `Receive instructions from the orchestrator.`

### 2.6 Competencies (righe 34–81)
- Tradurre tutte le descrizioni dei bullet point (20+ elementi)
- **Non tradurre**: percorsi file (`Team/Inbox/`, `Library/documents/`, ecc.), sintassi Obsidian (`![[...]]`), comandi shell (`uv run python -m tools.pdf_converter ...`)
- **Riga 45**: `Ricevi istruzioni da Hermes` → generalizzare
- **Riga 67**: `Il database e' in Library/data/pdf_index.db. I log sono in Library/data/pdf_converter.log.` — tradurre solo la frase, non i path
- **Riga 74**: `OpenCode agent specifications` — già in inglese parziale, allineare

### 2.7 Workflows (righe 82–144)
- Tradurre titoli, descrizioni, e testo nei commenti degli step
- **Non tradurre**: comandi nei blocchi codice, path dei file
- **Riga 117**: path `Library/Handoff/verifica-conformita-<nome>-<timestamp>.md` — preservare
- **Workflow 4 (righe 119–144)**: titolo `Feedback verso Efesto`
  - ⚠️ **Riferimento a Efesto nel titolo** → rinominare in `Feedback to the Developer` o simile
  - Template feedback (righe 122–144): tradurre le label (`Data`, `Strumento`, `Tipo`, `Priorità`, `Descrizione`, ecc.)
  - **Riga 143**: `Suggerimento (opzionale)` → `Suggestion (optional)`

### 2.8 Interactions (righe 146–150)
- **Sezione interamente da riscrivere**: contiene riferimenti espliciti a Hermes (×3), Atena (×2), Efesto (×2), Utente
- ⚠️ **Attenzione**: SOP agent-design-methodology.md dice "Never mention specific team member names. The orchestrator manages routing."
- Raccomandazione: ristrutturare in formato "Receive / Produce" (come Metis profile, righe 96-103)
  - Receive: instructions (PDF conversion, priorities, conformity checks)
  - Produce: status reports, feedback reports, enriched documents

### 2.9 Limitations (righe 152–156)
- Tradurre interamente
- **Riga 153**: menziona Efesto → generalizzare: "produce a report for the developer"
- **Riga 155**: menziona Hermes → generalizzare: "Execute instructions from the orchestrator"

### 2.10 Folder Structure (righe 158–165)
- Titolo da tradurre
- Path nei blocchi codice: **preservare invariati**

### 2.11 Output (righe 167–170)
- **Riga 168**: `restituiti a Hermes nella risposta` → generalizzare
- **Riga 169**: `File di feedback per Efesto` → generalizzare
- Path `Library/Handoff/` e `Library/documents/` → preservare

---

## 3. Riferimenti a Nomi di Membri — Inventory Completo

Secondo la SOP `agent-design-methodology.md` (riga 46): *"Never mention specific team member names."*

| # | Riga | Nome Membro | Contesto | Azione Raccomandata |
|---|------|-------------|----------|---------------------|
| 1 | 24 | Hermes, Efesto | Comunicazione adattiva | Sostituire con "orchestrator" e "developer" |
| 2 | 30 | Hermes | Regola operativa 3 | Sostituire con "orchestrator" |
| 3 | 147 | Hermes (×3) | Interazioni | Ristrutturare in Receive/Produce |
| 4 | 148 | Atena (×2) | Interazioni | Ristrutturare in Receive/Produce |
| 5 | 149 | Efesto | Interazioni | Ristrutturare in Receive/Produce |
| 6 | 150 | Utente | Interazioni | Ristrutturare |
| 7 | 153 | Efesto | Limitazioni | Generalizzare |
| 8 | 155 | Hermes | Limitazioni | Generalizzare |
| 9 | 168 | Hermes | Output | Generalizzare |
| 10 | 169 | Efesto | Output | Generalizzare |

**Totale**: ~10 occorrenze di nomi membri da rimuovere/generalizzare.
**Raccomandazione**: Tradurre E riscrivere le sezioni interessate in un unico passaggio, non separare traduzione e refactoring.

---

## 4. Direttiva Lingua Esplicita

**Trovata alla riga 27**:
```
- **Rispondi sempre in italiano.**
```

Questa è l'unica istruzione esplicita sulla lingua nel profilo. Obbligatorio cambiarla in:
```
- **Always reply in English.**
```

Come da standard Metis (riga 19): `**Always reply in English.**`

---

## 5. Riferimenti Culturali e Linguistici Specifici

| Elemento | Rischio | Raccomandazione |
|----------|---------|-----------------|
| `Clio, la Musa della storia` | Riferimento mitologico diretto. OK in EN come "Clio, the Muse of History" | Preservare — è il nome mitologico dell'agente, non un gioco di parole italiano |
| `Archivista Digitale` | Termine italiano per "digital archivist" | Tradurre letteralmente, nessuna perdita culturale |
| `custodisci la Library` | "Custodisci" è un italianismo per un vault digitale | Preferire "maintain", "manage", "curate" |
| `nulla sfugge alla tua revisione` | Espressione idiomatica italiana | Tradurre senso: "nothing escapes your review" o "every detail is caught in your review" |
| `La coerenza e' la tua firma` | Metafora italiana | "Consistency is your signature" — funziona anche in EN |
| Nome `Efesto` | Nome mitologico greco (Hephaestus in EN) | Nel team si usa il nome greco `Efesto`; nella traduzione si può usare `Efesto` (nome del membro) o generalizzare con "developer". OPTO PER GENERALIZZARE (per SOP) |
| `kba-catalog` | Termine inglese interno | Preservare invariato |
| `pdf_converter` | Nome tool | Preservare invariato |
| Date format `nk-2400-0150` | Codice interno | Preservare invariato |

**Nessun gioco di parole, dialetto, o riferimento culturale strettamente italiano** che possa causare problemi di traduzione. Il profilo è in italiano standard tecnico.

---

## 6. Elementi Strutturali da Preservare ASSOLUTAMENTE

Questi elementi NON devono essere modificati nella struttura, solo eventualmente tradotti nel testo circostante:

1. **Sequenza delle sezioni**: Frontmatter → Title → Identity → Communication Style → Operating Rules → Competencies → Workflows → Interactions → Limitations → Folder Structure → Output
   - Questa sequenza segue lo standard `agent-design-methodology.md` (righe 14-24)
2. **Permission block** (righe 7-10): `bash: ask, edit: allow, read: allow` — invariato
3. **Numero e ordine delle Regole Operative** (6 regole): da preservare come 6 punti, anche se riscritti
4. **Numero e ordine delle 6 sottosezioni Competenze**: preservare raggruppamento logico
5. **Numero e ordine dei 4 Workflow**: preservare con i loro step numerati
6. **Comandi shell** nei blocchi codice: preservare esattamente (righe 47-53, 86-96, 99-104, 107-115)
7. **Percorsi filesystem**: tutti i path (`Team/Inbox/`, `Library/documents/`, ecc.)
8. **Template feedback** (righe 122-144): preservare la struttura markdown, tradurre solo le etichette
9. **Blocco delle Limitazioni**: 4 punti, mantenerli come 4
10. **Blocco Output**: 3 punti, mantenerli come 3

---

## 7. Path e Comandi da NON Tradurre (preservare invariati)

| Riga | Elemento | Tipo |
|------|----------|------|
| 45 | `Team/Inbox/`, `Library/documents/`, `Library/assets/images/`, `Library/data/pdf_index.db` | Path |
| 47 | `uv run python -m tools.pdf_converter init` | Comando |
| 48 | `uv run python -m tools.pdf_converter convert <file>` | Comando |
| 49 | `uv run python -m tools.pdf_converter convert-all` | Comando |
| 50 | `uv run python -m tools.pdf_converter search <query>` | Comando |
| 51 | `uv run python -m tools.pdf_converter list` | Comando |
| 52 | `uv run python -m tools.pdf_converter stats` | Comando |
| 53 | `--force`, `--verbose`, `--limit` | Flag |
| 59 | `![[...]]` | Sintassi Obsidian |
| 67 | `Library/data/pdf_index.db`, `Library/data/pdf_converter.log` | Path |
| 117 | `Library/Handoff/verifica-conformita-<nome>-<timestamp>.md` | Path template |
| 159-165 | Path nel blocco folder structure | Path |
| 169 | `Library/Handoff/` | Path |
| 170 | `Library/documents/` | Path |
| 74 | `OpenCode agent specifications` | Nome proprio (parzialmente EN) |

---

## 8. Raccomandazioni per la Traduzione

### 8.1 Strategia
1. **Approccio**: traduzione + refactoring in unico passaggio (non separare)
2. **Ordinamento**: procedere top-down, sezione per sezione
3. **Modello di riferimento**: usare `.opencode/agents/metis.md` come template di stile EN
4. **Preservare la lunghezza**: non accorciare/diluire le descrizioni tecniche

### 8.2 Descrizione Frontmatter (priorità alta)
Riscrivere da zero seguendo lo standard ~150-200 char, operativa, senza nomi membri.

**Proposta**:
```
description: Vault archivist and QC specialist for Team Olimpo's Obsidian vault. Runs PDF conversion pipeline, validates Markdown structure and image links, enforces vault conventions, and audits OpenCode agent file conformity.
```
(197 caratteri — nel limite. Include trigger implicito: "use when PDF conversion or vault QC is needed")

### 8.3 Riscrittura Interazioni (priorità alta)
Rimuovere tutti i riferimenti a Hermes, Atena, Efesto, Utente. Strutturare come Metis:

```markdown
## Interactions

**Receive:**
- Conversion instructions from orchestrator (which PDFs, priorities, specific requests)
- Conformity check requests after Atena creates a new agent file

**Produce:**
- Status reports on conversion operations
- Quality check reports with errors found
- Feedback reports for tool issues (saved in `Library/Handoff/`)
- Enriched documents edited in-place in `Library/documents/`
```

### 8.4 Frontmatter — Header Comment (mancante)
Metis ha 2 righe header dopo il titolo (righe 12-13):
```
Thinking partner for brainstorming, strategic reflection, and complex problem-solving.
Does NOT execute tasks, write code, or produce generic documents.
```
Clio non ha questo header. **Aggiungerlo** nella versione tradotta, seguendo lo standard.

**Proposta**:
```
Vault archivist and quality control specialist for Team Olimpo's Obsidian knowledge base.
Does NOT write code, interpret document content, or decide processing priorities.
```

### 8.5 Traduzione Regola Lingua (critico)
Cambiare riga 27 da `Rispondi sempre in italiano.` a `Always reply in English.`
Posizionamento: primo bullet delle Operating Rules, come in Metis.

### 8.6 Formattazione Apostrofi
Tutto il profilo usa l'apostrofo dattilografico (`'`) invece dell'apostrofo tipografico (`'`). Es: `Identita'`, `integrita'`, `coerenza'`.
Nella traduzione EN: usare apostrofo tipografico standard (`'`) in parole come `don't`, `doesn't`, `it's`.

### 8.7 Template Feedback (Workflow 4)
Tradurre le label del template ma preservare la struttura markdown esatta.

---

## 9. Stima Complessità

| Fattore | Valutazione |
|---------|-------------|
| **Volume totale** | 170 righe |
| **Elementi da tradurre** | ~50-55 |
| **Elementi da preservare invariati** | ~20 (path, comandi, permission, mode, model) |
| **Nomi membri da rimuovere** | ~10 occorrenze |
| **Riscritture strutturali necessarie** | 2 (Interactions, Header comment) |
| **Sezioni da modificare** | 13 su 13 sezioni |
| **Giochi di parole italiani** | 0 |
| **Riferimenti culturali problematici** | 0 |

### Verdetto: COMPLESSITÀ MEDIA

**Motivazione**:
- **Non è semplice** (~15 minuti di lavoro minimo, richiede riscrittura strutturale + traduzione)
- **Non è complessa** (nessun tecnicismo intraducibile, nessun gioco di parole, struttura già chiara e ben organizzata)

**Tempo stimato per la traduzione**: 20-30 minuti per un traduttore esperto del dominio.

**Sezioni a maggiore sforzo**:
1. Interactions (da riscrivere completamente, non tradurre)
2. Frontmatter description (da riscrivere creativamente)
3. Competencies (alto volume di testo tecnico da tradurre)
4. Workflow 4 + template feedback (testo strutturato + traduzione)

**Sezioni a minore sforzo**:
1. Folder Structure (solo titolo + path invariati)
2. Output (3 frasi brevi)
3. Permission / mode / model (già in EN)

---

## 10. Checklist Pre-Traduzione (da consegnare a chi traduce)

- [ ] Frontmatter `description:` → riscrivere in EN (~150-200 char)
- [ ] Aggiungere header comment di 2 righe dopo il titolo
- [ ] Tradurre titolo H1
- [ ] Identity → tradurre + scorporare header
- [ ] Communication Style → tradurre tutto, rimuovere nomi membri
- [ ] Operating Rules → tradurre, cambiare direttiva lingua, rimuovere nomi membri
- [ ] Competencies → tradurre 6 sottosezioni + tutti i bullet, preservare path/comandi
- [ ] Workflows → tradurre titoli e descrizioni, preservare blocchi codice
- [ ] Workflow 4 → rimuovere "Efesto" dal titolo, tradurre template feedback
- [ ] Interactions → RISCIVERE completamente in formato Receive/Produce
- [ ] Limitations → tradurre, rimuovere nomi membri
- [ ] Folder Structure → tradurre solo titolo
- [ ] Output → tradurre, rimuovere nomi membri
- [ ] Verificare: nessun path tradotto, nessun comando modificato
- [ ] Verificare: nessun nome membro nel file finale
- [ ] Verificare: direttiva `Always reply in English.` presente
