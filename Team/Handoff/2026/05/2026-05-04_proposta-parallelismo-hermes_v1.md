---
title: "Proposta Parallelismo Selettivo per Hermes"
data: 2026-05-04
membro: "Metis"
versione: "v1"
step-corrente: "3-proposta"
stato-generale: "in-corso"
tags: [proposta, parallelismo, hermes, fase1, orchestrazione]
aliases: [proposta-parallelismo-hermes-v1]
---

# Proposta: Integrazione Parallelismo Selettivo nel Prompt di Hermes

## 1. Sintesi della proposta

Estendere la sezione "Decomposizione dei task" del prompt di Hermes (hermes.md righe 171-173) con un meccanismo leggero di **valutazione delle dipendenze** che permetta di identificare subtask indipendenti e lanciarli in parallelo tramite il tool `task` di OpenCode. Il meccanismo mantiene l'architettura esistente (Hermes orchestratore, mai esecutore), si integra con lo scratchpad per tracciare le deleghe parallele, e non introduce complessita' strutturale — aggiunge solo una domanda di filtro prima di delegare: *"questi subtask dipendono l'uno dall'altro?"*.

---

## 2. Analisi del prompt attuale

### Punti di forza

- **Gia' presente il concetto**: la sezione "Decomposizione dei task" (riga 171-173) contiene gia' la frase *"Subtask indipendenti → parallelo. Dipendenti → serializzati."* — il principio c'e', manca l'operativizzazione.
- **Scratchpad configurato**: le regole di aggiornamento (righe 30-33 e sezione "Gestione dello stato") forniscono il terreno per tracciare le deleghe parallele.
- **Briefing strutturato**: il template a 4 sezioni e le "tre domande prima di delegare" danno a Hermes un framework decisionale gia' solido.
- **Permesso `task` abilitato**: il frontmatter conferma `permission.task: allow`, quindi l'infrastruttura c'e'.

### Gap rispetto al parallelismo

| Gap | Dettaglio |
|-----|-----------|
| **Nessun criterio operativo** per "indipendente" | La frase "subtask indipendenti → parallelo" e' un principio, non un algoritmo. Hermes non ha domande guida per decidere. |
| **Nessun flusso di raccolta risultati** | Non e' specificato come Hermes gestisce il "dopo" — quando tutti i subtask paralleli completano, come si sintetizza? |
| **Scratchpad non menziona task_id multipli** | Le convenzioni scratchpad mostrano esempi con un task alla volta. Nessuna indicazione su come registrare 2-3 deleghe parallele simultanee. |
| **No esempio concreto** | Hermes non ha mai visto un caso d'uso di parallelismo nel proprio prompt. Senza esempio, il pattern rimane astratto. |
| **Anti-pattern non esplicitato** | Il registro errori ricorrenti (riga 189) menziona "deleghe seriali anche quando i task sono chiaramente indipendenti" ma non e' collegato alla sezione di decomposizione. |

---

## 3. Modifiche proposte

### 3.1 Estensione della sezione "Decomposizione dei task" (righe 171-173)

**Testo attuale** (righe 171-173):

```
### Decomposizione dei task

Scomponi per dipendenza, non per argomento. Domanda chiave: "quali subtask dipendono dall'output di altri?" Subtask indipendenti → parallelo. Dipendenti → serializzati. Esempio: nuovo membro richiede Proteo poi Atena (serie). Analisi KBA e conversione PDF → indipendenti (parallelo).
```

**Testo proposto** (sostituisce le righe 171-173):

```
### Decomposizione dei task

Scomponi per dipendenza, non per argomento. Per ogni richiesta multi-subtask, applica questo filtro:

**Criteri per subtask indipendente** (tutti devono essere veri):
1. L'output del subtask A non e' necessario come input del subtask B (e viceversa).
2. I subtask non condividono risorse che richiedono accesso esclusivo (es. stesso file in scrittura).
3. I subtask possono essere eseguiti da membri diversi senza che uno attenda l'altro.
4. La sintesi finale puo' avvenire dopo che tutti hanno completato, senza bisogno di coordinamento intermedio.

**Se tutti i criteri sono soddisfatti** → lancia le deleghe in parallelo usando il tool `task`. 
**Se anche uno solo fallisce** → serializza nell'ordine corretto.

**Esempi**:
- ✅ Parallelo: "analizza il KBA catalog e verifica la conformita' vault dei documenti convertiti" → Proteo (analisi) + Clio (conformita') in parallelo. Nessuno dipende dall'altro.
- ✅ Parallelo: "produci una guida per il pdf_converter e un report sull'architettura del team" → Calliope (guida) + Proteo (architettura) in parallelo.
- ❌ Seriale: "crea un nuovo membro per il dominio X" → Proteo (analisi dominio) PRIMA, poi Atena (costruzione profilo). Atena dipende dall'output di Proteo.
- ❌ Seriale: "converti un PDF e poi verifica la conformita' del risultato" → Efesto/Clio (conversione) PRIMA, poi Clio (verifica). La verifica dipende dal file prodotto.

**Registrazione su scratchpad prima del lancio parallelo**:
- Aggiorna `active_tasks` con una entry per ogni subtask parallelo (stesso task padre, ID diversi T-NNN).
- Imposta lo stato a `in_progress` per tutti.
- Nel body, sezione "Task in corso", annota `[PARALLELO]` prima del titolo.

**Raccolta risultati**:
- Quando tutti i subtask paralleli sono completati, aggiorna lo scratchpad (stato → `completed` per ogni subtask).
- Sintetizza i risultati in un unico output coerente per l'utente.
- Se un subtask fallisce o e' bloccato, registra il blocco e valuta se gli altri possono procedere o se e' necessario abortire.
```

### 3.2 Integrazione con le "Tre domande prima di delegare" (righe 163-169)

**Testo attuale** (righe 166-167):

```
2. *L'agente sa cosa non deve fare?* (vincoli, errori noti, anti-pattern)
```

**Modifica proposta** (aggiungere una 4a domanda, da usare SOLO quando ci sono 2+ subtask):

```
3b. *I subtask sono indipendenti?* Se si → parallelo. Se no → serializza. (Vedi "Decomposizione dei task".)
```

Posizionare come punto 3b, subito dopo la domanda 3 esistente. Non alterare le 3 domande originali — e' un'aggiunta condizionale.

### 3.3 Aggiornamento del "Registro errori ricorrenti" (riga 189)

**Testo attuale** (riga 189):

```
Mantieni conoscenza attiva degli errori già commessi. Efesto sbagliato sui path relativi → ogni briefing futuro con path menziona quel precedente come anti-pattern esplicito. Mai ripetere stesso errore di briefing due volte.
```

**Modifica proposta** (aggiungere una riga alla fine della sezione):

```
Errore storico: deleghe sempre seriali anche per task indipendenti (es. ricerca + analisi lanciati in sequenza invece che in parallelo). Da oggi: applica i criteri nella sezione "Decomposizione dei task".
```

### 3.4 Aggiornamento delle "Regole operative" (righe 29-32)

**Testo attuale** (riga 31):

```
- **Gestione dello stato.** Usa sempre `Team/Hermes/Scratchpad.md` come memoria persistente. Aggiornalo prima di delegare task complessi, dopo aver ricevuto output dai membri e alla fine di ogni interazione significativa.
```

**Modifica proposta** (estendere per coprire il caso parallelo):

```
- **Gestione dello stato.** Usa sempre `Team/Hermes/Scratchpad.md` come memoria persistente. Aggiornalo:
  - Prima di delegare task complessi (incluso il lancio di deleghe parallele — registra ogni subtask con il proprio ID).
  - Dopo aver ricevuto output da ciascun membro (aggiorna lo stato del singolo subtask, non aspettare tutti).
  - Dopo aver sintetizzato i risultati di deleghe parallele (aggiornamento finale).
  - Alla fine di ogni interazione significativa con l'utente.
```

---

## 4. Esempio operativo

**Scenario**: L'utente chiede: *"Voglio che il team analizzi lo stato attuale del KBA catalog e contemporaneamente produca una proposta di naming convention per i nuovi tool Python."*

### Come Hermes processa la richiesta (flusso con parallelismo)

**Step 1 — Decomposizione**:
Hermes identifica due subtask:
- A: Analisi stato KBA catalog → dominio di **Dike** (analista processi, catalogazione KBA)
- B: Proposta naming convention tool Python → dominio di **Efesto** (sviluppatore Python, convenzioni CLI)

**Step 2 — Filtro indipendenza**:
- L'output di Dike serve a Efesto? No.
- L'output di Efesto serve a Dike? No.
- Condividono risorse in scrittura? No (leggono entrambi file diversi).
- La sintesi finale puo' avvenire dopo entrambi? Si.
- → **Tutti i criteri soddisfatti → PARALLELO**

**Step 3 — Aggiornamento scratchpad (PRIMA del lancio)**:

```yaml
active_tasks:
  - id: "T-010a"
    title: "Analisi stato KBA catalog"
    delegated_to: "Dike"
    status: "in_progress"
    started_at: 2026-05-04
    handoff_ref: "Library/Handoff/2026-05-04_brief-analisi-kba-dike.md"
    notes: "[PARALLELO] Parte di richiesta utente multi-dominio"
  - id: "T-010b"
    title: "Proposta naming convention tool Python"
    delegated_to: "Efesto"
    status: "in_progress"
    started_at: 2026-05-04
    handoff_ref: "Library/Handoff/2026-05-04_brief-naming-convention-efesto.md"
    notes: "[PARALLELO] Parte di richiesta utente multi-dominio"
```

**Step 4 — Lancio parallelo**:
Hermes usa il tool `task` per lanciare simultaneamente:
- Task 1: Dike con brief in `Library/Handoff/2026-05-04_brief-analisi-kba-dike.md`
- Task 2: Efesto con brief in `Library/Handoff/2026-05-04_brief-naming-convention-efesto.md`

**Step 5 — Raccolta risultati** (quando entrambi completano):
- Dike produce: `Library/deliverables/analisi-stato-kba-catalog-2026-05.md`
- Efesto produce: `Library/Handoff/2026-05-04_proposta-naming-convention-efesto_v1.md`
- Hermes aggiorna scratchpad: entrambi → `completed`
- Hermes sintetizza: presenta all'utente i due risultati in un unico messaggio strutturato

**Step 6 — Aggiornamento finale scratchpad**:

```yaml
active_tasks: []
members_status:
  Dike:
    status: "idle"
    current_task: null
    last_contact: 2026-05-04
    blocks: []
  Efesto:
    status: "idle"
    current_task: null
    last_contact: 2026-05-04
    blocks: []
```

**Tempo risparmiato**: invece di (tempo_Dike + tempo_Efesto), il tempo totale e' max(tempo_Dike, tempo_Efesto).

---

## 5. Criteri di accettazione

Per verificare che l'integrazione funzioni correttamente:

| # | Criterio | Come verificare |
|---|----------|-----------------|
| 1 | Hermes identifica correttamente subtask indipendenti vs dipendenti | Test con 3 richieste: 1 con subtask indipendenti, 1 con dipendenti, 1 mista. Hermes deve parallelizzare solo la prima. |
| 2 | Lo scratchpad viene aggiornato prima del lancio parallelo con task_id multipli | Verificare che `active_tasks` contenga entry separate (T-NNNa, T-NNNb) per ogni subtask parallelo. |
| 3 | Lo scratchpad viene aggiornato dopo ogni completamento individuale | Verificare che lo stato di ogni subtask cambi a `completed` quando quel membro finisce, non solo quando tutti hanno finito. |
| 4 | La sintesi finale avviene solo quando tutti i subtask paralleli sono completi | Verificare che Hermes non restituisca risultati parziali all'utente. |
| 5 | Le modifiche non introducono verbosita' nel prompt | Il testo aggiunto non supera le ~30 righe. Lo stile resta "rapido e diretto". |
| 6 | L'architettura non cambia | Hermes continua a non eseguire compiti direttamente. Usa solo il tool `task` per delegare. |
| 7 | Il formato output rispetta le convenzioni vault | Frontmatter corretto, wikilink dove applicabile, slug nei nomi file, tags in forma plurale. |

---

## 6. Impatto su scratchpad e flussi esistenti

### 6.1 Cambiamenti minimi richiesti

Il meccanismo e' progettato per avere **impatto zero** sui flussi esistenti quando il parallelismo non si applica. I task singoli o dipendenti continuano esattamente come prima.

### 6.2 Nuovi pattern da introdurre nello scratchpad

**Pattern 1 — Task paralleli con ID composti**:
Quando un task padre viene scomposto in subtask paralleli, usare il suffisso `a`, `b`, `c` (es. `T-010a`, `T-010b`, `T-010c`). Questo permette di:
- Raggruppare visivamente i subtask dello stesso task padre.
- Tracciare lo stato individuale di ciascuno.
- Identificare rapidamente se uno e' bloccato mentre gli altri procedono.

**Pattern 2 — Tag `[PARALLELO]` nel body**:
Nella tabella "Task in corso" del body, aggiungere `[PARALLELO]` come prefisso al titolo. Esempio:

```
| T-010a | [PARALLELO] Analisi KBA catalog | Dike | in_progress | ... |
| T-010b | [PARALLELO] Naming convention | Efesto | in_progress | ... |
```

**Pattern 3 — Aggiornamento incrementale**:
Lo scratchpad va aggiornato **ogni volta che un subtask parallelo completa**, non solo alla fine. Questo permette a Hermes (in caso di context switch o recovery) di sapere esattamente quali subtask sono ancora pending.

### 6.3 Flusso integrato (aggiornato)

Il flusso dalla Parte 6 delle Convenzioni-Scratchpad viene esteso cosi':

```
1. Utente → Hermes: nuova richiesta
2. Hermes → Decomposizione: identifica subtask e valuta dipendenze
3a. Se dipendenti → delega seriale (flusso esistente)
3b. Se indipendenti → delega parallela:
    a. Hermes → Scratchpad: aggiorna active_tasks con entry multiple
    b. Hermes → Handoff: crea briefing per ciascun agente
    c. Hermes → task tool: lancia tutti i subtask simultaneamente
    d. Ogni agente → Lavora → Produce output (indipendentemente dagli altri)
    e. Hermes → Scratchpad: aggiorna stato di ogni subtask al completamento
    f. Hermes → Sintesi: raccoglie tutti i risultati, produce output unificato
4. Hermes → Scratchpad: aggiornamento finale
5. Hermes → Utente: restituisce risultato
```

### 6.4 Impatto sulle convenzioni esistenti

| Convenzione | Impatto | Azione |
|-------------|---------|--------|
| Convenzioni-Scratchpad.md | Minimo | Aggiungere nota sui task_id composti (`T-NNNx`) e sul pattern `[PARALLELO]` |
| Flusso creazione membro | Zero | Resta seriale (Proteo → Atena). Nessuna modifica. |
| Flusso ricerca/analisi | Minimo | Se la richiesta e' singola, resta invariato. Se multi-dominio, si applica il nuovo filtro. |
| Registro errori ricorrenti | Minimo | Aggiungere l'errore storico "deleghe sempre seriali" come promemoria. |

### 6.5 Cosa non cambia

- **Nessuna nuova infrastruttura**: si usa solo il tool `task` gia' abilitato.
- **Nessun nuovo file o cartella**: lo scratchpad esistente gestisce tutto.
- **Nessun cambio di architettura**: Hermes resta orchestratore puro.
- **Nessun cambiamento nei permessi**: i subagenti mantengono i loro permessi esistenti.
- **Nessun impatto sui task singoli**: il filtro di indipendenza si attiva solo quando ci sono 2+ subtask.
