---
data: 2026-05-18
timestamp: 2026-05-18T13:55:00
agent: efesto
task_id: T-LOC-001
invocation: 1
type: report
status: completed
priority: low
title: "Loc Counter tool — script conteggio righe agenti"
completion_notes: "Script loc_counter creato e testato con successo. 13 file .md processati, 2247 righe totali, 1752 non-vuote. Dipendenze (typer, loguru, rich) già presenti in pyproject.toml."
output_refs:
  - tools/loc_counter/__init__.py
  - tools/loc_counter/__main__.py
  - tools/loc_counter/cli.py
quality_score: 4
external_review: false
next_action: "Output ready for user. No further action needed."
---

# Loc Counter — Handoff Report

## Cosa fa lo script

Conta le righe di tutti i file `.md` nella directory `.opencode/agents/` e produce una tabella riepilogativa con:
- **Nome file**
- **Righe totali**
- **Righe non-vuote** (escluse righe bianche)
- **Riga TOTAL** con somme cumulative

## Comando di esecuzione

```bash
uv run python -m tools.loc_counter
```

Flag opzionali:
- `--verbose` / `-v`: abilita output DEBUG su stderr (default: INFO)
- `--help`: mostra help Typer

## Dipendenze

Nessuna nuova dipendenza richiesta. Tutte le librerie utilizzate sono già dichiarate in `pyproject.toml`:
- `typer>=0.15` — CLI framework
- `loguru>=0.7` — logging strutturato
- `rich>=13.7` — tabella formattata

## File prodotti

| File | Descrizione |
|------|-------------|
| `tools/loc_counter/__init__.py` | Versione del modulo (`0.1.0`) |
| `tools/loc_counter/__main__.py` | Entry point (`python -m tools.loc_counter`) |
| `tools/loc_counter/cli.py` | Logica CLI Typer + conteggio righe |

## Note operative

- Percorsi risolti dinamicamente rispetto alla root del progetto (`tools/loc_counter/cli.py` → `PROJECT_ROOT`)
- Gestione graceful: se la directory `.opencode/agents/` non esiste → exit code 1; se nessun `.md` trovato → exit code 0 con messaggio
- Codifica file: UTF-8
- Exit codes: `0` = successo, `1` = errore (directory mancante)

## Limiti

- Conta solo file `.md` diretti nella directory (non ricorsivo in sottocartelle)
- "Riga non-vuota" = riga con almeno un carattere non-whitespace dopo `strip()`
