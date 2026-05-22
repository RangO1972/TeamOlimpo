---
data: 2026-05-18
timestamp: 2026-05-18T16:30:00
agent: efesto
task_id: T-000
invocation: 1
type: report
status: completed
priority: high
title: "email_processor import redesign — completato"
completion_notes: >
  Riscritto il comando `import` di tools/email_processor secondo
  le specifiche del design in Library/Meta/email-processor-design.md.
  Test eseguito con --limit 3, --limit 5, --limit 10.
  Deduplica verificata: rieseguendo lo stesso comando, le email
  già importate vengono correttamente saltate.
output_refs:
  - tools/email_processor/cli.py
  - tools/email_processor/__init__.py (bump v0.2.0)
quality_score: 4
external_review: false
next_action: "Output pronto per il merge. Test funzionale completato."
---

# Handoff — email_processor import redesign

## Cosa è stato modificato

- **Riscritto `tools/email_processor/cli.py`**: interamente rielaborato il comando `import` secondo il design document.
- **Bump versione `__init__.py`**: `0.1.0` → `0.2.0`

### Struttura del nuovo comando `import`

**Parsing headers:**
- `email.utils.getaddresses()` per parsare From/To/CC in tuple `(nome, email)`
- Formatta come `"Nome <email>"` (niente più rimozione nomi con virgole — YAML double-quoted le gestisce)
- Message-ID normalizzato con `<>`
- Date parsata con `dateutil.parser` → output `YYYY-MM-DD`

**Body:**
- Solo primo `text/plain` part, stop dopo primo trovato

**Naming file:**
- `{YYYY-MM-DD}-{subject-slug-30}.md`
- Slug troncato a 30 caratteri, a word boundary (taglia sull'ultimo `-` prima di 30)
- Collisioni: hash MD5 (6 char del subject) → contatore progressivo

**Struttura directory:**
- `Inbox/emails/{YYYY}/{MM}/` per le note
- `Inbox/attachments/{YYYY}/{MM}/` per gli allegati
- Data non parsabile → `unknown/unknown/`

**Allegati:**
- Per ogni part MIME con `Content-Disposition: attachment`
- Nome originale preservato; collisione → timestamp `{YYYYMMDD_HHMMSS}_` anteposto
- Nome vuoto → `attachment-{n}.bin`
- Path lungo → nome troncato a 100 char proteggendo estensione
- Aggiunti `{name, path, size}` al frontmatter

**Deduplica:**
- Cache in-memory di `message_id` costruita all'avvio da `Inbox/emails/**/*.md`
- Skip con log se `message_id` già presente

**Flag CLI mantenuti:**
- `--limit` / `-l` (int, default None)
- `--email-dir` (Path, override EMAIL_DIR)
- `--verbose` / `-v` (bool, default False)

### Cose NON toccate
- Comando `process` (ex `elabora`) → rimasto stub
- Comando `status` → rimasto stub
- Eunomia / Addressbook → non toccati
- Vecchie note email → non migrate

### Dipendenza aggiunta
- `python-dateutil` — già presente in pyproject.toml via `uv add`

## Test eseguiti

| Test | Risultato |
|------|-----------|
| `import --limit 3 --verbose` | ✅ 3 email importate, frontmatter corretto |
| `import --limit 5` (non verbose) | ✅ Import silenzioso, exit code 0 |
| Riestensione `import --limit 3` | ✅ 3 saltate per dedup (già importate) |
| `import --email-dir` con path valido | ✅ Funziona |
| `import --email-dir` con path inesistente | ✅ Errore chiaro, exit code 1 |
| YAML frontmatter parsato con pyyaml | ✅ Valido per tutte le note create |
| Allegati estratti | ✅ Salvati in `Inbox/attachments/YYYY/MM/` |
| Collisioni naming note | ✅ Hash + contatore funzionanti |

## Problemi incontrati e risolti

1. **Formato loguru**: `<message>` nel format string viene interpretato come tag colore da loguru → sostituito con `{message}` (standard replacement field).
2. **Header MIME con newline**: Subject, From ecc. possono avere folded headers (CRLF) → `_decode_mime_header` ora normalizza whitespace.
3. **YAML escaping**: Nomi con virgole, backslash, doppi apici nei valori → aggiunta funzione `_yaml_escape()` per escaping consistente.
4. **Nomi con virgole**: Rimossa la logica che scartava i nomi con virgole — YAML double-quoted li gestisce nativamente.

## Limiti noti

- La cache deduplica è in memoria: su vault molto grandi (>10K note) la scansione iniziale potrebbe essere lenta, ma è una tantum per run.
- La cache non è persistente tra run: ogni run ricostruisce il set da capo. Se diventasse un problema, si potrebbe implementare un file indice in `_review/registry/` come suggerito dal design.
- Vecchie note (formato flat, senza `message_id:`) non interferiscono con la deduplica ma non vengono neppure aggiornate.
