---
data: '2026-05-20'
timestamp: '2026-05-20T12:41:02'
agent: hermes
invocation: 3
type: spec
status: completed
priority: medium
title: Aggiungere tool MCP handoff_list al server MCP handoff
task_id: T-HANDOFF-LIST-001
completion_notes: Brief per Efesto — aggiungere tool list al server MCP handoff
---

## Task: Aggiungere tool MCP `list` a `tools/handoff/server.py`

### Stato attuale

Il server MCP in `tools/handoff/server.py` espone solo il tool `create` (registrato come `handoff_create` in opencode.json).  
La CLI in `tools/handoff/cli.py` ha già un comando `list` completo con tutti i filtri (--agent, --type, --since, --until, --search, --json, --paths, --limit, --year, --month, --day).

### Obiettivo

Esporre la funzionalità di `list` come tool MCP aggiuntivo chiamato `list`, seguendo lo stesso pattern del tool `create` esistente.

### Specifica

1. **Apri** `tools/handoff/server.py`
2. **Aggiungi** una nuova funzione tool decorata con `@mcp.tool()` di nome `list` (o `list_handoffs` — vedi nota sul naming sotto).
3. **La funzione deve**:
   - Accettare parametri opzionali: `agent`, `type`, `task_id`, `search`, `since`, `until`, `limit`, `paths`, `json_output`, `year`, `month`, `day` (tutti `Optional[str | int | bool]`, come nel CLI)
   - Delegare alla logica esistente in `tools/handoff/cli.py` riutilizzando le funzioni di basso livello già presenti (`_find_project_root`, `_load_config`, `_get_scan_dirs`, `_collect_handoffs`), **senza chiamare** il comando Typer `list_handoffs()` (che usa `typer.echo` e `rich.Table` — non adatti a MCP).
   - Restituire una stringa: in formato JSON se `json_output=True`, altrimenti una tabella/testo leggibile.
   - Verificare la presenza del parametro prima di usare valori di default.
4. **Naming**: Il nome del tool MCP determina come viene chiamato dall'LLM. Valuta se chiamarlo `list` (semplice, ma potrebbe collidere con built-in Python), `list_handoffs`, o `handoff_list`. La scelta migliore per consistenza con `handoff_create` (nome MCP) è... decidi tu.

### Pattern da seguire

Il tool `create` esistente in `server.py` mostra come:
- Importare funzioni helper da `cli.py`
- Gestire parametri `Optional`
- Restituire stringhe di errore/successo

### Output atteso

Dopo la modifica, riavviando opencode il tool MCP `handoff_list` (o nome scelto) sarà disponibile per listing handoff con filtri.

### File interessati

- `tools/handoff/server.py` (da modificare)
- `tools/handoff/cli.py` (sola lettura — riusa la logica)
- `opencode.json` (NON deve cambiare — lo stesso server MCP servirà entrambi i tool)

### Verifica

1. `uv run python -m tools.handoff.server` parte senza errori
2. Il tool `list` risponde con risultati in formato JSON
