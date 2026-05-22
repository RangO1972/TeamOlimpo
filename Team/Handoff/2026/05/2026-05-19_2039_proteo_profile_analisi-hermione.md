---
data: 2026-05-19
timestamp: 2026-05-19T20:39:48
agent: proteo
task_id: T-NNN
invocation: 1
type: profile
status: completed
priority: medium
title: "Structural domain analysis — Hermione profile translation prep"
quality_score: 5
external_review: false
next_action: "Hermes: analysis ready. Hermione profile is COMPLEX — 24+ member-name references, massive Interaction table rewrite needed, 6-step Process section, and frontmatter description requires creative EN rewrite."
completion_notes: "Full structural mapping of hermione.md (174 lines). Every translatable element inventoried by section. Member name references comprehensively flagged (24+ occurrences). Cultural/technical preservation notes provided. Estimated 35-50 min translation effort."
output_refs:
  - .opencode/agents/hermione.md
  - Library/SOPs/handoff-guide.md
---

# Structural Domain Analysis — Hermione Agent Profile

**Source**: `.opencode/agents/hermione.md` (174 lines)
**Target**: Translation Italian → English per team-wide profile migration
**Reference**: Clio profile analysis at `Library/Handoff/2026/05/2026-05-19_2209_proteo_profile_analisi-clio.md` (same methodology)

---

## 1. Current Profile Map — Complete Section Inventory

| # | Section | Subsection | Lines | Language | Notes |
|---|---------|-----------|-------|----------|-------|
| 1 | Frontmatter | description | 2–4 | IT | Multi-line YAML, 2 sentences (~190 char) |
| 2 | Frontmatter | mode | 5 | EN | `subagent` — no change |
| 3 | Frontmatter | model | 6 | EN | `opencode/big-pickle` — no change |
| 4 | Frontmatter | permission | 7–10 | EN | `bash: deny, edit: allow, read: allow, task: deny` — no change |
| 5 | Title | `# Hermione — Scrittrice Tecnica Profonda del Team Olimpo` | 15 | IT | H1 heading |
| 6 | Identity | Section title `## Identita'` | 17 | IT | Apostrofo dattilografico |
| 7 | Identity | Paragraph (4 sentences) | 19 | IT | Core identity statement — contains member refs (Proteo, Dike, Metis) |
| 8 | Communication Style | Section title | 21 | IT | `Personalita' e stile di comunicazione` |
| 9 | Communication Style | Tone bullet | 23 | IT | `Tono` |
| 10 | Communication Style | Attitude bullet | 24 | IT | `Atteggiamento` — mentions "other members" |
| 11 | Communication Style | Language bullet | 25 | IT | `Linguaggio` |
| 12 | Communication Style | Rhythm bullet | 26 | IT | `Ritmo` |
| 13 | Communication Style | Depth bullet | 27 | IT | `Profondita'` |
| 14 | Communication Style | **Language directive** | 28 | IT | **`Rispondi sempre in italiano.`** |
| 15 | Operating Rules | Section title | 30 | IT | `Regole operative fondamentali` |
| 16 | Operating Rules | Rule 1 | 32 | IT | File autonomy |
| 17 | Operating Rules | Rule 2 | 33 | IT | Source fidelity |
| 18 | Operating Rules | Rule 3 | 34 | IT | Obsidian conventions |
| 19 | Operating Rules | Rule 4 | 35 | IT | Critical synthesis |
| 20 | Operating Rules | Rule 5 | 36 | IT | Source transparency |
| 21 | Competencies | Section title | 38 | IT | `Competenze` |
| 22 | Competencies | Sub 1: Scrittura tecnica profonda | 40 | IT | Title + 4 bullets |
| 23 | Competencies | — bullet: synthesis | 42 | IT | Contains member refs: Proteo, Dike, Metis |
| 24 | Competencies | — bullet: IA | 43 | IT | |
| 25 | Competencies | — bullet: reliability | 44 | IT | |
| 26 | Competencies | — bullet: document tone | 45 | IT | |
| 27 | Competencies | Sub 2: Padronanza Markdown | 47 | IT | Title + 5 bullets |
| 28 | Competencies | — bullet: standard syntax | 49 | IT | |
| 29 | Competencies | — bullet: Obsidian-specific syntax | 50–54 | IT | Wikilinks, Embeds, Callouts, Block IDs — preserves syntax `![[...]]`, `> [!INFO]` |
| 30 | Competencies | — bullet: frontmatter YAML | 55 | IT | |
| 31 | Competencies | Sub 3: Navigazione Vault | 57 | IT | Title + 4 bullets |
| 32 | Competencies | — bullet: naming conventions | 59 | IT | |
| 33 | Competencies | — bullet: path management | 60 | IT | Paths: `../assets/images/<slug>/` |
| 34 | Competencies | — bullet: linking strategy | 61 | IT | |
| 35 | Competencies | — bullet: KBA integration | 62 | IT | Dike ref |
| 36 | Competencies | Sub 4: Fonti eterogenee | 64 | IT | Title + 3 bullets |
| 37 | Competencies | — bullet: agent outputs | 66 | IT | Contains member refs: Proteo, Dike |
| 38 | Competencies | — bullet: tech documents | 67 | IT | |
| 39 | Competencies | — bullet: multi-source synthesis | 68 | IT | |
| 40 | Workflow | Section title | 70 | IT | `Processo operativo` |
| 41 | Workflow | Step 1: Ricezione e analisi | 72–75 | IT | 3 bullets |
| 42 | Workflow | Step 2: Analisi strutturale | 77–81 | IT | 4 bullets |
| 43 | Workflow | Step 3: Sintesi (Drafting) | 83–87 | IT | 5 bullets |
| 44 | Workflow | Step 4: Formattazione Vault | 89–93 | IT | 5 bullets |
| 45 | Workflow | Step 5: Quality Check | 95–105 | IT | Title + checklist (10 items) |
| 46 | Workflow | Step 6: Consegna | 107–110 | IT | 3 bullets — contains Hermes ref |
| 47 | Interactions | Section title | 112 | IT | `Interazioni con il team` |
| 48 | Interactions | Table | 114–120 | IT | **Table with 5 rows** — contains 7 member names (Hermes, Proteo, Pythagoras, Dike, Metis, Clio, Efesto) |
| 49 | Interactions | Note | 122 | IT | "Non interagisci mai direttamente con l'utente" |
| 50 | Limitations | Section title | 124 | IT | `Limitazioni` |
| 51 | Limitations | Limitation 1 | 126 | IT | No original research — Proteo, Pythagoras ref |
| 52 | Limitations | Limitation 2 | 127 | IT | No conformity check — Clio ref |
| 53 | Limitations | Limitation 3 | 128 | IT | No code — Efesto ref |
| 54 | Limitations | Limitation 4 | 129 | IT | No member creation — Atena ref |
| 55 | Limitations | Limitation 5 | 130 | IT | No orchestration — Hermes ref |
| 56 | Limitations | Limitation 6 | 131 | IT | No config files — Efesto, Clio ref |
| 57 | Output Format | Section title | 133 | IT | `Formato di output` |
| 58 | Output Format | Template | 137–164 | EN/IT | Code block — structure EN, comments IT |
| 59 | Output Format | Note on special docs | 166 | IT | Template note |
| 60 | Guiding Principles | Section title | 168 | IT | `Principi guida` |
| 61 | Guiding Principles | Principle 1 | 170 | IT | Depth over summary |
| 62 | Guiding Principles | Principle 2 | 171 | IT | Source fidelity |
| 63 | Guiding Principles | Principle 3 | 172 | IT | Structure as service |
| 64 | Guiding Principles | Principle 4 | 173 | IT | Conventions non-negotiable |
| 65 | Guiding Principles | Principle 5 | 174 | IT | Source transparency |

**Total line items to modify: ~58-65** (majority of the file — similar volume to Clio)
**Lines that stay unchanged: ~15-20** (paths, code blocks, frontmatter technical fields, permission block, Obsidian syntax examples)

---

## 2. Elementi da Tradurre — Per Sezione

### 2.1 Frontmatter — `description:` (righe 2–4)

- **Testo attuale (IT)**:
  ```
  description: Scrittrice Tecnica Profonda del Team Olimpo. Sintetizza fonti complesse
    e output di agenti in file Markdown strutturati, pronti per il vault Obsidian. Usa
    quando serve produrre documentazione tecnica profonda da fonti fornite.
  ```
- **Cosa fare**: Riscrivere in EN, ~150–200 char, operativa (cosa fa + quando invocarla), senza nomi membri.
- **Raccomandazione**: Allineare allo standard `description` EN già usato per Clio/Metis/Efesto. Includere trigger.
- **Linee guida SOP**: `description` deve essere in inglese, senza nomi di altri membri.
- **Complessità**: Media — richiede riscrittura creativa, non traduzione letterale.

### 2.2 Section Titles (da tradurre)

| Current IT | Proposed EN | Note |
|------------|-------------|------|
| `# Hermione — Scrittrice Tecnica Profonda del Team Olimpo` | `# Hermione — Deep Technical Writer, Team Olimpo` | Allineare formato `# <Nome> — <Ruolo EN>, Team Olimpo` |
| `## Identita'` | `## Identity` | Standard |
| `## Personalita' e stile di comunicazione` | `## Communication Style` | Standard |
| `## Regole operative fondamentali` | `## Core Operating Rules` | "Core" aggiunge chiarezza |
| `## Competenze` | `## Competencies` | Standard |
| `### 1. Scrittura tecnica profonda e sintesi critica` | `### 1. Deep Technical Writing & Critical Synthesis` | |
| `### 2. Padronanza del formato Markdown (Obsidian Flavor)` | `### 2. Markdown Mastery (Obsidian Flavor)` | |
| `### 3. Navigazione e struttura del Vault` | `### 3. Vault Navigation & Structure` | |
| `### 4. Elaborazione di fonti eterogenee` | `### 4. Heterogeneous Source Processing` | |
| `## Processo operativo` | `## Operational Process` | |
| `## Interazioni con il team` | `## Team Interactions` | |
| `## Limitazioni` | `## Limitations` | Standard |
| `## Formato di output` | `## Output Format` | |
| `## Principi guida` | `## Guiding Principles` | |

### 2.3 Identity (righe 17–19)

- **Testo attuale**: Paragrafo che definisce Hermione come "figlia di Hermes e dell'istruzione" — colei che trasforma flusso di informazioni in architettura scritta.
- **⚠️ Contiene riferimenti a membri**: "ricerche di Proteo, report di Dike, analisi di Metis" (line 19)
- **Raccomandazione**: Preservare il riferimento mitologico ("daughter of Hermes and instruction" → OK in EN). Rimuovere i nomi dei membri: sostituire con "output from the Researcher, the KBA Analyst, the Strategist" o generalizzazioni simili.
- **Attenzione**: "figlia di Hermes" è un gioco di ruolo (Hermes è l'orchestrator). In EN va preservato ma reso come "Hermes" (nome del membro orchestrator, ammissibile in contesto mitologico/ruolo) o generalizzato. **Raccomandazione**: dato che "Hermes" è il nome del membro orchestrator, valutare se va generalizzato o se si può tenere come parte della lore del personaggio. SOP dice "Never mention specific team member names" — ma "Hermes" potrebbe essere eccezione perché è il nome del ruolo orchestrator. **Da decidere durante la traduzione.**

### 2.4 Communication Style (righe 21–28)

- Tradurre interamente (6 bullet points)
- **Riga 28 — DIRETTIVA LINGUA**: `- **Rispondi sempre in italiano.**` → DEVE diventare `- **Always reply in English.**`
- **Riga 24**: "Ripercorri il lavoro di altri membri" — "other members" è già generico, OK in EN come "other members' work"
- **Riga 26**: "La coerenza strutturale e' una virtu' cardinale" — idiomatica, tradurre il senso: "Structural consistency is a cardinal virtue"

### 2.5 Core Operating Rules (righe 30–36)

- Tradurre tutte e 5 le regole
- **Nessun nome membro esplicito** in questa sezione — più facile delle altre
- Regola 3 menziona `Library/SOPs/obsidian-vault-conventions.md` — preservare path invariato
- Regola 5: "Usa riferimenti espliciti alla fonte" — traduzione diretta

### 2.6 Competencies (righe 38–68)

- Tradurre tutte e 4 le sottosezioni + descrizioni bullet
- ⚠️ **Riga 42** (Competency 1, bullet 1): contiene riferimenti a Proteo, Dike, Metis → generalizzare
- ⚠️ **Riga 62** (Competency 3, bullet 4): "record KBA di Dike" → generalizzare: "KBA records from the Risk Analyst"
- ⚠️ **Riga 66** (Competency 4, bullet 1): "ricerca di Proteo, scoring di Dike" → generalizzare: "research output, scoring data"
- **Non tradurre**: sintassi Obsidian (`[[nota]]`, `![[img.png|300]]`, `> [!INFO]`, ` ^nome-id`), tag esempio (`kba`, `deltav`, `security`, `report`), path (`../assets/images/<slug>/`)

### 2.7 Operational Process (6 steps, righe 70–110)

- **Sezione più lunga del profilo (~40 righe)** — tradurre interamente
- Step 1 (righe 72–75): tradurre 3 bullet — "Library/Handoff/" path preservare
- Step 2 (righe 77–81): tradurre 4 bullet — tag esempi (`kba`, `deltav`, `security`, `report`) preservare come sono (sono già EN)
  - **Riga 81**: "Library/documents/" path preservare
- Step 3 (righe 83–87): tradurre 5 bullet
- Step 4 (righe 89–93): tradurre 5 bullet — sintassi Obsidian preservare
  - **Riga 90**: `[testo](url)` e `[[wikilink]]` preservare
  - **Riga 91**: `![[../assets/images/<slug>/img.png|300]]` preservare
- Step 5 (righe 95–105): tradurre titolo + 10 item checklist
  - **Riga 100**: `../assets/images/<slug>/` preservare
  - **Riga 101**: `[[wikilink]]` preservare
  - **Riga 102**: `[text](url)` preservare
- Step 6 (righe 107–110): tradurre 3 bullet
  - **Riga 108**: "Library/documents/" preservare
  - **Riga 109**: "Library/Handoff/" + "Hermes" → **nome membro da generalizzare**
  - **Riga 110**: "Clio" → **nome membro da generalizzare**

### 2.8 Team Interactions (righe 112–122)

- **Sezione interamente da riscrivere**: contiene tabella con 7 nomi membri espliciti (Hermes, Proteo, Pythagoras, Dike, Metis, Clio, Efesto)
- **⚠️ CRITICO**: La SOP richiede di non menzionare nomi specifici. Questa tabella va completamente riprogettata.
- Raccomandazione: sostituire tabella con formato "Receive / Produce" (come Metis profile):
  - Receive: brief and source materials (from orchestrator), research outputs, reports and analyses
  - Produce: structured Markdown documents, completion confirmations, vault-ready files for QC verification
- **Riga 122**: "Non interagisci mai direttamente con l'utente" — tradurre e preservare come nota

### 2.9 Limitations (righe 124–131)

- Tradurre titolo e tutte e 6 le limitazioni
- ⚠️ **Ogni limitazione contiene un nome membro**:
  - Riga 126: Proteo, Pythagoras → generalizzare: "Researcher"
  - Riga 127: Clio → generalizzare: "Vault Archivist" o "QC specialist"
  - Riga 128: Efesto → generalizzare: "Developer"
  - Riga 129: Atena → generalizzare: "HR Manager" o "Agent Designer"
  - Riga 130: Hermes → generalizzare: "orchestrator"
  - Riga 131: Efesto, Clio → generalizzare: "Developer", "Vault Archivist"

### 2.10 Output Format (righe 133–166)

- Tradurre titolo e paragrafo introduttivo
- **Template code block** (righe 137–164): non tradurre la struttura Markdown. Tradurre i commenti/hint in italiano (es. "se applicabile" → "if applicable", "opzionale" → "optional")
- **Riga 166**: tradurre

### 2.11 Guiding Principles (righe 168–174)

- Tradurre titolo e tutti e 5 i principi
- **Riga 168**: `Principi guida` → `Guiding Principles`
- **Riga 173**: "obsidian-vault.md" — il nome del file di convenzioni è `obsidian-vault-conventions.md` nel path `Library/SOPs/`. In ogni caso il nome va preservato come path.

---

## 3. Riferimenti a Nomi di Membri — Inventory Completo

**⚠️ CRITICO**: Hermione ha un numero eccezionalmente alto di riferimenti (~24), il più alto tra i profili analizzati finora. La SOP `agent-design-methodology.md` richiede di non menzionare nomi specifici di membri.

| # | Linea | Nome Membro | Sezione | Azione Raccomandata |
|---|-------|-------------|---------|---------------------|
| 1 | 19 | Proteo | Identity | Generalizzare: "Researcher" |
| 2 | 19 | Dike | Identity | Generalizzare: "KBA Analyst / Risk Analyst" |
| 3 | 19 | Metis | Identity | Generalizzare: "Strategist" |
| 4 | 42 | Proteo | Competency 1 | Generalizzare |
| 5 | 42 | Dike | Competency 1 | Generalizzare |
| 6 | 42 | Metis | Competency 1 | Generalizzare |
| 7 | 62 | Dike | Competency 3 | Generalizzare: "the Risk Analyst" |
| 8 | 66 | Proteo | Competency 4 | Generalizzare |
| 9 | 66 | Dike | Competency 4 | Generalizzare |
| 10 | 109 | Hermes | Workflow Step 6 | Generalizzare: "orchestrator" |
| 11 | 110 | Clio | Workflow Step 6 | Generalizzare: "Vault Archivist" |
| 12 | 116 | Hermes | Interactions table | Riscrivere tabella |
| 13 | 116 | Proteo | Interactions table | Riscrivere tabella |
| 14 | 116 | Pythagoras | Interactions table | Riscrivere tabella |
| 15 | 116 | Dike | Interactions table | Riscrivere tabella |
| 16 | 116 | Metis | Interactions table | Riscrivere tabella |
| 17 | 116 | Clio | Interactions table | Riscrivere tabella |
| 18 | 116 | Efesto | Interactions table | Riscrivere tabella |
| 19 | 126 | Proteo | Limitation 1 | Generalizzare |
| 20 | 126 | Pythagoras | Limitation 1 | Generalizzare |
| 21 | 127 | Clio | Limitation 2 | Generalizzare |
| 22 | 128 | Efesto | Limitation 3 | Generalizzare |
| 23 | 129 | Atena | Limitation 4 | Generalizzare |
| 24 | 130 | Hermes | Limitation 5 | Generalizzare |
| 25 | 131 | Efesto | Limitation 6 | Generalizzare |
| 26 | 131 | Clio | Limitation 6 | Generalizzare |

**Totale: 26 occorrenze di nomi membri da rimuovere/generalizzare.**
**Raccomandazione**: Tradurre E riscrivere le sezioni interessate in un unico passaggio, non separare traduzione e refactoring.

---

## 4. Direttiva Lingua Esplicita

**Trovata alla riga 28**:

```
- **Rispondi sempre in italiano.**
```

Obbligatorio cambiarla in:

```
- **Always reply in English.**
```

Come da standard Metis (riga 19): `**Always reply in English.**`

---

## 5. Riferimenti Culturali e Linguistici Specifici

| Elemento | Rischio | Raccomandazione |
|----------|---------|-----------------|
| `Hermione, figlia di Hermes e dell'istruzione` | Riferimento mitologico greco. **Hermes** è anche il nome dell'orchestrator del team. | Preservare il riferimento mitologico. Decidere se "Hermes" come orchestrator va generalizzato o lasciato. Suggerimento: nella lore/identità si può lasciare "Hermes" (è backstory del personaggio), ma nelle sezioni operative va generalizzato in "orchestrator" |
| `Scrittrice Tecnica Profonda` | "Deep Technical Writer" suona bene in EN | Tradurre letteralmente, nessuna perdita culturale |
| `distilli, organizzi e restituisci` | Verbi italiani (3 verbi in sequenza) | "distill, organize, and return" — funziona in EN |
| `La coerenza strutturale e' una virtu' cardinale` | Metafora italiana | "Structural consistency is a cardinal virtue" — funziona in EN |
| `non fai riassunti superficiali` | Negazione enfatica | "you do not produce superficial summaries" |
| `non evapori il contenuto` | Metafora italiana (evaporare = perdere sostanza) | "you do not evaporate the content" — suona naturale in EN nel contesto |
| `Sintesi critica` | Termine tecnico, "critical synthesis" | Traduzione diretta: "critical synthesis" |
| Apostrofi dattilografici (`'`) in `Identita'`, `Profondita'`, `coerenza'`, `fedelta'`, `integrita'` | Non standard in EN | Nella traduzione EN usare apostrofo tipografico (`'`) solo dove necessario (contrazioni: `don't`, `doesn't`, `it's`). La maggior parte degli apostrofi italiani scompare in EN |
| `kba`, `deltav`, `security`, `report` (tag) | Già in inglese | Preservare invariati |
| Path `Library/SOPs/obsidian-vault-conventions.md` | Percorso interno | Preservare invariato |
| Path `Library/Handoff/`, `Library/documents/`, `../assets/images/<slug>/` | Percorsi interni | Preservare invariati |

**Nessun gioco di parole, dialetto, o riferimento culturale strettamente italiano** che possa causare problemi di traduzione. Il profilo è in italiano standard tecnico.

---

## 6. Elementi Strutturali da Preservare ASSOLUTAMENTE

Questi elementi NON devono essere modificati nella struttura, solo eventualmente tradotti nel testo circostante:

1. **Sequenza delle sezioni**: Frontmatter → Title → Identity → Communication Style → Operating Rules → Competencies → Process → Interactions → Limitations → Output Format → Guiding Principles
2. **Permission block** (righe 7–10): `bash: deny, edit: allow, read: allow, task: deny` — invariato
3. **Numero delle Regole Operative** (5 regole): preservare come 5 punti
4. **Numero e ordine delle 4 sottosezioni Competenze**: preservare raggruppamento logico
5. **Numero e ordine dei 6 Step del Processo Operativo**: preservare con i loro step numerati, inclusa la checklist di Step 5 (10 item)
6. **Numero delle Limitazioni** (6 punti): preservare come 6
7. **Numero dei Principi Guida** (5 punti): preservare come 5
8. **Template output** (righe 137–164): preservare la struttura Markdown, tradurre solo i commenti/etichette in italiano
9. **Percorsi filesystem**: tutti i path (`Library/Handoff/`, `Library/documents/`, `Library/SOPs/`, `../assets/images/<slug>/`)
10. **Sintassi Obsidian**: tutti gli esempi di sintassi (`[[wikilink]]`, `![[embed]]`, `> [!INFO]`, `[text](url)`, ` ^block-id`)

---

## 7. Path e Comandi da NON Tradurre (preservare invariati)

| Riga | Elemento | Tipo |
|------|----------|------|
| 34, 50, 173 | `Library/SOPs/obsidian-vault-conventions.md` | Path SOP |
| 51 | `[[nota]]`, `[[nota|alias]]`, `[[nota#sezione]]` | Sintassi Obsidian |
| 52 | `![[img.png|300]]`, `![[nota]]` | Sintassi Obsidian |
| 53 | `> [!INFO]`, `> [!WARNING]`, `> [!TIP]` | Sintassi Obsidian |
| 54 | ` ^nome-id` | Sintassi Obsidian |
| 55 | `tags: [a, b]` | Sintassi YAML |
| 59 | `nk-2400-0150.md` | Esempio naming |
| 60 | `../assets/images/<slug>/` | Path |
| 73 | `Library/Handoff/` | Path |
| 79 | `kba`, `deltav`, `security`, `report` | Tag esempi |
| 81 | `Library/documents/` | Path |
| 90 | `[testo](url)`, `[[wikilink]]` | Sintassi |
| 91 | `![[../assets/images/<slug>/img.png|300]]` | Path + sintassi |
| 100 | `../assets/images/<slug>/` | Path |
| 108 | `Library/documents/` | Path |
| 137–164 | Template code block | Struttura Markdown |

---

## 8. Raccomandazioni per la Traduzione

### 8.1 Strategia
1. **Approccio**: traduzione + refactoring in unico passaggio (non separare)
2. **Ordinamento**: procedere top-down, sezione per sezione
3. **Modelli di riferimento**: usare `.opencode/agents/metis.md` come template di stile EN (per Interactions, Language directive)
4. **Preservare la lunghezza**: non accorciare/diluire le descrizioni tecniche — Hermione è un profilo denso

### 8.2 Descrizione Frontmatter (priorità alta)
Riscrivere da zero seguendo lo standard ~150–200 char, operativa, senza nomi membri.

**Proposta**:
```
description: Deep technical writer for Team Olimpo. Synthesizes complex agent outputs and source materials into structured, vault-ready Markdown documents for the Obsidian knowledge base. Use when deep documentation from provided sources is needed.
```
(195 caratteri — nel limite. Include trigger implicito: "use when deep documentation is needed")

### 8.3 Riscrittura Interazioni (priorità alta — sezione più critica)
Rimuovere completamente la tabella. Strutturare come Metis (Receive/Produce):

```markdown
## Team Interactions

**Receive:**
- Briefs and source materials from the orchestrator (files in `Library/Handoff/`, research outputs, reports)
- Research output from the Researcher
- Reports and analyses from the Risk Analyst and Strategist

**Produce:**
- Structured Markdown documents saved to `Library/documents/` (or as specified in the brief)
- Completion confirmations returned to the orchestrator
- Vault-ready files for downstream QC verification

You never interact directly with the user (Team Olimpo protocol).
```

### 8.4 Header Comment (mancante)
Metis ha 2 righe header dopo il titolo. Hermione NON ha questo header. **Aggiungerlo** nella versione tradotta.

**Proposta**:
```markdown
Deep technical writer for Team Olimpo. Synthesizes complex sources into structured, vault-ready Markdown.
Does NOT conduct original research, write code, or orchestrate team workflows.
```

### 8.5 Traduzione Limitation 6 (più complessa)
Riga 131: `Non modifichi file di configurazione: non tocchi .obsidian/ o script di automazione (compito di Efesto/Clio).`
- Due nomi membri da generalizzare
- `.obsidian/` path da preservare
- **Proposta**: "Do not modify configuration files: do not touch `.obsidian/` or automation scripts (task of the Developer / Vault Archivist)."

### 8.6 Template Output — Traduzione commenti
Il template (righe 137–164) ha commenti in italiano all'interno del blocco codice:
- Riga 142: `# se applicabile` → `# if applicable`
- Riga 148: `opzionale` → `optional`
- Riga 156: `Nota importante sintetizzata dalla fonte.` → `Important note synthesized from the source.`

La struttura YAML e Markdown del template rimane invariata.

### 8.7 Principio 173 — Nome file convenzioni
Riga 173: `Le regole di obsidian-vault.md sono legge.`
- Nota: il file si chiama `obsidian-vault-conventions.md` (non `obsidian-vault.md`)
- **Raccomandazione**: nella traduzione, correggere il nome del file al path completo: `Library/SOPs/obsidian-vault-conventions.md`
- Traduzione: "The rules of `Library/SOPs/obsidian-vault-conventions.md` are law."

### 8.8 Riferimento a "Hermes" nella Identity
La lore identitaria dice "figlia di Hermes e dell'istruzione". Dato che nel Team Olimpo Hermes è l'orchestrator:
- **Opzione A**: Preservare "Hermes" come lore mitologica (è backstory del personaggio, non routing operativo)
- **Opzione B**: Generalizzare in "daughter of the messenger god and instruction" (puramente mitologico, nessun riferimento al membro)

**Raccomandazione (debole)**: Opzione A. È l'unico luogo nel profilo dove "Hermes" appare come riferimento mitologico/genitoriale, non operativo. Le altre occorrenze (righe 109, 116, 130) vanno invece generalizzate.

---

## 9. Stima Complessità

| Fattore | Valutazione |
|---------|-------------|
| **Volume totale** | 174 righe |
| **Elementi da tradurre** | ~58-65 |
| **Elementi da preservare invariati** | ~15-20 (path, sintassi, permission, mode, model) |
| **Nomi membri da rimuovere** | ~26 occorrenze (molto più di Clio: 10) |
| **Riscritture strutturali necessarie** | 3 (Interactions tabella → formato Receive/Produce, Header comment da aggiungere, Limitation 6) |
| **Sezioni da modificare** | 11 su 11 sezioni |
| **Giochi di parole italiani** | 0 |
| **Riferimenti culturali problematici** | 1 (Hermes nella lore — borderline) |

### Verdetto: COMPLESSITÀ ALTA

**Motivazione**:
- **Volume comparabile a Clio** (170 vs 174 righe) ma **più complesso** per due fattori:
  1. **26 riferimenti a nomi membri** (vs Clio: 10) — 2.6× più refactoring
  2. **Sezione Processo Operativo** con 6 step strutturati + checklist 10 item (vs Clio: 4 workflow concisi)
  3. **Tabella Interazioni** da smantellare con 7 nomi membri in unica struttura tabellare
- **Non è semplice** (richiede 35-50 minuti di lavoro)
- **Non è estremo** (nessun tecnicismo intraducibile, struttura chiara, modello Clio già disponibile)

**Tempo stimato per la traduzione**: 35-50 minuti per un traduttore esperto del dominio.

**Sezioni a maggiore sforzo**:
1. **Interactions** (righe 112–122): tabella da riscrivere completamente in formato Receive/Produce
2. **Competencies** (righe 38–68): alto volume di testo tecnico + 9 riferimenti a nomi membri da generalizzare
3. **Limitations** (righe 124–131): tutte e 6 le limitazioni contengono nomi membri
4. **Operational Process** (righe 70–110): sezione più lunga (~40 righe) con struttura complessa
5. **Frontmatter description** (righe 2–4): da riscrivere creativamente

**Sezioni a minore sforzo**:
1. **Operating Rules** (righe 30–36): nessun nome membro, traduzione diretta
2. **Output Format template** (righe 133–166): per lo più struttura invariata, solo commenti da tradurre
3. **Guiding Principles** (righe 168–174): traduzione lineare
4. **Permission/mode/model** (righe 5–10): già in EN

---

## 10. Checklist Pre-Traduzione (da consegnare a chi traduce)

- [ ] Frontmatter `description:` → riscrivere in EN (~150-200 char)
- [ ] Aggiungere header comment di 2 righe dopo il titolo (standard Metis)
- [ ] Tradurre titolo H1: `# Hermione — Deep Technical Writer, Team Olimpo`
- [ ] Identity → tradurre + valutare se tenere "Hermes" nella lore o generalizzare
- [ ] Communication Style → tradurre 6 bullet, cambiare direttiva lingua in "Always reply in English."
- [ ] Operating Rules → tradurre 5 regole (nessun nome membro — facile)
- [ ] Competencies → tradurre 4 sottosezioni + tutti i bullet, generalizzare 9 nomi membri, preservare sintassi/path
- [ ] Operational Process → tradurre 6 step + checklist 10 item, generalizzare Hermes/Clio in Step 6
- [ ] Interactions → **RISCIVERE completamente**: smantellare tabella, creare formato Receive/Produce
- [ ] Limitations → tradurre 6 item, generalizzare 10+ nomi membri
- [ ] Output Format → tradurre titolo e commenti nel template, struttura invariata
- [ ] Guiding Principles → tradurre 5 principi, correggere `obsidian-vault.md` → `obsidian-vault-conventions.md`
- [ ] Verificare: nessun path tradotto, nessuna sintassi Obsidian modificata
- [ ] Verificare: nessun nome membro nel file finale (eccetto eventuale lore Hermes in Identity)
- [ ] Verificare: direttiva `Always reply in English.` presente in Communication Style
