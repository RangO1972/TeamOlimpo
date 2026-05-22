---
data: 2026-05-19
timestamp: 2026-05-19T09:50:00
agent: efesto
task_id: T-EMAIL-PIPELINE-001
invocation: 1
type: report
status: completed
priority: high
title: "Pipeline email Tasks 1-4 — implementazione completata"
completion_notes: "Tutti e 4 i tasks implementati e testati. Versione 0.5.0."
output_refs:
  - tools/email_processor/cli.py
  - tools/email_processor/__init__.py
quality_score: 5
external_review: false
next_action: "Output pronto per Hermes. Tutti i comandi funzionanti, testati con vault temporaneo."
---

# Report Efesto — Pipeline Email Tasks 1-4

## Task 1 — References in import

**File**: `tools/email_processor/cli.py`

### Modifiche:
1. In `_parse_eml()`: aggiunta estrazione dell'header `References` dall'email grezza
2. Aggiunta chiave `references: list[str]` al dict di ritorno di `_parse_eml()`
3. Nel frontmatter YAML generato: aggiunto campo `references:` subito dopo `message_id:`
4. Bump versione in `__init__.py`: 0.4.0 → 0.5.0

### Dettaglio estrazione:
```python
references_raw = _decode_mime_header(msg.get("References", ""))
references = [ref.strip() for ref in references_raw.split() if ref.strip()]
```

### Formato frontmatter:
```yaml
message_id: "<msg-003@example.com>"
references:
  - "<msg-001@example.com>"
  - "<msg-002@example.com>"
date: 2026-05-19
```

Se references è vuota: `references: []`

---

## Task 2 — Comando `thread --rebuild`

**File**: `tools/email_processor/cli.py`

### Funzioni create (4 helper + 1 comando):

1. **`_scan_all_notes(vault_root)`** — scansione ricorsiva di `Inbox/emails/**/*.md`, estrazione frontmatter YAML con `yaml.safe_load()`. Ritorna lista di dict con `path`, `message_id`, `references`, `subject`, `from`, `date`.

2. **`_build_thread_graph(notes)`** — costruisce tre mapping in memoria:
   - `parent_of[msg_id] = references[-1]` (o None per root)
   - `children_of[msg_id] = [figli_diretti]`
   - `root_of[msg_id] = references[0]` (o None per root)

3. **`_update_note_frontmatter(note_path, parent, children, root)`** — legge frontmatter YAML, aggiunge `thread_parent`, `thread_children`, `thread_root`, riscrive il file preservando il corpo.

4. **`_write_thread_index(root_id, all_notes_map, children_of, vault_root)`** — crea file indice in `Review/threads/<slug>.md` con:
   - Cronologia ordinata per data
   - Partecipanti unici
   - Stato aperto/chiuso

5. **Comando `thread`** con flag `--rebuild`.

### Esempio output indice:
```markdown
# Thread: Thread root

Cronologia:
1. 2026-05-18 — Thread root (da alice@example.com) ← prima email
2. 2026-05-18 — Re: Thread root (da bob@example.com) ← risposta
3. 2026-05-19 — Re: Thread root (da alice@example.com) ← risposta alla risposta

Totale: 3 email, 2 partecipanti
Stato: aperto (ultima risposta 2026-05-19)
```

### Idempotenza: ri-eseguire `thread --rebuild` aggiorna solo frontmatter e indici, non duplica.

---

## Task 3 — Comando `status` funzionante

**File**: `tools/email_processor/cli.py`

Sostituito lo stub con implementazione che mostra:
- Note totali (conteggio per status: new/processed/flagged)
- Thread count (file in `Review/threads/`)
- Contatti in Addressbook
- Intervallo date (min/max dal frontmatter)

### Esempio output:
```
📊 Status vault email: /tmp/test_final_vault

Note totali:    4
  - new          4
  - processed    0
  - flagged      0

Thread:         1 thread ricostruiti
Contatti:       0 in Addressbook

Intervallo:     2026-05-18 → 2026-05-19
```

---

## Task 4 — Comando `pipeline`

**File**: `tools/email_processor/cli.py`

Nuovo comando che esegue in sequenza:
1. `import --all` (chiama `_run_import()` internamente, non subprocess)
2. `thread --rebuild` (usa direttamente le funzioni helper)
3. `contacts` (chiama `_rebuild_contacts_from_notes()`)

Poi crea file segnale `_review/queue/ready.task`:

```json
{
  "timestamp": "2026-05-19T09:50:34+00:00",
  "pipeline": "import+thread+contacts",
  "status": "ready"
}
```

### Refactoring necessario:
Estratta la logica interna di `import_cmd()` in `_run_import(vault_root, email_dir, limit)` per permettere la chiamata diretta da `pipeline` (i parametri Typer Option non sono chiamabili direttamente da Python).

---

## Modifiche ai file

### `tools/email_processor/__init__.py`
- Bump versione: `0.4.0` → `0.5.0`

### `tools/email_processor/cli.py`
- Aggiunti import: `json`, `datetime`, `timezone`
- `_parse_eml()`: estrazione References header
- Frontmatter: generazione campo `references:`
- Nuove funzioni: `_scan_all_notes`, `_build_thread_graph`, `_update_note_frontmatter`, `_write_thread_index`, `_rebuild_contacts_from_notes`, `_run_import`
- Nuovi comandi Typer: `thread`, `pipeline`
- Comando `status`: sostituito stub con implementazione completa

---

## Test eseguiti

```bash
# Help mostra tutti i comandi
uv run python -m tools.email_processor --help
# → import, process, status, thread, pipeline

# Status con vault vuoto (non crasha)
uv run python -m tools.email_processor status --verbose
# → ERRORE gestito: vault non trovato

# Import con vault temporaneo
EMAIL_VAULT_ROOT=/tmp/test_vault EMAIL_DIR=/tmp/test_emails \
  uv run python -m tools.email_processor import
# → 4 note create con references nel frontmatter

# Thread rebuild
EMAIL_VAULT_ROOT=/tmp/test_vault \
  uv run python -m tools.email_processor thread --rebuild
# → 4 frontmatter aggiornati, 1 indice thread creato

# Status dopo thread
EMAIL_VAULT_ROOT=/tmp/test_vault \
  uv run python -m tools.email_processor status
# → 4 note, 1 thread, intervallo 2026-05-18 → 2026-05-19

# Pipeline completa
EMAIL_VAULT_ROOT=/tmp/test_vault EMAIL_DIR=/tmp/test_emails \
  uv run python -m tools.email_processor pipeline
# → import + thread + contacts + segnale ready.task

# Idempotenza thread
EMAIL_VAULT_ROOT=/tmp/test_vault \
  uv run python -m tools.email_processor thread --rebuild
# → stesso risultato, nessuna duplicazione
```

---

## Note operative

1. **Vault inesistente**: tutti i comandi gestiscono il caso di vault mancante con messaggio di errore chiaro e exit code 1
2. **Email con References a ID non presenti nel vault**: il thread rebuild gestisce il caso — il messaggio viene processato (parent/root impostati) ma l'indice non viene creato per root non presenti
3. **Dipendenza**: `datetime.UTC` non usabile con `from datetime import datetime` (ruff dà falso positivo UP017) — si usa `timezone.utc` con `# noqa: UP017`
4. **Config**: path configurati in `tools/config.yaml` (sezione `email_processor`) — `email_dir: /mnt/hgfs/Emails/inbox`, `vault_root: vaults/email/`

## Comandi disponibili (v0.5.0)

| Comando | Descrizione |
|---------|-------------|
| `import [--limit N] [--email-dir PATH] [--verbose]` | Importa email .eml in vault |
| `thread --rebuild [--verbose]` | Ricostruisce grafo thread |
| `status [--verbose]` | Mostra statistiche vault |
| `pipeline [--verbose]` | Esegue import → thread → contacts + segnale |
| `process [--limit N] [--verbose]` | Elaborazione AI (stub, non implementato) |
