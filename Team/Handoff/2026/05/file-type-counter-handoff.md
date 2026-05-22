---
task_id: T-FILE-TYPE-001
agent: efesto
date: 2026-05-18
status: completed
---

# File Type Counter — Handoff

## Task ID
`T-FILE-TYPE-001`

## Cosa è stato creato

| File | Descrizione |
|------|-------------|
| `tools/file_type_counter/__init__.py` | Versione del modulo (`0.1.0`) |
| `tools/file_type_counter/__main__.py` | Punto di ingresso + logica di scansione |

## Cosa fa

Scansiona ricorsivamente `/home/stra/TeamOlimpo`, conta i file per estensione e stampa un riepilogo tabellare ordinato per conteggio decrescente, con percentuale sul totale.

- Usa solo stdlib (`pathlib`, `collections.Counter`).
- Gestisce `PermissionError` saltando i file inaccessibili.
- I file senza estensione sono contati come `(senza estensione)`.

## Come eseguirlo

```bash
uv run python -m tools.file_type_counter
```

Nessuna dipendenza esterna necessaria.

## Output di test

```
Estensione                 Conteggio        %
---------------------------------------------
.py                             7485    33.9%
.md                             3099    14.0%
.pyc                            2472    11.2%
.png                            2152     9.7%
(senza estensione)              1607     7.3%
.ts                             1417     6.4%
.map                             864     3.9%
.js                              847     3.8%
.pyi                             509     2.3%
.json                            293     1.3%
... (95 estensioni totali)
---------------------------------------------
TOTALE                         22109   100.0%

95 estensioni diverse, 22109 file totali.
```

## Note operative

- Nessun `uv add` necessario — solo stdlib.
- Il path di scansione è hardcoded su `/home/stra/TeamOlimpo`. Se serve renderlo configurabile, basta aggiungere un `typer.Argument()` (migrazione futura).
- I file `.pyc` e `.pyi` sono contati separatamente dai `.py` — se in futuro serve raggrupparli, è una modifica banale.

## Status
**Completed** — tool funzionante, testato, nessun errore.
