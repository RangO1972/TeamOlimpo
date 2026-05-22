---
data: 2026-05-19
timestamp: 2026-05-19T09:47:15
agent: efesto
task_id: T-EMAIL-ATTACH-001
invocation: 1
type: spec
status: completed
priority: high
title: "Content-addressable attachments per email_processor"
completion_notes: >
  Implementato SHA256 content-addressable storage per allegati email.
  Sostituito il vecchio naming con timestamp (collision-prone) con hash
  prefix a 16 caratteri. Aggiunta cache JSON persistente per deduplica
  cross-email. Test funzionale con import --limit 3 passato.
output_refs:
  - tools/email_processor/cli.py
  - tools/email_processor/attachment_cache.py
  - tools/email_processor/attachment_cache.json
quality_score: 5
external_review: false
next_action: "Output ready for Hermes verification. No further action needed."
---

# Handoff — Content-Addressable Attachments

## Cosa è stato fatto

### 1. Nuovo file: `tools/email_processor/attachment_cache.py`

Modulo per la gestione della cache JSON che mappa SHA256 full → metadati allegato.

Funzioni esposte:
- `load_cache()` — carica `attachment_cache.json` da disco, restituisce dict vuoto se assente
- `save_cache(cache)` — salva il dict su disco come JSON indentato
- `update_cache(cache, sha256_full, original_name, attach_path, size, message_id)` — aggiorna/crea entry

Struttura cache:
```json
{
  "<sha256_full>": {
    "original_name": "report.pdf",
    "path": "Inbox/attachments/2026/05/a3f8c2d1e5b790ab.pdf",
    "size": 123456,
    "first_seen": "2026-05-19T12:00:00",
    "email_ids": ["<msg-id-1>", "<msg-id-2>"]
  }
}
```

### 2. Modificato: `tools/email_processor/cli.py`

**`_save_attachment()`** — nuova firma con parametri `cache: dict` e `message_id: str`:

1. Calcola SHA256 del payload
2. Usa primi 16 caratteri hex come nome file + estensione originale
3. Se hash già in cache → **non scrive file**, solo aggiorna `email_ids`
4. Se hash nuovo → salva file + crea entry in cache
5. Restituisce `{name, path, size, hash}` (nuovo campo `hash`)

**`_mime_ext()`** — nuovo helper che mappa Content-Type a estensione (fallback per allegati senza filename)

**`import_cmd()`**:
- Carica `attach_cache` all'avvio dopo la cache message_id
- Passa `attach_cache` e `message_id` a `_save_attachment()` nel loop
- Salva cache alla fine (prima del report finale)

**Frontmatter** — campo `hash:` aggiunto per ogni allegato:
```yaml
attachments:
  - name: "report.pdf"
    path: "Inbox/attachments/2026/05/0e39697444a2ee58.pdf"
    size: 581275
    hash: "0e39697444a2ee588e4185711c9f55607fef57c504d255ce57e90ff8da9d3c80"
```

**Rimosso**: import `time` (non più usato).

### 3. Cosa NON è cambiato

- Directory struttura allegati: `Inbox/attachments/YYYY/MM/`
- Parametri chiamata da `import` (tranne aggiunta cache + message_id)
- Logging, error handling, safety net path lungo
- Altri comandi (`process`, `status`)

## Test funzionale

Eseguito con successo:
```
EMAIL_VAULT_ROOT=/home/stra/TeamOlimpo/vaults/email \
EMAIL_DIR=/mnt/hgfs/Emails/inbox \
uv run python -m tools.email_processor import --limit 3
```

**Risultati primo run**:
- 2 email importate, 1 skippata (duplicata)
- 1 allegato salvato: `0e39697444a2ee58.pdf` (581275 byte)
- Cache creata con 1 entry

**Risultati secondo run** (verifica deduplica):
- 3 email skippate (tutte già note)
- Cache invariata (1 entry)
- Nessun file duplicato scritto

## Limiti e note

- Se il vault viene cancellato ma la cache rimane, i riferimenti nella cache diventano stale. La cache non è un source of truth — il source of truth sono i file su disco. In caso di discrepanza, cancellare `attachment_cache.json`.
- La cache è salvata in `tools/email_processor/` (fisso), non nel vault.
- Il troncamento path lungo è mantenuto come safety net ma non dovrebbe mai scattare (16 char + estensione = path brevi).
