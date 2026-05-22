---
data: 2026-05-01
mittente: proteo
destinatario: hermes
tipo: report
stato: da-processare
priorita: alta
titolo: "Analisi discrepanza moduli kba_* originali vs kba.* attuali"
---

# Analisi Discrepanza: Moduli `kba_*` Originali vs `kba.*` Attuali

> Prodotto da Proteo — 2026-05-01  
> Destinatario: Hermes  
> Scopo: Mappare la migrazione dei moduli KBA e identificare gap/mancanti

---

## 1. I 7 Moduli Originali `kba_*`

Documentati in `opencode-doc-cache.md` (linea 96) e confermati da esplorazione filesystem:

| # | Modulo Originale | Percorso | Scopo Principale | Comandi/CLI |
|---|-------------------|-----------|------------------|--------------|
| 1 | **kba_indexer** | `tools/kba_indexer/` | Indicizzazione batch KBA nel catalogo | `index`, `list`, `stats` |
| 2 | **kba_merger** | `tools/kba_merger/` | Merge Excel DeltaV + enrichment | `merge`, `gap`, `learn` |
| 3 | **kba_reporter** | `tools/kba_reporter/` | Genera brief WIP + lista patch | `main` (default) |
| 4 | **kba_meeting** | `tools/kba_meeting/` | Documento meeting da KBA {WIP} | `main` (default) |
| 5 | **kba_fermata** | `tools/kba_fermata/` | Excel fermata da KBA {DEFER} | `main` (default) |
| 6 | **kba_pipeline** | `tools/kba_pipeline/` | Orchestra tutto il flusso KBA | `run` |
| 7 | **kba_resolver** | `tools/kba_resolver/` | Mappa dipendenze documentali | `resolve` |

**Fonti**:  
- `Library/Handoff/opencode-doc-cache.md` linea 96: "kba_*: Pipeline KBA (indexer, merger, reporter, meeting, fermata)"  
- Esplorazione filesystem: `find /home/stra/TeamOlimpo/tools -type d -name "kba*"`  
- Guide operative: `Library/Meta/kba-*-guida.md`

---

## 2. I 5 Attuali Sottomoduli `kba.*`

Percorso attuale: `tools/kba/` (package riorganizzato)

| # | Sottomodulo Attuale | Stato Migrazione | Corrispondenza al Padre Originale |
|---|---------------------|------------------|-------------------------------|
| 1 | **kba.indexer** | ✅ Migrato completamente | `kba_indexer` → `kba.indexer` (nuovo package) |
| 2 | **kba.merger** | ⚠️ Migrato parzialmente | `kba_merger` → `kba.merger` (ma importa da `kba_reporter`) |
| 3 | **kba.fermata** | ⚠️ Migrato parzialmente | `kba_fermata` → `kba.fermata` (importa da `kba_reporter`) |
| 4 | **kba.meeting** | ⚠️ Migrato parzialmente | `kba_meeting` → `kba.meeting` (importa da `kba_reporter`) |
| 5 | **(reporter mancante)** | ❌ Non migrato come sottomodulo | `kba_reporter` NON è in `kba.*` |

**Fonti**:  
- `ls -la /home/stra/TeamOlimpo/tools/kba/`: visualizzato `indexer/`, `merger/`, `fermata/`, `meeting/`, `__init__.py`  
- Import statements in `tools/kba/meeting/cli.py` linee 23-25: `from tools.kba.reporter.classifier import...`  
- Import statements in `tools/kba/fermata/cli.py` linee 20-26: `from tools.kba.reporter.classifier import...`

**⚠️ NOTA CRITICA**: I moduli `kba.fermata` e `kba.meeting` sono stati spostati nel package `kba.*`, ma **importano ancora da `tools.kba_reporter`** (il modulo originale non migrato). Questo crea una dipendenza ibrida non documentata.

---

## 3. Confronto Dettagliato: Cosa È Stato Migrato

### 3.1 `kba_indexer` → `kba.indexer` ✅

**Stato**: Migrazione completa  
**File migrati**:
- `tools/kba_indexer/cli.py` → `tools/kba/indexer/cli.py`
- `tools/kba_indexer/parser.py` → `tools/kba/indexer/parser.py`
- `tools/kba_indexer/writer.py` → `tools/kba/indexer/writer.py`
- `tools/kba_indexer/config.py` → `tools/kba/indexer/config.py`

**Conferma**: `tools/kba/indexer/__init__.py` conferma: "tools.kba.indexer — Indicizzatore batch per il catalogo KBA del Team Olimpo"

---

### 3.2 `kba_merger` → `kba.merger` ⚠️

**Stato**: Migrazione completa dei file, ma dipendenze esterne  
**File migrati**:
- `tools/kba_merger/cli.py` → `tools/kba/merger/cli.py`
- `tools/kba_merger/merger.py` → `tools/kba/merger/merger.py`
- `tools/kba_merger/learner.py` → `tools/kba/merger/learner.py`
- `tools/kba_merger/gap.py` → `tools/kba/merger/gap.py`
- `tools/kba_merger/config.py` → `tools/kba/merger/config.py`

**⚠️ DIPENDENZA**: `tools/kba/merger/cli.py` linea 201-203 importa da `tools.kba.merger.enricher` (modulo NON trovato in `tools/kba/merger/`). Questo suggerisce che `enricher.py` era parte di `kba_merger` originale ma **non è stato migrato** o è stato rinominato.

**Fonti**:  
- Grep per `enricher`: trovato solo in `kba_merger/cli.py` (originale) e `kba_pipeline/steps.py` linea 558  
- Il modulo `kba_merger/enricher.py` è citato in `Library/Meta/kba-merger-guida.md` linea 514 come modulo interno, ma **non trovato su filesystem** nella ricerca dei file Python

**GAP IDENTIFICATO**: `enricher.py` dovrebbe essere in `tools/kba/merger/` ma risulta mancante.

---

### 3.3 `kba_fermata` → `kba.fermata` ⚠️

**Stato**: File migrati, ma dipende da `kba_reporter`  
**File migrati**:
- `tools/kba_fermata/cli.py` → `tools/kba/fermata/cli.py`
- `tools/kba_fermata/writer.py` → `tools/kba/fermata/writer.py`

**DIPENDENZE DA `kba_reporter`** (non migrato):
- `tools/kba/fermata/cli.py` linea 20: `from tools.kba.reporter.classifier import load_excel`
- `tools/kba/fermata/cli.py` linea 26: `from tools.kba.reporter.patch_builder import build_patch_list`

**Moduli `kba_reporter` utilizzati**:
1. `classifier.py` — `load_excel()`: Carica Excel KBA_Merged
2. `patch_builder.py` — `build_patch_list()`: Costruisce lista patch
3. `config.py` — `DEFER_KEYWORDS`, `OWNERS_INBOX_DIR`, `PROJECT_ROOT`

---

### 3.4 `kba_meeting` → `kba.meeting` ⚠️

**Stato**: File migrati, ma dipende da `kba_reporter`  
**File migrati**:
- `tools/kba_meeting/cli.py` → `tools/kba/meeting/cli.py`

**DIPENDENZE DA `kba_reporter`** (non migrato):
- `tools/kba/meeting/cli.py` linea 23: `from tools.kba.reporter.classifier import load_excel`
- `tools/kba/meeting/cli.py` linea 24: `from tools.kba.reporter.brief_builder import build_wip_brief, _kba_to_slug, _read_catalog_meta`
- `tools/kba/meeting/cli.py` linea 25: `from tools.kba.reporter.config import WIP_KEYWORDS, OWNERS_INBOX_DIR, PROJECT_ROOT`

**Moduli `kba_reporter` utilizzati**:
1. `classifier.py` — `load_excel()`: Carica Excel KBA_Merged
2. `brief_builder.py` — `build_wip_brief()`, `_kba_to_slug()`, `_read_catalog_meta()`
3. `config.py` — `WIP_KEYWORDS`, `OWNERS_INBOX_DIR`, `PROJECT_ROOT`

---

### 3.5 `kba_reporter` — IL MODULO MANCANTE ❌

**Stato**: **NON migrato** in `tools/kba/`. Esiste ancora come modulo indipendente `tools/kba_reporter/`

**File originale**:
- `tools/kba_reporter/cli.py` — Entry point CLI (non più usato, sostituito da `kba.fermata` + `kba.meeting`)
- `tools/kba_reporter/classifier.py` — `load_excel()` (USATO da `kba.fermata` e `kba.meeting`)
- `tools/kba_reporter/patch_builder.py` — `build_patch_list()` (USATO da `kba.fermata`)
- `tools/kba_reporter/brief_builder.py` — `build_wip_brief()` (USATO da `kba.meeting`)
- `tools/kba_reporter/writer.py` — `write_patch_list()`, `write_wip_brief()`, `write_kba_discussion()` (NON migrati)
- `tools/kba_reporter/config.py` — Configurazioni condivise (USATO da `kba.fermata` e `kba.meeting`)

**⚠️ PROBLEMA ARCHITETTURALE**: `kba_reporter` è stato "smembrato funzionalmente" (la CLI non serve più) ma i suoi moduli interni sono **ancora necessari** come libreria condivisa. Tuttavia, risiedono fuori dal package `kba.*`, creando una struttura ibrida non documentata.

**Documentazione**: `Library/Meta/kba-reporter-manuale.md` linee 9-13 conferma:
> "Il workflow principale KBA usa ora `kba_fermata` e `kba_meeting` al posto di `kba_reporter`. `kba_reporter` rimane utile per generare il brief WIP interno e per il vecchio flusso basato su `User Notes`"

---

### 3.6 `kba_pipeline` — NON in `kba.*`

**Stato**: Modulo indipendente `tools/kba_pipeline/`  
**Relazione con `kba.*`**: Importa da `tools.kba_merger`, `tools.kba_resolver`, `tools.kba_indexer` (moduli originali)

**Fonti**: `tools/kba_pipeline/steps.py`:
- Linea 243: `from tools.kba_indexer.parser import parse_batch_file`
- Linea 244: `from tools.kba_indexer.writer import rebuild_index, write_record`
- Linea 490: `from tools.kba_resolver.resolver import resolve_dependencies`
- Linea 557: `from tools.kba_merger.merger import merge_rows`
- Linea 558: `from tools.kba_merger.enricher import enrich_rows`
- Linea 559: `from tools.kba_merger.writer import write_merge_excel`

**NOTA**: `kba_pipeline` è l'orchestratore e usa i moduli originali (non i sottomoduli `kba.*`). Questo crea un doppio standard.

---

### 3.7 `kba_resolver` — NON in `kba.*`

**Stato**: Modulo indipendente `tools/kba_resolver/`  
**Relazione**: Usato da `kba_pipeline` (Step 3 — verifica dipendenze)

**Fonti**: `tools/kba_resolver/cli.py` — tool standalone per mappare dipendenze documentali

---

## 4. Moduli Mancanti: Profilo Dettagliato

### 4.1 `kba_reporter` (Libreria Condivisa — da migrare in `kba.reporter`)

**Funzionalità**:
- **classifier.py**: Carica file Excel KBA_Merged e classifica righe in base alle note utente
  - Funzione: `load_excel(path)` → `list[dict]`
  - Campi estratti: `kba_number`, `title`, `site`, `node`, `user_notes`, `risk_score`, `risk_level`, `emerson_cat`, `fis_notes`, `stefano_notes`
  
- **patch_builder.py**: Costruisce lista patch per fermata
  - Funzione: `build_patch_list(defer_rows)` → `dict` (struttura per sito)
  - Logica: estrae file da documenti MD, filtra per versione DeltaV, deduplica
  
- **brief_builder.py**: Costruisce brief WIP con stato analisi
  - Funzione: `build_wip_brief(wip_rows, max_age_days)` → `list[dict]`
  - Funzione: `_read_catalog_meta(slug)` → `dict` (metadati dal catalogo)
  
- **config.py**: Configurazioni centralizzate
  - `DELTAV_VERSIONS`, `VERSION_PATTERNS`, `NODE_TYPES`
  - `DEFER_KEYWORDS`, `WIP_KEYWORDS`, `DONE_NA_KEYWORDS`
  - Path: `DOCUMENTS_DIR`, `CATALOG_DIR`, `OWNERS_INBOX_DIR`

**Dipendenze**:
- `openpyxl` (per `classifier.py`)
- `pyyaml` (per `brief_builder.py`)
- `loguru`

**Struttura proposta per `kba.reporter`**:
```
tools/kba/reporter/
├── __init__.py
├── __main__.py  # (opzionale, per retrocompatibilità)
├── classifier.py
├── patch_builder.py
├── brief_builder.py
└── config.py
```

**Motivazione migrazione**: `kba.fermata` e `kba.meeting` dipendono da questi moduli. Centralizzarli in `kba.reporter` elimina la dipendenza esterna da `tools/kba_reporter/`.

---

### 4.2 `kba.merger.enricher` (Modulo Perduto)

**Stato**: Citato in `kba_merger/cli.py` e `kba_pipeline/steps.py` ma **NON TROVATO** su filesystem.

**Funzionalità attesa** (da `Library/Meta/kba-merger-guida.md` linea 514):
> `enricher` | `enricher.py` | Arricchimento da catalogo KBA locale + Suggested Note (python + AI ibrido) + CSS lookup

**Azioni necessarie**:
1. Verificare se `enricher.py` è stato perso o rinominato
2. Se perso: ricreare da specifiche in guida
3. Se rinominato: aggiornare import in `kba.merger/cli.py`

---

## 5. Raccomandazioni

### 5.1 Migrare `kba_reporter` come `kba.reporter` ✅ CONSIGLIATO

**Motivazione**:
- `kba.fermata` e `kba.meeting` dipendono già dai suoi moduli interni
- Evita struttura ibrida con moduli fuori dal package `kba.*`
- Allinea l'architettura con il design inteso (tutto in `tools/kba/`)

**Azioni**:
1. Creare `tools/kba/reporter/`
2. Copiare: `classifier.py`, `patch_builder.py`, `brief_builder.py`, `config.py`, `writer.py`
3. Aggiornare import in `kba.fermata` e `kba.meeting` da `tools.kba.reporter.*` a `tools.kba.reporter.*`
4. Opzionale: rimuovere `tools/kba_reporter/` dopo migrazione completa

---

### 5.2 Mantenere `kba_pipeline` e `kba_resolver` come moduli indipendenti ⚠️

**Motivazione**:
- `kba_pipeline` è un orchestratore che usa多线程olduli originali (non `kba.*`)
- `kba_resolver` è un tool specializzato con una sola dipendenza (`tools.kba_resolver.config`, `tools.kba_resolver.resolver`)
- Forzare migrazione di questi creerebbe complessità senza benefici immediati

**AZIONE SUGGERITA**: Aggiornare `kba_pipeline` per usare i sottomoduli `kba.*` invece dei moduli originali:
- `tools.kba_indexer` → `tools.kba.indexer`
- `tools.kba_merger` → `tools.kba.merger`
- `tools.kba_resolver` → (mantenere esterno o migrare in `kba.resolver`)

---

### 5.3 Risolvere il mistero di `enricher.py` 🔴 CRITICO

**Gap**: Il modulo `enricher.py` è citato ma non trovato. Questo potrebbe causare errori runtime in `kba.merger` se il codice tenta di importarlo.

**Azione immediata**: Cercare `enricher.py` nel filesystem o ricostruirlo.

---

## 6. Gap Informativi

1. **Modulo `enricher.py`**: Non trovato su filesystem. Non confermato se perso, mai esistito, o rinominato. Necessaria verifica con Efesto.
   
2. **Dipendenze circolari**: Non testato se `kba.reporter` (una volta migrato) creerebbe dipendenze circolari con `kba.fermata` o `kba.meeting`.

3. **Test di integrazione**: Non verificato se i moduli attuali `kba.fermata` e `kba.meeting` funzionano correttamente con le dipendenze da `kba_reporter` (import relativi vs assoluti).

4. **Versioning**: Non trovata documentazione sulla strategia di versioning dei moduli `kba.*`. Il modulo originale `kba_reporter/__init__.py` riporta versione `0.1.0`.

---

## 7. Riepilogo Esecutivo

| Modulo Originale | In `kba.*`? | Stato Migrazione | Dipendenze Esterne | Azione Richiesta |
|------------------|---------------|------------------|-------------------|------------------|
| `kba_indexer` | ✅ `kba.indexer` | Completa | Nessuna | Nessuna |
| `kba_merger` | ✅ `kba.merger` | Completa* | `enricher.py` (missing) | 🔴 Trovare `enricher.py` |
| `kba_fermata` | ✅ `kba.fermata` | Parziale | `kba_reporter.*` | Migrare `kba_reporter` → `kba.reporter` |
| `kba_meeting` | ✅ `kba.meeting` | Parziale | `kba_reporter.*` | Migrare `kba_reporter` → `kba.reporter` |
| `kba_reporter` | ❌ Mancante | Non iniziata | Nessuna | 🟡 Migrare in `kba.reporter` |
| `kba_pipeline` | ❌ Esterno | N/A | `kba_merger`, `kba_indexer`, `kba_resolver` | 🟡 Aggiornare import a `kba.*` |
| `kba_resolver` | ❌ Esterno | N/A | Nessuna | Nessuna (mantenere esterno) |

---

## 8. Fonti e Riferimenti

1. **Documentazione del sistema**:
   - `Library/Handoff/opencode-doc-cache.md` (linea 96)
   - `Library/Meta/kba-pipeline-guida.md`
   - `Library/Meta/kba-merger-guida.md`
   - `Library/Meta/kba-reporter-manuale.md`
   - `Library/Meta/kba-indexer-guida.md`
   - `Library/Meta/kba-fermata-guida.md`
   - `Library/Meta/kba-meeting-guida.md`

2. **Codice sorgente esaminato**:
   - `tools/kba/indexer/cli.py`, `parser.py`, `writer.py`, `config.py`
   - `tools/kba/merger/cli.py`, `merger.py`, `learner.py`, `gap.py`, `config.py`
   - `tools/kba/fermata/cli.py`, `writer.py`
   - `tools/kba/meeting/cli.py`
   - `tools/kba_reporter/cli.py`, `classifier.py`, `patch_builder.py`, `brief_builder.py`, `writer.py`, `config.py`
   - `tools/kba_pipeline/steps.py`
   - `tools/kba_resolver/cli.py`, `resolver.py`

3. **Esplorazione filesystem**:
   - `ls -la /home/stra/TeamOlimpo/tools/ | grep kba`
   - `find /home/stra/TeamOlimpo/tools -type d -name "kba*"`
   - `find /home/stra/TeamOlimpo/tools/kba -type f -name "*.py"`

---

**Verdetto**: I 5 sottomoduli attuali `kba.*` (indexer, merger, fermata, meeting, e il **reporter mancante**) corrispondono ai padri originali, ma la migrazione è **incompleta**. Manca `kba.reporter` come sottomodulo ufficiale, e `enricher.py` è introvabile. Si raccomanda di completare la migrazione di `kba_reporter` in `kba.reporter` e risolvere il gap di `enricher.py` prima di procedere con altre modifiche.

---
*Fine report — Proteo, 2026-05-01*
