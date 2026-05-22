---
data: '2026-05-21'
timestamp: '2026-05-21T01:25:50'
agent: clio
invocation: 6
type: report
status: completed
priority: medium
title: Verify format batch — 9 agenti
task_id: T-REVISIONE-027
---

## Summary

Verdict: **PASS WITH NOTES**
Failures: 2
Notes: 9

Two decorative `---` lines issues (Atena, Metis) — structural but not functional failures. No blocking issues found. All frontmatter valid, all member files correct, all dependencies agent-free, all descriptions operational and in English, all references sections present (including Dike, now restored).

---

## Per-agent results

### Proteo

#### `.opencode/agents/proteo.md`
- ✅ description: 175 chars, operativa, inglese, senza nomi agenti
- ✅ mode: subagent
- ✅ model: opencode/big-pickle
- ✅ permission: edit (Team/Proteo), read, webfetch, websearch — proporzionale al ruolo
- ✅ No campi custom frontmatter
- ✅ Header: 2 righe (# Proteo — Senior Researcher, Team Olimpo + body line)
- ✅ Istruzioni nel body: presenti
- ✅ Prompt Minimal Standard: no righe decorative, auto-revisionato
- ✅ Sezioni complete: frontmatter, header, identity, comm style, operating rules, competencies (4), workflows (4 flow), interactions, limitations, references
- ✅ Nessun nome di agente nel body

#### `Team/Members/proteo.md`
- ✅ Frontmatter: type: member, agent: proteo, role: senior-researcher
- ✅ Title: # Proteo — Team Olimpo
- ✅ Sections: Identity, Values, Boundaries, Dependencies
- ✅ Inglese
- ✅ Dependencies: solo tool/SOP/datasource (WebSearch, WebFetch, handoff-guide), nessun agente

---

### Atena

#### `.opencode/agents/atena.md`
- ✅ description: ~165 chars, operativa, inglese, senza nomi agenti
- ✅ mode: subagent
- ✅ model: opencode/big-pickle
- ✅ permission: edit (.opencode/agents, Team/Atena), read — proporzionale
- ✅ No campi custom frontmatter
- ✅ Header: 2 righe
- ✅ Istruzioni nel body: presenti
- ❌ **Prompt Minimal Standard violato**: decorative `---` righe orizzontali alle righe 26, 37, 48, 60. Rimuovere per conformità Prompt Minimal Standard.
- ✅ Sezioni complete: frontmatter, header, identity, comm style, operating rules, competencies, workflows, interactions/limits, references
- ✅ Nessun nome di agente nel body

#### `Team/Members/atena.md`
- ✅ Frontmatter: type: member, agent: atena, role: agent-designer
- ✅ Title: # Atena — Team Olimpo
- ✅ Sections: Identity, Values, Boundaries, Dependencies
- ✅ Inglese
- ✅ Dependencies: solo SOP/datasource, nessun agente

---

### Efesto

#### `.opencode/agents/efesto.md`
- ✅ description: 155 chars, operativa, inglese, senza nomi agenti
- ✅ mode: subagent
- ✅ model: opencode/big-pickle
- ✅ permission: bash, edit (tools, Team/Efesto), read — proporzionale al ruolo dev
- ✅ No campi custom frontmatter
- ✅ Header: 2 righe
- ✅ Istruzioni nel body: presenti
- ✅ Prompt Minimal Standard: no righe decorative, auto-revisionato
- ⚠️ **Sezioni con nomi non standard**: "Rules" (→ Operating Rules), "Skills" (→ Competencies), "Workflow" (→ Workflows), "Limits" (→ Limitations). Contenuto presente ma nomenclatura fuori standard.
- ✅ Nessun nome di agente nel body
- ✅ References: presenti

#### `Team/Members/efesto.md`
- ✅ Frontmatter: type: member, agent: efesto, role: python-developer
- ✅ Title: # Efesto — Team Olimpo
- ✅ Sections: Identity, Values, Boundaries, Dependencies
- ✅ Inglese
- ✅ Dependencies: solo tool/SOP (uv, tools/_template, handoff-guide), nessun agente

---

### Hermes

#### `.opencode/agents/hermes.md`
- ✅ description: 183 chars, operativa, inglese, senza nomi agenti
- ✅ mode: primary
- ✅ model: opencode/big-pickle
- ✅ permission: edit/read/task/write — proporzionale al ruolo orchestrator
- ✅ No campi custom frontmatter
- ✅ Header: 2 righe
- ✅ Istruzioni nel body: presenti
- ✅ Prompt Minimal Standard: no righe decorative, auto-revisionato
- ✅ Sezioni complete: frontmatter, header, identity, comm style, operating rules, competencies, workflows (dettagliato), interactions, limitations, references
- ✅ Nessun nome di agente nel body

#### `Team/Members/hermes.md`
- ✅ Frontmatter: type: member, agent: hermes, role: orchestrator
- ✅ Title: # Hermes — Team Olimpo
- ✅ Sections: Identity, Values, Boundaries, Dependencies
- ✅ Inglese
- ✅ Dependencies: solo tool/SOP (MCP tools, SOPs), nessun agente

---

### Hermione

#### `.opencode/agents/hermione.md`
- ✅ description: ~188 chars, operativa, inglese, senza nomi agenti
- ✅ mode: subagent
- ✅ model: opencode/big-pickle
- ✅ permission: edit (Library/documents, Team/Hermione), read — proporzionale
- ✅ No campi custom frontmatter
- ⚠️ **Header title**: "# Hermione — Deep Technical Writer" — manca "Team Olimpo" nel titolo (presente solo in Identity)
- ✅ Istruzioni nel body: presenti
- ✅ Prompt Minimal Standard: no righe decorative, auto-revisionato
- ⚠️ **Sezione "Operational Process"** usata al posto di "Workflows" — contenuto presente, nome non standard
- ⚠️ **"Deep" technical writer** — aggettivo potenzialmente decorativo, ma è parte del titolo stabilito
- ✅ Nessun nome di agente nel body
- ✅ References: presenti (obsidian-vault-conventions, handoff-guide)

#### `Team/Members/hermione.md`
- ✅ Frontmatter: type: member, agent: hermione, role: technical-writer
- ✅ Title: # Hermione — Team Olimpo
- ✅ Sections: Identity, Values, Boundaries, Dependencies
- ✅ Inglese
- ✅ Dependencies: solo SOP (obsidian-vault-conventions, handoff-guide), nessun agente

---

### Metis

#### `.opencode/agents/metis.md`
- ✅ description: ~173 chars, operativa, inglese, senza nomi agenti
- ✅ mode: all
- ✅ model: opencode/big-pickle
- ✅ permission: edit (Team/Metis, Library/deliverables), read — proporzionale
- ✅ No campi custom frontmatter
- ✅ Header: 3 righe (title + 2 body lines)
- ✅ Istruzioni nel body: presenti
- ❌ **Prompt Minimal Standard violato**: decorative `---` righe orizzontali alle righe 26, 46, 57, 77, 87. Rimuovere per conformità.
- ✅ Sezioni complete: frontmatter, header, identity, comm style, operating rules, competencies, workflows (0-5), interactions, limitations, references
- ✅ Nessun nome di agente nel body

#### `Team/Members/metis.md`
- ✅ Frontmatter: type: member, agent: metis, role: thinking-partner
- ✅ Title: # Metis — Team Olimpo
- ✅ Sections: Identity, Values, Boundaries, Dependencies
- ✅ Inglese
- ✅ Dependencies: User, SOPs (agent-design-methodology, handoff-guide), nessun agente

---

### Dike

#### `.opencode/agents/dike.md`
- ✅ description: ~189 chars, operativa, inglese, senza nomi agenti
- ✅ mode: subagent
- ✅ model: opencode/big-pickle
- ✅ permission: edit (kba_catalog, Team/Dike), read — proporzionale
- ✅ No campi custom frontmatter
- ✅ Header: 3 righe (title + 2 body lines)
- ✅ Istruzioni nel body: presenti
- ✅ Prompt Minimal Standard: no righe decorative, auto-revisionato
- ✅ **References presenti e corrette** (handoff-guide, agent-design-methodology) — confermo che il fix è stato applicato correttamente dopo l'errore di Atena
- ⚠️ Sezioni top-level non standard: "Competency Domain: Industrial Automation", "Risk Scoring Framework", "Classification & Scoring Criteria" come sezioni extra. Contenuto presente e dettagliato, ma struttura molto estesa (281 righe) — proporzionale alla complessità del dominio
- ✅ Nessun nome di agente nel body

#### `Team/Members/dike.md`
- ✅ Frontmatter: type: member, agent: dike, role: kba-risk-analyst
- ✅ Title: # Dike — Team Olimpo
- ✅ Sections: Identity, Values, Boundaries, Dependencies
- ✅ Inglese
- ✅ Dependencies: solo datasource/SOP (KBA docs, kba_catalog, handoff-guide), nessun agente

---

### Eunomia

#### `.opencode/agents/eunomia.md`
- ✅ description: ~195 chars, operativa, inglese, senza nomi agenti
- ✅ mode: subagent
- ✅ model: opencode/big-pickle
- ✅ permission: edit (Team/Eunomia), read — proporzionale
- ✅ No campi custom frontmatter
- ⚠️ **Header title**: "# Eunomia — Contextual Analyst" — manca "Team Olimpo" nel titolo (presente solo in Identity)
- ✅ Istruzioni nel body: presenti
- ✅ Prompt Minimal Standard: no righe decorative, auto-revisionato
- ⚠️ **Riga 11**: linea vuota extra dopo frontmatter
- ⚠️ **"Interactions & Limits"** è una sezione combinata — la specifica richiede sezioni separate Interactions/Limitations
- ✅ Nessun nome di agente nel body
- ✅ References: presenti

#### `Team/Members/eunomia.md`
- ✅ Frontmatter: type: member, agent: eunomia, role: contextual-analyst
- ✅ Title: # Eunomia — Team Olimpo
- ✅ Sections: Identity, Values, Boundaries, Dependencies
- ✅ Inglese
- ✅ Dependencies: solo tool/SOP (email_processor, context sources, handoff-guide), nessun agente

---

### Pythagoras

#### `.opencode/agents/pythagoras.md`
- ✅ description: ~187 chars, operativa, inglese, senza nomi agenti
- ✅ mode: subagent
- ✅ model: opencode/big-pickle
- ✅ permission: edit (Library/documents, Team/Pythagoras), read, webfetch, websearch — proporzionale
- ✅ No campi custom frontmatter
- ✅ Header: 2 righe
- ✅ Istruzioni nel body: presenti
- ✅ Prompt Minimal Standard: no righe decorative, auto-revisionato
- ✅ Sezioni complete: frontmatter, header, identity, comm style, operating rules (6), competencies (4), workflows (5 numbered + I/O), output format, interactions, limitations (5), references
- ✅ Nessun nome di agente nel body

#### `Team/Members/pythagoras.md`
- ✅ Frontmatter: type: member, agent: pythagoras, role: academic-researcher
- ✅ Title: # Pythagoras — Team Olimpo
- ✅ Sections: Identity, Values, Boundaries, Dependencies
- ✅ Inglese
- ✅ Dependencies: solo tool/SOP (WebSearch, WebFetch, obsidian-vault-conventions, handoff-guide), nessun agente

---

## Cross-checks

- ✅ **No sovrapposizione Core Rules/Guiding Principles**: nessun file ha entrambi. Tutti usano "Operating Rules" (o "Rules") come sezione unica.
- ✅ **Aggettivi decorativi**: nessun "expert", "master", "guru", "ninja" trovato. "Deep" in Hermione è parte del titolo stabilito; segnalato come nota.
- ✅ **YAML frontmatter parsabile**: tutti i file hanno frontmatter YAML valido.
- ✅ **Inglese ovunque**: tutti i file sono in inglese.
- ✅ **Dike References**: presenti e corrette (handoff-guide, agent-design-methodology). Fix Atena confermato.
- ✅ **Registro.md**: contiene righe per tutti e 9 gli agenti verificati, con Date, Agent, Version, Notes.

---

## Detailed failure breakdown

| # | Agente | File | Issue | Severity |
|---|--------|------|-------|----------|
| 1 | Atena | `.opencode/agents/atena.md` | 4 decorative `---` righe (ll. 26, 37, 48, 60) | ❌ Failure |
| 2 | Metis | `.opencode/agents/metis.md` | 5 decorative `---` righe (ll. 26, 46, 57, 77, 87) | ❌ Failure |
| 3 | Efesto | `.opencode/agents/efesto.md` | Nomi sezioni non standard (Rules/Skills/Workflow/Limits) | ⚠️ Note |
| 4 | Hermione | `.opencode/agents/hermione.md` | Manca "Team Olimpo" nell'header title | ⚠️ Note |
| 5 | Hermione | `.opencode/agents/hermione.md` | "Operational Process" invece di "Workflows" | ⚠️ Note |
| 6 | Hermione | `.opencode/agents/hermione.md` | "Deep" come aggettivo nel titolo | ⚠️ Note |
| 7 | Eunomia | `.opencode/agents/eunomia.md` | Manca "Team Olimpo" nell'header title | ⚠️ Note |
| 8 | Eunomia | `.opencode/agents/eunomia.md` | Sezione "Interactions & Limits" combinata | ⚠️ Note |
| 9 | Eunomia | `.opencode/agents/eunomia.md` | Riga vuota extra dopo frontmatter (l. 11) | ⚠️ Note |
| 10 | Dike | `.opencode/agents/dike.md` | Struttura sezioni non standard (281 righe, sezioni dominio-specifiche top-level) | ⚠️ Note |
| 11 | Dike | `.opencode/agents/dike.md` | Nessun riferimento a obsidian-vault-conventions pur scrivendo file con frontmatter | ⚠️ Note |
