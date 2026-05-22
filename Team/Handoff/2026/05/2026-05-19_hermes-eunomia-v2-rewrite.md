---
type: handoff
from: Hermes
to: (self — profilo aggiornato)
task_id: T-EMAIL-EUNOMIA-001
status: completed
date: 2026-05-19
model: opencode/big-pickle
---

# Report — Riscrittura Eunomia v2

## Cosa è stato fatto

Riscritto completamente `.opencode/agents/eunomia.md`:

**Da**: Catalogatrice digitale
- Importava email, estraeva contatti, scriveva schede Persone in `Library/Persone/`
- Lavorava su `Team/Inbox/emails/` e produceva output in `Library/Persone/`

**A**: Analista contestuale
- Legge email già importate con `status: new` in `vaults/email/Inbox/emails/`
- Segue thread (parent/children) ricostruiti dal tool
- Cerca mittente in `Addressbook/`, concetti in `Library/Wiki/`, progetti in `projects/`
- Arricchisce note con: `## In breve`, `## Azioni / Decisioni`, `## Contesto`
- Setta `status: processed`
- Produce `Review/summaries/YYYY/MM/DD.md` e `Review/actions.md`

## Modifiche strutturali

| Aspetto | Vecchio | Nuovo |
|---------|---------|-------|
| Ruolo | Catalogatrice digitale | Analista contestuale |
| Vault target | `Library/Persone/`, `Team/Inbox/emails/` | `vaults/email/` |
| Input | File .eml grezzi | Note email già importate (status: new) |
| Output | Schede contatto in Persone/ | Note arricchite, summaries, actions |
| Competenze | Parsing, deduplicazione contatti | Analisi contestuale, linking, sintesi |
| Struttura email | Non seguiva thread | Segue thread parent/children |

## File modificato
- `.opencode/agents/eunomia.md` — riscritto integralmente (221→290 righe)
