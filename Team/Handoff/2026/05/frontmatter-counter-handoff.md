---
tool: frontmatter-counter
invoked_by: Hermes
date: 2026-05-18
agent: Efesto
---

# Handoff — Frontmatter Counter

## Cosa fa lo script

Scansione ricorsiva di tutti i file `.md` a partire da una directory radice (default: cwd).
Per ciascun file verifica se ha un **frontmatter YAML valido**, definito come:
- Riga 1: esattamente `---`
- Esistenza di un secondo `---` in una riga successiva (entro le prime 200 righe)

Directory escluse automaticamente: `node_modules/`, `.git/`, `Archivio/`.

Output: conteggio totale, file con frontmatter valido, file senza frontmatter valido.
Con `--verbose` elenca tutti i file suddivisi per categoria.

## Comando esatto

```bash
# Default: scansiona la directory corrente
uv run python -m tools.frontmatter_counter

# Directory specifica
uv run python -m tools.frontmatter_counter /path/to/dir

# Con output dettagliato
uv run python -m tools.frontmatter_counter -v
```

## Dipendenze

Nessuna dipendenza aggiuntiva. Usa solo:
- `typer` (già in `pyproject.toml`)
- `loguru` (già in `pyproject.toml`)
- `pathlib` (stdlib)

## Risultato della run (2026-05-18, repo root)

| Metrica | Valore |
|---|---|
| File `.md` totali analizzati | **3023** |
| Con frontmatter valido | **2901** (96.0%) |
| Senza frontmatter valido | **122** (4.0%) |

## Note

- Lo script non modifica alcun file, è puramente in lettura (safe).
- Il check è sintattico (presenza dei delimitatori `---`), non valida il contenuto YAML.
- Il limite di 200 righe per la ricerca del secondo `---` e' piu' che sufficiente per qualsiasi frontmatter realistico.
- Exit code: `0` in ogni caso (è un tool di analisi, non di validazione bloccante).

## Percorso script

```
tools/frontmatter_counter/
├── __init__.py      (v0.1.0)
├── __main__.py      (entry point)
└── cli.py           (logica Typer)
```
