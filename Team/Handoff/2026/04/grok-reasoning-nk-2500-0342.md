```yaml
---
# Identificazione
kba_id: "NK-2500-0342"
title: "An SI Dongle Is Required on Redundant Application Station or Interzone Servers After Switchover to Restore Good Redundancy Status"
source_file: "Library/documents/nk-2500-0342.md"
analyzed_at: "2026-04-05"

# Classificazione
emerson_category: "N/A"
risk_score: 4.8
risk_level: "Advisory"

# Scoring dettagliato
severity: 5
occurrence: 5
detectability: 4

# Classificazione del problema
problem_type: "bug_software"
architecture_level: 3
impact_domains:
  - availability

# Componenti
affected_products:
  - "VE210x-35 Workstation - DeltaV Inter-Zone"
  - "VE2201-23 Appstation - OPC - Application"
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

# Mitigazioni
workaround_available: true
workaround_complexity: "medium"
fix_available: true
fix_reference: "NK-2200-0460, NK-2400-0144, NK-2400-0598"

# Metadati
date_published: "2026-03-30"
author: "Emerson Process Management"
tags:
  - "redundancy"
  - "application-station"
  - "dongle"
  - "licensing"

# Confidence
confidence: "high"
confidence_note: ""
---
## Sintesi

La KBA descrive un problema per cui, su coppie ridondanti di Application Station o Inter-zone Server, dopo uno switchover è necessario inserire un SI dongle per ripristinare lo stato di “Good Redundancy”. Il difetto si manifesta tipicamente dopo upgrade eseguiti utilizzando un SI dongle. Non impatta direttamente il controllo del processo ma degrada la disponibilità del sistema ridondante fino a quando non viene eseguita la procedura di recovery.

## Analisi del rischio

### Severità — 5/10
Il problema causa perdita dello stato di ridondanza “Good”, richiedendo intervento manuale. Non comporta perdita di controllo né rischio safety, ma può portare a modalità degradate in sistemi progettati per alta disponibilità. Severità moderata.

### Probabilità — 5/10
Si verifica solo in configurazioni ridondanti di Application Station/Inter-zone dopo switchover, e prevalentemente quando l’upgrade è stato effettuato con SI dongle. Condizione specifica ma non rara negli impianti che seguono procedure di upgrade standard.

### Rilevabilità — 4/10
Lo stato di ridondanza viene riportato come non buono nelle diagnostiche DeltaV. Il problema è quindi visibile agli operatori e agli ingegneri di sistema senza bisogno di strumenti particolari.

### Score composito
Risk Score = (5 × 0.5) + (5 × 0.3) + (4 × 0.2) = 2.5 + 1.5 + 0.8 = 4.8  
Modificatori applicati: fix/hotfix disponibili per la maggior parte delle versioni (-0.7), workaround di complessità media (-0.3). Score finale 4.8.

## Workaround
- **Avoidance**: non utilizzare SI dongle durante l’upgrade.
- **Recovery**: cancellare entrambe le stazioni e eseguire un total download con il dongle cliente corretto collegato.

## Raccomandazione
Applicare i bundle di hotfix indicati (NK-2200-0460, NK-2400-0144, NK-2400-0598) durante la prossima finestra di manutenzione. Nei sistemi v15.FP1 e v16.LTS monitorare l’uscita della soluzione software annunciata.

## Note
La classificazione Emerson (“Product Issues – Next Service Interval”) è coerente con lo score Advisory assegnato. Il problema è circoscritto al sottosistema di licensing/redundancy delle workstation di livello 3 e non coinvolge controller o SIS. Divergenza nulla rispetto alla valutazione del produttore.
```