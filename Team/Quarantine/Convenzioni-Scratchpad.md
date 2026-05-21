---
title: "Convenzioni Scratchpad e Struttura Team"
tags:
  - convenzioni
  - scratchpad
  - team
  - workspace
  - hermes
aliases:
  - Convenzioni Scratchpad Hermes
  - Struttura Team Agent
created: 2026-05-04
---

# Convenzioni Scratchpad e Struttura `Team/<Agente>/`

Questo documento definisce le regole operative per l'uso dello scratchpad di Hermes e le convenzioni per la struttura `Team/<NomeAgente>/` — applicabili a **tutti i membri del Team Olimpo**, presenti e futuri.

---

## Parte 1 — Struttura `Team/<NomeAgente>/`

Ogni membro del team ha una cartella dedicata in `Team/` che funge da spazio di lavoro personale. Questa struttura e' **standardizzata** e va replicata per ogni nuovo agente.

### Layout della cartella

```
Team/<NomeAgente>/
├── Scratchpad.md          # Spazio di lavoro operativo (OBBLIGATORIO)
├── Tasks/                 # Task attivi e completati (OPZIONALE)
│   ├── active/            # Task in corso
│   └── completed/         # Task archiviati
├── Decisions/             # Decisioni prese e motivazioni (OPZIONALE)
├── Notes/                 # Appunti, ricerche, riferimenti (OPZIONALE)
└── Convenzioni/           # Regole specifiche dell'agente (OPZIONALE)
```

### Cosa contiene ogni file/cartella

| Elemento | Obbligatorio? | Scopo |
|----------|--------------|-------|
| `Scratchpad.md` | **SI** | Dashboard operativa: stato corrente, task attivi, decisioni, blocchi. Unico file che **deve** esistere. |
| `Tasks/active/` | No | File Markdown per task complessi che richiedono tracking dettagliato oltre lo scratchpad. |
| `Tasks/completed/` | No | Archiviazione dei task completati. Spostare qui i file da `active/` al completamento. |
| `Decisions/` | No | Tracciamento di decisioni strutturate (perche' e' stata presa una decisione, alternative scartate, conseguenze). |
| `Notes/` | No | Appunti temporanei, snippet di codice, riferimenti rapidi. Pulire periodicamente. |
| `Convenzioni/` | No | Regole specifiche dell'agente (es. convenzioni di naming per output, formati speciali). |

### Regole generali

1. **Solo `Scratchpad.md` e' obbligatorio.** Le altre cartelle si creano solo se servono.
2. **Niente file binari.** Solo Markdown e YAML.
3. **Naming coerente.** I file nelle sottocartelle usano: `<data>_<breve-descrizione>.md` (es. `2026-05-04_analisi-kba-batch.md`).
4. **Archiviazione periodica.** I task completati vanno spostati in `Tasks/completed/` o in `Library/Handoff/Archivio/` se sono handoff verso altri membri.
5. **No duplicazione con Handoff.** Se un file deve essere letto da un altro membro, va in `Library/Handoff/`, non in `Team/<Agente>/Notes/`.

---

## Parte 2 — Scratchpad: quando e come aggiornare

### Frequenza di aggiornamento

| Trigger | Azione |
|---------|--------|
| **Inizio sessione** | Leggere lo scratchpad per ripristinare il contesto. Aggiornare `last_updated`. |
| **Nuovo task delegato** | Aggiungere entry in `active_tasks` e sezione "Task in corso". |
| **Task completato** | Rimuovere da `active_tasks`, aggiungere al log con esito. |
| **Decisione presa** | Aggiungere a `decisions` nel frontmatter e sezione "Decisioni recenti". |
| **Blocco identificato** | Aggiungere a sezione "Blocchi aperti". |
| **Fine sessione** | Verificare che `active_tasks` rifletta lo stato reale. Aggiornare `last_updated`. |

### Cosa NON registrare nello scratchpad

- Output completi di task (vanno in `Library/Handoff/` o `Library/deliverables/`).
- Dati sensibili o credenziali.
- Transcript di conversazioni con l'utente.
- Output intermedi di tool/script (vanno nella loro cartella di destinazione).

### Cosa REGISTRARE nello scratchpad

- **Riferimenti** a file prodotti (path, non contenuto).
- **Stato** dei task (in corso, bloccato, completato).
- **Decisioni** prese e motivazione sintetica.
- **Blocchi** e cosa serve per risolverli.
- **Context switching**: quando si passa da un task a un altro, annotare dove si era rimasti.

---

## Parte 3 — Regole per i campi frontmatter

Il frontmatter dello scratchpad ha campi strutturati che Hermes (e ogni agente) deve mantenere aggiornati.

### `last_updated`

```yaml
last_updated: 2026-05-04
```

- Formato: `YYYY-MM-DD` (solo data, niente ora).
- Aggiornare ad **ogni modifica** dello scratchpad.

### `active_tasks`

Lista di task attualmente in corso. Ogni entry e' un oggetto YAML:

```yaml
active_tasks:
  - id: "T-001"
    title: "Analisi batch KBA NK-2500"
    delegated_to: "Dike"
    status: "in_progress"        # in_progress | blocked | awaiting_review
    started_at: 2026-05-04
    due_at: null                  # null se non c'e' scadenza
    handoff_ref: "Library/Handoff/kba_batch/"  # path ai file di riferimento
    notes: ""
```

#### Campi di ogni task

| Campo | Tipo | Obbligatorio? | Descrizione |
|-------|------|--------------|-------------|
| `id` | stringa | SI | Identificativo univoco. Formato: `T-NNN` (progressivo). |
| `title` | stringa | SI | Titolo descrittivo del task. |
| `delegated_to` | stringa | SI | Nome dell'agente a cui e' stato delegato. `"Hermes"` se non delegato. |
| `status` | stringa | SI | Uno di: `in_progress`, `blocked`, `awaiting_review`, `completed`. |
| `started_at` | data | SI | Data di inizio. |
| `due_at` | data/null | No | Scadenza, se applicabile. `null` altrimenti. |
| `handoff_ref` | stringa | No | Path relativo ai file di handoff correlati. |
| `notes` | stringa | No | Note brevi (max 1 riga). |

### `members_status`

Mappa dello stato di ogni membro del team. Usare quando serve tracciare la disponibilita' o lo stato operativo:

```yaml
members_status:
  Dike:
    status: "active"             # active | idle | blocked | unavailable
    current_task: "T-001"
    last_contact: 2026-05-04
    blocks: []                   # Lista di blocchi segnalati dal membro
  Clio:
    status: "idle"
    current_task: null
    last_contact: 2026-05-03
    blocks: []
```

**Quando aggiornare `members_status`:**
- All'inizio di una sessione, dopo aver letto lo stato precedente.
- Quando si delega un task (aggiornare `status` e `current_task` del membro).
- Quando un membro segnala un blocco.
- Non e' necessario aggiornare ad ogni singola operazione — basta uno snapshot ragionevole dello stato del team.

### `decisions`

Lista delle decisioni prese durante la sessione o recentemente. Ogni entry:

```yaml
decisions:
  - id: "D-001"
    date: 2026-05-04
    topic: "Struttura cartelle Team"
    decision: "Ogni agente avra' una cartella Team/<Nome>/ con Scratchpad.md obbligatorio"
    rationale: "Standardizzare il workspace per facilitare il contesto tra sessioni"
    alternatives_considered:
      - "Unico scratchpad condiviso in Team/"
      - "Nessuna struttura fissa, ogni agente gestisce a modo suo"
    impact: "Richiede creazione cartelle per agenti esistenti"
```

**Quando registrare una decisione:**
- Quando si sceglie tra due o piu' approcci alternativi.
- Quando si modifica una convenzione esistente.
- Quando si crea una nuova struttura o processo.
- **NON** registrare decisioni banali o operative di routine.

### Regole di sintassi YAML

- Usare sempre la **forma estesa** per liste di oggetti (come negli esempi sopra).
- `null` per valori assenti, **non** stringhe vuote o omissioni.
- Stringhe con caratteri speciali: usare le virgolette doppie `"..."`.
- Date: formato `YYYY-MM-DD`, **senza virgolette**.
- Mantenere l'indentazione coerente (2 spazi).

---

## Parte 4 — Struttura del body dello Scratchpad

Dopo il frontmatter, il body Markdown segue questa struttura fissa:

```markdown
> [!note] Scopo dello Scratchpad
> [1-2 frasi che spiegano a cosa serve questo file per QUESTO agente]

## Stato corrente

[1-2 paragrafi: panoramica dello stato operativo. Cosa sta succedendo ora?]

## Task in corso

[Lista dei task attivi con stato sintetico. Usare tabelle o liste puntate.]

| ID | Titolo | Delegato a | Stato | Note |
|----|--------|------------|-------|------|
| T-001 | Analisi KBA | Dike | in_progress | 12 KBA rimanenti |

## Decisioni recenti

[Lista delle decisioni prese, con link al dettaglio se esiste file separato.]

- **D-001** (2026-05-04): [Sintesi decisione] — [Link a Decisions/ se esiste]

## Blocchi aperti

[Elenco di cosa e' bloccato e perche'. Se vuoto: "_Nessun blocco._"]

## Prossimi step

[Cosa deve succedere dopo. Priorita' decrescente.]

1. [Step 1]
2. [Step 2]

## Log aggiornamenti

| Data | Cosa e' cambiato |
|------|-----------------|
| 2026-05-04 | Creazione convenzioni scratchpad |
```

### Regole per il body

1. **Mantenere le sezioni nell'ordine definito.** Non riordinare, non aggiungere sezioni custom senza motivo.
2. **Sintesi, non trascrizione.** Ogni sezione va al punto. Se serve dettaglio, creare un file in `Tasks/` o `Decisions/` e linkarlo.
3. **Tabelle per i task attivi.** La tabella "Task in corso" deve riflettere esattamente `active_tasks` nel frontmatter.
4. **Log degli aggiornamenti.** Ogni modifica significativa va registrata con data e descrizione.
5. **Pulizia periodica.** Quando un task e' completato da > 7 giorni, rimuovere dalla tabella e archiviare il riferimento.

---

## Parte 5 — Esempi pratici di aggiornamento

### Esempio 1: Hermes delega un task a Dike

**Scenario**: L'utente chiede di analizzare 15 KBA. Hermes delega a Dike.

**Frontmatter aggiornato:**

```yaml
active_tasks:
  - id: "T-001"
    title: "Analisi batch 15 KBA Emerson"
    delegated_to: "Dike"
    status: "in_progress"
    started_at: 2026-05-04
    due_at: null
    handoff_ref: "Library/Handoff/kba_batch/"
    notes: ""

members_status:
  Dike:
    status: "active"
    current_task: "T-001"
    last_contact: 2026-05-04
    blocks: []
```

**Body aggiornato (sezione Task in corso):**

```markdown
## Task in corso

| ID | Titolo | Delegato a | Stato | Note |
|----|--------|------------|-------|------|
| T-001 | Analisi batch 15 KBA | Dike | in_progress | Input: Library/Handoff/kba_batch/ |
```

**Log aggiornamenti:**

```markdown
| 2026-05-04 | Delegato T-001 a Dike: analisi 15 KBA da kba_batch |
```

### Esempio 2: Task completato, risultato archiviato

**Scenario**: Dike ha completato l'analisi. I record sono in `Library/data/kba_catalog/records/`.

**Frontmatter aggiornato:**

```yaml
active_tasks: []

members_status:
  Dike:
    status: "idle"
    current_task: null
    last_contact: 2026-05-04
    blocks: []
```

**Body aggiornato:**

```markdown
## Stato corrente

Analisi KBA completata. 15 record prodotti in catalogo. In attesa di nuove richieste.

## Task in corso

_Nessun task attivo._

## Prossimi step

1. Attendere feedback utente sul report KBA
2. Valutare se aggiornare index.yaml del catalogo
```

### Esempio 3: Decisione presa

**Scenario**: Si decide di standardizzare la struttura `Team/<Agente>/`.

**Frontmatter:**

```yaml
decisions:
  - id: "D-001"
    date: 2026-05-04
    topic: "Struttura cartelle Team"
    decision: "Ogni agente avra' cartella Team/<Nome>/ con Scratchpad.md obbligatorio"
    rationale: "Standardizzare workspace per contesto tra sessioni"
    alternatives_considered:
      - "Unico scratchpad condiviso"
      - "Nessuna struttura fissa"
    impact: "Creare cartelle per agenti esistenti"
```

### Esempio 4: Task bloccato

**Scenario**: Dike non puo' procedere perche' mancano i file sorgente.

**Frontmatter:**

```yaml
active_tasks:
  - id: "T-001"
    title: "Analisi batch 15 KBA Emerson"
    delegated_to: "Dike"
    status: "blocked"
    started_at: 2026-05-04
    due_at: null
    handoff_ref: "Library/Handoff/kba_batch/"
    notes: "Mancano 3 file sorgente in Library/documents/"

members_status:
  Dike:
    status: "blocked"
    current_task: "T-001"
    last_contact: 2026-05-04
    blocks:
      - "File sorgenti mancanti: nk-2500-0100.md, nk-2500-0101.md, nk-2500-0102.md"
```

**Body:**

```markdown
## Blocchi aperti

- **T-001**: Dike bloccato — mancano 3 file sorgente in Library/documents/. Serve azione di Clio per conversione PDF.
```

---

## Parte 6 — Integrazione con il flusso di lavoro esistente

### Relazione con `Library/Handoff/`

Lo scratchpad e l'handoff hanno ruoli complementari:

| | Scratchpad | Handoff |
|--|-----------|---------|
| **Scopo** | Tracking stato operativo | Trasferimento lavoro tra membri |
| **Contenuto** | Riferimenti, stato, decisioni | Output concreti, deliverable |
| **Durata** | Sessione corrente + breve storico | Fino ad archiviazione |
| **Lettori** | Solo l'agente proprietario + Hermes | Agente mittente + destinatario |

**Regola**: se un file deve essere letto da un altro membro, va in `Library/Handoff/`. Lo scratchpad contiene solo il **riferimento** (path), non il contenuto.

### Flusso tipico con scratchpad

```
1. Utente → Hermes: nuova richiesta
2. Hermes → Scratchpad: aggiorna active_tasks, members_status
3. Hermes → Handoff: crea file di briefing per l'agente delegato
4. Agente → Lavora → Produce output in Handoff o destinazione finale
5. Agente → Hermes: notifica completamento (via handoff o diretto)
6. Hermes → Scratchpad: aggiorna stato task, archivia riferimento
7. Hermes → Utente: restituisce risultato
```

### Relazione con `Library/Handoff/brief-*`

I briefing sono input per gli agenti. Lo scratchpad li **referenzia** ma non li contiene:

```yaml
active_tasks:
  - id: "T-002"
    title: "Verifica conformita' CLI tool"
    delegated_to: "Clio"
    status: "in_progress"
    started_at: 2026-05-04
    handoff_ref: "Library/Handoff/brief-wip-020426.md"
    notes: ""
```

### Relazione con `Team/Fucina/`

La Fucina e' lo spazio di **lavoro grezzo** — bozze, sperimentazioni, materiali non ancora validati. Lo scratchpad puo' riferirsi a file in Fucina quando un task e' in fase esplorativa:

```yaml
active_tasks:
  - id: "T-003"
    title: "Definire profilo nuovo agente"
    delegated_to: "Atena"
    status: "in_progress"
    handoff_ref: "Team/Fucina/proteo.md"
    notes: "Bozza in Fucina, da validare prima di spostare in .opencode/agents/"
```

### Relazione con `Library/deliverables/`

Output destinati all'utente finale vanno in `Library/deliverables/`. Lo scratchpad registra che il deliverable e' stato prodotto:

```yaml
active_tasks:
  - id: "T-001"
    title: "Report KBA"
    delegated_to: "Dike"
    status: "completed"
    notes: "Output: Library/deliverables/report-kba-maggio-2026.md"
```

---

## Parte 7 — Estensione ad altri agenti

Le convenzioni definite qui sono **progettate per Hermes ma applicabili a tutti i membri del team**. Ogni agente puo' (e dovrebbe) avere un proprio scratchpad con la stessa struttura.

### Adattamenti per ruolo

Ogni agente adatta lo scratchpad al proprio flusso operativo:

| Agente | Uso specifico dello scratchpad |
|--------|-------------------------------|
| **Hermes** | Tracking task delegati, stato del team, decisioni di orchestrazione |
| **Proteo** | Ricerche in corso, fonti consultate, domini analizzati |
| **Atena** | Profili in costruzione, membri da creare, validazioni pendenti |
| **Efesto** | Tool in sviluppo, bug aperti, test da eseguire |
| **Clio** | Documenti da verificare, conformita' da controllare, guide da aggiornare |
| **Dike** | KBA da analizzare, scoring in corso, record da catalogare |
| **Metis** | Analisi strategiche in corso, ottimizzazioni identificate |
| **Calliope** | Contenuti creativi in produzione, naming conventions |

### Come creare lo scratchpad per un nuovo agente

1. **Creare la cartella**: `mkdir Team/<NomeAgente>/`
2. **Copiare il template** (vedere sotto) in `Team/<NomeAgente>/Scratchpad.md`
3. **Personalizzare** il frontmatter con il nome dell'agente e i campi iniziali vuoti
4. **Aggiornare il box "[!note]"** con lo scopo specifico dell'agente
5. **Registrare la convenzione** nel Registro Membri

### Template universale Scratchpad

```markdown
---
title: "<NomeAgente> — Scratchpad"
tags:
  - scratchpad
  - <nome-agente-lowercase>
  - workspace
aliases:
  - "<NomeAgente> Workspace"
  - "<NomeAgente> Dashboard"
cssclasses:
  - scratchpad
last_updated: YYYY-MM-DD
active_tasks: []
members_status: {}
decisions: []
---

> [!note] Scopo dello Scratchpad
> Questo file e' lo spazio di lavoro operativo di **<NomeAgente>**, <ruolo> del Team Olimpo.
> [1-2 frasi specifiche sul ruolo di questo scratchpad]

## Stato corrente

_Nessuna attivita' in corso._

## Task in corso

_Nessun task attivo._

## Decisioni recenti

_Nessuna decisione registrata._

## Blocchi aperti

_Nessun blocco segnalato._

## Prossimi step

_Nessun step programmato._

## Log aggiornamenti

| Data | Aggiornamento |
|------|---------------|
| YYYY-MM-DD | Creazione iniziale dello scratchpad |
```

### Quando un agente DEVE avere uno scratchpad

- **Obbligatorio** per: Hermes (orchestratore), qualsiasi agente che gestisce task multipli o sessioni lunghe.
- **Raccomandato** per: tutti gli agenti che lavorano su task che span piu' di una conversazione.
- **Opzionale** per: agenti con task semplici e autoconclusivi in una singola sessione.

### Sharing dello scratchpad

- Lo scratchpad e' **read-only** per gli altri agenti. Solo il proprietario lo modifica.
- Hermes puo' leggere gli scratchpad degli altri membri per fare un check dello stato del team.
- Se un agente vuole comunicare qualcosa tramite lo scratchpad, lo scrive nella sezione "Blocchi aperti" o "Note" — Hermes lo leggera' al prossimo ciclo.

---

## Parte 8 — Riepilogo rapido

### Regole d'oro

1. **Scratchpad.md e' obbligatorio** per ogni agente. Il resto e' opzionale.
2. **Frontmatter sempre aggiornato** — `active_tasks`, `members_status`, `last_updated`.
3. **Riferimenti, non contenuti** — lo scratchpad punta ai file, non li contiene.
4. **Handoff per condivisione** — se un altro membro deve leggere qualcosa, mettilo in Handoff.
5. **Sintesi sempre** — lo scratchpad e' una dashboard, non un documento narrativo.
6. **Pulizia periodica** — task completati da > 7 giorni: archiviare e rimuovere.
7. **ID progressivi** — `T-NNN` per task, `D-NNN` per decisioni.
8. **Date ISO 8601** — `YYYY-MM-DD`, senza virgolette.
9. **Coerenza** — frontmatter e body devono essere allineati (stessi task, stessi stati).
10. **Italiano sempre** — come ogni comunicazione del Team Olimpo.

### Checklist per nuovo agente

- [ ] Creata cartella `Team/<NomeAgente>/`
- [ ] Creato `Scratchpad.md` con template personalizzato
- [ ] Frontmatter compilato con tags corretti
- [ ] Box "[!note]" personalizzato per il ruolo
- [ ] Registrato nel Registro Membri
- [ ] Convenzioni specifiche dell'agente documentate (se necessarie) in `Convenzioni/`

---

## Cronologia del documento

| Data | Autore | Modifica |
|------|--------|----------|
| 2026-05-04 | Dike | Creazione iniziale — convenzioni scratchpad e struttura Team |
