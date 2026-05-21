# Fase 2 — Knowledge Base MCP: Brief di Analisi

**Task:** T-MCP-004
**Parent:** T-MCP-003 (Fase 2 KB MCP)
**Stato:** 🔍 Analisi in corso
**Data:** 2026-05-20

---

## Obiettivo

Analizzare e decidere come implementare un **Knowledge Base MCP server** per Team Olimpo, che permetta a Hermes e agli agenti di fare query sul Wiki (`Library/Wiki/`) via strumenti MCP invece di caricare file interi nel contesto.

## Contesto Roadmap (dalla Fase 1 consolidata)

La roadmap MCP (vedi `Library/Wiki/concepts/2026/05/mcp-roadmap.md`) definisce:

- **Priorità**: P1 — Build Phase 2 (dopo Task/State Manager che è ✅ completato)
- **Approccio**: grep-first, niente vector DB, niente Chroma
- **Sforzo stimato**: 1-2 giorni
- **Impatto**: Medio-Alto (riduce contesto, query senza caricare file interi)

### Architettura Attuale

```
Hermes (orchestratore)
  │
  ├── taskmanager MCP ✅ (6 tool: create, update, query, summary, log_event, export)
  ├── handoff MCP ✅ (create, list)
  ├── email_processor MCP ✅ (status, search, discover, rules_list, contacts)
  └── ❌ Knowledge Base MCP — DA COSTRUIRE
```

### Principi Architetturali (inviolati)

- MCP è il **layer di interfaccia** (come accedi allo stato)
- Il filesystem è il **layer di persistenza** (dove lo stato vive)
- Gli handoff sono il **substrato di comunicazione**
- Hermes è il **layer di orchestrazione**
- Ogni MCP server è **opzionale** — gli agenti cadono su accesso diretto ai file

---

## Decisioni da Prendere nell'Analisi

### 1. Scelta Architetturale: Option A vs Option B

**Option A (default roadmap):** Estendere il server handoff **esistente** con:
- Un nuovo tool `wiki_search(query)` 
- Resources MCP per `wiki_read(page)`
- Vantaggio: zero nuovi server, configurazione minima
- Rischio: il server handoff diventa troppo complesso/instabile

**Option B:** Server MCP separato per Knowledge Base
- Vantaggio: separazione delle responsabilità, isolamento fallimenti
- Svantaggio: nuovo server da configurare in opencode.json, più complessità

**Criterio di scelta:** Se il server handoff esistente ha già troppe responsabilità o se le query wiki richiedono dipendenze/gestioni specifiche → Option B.

### 2. Design dei Tool

Tool minimi proposti:

| Tool | Parametri | Output | Note |
|------|-----------|--------|------|
| `wiki_search(query)` | `query: str` | Array di {path, title, snippet, score} | grep -r su Library/Wiki/ |
| `wiki_read(page)` | `path: str` | Contenuto pagina | MCP Resource o tool separato |

Domande aperte:
- `wiki_search` deve supportare regex o solo plain text?
- Quanti risultati restituire? (default 5-10?)
- Formato snippet: quante righe di contesto?
- Filtri opzionali: per data, per categoria, per tag?
- Rispetta il limite di 3 server MCP massimi? (Sì: handoff + taskmanager + email_processor + questo = 4 SOU)

### 3. Scope della Ricerca

`wiki_search` deve cercare:
- Solo in `Library/Wiki/`? O anche in `Library/documents/`?
- Solo `.md` file o anche altri formati?
- Frontmatter YAML incluso nella ricerca?

### 4. Performance e Limiti

- Quanti file ci sono in `Library/Wiki/`? (misurare)
- grep su quanti MB?
- Timeout per query?
- Caching? (risultati recenti memorizzati)

### 5. Integrazione con Hermes

- Come cambia il system prompt di Hermes?
- Sostituisce l'accesso diretto ai file wiki nel contesto?
- Metriche di successo: ≥5 query/settimana dopo 2 settimane, ≥500 token risparmiati per query

### 6. Rischi Specifici

- **Grep lento su directory grande**: mitigare con limit path, index leggero?
- **Wiki in evoluzione**: i risultati cambiano nel tempo, caching problematico
- **Dipendenze**: il server richiede `grep` installato (su Linux sì, ma portabilità?)
- **Confine con handoff server**: se Option A, non mischiare logiche di orchestrazione

---

## Deliverable dell'Analisi

Al termine dell'analisi, produrre:

1. **Decisione architetturale** motivata (Option A o B)
2. **Specifica tool** completa: signature, parametri, output, errori
3. **Stima impatto** sul server handoff esistente (se Option A)
4. **Analisi rischi** con mitigazioni
5. **Raccomandazione** per la fase di Design Document

---

## Riferimenti

| Documento | Path |
|-----------|------|
| Roadmap MCP Consolidata | `Library/Wiki/concepts/2026/05/mcp-roadmap.md` |
| Handoff MCP server | `tools/handoff/` |
| Taskmanager MCP server (reference) | `tools/taskmanager/` |
| Wiki directory | `Library/Wiki/` |
| Email processor MCP (reference) | `tools/email_processor/` |
| OpenCode config (MCP servers) | `opencode.json` |

---

## Flow Proposto

```
Analisi (questa fase)
  │
  ├── Proteo → ricerca pattern esistenti per KB MCP, best practices
  ├── Pythagoras → academic research su knowledge retrieval per agenti
  ├── Metis → stress-test delle opzioni architetturali, pre-mortem
  │
  └── Hermes → consolidamento in Design Document (T-MCP-005)
         │
         └── Efesto → implementazione (T-MCP-006)
```

---

*Prompt preparato per l'avvio dell'analisi Fase 2 Knowledge Base MCP.*
*Task: T-MCP-004 | Parent: T-MCP-003*
