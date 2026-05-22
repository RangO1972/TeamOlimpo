---
data: 2026-05-16
mittente: hermes
destinatario: efesto
tipo: specifica
stato: completato
preso_in_carico_da: efesto
preso_in_carico_il: 2026-05-16
processato_da: efesto
processato_il: 2026-05-16
note_completamento: "Fase 2 completata. report.py creato (155 righe). Comandi report/diff/stats aggiunti. 20 discrepanze trovate nel diff (YAML malformato). Tool versione 0.2.0."
quality_score: 5
verifica_esterna: false
priorita: alta
titolo: "Fase 2 — hermes_cli: Diagnostica e Report"
---

# Specifica — hermes_cli Fase 2

## Obiettivo

Estendere il tool `tools/hermes_cli/` (Fase 1 già completata) con comandi di diagnostica e reportistica. La Fase 2 aggiunge tre nuovi comandi al gruppo principale e un nuovo modulo `report.py`.

## Prerequisito

Il tool esiste già in `tools/hermes_cli/`. La Fase 1 ha creato:
- `cli.py` — app Typer con gruppi `validate` e `id`
- `scanner.py` — lettura scratchpad e handoff
- `validator.py` — regole di validazione
- `id_manager.py` — gestione ID
- `config.py` — path, enum
- `models.py` — dataclass

Leggi questi file per capire la struttura prima di iniziare.

## Specifica comandi (da AGGIUNGERE)

```bash
# Report overview dello stato corrente
uv run python -m tools.hermes_cli report [--short]

# Confronto coerenza frontmatter vs body dello scratchpad
uv run python -m tools.hermes_cli diff scratchpad

# Statistiche aggregate
uv run python -m tools.hermes_cli stats [--month 2026-05]
```

### Dettaglio comandi

#### `report`
Stampa un overview dello stato corrente del sistema Hermes:

```
╭─ hermes-cli report ────────────────────────────────────────────╮
│  Hermes CLI — Report stato                                     │
│                                                                │
│  Task:                                                         │
│    Aperti:      3 (T-CLI-001, T-EMAIL-001, T-XAI-001)         │
│    Completati:  15                                             │
│    Bloccati:    0                                              │
│                                                                │
│  Agenti coinvolti:                                             │
│    Efesto:     T-CLI-001 (in_progress)                         │
│    Hermes:     T-EMAIL-001 (in_progress)                       │
│    ...                                                         │
│                                                                │
│  Handoff attivi:                                               │
│    da-processare:  5                                           │
│    in-corso:       2                                           │
│    bloccati:        0                                           │
│    completati:     70                                          │
│    senza stato:    3                                           │
│                                                                │
│  Conformità:                                                   │
│    Scratchpad:  ❌ 1 errore, 0 warning (YAML malformato)       │
│    Handoff:     ✓ 65/80 conformi, 12 warning, 3 errori        │
│    ID:          ⚠ 4 duplicati (falsi positivi nel body)        │
╰────────────────────────────────────────────────────────────────╯
```

- Con `--short`: output ridotto a 3-4 righe
- Con `--json`: output machine-readable

#### `diff scratchpad`
Confronta il frontmatter `active_tasks[]` con la sezione body "Task in Corso".

Trova discrepanze:
1. Task in frontmatter ma non nel body → segnala
2. Task nel body ma non in frontmatter → segnala
3. Task in entrambi ma con stato diverso → segnala

Output:
```
╭─ hermes-cli diff scratchpad ───────────────────────────────────╮
│  Confronto frontmatter vs body                                 │
│                                                                │
│  Task in frontmatter ma non nel body:                          │
│    - T-EMAIL-001 (in_progress)                                 │
│                                                                │
│  Task nel body ma non in frontmatter:                          │
│    - T-CV-001 (completato) — legacy, forse da ripulire         │
│                                                                │
│  Task con stato diverso:                                       │
│    - T-XAI-001: frontmatter=in_progress, body=in_progress ✓   │
│                                                                │
│  Esito: 2 discrepanze trovate                                  │
╰────────────────────────────────────────────────────────────────╯
```

- Con `--json`: output JSON
- Exit code: 0 = allineato, 1 = discrepanze trovate

#### `stats`
Statistiche aggregate del sistema:

```
╭─ hermes-cli stats ─────────────────────────────────────────────╮
│  Statistiche Team Olimpo                                       │
│                                                                │
│  Task per agente:                                              │
│    Proteo:    12 (completati: 10, in corso: 2)                 │
│    Hermes:    10 (completati: 8, in corso: 2)                  │
│    Efesto:     3 (completati: 1, in corso: 2)                  │
│    Clio:       3 (completati: 3, in corso: 0)                  │
│    ...                                                         │
│                                                                │
│  Handoff per tipo:                                             │
│    report:      24                                             │
│    specifica:   18                                             │
│    profilo:     12                                             │
│    bug:          6                                             │
│    ...                                                         │
│                                                                │
│  Volume per mese:                                              │
│    2026-03:     3 handoff                                      │
│    2026-04:    10 handoff                                      │
│    2026-05:    64 handoff                                      │
╰────────────────────────────────────────────────────────────────╯
```

- Con `--month YYYY-MM`: filtra per mese specifico
- Con `--json`: output JSON
- Con `--agente <nome>`: filtra per agente

## Anti-pattern da evitare

1. **NON rompere i comandi esistenti** della Fase 1. Aggiungi, non modificare.
2. **NON duplicare logica di scansione** — usa `scanner.py` esistente (`read_scratchpad()`, `scan_handoff_files()`)
3. **NON parsare il body markdown con regex** — il body è markdown semi-strutturato. Usa un approccio pragmatico: cerca titoli di sezione (`##`), poi cerca pattern `[T-XXX]` nelle righe successive.
4. **NON assumere che body e frontmatter siano allineati** — anzi, il `diff` esiste proprio per trovare le discrepanze.
5. **NON aggiungere dipendenze esterne** — usa solo Typer, loguru, rich (già presenti), json (standard library).

## Formato output atteso

### Nuovo modulo: `report.py`

```python
# tools/hermes_cli/report.py
# Funzioni:
#   generate_report(scratchpad, handoff_results, short=False) -> dict
#   generate_diff(scratchpad) -> dict
#   generate_stats(handoff_paths, month=None, agent=None) -> dict
```

Ogni funzione torna un dizionario che `cli.py` formatta in testo (Rich) o JSON.

### Criteri di accettazione

1. `uv run python -m tools.hermes_cli report` stampa overview completa senza crash
2. `uv run python -m tools.hermes_cli report --short` stampa versione ridotta
3. `uv run python -m tools.hermes_cli report --json` produce JSON valido
4. `uv run python -m tools.hermes_cli diff scratchpad` trova almeno 2 discrepanze (lo scratchpad reale ne ha)
5. `uv run python -m tools.hermes_cli diff scratchpad --json` produce JSON
6. `uv run python -m tools.hermes_cli diff scratchpad` exit 1 se discrepanze, 0 se allineato
7. `uv run python -m tools.hermes_cli stats` stampa statistiche senza crash
8. `uv run python -m tools.hermes_cli stats --month 2026-05` filtra per mese
9. `uv run python -m tools.hermes_cli stats --agente efesto` filtra per agente
10. Tutti i comandi Fase 1 continuano a funzionare invariant

## Riferimenti

- Fase 1 completata: `tools/hermes_cli/` (leggere tutti i file)
- Briefing Fase 1: `Library/Handoff/2026/05/2026-05-16_hermes-efesto_specifica_hermes-cli-fase1.md`
- Scratchpad reale: `Team/Hermes/Scratchpad.md` (342 righe)
