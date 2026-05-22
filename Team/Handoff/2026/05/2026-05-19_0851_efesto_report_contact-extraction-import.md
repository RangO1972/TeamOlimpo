---
data: 2026-05-19
timestamp: 2026-05-19T08:51:00
agent: efesto
task_id: T-001
invocation: 1
type: report
status: completed
priority: medium
title: "Implementata estrazione contatti durante import email_processor"
completion_notes: >
  Creato il modulo contacts.py con build_addressbook_index(), upsert_contact(),
  upsert_contacts_from_email(), save_index_cache(). Modificato _parse_eml()
  per esporre from_raw/to_raw/cc_raw. Integrato in import_cmd() con estrazione
  contatti prima della deduplica. Testato con 4 email fake: funziona skip
  utente, skip macchina, creazione nuovi, aggiornamento last_contact,
  inversione "Cognome, Nome", idempotenza su secondo import.
output_refs:
  - tools/email_processor/contacts.py
  - tools/email_processor/cli.py
  - tools/email_processor/__init__.py
quality_score: 4
next_action: "Nessuna azione necessaria. Tool testato e funzionante."
---

# Report: Estrazione contatti durante `import` in email_processor

## Cosa è stato fatto

### 1. Nuovo file: `tools/email_processor/contacts.py`

Modulo specializzato per la gestione delle schede contatto in `Addressbook/`.

**Funzioni pubbliche:**

| Funzione | Descrizione |
|----------|-------------|
| `build_addressbook_index(addressbook_dir)` | Scansiona `Addressbook/*.md`, estrae `email:` dal frontmatter, restituisce `{email_lower: slug}` |
| `upsert_contact(addressbook_dir, name, email, date, index)` | Crea o aggiorna una scheda contatto con frontmatter standard. Skip utente e mittenti macchina. Aggiorna `last_contact` solo se data > esistente. |
| `upsert_contacts_from_email(addressbook_dir, from_raw, to_raw, cc_raw, date, index)` | Chiama `upsert_contact()` per mittente + To + Cc. Restituisce `{"created": N, "updated": N, "skipped": N}` |
| `save_index_cache(addressbook_dir, index)` | Salva `Addressbook/_index.json` come cache persistente |
| `load_index_cache(addressbook_dir)` | Carica cache (fallback, source of truth sono i .md) |

**Helper privati:**
- `_clean_display_name(raw)` — adattato da vecchio extractor: rimuove `[dipartimento]`, `<email>`, inverte `"Cognome, Nome"`, pulisce virgolette
- `_name_to_slug(name)` — genera slug lowercase con trattini, max 60 char

### 2. Modifiche a `tools/email_processor/cli.py`

**`_parse_eml()`:**
- Aggiunti `from_raw`, `to_raw`, `cc_raw` al return dict (tuple/liste di tuple `(name, email)` normalizzate)

**`import_cmd()`:**
- `addressbook_index` costruito all'avvio con `build_addressbook_index()`
- `total_created` / `total_updated` trackati
- Estrazione contatti eseguita **PRIMA** della deduplica (come da specifica)
- `save_index_cache()` chiamato dopo il loop
- Report finale include `Contatti creati` e `Contatti agg.`

### 3. Versione bumpata a `0.4.0`

## Test eseguiti

| Test | Risultato |
|------|-----------|
| 3 email fake: normale, "Cognome, Nome [Sales]", noreply automatico | ✅ 3 email importate, 3 contatti creati, 1 aggiornato, noreply skippato |
| Inversione "Bianchi, Laura" → slug "laura-bianchi", matching contatto esistente | ✅ |
| Aggiornamento `last_contact` se data più recente | ✅ "2026-05-19" → "2026-05-22" |
| Secondo import: idempotenza (0 creati, nessun duplicato) | ✅ |
| Rimozione virgolette YAML dal parsing email nel frontmatter | ✅ Fixato bug in build_addressbook_index |
| Skip `stefano.ranghetto@emerson.com` | ✅ |
| Skip mittenti macchina (nome vuoto dopo clean) | ✅ |

## Path file modificati

- **`tools/email_processor/contacts.py`** — nuovo modulo (370 righe)
- **`tools/email_processor/cli.py`** — modificato: import, _parse_eml(), import_cmd()
- **`tools/email_processor/__init__.py`** — versione `0.4.0`

## Limiti e note

- `organization` e `role` nel frontmatter sono lasciati vuoti (da popolare con arricchimento futuro)
- Il conteggio "Contatti agg." include anche i contatti trovati ma con data non più recente (nessuna modifica file effettiva, ma operazione comunque eseguita)
- L'estrazione contatti avviene anche per email duplicate (message-id già presente) — comportamento voluto per tenere traccia dei contatti anche da email già importate
- L'indice `_index.json` è una cache; la fonte autoritativa rimangono i file `.md` in `Addressbook/`
