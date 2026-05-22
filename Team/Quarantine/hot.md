---
title: "hot.md — Contesto Attivo del Team Olimpo"
tags: [meta, contesto, hot, team-olimpo]
cssclasses: [hot-context]
---

# hot.md — Contesto Attivo

Ultimo aggiornamento: 2026-05-16

## Stato attuale
- **Progetto corrente**: Fase 1 migliorie Team Olimpo — implementazione wiki layer ([[Library/Wiki/index.md]])
- **Task attivi**:
  - **T-WIKI-001** (Fase 1 wiki layer) — Hermione struttura wiki, Calliope hot.md, Clio guide, Hermes verifica finale. Subtask: WIKI-1 (struttura) in corso, WIKI-2 (hot.md) in corso, WIKI-3 (guide) in corso, WIKI-4 (verifica) pending
  - **T-EMAIL-001** (integrazione email vault) — Efesto subtask EMAIL-9 (script pulizia nomi .eml ENAMETOOLONG) in corso. Precedenti EMAIL 1-8 completati (migrazione Typer, creazione agente Clio/Eunomia, mapping vault, integrazione skills, fix path)
  - **T-XAI-001** (report xAI Terafactory) — Proteo subtask XAI-1 (ricerca posizioni aperte Memphis su X) in corso; XAI-2 (mapping con CV Stefano) e XAI-3 (sintesi Hermes) pending
- **Altri progetti**: Progetto Tucson (in pausa), Strategia IA 2026 (completata e archiviata su richiesta utente il 2026-05-16)
- **Membri coinvolti**: Hermione (wiki), Calliope (hot.md), Clio (guide/AGENTS), Efesto (email), Proteo (xAI)

## Decisioni recenti

| Decisione | Data | Stato |
|-----------|------|-------|
| Struttura cronologica YYYY/MM/ per wiki (concepts/decisions/research) | 2026-05-16 | ✅ Attiva |
| Wiki centralizzato unico (non wiki per agente) in Fase 1 | 2026-05-16 | ✅ Attiva |
| T-STRATEGIA-IA-001 archiviato su richiesta utente | 2026-05-16 | ✅ Attiva |
| .opencode/agents/ come fonte unica verità profili membri | 2026-05-06 | ✅ Attiva |
| Checklist validazione OpenCode obbligatoria per nuovi agenti | 2026-05-06 | ✅ Attiva |
| Migrazione progetti in cartella projects/ (tucson come pilota) | 2026-05-09 | ✅ Attiva |

## Ultime operazioni

1. **[2026-05-16]** Hermione — creata [[Library/Wiki/index.md]] + [[Library/Wiki/log.md]] + cartelle cronologiche `concepts/2026/05/`, `decisions/2026/05/`, `research/2026/05/`; seeding pagina [[Library/Wiki/concepts/2026/05/llm-wiki-pattern]]
2. **[2026-05-16]** Calliope — creazione [[Team/Meta/hot.md]] (questo file)
3. **[2026-05-16]** Clio — aggiornamento [[AGENTS.md]] (sezione Knowledge Wiki) e guide del team con riferimenti wiki (in corso)
4. **[2026-05-11]** Metis — [[Handoff/2026-05-11_metis-hermes_analisi-costi-benefici-llm-wiki|analisi costi-benefici 5 miglioramenti LLM Wiki]]: priorità Fase 1 (wiki layer + hot.md) > Fase 2 (wiki-summary su ogni ricerca) > Fase 3 (linking automatico). Costo medio stimato: 300-800 token/sessione Fase 1, 50-150 token/sessione Fase 2
5. **[2026-05-11]** Proteo — [[Handoff/2026-05-11_proteo-hermes_ricerca_llm-wiki-team-olimpo|ricerca LLM Wiki Karpathy]] completata: raccomandata struttura cronologica YYYY/MM/, index navigabile con summary, log operativo, e convenzione naming per pagine concettuali

## Domande aperte

- **Fase 2 wiki**: quando attivare wiki-summary obbligatorio in calce a ogni ricerca/conclusione? Servono una soglia minima di contenuti seed prima di imporre il formato, o si parte subito?
- **Linting wiki**: serve script periodico per verificare coerenza wikilink, frontmatter e assenza di pagine orfane dopo il seeding iniziale, o si procede manualmente su richiesta?
- **Priorità cross-task**: dopo consegna WIKI-001, quale sbloccare — T-EMAIL-001 (quasi completo, solo EMAIL-9 residuo) o T-XAI-001 (report xAI per decisioni utente)?
- **Tassonomia wiki**: servono tag/categorie oltre la struttura cronologica YYYY/MM/? La decisione è rimandata a Fase 2, ma utile iniziare a pensarne le implicazioni.

## Collegamenti rapidi

- [[Library/Wiki/index.md]]
- [[Library/Wiki/log.md]]
- [[Team/Hermes/Scratchpad.md]]
- [[Handoff/2026-05-11_metis-hermes_analisi-costi-benefici-llm-wiki.md]]
- [[Handoff/2026-05-11_proteo-hermes_ricerca_llm-wiki-team-olimpo.md]]
- [[AGENTS.md]]
