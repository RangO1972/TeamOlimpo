---
title: "Indice Prompts — Team Olimpo"
aliases: [prompts, prompt library, indice prompts]
tags: [meta, prompts, indice]
---

# Indice Prompts — Team Olimpo

Tutti i prompt disponibili nel vault. Ogni prompt è uno strumento specializzato per delega
a provider AI esterni (Grok, Gemini). Il campo **invocato_da** indica chi lo usa e come.

---

## Struttura

```
Team/Prompts/
  kba/      — prompt operativi per il workflow DeltaV KBA
  team/     — prompt per la gestione e il test degli agenti del Team Olimpo
```

---

## Prompt KBA

Usati nella pipeline di analisi e gestione KBA Emerson DeltaV.

### [[kba/analisi-rischio-kba|Analisi Rischio KBA]]

| Campo | Valore |
|-------|--------|
| **Autore** | Dike |
| **Versione** | 1.0 |
| **Invocato da** | `consulto` batch — step 2B del workflow KBA |
| **Input** | Testo KBA (`{{kba_text}}`) |
| **Output** | JSON FMEA con risk score, livello, modificatori, raccomandazione |
| **Provider** | grok-4.20-0309-reasoning (consigliato) |

```powershell
uv run python -m tools.consulto --provider grok --model grok-4.20-0309-reasoning `
  --system ".claude/agents/dike.md" `
  --prompt "Team/Prompts/kba/analisi-rischio-kba.md" `
  --input "Library/documents/<slug>.md" --output "Library/Fucina/Handoff/kba_batch/"
```

---

### [[kba/raccomandazione-azione|Raccomandazione azione KBA]]

| Campo | Valore |
|-------|--------|
| **Autore** | Efesto |
| **Versione** | 1.0 |
| **Invocato da** | `tools/kba_merger/recommender.py` — `kba_merger merge --recommend` |
| **Input** | Riga KBA con metadati e User Notes (`{{kba_text}}`), regole prontuario (`{{rules_context}}`) |
| **Output** | JSON: `{action, rationale, confidence}` |
| **Provider** | grok (default merger) |

Chiamato automaticamente da `kba_merger` — non invocare manualmente.

---

### [[kba/estrai-regole-prontuario|Estrai regole prontuario KBA]]

| Campo | Valore |
|-------|--------|
| **Autore** | Efesto |
| **Versione** | 1.0 |
| **Invocato da** | `tools/kba_merger/recommender.py` — `kba_merger learn --provider grok` |
| **Input** | Casi di disaccordo AI/umano (`{{kba_text}}`) |
| **Output** | Lista numerata Markdown di regole euristiche |
| **Provider** | qualsiasi |

Chiamato automaticamente da `kba_merger learn` — non invocare manualmente.

---

### [[kba/report-meeting|Report KBA per meeting cliente]]

| Campo | Valore |
|-------|--------|
| **Autore** | Dike |
| **Versione** | 1.0 |
| **Invocato da** | `tools/kba_meeting/cli.py` — `kba_meeting` |
| **Input** | Lista KBA WIP con sintesi, workaround, nota Stefano (`{{kba_text}}`) |
| **Output** | Documento Markdown italiano colloquiale per meeting |
| **Provider** | grok-4.20-0309-reasoning (default kba_meeting) |

```powershell
uv run python -m tools.kba_meeting "Library/deliverables/KBA_Merged_xxx.xlsx"
```

---

### [[kba/sintesi-cliente|Sintesi KBA per il cliente]]

| Campo | Valore |
|-------|--------|
| **Autore** | Hermes / kba_reporter |
| **Versione** | 1.0 |
| **Invocato da** | `kba_reporter` (vecchio workflow) |
| **Input** | Testo KBA + record catalogo (`{{kba_text}}`, `{{catalog_record}}`) |
| **Output** | Sezione Markdown strutturata (problema / componenti / condizioni / azioni) |
| **Provider** | grok-4.20-0309-reasoning |

> Usato dal vecchio workflow `kba_reporter`. Nel nuovo workflow il documento meeting
> è prodotto da `kba_meeting` con [[kba/report-meeting]].

---

## Prompt Team

Usati da Hermes per la gestione del ciclo di vita degli agenti del Team Olimpo.

### [[team/valutazione-ricerca|Valutazione ricerca Proteo]]

| Campo | Valore |
|-------|--------|
| **Autore** | Hermes |
| **Versione** | 1.0 |
| **Invocato da** | Hermes — flusso creazione membro, step 4 |
| **Input** | Ricerca di Proteo su un dominio professionale (`{{kba_text}}`) |
| **Output** | Tabella punteggi (6 criteri), lacune critiche, giudizio APPROVATA/RIVEDERE/RIFARE |
| **Provider** | grok-4.20-0309-reasoning |

```powershell
uv run python -m tools.consulto --provider grok --model grok-4.20-0309-reasoning `
  --prompt "Team/Prompts/team/valutazione-ricerca.md" `
  --input "Library/Fucina/YYYY-MM-DD_ricerca_MEMBRO_vN.md" --output "Library/Fucina/"
```

---

### [[team/valutazione-profilo|Valutazione profilo Atena]]

| Campo | Valore |
|-------|--------|
| **Autore** | Hermes |
| **Versione** | 1.0 |
| **Invocato da** | Hermes — flusso creazione membro, step 6 |
| **Input** | Profilo vecchio + profilo nuovo concatenati (`{{kba_text}}`) |
| **Output** | Tabella punteggi (6 criteri), delta vecchio/nuovo, giudizio APPROVATO/RIVEDERE/RIFARE |
| **Provider** | grok-4.20-0309-reasoning |

```powershell
uv run python -m tools.consulto --provider grok --model grok-4.20-0309-reasoning `
  --prompt "Team/Prompts/team/valutazione-profilo.md" `
  --input ".claude/agents/MEMBRO.md" "Library/Fucina/YYYY-MM-DD_profilo_MEMBRO_vN.md" `
  --merge --output "Library/Fucina/"
```

---

### [[team/test-profilo|Test profilo agente esistente]]

| Campo | Valore |
|-------|--------|
| **Autore** | Hermes |
| **Versione** | 1.0 |
| **Invocato da** | Hermes — audit periodico o dopo modifiche puntuali a un agente |
| **Input** | File agent `.claude/agents/MEMBRO.md` (`{{kba_text}}`) |
| **Output** | Test chiarezza/coerenza/completezza, scenari, giudizio SOLIDO/MIGLIORABILE/DA RIVEDERE |
| **Provider** | grok-4.20-0309-reasoning |

```powershell
uv run python -m tools.consulto --provider grok --model grok-4.20-0309-reasoning `
  --prompt "Team/Prompts/team/test-profilo.md" `
  --input ".claude/agents/MEMBRO.md" --output "Library/deliverables/"
```

---

## Regole di manutenzione

- **Ogni prompt ha frontmatter** con `title`, `tags`, `versione`, `autore`, `invocato_da`, `placeholder`
- **Bump versione** se il framework o i criteri cambiano — rieseguire test su 3-5 input noti
- **invocato_da** deve sempre essere aggiornato se lo script che usa il prompt cambia path
- **Prompt deprecati**: spostare in `Team/Prompts/_archivio/` invece di cancellare

*Ultimo aggiornamento: 2026-04-03*
