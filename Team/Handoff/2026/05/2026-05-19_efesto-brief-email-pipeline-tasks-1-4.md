---
type: handoff
from: Hermes
to: Efesto
task_ids:
  - T-EMAIL-PIPELINE-001
status: ready
date: 2026-05-19
---

# Brief Efesto — Pipeline Email: Tasks 1-4

## Stato

- **Tool**: `tools/email_processor/` v0.4.0 — `import` funzionante, `process` stub, `status` stub
- **Sorgente**: `/mnt/hgfs/Emails/inbox/` — 2.070 .eml (struttura `YYYY/Month/`)
- **Vault**: `vaults/email/` — da creare (directory vuota, non esiste ancora)
- **Config**: `tools/config.yaml` — `email_dir` e `vault_root` già configurati

## Task 1 — References in import

**File**: `tools/email_processor/cli.py`

**Cosa fare**:
1. In `_parse_eml()`: dopo l'estrazione di `message_id` (riga ~348), aggiungi estrazione campo `References` dall'header email
2. Salva nel dict di ritorno come `references: list[str]`
3. Nella generazione frontmatter (dopo la riga `message_id:` nel generatore YAML), aggiungi campo `references:` come lista YAML
4. Bump versione in `__init__.py`: 0.4.0 → 0.5.0

**Dettaglio estrazione**:
```python
references_raw = _decode_mime_header(msg.get("References", ""))
references = [ref.strip() for ref in references_raw.split() if ref.strip()]
```

**Frontmatter aggiunto** (subito dopo `message_id:`):
```yaml
references:
  - "<msg-id-1>"
  - "<msg-id-2>"
```

**Se references è vuota**: non includere il campo (o mettere `references: []`).

## Task 2 — Nuovo comando `thread`

**File**: `tools/email_processor/cli.py`

Nuovo comando Typer:
```bash
uv run python -m tools.email_processor thread --rebuild
```

### Cosa fa:
1. Scansiona ricorsivamente `vault_root / "Inbox" / "emails"` per tutti i `*.md`
2. Per ogni file, estrae `message_id` e `references` dal frontmatter YAML
3. Costruisce grafo delle relazioni in memoria:
   - `parent_map[message_id] = references[-1]` (se references non vuoto)
   - `children_map[msg_id] = [msg_id_direct_children]`
   - `root_map[message_id] = references[0]` (se references ha almeno 1 elemento)
4. **Algoritmo thread**:
   - Se references vuoto → è un thread root
   - Se references ha N elementi → parent = references[-1], root = references[0]
5. Per ogni file, aggiorna frontmatter aggiungendo:
   ```yaml
   thread_parent: "<msg-id>"
   thread_children:
     - "<msg-id>"
   thread_root: "<msg-id>"
   ```
6. Crea file indice per ogni thread root in `Review/threads/<slug-root-message-id>.md`

### Funzioni da scrivere:

```python
def _scan_all_notes(vault_root: Path) -> list[dict]:
    """Scansiona Inbox/emails/**/*.md, restituisce [{path, message_id, references}].
    Legge frontmatter YAML di ogni file.
    """
```

```python
def _build_thread_graph(notes: list[dict]) -> tuple[dict, dict, dict]:
    """Costruisce parent_map, children_map, root_map.
    Restituisce (parent_of, children_of, root_of).
    """
```

```python
def _update_note_frontmatter(note_path: Path, parent: str | None, children: list[str], root: str | None) -> None:
    """Aggiorna frontmatter YAML preservando altri campi.
    Usa yaml.safe_load() per leggere, modifica dict, riscrive.
    """
```

```python
def _write_thread_index(root_id: str, thread_info: dict, vault_root: Path) -> None:
    """Scrive Review/threads/<slug>.md con cronologia thread.
    thread_info contiene: messages (lista ordinate per data), subject, participants.
    """
```

### File indice thread (`Review/threads/<slug>.md`):
```markdown
# Thread: Oggetto originale

Cronologia:
1. 2026-05-18 — Email A (da X) ← prima email
2. 2026-05-18 — Email B (da Y) ← risposta
3. 2026-05-19 — Email C (da X) ← risposta alla risposta

Totale: 3 email, 2 partecipanti
Stato: aperto (ultima risposta oggi)
```

### Idempotenza:
Ri-eseguire `thread --rebuild` aggiorna solo frontmatter e indici, non duplica.

## Task 3 — Comando `status` funzionante

**File**: `tools/email_processor/cli.py`

Sostituire lo stub attuale (righe 895-910) con implementazione funzionante che mostra:

```
📊 Status vault email: vaults/email/

Note totali:    1,234
  - new:        980
  - processed:  250
  - flagged:    4

Thread:         89 thread ricostruiti
Contatti:       456 in Addressbook

Intervallo:     2024-01-15 → 2026-05-19
```

### Implementazione:
1. Scansiona `Inbox/emails/**/*.md` e conta per status
2. Conta file in `Review/threads/` per thread count
3. Conta file in `Addressbook/` per contatti
4. Trova min/max date dal frontmatter

Usa `pathlib.Path.rglob("*.md")` e semplice lettura frontmatter con regex o `yaml.safe_load`.

## Task 4 — Comando `pipeline`

**File**: `tools/email_processor/cli.py`

Nuovo comando Typer che esegue in sequenza:
1. `import --all` (chiama internamente la funzione, non subprocess)
2. `thread --rebuild`
3. `contacts` (chiama la funzione esistente)

Poi crea file segnale:
```
_review/queue/ready.task
```

Contenuto del file segnale:
```json
{
  "timestamp": "2026-05-19T12:00:00",
  "pipeline": "import+thread+contacts",
  "status": "ready"
}
```

Comando:
```bash
uv run python -m tools.email_processor pipeline
```

## Output atteso

- `tools/email_processor/cli.py` modificato con tutte e 4 le modifiche
- `tools/email_processor/__init__.py` con versione 0.5.0
- Handoff file in `Library/Handoff/2026/05/` con report

## Handoff

Al completamento, scrivere un handoff in `Library/Handoff/2026/05/2026-05-19_efesto-report-email-pipeline.md` con:
- Riepilogo modifiche apportate
- Test eseguiti (se possibile testare che il tool si avvii senza errori)
- Versione finale 0.5.0
