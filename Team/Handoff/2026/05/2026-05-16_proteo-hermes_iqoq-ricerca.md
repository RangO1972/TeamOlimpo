# Ricerca IQ/OQ/PQ/DQ/CPV — Trasferibilità al Team Olimpo (Agenti AI)

> Prodotto da Proteo — 2026-05-16
> Destinatario: Hermes

## Sintesi del dominio

Il framework IQ/OQ/PQ (con DQ e CPV) è lo standard regolatorio FDA/EMA/ISPE per la qualifica di apparecchiature, sistemi e processi nell'industria farmaceutica e dei dispositivi medici. Si basa su un approccio **risk-based** e su un ciclo di vita del processo (Process Validation Lifecycle). L'obiettivo è dimostrare, in modo documentato e verificabile, che un sistema è progettato, installato, opera e performa in modo controllato e riproducibile.

## Sintesi dei concetti chiave

### DQ (Design Qualification)
Verifica che il design del sistema soddisfi i requisiti utente (URS — User Requirement Specification) e i requisiti regolatori prima dell'acquisto o dello sviluppo. Include review di specifiche tecniche, diagrammi, rischi identificati e traceability matrix.

### IQ (Installation Qualification)
Verifica che l'installazione fisica sia conforme alle specifiche del fornitore e del progetto. Controlla: cablaggi, connessioni, configurazioni hardware/software, documentazione as-built, calibrazioni iniziali.

### OQ (Operational Qualification)
Verifica che il sistema funzioni correttamente in tutto il range operativo previsto (limiti superiori e inferiori). Include test di stress, allarmi, interblocchi, recovery da failure.

### PQ (Performance Qualification)
Verifica che il processo produca output consistenti e conformi in condizioni reali di produzione (o simulate). Usa lotti di convalida e acceptance criteria predefiniti.

### CPV (Continued Process Verification)
Fase di monitoraggio continuo durante la produzione commerciale. Raccoglie dati in tempo reale per rilevare drift, trend e variazioni prima che diventino deviazioni.

### Risk-based approach (FDA/EMA)
Dal 2011 (FDA Process Validation Guidance) la qualifica è proporzionata al rischio per la qualità del prodotto e la sicurezza del paziente. Non tutti i parametri richiedono lo stesso livello di test.

### Deviation management
Ogni deviazione dai protocolli approvati deve essere documentata, investigata, giustificata o corretta. Le deviazioni critiche bloccano il rilascio del sistema.

### Documentazione
- Protocolli approvati prima dell'esecuzione
- Report con dati grezzi, calcoli, firme
- Acceptance criteria chiari e misurabili
- Traceability matrix (requisiti → test → risultati)

### CSA (Computer Software Assurance) — FDA 2022+
Nuovo approccio che sostituisce l'IQ/OQ/PQ tradizionale per software puro. Si focalizza su **assurance activities** basate sul rischio (testing, audit, code review, simulation) invece di protocolli rigidi. Riduce la documentazione pesante per software a basso rischio.

## Analisi di trasferibilità al Team Olimpo

| Fase | Ha senso per agenti AI? | Adattamento proposto | Note |
|------|--------------------------|----------------------|------|
| **DQ** | Sì — alto valore | Review strutturata del prompt + metadati + identità prima della creazione (Atena) | Equivale a "design review" del membro prima del birth |
| **IQ** | Parzialmente | Verifica che il file `.opencode/agents/<nome>.md` sia correttamente formattato, con frontmatter completo, permessi corretti, e che l'agente sia "caricato" nel sistema | Controlli automatici + checklist manuale |
| **OQ** | Sì — molto utile | Test operativi su range di input: edge cases, prompt ambigui, failure mode (es. tool non disponibile), recovery | Simile a test di robustezza |
| **PQ** | Sì — critico | Verifica che l'agente produca output consistenti e conformi su task reali (es. 3-5 scenari di produzione) | Acceptance criteria definiti da Hermes |
| **CPV** | Sì — molto promettente | Monitoraggio continuo dei log, deviation rate, quality score degli output, drift nei comportamenti | Può diventare un "quality dashboard" del team |
| **Risk-based** | Sì | Classificare ogni nuovo membro per rischio (basso/medio/alto) in base all'impatto su output finali | Es. efesto = alto rischio; euterpe = medio |
| **Deviation** | Sì | Protocollo formale per deviation durante test o produzione (es. output fuori specifica) | Gestito da Clio o Dike |
| **Documentazione** | Sì — adattato | Protocolli leggeri in Markdown + traceability matrix YAML | Evitare burocratizzazione eccessiva |
| **CSA** | Sì — modello ideale | Adottare il mindset CSA: assurance basata su rischio + testing intelligente invece di protocolli rigidi | Riduce overhead |

**Cosa NON ha senso**:
- Verifica fisica dell'hardware (cablaggi, sensori)
- Calibrazione di strumenti di misura
- Test di installazione su filesystem (a meno di automazioni)

## Framework analoghi esistenti

- **CMMI / SPICE** — maturità dei processi software (livelli 1-5)
- **ISO 9001:2015** — gestione qualità con approccio risk-based e miglioramento continuo
- **NIST AI RMF 1.0 (2023)** — framework per la gestione del rischio AI (Govern, Map, Measure, Manage)
- **ISO/IEC 42001** — sistema di gestione per AI (in sviluppo)

## Raccomandazioni preliminari per il Team Olimpo

1. **Adottare un approccio ibrido DQ + CSA** per la creazione di nuovi membri (Hermes → Proteo → Atena).
2. Definire **acceptance criteria** chiari per ogni fase (es. "l'agente risponde correttamente al 95% dei test OQ").
3. Introdurre un **quality gate** prima del rilascio in produzione (PQ).
4. Implementare un meccanismo leggero di **CPV** (monitoraggio deviation rate, log analysis, feedback loop).
5. Mantenere la documentazione **snella** (principio CSA) — privilegiare automazione e metriche rispetto a protocolli cartacei.
6. Classificare i membri per **classe di rischio** (es. core orchestrator = alto; writer tematici = basso).

## Gap informativi

- Dettagli operativi del draft FDA CSA Guidance (2022) non recuperati completamente (link 404).
- Esempi concreti di applicazione IQ/OQ/PQ a sistemi AI puri sono ancora rari nella letteratura regolatoria (2026).
- Non sono state identificate metriche standardizzate per "performance" di agenti LLM orchestrati.

## Fonti e riferimenti

- FDA Guidance for Industry: Process Validation: General Principles and Practices (January 2011)
- ISPE Baseline® Guide: Volume 5 — Commissioning and Qualification (2nd Edition)
- FDA Draft Guidance: Computer Software Assurance for Production and Quality System Software (2022)
- NIST AI Risk Management Framework 1.0 (2023)
- EMA Guideline on Process Validation (2016)
