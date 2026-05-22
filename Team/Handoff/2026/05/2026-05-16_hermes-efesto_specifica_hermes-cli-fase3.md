---
data: 2026-05-16
mittente: hermes
destinatario: efesto
tipo: specifica
stato: completato
priorita: alta
titolo: "Fase 3 — hermes_cli: Generazione Template e --fix"
preso_in_carico_da: efesto
preso_in_carico_il: 2026-05-16
processato_da: efesto
processato_il: 2026-05-16
note_completamento: "Fase 3 completata: templates (scratchpad+handoff), generator.py, scratchpad init, handoff create, --fix. Tool versione 0.3.0. Verifica Clio: APPROVATO CON RISERVA (fix placeholder template applicato)."
quality_score: 4
verifica_esterna: true
---

# Specifica — hermes_cli Fase 3

## Obiettivo

Estendere `tools/hermes_cli/` (Fase 1+2 già completate) con comandi di **generazione template** e **riparazione** (`--fix`). La Fase 3 completa il tool aggiungendo:

1. Directory `templates/` con template scratchpad e handoff
2. Comando `scratchpad init --agent <nome>` — crea scratchpad per nuovo agente
3. Comando `handoff create --type <tipo> --dest <nome> --title "..."` — crea file handoff con nome + frontmatter corretti
4. Flag `--fix` su `validate` — riparazioni automatiche (rinomina file, aggiunge frontmatter)

## Prerequisito

Leggi i file esistenti del tool per capire la struttura:
- `tools/hermes_cli/cli.py`
- `tools/hermes_cli/validator.py`
- `tools/hermes_cli/scanner.py`
- `tools/hermes_cli/config.py`
- `tools/hermes_cli/models.py`
- `Team/Hermes/Convenzioni-Scratchpad.md` (parte 7 per template scratchpad)
- `Library/Meta/handoff-guida.md` (naming e frontmatter handoff)

## Specifica comandi (da AGGIUNGERE)

```bash
# Inizializza scratchpad per nuovo agente
uv run python -m tools.hermes_cli scratchpad init --agent Eunomia [--force]

# Crea file handoff con naming e frontmatter corretti
uv run python -m tools.hermes_cli handoff create --type bug --dest efesto --title "Titolo" [--force]

# Validazione con riparazione automatica
uv run python -m tools.hermes_cli validate handoff <file> --fix
uv run python -m tools.hermes_cli validate handoffs --fix
uv run python -m tools.hermes_cli validate scratchpad --fix (solo reporting, nessuna modifica)
```

### Dettaglio comandi

#### `scratchpad init`
Crea un nuovo `Team/<NomeAgente>/Scratchpad.md` dal template.

Comportamento:
1. Verifica che la cartella `Team/<NomeAgente>/` esista (se no, chiedi se crearla con `--force`)
2. Crea `Team/<NomeAgente>/Scratchpad.md` dal template (sotto)
3. Sostituisce i placeholder `<NomeAgente>` e `<ruolo>` con i valori forniti
4. Se il file esiste già e non c'è `--force`, abortisce

Template da usare (da `Convenzioni-Scratchpad.md` parte 7):
```markdown
---
title: "<NomeAgente> — Scratchpad"
tags:
  - scratchpad
  - <nome-agente-lowercase>
  - workspace
aliases:
  - "<NomeAgente> Workspace"
  - "<NomeAgente> Dashboard"
cssclasses:
  - scratchpad
last_updated: YYYY-MM-DD
active_tasks: []
members_status: {}
decisions: []
---

> [!note] Scopo dello Scratchpad
> Questo file è lo spazio di lavoro operativo di **<NomeAgente>**, <ruolo> del Team Olimpo.
> [1-2 frasi specifiche sul ruolo di questo scratchpad]

## Stato corrente

_Nessuna attività in corso._

## Task in corso

_Nessun task attivo._

## Decisioni recenti

_Nessuna decisione registrata._

## Blocchi aperti

_Nessun blocco segnalato._

## Prossimi step

_Nessun step programmato._

## Log aggiornamenti

| Data | Aggiornamento |
|------|---------------|
| YYYY-MM-DD | Creazione iniziale dello scratchpad |
```

Flag aggiuntivi:
- `--role "ruolo descrittivo"` — per personalizzare il ruolo
- `--force` — sovrascrive se esiste

#### `handoff create`
Crea un file handoff nella cartella `Library/Handoff/YYYY/MM/` con nome e frontmatter corretti.

Comportamento:
1. Genera il nome file: `YYYY-MM-DD_hermes-<dest>_<tipo>_<slug>.md`
2. La data è sempre oggi (o `--date YYYY-MM-DD`)
3. Il mittente è sempre "hermes" (o `--from <nome>`)
4. Lo slug deriva dal titolo: lowercase, kebab-case, max 5 parole, caratteri alfanumerici + trattini
5. Crea il frontmatter con tutti i campi obbligatori
6. Se il file esiste già e non c'è `--force`, abortisce

Frontmatter generato:
```yaml
---
data: 2026-05-16
mittente: hermes
destinatario: <dest>
tipo: <tipo>
stato: da-processare
priorita: media
titolo: "<title>"
---
```

Flag aggiuntivi:
- `--from <nome>` — mittente (default: hermes)
- `--priorita alta|media|bassa` — default: media
- `--date YYYY-MM-DD` — default: oggi
- `--force` — sovrascrive se esiste
- `--dry-run` — stampa il nome file e il contenuto senza scrivere

Validazione input:
- `--type` deve essere uno dei tipi validi (da config.py: profilo, specifica, feedback, bug, report, test, nota)
- `--dest` deve essere un nome mitologico valido (da config.py) o "team"
- `--priorita` deve essere alta|media|bassa
- `--title` massimo 60 caratteri

#### `--fix` su comandi validate
Aggiungere comportamento `--fix` ai comandi di validazione esistenti.

**`validate handoff <file> --fix`**:
- Rinomina il file se il nome non segue la convenzione (es. toglie spazi, mette lowercase, aggiunge data se mancante)
- Aggiunge frontmatter minimale se assente
- MAI modificare il corpo del file

**`validate handoffs --fix`**:
- Applica --fix a tutti i file handoff non conformi
- Stampa report di cosa è stato modificato

**`validate scratchpad --fix`**:
- Solo reporting: segnala gli errori, non li corregge (troppo rischioso modificare YAML automaticamente)

**Regole di sicurezza per --fix**:
1. MAI modificare il contenuto del corpo di un file
2. MAI cancellare dati
3. Per rinomina: chiedere conferma (se non --force)
4. Per aggiunta frontmatter: usare campi minimi con valori di default ragionevoli
5. Loggare ogni modifica (su stderr, livello INFO)
6. Backup del file originale in `/tmp/hermes-cli-backup/` prima di qualsiasi modifica

## Anti-pattern da evitare

1. **NON generare slug dal titolo con caratteri speciali** — solo [a-z0-9-], niente accenti, niente spazi
2. **NON hardcodare il template scratchpad nel codice** — metterlo in `templates/scratchpad-template.md`
3. **NON modificare il corpo dei file in --fix** — solo metadati (nome, frontmatter)
4. **NON usare `shutil.move` per rinomina senza verificare collisioni** — controlla prima se il nuovo nome esiste
5. **NON dimenticare di aggiornare `__init__.py`** — versione → 0.3.0

## Formato output atteso

### Nuovo comando `scratchpad init`
```
╭─ hermes-cli scratchpad init ───────────────────────────────────╮
│  Creato: Team/Eunomia/Scratchpad.md                           │
│  Template: tools/hermes_cli/templates/scratchpad-template.md  │
│  Agente: Eunomia                                              │
│  Ruolo: Specialista in ...                                    │
╰──────────────────────────────────────────────────────────────────╯
```

### Nuovo comando `handoff create`
```
╭─ hermes-cli handoff create ────────────────────────────────────╮
│  Creato: Library/Handoff/2026/05/2026-05-16_hermes-efesto_bug_ti │
│ tolo.md                                                       │
│  Tipo: bug → efesto (priorità: media)                         │
╰──────────────────────────────────────────────────────────────────╯
```

### --fix su validate
```
╭─ hermes-cli validate handoff <file> --fix ─────────────────────╮
│  File rinominato: vecchio-nome.md → 2026-05-16_hermes-efesto_ │
│ tipo_nuovo-nome.md                                            │
│  Backup: /tmp/hermes-cli-backup/2026-05-16/vecchio-nome.md    │
│  Frontmatter aggiunto (era assente)                           │
╰──────────────────────────────────────────────────────────────────╯
```

## Template directory

Creare `tools/hermes_cli/templates/` con:

1. **`scratchpad-template.md`** — il template dal briefing (sezione "Dettaglio comandi" > `scratchpad init`)
2. **`handoff-template.md`** — template minimale handoff (per copia/incolla manuale):
```markdown
---
data: YYYY-MM-DD
mittente: mittente
destinatario: destinatario
tipo: specifica
stato: da-processare
priorita: media
titolo: "Titolo descrittivo"
---

# Titolo leggibile

## Descrizione

[Descrizione del task]

## Riferimenti

-
```

## Criteri di accettazione

1. `uv run python -m tools.hermes_cli scratchpad init --agent Eunomia` (con --force) crea `Team/Eunomia/Scratchpad.md` con template corretto
2. `uv run python -m tools.hermes_cli handoff create --type bug --dest efesto --title "Errore test" --dry-run` stampa senza scrivere
3. `uv run python -m tools.hermes_cli handoff create --type bug --dest efesto --title "Errore test"` crea il file con nome e frontmatter corretti
4. `uv run python -m tools.hermes_cli handoff create --type invalid --dest efesto --title "Test"` fallisce con errore (tipo non valido)
5. `uv run python -m tools.hermes_cli validate handoff <file-senza-frontmatter> --fix` aggiunge frontmatter
6. `uv run python -m tools.hermes_cli validate handoffs --fix` applica fix a tutti i file che ne hanno bisogno
7. I template esistono in `tools/hermes_cli/templates/`
8. Backup dei file originali in `/tmp/hermes-cli-backup/`
9. Tutti i comandi Fase 1 e Fase 2 continuano a funzionare
10. `__version__` in `__init__.py` è "0.3.0"

## Riferimenti

- Tool esistente: `tools/hermes_cli/` (leggere tutto)
- Fase 1 briefing: `Library/Handoff/2026/05/2026-05-16_hermes-efesto_specifica_hermes-cli-fase1.md`
- Fase 2 briefing: `Library/Handoff/2026/05/2026-05-16_hermes-efesto_specifica_hermes-cli-fase2.md`
- Template scratchpad: `Team/Hermes/Convenzioni-Scratchpad.md` parte 7
- Handoff naming/frontmatter: `Library/Meta/handoff-guida.md`
- Nomi membri validi: da `tools/hermes_cli/config.py` (o `Team/Members/Registro.md`)
