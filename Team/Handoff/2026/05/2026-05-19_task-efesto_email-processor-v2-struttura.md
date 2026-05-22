---
data: 2026-05-19
timestamp: 2026-05-19T16:00:00
agent: efesto
task_id: T-EMAIL-V2-001
invocation: 1
type: brief
status: todo
priority: high
title: "email_processor — adeguamento struttura vault (v3)"
completion_notes: ""
output_refs: []
quality_score: null
external_review: false
next_action: "Implementare modifiche in cli.py come da brief"
---

# Task: email_processor — adeguamento struttura vault (v3)

## Riferimenti

- **Design completo**: `Library/Meta/email-vault-struttura.md` (all'epoca: `email-vault-struttura-v2.md`)
- **Design import attuale**: `Library/Meta/email-processor-design.md`
- **File da modificare**: `tools/email_processor/cli.py` (+ bump `__init__.py`)
- **Brainstorming chiuso**: tutte le decisioni sono definitive

---

## Modifiche richieste in `cli.py`

### 1. Slug: default 30 → 60

`_truncate_slug()` (riga 222): cambiare default da `30` a `60`.

```python
def _truncate_slug(slug: str, max_len: int = 60) -> str:
```

Invocazione a riga 631:
```python
slug = _truncate_slug(slug, 60)
```

### 2. `_parse_date()` — aggiungere giorno

Attuale (riga 245): restituisce `(date_iso, year, month)`.

Nuovo: restituire `(date_iso, year, month, day)` dove `day` è `%d` zero-padded (01–31). Per `unknown`: `(date_iso, "unknown", "unknown", "unknown")`.

Aggiornare anche la chiamata in `_parse_eml()` (riga 355) e il dict restituito (riga 372+) per includere `"day": day`.

### 3. Directory struttura: `YYYY/MM/DD`

Attuale (riga 636-638):
```python
emails_dir = vault_root / "Inbox" / "emails" / year / month
```

Nuovo:
```python
emails_dir = vault_root / "Inbox" / "emails" / year / month / day
emails_dir.mkdir(parents=True, exist_ok=True)
```

### 4. Nome file: niente prefisso data

`_resolve_note_path()` (riga 477):

Oggi genera `{date}-{slug}.md`. Nuovo: genera `{slug}.md`.

Invocazione a riga 664-666: il parametro `date_iso` non serve più. Puoi rimuoverlo dalla firma o ignorarlo.

Nuova strategia:
```python
# 1. Prova {slug}.md
# 2. Se esiste → hash MD5(subject)[:6] → {slug}-{hash}.md
# 3. Se ancora collisione → contatore → {slug}-{hash}-{n}.md
```

### 5. Body: rimuovere metadati duplicati

Blocco attuale (righe 710-727): da sostituire con:

```python
fm_lines.append(f"# {data['subject']}")
fm_lines.append("")

# Body — solo text/plain raw
if data["body"]:
    fm_lines.append(data["body"])
    fm_lines.append("")
```

Da rimuovere: le righe 714-720 (`**Da:**`, `**Data:**`, `**A:**`) e la riga 724 (`## Contenuto`). Il body va direttamente dopo il titolo.

### Riepilogo modifiche per file

| Sezione | Cosa cambia |
|---|---|
| `_truncate_slug` (L222) | Default `30` → `60` |
| `_parse_date` (L245) | Restituisce anche `day` (4° elemento) |
| Chiamata `_parse_date` in `_parse_eml` (L355) | Aggiornare unpacking |
| Dict `_parse_eml` return (L372+) | Aggiungere `"day"` |
| Slug invocazione (L631) | 30 → 60 |
| Directory nota (L636-638) | `YYYY/MM` → `YYYY/MM/DD` |
| `_resolve_note_path` (L477-518) | Nome file senza prefisso data |
| Corpo nota (L710-727) | Solo `#` + body raw, niente metadati |

---

## Cosa NON fare

- ❌ Non toccare `process` e `status` (restano stub)
- ❌ Non toccare il frontmatter (rimane identico)
- ❌ Non toccare `_save_attachment()` (invariato)
- ❌ Non toccare `_build_message_id_cache()` (già funziona con `**/*.md`)
- ❌ Non migrare note esistenti (le cancella l'utente)
- ❌ Non toccare `_slugify()` (invariato)
- ❌ Non toccare `_yaml_escape()` (invariato)
- ❌ Non toccare `_decode_mime_header()`, `_format_address()`, `_format_address_list()` (invariati)

---

## Test

Verificare su un backup del vault o su directory temporanea:

| Test | Cosa verificare |
|---|---|
| `import --limit 3` | Note in `YYYY/MM/DD/*.md`, nome file senza data |
| Controllo body | Solo `# Subject` + body raw, niente `**Da:**` |
| Nome file | Max 60 char, slug pulito |
| Collisioni | Se 2 email stesso giorno con stesso subject → hash+counter |
| Data unknown | Cartella `unknown/unknown/unknown/` |
| Deduplica | Secondo run salta già importate |
| Allegati | Invariato in `Inbox/attachments/` |
| Slug con <60 char | Non viene troncato |
| Slug >60 char | Troncato a word boundary (ultimo `-` prima di 60) |
| Giorno | `01`, `02`, …, `31` (zero-padded) |
