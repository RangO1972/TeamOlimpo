---
title: "Mappatura Processi Team Olimpo — Gap Analysis per Framework di Qualifica"
date: 2026-05-16
author: Dike
tags: [processi, gap-analysis, iq-oq-pq, workflow]
status: completato
---

# Mappatura Processi Team Olimpo — Gap Analysis

> [!note] Scopo
> Questo documento mappa i principali flussi operativi del Team Olimpo e identifica i gap rispetto a un framework di qualifica ispirato a IQ/OQ/PQ farmaceutico.

---

## Premessa: il framework IQ/OQ/PQ trasferito

Nel contesto farmaceutico:
- **IQ (Installation Qualification)**: verifica che l'ambiente e gli strumenti siano installati correttamente
- **OQ (Operational Qualification)**: verifica che i processi operino come specificato
- **PQ (Performance Qualification)**: verifica che i processi producano risultati consistenti nel tempo
- **CPV (Continued Process Verification)**: monitoraggio continuo post-qualifica

Applicato a un sistema agentico:
- **IQ**: validazione dell'ambiente (tool, permessi, configurazione) prima di ogni task
- **OQ**: validazione del processo (criteri di accettazione, gate, verifiche)
- **PQ**: validazione dell'output (metriche, qualità, consistenza)
- **CPV**: monitoraggio continuo (trend, anomalie, miglioramento)

---

## 1. Flusso Creazione Nuovo Membro

### Descrizione sintetica

Il flusso trasforma una richiesta utente in un membro operativo del team. Segue uno schema 8-step: richiesta utente → brief Hermes → ricerca Proteo → valutazione (Grok) → profilo Atena → valutazione (Grok) → creazione file agente → verifica conformità Clio → operativo.

### Diagramma testuale

```
Utente → Hermes → Brief (Fucina)
          ↓
        Proteo → Ricerca (Fucina)
          ↓
        Grok → Valutazione ricerca
          ↓
        Atena → Profilo (Fucina)
          ↓
        Grok → Valutazione profilo
          ↓
        Atena → File Agente (.opencode/agents/)
          ↓
        Clio → Verifica conformità OpenCode
          ↓
        Membro operativo
```

### Gap Analysis

| # | Cosa manca | Impatto | Priorità |
|---|------------|---------|----------|
| 1 | Nessun protocollo di validazione IQ per l'ambiente prima della ricerca Proteo (es. verifica che il tool LLM sia funzionante, permessi sufficienti) | Se il tool è giù o mal configurato, il processo perde tempo prima di fallire | Media |
| 2 | Criteri di accettazione non definiti esplicitamente per la "ricerca" di Proteo — cosa significa "buona ricerca"? | Qualità inconsistente, dipendente dal giudizio umano | Alta |
| 3 | Gate di valutazione Grok non ha criteri quantitativi — solo giudizio qualitativo | Soggettività, rischio di accettare output subottimali | Alta |
| 4 | Nessuna PQ post-creazione: il membro viene creato ma non c'è monitoraggio delle performance nelle prime settimane | Non si rilevano problemi di integrazione fino a quando non emergono in produzione | Media |
| 5 | Nessuna CPV: nessun tracciamento delle metriche operative del nuovo membro (task completati, errori, feedback) | Impossibile identificare trend di degrado o miglioramento | Alta |
| 6 | Deviazioni non tracciate: se uno step viene rifatto (v2), non si documenta il "perché" della deviazione dal flusso standard | Perdita di conoscenza, rischio di ripetere errori | Media |

---

## 2. Flusso Ricerca/Analisi (delega a Proteo)

### Descrizione sintetica

Hermes riceve una richiesta dell'utente, la interpreta e delega a Proteo per ricerca/analisi. Proteo produce un output che viene restituito all'utente. Il flusso non è formalizzato come guida dedicata ma è descritto nello scratchpad e nelle convenzioni.

### Diagramma testuale

```
Richiesta utente
      ↓
Hermes → Interpretazione + brief
      ↓
Proteo → Ricerca web/sources + analisi
      ↓
Handoff report a Hermes
      ↓
Hermes → Sintesi/restituzione utente
```

### Gap Analysis

| # | Cosa manca | Impatto | Priorità |
|---|------------|---------|----------|
| 1 | Nessun protocollo IQ: prima di delegare a Proteo, non si verifica che il tool di ricerca sia funzionante | Possibili fallimenti a metà processo | Media |
| 2 | Criteri di accettazione OQ non definiti: quando la ricerca di Proteo è "sufficiente"? | Output di qualità variabile | Alta |
| 3 | Nessun gate di validazione tra output Proteo e consegna utente — Hermes non verifica l'output prima di restituirlo | Rischio di consegnare informazioni errate o incomplete | Alta |
| 4 | Nessuna PQ: non si misura la qualità della ricerca (precisione, completezza, fonti) | Non si identifica il deterioramento della qualità | Media |
| 5 | Nessuna CPV: non si tracciano metriche come tempo di ricerca, tasso di successo, feedback utente | Impossibile ottimizzare il processo | Alta |
| 6 | Flusso non formalizzato in guida dedicata — solo accenni nello scratchpad | Difficoltà di onboarding, inconsistenza | Bassa |

---

## 3. Flusso Conversione PDF

### Descrizione sintetica

Un PDF viene depositato in Team/Inbox/, Efesto/Clio esegue la conversione tramite il tool `pdf_converter`, il Markdown risultante viene depositato in Library/documents/ con le immagini in Library/assets/images/.

### Diagramma testuale

```
PDF → Team/Inbox/
        ↓
pdf_converter convert "file.pdf"
        ↓
[1] extract_metadata()
[2] convert_pdf() → Markdown + immagini
[3] post_process() → pulizia + frontmatter
[4] index_document() → SQLite
        ↓
Library/documents/<slug>.md
Library/assets/images/<slug>/
```

### Gap Analysis

| # | Cosa manca | Impatto | Priorità |
|---|------------|---------|----------|
| 1 | IQ parziale: il tool verifica la presenza delle dipendenze all'avvio, ma non valida l'ambiente (es. permessi di scrittura su Library/, spazio disco) | Fallimenti durante la conversione, file corrotti | Media |
| 2 | OQ parziale: esiste una checklist di output atteso (frontmatter valido, path immagini relativi) ma non è automatizzata — richiede ispezione manuale | Errori non rilevati prima della consegna | Media |
| 3 | Nessun gate strutturato: la conversione termina senza verifica formale che l'output sia corretto | Documenti mal formattati entrano nel vault | Alta |
| 4 | PQ limitata: nessuna metrica sulla qualità della conversione (es. tasso di errori, qualità dell'estrazione) | Non si identifica il deterioramento del tool | Media |
| 5 | CPV assente: non si monitorano nel tempo errori ricorrenti, formati problematici, trend | Non si interviene proattivamente | Alta |
| 6 | Deviazioni non tracciate: se una conversione fallisce, il log c'è ma non viene analizzato strutturalmente | Stessi errori si ripetono | Media |

---

## 4. Flusso Handoff tra Membri

### Descrizione sintetica

Sistema di comunicazione asincrona basato su file Markdown con frontmatter YAML. Ogni handoff ha un mittente, un destinatario, un tipo (profilo, specifica, bug, report, test, nota), uno stato (da-processare, in-corso, completato, bloccato), e una priorità.

### Diagramma testuale

```
Mittente → Crea file handoff (YYYY-MM-DD_mittente-destinatario_tipo_slug.md)
            ↓
          Notifica destinatario (manuale)
            ↓
Destinatario → Legge, aggiorna stato a "in-corso"
            ↓
          Lavora → Aggiorna frontmatter + corpo
            ↓
          Completa → Aggiorna stato a "completato" + note_completamento
            ↓
handoff_register sync → Aggiorna Registro.md
```

### Gap Analysis

| # | Cosa manca | Impatto | Priorità |
|---|------------|---------|----------|
| 1 | IQ assente: non si valida che il file handoff sia ben formato prima di notificare il destinatario | Handoff illegibili o incompleti causano confusione | Alta |
| 2 | OQ limitato: i criteri di "completato" sono nel campo `note_completamento` ma non sono standardizzati — ogni membro scrive come vuole | Difficoltà di valutazione, inconsistenza | Media |
| 3 | Gate di accettazione debole: lo stato "completato" viene impostato dal destinatario stesso senza validazione esterna | Output di qualità variabile accettati come "completati" | Alta |
| 4 | PQ assente: non si misura il tempo di completamento medio per tipo di handoff, tasso di blocchi, qualità percepita | Non si identificano colli di bottiglia | Media |
| 5 | CPV assente: non si monitorano nel tempo i pattern di handoff (es. aumento di bug report, tempo di risposta) | Non si interviene su trend problematici | Media |
| 6 | Deviazioni non tracciate: se un handoff viene abbandonato (stato "bloccato" > 30 giorni), non si fa root-cause analysis | Problemi sistemici non risolti | Media |

---

## 5. Flusso Verifica Conformità Vault (Clio)

### Descrizione sintetica

Clio verifica che i documenti rispettino le convenzioni del vault Obsidian (frontmatter, tags, naming, struttura). Viene invocato dopo eventi specifici (creazione membro, verifica batch KBA, integrazione email).

### Diagramma testuale

```
Trigger (Hermes o auto)
        ↓
Clio → Legge documento/i da verificare
        ↓
Verifica rispetto a convenzioni vault (checklist)
        ↓
[Se OK] → Report positivo
[Se FAIL] → Report problemi + correzioni richieste
        ↓
Hermes → Notifica autore correzioni
```

### Gap Analysis

| # | Cosa manca | Impatto | Priorità |
|---|------------|---------|----------|
| 1 | IQ parziale: Clio verifica le convenzioni ma non valida l'ambiente (es. il vault è accessibile, le cartelle esistono) | Verifica in ambiente non pronto | Bassa |
| 2 | OQ debole: la checklist è applicata ma non ha criteri quantitativi — Clio usa giudizio qualitativo | Inconsistenza nelle valutazioni | Media |
| 3 | Gate disaccoppiato: la verifica di Clio è post-hoc — il documento è già stato creato, la correzione è successiva | rework, inefficienza | Media |
| 4 | PQ assente: non si misura il tasso di fallimento delle verifiche, i problemi più comuni | Non si migliorano le convenzioni proattivamente | Media |
| 5 | CPV assente: non si tracciano nel tempo i pattern di violazione (es. aumento di errori di frontmatter dopo certe modifiche) | Non si identificano cause radice | Alta |
| 6 | Nessun automa: la verifica è manuale, non integrata nel flusso CI/CD o pre-commit | Errori entrano nel vault | Media |

---

## 6. Flusso KBA (Knowledge Base Articles)

### Descrizione sintetica

Workflow strutturato per gestire KBA Emerson: estrazione da Guardian → gap check → merge → revisione manuale → lista fermata → documento meeting → consegna cliente.

### Diagramma testuale

```
1. Estrazione Guardian (manuale)
     ↓
2. Gap check (kba_merger gap)
     ↓ (STOP se mancano KBA)
3. Merge (kba_merger merge)
     ↓
4. Revisione manuale (compila Stefano's Notes)
     ↓ (obbligatoria)
5A. Lista fermata (kba_fermata) → fermata-DDMMYY.xlsx
5B. Documento meeting → meeting-DDMMYY.md
     ↓
6. Consegna cliente (ritocchi manuali)
```

### Gap Analysis

| # | Cosa manca | Impatto | Priorità |
|---|------------|---------|----------|
| 1 | IQ: il gap check è ben implementato come stop gate, ma non valida l'ambiente prima di iniziare (es. database KBA accessibile, tool funzionanti) | Fallimenti durante il processo | Media |
| 2 | OQ: i criteri di "KBA completa" sono impliciti — non c'è una checklist formalizzata di cosa deve essere presente nel merge | Output incompleti | Alta |
| 3 | Gate ben strutturati: stop al gap check, obbligo compilazione note — questo è un punto di forza | — | — |
| 4 | PQ: il processo produce output misurabili (excel, markdown) ma non si misura la qualità del contenuto (precisione note, appropriatezza tag) | Non si migliora la qualità del deliverable | Media |
| 5 | CPV assente: non si tracciano nel tempo metriche come tempo medio per KBA, tasso di errori, feedback cliente | Non si ottimizza il processo | Alta |
| 6 | Deviazioni: i ritocchi manuali post-consegna non vengono tracciati come deviazioni dal processo standard | Non si identifica dove il processo fallisce | Media |

---

## 7. Flusso Recovery (Task Interrotti)

### Descrizione sintetica

Quando un task si blocca (stato "bloccato" nell'handoff o nello scratchpad), Hermes dovrebbe riprenderlo. Non esiste un protocollo strutturato: dipende dalla memoria dello scratchpad e dall'attenzione umana.

### Diagramma testuale

```
Task in corso
      ↓
Blocco identificato (da membro o Hermes)
      ↓
Stato "bloccato" + documentazione blocco
      ↓
Hermes → Legge scratchpad + individua blocchi
      ↓
Azione correttiva (manuale)
      ↓
Ripresa task
```

### Gap Analysis

| # | Cosa manca | Impatto | Priorità |
|---|------------|---------|----------|
| 1 | IQ assente: non si valida che le condizioni di blocco siano state risolte prima di riprendere | Ripresa prematura, nuovo blocco | Alta |
| 2 | OQ assente: non esistono criteri di "blocco risolto" — Hermes decide quando riprendere | Soggettività, inconsistenza | Alta |
| 3 | Nessun gate: la ripresa è automatica, senza verifica formale | Task ripresi in condizioni non pronte | Alta |
| 4 | PQ assente: non si misura il tempo medio di recovery, tasso di recidiva del blocco | Non si identificano problemi sistemici | Alta |
| 5 | CPV assente: non si tracciano i pattern di blocco (es. task di certo tipo più soggetti a blocchi) | Non si prevengono i blocchi | Alta |
| 6 | Deviazioni non tracciate: i blocchi non vengono categorizzati — si perde la storia | Stessi problemi si ripetono | Alta |

---

## 8. Altri Flussi Identificati

### Flusso Integrazione Email (Eunomia)

Pipeline per catalogare email in vault Obsidian: parsing → arricchimento → scheda persona → archiviazione. Descritto parzialmente in `email-processor-guida.md`.

**Gap**: simile al flusso conversione PDF — nessuna PQ né CPV.

### Flusso Parallelismo (Hermes)

Possibilità di delegare subtask paralleli a più membri contemporaneamente. Descritto in `proposta-parallelismo-hermes_v1.md`.

**Gap**: non c'è protocollo per raccogliere e sintetizzare i risultati paralleli — solo accenni.

---

## Riepilogo Gap per Priorità

### Alta (impatto significativo sulla qualità/affidabilità)

| Processo | Gap |
|----------|-----|
| Creazione membro | Criteri di accettazione per ricerca Proteo e valutazione Grok non quantitativi |
| Ricerca/Analisi | Nessun gate di validazione tra output Proteo e consegna utente |
| Handoff | Stato "completato" senza validazione esterna |
| Recovery | Nessun criterio OQ, nessun gate, nessuna CPV |
| KBA | CPV assente, deviazioni non tracciate |
| Creazione membro | Nessuna CPV post-creazione |

### Media (migliorabile)

| Processo | Gap |
|----------|-----|
| Conversione PDF | Gate manuale, PQ limitata |
| Handoff | Deviazioni non tracciate |
| Verifica conformità | Gate disaccoppiato, automazione assente |
| KBA | PQ assente, rework non tracciato |
| Creazione membro | IQ parziale, deviazioni non documentate |

### Bassa (miglioramenti incrementali)

| Processo | Gap |
|----------|-----|
| Ricerca/Analisi | Flusso non formalizzato in guida |
| Verifica conformità | IQ parziale |

---

## Raccomandazioni Preliminari

Dove un framework di qualifica porterebbe più valore:

1. **Recovery (priorità assoluta)**: il flusso più carente. L'assenza di gate e CPV significa che i task bloccati possono rimanere tali per settimane senza che nessuno se ne accorga.

2. **Creazione membro**: la PQ (post-creazione) manca completamente. Un nuovo membro viene "attivato" e poi dimenticato — nessun monitoraggio delle performance nelle prime settimane.

3. **Handoff**: il gate debole ("completato" auto-dichiarato) crea rischio di output di qualità variabile accettati come finiti.

4. **Ricerca/Analisi**: il gap tra output Proteo e consegna utente è il punto dove il rischio di errore è più alto — nessuna validazione indipendente.

5. **KBA**: la CPV fornirebbe dati preziosi per ottimizzare il processo nel tempo (es. tempo medio per KBA, pattern di revisione).

### Prossimi passi suggeriti

- Definire metriche OQ per i flussi prioritari (recovery, creazione membro, handoff)
- Implementare gate di validazione dove mancano
- Aggiungere tracciamento delle deviazioni nel frontmatter dei file handoff
- Valutare automazione della verifica conformità (pre-commit hook)

---

*Documento generato da Dike — Analista processi e workflow del Team Olimpo*
*Task: T-IQOQ-001, subtask IQOQ-2*