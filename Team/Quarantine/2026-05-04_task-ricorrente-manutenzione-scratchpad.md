---
title: "Task Ricorrente - Manutenzione Scratchpad Hermes"
tags: [dike, hermes, manutenzione, scratchpad, processo]
aliases: [Task T-011]
date: 2026-05-04
---

# Task Ricorrente T-011: Manutenzione Periodica Scratchpad Hermes

**Frequenza**: Ogni 7-10 giorni (prossima esecuzione: 2026-05-11)  
**Responsabile**: Dike  
**Obiettivo**: Mantenere lo scratchpad di Hermes leggero, ordinato e performante.

## Azioni da eseguire

### 1. Rotazione Log Settimanale (Hermes)
Hermes esegue automaticamente ogni lunedì la rotazione del log:
- Sposta la sezione "Log aggiornamenti" in `Team/Hermes/Logs/Scratchpad-Log-YYYY-WW.md`
- Lascia solo le ultime 3-5 righe di log nello scratchpad principale

### 2. Pulizia e Consolidamento (Dike)
Ogni 7-10 giorni Dike esegue:

- **Verifica task attivi**:
  - Controlla che tutti i task con `status: "in_progress"` abbiano un output corrispondente in `Library/Handoff/`
  - Segnala task orfani o bloccati

- **Consolidamento decisioni**:
  - Sposta le decisioni più vecchie di 30 giorni in `Team/Hermes/Decisions/Archivio/`
  - Mantieni solo le ultime 10-12 decisioni attive nello scratchpad

- **Pulizia sezioni**:
  - Verifica che "Blocchi aperti" non contenga voci obsolete
  - Aggiorna "Prossimi step" se necessario

- **Report mini**:
  - Produce un breve report in `Team/Hermes/Snapshots/Report-YYYY-MM-DD.md` con:
    - Numero di task attivi
    - Decisioni consolidate
    - Eventuali anomalie rilevate
    - Raccomandazioni

### 3. Snapshot Mensile (ogni 4 settimane)
Dike crea uno snapshot completo:
- Copia lo stato corrente dello scratchpad in `Team/Hermes/Snapshots/Scratchpad-Snapshot-YYYY-MM.md`

## Struttura cartelle

- `Team/Hermes/Logs/` → Log settimanali
- `Team/Hermes/Snapshots/` → Snapshot mensili e report
- `Team/Hermes/Decisions/Archivio/` → Decisioni storiche

## Criteri di successo

- Scratchpad principale sempre sotto 150 righe
- Nessun task orfano > 7 giorni
- Log e decisioni facilmente recuperabili
- Dike produce report chiari e azionabili

---

**Nota**: Questo task è ricorrente e deve essere eseguito anche se non ci sono nuove attività. È un'operazione di igiene del sistema.
