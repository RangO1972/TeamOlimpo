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
note_completamento: "Tool creato in tools/hermes_cli/. Tutti i 10 criteri di accettazione soddisfatti. 80 handoff processati, ID manager funzionante, YAML malformato gestito."
quality_score: 5
verifica_esterna: false
priorita: alta
titolo: "Fase 1 — hermes_cli: Validatore + ID Manager"
---

# Specifica — hermes_cli Fase 1

## Obiettivo

Creare il tool CLI `tools/hermes_cli/` con i comandi di validazione e gestione ID. Il tool deve:

1. **Validare** lo scratchpad di Hermes (`Team/Hermes/Scratchpad.md`) — YAML, campi obbligatori, tipi corretti
2. **Validare** i file handoff (`Library/Handoff/`) — naming convention, frontmatter, campi
3. **Gestire** gli ID progressivi T-NNN e D-NNN (next, check duplicati)
4. **Essere estendibile** per le Fasi 2 e 3 (stessa struttura a moduli)

## Specifica comandi

```bash
# Validazione scratchpad
uv run python -m tools.hermes_cli validate scratchpad [--fix]

# Validazione singolo handoff
uv run python -m tools.hermes_cli validate handoff <file-path>

# Validazione tutti gli handoff
uv run python -m tools.hermes_cli validate handoffs [--summary]

# Validazione completa (scratchpad + tutti gli handoff)
uv run python -m tools.hermes_cli validate all [--json]

# ID: next disponibile
uv run python -m tools.hermes_cli id next task
uv run python -m tools.hermes_cli id next decision

# ID: check duplicati
uv run python -m tools.hermes_cli id check

# Flag globali
uv run python -m tools.hermes_cli <comando> --verbose   # output DEBUG
uv run python -m tools.hermes_cli <comando> --json       # output JSON machine-readable
```

### Dettaglio comportamento per comando

#### `validate scratchpad`
- Legge `Team/Hermes/Scratchpad.md`
- Verifica: YAML ben formato, `active_tasks[]` presente, ogni task ha `id`/`description`/`status`/`responsible`
- Verifica: `members_status` presente (anche se mappa di stringhe, per ora)
- Verifica: `decisions[]` presente, ogni decisione ha `id`/`date`/`description`
- **NON** bloccarsi su YAML malformato — segnala errore specifico (riga, tipo), continua
- Output su stdout (testo leggibile), warning su stderr
- Exit code: 0 = ok, 1 = errori strutturali

#### `validate handoff <file>`
- Legge il file specificato
- Verifica naming: `YYYY-MM-DD_mittente-destinatario_tipo_slug.md`
- Verifica frontmatter: campi obbligatori presenti (data, mittente, destinatario, tipo, stato, priorita, titolo)
- Verifica valori enum: tipo in lista chiusa, stato in lista chiusa, priorità in lista chiusa
- Verifica mittente/destinatario siano nomi mitologici validi (da config.py)
- Gestione graceful se file senza frontmatter o YAML rotto

#### `validate handoffs`
- Scansiona ricorsivamente `Library/Handoff/` saltando: `templates/`, `kba_batch/`, `kba_batch2/`, `tucson/`, `Legacy/`, `scripts/`, `Registro.md` (stessa logica di `handoff_register`)
- Per ogni file .md trovato, esegue validate handoff
- Con `--summary`: solo conteggi (X conformi, Y warning, Z errori)
- Output: tabella riassuntiva

#### `validate all`
- Esegue validate scratchpad + validate handoffs
- Con `--json`: output in JSON parsabile

#### `id next task`
- Scansiona tutti i task ID nello scratchpad (frontmatter `active_tasks`)
- Trova il massimo T-NNN
- Stampa il successivo (es. T-043)
- Se nessun ID trovato, stampa T-001

#### `id next decision`
- Stessa logica per D-NNN e `decisions[]`

#### `id check`
- Scansiona scratchpad + handoff
- Trova ID duplicati (stesso T-NNN usato in più punti)
- Report: lista conflitti o "Nessun duplicato"

## Anti-pattern da evitare

1. **NON usare argparse** — Typer è obbligatorio (convenzione team). Seguire lo skeleton in `tools/_template/`
2. **NON duplicare logica da handoff_register** — il modulo `tools.handoff_register/scanner.py` ha già `_read_frontmatter()` e `_validate_frontmatter()`. Importa e riusa. Se serve estendere, modifica l'originale o crea una funzione condivisa in una nuova libreria comune.
3. **NON assumere YAML valido** — Il 29% degli handoff non ha frontmatter. Lo scratchpad ha YAML invalido (righe 153-154, 325-330). Il tool non deve mai crashare su input malformato.
4. **NON scrivere su file a meno di --fix esplicito** — Fase 1 è read-only (tranne `--fix`). In Fase 1, `--fix` è opzionale e limitato: nessuna modifica automatica del contenuto, solo rinomina file handoff.
5. **NON hardcodare la lista membri** — Mettila in `config.py` come enum o costante. Lista attuale: hermes, proteo, atena, efesto, clio, dike, metis, calliope, pythagoras, hermione, euterpe, demetra, eunomia.
6. **NON usare path assoluti** — Tutti i path sono relativi alla root del repository (`/home/stra/TeamOlimpo`). Usa un `ROOT_DIR` in `config.py` che si adatta automaticamente.
7. **NON ignorare il pattern di logging** — Seguire loguru come in `handoff_register` (stderr per warning+, DEBUG con --verbose)

## Formato output atteso

### Struttura moduli
```
tools/hermes_cli/
├── __init__.py           # __version__ = "0.1.0"
├── __main__.py           # from .cli import app; app()
├── cli.py                # app Typer, callback verbose, dispatch comandi
├── models.py             # dataclass: Scratchpad, Handoff, Task, Decision
├── scanner.py            # lettura/parsing scratchpad + handoff
├── validator.py          # regole di validazione
├── id_manager.py         # ID tracking (T-NNN, D-NNN)
├── config.py             # path, enum, lista membri, skip dirs
└── templates/            # (vuoto in Fase 1, per Fase 3)
    └── .gitkeep
```

### Output console (esempio validate scratchpad)
```
╭─ hermes-cli validate scratchpad ─────────────────────────────────╮
│                                                                  │
│  Scratchpad: Team/Hermes/Scratchpad.md                           │
│                                                                  │
│  ⚠ YAML: frontmatter valido                                     │
│  ⚠ Campi: last_updated mancante (opzionale)                     │
│  ⚠ active_tasks[0]: usa 'description' invece di 'title'         │
│  ⚠ members_status: formato mappa di stringhe (atteso: oggetti)  │
│  ⚠ decisions[].id: D-OPT-001 — ok                               │
│  ⚠ decisions[12]: YAML malformato (riga ~325)                   │
│                                                                  │
│  Risultato: 1 errore, 4 warning                                  │
╰──────────────────────────────────────────────────────────────────╯
```

### Output JSON (con --json)
```json
{
  "target": "Team/Hermes/Scratchpad.md",
  "valid": false,
  "errors": [
    {"type": "yaml_parse", "line": 325, "description": "Oggetto YAML annidato in lista decisions non valido"}
  ],
  "warnings": [
    {"type": "missing_field", "field": "last_updated", "severity": "minor"},
    {"type": "wrong_field", "field": "active_tasks[0].title", "expected": "title", "actual": "description"}
  ],
  "stats": {"tasks": 11, "decisions": 12, "members": 3}
}
```

## Criteri di accettazione

1. `uv run python -m tools.hermes_cli validate scratchpad` — esegue sullo scratchpad REALE (342 righe, con errori noti), termina con exit 0, stampa warning specifici
2. `uv run python -m tools.hermes_cli validate handoff <file-senza-frontmatter>` — non crasha, stampa "frontmatter YAML assente"
3. `uv run python -m tools.hermes_cli validate handoffs` — processa 406+ file in < 5 secondi, non crasha
4. `uv run python -m tools.hermes_cli id next task` — stampa T-043 (o numero corretto successivo)
5. `uv run python -m tools.hermes_cli id next decision` — stampa D-016 (o numero corretto successivo)
6. `uv run python -m tools.hermes_cli id check` — trova i duplicati se presenti, o dice "nessun duplicato"
7. `--verbose/-v` attiva output DEBUG su stderr
8. Tutti i comandi con --json producono JSON valido parsabile
9. Tool si avvia con `uv run python -m tools.hermes_cli` dalla root repo
10. **Test minimo**: lo stesso tool può validare sé stesso (`uv run python -m tools.hermes_cli validate handoffs` deve includere questo file nei risultati)

## Riferimenti

- Template tool: `tools/_template/`
- Scanner esistente: `tools/handoff_register/scanner.py` (da riusare)
- Convenzioni scratchpad: `Team/Hermes/Convenzioni-Scratchpad.md`
- Convenzioni handoff: `Library/Meta/handoff-guida.md`
- Scratchpad attuale: `Team/Hermes/Scratchpad.md`
- Scratchpad struttura attesa (frontmatter): Convenzioni-Scratchpad.md parte 3
- Handoff struttura attesa (naming + frontmatter): handoff-guida.md sezioni Naming Convention e Frontmatter YAML
