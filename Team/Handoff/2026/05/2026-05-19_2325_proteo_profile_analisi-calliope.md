---
data: 2026-05-19
timestamp: 2026-05-19T23:25:00
agent: proteo
task_id: T-NNN
invocation: 1
type: profile
status: completed
priority: medium
title: "Structural domain analysis — Calliope profile translation prep"
quality_score: 5
external_review: false
next_action: "Hermes: analysis ready. The Calliope profile requires medium complexity translation with ~40 elements to localize, 6 member-name references to generalize, and one critical frontmatter inconsistency to resolve."
completion_notes: "Full structural mapping of calliope.md (111 lines). Every translatable element inventoried by section. Member name references flagged. Frontmatter discrepancy detected: description field describes a different role (creative documentation) than the body (mythological naming). Path inconsistency noted: Team/Registro.md vs Team/Members/Registro.md."
output_refs:
  - .opencode/agents/calliope.md
  - .opencode/agents/clio.md
  - Library/SOPs/member-creation-flow.md
  - Library/SOPs/agent-design-methodology.md
  - Library/SOPs/handoff-guide.md
  - Team/Members/Registro.md
---

# Structural Domain Analysis — Calliope Agent Profile (Translation Preparation)

**Source**: `.opencode/agents/calliope.md` (111 lines)
**Target**: Translation Italian → English per team-wide profile migration
**Reference SOP**: `Library/SOPs/member-creation-flow.md` (step 3, handoff type: profile)

---

## 0. Critical Pre-Analysis Findings

### ⚠️ FINDING 1: Frontmatter Description Inconsistency

The `description` field (lines 2–4) describes a **different role** from the rest of the profile:

| Element | Described Role | Verdict |
|---------|---------------|---------|
| `description` frontmatter (l.2–4) | *"Specialista in documentazione creativa e narrativa […] gestisce la voce del brand e cura la newsletter"* | ❌ **MISMATCH** — describes a comms/content role |
| H1 title (l.13) | *"Specialista di Nomenclatura Mitologica del Team Olimpo"* | ✅ Matches AGENTS.md |
| AGENTS.md system prompt | *"Mythological Naming Specialist"* | ✅ Consistent with body |

**Impact**: The frontmatter description must be **rewritten from scratch** in English to describe the mythological naming role, not translated from the current text. This is not a translation task — it is a **correction**.

**Recommended EN description** (~150-200 chars):
```
description: Mythological naming specialist for Team Olimpo. Use when a new agent, project, tool, or concept needs a name rooted in classical mythology with symbolic and etymological fit analysis.
```

### ⚠️ FINDING 2: Path Inconsistency — `Team/Registro.md`

The profile references `Team/Registro.md` (lines 27, 76), but the actual file is at `Team/Members/Registro.md`. This path must be corrected during translation.

Also: `Team Inbox/` (line 111) should be `Team/Inbox/` per current conventions.

---

## 1. Current Profile Map — Complete Section Inventory

| # | Section | Subsection | Lines | Language | Notes |
|---|---------|-----------|-------|----------|-------|
| 1 | Frontmatter | `description` | 2–4 | IT | ⚠️ Wrong role (docs/comms, not naming) |
| 2 | Frontmatter | `mode` | 5 | EN | `subagent` — no change |
| 3 | Frontmatter | `model` | 6 | EN | `opencode/big-pickle` — no change |
| 4 | Frontmatter | `permission` | 7–10 | EN | `edit: allow, read: allow` — no change |
| 5 | **Title** | `# Calliope — Specialista di Nomenclatura Mitologica del Team Olimpo` | 13 | IT | H1 — includes role title |
| 6 | **Identity** | Section title | 15 | IT | `## Identita'` |
| 7 | **Identity** | Paragraph (4 sentences) | 16 | IT | Mythological origin + mission statement. Contains Greek etymology (`kallos` + `ops`). |
| 8 | **Personality & Style** | Section title | 18 | IT | `## Personalita' e stile di comunicazione` |
| 9 | **Personality & Style** | Bullet: Tono | 19 | IT | Tone description |
| 10 | **Personality & Style** | Bullet: Approccio | 20 | IT | Approach description |
| 11 | **Personality & Style** | Bullet: Struttura | 21 | IT | Structure of proposals |
| 12 | **Personality & Style** | Bullet: Onesta' intellettuale | 22 | IT | Intellectual honesty rule |
| 13 | **Operating Rules** | Section title | 24 | IT | `## Regole operative` |
| 14 | **Operating Rules** | Rule 1 — **Language directive** | 25 | IT | `**Rispondi sempre in italiano.**` |
| 15 | **Operating Rules** | Rule 2 — Greek name preference | 26 | IT | Contains member names (Hermes, Atena, Proteo, Efesto) as examples |
| 16 | **Operating Rules** | Rule 3 — Registry check | 27 | IT | Path `Team/Registro.md` (⚠️ wrong path) |
| 17 | **Operating Rules** | Rule 4 — No reassignment | 28 | IT | |
| 18 | **Operating Rules** | Rule 5 — Brand conflicts | 29 | IT | Contains brand examples (Apollo GraphQL/NASA, AWS Athena) |
| 19 | **Competencies** | Section title | 31 | IT | `## Competenze` |
| 20 | **Competency 1** | Subtitle: Classical mythology | 33 | IT | `### Conoscenza enciclopedica della mitologia classica` |
| 21 | **Competency 1** | Bullet: Olympian gods | 34 | IT | |
| 22 | **Competency 1** | Bullet: Titans & Primordials | 35 | IT | Greek names in Italian transliteration |
| 23 | **Competency 1** | Bullet: Heroes & Demigods | 36 | IT | Greek names in Italian transliteration |
| 24 | **Competency 1** | Bullet: Muses | 37 | IT | Lists all 9 Muses (incl. Calliope, Clio, Euterpe — overlap with team members is coincidental) |
| 25 | **Competency 1** | Bullet: Nymphs | 38 | IT | |
| 26 | **Competency 1** | Bullet: Daimones | 39 | IT | Mix of Greek/Latin transliteration |
| 27 | **Competency 1** | Bullet: Creatures & places | 40 | IT | Italian transliteration of Greek names |
| 28 | **Competency 2** | Subtitle: Roman mythology | 42 | IT | `### Mitologia romana e sincretismo` |
| 29 | **Competency 2** | Bullet 1 | 43 | IT | Greco-Roman correspondences |
| 30 | **Competency 2** | Bullet 2 | 44 | IT | Exclusively Roman figures |
| 31 | **Competency 2** | Bullet 3 | 45 | IT | Criteria (Greek preference) |
| 32 | **Competency 3** | Subtitle: Etymology | 47 | IT | `### Etimologia e semantica dei nomi` |
| 33 | **Competency 3** | Bullet 1 | 48 | IT | Root analysis (Prometheus example in IT) |
| 34 | **Competency 3** | Bullet 2 | 49 | IT | Meaning evaluation |
| 35 | **Competency 3** | Bullet 3 | 50 | IT | Phonetic evaluation (pronunciabilita', memorizzabilita', distinguibilita') |
| 36 | **Methodology** | Section title | 52 | IT | `## Metodologia: processo di associazione` |
| 37 | **Methodology** | Subtitle: Association types | 54 | IT | `### Tipologie di associazione (dalla piu' forte alla piu' debole)` |
| 38 | **Methodology** | Point 1: Direct association | 55 | IT | Example: `Efesto = forgiatore = sviluppatore` ⚠️ member name |
| 39 | **Methodology** | Point 2: Attribute association | 56 | IT | Example: `Hermes = messaggero = orchestratore` ⚠️ member name |
| 40 | **Methodology** | Point 3: Narrative association | 57 | IT | Example: `Proteo = trasformazioni = ricercatore` ⚠️ member name |
| 41 | **Methodology** | Point 4: Etymological association | 58 | IT | |
| 42 | **Methodology** | Subtitle: Quality criteria | 60 | IT | `### Criteri di qualita' (in ordine di priorita')` |
| 43 | **Methodology** | Criterion 1: Symbolic coherence (high weight) | 61 | IT | |
| 44 | **Methodology** | Criterion 2: Uniqueness (high weight) | 62 | IT | |
| 45 | **Methodology** | Criterion 3: Legibility (medium weight) | 63 | IT | `pronunciabile in italiano` — language-specific criterion ⚠️ |
| 46 | **Methodology** | Criterion 4: Depth (medium weight) | 64 | IT | |
| 47 | **Methodology** | Criterion 5: Elegance (low weight) | 65 | IT | |
| 48 | **Methodology** | Criterion 6: Recognizability (low weight) | 66 | IT | |
| 49 | **Methodology** | Subtitle: Anti-patterns | 68 | IT | `### Anti-pattern da evitare` (term is already EN) |
| 50 | **Methodology** | Anti-pattern 1: Forced association | 69 | IT | |
| 51 | **Methodology** | Anti-pattern 2: Single-attribute reduction | 70 | IT | |
| 52 | **Methodology** | Anti-pattern 3: Ignored negative connotations | 71 | IT | Examples: Medea, Crono |
| 53 | **Methodology** | Anti-pattern 4: Brand homonymy | 72 | IT | |
| 54 | **Process** | Section title | 74 | IT | `## Processo operativo` |
| 55 | **Process** | Step 1 | 75 | IT | ⚠️ Contains `Hermes (o da Atena)` — member names |
| 56 | **Process** | Step 2 | 76 | IT | Path `Team/Registro.md` ⚠️ wrong path |
| 57 | **Process** | Step 3 | 77 | IT | |
| 58 | **Process** | Step 4 | 78 | IT | |
| 59 | **Process** | Step 5 | 79 | IT | |
| 60 | **Output Format** | Section title | 81 | IT | `## Formato dell'output` |
| 61 | **Output Format** | Intro line | 83 | IT | `Per ogni proposta:` |
| 62 | **Output Format** | Template code block | 85–97 | IT | Template labels in Italian: "Nome raccomandato", "Chi e' nella mitologia", etc. |
| 63 | **Reference Sources** | Section title | 99 | IT | `## Fonti di riferimento` |
| 64 | **Reference Sources** | Bullet: Primary sources | 100 | IT | Greek/Latin works in Italian titles |
| 65 | **Reference Sources** | Bullet: Digital sources | 101 | EN | Already in English — Theoi.com, Britannica, etc. |
| 66 | **Reference Sources** | Bullet: Academic sources | 102 | IT | Italian editions listed |
| 67 | **Limitations** | Section title | 104 | IT | `## Limitazioni` |
| 68 | **Limitations** | Point 1 | 105 | IT | ⚠️ Contains `Atena` — member name |
| 69 | **Limitations** | Point 2 | 106 | IT | ⚠️ Contains `Proteo` — member name |
| 70 | **Limitations** | Point 3 | 107 | IT | |
| 71 | **Limitations** | Point 4 | 108 | IT | |
| 72 | **Output** | Section title | 110 | IT | `## Output` (same word in EN — no change needed) |
| 73 | **Output** | Line 1 | 110 | IT | ⚠️ Contains `Hermes o Atena` |
| 74 | **Output** | Line 2 | 111 | IT | Path `Team Inbox/` ⚠️ should be `Team/Inbox/` |

**Total line items to modify**: ~40–45 (majority of the file)
**Lines that stay unchanged**: ~8 (frontmatter technical fields, digital sources bullet, parts of code block content like mythology names)

---

## 2. Elementi da Tradurre — Per Sezione

### 2.1 Frontmatter — `description:` (righe 2–4)
- **Testo attuale (IT)**: `Specialista in documentazione creativa e narrativa per il Team Olimpo. Trasforma documentazione tecnica in contenuti coinvolgenti, gestisce la voce del brand e cura la newsletter del team.`
- **Problema**: ⚠️ Questa descrizione NON corrisponde al ruolo descritto nel corpo del file. Parla di documentazione creativa e newsletter, non di nomenclatura mitologica.
- **Cosa fare**: **Riscrivere da zero** in EN (~150-200 char, operativa, senza nomi membri). Non tradurre il testo attuale.
- **Raccomandazione**: La descrizione deve rispondere a: "When should Hermes invoke Calliope?" → When a new agent, project, tool, or concept needs a name.
- **Complessità**: Alta — richiede riscrittura creativa, non traduzione.

### 2.2 Section Titles (da tradurre / allineare)

| Current IT | Proposed EN | Note |
|------------|-------------|------|
| `# Calliope — Specialista di Nomenclatura Mitologica del Team Olimpo` | `# Calliope — Mythological Naming Specialist, Team Olimpo` | Allineare a formato Clio/Metis: `# <Nome> — <Ruolo EN>, Team Olimpo` |
| `## Identita'` | `## Identity` | Standard |
| `## Personalita' e stile di comunicazione` | `## Communication Style` | Standard Clio |
| `## Regole operative` | `## Operating Rules` | Standard |
| `## Competenze` | `## Competencies` | Standard |
| `### Conoscenza enciclopedica della mitologia classica` | `### Encyclopedic Knowledge of Classical Mythology` | |
| `### Mitologia romana e sincretismo` | `### Roman Mythology & Syncretism` | |
| `### Etimologia e semantica dei nomi` | `### Etymology & Name Semantics` | |
| `## Metodologia: processo di associazione` | `## Methodology: Association Process` | |
| `### Tipologie di associazione (dalla piu' forte alla piu' debole)` | `### Association Types (Strongest to Weakest)` | |
| `### Criteri di qualita' (in ordine di priorita')` | `### Quality Criteria (in Priority Order)` | |
| `### Anti-pattern da evitare` | `### Anti-Patterns to Avoid` | Keep term "anti-pattern" — already EN |
| `## Processo operativo` | `## Operational Process` | |
| `## Formato dell'output` | `## Output Format` | |
| `## Fonti di riferimento` | `## Reference Sources` | |
| `## Limitazioni` | `## Limitations` | Standard |
| `## Output` | `## Output` | Same in both languages — no change |

### 2.3 Identity (righe 15–16)
- **Testo attuale**: Paragrafo di 4 frasi. Identità come "prima delle nove Muse", etimologia del nome, missione nel team.
- Elementi da preservare: riferimento a Calliope come Musa, etimologia `kallos` + `ops`, descrizione del ruolo (scegliere epiteti, dare nomi).
- ⚠️ **Attenzione culturale**: L'etimologia greca va preservata invariata (è la stessa in EN).
- Raccomandazione: dopo l'H1, aggiungere **header comment** di 2-3 righe (standard Atena/Metis/Clio):
  ```
  Mythological naming specialist for Team Olimpo. Proposes names rooted in classical
  mythology for agents, projects, tools, and concepts.
  Does NOT create agent profiles, conduct domain research, or make team structure decisions.
  ```

### 2.4 Communication Style (righe 18–22)
- Tradurre interamente: 4 bullet point con label in grassetto.
- **Tono** → **Tone** — descrizione della voce (colto, preciso, appassionato ma mai pedante)
- **Approccio** → **Approach** — ogni proposta motivata
- **Struttura** → **Structure** — nome raccomandato + 1-2 alternative
- **Onesta' intellettuale** → **Intellectual Honesty** — rischi e compromessi
- Nessun nome membro in questa sezione — traduzione diretta.

### 2.5 Operating Rules (righe 24–29)
- **Riga 25 — DIRETTIVA LINGUA**: `**Rispondi sempre in italiano.**` → **DEVE diventare** `**Always reply in English.**`
- **Riga 26 — Nomi greci**: contiene `(Hermes, Atena, Proteo, Efesto)` come esempi dello schema di naming del team.
  - ⚠️ **Da generalizzare**: questi sono esempi della convenzione di naming, non istruzioni di routing. Opzioni:
    - Opzione A: "Prefer Greek names for consistency with the team's naming scheme (existing members follow this pattern)."
    - Opzione B: Rimuovere la lista e lasciare solo la regola generale.
    - Raccomandazione: **Opzione A** — mantiene il senso senza citare nomi specifici.
- **Riga 27**: `Team/Registro.md` → **Correggere** in `Team/Members/Registro.md` (path reale).
- **Riga 29**: Brand conflict examples (Apollo GraphQL/NASA, Athena AWS) — **preservare** ma tradurre: `(Apollo = Apollo GraphQL/NASA, Athena = AWS Athena, etc.)`

### 2.6 Competencies (righe 31–50)

#### 2.6.1 Competency 1: Classical Mythology (righe 33–40)
- **Subtitle**: Tradurre
- **8 bullet point**: Tradurre descrizioni. Nomi mitologici in italiano (es. "Eracle", "Odisseo", "Giove") → decidere se usare forma italiana o inglese.
  - ⚠️ **Scelta di traduzione**: I nomi mitologici hanno forme diverse in IT e EN (es. Eracle/Heracles, Odisseo/Odysseus, Giove/Jupiter). Calliope lavora con la mitologia greca — la scelta è tra:
    1. **Forma inglese standard** (Heracles, Odysseus, Jupiter) — più coerente con un profilo EN
    2. **Forma italiana** (Eracle, Odisseo, Giove) — preserva la specificità culturale
    3. **Forma greca** (Herakles, Odysseus) — più autentica per una specialista di mitologia
  - **Raccomandazione**: Usare forma **inglese standard** per coerenza con un profilo in lingua inglese. Le forme greche originali possono essere indicate tra parentesi quando rilevante.
  - **Eccezione**: Le figure che nel team sono nomi di membri (Calliope, Clio, Euterpe, Hermes, Proteo, Atena, Efesto) vanno nella loro forma greca standard che è uguale in EN e IT.
- **Riga 37 (Muse)**: Include i nomi Clio ed Euterpe — nomi che esistono anche come membri del team. NON sono riferimenti ad altri agenti, ma semplici elenchi mitologici. **Nessuna azione richiesta**.
- **Riga 38 (Ninfe)**: Naiadi, Nereidi, Driadi, Oreadi, Napee → Naiads, Nereids, Dryads, Oreads, Napeae
- **Riga 40 (Creature)**: Pegaso, Fenice, Sfinge, Chimera, Olimpo, Eliso, Tartaro, Stige → Pegasus, Phoenix, Sphinx, Chimera, Olympus, Elysium, Tartarus, Styx

#### 2.6.2 Competency 2: Roman Mythology (righe 42–45)
- Tradurre descrizioni. Corrispondenze greco-romane (Zeus/Giove → Zeus/Jupiter, Hera/Giunone → Hera/Juno, etc.).
- ⚠️ **Nota culturale**: I nomi romani sono già quasi identici in IT e EN (Giove/Jupiter, Saturno/Saturn, Fortuna/Fortuna). Tradurre le descrizioni, preservare i nomi.

#### 2.6.3 Competency 3: Etymology (righe 47–50)
- Tradurre descrizioni. Esempio Prometeo → Prometheus (forma EN).
- **Riga 50**: `pronunciabilita', memorizzabilita', distinguibilita'` → `pronounceability, memorability, distinguishability`

### 2.7 Methodology: Association Process (righe 52–72)

#### 2.7.1 Association Types (righe 54–58)
- Tradurre titolo e descrizioni dei 4 punti.
- **⚠️ Righe 55–57 contengono nomi membri come esempi:**
  - `Efesto = forgiatore = sviluppatore` (l.55)
  - `Hermes = messaggero = orchestratore` (l.56)
  - `Proteo = trasformazioni = ricercatore` (l.57)
- **Giudizio**: Questi sono esempi **illustrativi della metodologia** di associazione mitologica, non istruzioni operative. Mostrano come i nomi esistenti del team sono stati scelti. Tuttavia, la SOP `agent-design-methodology.md` dice: *"Never mention specific team member names."*
- **Raccomandazione**: Sostituire con esempi generici di figure mitologiche, o con esempi che usano solo il nome mitologico senza il corrispettivo membro:
  - Opzione A (generalizzata): "Direct association: the figure's domain matches the function (e.g., Hephaestus = forger = build/craft role)"
  - Opzione B (solo figura): "Direct association: the figure's domain matches the function (e.g., Hephaestus = forger/smith)"
  - **Raccomandazione**: **Opzione A** — mantiene l'esempio didattico senza riferirsi a membri specifici del team.

#### 2.7.2 Quality Criteria (righe 60–66)
- Tradurre titolo e 6 criteri numerati.
- **⚠️ Riga 63**: `pronunciabile in italiano` — criterio linguisticamente specifico. In EN va adattato: `pronounceable, memorable, distinct` (senza specificare una lingua, o specificando "in English").
- **Raccomandazione**: Cambiare il criterio in `pronounceable in [English/team's working language]` o semplicemente `pronounceable and memorable`.

#### 2.7.3 Anti-Patterns (righe 68–72)
- Tradurre titolo (parzialmente già EN: "Anti-pattern") e 4 descrizioni.
- **Riga 71**: Esempi `(Medea, Crono, ecc.)` → tradurre in `(Medea, Cronus, etc.)`
- **Riga 72**: `Omonimia con brand` → `Brand homonymy`

### 2.8 Operational Process (righe 74–79)
- Tradurre titolo e 5 step numerati.
- **⚠️ Riga 75 — Membro**: `Riceve da Hermes (o da Atena)` → `Receives from the orchestrator (or from the agent designer)`
- **Riga 76 — Path**: `Team/Registro.md` → **Correggere** in `Team/Members/Registro.md`
- Righe 77–79: traduzione diretta, nessun nome membro.

### 2.9 Output Format (righe 81–97)
- Tradurre titolo e intro (`Per ogni proposta:` → `For each proposal:`)
- **Template code block (righe 85–97)**: Tradurre le label ma **preservare la struttura markdown**:
  - `### Nome raccomandato: [Nome]` → `### Recommended Name: [Name]`
  - `**Chi e' nella mitologia**` → `**Who they are in mythology**`
  - `**Perche' questo nome**` → `**Why this name**`
  - `**Etimologia**` → `**Etymology**`
  - `**Rischi**` → `**Risks**`
  - `### Alternativa 1/2: [Nome]` → `### Alternative 1/2: [Name]`
  - `[stessa struttura, piu' sintetica]` → `[same structure, more concise]`

### 2.10 Reference Sources (righe 99–102)
- **Titolo**: Tradurre.
- **Riga 100 — Fonti primarie**: Nomi di opere in italiano (Teogonia, Iliade, Odissea, Metamorfosi, Biblioteca, Eneide).
  - ⚠️ **Scelta**: Tradurre i titoli in inglese (Theogony, Iliad, Odyssey, Metamorphoses, Library/Bibliotheca, Aeneid) o lasciare in italiano? Raccomandazione: **usare titoli inglesi standard**, che sono più riconoscibili in un profilo EN.
- **Riga 101 — Fonti digitali**: Già in inglese. Preservare invariato.
- **Riga 102 — Fonti accademiche**: Riferimenti a edizioni italiane (Grimal, Graves, Kerenyi).
  - ⚠️ **Scelta**: Tradurre i titoli in inglese (Dictionary of Classical Mythology, The Greek Myths, The Gods of the Greeks) o lasciare i riferimenti italiani? Raccomandazione: **usare i titoli inglesi** per coerenza con la lingua del profilo. Gli autori sono gli stessi.

### 2.11 Limitations (righe 104–108)
- Tradurre titolo e 4 punti.
- **⚠️ Riga 105**: `quello e' compito di Atena` → `that is the agent designer's responsibility`
- **⚠️ Riga 106**: `quello e' compito di Proteo` → `that is the domain researcher's responsibility`
- Righe 107–108: traduzione diretta.

### 2.12 Output (righe 110–111)
- **Titolo**: `## Output` — già uguale in EN. Nessuna modifica.
- **⚠️ Riga 110**: `Salva le proposte di naming nella posizione indicata da Hermes o Atena.` → `Save naming proposals to the location specified by the orchestrator or agent designer.`
- **⚠️ Riga 111 — Path**: `Team Inbox/` → **Correggere** in `Team/Inbox/` (con slash, path standard)

---

## 3. Riferimenti a Nomi di Membri — Inventory Completo

Secondo la SOP `agent-design-methodology.md` (riga 46): *"Never mention specific team member names."*

| # | Riga | Nome Membro | Contesto | Azione Raccomandata |
|---|------|-------------|----------|---------------------|
| 1 | 26 | Hermes, Atena, Proteo, Efesto | Regola nomi greci (esempi della convenzione) | Generalizzare: "existing members follow this pattern" o rimuovere lista |
| 2 | 55 | Efesto | Esempio didattico metodologia (associazione diretta) | Sostituire con esempio generico (es. "Hephaestus = forger = build/craft role") |
| 3 | 56 | Hermes | Esempio didattico metodologia (associazione per attributo) | Sostituire con esempio generico (es. "messenger god = coordination/communication role") |
| 4 | 57 | Proteo | Esempio didattico metodologia (associazione per narrativa) | Sostituire con esempio generico (es. "shape-shifting god = adaptable/research role") |
| 5 | 75 | Hermes, Atena | Processo operativo step 1 (mittente) | Sostituire con "orchestrator" e "agent designer" |
| 6 | 105 | Atena | Limitazioni | Sostituire con "agent designer" |
| 7 | 106 | Proteo | Limitazioni | Sostituire con "domain researcher" |
| 8 | 110 | Hermes, Atena | Output (destinazione salvataggio) | Sostituire con "orchestrator" e "agent designer" |

**Totale**: ~8 occorrenze di nomi membri da rimuovere/generalizzare.
**Nota**: I nomi mitologici in elenchi (Clio, Euterpe nella lista delle Muse, riga 37) NON sono riferimenti a membri — sono figure mitologiche citate per competenza. **Non modificare.**

---

## 4. Direttiva Lingua Esplicita

**Trovata alla riga 25**:
```
- **Rispondi sempre in italiano.**
```

Obbligatorio cambiarla in:
```
- **Always reply in English.**
```

Posizionamento: primo bullet delle Operating Rules, come da standard Clio/Metis.

---

## 5. Riferimenti Culturali e Linguistici Specifici

| Elemento | Rischio | Raccomandazione |
|----------|---------|-----------------|
| `kallos` + `ops` (etimologia di Calliope) | Nessun rischio — è greco antico, invariato in EN | Preservare invariato |
| Nomi mitologici in italiano (Eracle, Odisseo, Giove, Crono, ecc.) | Hanno forma diversa in EN (Heracles, Odysseus, Jupiter, Cronus) | **Decisione richiesta**: forma inglese (consigliato) o forma italiana |
| `pronunciabile in italiano` (criterio qualità) | Criterio linguisticamente specifico all'italiano | Adattare: `pronounceable` senza specificare lingua, o specificare `in English` |
| `Teogonia` (Esiodo), `Iliade/Odissea` (Omero), ecc. | Titoli di opere classiche con forme italiane | Tradurre in inglese: Theogony, Iliad/Odyssey, Metamorphoses, etc. |
| `Grimal`, `Graves`, `Kerenyi` (fonti accademiche) | Riferimenti a edizioni italiane | Tradurre titoli in inglese; autori invariati |
| `Dizionario di mitologia classica`, `I miti greci`, `Miti e dei della Grecia` | Titoli italiani di opere con equivalenti EN | Tradurre: Dictionary of Classical Mythology, The Greek Myths, The Gods of the Greeks |
| Brand examples: Apollo GraphQL/NASA, Athena AWS | Riferimenti a brand globali — invariati in EN | Preservare ma tradurre la frase circostante |
| `Nella mitologia` vs `in mythology` | Struttura frase italiana | Tradurre naturalmente in EN, non letteralmente |
| `Trova la parola esatta che cristallizza l'identita'` | Espressione idiomatica italiana | Tradurre senso: "finds the exact word that crystallizes identity" |
| `dalla bella voce` (traduzione di Calliope) | Traduzione italiana del greco | In EN: "beautiful-voiced" o "she of the beautiful voice" |

**Nessun gioco di parole intraducibile, dialetto, o riferimento culturale strettamente italiano** che blocchi la traduzione. Le principali decisioni riguardano la forma dei nomi mitologici (greca/italiana/inglese).

---

## 6. Elementi Strutturali da Preservare ASSOLUTAMENTE

Questi elementi NON devono essere modificati nella struttura, solo eventualmente tradotti nel testo circostante:

1. **Sequenza delle sezioni**: Frontmatter → Title → Identity → Communication Style → Operating Rules → Competencies → Methodology → Operational Process → Output Format → Reference Sources → Limitations → Output
   - Nota: Calliope ha una sezione "Methodology" che non è presente in tutti i profili. **Preservare** nella sua posizione tra Competenze e Processo Operativo.
2. **Permission block** (righe 7–10): `edit: allow, read: allow` — invariato
3. **Numero e ordine delle Regole Operative** (5 regole): da preservare come 5 punti
4. **Numero e ordine delle 3 sottosezioni Competenze**: preservare raggruppamento logico (Classical Mythology, Roman Mythology, Etymology)
5. **Numero e ordine dei 4 elementi della Metodologia**: Association Types (4 punti), Quality Criteria (6 criteri), Anti-patterns (4 punti)
6. **Numero degli step del Processo Operativo**: 5 step numerati
7. **Struttura dell'Output Format**: code block con template a 5 campi + 2 alternative
8. **Numero e ordine delle Limitazioni**: 4 punti
9. **Percorsi filesystem**: tutti i path (`Team/Members/Registro.md` **corretto**, `Team/Inbox/` **corretto**)
10. **Nomi mitologici in elenchi**: non tradurre i nomi propri delle divinità (sono nomi propri)

---

## 7. Path e Comandi da NON Tradurre (preservare invariati / correggere)

| Riga | Elemento | Tipo | Azione |
|------|----------|------|--------|
| 27 | `` `Team/Registro.md` `` | Path | ⚠️ **Correggere** in `Team/Members/Registro.md` |
| 76 | `` `Team/Registro.md` `` | Path | ⚠️ **Correggere** in `Team/Members/Registro.md` |
| 111 | `` `Team Inbox/` `` | Path | ⚠️ **Correggere** in `Team/Inbox/` |
| 101 | `Theoi.com`, `Britannica Greek Mythology`, `Behind the Name (Mythology)`, `British Museum Pantheon` | Nomi propri | Preservare invariati |
| 85–97 | Struttura template output | Blocco codice | Preservare struttura markdown, tradurre solo le label |
| 7–10 | `permission:` block | Frontmatter | Invariato |

---

## 8. Raccomandazioni per la Traduzione

### 8.1 Strategia Generale
1. **Approccio**: traduzione + correzione + refactoring in unico passaggio
2. **Ordinamento**: procedere top-down, sezione per sezione
3. **Modello di riferimento**: usare `.opencode/agents/clio.md` (versione EN già approvata) come template di stile
4. **Non separare traduzione e correzione**: il file ha bisogno sia di traduzione che di fix strutturali (path errati, descrizione sbagliata)

### 8.2 Descrizione Frontmatter (priorità altissima)
Riscrivere da zero. Proposta:

```yaml
description: Mythological naming specialist for Team Olimpo's agent roster. Use for naming new agents, projects, tools, and concepts with symbolic, etymological, and narrative fit analysis rooted in classical mythology.
```
(194 caratteri — nel limite)

### 8.3 Aggiungere Header Comment (standard Atena)
Dopo il titolo H1, aggiungere 2-3 righe human-readable:

```
Mythological naming specialist for Team Olimpo. Proposes names with mythological,
symbolic, and etymological justification.
Does NOT create agent profiles, conduct domain research, or make team composition decisions.
```

### 8.4 Gestione dei Nomi Mitologici (decisione chiave)
La scelta più impattante è: **forma inglese o forma italiana dei nomi mitologici?**

| Figura | Italiano | Inglese | Greco |
|--------|----------|---------|-------|
| Eracle | Eracle | Heracles | Herakles |
| Odisseo | Odisseo | Odysseus | Odysseus |
| Giove | Giove | Jupiter | Zeus |
| Crono | Crono | Cronus | Kronos |
| Enea | Enea | Aeneas | Aineias |

**Raccomandazione**: **Usare forma inglese standard** per coerenza. Il profilo sarà in inglese, e i nomi mitologici in forma inglese sono lo standard internazionale. Eccezioni: figure il cui nome greco è universalmente usato (Zeus, Hera, Apollo — che sono identici).

### 8.5 Riscrittura Esempi nella Metodologia (righe 55–57)
Sostituire i riferimenti a Hermes/Efesto/Proteo con esempi generici:

```
1. **Direct association**: the figure's domain matches the function (e.g., Hephaestus = forger/smith = build/craft role).
2. **Attribute association**: a characteristic of the figure connects to the function (e.g., messenger god = coordination/communication role).
3. **Narrative association**: a mythical episode reflects the work type (e.g., shape-shifting god = adaptable/research role).
4. **Etymological association**: the name's meaning illuminates the function.
```

### 8.6 Traduzione Criterio "Pronunciabile in italiano" (riga 63)
Opzioni:
- `pronounceable and memorable` (senza specificare lingua)
- `pronounceable in the team's working language` (più preciso)
- **Raccomandazione**: prima opzione — più pulita e non vincolante.

### 8.7 Riscrittura Limitazioni (righe 105–106)
Generalizzare i riferimenti ad Atena e Proteo:

```
- **Does not create member profiles**: that is the agent designer's responsibility.
- **Does not conduct domain research**: that is the domain researcher's responsibility.
```

### 8.8 Formattazione Apostrofi
Il profilo IT usa l'apostrofo dattilografico (`'`) in parole come `Identita'`, `Personalita'`, `Onesta'`, ecc. In EN si userà l'apostrofo tipografico standard (`'`) in contrazioni come `don't`, `doesn't`, `it's`.

---

## 9. Stima Complessità

| Fattore | Valutazione |
|---------|-------------|
| **Volume totale** | 111 righe |
| **Elementi da tradurre** | ~40-45 (descrizioni, bullet, titoli) |
| **Elementi da preservare invariati** | ~8 (mode, model, permission, fonti digitali, path invariati) |
| **Nomi membri da rimuovere** | ~8 occorrenze |
| **Path da correggere** | 3 (`Team/Registro.md`×2 → `Team/Members/Registro.md`; `Team Inbox/` → `Team/Inbox/`) |
| **Riscritture strutturali necessarie** | 2 (Frontmatter description da zero + aggiunta header comment) |
| **Inconsistenze da risolvere** | 1 (frontmatter description non corrisponde al corpo) |
| **Sezioni da modificare** | 12 su 12 sezioni |
| **Giochi di parole italiani** | 0 |
| **Riferimenti culturali problematici** | 1 (criterio "pronunciabile in italiano" da adattare) |
| **Decisioni di traduzione aperte** | 3 (nomi mitologici: forma inglese/italiana; criterio lingua-specifico; titoli opere classiche) |

### Verdetto: COMPLESSITÀ MEDIA

**Motivazione**:
- **Non è semplice** (~20 minuti di lavoro minimo): richiede riscrittura creativa della frontmatter, correzione di path errati, e decisioni su nomi mitologici.
- **Non è complessa** (nessun tecnicismo intraducibile, nessun gioco di parole, struttura chiara e compatta).
- **Più semplice di Clio** (111 righe vs 170, meno workflow, meno elementi tecnici).
- **Più complessa per le decisioni culturali** (nomi mitologici, titoli di opere classiche).

**Tempo stimato per la traduzione**: 15-20 minuti per un traduttore esperto del dominio.

**Sezioni a maggiore sforzo**:
1. Frontmatter description (da riscrivere creativamente)
2. Competency 1: Classical Mythology (8 bullet con molti nomi propri da normalizzare)
3. Methodology: Association Types (3 esempi con nomi membri da riscrivere)
4. Reference Sources (titoli opere da decidere se italianizzare o anglicizzare)

**Sezioni a minore sforzo**:
1. Output Format (solo label del template da tradurre)
2. Limitations (4 frasi brevi)
3. Permission / mode / model (già in EN)
4. Output (2 frasi brevi)

---

## 10. Checklist Pre-Traduzione (da consegnare a chi traduce)

- [ ] **Frontmatter `description:`** → Riscrivere da zero in EN (~150-200 char, ruolo corretto di nomenclatura mitologica)
- [ ] **Aggiungere header comment** di 2-3 righe dopo il titolo H1
- [ ] **Tradurre titolo H1** → `# Calliope — Mythological Naming Specialist, Team Olimpo`
- [ ] **Identity** → Tradurre, preservare etimologia greca
- [ ] **Communication Style** → Tradurre 4 bullet (Tono/Approccio/Struttura/Onestà intellettuale)
- [ ] **Operating Rules** → Tradurre 5 regole, cambiare direttiva lingua, generalizzare nomi membri nella regola 2
- [ ] **Competency 1: Classical Mythology** → Tradurre 8 bullet + decidere forma nomi mitologici (EN consigliato)
- [ ] **Competency 2: Roman Mythology** → Tradurre 3 bullet
- [ ] **Competency 3: Etymology** → Tradurre 3 bullet
- [ ] **Methodology: Association Types** → Tradurre 4 punti, riscrivere 3 esempi (rimuovere Hermes/Efesto/Proteo)
- [ ] **Methodology: Quality Criteria** → Tradurre 6 criteri, adattare "pronunciabile in italiano"
- [ ] **Methodology: Anti-Patterns** → Tradurre 4 punti
- [ ] **Operational Process** → Tradurre 5 step, generalizzare "Hermes/Atena" nello step 1
- [ ] **Output Format** → Tradurre label del template (mantenere struttura code block)
- [ ] **Reference Sources** → Tradurre titoli opere + autori (decidere forma inglese/italiana)
- [ ] **Limitations** → Tradurre 4 punti, generalizzare "Atena" e "Proteo"
- [ ] **Output** → Tradurre 2 frasi, generalizzare "Hermes/Atena"
- [ ] **Correggere path**: `Team/Registro.md` → `Team/Members/Registro.md` (×2)
- [ ] **Correggere path**: `Team Inbox/` → `Team/Inbox/` (×1)
- [ ] **Verificare**: nessun path tradotto, nessun comando modificato
- [ ] **Verificare**: nessun nome membro nel file finale
- [ ] **Verificare**: direttiva `Always reply in English.` presente come primo bullet delle Operating Rules
