---
title: "Piano di Implementazione Fase 2: Recovery e Plan Approval"
tags:
  - fase2
  - recovery
  - plan-approval
  - hermes
  - metis
  - governance
aliases:
  - Piano Fase 2 Recovery
  - Fase 2 Recovery Plan Approval
cssclasses:
  - clio-archivio
  - documento-formale
  - fase2
---

# Piano di Implementazione Fase 2: Recovery e Plan Approval

**Data**: 2026-05-04  
**Stato**: Bozza per implementazione  
**Responsabile**: Hermes (implementazione), Clio (verifica conformità)  
**Riferimenti**: Analisi Metis sez. 4.1 e 5.1, Report dike-hermes 2026-05-01

---

## Sommario Esecutivo

Il presente piano definisce l'implementazione di due componenti critiche per la Fase 2 del Team Olimpo, basate sugli input strategici di Metis:

1. **Recovery Semplice**: Meccanismo di rilevamento task interrotti tramite tag `[RECOVERY NEEDED: TaskID]` nello scratchpad di Hermes, con segnalazione all'utente e senza ripristino automatico.
2. **Plan Approval**: Criterio di approvazione esplicita per task complessi (≥3 passaggi o multi-worker), con presentazione sintetica del piano all'utente prima della delega.

L'approccio è **minimalista**: sfrutta l'infrastruttura esistente (scratchpad Hermes, file system Handoff) senza introdurre task list condivise pesanti o modifiche architetturali.

---

## Componente 1: Recovery Semplice

### Meccanismo di funzionamento

Il recovery si basa su un controllo allo startup di Hermes che analizza lo stato dei task nello scratchpad.

#### Flusso Hermes

1. **Check allo startup**: Hermes legge il proprio scratchpad alla prima interazione utente
2. **Rilevamento task interrotti**: Identifica task con stato `in_progress` che non hanno prodotto output corrispondente in `Library/Handoff/`
3. **Tagging automatico**: Per ogni task interrotto, Hermes aggiunge il tag:
   ```
   [RECOVERY NEEDED: <TaskID>]
   ```
4. **Segnalazione**: Hermes presenta all'utente l'elenco dei task interrotti, chiedendo istruzioni (riprendere, annullare, ignorare)
5. **Nessun ripristino automatico**: Hermes NON riprende automaticamente i task — attende decisione esplicita dell'utente

#### Integrazione nello scratchpad Hermes

Lo scratchpad di Hermes deve includere, per ogni task:
```yaml
tasks:
  - id: "task-20260504-001"
    description: "Analisi competenze Python"
    status: "in_progress"  # completed | in_progress | pending
    worker: "proteo"
    created: "2026-05-04T09:00:00"
    output_expected: "Library/Handoff/2026-05-04_proteo_report_competenze.md"
```

#### Esempio pratico

**Scenario**: Hermes ha delegato a Proteo un'analisi il giorno precedente, ma la sessione è terminata prima del completamento.

**Scratchpad allo startup**:
```yaml
tasks:
  - id: "task-20260503-012"
    description: "Analisi mercato AI 2026"
    status: "in_progress"
    worker: "proteo"
    created: "2026-05-03T18:30:00"
    output_expected: "Library/Handoff/2026-05-03_proteo_analisi-ai-2026.md"
```

**Azione Hermes**: Verifica esistenza file in `output_expected`. File non trovato → Aggiunge tag:
```
[RECOVERY NEEDED: task-20260503-012]
```

**Messaggio all'utente**:
> "Rilevato task interrotto: Analisi mercato AI 2026 (ID: task-20260503-012).  
> Vuoi che riprenda il task con Proteo, lo annulli, o lo ignori?"

---

## Componente 2: Criteri e Workflow Plan Approval

### Definizione di "Task Complesso"

Un task richiede **Plan Approval** se soddisfa almeno uno dei criteri:

1. **Multi-passaggio**: Il task richiede più di 2 passaggi operativi
2. **Multi-worker**: Il task coinvolge più di un worker (es. Proteo + Efesto, Atena + Clio)

### Quando attivare il Plan Approval

| Criterio | Esempio | Richiede Approval |
|----------|---------|-------------------|
| Task a passaggio singolo | "Crea profilo Python" (Proteo) | NO |
| Task a 2 passaggi | "Profilo Python → Atena crea agente" | NO |
| Task ≥3 passaggi | "Analisi → Profilo → Agente → Test" | **SÌ** |
| Multi-worker (2) | "Proteo + Efesto" | **SÌ** |
| Multi-worker (1) | "Solo Proteo" | NO |

### Workflow di approvazione

1. **Rilevamento**: Hermes identifica task complesso prima di delegare
2. **Generazione piano**: Hermes crea un piano sintetico (massimo 5 righe per passaggio)
3. **Presentazione all'utente**: 
   ```
   Piano di esecuzione per: [Descrizione Task]
   
   Passaggi:
   1. [Worker] - [Azione breve]
   2. [Worker] - [Azione breve]
   3. [Worker] - [Azione breve]
   
   Procedo? (sì/no/modifica)
   ```
4. **Attesa approvazione esplicita**: Hermes NON procede senza risposta positiva dell'utente
5. **Esecuzione**: Dopo approvazione, Hermes delega secondo il piano concordato

### Esempio pratico

**Task**: "Crea un nuovo agente per l'analisi dati che usa Python e API esterne"

**Piano generato da Hermes**:
```
Piano di esecuzione per: Nuovo agente analisi dati

Passaggi:
1. [Proteo] - Analisi dominio analisi dati e competenze Python/API
2. [Proteo] - Produzione profilo competenze strutturato
3. [Atena] - Costruzione identità agente e istruzioni operative
4. [Efesto] - Implementazione script di supporto per API

Procedo? (sì/no/modifica)
```

**Dopo approvazione**: Hermes delega sequenzialmente a Proteo → Atena → Efesto.

---

## Roadmap di Esecuzione

### Step 1: Aggiornamento prompt Hermes
- **Responsabile**: Hermes (auto-aggiornamento)
- **Effort**: Basso (modifica prompt system)
- **Azioni**:
  - Aggiungere sezione "Recovery Check" allo startup prompt
  - Aggiungere sezione "Plan Approval" con criteri di attivazione
  - Definire formato tag `[RECOVERY NEEDED: TaskID]`
  - Definire template piano sintetico

### Step 2: Test Recovery Semplice
- **Responsabile**: Hermes + Utente
- **Effort**: Medio
- **Azioni**:
  - Simulare interruzione task con stato `in_progress`
  - Verificare rilevamento allo startup successivo
  - Testare interazione utente per decisione recovery

### Step 3: Test Plan Approval
- **Responsabile**: Hermes + Utente
- **Effort**: Medio
- **Azioni**:
  - Testare identificazione task complessi (≥3 passaggi, multi-worker)
  - Verificare generazione piano sintetico
  - Testare flusso approvazione/rifiuto

### Step 4: Verifica conformità vault
- **Responsabile**: Clio
- **Effort**: Basso
- **Azioni**:
  - Verificare che i file in Handoff seguano naming convention
  - Verificare frontmatter dei documenti prodotti
  - Verificare coerenza con struttura esistente

---

## Criteri di Accettazione e Test

### Criterio 1: Recovery funzionante
- [ ] Hermes rileva task `in_progress` senza output in Handoff
- [ ] Tag `[RECOVERY NEEDED: TaskID]` generato correttamente
- [ ] Messaggio all'utente chiaro e con opzioni esplicite
- [ ] Nessun ripristino automatico senza consenso

### Criterio 2: Plan Approval attivato correttamente
- [ ] Task ≥3 passaggi attivano approval
- [ ] Task multi-worker (≥2) attivano approval
- [ ] Task semplici (<3 passaggi, 1 worker) procedono senza approval
- [ ] Piano sintetico presentato in formato leggibile

### Criterio 3: Minimalismo mantenuto
- [ ] Nessuna task list condivisa aggiuntiva creata
- [ ] Nessuna modifica architetturale al sistema Handoff
- [ ] Scratchpad Hermes non duplicato
- [ ] Recovery manuale, non automatico

### Criterio 4: Conformità vault (verifica Clio)
- [ ] Naming convention file `Library/Handoff/` rispettata
- [ ] Frontmatter completo (title, tags, aliases, cssclasses)
- [ ] Struttura documenti coerente con il vault
- [ ] Nessun file orfano o riferimento rotto

---

## Rischi e Mitigazioni

| Rischio | Probabilità | Impatto | Mitigazione |
|---------|-------------|---------|-------------|
| Hermes non rileva task interrotto | Media | Alto | Check esplicito su `output_expected` in scratchpad; log di debug |
| Utente confuso da opzioni recovery | Bassa | Medio | Messaggio chiaro con 3 opzioni (riprendi/annulla/ignora) |
| Piano troppo prolisso per approval | Media | Medio | Limite massimo 5 righe per passaggio; formato tabellare |
| Tag recovery non interpretato | Bassa | Alto | Formato fisso `[RECOVERY NEEDED: TaskID]`; parsing regex semplice |
| Sobreccarico scratchpad Hermes | Bassa | Medio | Mantenere solo ultimi 10 task; archiviare completati |

---

## Note di Implementazione

### Modifiche al prompt Hermes (estratto)

```
## Startup Check
All'avvio, verifica i task in scratchpad con stato `in_progress`.
Per ogni task senza file corrispondente in `output_expected`:
1. Aggiungi tag `[RECOVERY NEEDED: <task_id>]`
2. Segnala all'utente: "Task interrotto: <descrizione>. RIPRENDI/ANNULLA/IGNORA?"

## Plan Approval
Prima di delegare un task, valuta:
- Se ha più di 2 passaggi OPPURE coinvolge più di 1 worker
- Se sì, genera piano sintetico e chiedi approvazione esplicita
- Non procedere senza risposta positiva dell'utente

Formato piano:
```
Piano: [Titolo]
1. [Worker] - [Azione]
2. [Worker] - [Azione]
Procedo? (sì/no)
```
```

---

**Documento redatto da**: Clio, Archivista Digitale  
**Verifica conformità vault**: In corso  
**Stato**: Pronto per revisione Hermes
