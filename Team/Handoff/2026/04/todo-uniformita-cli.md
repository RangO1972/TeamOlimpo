---
title: TODO — Backlog tool KBA
data: 2026-04-07
aggiornato: 2026-04-07
stato: chiuso
assegnato: Efesto
---

# TODO — Backlog tool KBA

---

## ✅ Completati

| Item | Descrizione |
|------|-------------|
| `kba_resolver` | Nuovo tool — mappa dipendenze fix_reference ricorsivamente |
| AI enrichment `Suggested Notes` | Refactor enricher.py ibrido Python+AI, eliminato `--recommend` |
| `pdf_converter convert-all --inbox` | Aggiunto parametro path custom |
| `kba_pipeline` | Nuovo orchestratore — esegue l'intera pipeline in un comando |
| Output colorato `kba_resolver` | `typer.echo` sostituito con `rich.Console(highlight=False)`, markup colore coerente |
| Output colorato `kba_pipeline` | `typer.echo` sostituito con `rich.Console(highlight=False)`, markup colore coerente |
| Rimozione `generate_suggested_notes.py` | File standalone rimosso (non referenziato) |
| Rename `Suggested Note` → `Suggested Notes` | config.py, enricher.py, writer.py aggiornati |
| Logging default `WARNING` | `kba_reporter`, `kba_fermata`, `kba_meeting` — `_setup_logging` usa `WARNING` |
| `__version__` nei `__init__.py` | Aggiunto `"0.1.0"` a kba_indexer, kba_merger, kba_reporter, kba_fermata, kba_meeting, handoff_register |

---

## 🟡 Saltati (decisione operativa)

### 5. Verbose via `@app.callback()`

Per `kba_reporter`, `kba_fermata`, `kba_meeting`: tool con singolo comando — il parametro diretto è accettabile e il refactor non porta benefici concreti.

Per `llm`: ha più comandi ma rischio di regressioni alto, beneficio basso.

**Decisione:** Non implementato.
