# Agent Qualification Framework (AQF) — Team Olimpo

**Prodotto da**: Metis (Thinking Partner & Stratega)
**Data**: 2026-05-16
**Destinatario**: Hermes
**Input**: Proteo (ricerca IQ/OQ/PQ) + Dike (mappatura processi e gap analysis)
**Stato**: Analisi strategica — in attesa di approvazione per implementazione

---

## Indice

1. [Visione d'insieme](#1-visione-dinsieme)
2. [Framework AQF per fase](#2-framework-aqf-per-fase)
3. [Prioritizzazione per processi](#3-prioritizzazione-per-processi)
4. [Raccomandazioni operative](#4-raccomandazioni-operative)
5. [Rischi e attenzioni](#5-rischi-e-attenzioni)
6. [Sintesi per Hermes](#6-sintesi-per-hermes)

---

## 1. Visione d'insieme

### 1.1 Mappa concettuale: dal farmaceutico al sistema agentico

```
Farmaceutico (FDA/ISPE)              Team Olimpo (Agenti AI)
─────────────────────────            ─────────────────────────────

DQ (Design Qualification)   ───→   ADQ — Agent Design Qualification
  Verifica design prima              Review design/prompt/identità
  di costruire                       PRIMA di creare il membro

IQ (Installation Qual.)     ───→   AEQ — Agent Environment Qual.
  Verifica installazione             Verifica ambiente, tool, permessi
  corretta                           PRIMA di eseguire un task

OQ (Operational Qual.)      ───→   AOQ — Agent Operational Qual.
  Verifica operatività in            Test operativi su range di input
  range definiti                     (edge case, failure mode, recovery)

PQ (Performance Qual.)      ───→   APQ — Agent Performance Qual.
  Verifica performance in            Verifica output consistenti su
  condizioni reali                   task produttivi reali

CPV (Continued Process      ───→   ACM — Agent Continuous Monitoring
  Verification)                      Monitoraggio continuo: deviation
  Monitoraggio continuo              rate, quality trend, drift detection
```

### 1.2 Principio ispiratore: CSA (risk-based) > IQ/OQ/PQ tradizionale

Il framework farmaceutico tradizionale è nato per **macchine fisiche** che producono farmaci. Applicarlo pari pari a un sistema di agenti AI sarebbe un errore: creerebbe burocrazia senza valore, protocolli rigidi per sistemi che cambiano ogni settimana.

**La scelta giusta è CSA (Computer Software Assurance) — FDA 2022+**:

| Dimensione | IQ/OQ/PQ tradizionale | CSA approach | Scelta AQF |
|-----------|----------------------|--------------|------------|
| Documentazione | Protocolli cartacei pre-approvati | Assurance activities leggere | **CSA → leggero** |
| Test | Script rigidi, tutti uguali | Risk-based, mirati | **CSA → su misura** |
| Frequenza | One-shot, poi CPV | Ciclo continuo | **Ibrido** |
| Deviazioni | Blocco del rilascio | Investigazione + azione | **CSA → snello** |
| Overhead | Alto | Proporzionale al rischio | **CSA → minimo** |

**Regola d'oro AQF**: *tanta assurance quanto serve, non più di quanto serve.*

### 1.3 Classificazione per rischio dei membri

Prima di applicare l'AQF, ogni membro va classificato. Questo determina *quanta* assurance serve.

| Classe | Criterio | Esempi | Livello AQF richiesto |
|--------|----------|--------|----------------------|
| **Alto** | Impatto diretto su output utente finale, orchestrazione, dati critici | Hermes, Atena | ADQ completo + AEQ + AOQ + APQ + ACM |
| **Medio** | Impatto su qualità vault o processi interni, ma non direttamente su utente | Proteo, Efesto, Clio, Dike | ADQ essenziale + AOQ + ACM |
| **Basso** | Produzione contenuti tematici, task ben delimitati | Euterpe, Calliope, Hermione | ADQ minimo + ACM leggero |

> **Nota**: la classificazione è dinamica. Se un membro basso rischio inizia a gestire dati critici, va riclassificato.

---

## 2. Framework AQF per fase

### 2.1 ADQ — Agent Design Qualification

| | |
|---|---|
| **Nome adattato** | Agent Design Qualification |
| **Ispirato a** | DQ (Design Qualification) |
| **Cosa significa** | Verifica che il design/identità/prompt di un nuovo membro soddisfi i requisiti PRIMA di crearlo. È il "quality gate" tra la ricerca di Proteo e la costruzione di Atena. |
| **Quando si applica** | Prima della creazione di ogni nuovo membro del Team Olimpo. |

**Come implementarlo** (operazioni concrete):

1. **Risk classification**: Hermes assegna una classe di rischio (alto/medio/basso) al nuovo membro in base all'impatto atteso.
2. **Design review checklist**: Atena compila una checklist prima di scrivere il file agente:
   - [ ] Frontmatter YAML completo (nome, ruolo, archetipo, competenze)
   - [ ] Identità e personalità definite in modo non ambiguo
   - [ ] Competenze mappate su operazioni concrete (non generiche)
   - [ ] Istruzioni operative chiare (cosa fare, cosa NON fare)
   - [ ] Limiti e confini esplicitati (quando rifiutare un task)
   - [ ] Tool abilitati coerenti con le competenze dichiarate
   - [ ] Riferimenti a guiding documents (se applicabile)
3. **Traceability matrix**: per ogni requisito nel brief di Hermes, un test OQ che lo verificherà.
4. **DQ sign-off**: Hermes approva il design prima che Atena produca il file.

**Metriche/criteri**:
- Checklist completezza: 100% degli item verificati (requisito minimo)
- Tempo medio di design review: target < 15 min per membri basso rischio, < 30 min per alto rischio
- Numero di revisioni del design prima di approvazione: target ≤ 2

**Responsabile**: Hermes (approvazione), Atena (esecuzione design), Proteo (input analisi dominio)

---

### 2.2 AEQ — Agent Environment Qualification

| | |
|---|---|
| **Nome adattato** | Agent Environment Qualification |
| **Ispirato a** | IQ (Installation Qualification) |
| **Cosa significa** | Verifica che l'ambiente di esecuzione (tool, permessi, configurazioni) sia pronto PRIMA di eseguire un task o attivare un membro. |
| **Quando si applica** | Prima di ogni sessione di lavoro o prima di delegare un task significativo. |

**Come implementarlo** (operazioni concrete):

1. **Pre-flight check automatizzato**: script che verifica prima di ogni sessione:
   - Tool LLM raggiungibile e reattivo
   - Permessi di scrittura su `Library/Handoff/` e `Library/deliverables/`
   - Spazio disco sufficiente (soglia: > 500 MB liberi)
   - File agente `.opencode/agents/<nome>.md` valido e accessibile
   - Connessione internet attiva (per tool che la richiedono)
2. **Ambiente validation per tool specifici**:
   - **Efesto**: Python environment attivo, dipendenze installate (`pip list --format=freeze`)
   - **Proteo**: web search tool funzionante
   - **Clio**: vault Obsidian accessibile e non corrotto
3. **Fallback procedure**: se un pre-flight check fallisce, log + notifica a Hermes + non procedere.

**Metriche/criteri**:
- Tasso di successo pre-flight: target > 95%
- Tempo medio di pre-flight: target < 5 secondi
- % di fallimenti che avrebbero causato failure a metà task: target 0% (catch-all)

**Responsabile**: Hermes (trigger), Efesto (automazione pre-flight script), Dike (metriche)

---

### 2.3 AOQ — Agent Operational Qualification

| | |
|---|---|
| **Nome adattato** | Agent Operational Qualification |
| **Ispirato a** | OQ (Operational Qualification) |
| **Cosa significa** | Test operativi che verificano il corretto funzionamento del membro in range definiti: input normale, input estremo, input malformato, failure mode. |
| **Quando si applica** | Dopo la creazione del membro (pre-rilascio) e periodicamente (ogni N task o dopo modifiche al prompt). |

**Come implementarlo** (operazioni concrete):

1. **Test case standardizzati** (3-5 per membro):
   - *Happy path*: input tipico che il membro dovrebbe gestire
   - *Edge case*: input al limite (molto corto, molto lungo, ambiguo)
   - *Failure mode*: strumento non disponibile, timeout, permessi negati
   - *Rifiuto appropriato*: richiesta fuori dal dominio di competenza
2. **Acceptance criteria chiari**:
   - Risposta pertinente (non fuori tema)
   - Formato corretto (aderenza al template atteso)
   - Nessun errore tecnico (crash, loop infinito, output vuoto)
   - Tempo di risposta < soglia definita (es. 30 secondi per task semplici)
3. **Soglia di passaggio**: per membri alto rischio: 100% test passati; medio: 80%; basso: 60%.
4. **Report OQ**: file markdown con risultati, note, e decisione (passato/non passato/riferito).

**Esempio concreto** — OQ per Proteo:
| Test | Input | Criterio di accettazione |
|------|-------|------------------------|
| Happy path | "Ricerca ultime tendenze AI 2026" | Almeno 3 fonti citate, nessun link rotto |
| Edge case | "Ricerca" (input minimo) | Risposta educata che chiede chiarimenti, non crash |
| Failure mode | Tool web search non disponibile | Dice che non può completare, non inventa risultati |
| Rifiuto | "Dimmi una barzelletta" | Dice che non è nel suo dominio di competenza |

**Metriche/criteri**:
- % test passati per classe di rischio (target: alto = 100%, medio ≥ 80%, basso ≥ 60%)
- Numero di failure mode scoperti (più sono, meglio è — significa che il test è efficace)
- Tempo medio di esecuzione OQ: target < 10 min per membro

**Responsabile**: Hermes (definisce test case), Dike (traccia risultati e metriche), Singolo membro (esegue in simulazione)

---

### 2.4 APQ — Agent Performance Qualification

| | |
|---|---|
| **Nome adattato** | Agent Performance Qualification |
| **Ispirato a** | PQ (Performance Qualification) |
| **Cosa significa** | Verifica che il membro produca output consistenti e di qualità su task reali o realistici in condizioni di produzione. Non è più un test artificiale: è un "esame di maturità". |
| **Quando si applica** | Dopo OQ superato (pre-rilascio), e periodicamente (ogni 10 task o ogni 2 settimane per membri alto rischio). |

**Come implementarlo** (operazioni concrete):

1. **Task di verifica** (3-5 task produttivi reali):
   - Task rappresentativi del lavoro che il membro farà realmente
   - Misurati su: completezza, accuratezza, formattazione, tempo
2. **Quality score** composito (0-100):
   - Completezza: 30% — ha coperto tutti i punti richiesti?
   - Accuratezza: 40% — le informazioni sono corrette (verifica umana o automatica)?
   - Conformità: 20% — il formato/output rispetta le convenzioni?
   - Efficienza: 10% — tempo di completamento entro soglia?
3. **Soglia di passaggio**: score ≥ 80 per rilascio; score < 60 richiede revisione del design (ADQ).
4. **Report APQ**: markdown con score, note, e raccomandazioni.

**Esempio concreto** — APQ per Clio:
| Task | Criterio | Peso |
|------|---------|------|
| Verifica conformità di 5 documenti vault | 100% di item checklist coperti | 30% |
| Identificazione errori reali in documenti alterati | Almeno 4/5 errori trovati | 40% |
| Report conforme al template markdown standard | Struttura, frontmatter, tag corretti | 20% |
| Completamento in < 5 min | Tempo effettivo | 10% |

**Metriche/criteri**:
- Quality score medio: target ≥ 85
- Tasso di superamento APQ al primo tentativo: target ≥ 70%
- Correlazione tra score APQ e feedback utente: da monitorare

**Responsabile**: Hermes (esegue APQ su task reali), Clio (verifica conformità output), Dike (metriche e trend)

---

### 2.5 ACM — Agent Continuous Monitoring

| | |
|---|---|
| **Nome adattato** | Agent Continuous Monitoring |
| **Ispirato a** | CPV (Continued Process Verification) |
| **Cosa significa** | Monitoraggio continuo delle performance del membro nella vita operativa: deviation tracking, trend, quality drift. Non è un checkpoint — è l'osservazione sistematica di come il membro si comporta nel tempo. |
| **Quando si applica** | Continuamente, per tutta la vita operativa del membro. |

**Come implementarlo** (operazioni concrete):

1. **Deviation log strutturato**: ogni output fuori specifica genera una entry:
   ```
   data: 2026-05-16
   membro: proteo
   tipo_deviazione: output_incompleto
   descrizione: ricerca su X ha restituito solo 2 fonti invece di 3
   causa: web search tool ha timeout su terza fonte
   azione: rieseguito con parametri diversi
   esito: risolto
   ```
   Opzione leggera: frontmatter YAML nel file handoff del task.

2. **Metriche continue da tracciare** (per membro):
   - Deviation rate: # deviazioni / # task completati
   - Quality score medio (rolling average, ultimi 10 task)
   - Tempo medio di completamento per tipo task
   - Tasso di blocchi/errori (failure rate)
   - Trend: in miglioramento, stabile, in deterioramento

3. **Soglie di allarme**:
   - Deviation rate > 20% → notifica a Hermes (giallo)
   - Deviation rate > 40% → sospensione del membro + revisione ADQ (rosso)
   - Quality score < 70 per 3 task consecutivi → notifica a Hermes

4. **Review periodica**: ogni settimana, Dike produce un ACM report per i membri attivi.

**Metriche/criteri**:
- Deviation rate target: < 10% per membri alto rischio, < 20% per medio/basso
- Tempo medio tra notifica e risoluzione: target < 24h per alto rischio
- Copertura membri monitorati: target 100% per alto rischio

**Responsabile**: Dike (monitoraggio, report periodici), Hermes (interviene su allarmi), Efesto (automazione raccolta metriche)

---

## 3. Prioritizzazione per processi

Basata sulla gap analysis di Dike. Ordine di implementazione suggerito:

### 3.1 Recovery — PRIORITÀ ASSOLUTA

| Perché | Cosa manca | Cosa implementare dell'AQF | Effetto atteso |
|--------|-----------|---------------------------|----------------|
| Task bloccati restano in stallo. Nessun gate, nessuna CPV, nessun criterio. | AOQ (criteri "blocco risolto"), AEQ (ambiente check prima di riprendere), ACM (tracciamento blocchi) | AOQ per recovery (criteri standardizzati), ACM con deviation log | Riduzione tempo medio di recovery, visibilità sui blocchi |

**Impatto stimato**: ALTO — ogni task bloccato non recuperato è tempo perso e frustrazione.

### 3.2 Creazione Membro

| Perché | Cosa manca | Cosa implementare dell'AQF | Effetto atteso |
|--------|-----------|---------------------------|----------------|
| Membro creato e dimenticato. Criteri di accettazione non quantitativi. | ADQ (design review strutturata), APQ (performance check post-birth), ACM (monitoraggio prime settimane) | ADQ checklist + APQ con 3 task di verifica + ACM per primi 30 giorni | Membri più robusti, problemi individuati prima |

**Impatto stimato**: ALTO — un membro mal progettato impatta TUTTI i task che esegue.

### 3.3 Handoff

| Perché | Cosa manca | Cosa implementare dell'AQF | Effetto atteso |
|--------|-----------|---------------------------|----------------|
| "Completato" auto-dichiarato senza validazione. | AOQ (criteri di completamento), gate di accettazione con validazione esterna | AOQ leggero: frontmatter con quality_score minimo + verifica esterna | Output di qualità più consistente |

**Impatto stimato**: MEDIO-ALTO — output variabili accettati come finiti erodono la fiducia.

### 3.4 Ricerca/Analisi

| Perché | Cosa manca | Cosa implementare dell'AQF | Effetto atteso |
|--------|-----------|---------------------------|----------------|
| Nessun gate tra output Proteo e consegna utente. | AEQ (pre-flight tool check), AOQ (criteri "ricerca sufficiente") | Pre-flight check tool + AOQ con criteri di accettazione per completezza e fonti | Riduzione rischio di consegnare informazioni errate |

**Impatto stimato**: MEDIO — il rischio è reale ma mitigabile con un gate semplice.

### 3.5 KBA

| Perché | Cosa manca | Cosa implementare dell'AQF | Effetto atteso |
|--------|-----------|---------------------------|----------------|
| Deviazioni non tracciate, CPV assente. | ACM (deviation log e trend analysis), criteri AOQ per "KBA completa" | ACM con deviation log per i ritocchi manuali post-consegna | Ottimizzazione progressiva del processo KBA |

**Impatto stimato**: MEDIO — miglioramento incrementale su un processo già strutturato.

### 3.6 Conversione PDF

| Perché | Cosa manca | Cosa implementare dell'AQF | Effetto atteso |
|--------|-----------|---------------------------|----------------|
| Gate manuale, PQ limitata, nessun CPV. | AEQ (ambiente check), automazione gate, ACM (metriche qualità) | AEQ pre-flight check + automazione verifica output (frontmatter valido, path immagini) | Riduzione documenti malformati nel vault |

**Impatto stimato**: BASSO-MEDIO — il processo funziona già ragionevolmente bene.

### 3.7 Verifica Conformità

| Perché | Cosa manca | Cosa implementare dell'AQF | Effetto atteso |
|--------|-----------|---------------------------|----------------|
| Gate disaccoppiato, automazione assente. | PQ (metriche tasso di fallimento), ACM (pattern violation) | PQ metrics + trend analysis | Miglioramento incrementale |

**Impatto stimato**: BASSO — miglioramento nice-to-have, non blocca nulla.

---

## 4. Raccomandazioni operative

### 4.1 SUBITO (quick wins — entro 1 settimana)

Queste operazioni richiedono **poco sforzo, alto impatto**. Si implementano con modifiche minime ai processi esistenti, senza nuovi tool.

| # | Azione | AQF Phase | Processo | Chi | Difficoltà |
|---|--------|-----------|----------|-----|------------|
| 1 | **Deviation log in frontmatter handoff**: aggiungere campi `deviazione`, `causa`, `azione_correttiva` nel frontmatter di ogni handoff bloccato o con esito anomalo | ACM | Recovery, Handoff | Dike (template), tutti (compilazione) | ★☆☆ |
| 2 | **Pre-flight checklist mentale per Hermes**: prima di delegare un task, verificare mentalmente: tool funzionante? spazio disco? ambiente valido? Documentare in una checklist markdown in `Library/Meta/` | AEQ | Tutti | Hermes | ★☆☆ |
| 3 | **Risk classification dei membri esistenti**: assegnare classe di rischio (alto/medio/basso) a ogni membro attuale. Aggiornare frontmatter in `.opencode/agents/` con campo `risk_class` | ADQ | — | Hermes + Atena | ★☆☆ |
| 4 | **Template OQ minimo per Recovery**: definire 3 criteri standardizzati per considerare "blocco risolto" (es. tool reattivo, condizioni di blocco rimosse, log letto) | AOQ | Recovery | Dike + Hermes | ★☆☆ |
| 5 | **Quality gate su output Proteo**: Hermes aggiunge una validazione di 2 minuti prima di consegnare output Proteo all'utente (completezza: 3 fonti? accuratezza: senso generale? fonti: link vivi?) | AOQ | Ricerca | Hermes | ★☆☆ |

**Totale effort**: circa 2-3 ore in una settimana.

### 4.2 FASE 2 (media priorità — entro 2-3 settimane)

Operazioni che richiedono **strutturazione maggiore** ma sono ancora implementabili con risorse esistenti.

| # | Azione | AQF Phase | Processo | Chi | Difficoltà |
|---|--------|-----------|----------|-----|------------|
| 6 | **ADQ checklist formale per nuovi membri**: creare template markdown in `Library/Meta/` con la checklist di design review. Usare per ogni nuovo membro da oggi in poi | ADQ | Creazione Membro | Atena + Hermes | ★★☆ |
| 7 | **APQ post-creazione**: dopo la creazione di un nuovo membro, eseguire 3 task reali di verifica e calcolare quality score prima del rilascio | APQ | Creazione Membro | Hermes | ★★☆ |
| 8 | **Criteri di completamento standardizzati per handoff**: frontmanda obbligatorio con `quality_score: [1-5]` e `verifica_esterna: [true/false]` | AOQ | Handoff | Dike (template), tutti (compilazione) | ★☆☆ |
| 9 | **ACM leggero**: Dike produce un report settimanale (5 min) con deviation rate e quality score per i membri attivi | ACM | Tutti | Dike | ★★☆ |
| 10 | **Automazione pre-flight check**: script bash/Python che Hermes può lanciare all'inizio di ogni sessione per verificare ambiente | AEQ | Tutti | Efesto + Hermes | ★★☆ |

**Totale effort**: circa 5-7 ore distribuite in 2-3 settimane.

### 4.3 RIMANDARE (bassa priorità / troppo overhead per ora)

Queste operazioni hanno **valore reale** ma il costo di implementazione non è giustificato oggi.

| # | Azione | Perché rimandare | Quando rivalutare |
|---|--------|-----------------|-------------------|
| 11 | Automazione completa verifica conformità (pre-commit hook) | Troppo overhead tecnico per il beneficio attuale. Clio fa già verifica post-hoc. | Quando il vault supera 500 documenti |
| 12 | PQ per Conversione PDF con metriche dettagliate | Il tool funziona bene. Le metriche sarebbero interessanti ma non risolvono un problema reale oggi. | Se emergono problemi di qualità (tasso errori > 10%) |
| 13 | CPV completo per KBA | Il processo KBA è già strutturato. L'ACM leggero (punto 9) è sufficiente. | Se il volume KBA supera 10/settimana |
| 14 | Test OQ automatici per ogni modifica al prompt | Sarebbe ideale, ma richiede infrastructure di testing (CI/CD) che non abbiamo. | Quando il team supera 15 membri |
| 15 | ADQ retroattivo per membri esistenti | Implementarlo sui membri attuali richiederebbe ore di review per beneficio incerto. | Solo se un membro esistente mostra deterioramento |

---

## 5. Rischi e attenzioni

### 5.1 Burocratizzazione

**Rischio**: L'AQF diventa fine a se stesso. Template da riempire perché "il framework lo richiede". Il tempo speso a compilare moduli supera il tempo speso a fare.

**Come evitarlo**:
- Ogni elemento dell'AQF deve avere un **valore dimostrabile** nella prevenzione di errori reali. Se un gate non ha mai bloccato nulla in 3 mesi, si elimina.
- Regola del "costo del gate < costo dell'errore che previene" — se un errore costa 5 minuti, non creare un gate che ne richiede 10.
- Metriche di efficacia del framework stesso: quante deviazioni ha catturato? Quanto tempo ha risparmiato?

### 5.2 Paralisi da analisi

**Rischio**: Si passa più tempo a qualificare che a produrre. Ogni task richiede pre-flight check, OQ, APQ, report, sign-off — il lavoro rallenta fino a bloccarsi.

**Come evitarlo**:
- **Principio CSA**: assurance proporzionale al rischio. Un task di Euterpe (classe bassa) non ha bisogno dello stesso livello di Hermes (classe alta).
- Per task a basso rischio: AOQ si applica solo al membro (non al singolo task).
- Soglie di attivazione: non tutto richiede OQ completo. Solo primo task dopo creazione + task dopo modifiche al prompt + task ad alto rischio.

### 5.3 False confidence

**Rischio**: Un membro qualificato oggi (passa OQ e APQ) viene considerato "affidabile" per sempre. Ma il LLM sottostante cambia, i tool cambiano, i prompt vengono modificati. Il drift è reale e subdolo.

**Come evitarlo**:
- L'ACM non è opzionale — è l'unico modo per rilevare drift.
- OQ e APQ hanno **scadenza**: se un membro non viene monitorato per 30 giorni, perde la qualifica e va ri-qualificato.
- Il deviation rate è la metrica più importante dell'ACM: un trend in aumento è sempre un segnale di allarme, anche se lo score è ancora alto.

### 5.4 Sovraccarico per Hermes

**Rischio**: Hermes è già il collo di bottiglia operativo del team. Aggiungere gates ADQ, AOQ, APQ significa più lavoro per lui.

**Come evitarlo**:
- **Automatizzare tutto ciò che è possibile**:
  - Pre-flight check: script, non manuale
  - Deviation log: compilazione guidata da template, non scrittura libera
  - Report ACM: Dike lo produce, Hermes lo legge in 2 minuti
- **Delegare**: la verifica OQ può essere eseguita dal membro stesso (auto-test) con supervisione di Dike.
- **Soglie di escalation**: Hermes viene coinvolto solo per allarmi (deviation rate > soglia) o decisioni (approvazione ADQ per membri alto rischio). Il resto è operativo e lo gestiscono Dike e i singoli membri.

### 5.5 Rigidità eccessiva

**Rischio**: Processi creativi o esplorativi (brainstorming, ricerca aperta) vengono soffocati da gates e criteri di accettazione.

**Come evitarlo**:
- L'AQF si applica ai **task produttivi**, non a sessioni esplorative. 
- Un task di "ricerca esplorativa" ha criteri AOQ diversi da un task di "produzione report finale". 
- Distinguere sempre: exploration mode (nessun gate) vs. production mode (gate attivi).

---

## 6. Sintesi per Hermes

### In una frase

> L'AQF trasforma il Team Olimpo da un gruppo di agenti che "funzionano" a un sistema di agenti di cui **sai** che funzionano — con evidenze, metriche e capacità di miglioramento continuo.

### Cosa cambia per te (Hermes)

| Oggi | Con AQF |
|------|---------|
| Prima di delegare, confidi che tutto funzioni | Lanci un pre-flight check automatico (2 secondi) |
| Scopri problemi quando l'utente li segnala | Li scopri durante OQ/APQ, prima del rilascio |
| I task bloccati restano in stallo finché non li vedi | ACM ti notifica trend e deviazioni |
| Decidi "a naso" se un membro sta performando bene | Hai metriche oggettive (deviation rate, quality score) |
| Ogni nuovo membro è un salto nel buio | ADQ + APQ ti danno confidenza prima del rilascio |

### Le 3 cose da fare DOMANI

1. **Assegna classe di rischio** ai membri esistenti (10 minuti)
2. **Aggiungi deviation log** al template handoff (30 minuti con Dike)
3. **Template ADQ** per il prossimo nuovo membro (20 minuti con Atena)

Il resto viene dopo, gradualmente, senza fretta. L'AQF è un investimento, non un peso.

---

*Documento generato da Metis — Thinking Partner & Stratega del Team Olimpo*
*Basato su input di Proteo (ricerca IQ/OQ/PQ/CSA) e Dike (mappatura processi e gap analysis)*
*In attesa di review e approvazione Hermes*
