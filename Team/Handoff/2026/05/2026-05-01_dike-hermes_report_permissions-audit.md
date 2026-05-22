---
title: "Revisione Permessi Subagenti — Team Olimpo"
date: "2026-05-01"
author: "Dike"
type: "audit"
stato: "da-processare"
destinatario: "hermes"
tags: [audit, permissions, security, team-structure]
---

# Revisione Completa Permessi Subagenti — Team Olimpo

**Data analisi**: 2026-05-01  
**Analista**: Dike  
**Scope**: File in `.opencode/agents/*.md` (8 agenti)  
**Destinatario**: Hermes (orchestratore)

---

## 1. Sintesi Esecutiva

L'analisi dei permessi (tool access) dei subagenti del Team Olimpo rivela una configurazione funzionale ma con **incoerenze significative** nel principio del minimo privilegio.

**Rilevamenti chiave**:
- **6 su 7 subagenti** dispongono del permesso `task` (delega ad altri agenti), ma solo 2 (Hermes, Atena) hanno un ruolo che giustifica questa capacità.
- I permessi `read` e `edit` sono uniformemente assegnati a tutti gli agenti, configurazione appropriata al modello operativo del team.
- Il permesso `bash` è correttamente limitato a soli 3 agenti (hermes, efesto, clio), con approccio prudente (`ask`).
- I permessi specialistici (`webfetch`, `websearch`) sono correttamente ristretti a Proteo.

**Raccomandazione principale**: revoca del permesso `task` ai subagenti che non hanno funzioni di orchestrazione/delega, riducendo superficie di errore e allineando permessi a ruolo.

---

## 2. Matrice Permessi Subagenti

| Agente | Ruolo | read | edit | bash | task | webfetch | websearch | Modello |
|--------|-------|------|------|------|------|----------|-----------|---------|
| **hermes** | Orchestratore (primary) | ✅ allow | ✅ allow | ⚠️ ask | ✅ allow | ❌ | ❌ | xai/grok-code-fast-1 |
| **proteo** | Ricercatore | ✅ allow | ✅ allow | ❌ | ✅ allow | ✅ allow | ✅ allow | opencode/big-pickle |
| **atena** | HR Manager | ✅ allow | ✅ allow | ❌ | ✅ allow | ❌ | ❌ | opencode/big-pickle |
| **efesto** | Sviluppatore Python | ✅ allow | ✅ allow | ⚠️ ask | ✅ allow | ❌ | ❌ | xai/grok-code-fast-1 |
| **clio** | Archivista Digitale | ✅ allow | ✅ allow | ⚠️ ask | ✅ allow | ❌ | ❌ | opencode/big-pickle |
| **dike** | Analista KBA | ✅ allow | ✅ allow | ❌ | ✅ allow | ❌ | ❌ | opencode/big-pickle |
| **metis** | Thinking Partner | ✅ allow | ✅ allow | ❌ | ✅ allow | ❌ | ❌ | opencode/big-pickle |
| **calliope** | Naming Specialist | ✅ allow | ✅ allow | ❌ | ✅ allow | ❌ | ❌ | opencode/big-pickle |

**Legenda**: ✅ allow | ⚠️ ask (richiede approvazione) | ❌ non disponibile

---

## 3. Analisi per Agente

### 3.1 Hermes (Orchestratore — Primary)
**Permessi attuali**: read ✅, edit ✅, bash ⚠️, task ✅

**Coerenza**: ✅ Coerente
- `task`: necessario per delega (core del ruolo)
- `bash`: appropriato con `ask` (può coordinare operazioni sistema)
- `read/edit`: necessari per gestione brief, registro, coordinamento

**Note**: Configurazione corretta. Come primary agent, ha visibilità su tutto.

---

### 3.2 Proteo (Ricercatore Senior)
**Permessi attuali**: read ✅, edit ✅, task ✅, webfetch ✅, websearch ✅

**Coerenza**: ⚠️ Parzialmente coerente
- `webfetch/websearch`: ✅ appropriati (core del ruolo di ricerca)
- `task`: ❌ **NON coerente** — il file agente dichiara esplicitamente: *"Non orchestri il lavoro del team. Quello è Hermes."*
- `read/edit`: ✅ necessari per produzione output in `Library/Handoff/`

**Raccomandazione**: Revocare `task`. Proteo non deve delegare ad altri agenti.

---

### 3.3 Atena (HR Manager / Agent Designer)
**Permessi attuali**: read ✅, edit ✅, task ✅

**Coerenza**: ✅ Coerente
- `task`: ✅ appropriato — delega a Calliope per scelta nomi ("Delega (via Agent) | Calliope")
- `read/edit`: ✅ necessari per creazione file `.md` e aggiornamento registro

**Note**: Unico subagente (oltre a Hermes) per cui `task` è giustificato.

---

### 3.4 Efesto (Sviluppatore Python)
**Permessi attuali**: read ✅, edit ✅, bash ⚠️, task ✅

**Coerenza**: ⚠️ Parzialmente coerente
- `bash`: ✅ appropriato con `ask` (sviluppo, test, esecuzione script)
- `task`: ❌ **NON coerente** — Efesto è un esecutore, non un orchestratore. Nessun riferimento nel ruolo a delega ad altri agenti.
- `read/edit`: ✅ necessari per sviluppo script

**Raccomandazione**: Revocare `task`. Non ci sono scenari documentati dove Efesto debba spawnare altri agenti.

---

### 3.5 Clio (Archivista Digitale)
**Permessi attuali**: read ✅, edit ✅, bash ⚠️, task ✅

**Coerenza**: ⚠️ Parzialmente coerente
- `bash`: ✅ appropriato con `ask` (esecuzione `pdf_converter`)
- `task`: ❌ **NON coerente** — Clio dichiara: *"Non decidere autonomamente quali documenti processare. Ricevi istruzioni da Hermes."* e *"Non interagisci direttamente — i file passano tramite Hermes"*
- `read/edit`: ✅ necessari per gestione `Library/documents/` e metadati

**Raccomandazione**: Revocare `task`. Clio opera in modo autonomo o su istruzioni dirette, non delega.

---

### 3.6 Dike (Analista KBA)
**Permessi attuali**: read ✅, edit ✅, task ✅

**Coerenza**: ❌ Non coerente
- `task`: ❌ **NON coerente** — Dike è un analista che produce record strutturati. Il file agente dichiara: *"Non decidi le priorita' di business: produci lo score, non decidi cosa farne."* Nessuna funzione di delega.
- `read/edit`: ✅ necessari per lettura KBA e creazione record in `kba_catalog/records/`

**Raccomandazione**: Revocare `task`. Dike opera in analisi isolata.

---

### 3.7 Metis (Thinking Partner)
**Permessi attuali**: read ✅, edit ✅, task ✅

**Coerenza**: ❌ Non coerente
- `task`: ❌ **NON coerente** — Metis dichiara esplicitamente: *"Non sei un esecutore. Non scrivi codice, non produci documenti, non crei artefatti. Se l'utente ha bisogno di esecuzione, suggerisci di rivolgersi al membro appropriato."*
- `read`: ✅ necessario per analisi file di progetto ("Puoi usare Read, Glob e Grep se l'utente vuole ragionare su qualcosa")
- `edit`: ⚠️ **Controverso** — Metis dichiara *"Non creare, modificare o scrivere file. Mai."* — il permesso `edit` non dovrebbe essere necessario.

**Raccomandazione**: Revocare `task` e valutare revoca `edit` (vedi Sezione 4.1).

---

### 3.8 Calliope (Naming Specialist)
**Permessi attuali**: read ✅, edit ✅, task ✅

**Coerenza**: ❌ Non coerente
- `task`: ❌ **NON coerente** — Calliope riceve richieste e produce proposte di naming. Nessun riferimento a delega ad altri agenti. (La delega Atena → Calliope usa il `task` di Atena, non di Calliope).
- `read/edit`: ✅ necessari per lettura `Registro.md` e produzione proposte

**Raccomandazione**: Revocare `task`.

---

## 4. Gap e Sovrapposizioni

### 4.1 Gap Identificati

| Gap | Impatto | Agente/i |
|-----|---------|----------|
| **`task` non giustificato** | 6 subagenti possono teoricamente delegare, ma non dovrebbero. Rischio di comportamenti non coordinati o loop di delega. | proteo, efesto, clio, dike, metis, calliope |
| **`edit` per Metis** | Metis dichiara esplicitamente di non scrivere/modificare file. Il permesso `edit` è contraddittorio con il ruolo. | metis |
| **Mancanza di `bash` per Hermes** | Hermes ha `bash: ask`, ma come orchestratore potrebbe avere bisogno di maggiore fluidità operativa. Da valutare se `allow` invece di `ask`. | hermes |

### 4.2 Sovrapposizioni

| Sovrapposizione | Valutazione |
|----------------|-------------|
| `read` + `edit` su tutti gli agenti | ✅ **Appropriata** — tutti producono output su filesystem |
| `bash: ask` su 3 agenti operativi | ✅ **Appropriata** — allinea necessità tecniche (efesto=dev, clio=tools, hermes=orchestration) |
| `webfetch` + `websearch` solo su Proteo | ✅ **Appropriata** — coerente con ruolo di ricerca |

### 4.3 Incoerenze con le Regole Operative

| Agente | Incoerenza | Riferimento nel file agente |
|--------|------------|---------------------------|
| **Proteo** | Ha `task` ma dichiara "Non orchestro" | *"Non orchestri il lavoro del team. Quello è Hermes."* |
| **Metis** | Ha `edit` ma dichiara "Non creare/modificare" | *"Non creare, modificare o scrivere file. Mai."* |
| **Metis** | Ha `task` ma dichiara "Non sei un esecutore" | *"Non sei un esecutore... Se l'utente ha bisogno di esecuzione, suggerisci..."* |
| **Calliope** | Ha `task` ma non ha funzioni di delega | Nessun riferimento a delega nel processo operativo |
| **Dike** | Ha `task` ma è analista isolato | *"Non decidi le priorita'... produci lo score"* |
| **Efesto** | Ha `task` ma è sviluppatore esecutore | Nessun riferimento a delega |
| **Clio** | Ha `task` ma opera su istruzioni dirette | *"Non interagisci direttamente — i file passano tramite Hermes"* |

---

## 5. Raccomandazioni

### 5.1 Prioritarie (Alta)

**R1 — Revoca `task` ai subagenti non orchestratori**  
Modificare i seguenti file in `.opencode/agents/`:
- `proteo.md`: rimuovere `task: allow`
- `efesto.md`: rimuovere `task: allow`
- `clio.md`: rimuovere `task: allow`
- `dike.md`: rimuovere `task: allow`
- `metis.md`: rimuovere `task: allow`
- `calliope.md`: rimuovere `task: allow`

**Motivazione**: Allineamento a principio del minimo privilegio. Solo Hermes (orchestratore) e Atena (delega a Calliope) necessitano di `task`.

---

**R2 — Valutare revoca `edit` per Metis**  
Metis dichiara esplicitamente di non scrivere file. Se il `task` tool richiede `edit` (da verificare nell'implementazione OpenCode), la revoca di `task` potrebbe bastare. Altrimenti, rimuovere `edit: allow` da `metis.md`.

**Motivazione**: Coerenza tra permessi e dichiarazioni operative.

---

### 5.2 Secondarie (Media)

**R3 — Valutare `bash: allow` per Hermes**  
Hermes attualmente ha `bash: ask`. Come orchestratore che coordina operazioni file system (creazione cartelle, spostamenti in Archivio, ecc.), potrebbe beneficiare di `bash: allow` per fluidità operativa.

**Motivazione**: Ridurre attriti nelle operazioni di coordinamento.

---

**R4 — Aggiungere sezione "Permessi" nelle Linee Guida**  
In `AGENTS.md` o documento dedicato, definire criteri chiari per assegnazione permessi basati su:
- Ruolo (orchestratore vs esecutore vs analista)
- Necessità documentate nel file agente
- Principio del minimo privilegio

**Motivazione**: Prevenire futuri assegnamenti erronei.

---

### 5.3 Configurazione Post-Raccomandazioni

| Agente | read | edit | bash | task | webfetch | websearch |
|--------|------|------|------|------|----------|-----------|
| hermes | ✅ | ✅ | ⚠️→✅* | ✅ | ❌ | ❌ |
| proteo | ✅ | ✅ | ❌ | ❌* | ✅ | ✅ |
| atena | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| efesto | ✅ | ✅ | ⚠️ | ❌* | ❌ | ❌ |
| clio | ✅ | ✅ | ⚠️ | ❌* | ❌ | ❌ |
| dike | ✅ | ✅ | ❌ | ❌* | ❌ | ❌ |
| metis | ✅ | ✅→❌* | ❌ | ❌* | ❌ | ❌ |
| calliope | ✅ | ✅ | ❌ | ❌* | ❌ | ❌ |

*✅ = allow, ⚠️ = ask, ❌ = non presente, → = modifica raccomandata*

---

## 6. Analisi di Sicurezza

### 6.1 Superficie di Attacco
La presenza di `task` su 6 subagenti espone a:
- **Loop di delega**: A chiama B che chiama A (teoricamente possibile)
- **Comportamenti non coordinati**: Subagenti che spawnano altri agenti senza passare da Hermes
- **Violazione protocollo**: Il protocollo Team Olimpo stabilisce che "l'utente interagisce solo con Hermes"

### 6.2 Principio del Minimo Privilegio
Configurazione attuale: **6 agenti su 7 subagenti hanno privilegi di delega non necessari** (85% sovra-permessi in questa categoria).

Configurazione raccomandata: **Solo 2 agenti con `task`** (Hermes, Atena) — riduzione del 67% della superficie.

---

## 7. Impatto Operativo delle Modifiche

| Modifica | Impatto | Rischi |
|----------|---------|--------|
| Revoca `task` a 6 agenti | Nessun impatto negativo — ruoli non prevedono delega | Nessuno identificabile |
| Revoca `edit` a Metis | Metis non potrà più leggere/modificare file — coerente col ruolo | Se Metis dovesse mai produrre output diretto, servirebbe ripristino |
| `bash: allow` per Hermes | Maggiore fluidità in operazioni file system | Rischio teorico di esecuzione non intenzionale (mitigato da responsabilità Hermes) |

---

## 8. Conclusioni

La revisione rivela che il Team Olimpo ha una struttura di permessi **funzionale ma sovra-permessa**. Il problema principale non è nell'assegnazione di permessi pericolosi (es. `bash` è ben controllato), ma nella violazione del principio del minimo privilegio per il permesso `task`.

**Punti chiave**:
1. ✅ Permessi specialistici (`webfetch`, `websearch`) correttamente ristretti
2. ✅ `bash` limitato ai 3 agenti che ne hanno reale necessità
3. ❌ `task` assegnato a 6 agenti che dichiarano esplicitamente di non dover delegare
4. ⚠️ Incoerenza `edit` per Metis rispetto alle sue regole operative

**Azioni immediate raccomandate**:
1. Applicare **R1** (revoca `task` ai 6 subagenti)
2. Valutare **R2** (revoca `edit` per Metis)
3. Documentare criteri di assegnazione permessi per futuri membri

---

**Stato**: Pronto per revisione di Hermes  
**Priorità**: Alta (allineamento strutturale)  
**Sforzo stimato**: 15 minuti (modifica 6 file YAML frontmatter)
