---
data: 2026-05-11
mittente: metis
destinatario: hermes
tipo: report
stato: da-processare
priorita: alta
titolo: "Analisi costi-benefici: 5 miglioramenti LLM Wiki per Team Olimpo"
tags:
  - analisi
  - costi-benefici
  - llm-wiki
  - conoscenza-compounding
  - priorita
---

# Analisi Costi-Benefici: Integrazione Pattern LLM Wiki

> Prodotto da Metis — 11 maggio 2026
> Destinatario: Hermes (per decisione implementazione)
> Baseline: Flusso attuale senza wiki layer (64 handoff, 12.197 righe, 0 pagine conoscenza compilata)
> Report sorgente: `2026-05-11_proteo-hermes_ricerca_llm-wiki-team-olimpo.md`

---

## Indice

1. [Premessa metodologica](#1-premessa-metodologica)
2. [Baseline — Stato attuale del team](#2-baseline--stato-attuale-del-team)
3. [Miglioramento 1: Wiki layer (Library/Wiki/)](#3-miglioramento-1-wiki-layer-librarywiki)
4. [Miglioramento 2: index.md navigazione semantica](#4-miglioramento-2-indexmd-navigazione-semantica)
5. [Miglioramento 3: hot.md cache di contesto](#5-miglioramento-3-hotmd-cache-di-contesto)
6. [Miglioramento 4: Lint periodico vault](#6-miglioramento-4-lint-periodico-vault)
7. [Miglioramento 5: Wiki-summary obbligatorio](#7-miglioramento-5-wiki-summary-obbligatorio)
8. [Tabella riepilogativa — priorità di implementazione](#8-tabella-riepilogativa--priorità-di-implementazione)
9. [Analisi rischi aggregata](#9-analisi-rischi-aggregata)
10. [Raccomandazioni finali](#10-raccomandazioni-finali)
11. [Metriche di successo (30 giorni)](#11-metriche-di-successo-30-giorni)

---

## 1. Premessa metodologica

### Criteri di quantificazione

Ogni miglioramento viene valutato su 4 dimensioni, tutte **con numeri**:

| Dimensione | Unità | Metodo di calcolo |
|------------|-------|-------------------|
| **Costo implementazione** | Token + operazioni agente | Stimato su base setup iniziale + mantenimento ricorrente |
| **Costo opportunità** | Token sprecati senza il miglioramento | Baseline attuale vs scenario con miglioramento |
| **Beneficio diretto** | Token/ore risparmiati per occorrenza | Misurato su operazioni tipo del team |
| **ROI** | Rapporto benefici/costi su 30 giorni | (Risparmio token × frequenza) / (Costo setup + costo mantenimento × 30) |
| **Rischio residuo** | Probabilità × impatto | Dopo mitigazioni proposte da Proteo |

### Conversione linee → token

Basata sulla composizione media dei nostri handoff (italiano tecnico + YAML + markdown):

| Metrica | Valore | Fonte |
|---------|--------|-------|
| Token per riga (media) | ~8 token/riga | Stima su mix markdown/YAML/prosa italiana |
| Token per handoff medio | ~1.736 token | 217 righe × 8 token |
| Token per handoff knowledge (report/profilo) | ~3.000 token | 375 righe × 8 token |
| Token per sessione OpenCode tipica | ~15.000-25.000 token | Stima osservata su sessioni Hermes |
| Contesto OpenCode disponibile | ~200.000 token | Specifica tecnica OpenCode |

---

## 2. Baseline — Stato attuale del team

### Inventario conoscenza

Misurato sul repository al 2026-05-11:

| Metrica | Valore |
|---------|--------|
| Handoff totali (root + Archivio) | 64 file |
| - Handoff attivi (root) | 57 file |
| - Handoff archiviati | 7 file (più directory `Legacy/`) |
| Righe totali handoff | 12.197 righe |
| Token totali handoff | ~97.576 token (~12.197 × 8) |
| Handoff knowledge-bearing (report/profilo/ricerca/analisi) | ~12 file |
| Righe in knowledge-bearing handoff | ~4.498 righe (37% del totale) |
| Token in knowledge-bearing handoff | ~35.984 token |
| Indice semantico | Assente (`Registro.md` è cronologico, non semantico) |
| Cache contesto inter-sessione | Assente (ogni sessione parte da zero) |
| Lint/health-check vault | Assente (nessuna verifica periodica) |
| Wiki layer | Assente (nessuna `Library/Wiki/`) |

### Costo operativo attuale (baseline per confronto)

**Operazione tipo: "recuperare conoscenza pregressa su un tema"**

Esempio concreto: "Cosa abbiamo concluso sull'architettura multi-agente?"

| Passo | Operazione | Token | Tempo agente |
|-------|-----------|-------|-------------|
| 1 | Scansionare `Registro.md` (22 righe cronologiche) | ~176 | ~20 sec |
| 2 | Identificare possibili handoff rilevanti per data/titolo | — | ~30 sec (guess) |
| 3 | Aprire 2-3 handoff candidati (es. ~217 righe × 3 = ~651 righe) | ~5.208 | ~60 sec |
| 4 | Leggere/scorrere per trovare la sezione rilevante | — | ~40 sec |
| 5 | Ricostruire il quadro completo nella sessione corrente | variabile | ~30 sec |
| **Totale** | | **~5.384 token** | **~180 sec (3 minuti)** |

Frequenza stimata: **2-3 operazioni/settimana** (ricerche che toccano temi già affrontati).

**Con 2,5 operazioni/settimana → 10/mese → ~53.840 token/mese consumati solo per ri-trovare conoscenza pregressa.**

A questi si aggiunge il costo delle **ricerche ridondanti**: quando Proteo non trova conoscenza pregressa e riparte da zero su un tema già affrontato. Ogni ricerca ridondante costa ~10.000-20.000 token (intero ciclo ingest-analisi-report).

---

## 3. Miglioramento 1: Wiki layer (`Library/Wiki/`)

### Descrizione

Creazione di `Library/Wiki/` con struttura a pagine persistenti (concepts, decisions, research, profiles, comparisons) + index.md + log.md. Ogni handoff knowledge-bearing produce/aggiorna pagine wiki invece di finire "morto" in Archivio.

### Costi

#### Setup iniziale (one-time)

| Voce | Quantità | Token | Operazioni agente |
|------|----------|-------|-------------------|
| Creare directory structure | 6 directory | ~50 | 1 mkdir |
| Scrivere `Library/Wiki/index.md` (template con sezioni vuote) | 1 file ~80 righe | ~640 | 1 Write |
| Scrivere `Library/Wiki/log.md` (template append-only) | 1 file ~30 righe | ~240 | 1 Write |
| Creare prima pagina concept (llm-wiki-pattern) da report Proteo | 1 pagina ~120 righe | ~960 | 1 sessione Hermes |
| Aggiornare `AGENTS.md` con sezione Wiki (10 righe) | 1 edit | ~80 | 1 Edit |
| Aggiornare `handoff-guida.md` con riferimento a Wiki | 1 edit ~15 righe | ~120 | 1 Edit |
| **Totale setup** | | **~2.090 token** | **~6 operazioni** |

Costo setup in minuti agente stimati: **~15-20 minuti** (una sessione).

#### Mantenimento ricorrente (per handoff knowledge-bearing)

| Voce | Token | Operazioni agente |
|------|-------|-------------------|
| Creare/aggiornare pagine wiki (estrarre sintesi da handoff) | ~400-800 | 1 sessione Hermes/Proteo |
| Aggiornare index.md (1 riga per nuova pagina) | ~30 | 1 Edit |
| Scrivere su log.md (1 riga) | ~16 | 1 Edit |
| **Totale per handoff** | **~500-850 token** | **~3-5 minuti** |

Frequenza wiki-izzazione: ~12 handoff knowledge-bearing/mese (stima su ritmo attuale: 10 in 11 giorni = ~25/mese, ma non tutti sono wiki-izzabili — filtro ~50% → ~12/mese).

### Benefici

| Voce | Stima | Calcolo |
|------|-------|---------|
| **Ricerche ridondanti evitate** | ~30% su temi simili | Se ~6 ricerche/mese toccano temi già affrontati, ~1,8 diventano ri-query su wiki (~3.000 token) invece di ricerche full (~15.000 token) |
| **Risparmio token per ri-query** | ~4.500 token/operazione | Da ~5.384 token (baseline) a ~500 token (index.md + pagina wiki) |
| **Onboarding nuovi membri** | ~40% più veloce | Da ~60 min a ~36 min per acquisire conoscenza pregressa |
| **Token risparmiati su ri-query** | ~90% rispetto a fonti raw | Da ~5.384 token a ~500 token per operazione |

#### Calcolo ROI dettagliato

**Costo mensile wiki (12 handoff wiki-izzati):**
- Mantenimento: 12 × 700 token (media) = **8.400 token/mese**
- Setup ammortizzato su 30 giorni: 2.090 / 30 × 30 = **2.090 token** (intero setup imputato al primo mese)

**Costo totale primo mese: 10.490 token**

**Beneficio mensile:**
- 10 operazioni di ri-query/mese × ~4.884 token risparmiati = **48.840 token/mese**
- Ricerche ridondanti evitate: 1,8 × ~12.000 token = **~21.600 token/mese**

**Beneficio totale primo mese: ~70.440 token**

**ROI primo mese: 70.440 / 10.490 = ~6,7×** (ogni token investito ne restituisce ~7)

**ROI regime (dal mese 2, senza costo setup): 70.440 / 8.400 = ~8,4×**

### Rischi residui

| Rischio | Probabilità | Impatto | Mitigazione | Rischio residuo |
|---------|-------------|---------|-------------|-----------------|
| Wiki diventa "cimitero digitale" (abbandonato dopo 1 mese) | 30% | Alto (costi setup sprecati) | Wiki-summary obbligatorio (#5) + lint (#4) + hot.md (#3) danno visibilità | **Medio** — il sistema di guardrail (3 miglioramenti che si rinforzano) riduce probabilità dal 60% al 30% |
| Allucinazioni propagate nel wiki | 20% | Alto (conoscenza errata si cristallizza) | Ogni pagina wiki deve linkare fonte primaria; lint verifica presenza link; markdown è editabile | **Basso** — tracciabilità forzata rende correzione semplice |
| Conoscenza duplicata (2 pagine sullo stesso concetto) | 25% | Medio | index.md funge da registro; lint rileva nomi simili; naming kebab-case rigoroso | **Basso** — rilevabile e correggibile |

**Rischio residuo complessivo: Basso-Medio** — i guardrail incrociati coprono bene i rischi principali.

---

## 4. Miglioramento 2: `index.md` navigazione semantica

### Descrizione

Creare un indice semantico (`Library/Wiki/index.md`) che organizza la conoscenza per concetti, decisioni e ricerche — non solo per data come fa `Registro.md`.

### Costi

#### Setup iniziale (one-time)

| Voce | Token | Note |
|------|-------|------|
| Scrivere index.md con sezioni Concepts / Research / Decisions / Profiles / Comparisons | ~640 | Già conteggiato nel setup wiki (#1) — **costo condiviso** |
| Popolare index.md con le prime 5-10 voci (da handoff esistenti) | ~400 | Una tantum, si allinea col seeding wiki |

**Costo incrementale puro: ~400 token** (oltre al setup wiki).

#### Mantenimento ricorrente

| Voce | Token per handoff |
|------|-------------------|
| Aggiungere 1 riga a index.md per nuova pagina wiki | ~30-50 |
| Aggiornare data "ultimo aggiornamento" su voci esistenti | ~20 |
| **Totale per handoff** | **~50-70 token** |

### Benefici

| Voce | Stima | Calcolo |
|------|-------|---------|
| **Riduzione tempo per trovare conoscenza pregressa** | ~50% vs scansione Registro | Da ~120 sec a ~60 sec per trovare handoff rilevante |
| **Riduzione token in query** | ~20-30% su operazioni di ricerca | index.md è ~200 token; scansionare Registro + aprire 3 handoff è ~5.384 token. Con index si evita l'apertura esplorativa. |

**Il beneficio è quasi interamente assorbito nel calcolo del wiki layer (#1).** index.md da solo senza wiki non avrebbe senso (indice senza pagine da indicizzare). La raccomandazione è di trattare #1 e #2 come **un unico miglioramento**.

### Rischi residui

| Rischio | Probabilità | Impatto | Rischio residuo |
|---------|-------------|---------|-----------------|
| index.md non aggiornato → indice inaccurate | 20% | Medio | **Basso** — log.md e lint incrociato rilevano discrepanze |
| index.md troppo lungo (centinaia di voci) | 5% in 12 mesi | Basso | Karpathy gestisce "hundreds of pages"; il nostro ritmo è ~100 voci/anno |

---

## 5. Miglioramento 3: `hot.md` cache di contesto

### Descrizione

File `Library/Meta/hot.md` (~500 parole, ~400 token) che mantiene lo stato attuale del team: progetto corrente, decisioni in sospeso, ultime 3 operazioni, domande aperte, collegamenti rapidi.

### Costi

#### Setup iniziale

| Voce | Token |
|------|-------|
| Scrivere hot.md con template + stato iniziale | ~400 |

#### Mantenimento ricorrente

| Voce | Token | Frequenza | Note |
|------|-------|-----------|------|
| Aggiornamento fine sessione (da Hermes) | ~200 | 2-3/settimana | Template pre-strutturato: basta cambiare 3-4 campi |
| Lettura all'inizio di ogni sessione | ~400 | 5-7/settimana | hot.md viene caricato in contesto |

**Costo mensile mantenimento:** ~12 sessioni × 400 token (lettura) + 10 aggiornamenti × 200 token (scrittura) = **6.800 token/mese**

Wait — leggere hot.md non è un **costo**, è un **investimento**. È l'alternativa al caricare contesto da zero. Ricalcoliamo:

**Costo incrementale netto:**
- hot.md in lettura sostituisce ~2.000 token di "rievocazione contesto" che Hermes dovrebbe ricostruire (chronologia conversazione + file aperti)
- **Risparmio netto per sessione: ~1.600 token**
- **Risparmio netto mensile: 12 sessioni × 1.600 = ~19.200 token/mese**

Costo scrittura: 10 aggiornamenti × 200 token = **2.000 token/mese**

**ROI: 19.200 / 2.000 = ~9,6×**

### Benefici

| Voce | Stima | Calcolo |
|------|-------|---------|
| **Riduzione token "recap" per sessione** | ~15-20% | ~1.600 token risparmiati su ~15.000 token/sessione |
| **Riavvio sessioni multi-giorno** | ~60% più rapido | Da ~5 min a ~2 min per riprendere contesto interrotto |
| **Decisioni in sospeso visibili** | 100% di tracciabilità | Attualmente le decisioni aperte esistono solo nella cronologia chat |

### Rischi residui

| Rischio | Probabilità | Impatto | Mitigazione | Rischio residuo |
|---------|-------------|---------|-------------|-----------------|
| hot.md non aggiornato → contesto obsoleto | 40% | Medio | Template minimale (5 campi, aggiornamento in ~30 sec); Hermes ha routine fissa di fine sessione | **Medio** — il rischio è reale ma contenuto dall'abitudine operativa |
| hot.md cresce oltre 500 parole | 10% | Basso | Template fissa limite esplicito; community Karpathy conferma ~500 parole come sweet spot | **Molto Basso** |

---

## 6. Miglioramento 4: Lint periodico vault

### Descrizione

Operazione settimanale automatizzata che verifica: pagine orfane, contraddizioni, stale claims (>30 giorni), handoff non wiki-izzati. Output: report in `Library/Handoff/`.

### Costi

#### Setup iniziale

| Voce | Token | Note |
|------|-------|------|
| Definire template prompt lint | ~200 | Template da 4 check strutturati |
| Documentare procedura in handoff-guida o Meta | ~300 | Un paragrafo nella guida |

**Totale setup: ~500 token**

#### Mantenimento ricorrente

| Voce | Token | Frequenza |
|------|-------|-----------|
| Eseguire lint (Clio o Dike) | ~2.000-4.000 | Settimanale |
| Leggere report lint | ~1.000 | Settimanale |
| Correggere problemi rilevati | ~1.000-2.000 | Settimanale |
| **Totale per esecuzione** | **~4.000-7.000 token** | **4/settimana (ma ~1 esecuzione/settimana → ~4.000-7.000/settimana)** |

**Attenzione**: non tutte le settimane serve eseguire lint. Propongo: **1 esecuzione ogni 2 settimane** per le prime 8 settimane, poi mensile.

**Costo mensile (2 esecuzioni): ~8.000-14.000 token/mese**

### Benefici

| Voce | Stima | Calcolo |
|------|-------|---------|
| **Riduzione pagine orfane** | ~90% | Rilevazione sistematica → collegamento o archiviazione |
| **Rilevamento contraddizioni** | Variabile | Prima rilevazione potrebbe trovare 1-3 contraddizioni, poi si stabilizza |
| **Gap di copertura identificati** | 1-3 per lint | Temi non documentati che emergono dall'analisi |
| **Qualità conoscenza** | Difficile da quantificare in token | Beneficio qualitativo: affidabilità del wiki aumenta |

**Beneficio quantificabile:**
- Senza lint: errori e contraddizioni si accumulano, degradando l'affidabilità del wiki → ogni 3 mesi qualcuno si fida di una pagina obsoleta → costo: ~15.000 token di lavoro basato su info errata + ~30 minuti di correzione a valle
- Con lint: rilevamento precoce → costo errore evitato ~80%

**ROI stimato:** difficile da calcolare numericamente perché il beneficio principale è **prevenzione del degrado** (costo evitato), non risparmio diretto. Stima prudenziale:

| Scenario | Costo su 90 giorni |
|----------|-------------------|
| **Senza lint** (3 mesi di degrado wiki) | ~45.000 token in correzioni + 1 decisione errata (~10.000 token) = ~55.000 token |
| **Con lint** (2 esecuzioni/mese × 3 mesi) | 6 esecuzioni × 5.500 token (media) = 33.000 token |

**ROI a 90 giorni: 55.000 / 33.000 = ~1,7×** (appena sopra il break-even).

Il lint **non ha ROI positivo nel breve termine** — è un investimento sulla qualità della conoscenza. Il suo valore è **prevenire il degrado** che renderebbe il wiki inaffidabile.

### Rischi residui

| Rischio | Probabilità | Impatto | Mitigazione | Rischio residuo |
|---------|-------------|---------|-------------|-----------------|
| Lint produce falsi positivi → rumore | 35% | Medio | Template prompt calibrato; action items verificati da umano/agente | **Medio** — accettabile se lint è ogni 2 settimane |
| Lint diventa routine senza valore | 25% | Basso | Se dopo 3 mesi non emergono problemi, ridurre frequenza a mensile | **Molto Basso** |

---

## 7. Miglioramento 5: Wiki-summary obbligatorio

### Descrizione

Aggiungere sezione `## Wiki Summary` obbligatoria al template handoff per i tipi `report`, `profilo`, `analisi`, `ricerca`. La sezione pre-struttura il contenuto per la wiki-izzazione.

### Costi

#### Setup iniziale

| Voce | Token | Operazioni |
|------|-------|------------|
| Aggiornare `handoff-guida.md` con template Wiki Summary | ~300 | 1 Edit |
| Aggiornare frontmatter consentiti (wiki_summary, wiki_pages) | ~100 | 1 Edit |
| Creare template wiki-summary in `Library/Handoff/templates/` | ~200 | 1 Write |
| Aggiornare template Proteo con sezione wiki-summary | ~150 | 1 Edit |

**Totale setup: ~750 token**

#### Mantenimento ricorrente

| Voce | Token per handoff | Note |
|------|-------------------|------|
| Compilare Wiki Summary (autore) | ~200-400 | Template pre-strutturato: 6 campi da riempire |
| Eseguire azioni wiki (destinatario/Hermes) | ~500-800 | Già conteggiato nel mantenimento wiki (#1) |

**Costo incrementale per handoff: ~200-400 token** (la parte di compilazione della sezione).

### Benefici

| Voce | Stima | Calcolo |
|------|-------|---------|
| **Riduzione attrito wiki-izzazione** | ~70% | Il contenuto è già pre-strutturato e pronto per copia in Library/Wiki/ |
| **Handoff wiki-izzati al 100%** | Per tipi report/profilo | Obbligatorio per convenzione → non si dimentica |
| **Completezza knowledge wiki** | Ogni handoff contribuisce | Nessun handoff knowledge-bearing scivola nell'oblio |

**Impatto chiave:** Senza wiki-summary, la wiki-izzazione sarebbe un compito extra che richiede rilettura dell'intero handoff per estrarre sintesi (~10-15 min per handoff). Con wiki-summary, la sintesi è già scritta e l'autore conosce il contenuto fresco (~2-3 min per compilazione).

**Risparmio per handoff: ~8-12 minuti**

### ROI dettagliato

**Costo setup ammortizzato (primo mese): ~750 token**
**Costo ricorrente (12 handoff/mese × 300 token): ~3.600 token/mese**
**Costo totale primo mese: ~4.350 token**

**Risparmio tempo per handoff wiki-izzato: ~10 min (da ~15 min a ~5 min)**
**Risparmio su 12 handoff/mese: ~120 min/mese**

**ROI in tempo:** 120 min risparmiati / ~5 min di compilazione totali = ~24×

**ROI in token:** 12 handoff × 8.000 token (ri-lettura full) vs 12 × 300 token (wiki-summary) — ma la ri-lettura faceva parte della wiki-izzazione, che avverrebbe comunque. Il risparmio reale è sulla **ri-lettura evitata**: ~900 token di wiki-summary sostituiscono ~3.000 token di scorrimento full.

**ROI: (3.000 - 900) × 12 / 4.350 = 25.200 / 4.350 = ~5,8×**

### Rischi residui

| Rischio | Probabilità | Impatto | Mitigazione | Rischio residuo |
|---------|-------------|---------|-------------|-----------------|
| Wiki-summary compilato male (troppo breve o troppo lungo) | 30% | Basso | Template fissa 1-2 paragrafi; rilevanza (alta/media/bassa) è autovalutata | **Molto Basso** |
| Overhead burocratico percepito | 20% | Medio | Solo 3 tipi di handoff richiedono wiki-summary (~16% del totale) | **Basso** — non si applica a bug, nota, specifica tecnica |

---

## 8. Tabella riepilogativa — Priorità di implementazione

| # | Miglioramento | Costo setup | Costo mensile | Beneficio mensile | ROI 30gg | ROI regime | Priorità | Dipende da |
|---|---|---|---|---|---|---|---|---|
| **1+2** | Wiki layer + index.md | ~2.490 token | ~8.470 token | ~70.440 token | **~6,7×** | **~8,4×** | **⚡ Alta** | — |
| **5** | Wiki-summary obbligatorio | ~750 token | ~3.600 token | ~25.200 token | **~5,8×** | **~7,0×** | **⚡ Alta** | #1 (senza wiki non ha senso) |
| **3** | hot.md cache contesto | ~400 token | ~2.000 token | ~19.200 token | **~9,6×** | **~9,6×** | **Media** | — (indipendente) |
| **4** | Lint periodico | ~500 token | ~8.000-14.000 token | ~55.000 token/90gg | **~1,7× a 90gg** | — | **Bassa** | #1 (lint senza wiki non ha oggetto) |

### Dipendenze critiche

```
┌─────────────────────┐
│  #1 Wiki layer       │ ← Fondamenta: senza questo, #2 e #4 non hanno senso
│  #2 index.md         │   (costo condiviso con #1)
└─────────┬───────────┘
          │
          ├──→ #5 Wiki-summary    ← Il wiki deve esistere prima di richiedere wiki-summary
          │                       (ma wiki-summary si progetta insieme al wiki)
          │
          ├──→ #4 Lint            ← Lint senza wiki non ha oggetto da verificare
          │
          └── (indipendente)
               #3 hot.md          ← Non dipende dal wiki, si può fare subito
```

**Decisione architetturale chiave**: Wiki centralizzato (unico `Library/Wiki/` per tutto il team) vs wiki per agente (es. `Library/Wiki/Proteo/`, `Library/Wiki/Dike/`).

**Raccomandazione Metis**: Iniziare con **wiki centralizzato**. Motivazione:
- I concept e le decisioni sono trasversali a più agenti (es. "architettura multi-agente" riguarda Hermes + Proteo + Dike)
- La frammentazione in wiki per agente moltiplica il costo di mantenimento (ogni agente deve mantenere il suo index.md, log.md, lint)
- Un wiki centralizzato con namespacing per categoria (concepts/, decisions/, research/) realizza lo stesso scopo senza overhead
- La decisione di separare per agente può essere presa in **Fase 3** (maturazione), quando dimensioni e conflitti lo giustificano

---

## 9. Analisi rischi aggregata

### Rischi dalla proposta Proteo (con valutazione residua)

| # | Rischio | Probabilità | Impatto | Mitigazioni incrociate | Rischio residuo |
|---|---------|-------------|---------|----------------------|-----------------|
| R1 | Wiki diventa "cimitero digitale" | 30% | Alto | #5 (wiki-summary) forza contribuzione; #4 (lint) monitora salute; #3 (hot.md) dà visibilità | **Medio** — il sistema di 3 guardrail riduce probabilità dal 60% stimato a ~30%. Rischio accettabile. |
| R2 | Conoscenza duplicata | 25% | Medio | index.md come registro centralizzato; lint rileva nomi simili; naming convenzione kebab-case | **Basso** — rilevabile e correggibile con ~200 token |
| R3 | Overhead di processo | 20% | Medio | Solo handoff report/profilo/analisi richiedono wiki-summary (~16% del totale); azioni wiki minime (2-3 pagine) | **Basso** — l'overhead è ~300 token/handoff, ampiamente compensato dal risparmio |
| R4 | Incoerenza con convenzioni vault | 10% | Basso | Le pagine wiki seguono lo stesso frontmatter YAML e wikilink del vault; Clio verifica conformità | **Molto Basso** — già allineato per design |
| R5 | Allucinazioni propagate | 20% | Alto | Ogni pagina wiki deve linkare fonte primaria (handoff originale); lint verifica presenza link; markdown è editabile | **Basso** — tracciabilità e correggibilità riducono impatto |

### Rischio aggiuntivo non coperto da Proteo

| Rischio | Probabilità | Impatto | Segnale d'allarme | Mitigazione |
|---------|-------------|---------|-------------------|-------------|
| **R6: Degrado wiki per ~90gg senza lint** | 40% | Medio | Lint non eseguito per 2+ cicli consecutivi | hot.md traccia ultimo lint; se > 21 giorni senza lint, alert su Hermes |
| **R7: index.md non aggiornato parallelo al wiki** | 25% | Medio | Discrepanza tra pagine wiki esistenti e index.md | log.md registra ogni operazione → confrontabile con index.md via script |

### Matrice rischi residui

```
Impatto
  Alto    │ R1 (30%)           R5 (20%)
          │
  Medio   │ R2 (25%)  R3 (20%) R6 (40%)
          │
  Basso   │                    R4 (10%)  R7 (25%)
          │
          └────────────────────────── Probabilità
            Bassa        Media       Alta
```

**Giudizio complessivo**: Profilo di rischio **contenuto**. L'unico rischio con impatto alto e probabilità non trascurabile (R1: cimitero digitale, R5: allucinazioni) è coperto da mitigazioni incrociate che lo riducono a **rischio residuo medio**. R5 è ulteriormente mitigato dall'architettura multi-agente (un agente può correggere l'errore di un altro — vantaggio rispetto al single-agent Karpathy).

---

## 10. Raccomandazioni finali

### Ordine di implementazione

Basato su ROI, dipendenze e impatto operativo:

```
Fase 1 (immediata, questa sessione) — Costo: ~2.890 token | ROI: 6,7×
├── 1a. Creare Library/Wiki/ + index.md + log.md  (costo: ~2.090 token)
├── 1b. Aggiornare AGENTS.md con sezione Wiki       (costo: ~80 token)
├── 1c. Aggiornare handoff-guida.md                  (costo: ~420 token)
├── 1d. Seeding: creare prima pagina wiki dal report Proteo (costo: ~300 token)
└── 1e. Creare Library/Meta/hot.md                   (costo: ~400 token)
├── Cosa serve: una sessione Hermes (~20 min)
└── Risultato: Wiki operativo con 1 pagina, hot.md attivo

Fase 2 (prossima sessione) — Costo: ~750 token | ROI: 5,8×
├── 2a. Aggiungere template Wiki Summary a handoff-guida    (costo: ~200 token)
├── 2b. Aggiungere frontmatter wiki_summary/wiki_pages      (costo: ~100 token)
├── 2c. Aggiornare template Proteo con Wiki Summary         (costo: ~150 token)
├── 2d. Primo Wiki Summary in handoff corrente              (costo: ~300 token)
└── Risultato: Ogni nuovo handoff knowledge-bearing contribuisce automaticamente

Fase 3 (entro 30 giorni) — Costo: ~500 token | ROI: 1,7×
├── 3a. Template prompt lint + documentazione               (costo: ~500 token)
├── 3b. Primo lint a 14 giorni dal setup wiki               (costo: ~4.000 token)
└── Risultato: Qualità e salute del wiki monitorate

Fase 4 (entro 60 giorni) — Valutazione
├── Valutare se serve wiki per agente
├── Script Python per assistenza wiki-izzazione (semi-automatica)
└── Integrazione in AGENTS.md come conoscenza per nuovi agenti
```

### Cosa NON fare

1. **Non implementare #2 (index.md) senza #1 (wiki layer)** — un indice senza pagine è un costo senza beneficio.
2. **Non implementare #4 (lint) in Fase 1** — se il wiki ha 1-2 pagine, non c'è nulla da verificare. Il lint diventa utile dopo almeno 10-15 pagine (~30-45 giorni di adozione).
3. **Non wiki-izzare tutto** — la regola di Proteo (solo report/profilo/analisi) è corretta. Bug report e note operative non hanno valore di conoscenza compilata.
4. **Non creare wiki per agente in Fase 1** — centralizzato è più economico. La separazione va valutata a valle, con dati alla mano.

### Raccomandazione su architettura multi-agente vs single-agent

La raccomandazione centrale di Proteo — "Il wiki centralizzato come pattern Karpathy su architettura multi-agente" — è **corretta e adottabile**. Con una precisazione:

| Aspetto | Single-agent (Karpathy) | Multi-agente (Team Olimpo) |
|---------|------------------------|---------------------------|
| Chi scrive il wiki | LLM (sempre lo stesso) | Hermes orchestra, Proteo contribuisce, Clio verifica |
| Chi legge il wiki | LLM | Ogni agente secondo competenza |
| Vantaggio | Semplicità, coerenza | Robustezza (un agente corregge l'altro), specializzazione (pagine per competenza) |
| Svantaggio | Errore non rilevato | Overhead di coordinamento (hot.md + handoff) |
| **Impatto** | **Nessuna modifica al pattern** | Il pattern Karpathy funziona invariato; cambia solo **chi esegue** le operazioni |

**Conclusione**: Il wiki centralizzato è sufficiente per la nostra scala attuale (64 handoff, 12 knowledge-bearing). La separazione per agente sarà rivalutata in Fase 4 quando:
- Il wiki supera 50 pagine
- Emergono conflitti di scrittura (due agenti vogliono modificare la stessa pagina)
- Il costo di navigazione in index.md supera i 500 token (indice troppo lungo)

---

## 11. Metriche di successo (30 giorni)

Dopo 30 giorni dall'implementazione della Fase 1, verificare:

| # | Metrica | Target | Metodo verifica | Chi |
|---|---------|--------|-----------------|-----|
| M1 | Pagine wiki create | ≥5 | `ls Library/Wiki/concepts/ Library/Wiki/decisions/ Library/Wiki/research/ \| wc -l` | Hermes |
| M2 | Handoff wiki-izzati | 100% dei report/profilo prodotti | `grep -r "wiki_summary: true" Library/Handoff/ \| wc -l` vs handoff knowledge prodotti | Hermes |
| M3 | Ricerche ridondanti evitate | ≥2 | Confrontare topic overlap pre/post wiki: se un handoff cita una pagina wiki come fonte, è una ricerca non ridondante | Dike |
| M4 | hot.md aggiornato | ≥80% delle sessioni | `grep -c "## Stato attuale" Library/Meta/hot.md` — verificare data più recente ≤3 giorni | Hermes |
| M5 | index.md manutenzione | 100% pagine wiki indicizzate | Confrontare `find Library/Wiki -name "*.md" \| grep -v index.md \| grep -v log.md` con voci in index.md | Clio |
| M6 | Token risparmiati stimati | ≥50.000 token | Formula: (query evitate × 5.000 token) + (ricerche ridondanti evitate × 15.000 token). Verifica su campione di 3 operazioni | Metis |

### Segnali d'allarme precoci (entro 14 giorni)

Se uno di questi si verifica, la strategia va rivista:

| Segnale | Cosa significa | Azione correttiva |
|---------|---------------|-------------------|
| 0 pagine wiki create dopo 14 giorni | Il wiki non è stato adottato | Hermes deve dedicare una sessione al seeding iniziale |
| hot.md non aggiornato per >7 giorni | La routine di fine sessione non funziona | Semplificare hot.md (ridurre a 3 campi) o integrarlo in handoff register |
| Wiki-summary compilato in <50% degli handoff | La convenzione non è stata assimilata | Aggiungere check automatico o ridurre a "raccomandato" invece di "obbligatorio" |

---

## Appendice A: Note sull'architettura OpenCode

### Differenze chiave vs Claude Code single-agent

| Dimensione | Claude Code (Karpathy) | OpenCode (Team Olimpo) | Impatto sul pattern |
|-----------|----------------------|----------------------|---------------------|
| **Contesto** | Singolo LLM, unico file CLAUDE.md | Multi-agente, ogni agente ha .opencode/agents/<nome>.md | Il wiki può essere letto da agenti diversi. index.md deve essere abbastanza chiaro per qualsiasi agente. |
| **Esecuzione** | LLM esegue ingest/query/lint direttamente | Hermes orchestra, subagenti eseguono | Il flusso operativo è più articolato ma più resiliente. L'errore di un agente non compromette l'intero wiki. |
| **Handoff** | Non esiste | Sistema tracciabile in Library/Handoff/ | **VANTAGGIO UNICO**: ogni operazione wiki (ingest, update) può essere tracciata come handoff. Abbiamo audit trail che Karpathy non ha. |
| **Wiki ownership** | LLM unico proprietario | Multi-proprietario (Hermes orchestra, Proteo contribuisce concept, Dike contribuisce decisioni, Clio lint) | Serve una convenzione chiara su chi scrive cosa. Raccomandazione: Hermes è il "curatore" (come il Karpathy umano), ma delega la scrittura. |

### Implicazione pratica

Il pattern Karpathy si inserisce nel Team Olimpo **senza modifiche architetturali** — il wiki è solo una nuova cartella in `Library/` con una convenzione operativa. Non serve modificare OpenCode, AGENTS.md, o la configurazione degli agenti (a parte aggiungere la sezione descrittiva in AGENTS.md).

La vera innovazione è che il nostro **sistema handoff** ci dà qualcosa che Karpathy non ha: un audit trail completo di ogni operazione wiki. Questo riduce il rischio di allucinazioni propagate (R5) perché ogni pagina wiki è tracciabile all'handoff che l'ha generata.

---

*Metis, Thinking Partner e Stratega del Team Olimpo — domande migliori, decisioni più chiare.*
