# Prompt — Fix broken references after repo split

*Copia questo messaggio in una nuova chat con Hermes.*

---

Abbiamo fatto il repo split di TeamOlimpo. Ora:

- **Repo pubblico** (`TeamOlimpo/`) — contiene: `.opencode/`, `tools/`, `Team/` (Members, SOPs, Prompts, Meta, Quarantine), `scripts/`, `paper/`, `opencode.json`, `AGENTS.md`
- `Library/` è un **symlink** → `/home/stra/Library/` (repo privato esterno, con `Wiki/`, `documents/`, `deliverables/`, `Fucina/`, `data/`, `emails/`, `assets/`, `projects/`)

Ci sono decine di riferimenti a path **spostati** che ora sono rotti. Vanno tutti corretti.

## Path mapping (old → new)

| Old path | New path |
|----------|----------|
| `Team/Hermes/` | `Library/Fucina/Hermes/` |
| `Team/Handoff/` | `Library/Fucina/Handoff/` |
| `Team/Fucina/` | `Library/Fucina/` |
| `Library/SOPs/` | `Team/SOPs/` |
| `Library/Prompts/` | `Team/Prompts/` |
| `Library/Meta/` | `Team/Meta/` |
| `Library/Handoff/` | `Library/Fucina/Handoff/` |
| `Team/Inbox/` | `Inbox/` |

**NOTA BENE**: `Library/Fucina/`, `Library/Wiki/`, `Library/documents/`, `Library/deliverables/`, `Library/emails/`, `Library/data/`, `Library/assets/`, `Library/projects/` sono TUTTI raggiungibili via symlink e funzionano. NON vanno toccati.

## Cosa sistemare

### 1. Tool Python — path hardcoded in help text e docstring

| File | Cosa cambia |
|------|-------------|
| `tools/taskmanager/migration.py` | righe 1, 36, 301: `Team/Hermes/Scratchpad.md` → `Library/Fucina/Hermes/Scratchpad.md` |
| `tools/handoff/server.py` | riga 124: `Team/Handoff/` → `Library/Fucina/Handoff/` |
| `tools/handoff/cli.py` | righe 278, 294, 593: `Team/Handoff/` → `Library/Fucina/Handoff/` |
| `tools/preflight_check/cli.py` | riga 80: `Library/Handoff` → `Library/Fucina/Handoff` |
| `tools/extract_kba_excel.py` | riga 18: `Team/Handoff/` → `Library/Fucina/Handoff/` |
| `tools/kba/reporter/cli.py` | righe 89, 91, 92: `Library/Prompts/` → `Team/Prompts/` ; `Team/Handoff/` → `Library/Fucina/Handoff/` |
| `tools/kba_reporter/cli.py` | righe 89, 91, 92: stesso pattern |
| `tools/kba_indexer/__init__.py` | riga 5: `Team/Handoff/kba_batch/` → `Library/Fucina/Handoff/kba_batch/` |
| `tools/kba/indexer/__init__.py` | riga 5: stesso pattern |
| `tools/llm/interactive.py` | righe 5, 10: `Library/Prompts/` → `Team/Prompts/` |
| `tools/llm/cli.py` | riga 21: `Library/Prompts/` → `Team/Prompts/` |

### 2. Agenti `.opencode/agents/` — riferimenti a documentazione spostata

Ogni file .md in `.opencode/agents/` ha riferimenti a `Library/SOPs/` che ora è `Team/SOPs/`.

**Elenco file** (tutti in `.opencode/agents/`):
- `hermes.md` — riga 58: `Library/SOPs/agent-creation-flow.md` → `Team/SOPs/agent-creation-flow.md`; riga 105: `Team/Hermes/` → `Library/Fucina/Hermes/`; righe 121-124: tutti i `Library/SOPs/` → `Team/SOPs/`
- `atena.md` — righe 61-64: `Library/SOPs/` → `Team/SOPs/`
- `proteo.md` — righe 81-82: `Library/SOPs/` → `Team/SOPs/`
- `efesto.md` — righe 64-65: `Library/SOPs/` → `Team/SOPs/`
- `clio.md` — riga 50: `Library/Meta/pdf-converter-guida.md` → `Team/Meta/pdf-converter-guida.md`; riga 124: stessso; righe 121-123: `Library/SOPs/` → `Team/SOPs/`
- `dike.md` — righe 280-282: `Library/SOPs/` → `Team/SOPs/`
- `hermione.md` — righe 29, 45, 101-102: `Library/SOPs/` → `Team/SOPs/`
- `euterpe.md` — righe 36, 98-100, 118: `Library/SOPs/` → `Team/SOPs/`
- `eunomia.md` — righe 109-111: `Library/SOPs/` → `Team/SOPs/`
- `metis.md` — righe 69, 90-92: `Library/SOPs/` → `Team/SOPs/`
- `pythagoras.md` — righe 80-81: `Library/SOPs/` → `Team/SOPs/`

### 3. Documentazione `Team/Meta/` — riferimenti a Library/Handoff e Library/Meta

Tutti i file in `Team/Meta/` che referenziano `Library/Handoff/` → vanno in `Library/Fucina/Handoff/`.
E quelli che referenziano `Library/Meta/` → diventano `Team/Meta/` (self-reference, fix relativo).

File coinvolti (controlla ogni occorrenza):
- `Team/Meta/opencode-permissions-spec.md`
- `Team/Meta/agent-template-bozza.md`
- `Team/Meta/adq-checklist.md`
- `Team/Meta/acm-report-template.md`
- `Team/Meta/deviation-log-guida.md`
- `Team/Meta/automation_video_ia-guida.md`
- `Team/Meta/opencode-agents-guida.md`
- `Team/Meta/strumenti-indice.md`
- `Team/Meta/handoff-register-guida.md`
- `Team/Meta/consulto-guida.md`
- `Team/Meta/tools/handoff/guide.md`
- `Team/Meta/tools/llm/guida.md`
- `Team/Meta/email-vault-struttura.md`
- `Team/Meta/pdf-converter-guida.md`
- `Team/Meta/email-vault-mapping.md`
- `Team/Prompts/_indice.md`
- `Team/SOPs/handoff-guide.md`
- `Team/Members/clio.md`
- `Team/Members/hermes.md`

### 4. AGENTS.md (root)

Righe da sistemare:
- 23: `Library/Handoff/YYYY/MM/` → `Library/Fucina/Handoff/YYYY/MM/`
- 23, 26, 30, 52: tutti i `Library/SOPs/` → `Team/SOPs/`
- 24: `Team/Inbox/` → `Inbox/`
- 30: `Library/Meta/` → `Team/Meta/`
- 37: `Library/Meta/pdf-converter-guida.md` → `Team/Meta/pdf-converter-guida.md`
- 66: `Team/Hermes/Scratchpad.md` → `Library/Fucina/Hermes/Scratchpad.md`
- 95: `Team/Inbox` → `Inbox`

### 5. Carte varie

- `paper/whitepaper.md` e `paper/whitepaper-it.md` — riferimenti a `Library/Meta/` e `Library/Handoff/`
- `scripts/test-template.sh` — riferimenti a `Team/Hermes/`, `Team/Handoff/`, `Team/Fucina/`, `Library/Meta/`, `Library/Prompts/`, `Team/Inbox/`
- `Team/Quarantine/` (3 file) — vecchi path vai

### 6. Cosa NON toccare

- `tools/config.yaml` — è **già corretto** con `handoff_root: Library/Fucina/Handoff`
- Tutti i riferimenti a `Library/Fucina/`, `Library/Wiki/`, `Library/documents/`, `Library/deliverables/`, `Library/data/`, `Library/emails/`, `Library/assets/`, `Library/projects/` — funzionano via symlink, lasciare stare

## Approccio consigliato

1. Prima fai una scan completa: `rg -n "Team/Hermes|Team/Handoff|Team/Fucina|Library/SOPs|Library/Prompts|Library/Meta|Library/Handoff|Team/Inbox" --glob '!.git' --glob '!.venv' --glob '!Library/Fucina/'` così vedi TUTTE le occorrenze ancora da sistemare
2. Poi procedi per blocco: tool Python → agent prompts → documentazione → AGENTS.md → carte varie
3. Ogni file va letto, verificato il contesto, e corretto con l'edit tool

---

Questo è il perimetro completo. Buona caccia ai link morti 🎯
