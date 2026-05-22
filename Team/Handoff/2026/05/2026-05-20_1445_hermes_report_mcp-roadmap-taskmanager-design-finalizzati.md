---
data: '2026-05-20'
timestamp: '2026-05-20T14:45:18'
agent: hermes
invocation: 5
type: report
status: completed
priority: medium
title: MCP Roadmap + Taskmanager Design Finalizzati
task_id: T-MCP-ROADMAP-001
---

## Completato

### Documento 1: MCP Roadmap (Consolidato)
- **Path**: `Library/Wiki/concepts/2026/05/mcp-roadmap.md`
- 4 miglioramenti integrati: exit criteria Fase 1, KB MCP rischio, Quality Gate decisione esplicita, coesistenza Scratchpad
- Nome tool aggiornato a `taskmanager`

### Documento 2: Task/State Manager Design (Finalizzato)
- **Path**: `Library/Wiki/concepts/2026/05/taskmanager-design.md`
- **Tool name**: `taskmanager`
- **Tool prefix**: `taskmanager_` (es. `taskmanager_task_create`)
- **Backing store**: `Team/Hermes/state.yaml` (YAML puro)
- **6 tool**: taskmanager_task_create, taskmanager_task_update_status, taskmanager_task_query, taskmanager_task_summary, taskmanager_task_log_event, taskmanager_task_export

### Decisioni Utente Chiuse
D1: Auto-promozione parent ✅
D2: Limite descrizione 150 caratteri, prompt < 140 ✅
D3: Tag una parola, liberi ✅
D4: state.yaml in Team/<agent>/ ✅
D5: IDs storici preservati ✅
D6: No backup automatico ✅
D7: Prefisso taskmanager_ ✅
D8: Nessun WIP limit ✅

### Prossimo Step
Implementazione del server MCP taskmanager in tools/taskmanager/
