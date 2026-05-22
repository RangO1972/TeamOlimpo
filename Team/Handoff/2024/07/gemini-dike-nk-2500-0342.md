Sono Dike, analista KBA del Team Olimpo. Ho esaminato la KBA `NK-2500-0342` e ho elaborato la mia analisi.

---
kba_id: "NK-2500-0342"
title: "An SI Dongle Is Required on Redundant Application Station or Interzone Servers After Switchover to Restore Good Redundancy Status"
source_file: "Library/documents/nk-2500-0342.md"
analyzed_at: "2024-07-30"

emerson_category: "Advisory"
risk_score: 5.3
risk_level: "Advisory"

severity: 7
occurrence: 5
detectability: 4

problem_type: "bug_software"
architecture_level: 3
impact_domains:
  - availability

affected_products:
  - "VE210x-35 Workstation - DeltaV Inter-Zone"
  - "VE2201-23 Appstation - OPC - Application Program"
  - "VE2212RED Redundant OPC Mirror"
  - "VE2224RED Redundant OPC DA Server"
  - "VE2238RED Redundant Batch Executive"
  - "VE2241 DeltaV Connect for Bailey"
  - "VE2244 DeltaV Connect for Honeywell"
affected_versions:
  - "v15.FP1"
  - "v15.FP2"
  - "v15.FP3"
  - "v15.LTS"
  - "v16.LTS"

workaround_available: true
workaround_complexity: "complex"
fix_available: true
fix_reference: "NK-2200-0460, NK-2400-0144, NK-2400-0598"

date_published: "2026-03-30"
author: "Emerson Process Management"
tags:
  - redundancy
  - application_station
  - interzone_server
  - licensing
  - hotfix
  - upgrade

confidence: "medium"
confidence_note: "La KBA classifica il problema come 'Product Issues' con azione 'Next Service Interval', che ho interpretato come 'Advisory'. La disponibilita' della fix varia tra le versioni affette, e la soluzione include sia un'azione di prevenzione semplice che una di recupero complessa, introducendo una sfumatura nella valutazione dei modificatori."
---

## Sintesi

La KBA `NK-2500-0342` descrive un problema in cui le Stazioni Applicative ridondanti o gli Interzone Server richiedono un dongle SI (System Integrity) dopo un'operazione di switchover per ripristinare lo stato di ridondanza ottimale. Questo si manifesta tipicamente dopo un aggiornamento del sistema eseguito utilizzando un dongle SI, compromettendo la disponibilita' del sistema ridondante in caso di failure del componente primario.

## Analisi del rischio

### Severita' — 7/10
La perdita di ridondanza per componenti critici come Application Stations e Interzone Servers comporta un rischio significativo per la continuita' operativa. Se il componente primario dovesse fallire mentre la ridondanza non e' pienamente operativa, si verificherebbe un'interruzione dei servizi essenziali (es. OPC, Batch Executive, comunicazioni inter-zona), con potenziale impatto sulla produzione e sull'integrita' dei dati. Sebbene non causi un arresto immediato dell'impianto, la degradazione della protezione offerta dalla ridondanza e' seria.

### Probabilita' — 5/10
Il problema si manifesta sotto una condizione specifica: "dopo un aggiornamento completato utilizzando un dongle SI". Gli aggiornamenti sono operazioni pianificate e non quotidiane, ma sono parte del ciclo di vita del sistema. L'uso di un dongle SI durante l'aggiornamento e' una procedura specifica che rende l'occorrenza plausibile, ma non automatica o frequente in condizioni operative standard.

### Rilevabilita' — 4/10
La KBA afferma che e' necessario un dongle per "restoring good redundancy status", il che implica che lo stato di ridondanza non e' "good" e quindi e' rilevabile. I sistemi DeltaV dispongono di strumenti diagnostici che dovrebbero indicare lo stato di ridondanza. Pertanto, il problema non e' completamente silenzioso e dovrebbe essere rilevabile tramite il monitoraggio dello stato del sistema.

### Score composito
Il calcolo del Risk Score base e': `(7 * 0.5) + (5 * 0.3) + (4 * 0.2) = 3.5 + 1.5 + 0.8 = 5.8`.

Sono stati applicati i seguenti modificatori:
-   Il problema richiede un'azione utente (aggiornamento con SI dongle) per manifestarsi: `-0.5`
-   Il numero di versioni affette e' superiore a 3 (v15.FP1, FP2, FP3, LTS, v16.LTS): `+0.5`
-   E' disponibile un workaround di recupero, ma e' complesso e richiede una reinstallazione/download completa delle stazioni: `-0.5`

Il Risk Score finale e': `5.8 - 0.5 - 0.5 + 0.5 = 5.3`.

Questo score si traduce in un livello di rischio **Advisory**.

## Workaround
Per prevenire l'insorgenza del problema, si raccomanda di non utilizzare un dongle SI durante la procedura di upgrade. Se il problema si e' gia' manifestato, la procedura di recupero implica la pulizia di entrambe le stazioni e un download completo con il dongle del cliente collegato. Questa procedura di recupero e' complessa e potenzialmente interruttiva.

## Raccomandazione
Si raccomanda di verificare le procedure di upgrade per assicurarsi che non sia utilizzato un dongle SI. Per le versioni DeltaV v15.LTS, v15.FP2 e v15.FP3, si consiglia di applicare l'hotfix bundle piu' recente che include la correzione per `TFSB1089087`, facendo riferimento alle KBA `NK-2200-0460`, `NK-2400-0144` e `NK-2400-0598` rispettivamente. Per le versioni v15.FP1 e v16.LTS, per le quali la soluzione software e' ancora in fase di sviluppo, e' fondamentale aderire alla procedura di evitamento e, in caso di manifestazione del problema, attuare la complessa procedura di recupero.

## Note
La KBA non fornisce una classificazione esplicita di Emerson come "Alert", "Advisory" o "Informational". Tuttavia, la categoria "Product Issues" e l'azione richiesta "Next Service Interval" suggeriscono che il problema e' di tipo Advisory. La disponibilità di una patch per alcune versioni ma non per tutte, insieme alla distinzione tra un semplice workaround di evitamento e una complessa procedura di recupero, hanno richiesto un'attenta valutazione nell'applicazione dei modificatori.