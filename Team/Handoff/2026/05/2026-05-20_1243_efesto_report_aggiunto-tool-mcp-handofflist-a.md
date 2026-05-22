---
data: '2026-05-20'
timestamp: '2026-05-20T12:43:24'
agent: efesto
invocation: 14
type: report
status: completed
priority: medium
title: Aggiunto tool MCP handoff_list a server.py
task_id: T-HANDOFF-LIST-001
---

## Task completato: T-HANDOFF-LIST-001

### Modifica effettuata

**File modificato**: `tools/handoff/server.py`

Sono stati apportati due cambiamenti:

1. **Import aggiornati**: aggiunti `json` (come `json_lib`), `date` (come `date_type`), e le funzioni `_collect_handoffs` e `_get_scan_dirs` da `cli.py`.

2. **Nuovo tool MCP `handoff_list`**: funzione decorata con `@mcp.tool()` che espone la funzionalità di listing handoff come tool MCP.

### Nome scelto

Il tool si chiama **`handoff_list`** — scelta per consistenza con la convenzione `handoff_create` usata in opencode.json.

### Parametri accettati (tutti opzionali)

| Parametro | Tipo | Default | Descrizione |
|-----------|------|---------|-------------|
| `agent` | `Optional[str]` | `None` | Filtro per nome agente |
| `type` | `Optional[str]` | `None` | Filtro per tipo handoff |
| `task_id` | `Optional[str]` | `None` | Filtro per task ID |
| `search` | `Optional[str]` | `None` | Ricerca full-text in titolo e corpo |
| `since` | `Optional[str]` | `None` | Data inizio range (YYYY-MM-DD) |
| `until` | `Optional[str]` | `None` | Data fine range (YYYY-MM-DD) |
| `limit` | `Optional[int]` | `None` | Max risultati |
| `paths` | `bool` | `False` | Solo path relativi |
| `json_output` | `bool` | `False` | Output come JSON array |
| `year` | `Optional[int]` | `None` | Filtro anno |
| `month` | `Optional[int]` | `None` | Filtro mese |
| `day` | `Optional[int]` | `None` | Filtro giorno |

### Pattern seguito

- Stesso pattern del tool `create` esistente (gestione errori con return string, Optional parameters, logging con loguru)
- Riutilizza le funzioni helper esistenti da `cli.py` senza chiamare il comando Typer (`_get_scan_dirs`, `_collect_handoffs`)
- La risoluzione del `handoff_root` usa `_get_handoff_root()` già presente in `server.py`

### Formati di output

- **`json_output=True`**: JSON array con 9 campi per record (date, time, agent, type, title, task_id, status, priority, path)
- **`paths=True`**: un path relativo per riga
- **Default**: tabella testuale allineata con intestazione

### Verifica

1. `uv run python -m tools.handoff.server` — il server parte senza errori ✅
2. `handoff_list()` chiamato direttamente restituisce risultati in formato JSON ✅
3. Filtri per agent, type, search, limit funzionano correttamente ✅
4. CLI esistente (`uv run python -m tools.handoff list`) ancora funzionante ✅

### Note operative

- Non è stato modificato `opencode.json` — lo stesso server MCP serve entrambi i tool
- Non è stato modificato `cli.py` — solo lettura e riuso
- Il warning "Failed to parse YAML frontmatter" durante il test è comportamento esistente di `_parse_frontmatter` per file .md non-handoff presenti nelle directory
