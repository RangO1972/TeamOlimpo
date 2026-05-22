```yaml
---
# Identificazione
kba_id: "NK-2500-0342"
title: "An SI Dongle Is Required on Redundant Application Station or Interzone Servers After Switchover to Restore Good Redundancy Status"
source_file: "Library/documents/nk-2500-0342.md"
analyzed_at: "2026-04-02"

# Classificazione
emerson_category: "N/A"             # Nessuna classificazione Alert/Advisory/Informational esplicita; "Required Action: Next Service Interval" implica basso rischio
risk_score: 2.3                     # 1.0 - 10.0
risk_level: "Informational"         # Negligible | Informational | Advisory | Warning | Critical

# Scoring dettagliato
severity: 5                         # 1-10
occurrence: 4                       # 1-10
detectability: 3                    # 1-10 (10 = difficile da rilevare)

# Classificazione del problema
problem_type: "configuration"       # bug_software | security_vulnerability | incompatibility | configuration | hardware | procedural
architecture_level: 3               # 0-4 (da campo a enterprise)
impact_domains:                     # Lista dei domini impattati
  - availability

# Componenti
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

# Mitigazioni
workaround_available: true
workaround_complexity: "medium"     # trivial | simple | medium | complex | none
fix_available: true
fix_reference: "NK-2200-0460, NK-2400-0144, NK-2400-0598 (hotfix per TFSB1089087); in sviluppo per v15.FP1 e v16.LTS"

# Metadati
date_published: "2026-03-30"
author: "Emerson Process Management"
tags:
  - redundancy
  - dongle
  - upgrade
  - workstation
  - hotfix

# Confidence
confidence: "high"                  # high | medium | low
confidence_note: ""                 # Motivazione sintetica — obbligatoria se confidence != high
---
```

## Sintesi

Problema di configurazione su stazioni ridondanti (Application/Inter-zone Servers): dopo switchover successivo a upgrade con SI dongle, lo status di ridondanza diventa cattivo e richiede l'inserimento del dongle per ripristino. Impatto limitato alla disponibilità ridondante su livello workstation; nessun effetto su controllo processo.

## Analisi del rischio

### Severita' — 5/10
Degradazione status ridondanza su componenti livello 3 (workstation OPC/Batch), con workaround manuale. Nessun rischio su produzione, safety o integrità dati; impatta solo disponibilità ridondante post-upgrade.

### Probabilita' — 4/10
Manifesta solo dopo upgrade specifico con SI dongle (configurazione plausibile ma non universale); avoidance semplice (non usare dongle SI).

### Rilevabilita' — 3/10
Immediatamente evidente post-switchover tramite status ridondanza visualizzato su HMI/DeltaV Operate.

### Score composito
(5 x 0.5) + (4 x 0.3) + (3 x 0.2) = 2.5 + 1.2 + 0.6 = 4.3  
Modificatori: workaround disponibile (-1), fix/hotfix per molte versioni (-1), trigger utente-dipendente (-0.5), >3 versioni (+0.5) → 4.3 - 2.5 + 0.5 = 2.3  
Livello: Informational.

## Workaround
Avoidance: non usare SI dongle durante upgrade. Recovery: clear entrambe le stazioni + total download con customer dongle.

## Raccomandazione
Applicare avoidance durante upgrade; verificare hotfix nelle KB correlate al prossimo service interval.

## Note
Classificazione Emerson implicita ("Next Service Interval") coerente con score basso. Fix parzialmente disponibile; monitorare aggiornamenti per v15.FP1/v16.LTS. Nessuna divergenza.