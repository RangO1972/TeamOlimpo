---
data: 2026-03-26
mittente: efesto
destinatario: clio
tipo: specifica
stato: completato
priorita: alta
titolo: "Nuovo tool: handoff_register — registro e archiviazione handoff"
processato_da: clio
processato_il: 2026-03-26
---

# Specifica — Tool handoff_register

## Contesto

Ho implementato il modulo `tools/handoff_register/` che automatizza due operazioni sul sistema handoff del Team Olimpo:
1. Archiviazione dei file con `stato: completato` da `Library/Handoff/` a `Library/Handoff/Archivio/`
2. Rigenerazione di `Library/Handoff/Registro.md`

## Struttura del modulo

```
tools/handoff_register/
    __init__.py      — docstring del package
    __main__.py      — entry point per python -m
    config.py        — costanti di path (PROJECT_ROOT, HANDOFF_DIR, ARCHIVIO_DIR, REGISTRO_PATH)
    scanner.py       — legge frontmatter da tutti i file handoff
    archiver.py      — sposta file completati in Archivio/
    writer.py        — genera Registro.md
    cli.py           — argparse + dispatch dei comandi
```

## Comandi disponibili

```bash
uv run python -m tools.handoff_register sync       # archivia completati + rigenera Registro
uv run python -m tools.handoff_register registro   # solo rigenera Registro (read-only)
uv run python -m tools.handoff_register archivia   # solo sposta i completati in Archivio/
```

Flag globale `--verbose / -v` per output debug su stderr.

## Comportamento su file legacy

La cartella `Library/Handoff/` contiene file storici che non seguono le naming convention e frontmatter attuali (es. `feedback-efesto-loguru-missing.md`, `profilo-competenze-hermes.md`). Lo script:
- Non crasha su questi file
- Emette WARNING su stderr per ogni campo mancante
- Li include nel Registro con `—` nei campi assenti
- Non li tocca mai (policy read-only sui sorgenti)

## Policy operative (invarianti)

- Lo script è **sempre read-only** sui file handoff sorgente: non modifica mai frontmatter né corpo
- `Library/Handoff/templates/` è sempre ignorato
- `Library/Handoff/Registro.md` è sempre escluso dalla scan
- Se un file con lo stesso nome esiste già in Archivio/, lo spostamento viene saltato con WARNING (no sovrascrittura)
- Le directory di destinazione sono create automaticamente se assenti

## Dipendenze

Nessuna dipendenza nuova: usa `pyyaml`, `loguru`, `rich` già presenti in `pyproject.toml`.

## Criteri di accettazione verificati

- [x] `registro` su cartella vuota non crasha
- [x] `archivia` su cartella senza completati riporta "Nessun file completato"
- [x] File con frontmatter assente o incompleto emettono WARNING ma non interrompono l'esecuzione
- [x] Registro.md generato ha le due tabelle (attivi + archiviati)

## Azione richiesta

Prendi in carico questo handoff e verifica che il Registro.md generato sia leggibile e navigabile nel vault Obsidian. Se noti problemi di formattazione Markdown o campi mancanti che rendono il Registro poco utile, apri un handoff feedback verso Efesto.
