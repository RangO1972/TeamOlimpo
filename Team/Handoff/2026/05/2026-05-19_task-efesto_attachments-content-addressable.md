---
from: Hermes
to: Efesto
task_id: "ATTACH-1"
task_ref: "T-EMAIL-ATTACH-001"
date: 2026-05-19
status: sent
---

# Brief: Implementare content-addressable attachments per email_processor

## Obiettivo

Risolvere due criticità nel salvataggio allegati di `tools/email_processor/cli.py`:

1. **Collisioni su stesso nome**: se due allegati hanno lo stesso nome (specie nella stessa email), il timestamp `time.strftime("%Y%m%d_%H%M%S")` ha risoluzione al secondo e collapse.
2. **Deduplica assente**: stesso file allegato a N email viene salvato N volte — spreco.

## Soluzione: Content-Addressable Storage

Sostituire l'attuale logica di naming con un sistema basato su **SHA256 hash del payload**.

### Dettagli implementativi

#### 1. Nome file

```
{sha256_prefix(16)}.{ext}
```

- Prendi i primi **16 caratteri** dell'hex digest SHA256 del payload
- Estensione dal filename originale (o da `Content-Type` se assente)
- Lunghezza fissa: `16 + 1 + len(ext)` — mai path troppo lungo

#### 2. Cache mapping

Salvare un file `tools/email_processor/attachment_cache.json` con struttura:

```json
{
  "<sha256_full>": {
    "original_name": "report.pdf",
    "path": "Inbox/attachments/2026/05/a3f8c2d1e5b790ab.pdf",
    "size": 123456,
    "first_seen": "2026-05-19T12:00:00",
    "email_ids": ["<message-id-1>", "<message-id-2>"]
  }
}
```

- Aggiornato a ogni import: se hash già presente, aggiungi message-id alla lista
- Se hash non presente, salva file + inserisci entry
- Caricato all'avvio, riscritto alla fine

#### 3. Modifiche a `_save_attachment()`

```python
def _save_attachment(part, attach_base, year, month, index, cache, message_id):
```

Nuova firma con `cache: dict` e `message_id: str`.

Logica:

1. Calcola `sha256(payload).hexdigest()`
2. Se hash già in cache → **non salvare file**, solo aggiungi `message_id` alla lista
3. Se hash nuovo → salva come `{hash_prefix(16)}{ext}` in `attach_base/year/month/`
4. Aggiorna cache con metadati

#### 4. Frontmatter

L'`attachments:` nel frontmatter della nota deve includere l'hash:

```yaml
attachments:
  - name: "report.pdf"
    path: "Inbox/attachments/2026/05/a3f8c2d1e5b790ab.pdf"
    size: 123456
    hash: "a3f8c2d1e5b790ab..."  # full SHA256
```

#### 5. Cosa NON cambiare

- Directory struttura: `Inbox/attachments/YYYY/MM/`
- Parametri chiamata da `import` (tranne aggiunta cache + message_id)
- Logging, error handling, troncamento path (non serve più ma lasciare come safety net)

## File da modificare

- **`tools/email_processor/cli.py`**: `_save_attachment()`, `import` command, sezione allegati
- **`tools/email_processor/attachment_cache.py`** (NUOVO): classe/cache load/save
- **`tools/email_processor/__init__.py`**: aggiorna eventuali `__all__`

## Criteri di accettazione

- [ ] Due allegati con stesso nome nella stessa email → salvati come file distinti (hash diverso → nome diverso)
- [ ] Stesso file in email diverse → secondo import non riscrive il file, solo aggiorna cache
- [ ] Frontmatter include campo `hash` per ogni allegato
- [ ] Cache JSON correttamente letta/scritta
- [ ] `uv run python -m tools.email_processor import --limit 3` funziona senza errori
- [ ] Test con email che hanno allegati duplicati (nome e contenuto)

## Consegnabili

1. Codice modificato
2. Handoff di riepilogo da salvare in `Library/Handoff/2026/05/`
3. Nessun test formale richiesto — test funzionale con `import --limit N`
