---
data: 2026-05-01
mittente: proteo
destinatario: team
tipo: report
stato: da-processare
priorita: bassa
titolo: "Cache documentazione OpenCode — Architettura, Agenti, Convenzioni Vault"
---

# Cache Documentazione OpenCode

> Prodotto da Proteo — 2026-05-01
> Destinatario: Team Olimpo
> Scopo: Sintesi della documentazione di riferimento per consultazione rapida

## 1. Architettura del Team Olimpo

### Pattern generale
- **Orchestrator-workers**: Hermes (orchestratore) delega a membri specializzati
- **Lingua operativa**: Italiano
- **Identità**: Figure mitologiche greche

### Membri principali
| Membro | Ruolo | Archetipo |
|--------|-------|-----------|
| Hermes | Orchestratore | Comunicazione trasparente con utente |
| Proteo | Ricercatore Senior | Analisi domini, profili competenze |
| Atena | HR Manager | Costruzione nuovi membri da profili |
| Efesto | Sviluppatore Python | Script, automazioni, API |
| Clio | Esperta documentazione | Gestione Library e conversioni |
| Dike | Analista processi | Analisi flussi e KBA |
| Metis | Strategia e ottimizzazione | Ottimizzazione sistema |
| Calliope | Documentazione creativa | Contenuti creativi |

### Flusso creazione membro
Hermes → Proteo (analisi dominio) → Hermes → Atena (costruzione persona) → file in `Team/Members/<Nome>.md`

## 2. Struttura del Vault Obsidian (Library/)

### Convenzioni chiave
- **Wikilink**: `[[nota]]`, `[[nota|alias]]`, `[[nota#sezione]]`
- **Frontmatter YAML**: sempre presente, campi plurali (`tags`, `aliases`, `cssclasses`)
- **Immagini**: in `Library/assets/images/<slug>/`, riferite con path relativo `../assets/images/<slug>/`
- **Naming**: slug in kebab-case minuscolo

### Cartelle principali
```
Library/
├── documents/          # File Markdown convertiti da PDF
├── assets/images/      # Immagini organizzate per slug
├── data/               # Database SQLite, log (non indicizzato da Obsidian)
└── Meta/               # Documentazione del sistema
```

### Regole critiche
- No path assoluti nelle immagini
- No file non-Markdown in `documents/`
- No modifiche manuali a `.obsidian/`

## 3. Sistema di Handoff

### Naming convention
```
YYYY-MM-DD_mittente-destinatario_tipo_slug.md
```

### Tipi di handoff
- `profilo` — Profilo di competenze (Proteo → Atena)
- `specifica` — Specifica tecnica (Efesto, Atena)
- `feedback` — Segnalazione problemi
- `bug` — Bug ufficiale
- `report` — Relazione completamento
- `test` — Specifiche di test
- `nota` — Comunicazione informativa

### Stati
- `da-processare` → `in-corso` → `completato` | `bloccato`

### Cartelle
- `Library/Handoff/` — File attivi
- `Library/Handoff/Archivio/` — File completati (spostamento automatico)
- `Library/Handoff/Registro.md` — Indice autogenerato

## 4. Strumenti Python (tools/)

### Convenzioni CLI
- **Framework**: Typer (mai argparse)
- **Struttura**: `__init__.py`, `__main__.py`, `cli.py`
- **Entry point**: `uv run python -m tools.<nome>`
- **Logging**: loguru su stderr, `--verbose` per DEBUG
- **Exit code**: 0=successo, 1=errore gestito, 2=errore argomenti

### Tool principali
- **pdf_converter**: Conversione PDF → Markdown per Obsidian
- **kba_***: Pipeline KBA (indexer, merger, reporter, meeting, fermata)
- **consulto**: Valutazione esterna via Grok

## 5. Convenzioni File e Frontmatter

### Team/Members/<Nome>.md
```yaml
---
nome: Nome
ruolo: Descrizione ruolo
archetipo: Riferimento mitologico
---
```

### File Handoff (completo)
```yaml
---
data: YYYY-MM-DD
mittente: nome
destinatario: nome|team
tipo: [profilo|specifica|feedback|bug|report|test|nota]
stato: [da-processare|in-corso|completato|bloccato]
priorita: [alta|media|bassa]
titolo: "Titolo leggibile"
---
```

### File Library (Obsidian)
```yaml
---
title: Titolo
tags: [tag1, tag2]
aliases: [nome-alt]
---
```

## 6. Flusso Documentazione (Clio)

- Input: PDF in `Team/Inbox/`
- Tool: `uv run python -m tools.pdf_converter convert-all`
- Output: `Library/documents/<slug>.md` + immagini in `Library/assets/images/<slug>/`
- Indicizzazione: SQLite `Library/data/pdf_index.db` con FTS5

## 7. File di Configurazione Agent

- `.opencode/agents/*.md` — System prompt operativi (150-300 righe)
- `opencode.json` — Configurazione principale (default_agent: hermes)
- `AGENTS.md` — Panoramica architettura per OpenCode

## 8. Riferimenti File Chiave

| File | Scopo |
|------|-------|
| `AGENTS.md` | Architettura generale Team Olimpo |
| `Library/Meta/obsidian-vault.md` | Convenzioni vault Obsidian |
| `Library/Meta/pdf-converter-guida.md` | Guida tool conversione PDF |
| `Library/Meta/handoff-guida.md` | Sistema handoff completo |
| `Library/Meta/flusso-creazione-membro.md` | Flusso 7-step creazione membri |
| `Library/Meta/kba-pipeline-guida.md` | Pipeline KBA |
| `.opencode/agents/proteo.md` | Istruzioni operative Proteo |
| `tools/pdf_converter/` | Modulo conversione PDF |

---
*Cache generata automaticamente da Proteo il 2026-05-01. Per dettagli completi, consultare i file originali.*
