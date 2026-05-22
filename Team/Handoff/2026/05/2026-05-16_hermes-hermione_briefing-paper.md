---
data: 2026-05-16
mittente: hermes
destinatario: hermione
tipo: briefing
stato: in-esecuzione
priorita: alta
titolo: "Briefing — Whitepaper Team Olimpo"
---

# Briefing: Whitepaper Tecnico Team Olimpo

## 1. Obiettivo

Scrivere un whitepaper tecnico in **inglese** (~10-15 pagine, formato arXiv-ready) che descriva il Team Olimpo come sistema multi-agente con particolare focus su **AQF (Agent Qualification Framework)**, l'innovazione principale.

Titolo suggerito:  
**"Team Olimpo: An Agent Qualification Framework for Production-Ready Multi-Agent Systems"**

Pubblicazione target: arXiv (cs.AI / cs.MA), con successiva pubblicazione su GitHub Pages del repo `teamolimpo-paper`.

## 2. Anti-pattern (cosa NON fare)

- **Non scrivere in italiano** — tutto in inglese britannico/americano standard
- **Non usare toni promozionali/markettari** — deve essere un paper tecnico, serio, citabile
- **Non inserire informazioni sensibili** (email reali, dati personali, CV, strategie private) — solo concetti, architettura, pattern
- **Non usare link interni a file locali** — solo riferimenti pubblici o citazioni accademiche
- **Non superare 15 pagine** (arXiv limite ~10-12 pagine standard, massimo 15 per paper esteso)
- **Non dimenticare il frontmatter YAML** se il file è in Markdown
- **Non copiare testi da fonti senza citarle** — citare sempre Karpathy (LLM Wiki), Anthropic, OpenAI, paper rilevanti
- **Niente path assoluti** nelle immagini

## 3. Formato output

File: da salvare con naming `Library/Handoff/2026/05/2026-05-16_whitepaper-teamolimpo_v1.md`

Formato:
- Markdown con frontmatter YAML
- DOI e arXiv placeholder nel frontmatter
- Diagrammi Mermaid per architettura, flussi, AQF lifecycle
- Citazioni in formato accademico ([Autore, Anno] o [1], [2] con References in fondo)
- Sezioni numerate (1., 1.1, 2., etc.)

## 4. Struttura dettagliata

### Section 1: Abstract (150-200 parole)
- Problema: i sistemi multi-agente mancano di reliability, tracciabilità, e quality assurance
- Soluzione: Team Olimpo — architettura orchestrator-workers con handoff tracciabile, AQF (Agent Qualification Framework), knowledge persistence layer
- Risultati principali: 13 agenti operativi, 64+ handoff documentati, framework di qualifica a 5 fasi, knowledge compounding con ROI 6,7x
- Keywords: multi-agent systems, agent qualification, LLM wiki, agent factory, quality assurance

### Section 2: Introduction
- Contesto: l'esplosione dei sistemi multi-agente (AutoGPT, CrewAI, LangGraph, OpenAI Agents SDK)
- Problemi irrisolti:
  1. **Reliability**: come certificare che un agente fa ciò che deve?
  2. **Tracciabilità**: chi ha fatto cosa e quando?
  3. **Knowledge persistence**: come evitare che gli agenti dimentichino?
  4. **Agent creation**: come creare nuovi agenti in modo sistematico?
- Contributi del paper:
  1. AQF — framework di qualifica strutturato
  2. File-based handoff system con audit trail completo
  3. Agent Factory Pipeline per creazione sistematica
  4. LLM Wiki multi-agente adattato da Karpathy
  5. Multi-model orchestration nativa

### Section 3: System Architecture
- Presentazione del pattern orchestrator-workers
- Hermes come orchestratore puro: non esegue MAI, solo decompone, delega, sintetizza
- 13 agenti specializzati con ruoli distinti
- Tabella riassuntiva degli agenti (nome, ruolo, modello, classe di rischio AQF)
- Diagramma Mermaid: architettura generale
- Principio: separazione delle competenze, confini netti

### Section 4: The Handoff System
- Comunicazione asincrona basata su file Markdown
- Struttura: `Library/Handoff/YYYY/MM/data_mittente-destinatario_titolo.md`
- Frontmatter YAML: data, mittente, destinatario, tipo, stato, priorità
- Vantaggi: audit trail, recovery da crash, isolamento contesto, parallelismo
- Statistiche: ~64+ handoff prodotti, tempo medio ~5 minuti
- Diagramma Mermaid: flusso handoff (Hermes → agente → Hermes → utente)
- Confronto con altri approcci: comunicazione in-memory vs file-based

### Section 5: AQF — Agent Qualification Framework ★ (sezione principale)
- Ispirazione: standard farmaceutici FDA/EMA (IQ/OQ/PQ/CPV) + CSA (Computer Software Assurance)
- Le 5 fasi:
  1. **ADQ** (Agent Design Qualification): review del design/prompt/identità pre-creazione
  2. **AEQ** (Agent Environment Qualification): verifica ambiente, tool, permessi pre-esecuzione
  3. **AOQ** (Agent Operational Qualification): test su range di input (happy path, edge case, failure)
  4. **APQ** (Agent Performance Qualification): verifica output consistenti su task produttivi
  5. **ACM** (Agent Continuous Monitoring): deviation rate, quality trend, drift detection
- Risk classification: Alto/Medio/Basso → assurance proporzionale (principio CSA)
- Quality score composito: completezza (30%) + accuratezza (40%) + conformità (20%) + efficienza (10%)
- Deviation log strutturato con soglie di allarme
- Diagramma Mermaid: AQF lifecycle con fasi e gates
- Esempio concreto: qualifica di un nuovo membro (Eunomia)

### Section 6: Agent Factory Pipeline
- Processo sistematico di creazione di nuovi agenti:
  1. Hermes identifica dominio → 2. Proteo analizza e produce profilo competenze
  3. Hermes valuta → 4. Atena costruisce identità e prompt
  5. AQF gates → 6. Deploy e integrazione
- Separazione dei ruoli: chi analizza (Proteo) ≠ chi costruisce (Atena)
- Atena come HR Manager specializzato: design di personalità AI, architettura prompt, confini netti
- Template di file agente: struttura e sezioni obbligatorie
- Risultati: 13 agenti creati con questo processo
- Diagramma Mermaid: flusso Agent Factory con le 6 fasi

### Section 7: Knowledge Persistence — LLM Wiki + hot.md
- Pattern LLM Wiki (Karpathy, 2025) adattato a contesto multi-agente
- Struttura cronologica: `Library/Wiki/YYYY/MM/{concepts,decisions,research}/`
- hot.md: cache di contesto ~400 token con stato attuale
- Differenze chiave rispetto al pattern Karpathy:
  - Multi-autore: Hermes orchestra, Proteo contribuisce, Clio verifica
  - Audit trail: ogni operazione wiki tracciata via handoff
  - Quality gate: Clio + Dike per lint e verifica
  - Correzione incrociata: un agente corregge l'errore di un altro
- ROI calcolato: ~6,7x nel primo mese (70.440 token risparmiati su 10.490 investiti)
- hot.md ROI: ~9,6x (19.200 token risparmiati/mese su 2.000 investiti)

### Section 8: Multi-Model Orchestration
- 3 modelli LLM in uso simultaneo:
  - big-pickle per orchestrazione e task generali
  - xai/grok-4.3 per scrittura creativa (Euterpe)
  - sonnet (Claude) per analisi ambientale e catalogazione (Demetra, Eunomia)
- Routing basato sul tipo di task
- Nessun vendor lock-in: architettura agnostica rispetto al modello
- Lezioni apprese: come gestire formati di output diversi, quality variance tra modelli

### Section 9: Quality Assurance
- Sistema a più livelli:
  1. Hermes: checklist rapida 6 punti pre-accettazione
  2. Clio: gate di qualità specializzato per vault Obsidian
  3. Dike: audit, mappature, gap analysis
  4. ACM: monitoraggio continuo, deviation log, drift detection
- Metriche: deviation rate, quality score composito, OQ pass rate
- Soglie: deviation rate > 20% → notifica, > 40% → sospensione
- Schema deviation log: data, membro, tipo, descrizione, causa, azione, esito

### Section 10: Operational Results
- 13 agenti operativi
- 64+ handoff completati
- 3+ mesi di operatività continuativa
- Task completati: business plan, ricerca USA, progetto Tucson, audit AQF, wiki implementation, integrazione email, sviluppo CLI
- Metriche: parallelismo ha ridotto tempi del 50-90% su task multi-subtask
- Knowledge wiki: 10+ pagine, 3 categorie (concepts, decisions, research)
- Esempi di task complessi completati con successo (breve descrizione di 3-4 casi)

### Section 11: Related Work
- AutoGPT, CrewAI, LangGraph, OpenAI Agents SDK — confronto architetturale
- Karpathy LLM Wiki — confronto single-agent vs multi-agent
- AgentOrchestra (arXiv 2506.12508) — benchmark multi-agente
- Anthropic Multi-Agent Research System — pattern di ricerca parallela
- IQ/OQ/PQ in ambito farmaceutico (FDA 21 CFR Part 11, GAMP 5)

### Section 12: Conclusion & Future Work
- Team Olimpo dimostra che reliability e tracciabilità sono raggiungibili in sistemi multi-agente
- AQF è il contributo principale: un framework di qualifica che manca al settore
- Prossimi passi:
  - Automazione AQF: checklist in codice eseguibile
  - Scaling: GitHub Actions per CI/CD delle qualifiche
  - AQF come standard aperto: pubblicazione su arXiv, contributi esterni
  - espansione a più modelli (Grok, Gemini, DeepSeek)
  - Paper di follow-up su specifiche AQF

## 5. Fonti da consultare (leggere prima di scrivere)

1. `Library/Handoff/2026/05/2026-05-16_metis-hermes_caratteristiche-distintive-teamolimpo.md` — analisi completa Metis (508 righe)
2. `Library/Handoff/2026/05/2026-05-01_proteo-hermes_report_agent-architecture-comparison.md` — confronto architetturale
3. `Library/Handoff/2026/05/2026-05-16_dike-hermes_audit-adozione-aqf.md` — audit AQF
4. `Library/Handoff/2026/05/2026-05-11_metis-hermes_analisi-costi-benefici-llm-wiki.md` — ROI wiki
5. `Team/Members/Registro.md` — registro membri
6. `AGENTS.md` — descrizione progetto
7. `Library/Handoff/2026/05/2026-05-16_proteo-hermes_strategia-pubblicazione-paper.md` — strategia

## 6. Criteri di accettazione

- [ ] Paper completo in inglese, ~10-15 pagine
- [ ] Sezioni tutte presenti come da struttura
- [ ] Diagrammi Mermaid per: architettura, handoff flow, AQF lifecycle, Agent Factory
- [ ] Citazioni e references in formato accademico
- [ ] Frontmatter YAML valido
- [ ] Nessun dato sensibile o path assoluto
- [ ] Tonico tecnico, non promozionale
- [ ] AQF è la sezione più corposa e dettagliata
- [ ] File salvato in Library/Handoff/2026/05/2026-05-16_whitepaper-teamolimpo_v1.md
- [ ] Riferimenti a GitHub repo pubblico (segnaposto: creeremo repo dopo)
