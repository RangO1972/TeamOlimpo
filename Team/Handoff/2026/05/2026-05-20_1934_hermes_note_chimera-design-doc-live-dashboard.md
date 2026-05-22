---
data: '2026-05-20'
timestamp: '2026-05-20T19:34:05'
agent: hermes
invocation: 8
type: note
status: completed
priority: medium
title: Chimera Design Doc + Live Dashboard
task_id: T-CHIMERA-001
completion_notes: Chimera ha ora un design doc e una dashboard live. Il ciclo di dover
  chiedere "stato" è rotto — Hermes aggiorna automaticamente.
---

## Cosa è stato fatto

### Problema
La Chimera Roadmap era un documento statico (forward-looking) che non tracciava lo stato reale dell'implementazione. L'utente doveva chiedere "stato" per sapere cosa era stato fatto — risultato: incazzatura.

### Soluzione

1. **`Library/deliverables/chimera-design.md`** — Nuovo Design Document che cattura:
   - Visione e principi architetturali
   - Architettura del sistema (mappa componenti, agenti, MCP tools, strumenti Python)
   - Pattern implementati con stato reale (✅ / 🟡 / 🔴)
   - Idee Fase 1 con stato reale vs pianificato
   - Decisioni Architetturali (ADR-001 → ADR-006)
   - Cose fatte non tracciate dalla roadmap (15+ voci)
   - Dashboard complessiva per fase e per progetto
   - Regola: aggiornamento automatico ogni volta che Hermes tocca Chimera

2. **`Library/Wiki/topics/chimera.md`** — Riscritta come dashboard live:
   - Stato complessivo per fase (con emoji semaforo)
   - Tabella per ogni fase con stato reale per idea
   - Sezione "Cosa abbiamo fatto che la roadmap non prevedeva"
   - Collegamenti al Design Document e legacy roadmap

### Cosa NON è stato fatto (resta da fare)
- Auto-capture sessioni Hermes (idea 1.7)
- System prompt audit (idea 1.1)
- Tutta Fase 2-4 tranne provenance tracking e template brief

### Output
- `Library/deliverables/chimera-design.md`
- `Library/Wiki/topics/chimera.md` (aggiornato)
