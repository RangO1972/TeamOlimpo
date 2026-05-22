---
title: "Brief Fase 1 - Parallelismo Selettivo per Hermes"
data: 2026-05-04
membro: "Metis"
versione: "v1"
step-corrente: "1-brief"
stato-generale: "in-corso"
tags: [brief, fase1, parallelismo, hermes, metis]
aliases: [brief-fase1-parallelismo]
---

# Brief: Integrazione Parallelismo Selettivo nel Prompt di Hermes

**Contesto**: Stiamo implementando la **Fase 1** del piano di miglioramento derivato dall'analisi comparativa `Library/deliverables/analisi-team-olimpo-vs-opencode-claude.md`. Lo scratchpad di stato per Hermes e' gia' stato implementato e istruito. Ora si passa al secondo item ad alta priorita': abilitare il **parallelismo selettivo** per task con subtask indipendenti.

**Riferimento principale**: Sezione 4.1 B e 5.1 della analisi (Parallelismo Selettivo).

---

## 1. Obiettivo

Produci una **proposta concreta di integrazioni** al prompt di Hermes (`.opencode/agents/hermes.md`) che abiliti il parallelismo selettivo. 

Hermes deve essere in grado di:
- Identificare automaticamente (o con domanda esplicita) quando una richiesta utente puo' essere scomposta in subtask **indipendenti** (i cui output non dipendono l'uno dall'altro).
- Lanciare deleghe **in parallelo** usando il tool `task` di OpenCode (che supporta esecuzioni concorrenti).
- Raccogliere e sintetizzare i risultati una volta che tutti i subtask paralleli sono completati.
- Mantenere il controllo e la visibilita' tramite scratchpad (già implementato).

L'obiettivo e' ridurre il tempo totale per task multi-dominio (es. ricerca + strategia, analisi + verifica conformita') dal tempo somma a tempo massimo.

---

## 2. Anti-pattern

**Non fare**:
- Non duplicare la sezione esistente "Decomposizione dei task" (gia' presente in hermes.md righe 171-173) — integrala o estendila, non riscriverla.
- Non abilitare parallelismo per task **dipendenti** (es. Proteo → Atena per creazione membro; o ricerca che serve come input a sviluppo).
- Non introdurre complessita' eccessiva: il meccanismo deve rimanere semplice e allineato allo stile "rapido e diretto" di Hermes.
- Non cambiare l'architettura (Hermes resta orchestratore che non esegue mai direttamente).
- Non ignorare la necessita' di aggiornare lo scratchpad prima di lanciare deleghe parallele e dopo aver raccolto i risultati.
- Non proporre modifiche che richiedano tool o infrastrutture non presenti (usa solo `task` tool gia' abilitato).

**Errori noti da evitare** (da registro errori ricorrenti):
- Deleghe seriali anche quando i task sono chiaramente indipendenti (collo di bottiglia attuale).

---

## 3. Formato output

Crea un file Markdown in `Library/Handoff/2026-05-04_proposta-parallelismo-hermes_v1.md` con la seguente struttura:

1. **Sintesi della proposta** (1 paragrafo)
2. **Analisi del prompt attuale** — punti di forza e gap rispetto al parallelismo
3. **Modifiche proposte** — in forma di diff o sezioni esatte da inserire/aggiornare nel prompt (con riferimenti a righe o sezioni)
4. **Esempio operativo** — un caso d'uso concreto (es. "utente chiede analisi KBA + ottimizzazione workflow") con come Hermes lo scomporrebbe e lancerebbe in parallelo
5. **Criteri di accettazione per le modifiche** (come verificare che l'integrazione funzioni)
6. **Impatto su scratchpad e flussi esistenti** (come integrare con gli aggiornamenti obbligatori dello scratchpad)

Il file deve essere **pronto per revisione** da Hermes e successivo editing del prompt.

---

## 4. Criteri di accettazione

- [ ] La proposta identifica chiaramente i criteri per "subtask indipendente" (es. "non condividono output, non hanno dipendenze temporali, possono essere eseguiti da membri diversi senza sincronizzazione")
- [ ] Le modifiche al prompt sono **concrete** (snippet di testo da aggiungere, non solo concetti)
- [ ] Il parallelismo e' **selettivo** (non sempre parallelo; Hermes valuta caso per caso)
- [ ] Il meccanismo prevede aggiornamento scratchpad **prima** del lancio parallelo (con task_id multipli) e **dopo** la sintesi
- [ ] Esempio operativo e' realistico e allineato ai task tipici del Team Olimpo (ricerca, analisi, documentazione, strategia)
- [ ] Le modifiche rispettano lo stile di Hermes (cordiale, efficiente, rapido) e non introducono verbosita'
- [ ] Output conforme alle convenzioni vault (frontmatter corretto, wikilink, slug)

**Riferimenti da consultare**:
- `Library/deliverables/analisi-team-olimpo-vs-opencode-claude.md` (sezioni 4.1 B, 5.1, 3.2.2)
- `.opencode/agents/hermes.md` (intera, in particolare Metodologia di orchestrazione e Decomposizione dei task)
- `Team/Hermes/Convenzioni-Scratchpad.md` (flusso con scratchpad)
- `Team/Hermes/Scratchpad.md` (stato corrente T-002)

**Nota per Metis**: Poiche' questo e' un task di ottimizzazione operativa, focalizzati su flussi di lavoro e colli di bottiglia. Non e' necessario scrivere codice — solo proporre il testo da integrare nel prompt.

Una volta pronto, notifica Hermes con riferimento al file prodotto.
