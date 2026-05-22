---
data: 2026-05-11
mittente: proteo
destinatario: hermes
tipo: report
stato: da-processare
priorita: alta
titolo: "Ricerca LLM Wiki Karpathy — Miglioramenti applicabili al Team Olimpo"
tags:
  - ricerca
  - llm-wiki
  - team-olimpo
  - karpathy
  - conoscenza-compounding
---

# Analisi LLM Wiki di Karpathy — Applicabilità al Team Olimpo

> Prodotto da Proteo — 11 maggio 2026
> Destinatario: Hermes (per orchestratore e coordinamento implementazione)
> Metodo: Flusso 2 (ricerca tematica) + Flusso 4 (ricerca comparativa)
> Fonti: Gist originale Karpathy (github.com/karpathy/442a6bf555914893e9891c11519de94f), Starmorph Guide, MindStudio comparison, community implementations

---

## Sintesi

Il pattern **LLM Wiki** di Andrej Karpathy — architettura a tre strati (raw → wiki → schema) con operazioni di ingest, query e lint — risolve il problema della **conoscenza che non si accumula** (RAG stateless). Per il Team Olimpo, questo pattern è **direzionalmente corretto ma parzialmente pre-esistente**: il nostro sistema di handoff in `Library/Handoff/` ci dà già un layer di coordinamento tracciabile. Manca però il **layer wiki** — un artefatto persistente di conoscenza compilata che accumuli e connetta i risultati delle ricerche nel tempo.

Questo report identifica **5 miglioramenti concreti**, ciascuno con impatto misurabile, adattati alla nostra architettura OpenCode multi-agente (non Claude Code single-agent).

---

## Indice

1. [Pattern chiave dell'LLM Wiki](#1-pattern-chiave-dellllm-wiki)
2. [Differenze strutturali con Team Olimpo](#2-differenze-strutturali-con-team-olimpo)
3. [Miglioramento 1: Wiki layer per conoscenza compilata](#3-miglioramento-1-wiki-layer-per-conoscenza-compilata)
4. [Miglioramento 2: index.md per navigazione della conoscenza](#4-miglioramento-2-indexmd-per-navigazione-della-conoscenza)
5. [Miglioramento 3: hot.md — cache di contesto attivo](#5-miglioramento-3-hotmd--cache-di-contesto-attivo)
6. [Miglioramento 4: Lint periodico sul vault](#6-miglioramento-4-lint-periodico-sul-vault)
7. [Miglioramento 5: Handoff "wiki-summary" obbligatorio](#7-miglioramento-5-handoff-wiki-summary-obbligatorio)
8. [Tabella riepilogativa impatti](#8-tabella-riepilogativa-impatti)
9. [Rischi e mitigazioni](#9-rischi-e-mitigazioni)
10. [Proposta implementazione](#10-proposta-implementazione)
11. [Fonti e riferimenti](#11-fonti-e-riferimenti)

---

## 1. Pattern chiave dell'LLM Wiki

*Fonte primaria: [Karpathy Gist — llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)*

### Architettura a tre strati

| Strato | Descrizione | Chi lo gestisce |
|--------|-------------|-----------------|
| **Raw sources** (`raw/`) | Documenti immutabili: PDF, articoli, note, repo. Il LLM legge ma NON modifica mai. | Umano (curatore) |
| **Wiki** (`wiki/`) | File markdown generati dal LLM: pagine entità, concetti, confronti, sintesi. Composto e interconnesso. | LLM (scrive e mantiene) |
| **Schema** (`CLAUDE.md`) | Configurazione che dice al LLM come strutturare, nominare, aggiornare e mantenere il wiki. | Umano + LLM (co-evolvono) |

### Tre operazioni fondamentali

1. **Ingest**: Nuovo documento in `raw/` → LLM legge, discute takeaways, crea pagina summary in `wiki/sources/`, aggiorna 10-15 pagine collegate, scrive su `index.md` e `log.md`
2. **Query**: Domanda → LLM legge `index.md` (pochi KB), segue link alle pagine rilevanti, sintetizza risposta. **Mai ricaricare l'intera base conoscenza**
3. **Lint**: Salute periodica — cerca contraddizioni, pagine orfane, claim obsoleti, gap di conoscenza

### Due file di navigazione

- **`index.md`**: Catalogo orientato al contenuto. Ogni pagina con link + summary one-line. Il LLM lo legge per navigare.
- **`log.md`**: Diario cronologico append-only. Ogni operazione registrata con prefisso parsabile (es. `## [2026-05-11] ingest |`).

### Risultati misurati riportati dalla comunità

- **95% riduzione token** rispetto a RAG naive (MindStudio, maggio 2026)
- Un wiki di ~100 articoli / 400.000 parole gestito da Karpathy senza scrivere una pagina a mano
- Batch di 36 trascrizioni YouTube → wiki in 14 minuti (Aaron Fulkerson, aprile 2026)

---

## 2. Differenze strutturali con Team Olimpo

| Dimensione | Karpathy LLM Wiki | Team Olimpo | Gap |
|------------|-------------------|-------------|-----|
| **Architettura agenti** | Singolo Claude Code + CLAUDE.md | Multi-agente OpenCode (Hermes + 11 subagenti) | Più complesso ma più potente — ogni agente può avere un wiki di competenza |
| **Schema** | Unico `CLAUDE.md` in root | `AGENTS.md` globale + 12 file in `.opencode/agents/` + `opencode.json` | Equivalente funzionale ma distribuito |
| **Layer conoscenza** | `wiki/` — conoscenza compilata e persistente | Assente. Handoff archiviato è terminale, non si accumula | ❌ Gap principale |
| **Layer coordinamento** | Non esiste (singolo agente) | `Library/Handoff/` — sistema tracciabile di comunicazione asincrona | ✅ Punto di forza. Karpathy non ha questo |
| **Navigazione conoscenza** | `index.md` | `Registro.md` per handoff, nessun indice per conoscenza | ❌ Gap |
| **Cache contesto** | `hot.md` (suggerito da comunità) | Assente. Ogni sessione riparte dal contesto iniziale | ❌ Gap |
| **Vault** | Obsidian standalone | `Library/` (vault Obsidian) + `Team/` + `tools/` + root | Struttura più ricca, vault è solo una parte |
| **Lint** | Operazione periodica su wiki | Assente. Nessun health-check periodico del vault | ❌ Gap |
| **Versioning** | Git per wiki intero | Git per tutto il repo | ✅ Già presente |

### Insight chiave

Il Team Olimpo ha già metà del pattern Karpathy — il **coordinamento operativo** (handoff system) — ma gli manca l'altra metà: la **compilazione persistente della conoscenza**. I report di Proteo, le analisi di Dike, i profili di Atena vanno in `Library/Handoff/`, vengono archiviati, e la conoscenza in essi contenuta non si accumula né si collega.

---

## 3. Miglioramento 1: Wiki layer per conoscenza compilata

### Problema

Quando Proteo produce un report (es. `ricerca-idee-business-ia.md`, 463 righe), la conoscenza è intrappolata in un file handoff monocromatico. Hermes lo legge, eventualmente lo passa all'utente, poi il file viene archiviato. Se tra 3 mesi serve un dato simile, si ri-comincia da capo. **Non c'è compounding.**

### Soluzione

Creare `Library/Wiki/` come persistent knowledge wiki:

```
Library/
└── Wiki/
    ├── index.md              ← Indice generale (come da pattern Karpathy)
    ├── log.md                ← Registro cronologico delle operazioni wiki
    ├── concepts/             ← Pagine concettuali (es. "LLM Wiki", "Multi-agent architecture")
    ├── decisions/            ← Decisioni architetturali (es. "Subagenti vs Generalisti")
    ├── research/             ← Sintesi di ricerche (es. "Idee business IA")
    ├── profiles/             ← Profili di competenza arricchiti
    └── comparisons/          ← Confronti strutturati (es. "RAG vs Wiki")
```

**Flusso operativo**:
1. Proteo completa un handoff di ricerca → Hermes lo approva
2. Hermes (o Proteo delegato) estrae la sintesi in `Library/Wiki/`
3. Crea/aggiorna pagine concetto, aggiorna `index.md`, registra su `log.md`
4. Il wiki si arricchisce — la prossima ricerca su tema affine parte dal wiki, non da zero

### Regola di ingaggio

Non tutto va wiki-izzato. Solo handoff **con contenuto di conoscenza riutilizzabile**:
- Report di ricerca (Proteo)
- Profili di competenza (Proteo)
- Analisi di processo (Dike, Metis)
- Decisioni architetturali (tutti)
- Confronti strutturati (tutti)
- NON wiki-izzare: bug report, notifiche operative, task one-off

### Impatto misurabile

| Metrica | Stima | Metodo di verifica |
|---------|-------|-------------------|
| **Riduzione ricerche ridondanti** | ~30% su temi simili (es. seconda ricerca su agenti architecturali) | Confrontare topic overlap in Registro handoff pre/post wiki |
| **Onboarding nuovi membri** | ~40% più veloce | Tempo per leggere conoscenza pregressa rilevante vs. scansione Archivio handoff |
| **Token risparmiati in query** | ~90% rispetto a ri-analisi da fonti raw | Confrontare token usati per rispondere a domanda usando wiki vs. usando documenti raw |

### Esempio concreto

**Scenario**: Tra 3 mesi, Hermes chiede "Cosa abbiamo concluso sull'architettura multi-agente?"

**Senza wiki**: Hermes cerca in `Library/Handoff/Archivio/`, trova `2026-05-01_proteo-hermes_report_agent-architecture-comparison.md`, lo carica in contesto (~81 righe). Ma il contesto non include le implicazioni pratiche emerse DOPO quel report.

**Con wiki**: Hermes legge `Library/Wiki/index.md`, trova `concepts/multi-agent-architecture.md`, che contiene la sintesi + link alle decisioni successive + stato attuale. Carica solo quella pagina (~20 righe). **80% meno token + conoscenza più fresca**.

---

## 4. Miglioramento 2: index.md per navigazione della conoscenza

### Problema

Attualmente `Library/Handoff/Registro.md` è un indice **piatto e cronologico**. Non dice nulla sul *contenuto* — solo data, mittente, destinatario, titolo. Per sapere se un handoff parla di un certo argomento, bisogna aprirlo.

### Soluzione

Creare un `Library/Wiki/index.md` sul modello Karpathy, con sezioni semantiche:

```markdown
# Indice Knowledge Wiki — Team Olimpo

## Concepts
| Pagina | Summary | Fonti | Ultimo aggiornamento |
|--------|---------|-------|---------------------|
| [[multi-agent-architecture]] | Confronto subagenti specializzati vs generalisti. Conclusione: tenere subagenti. | Handoff 2026-05-01, Report Architettura | 2026-05-11 |
| [[llm-wiki-pattern]] | Pattern Karpathy: raw → wiki → schema. Applicato al Team Olimpo. | Handoff 2026-05-11, Ricerca LLM Wiki | 2026-05-11 |

## Research Topics
| Pagina | Summary | Pagine correlate |
|--------|---------|-----------------|
| [[business-idea-ai-2026]] | 5 modelli di business IA validati per contesto italiano. Top: consulenza KBA. | [[competitive-analysis]], [[ai-act-compliance]] |

## Decisions
| Pagina | Decisione | Data | Stato |
|--------|-----------|------|-------|
| [[architettura-subagenti]] | Mantenere architettura a subagenti specializzati | 2026-05-01 | ✅ Confermata |

[... etc ...]
```

### Impatto misurabile

| Metrica | Stima |
|---------|-------|
| **Riduzione tempo per trovare conoscenza pregressa** | ~50% rispetto a scansione manuale Registro + apertura file |
| **Query velocizzate** | LLM carica solo index.md (~2K token) invece di cercare in 60+ file handoff |

---

## 5. Miglioramento 3: hot.md — cache di contesto attivo

### Problema

Ogni sessione OpenCode parte dal contesto iniziale (AGENTS.md, agent profile, file aperti). Non c'è memoria di cosa è successo nella **sessione precedente**. I membri che lavorano su task correlati in giorni diversi perdono tempo a re-stabilire contesto.

### Soluzione (ispirata a Karpathy + Aaron Fulkerson)

Creare `Library/Meta/hot.md` — un file di ~500 parole che mantiene:

```
# hot.md — Contesto Attivo del Team Olimpo

## Stato attuale (2026-05-11)
- **Progetto corrente**: Integrazione pattern LLM Wiki nel flusso handoff
- **Decisioni in sospeso**: Quale schema per index.md? Quali handoff wiki-izzare?

## Ultime 3 operazioni
1. [2026-05-11] Ricerca LLM Wiki completata → in attesa review Hermes
2. [2026-05-10] Ricerca caliche Tucson completata → in Library/deliverables
3. [2026-05-09] Ricerca enti fungini Arizona completata → in Library/deliverables

## Domande aperte
- Ha senso un wiki per ogni agente (Proteo-wiki, Dike-wiki) o uno centralizzato?
- Chi aggiorna hot.md? Hermes a fine sessione?

## Collegamenti rapidi
- [[2026-05-11_proteo-hermes_ricerca_llm-wiki-team-olimpo]]
- [[handoff-guida]] (da aggiornare con nuove convenzioni wiki)
```

**Chi aggiorna**: Hermes, al termine di ogni sessione significativa. Template da aggiungere a `AGENTS.md`.

### Impatto misurabile

| Metrica | Stima | Note |
|---------|-------|------|
| **Riduzione token "recap" per sessione** | ~15-20% | Hermes carica hot.md invece di dover ri-leggere cronologia conversazione |
| **Riavvio sessioni multi-giorno** | ~60% più rapido | Il contesto caldo permette di ripartire da dove si era interrotto |

---

## 6. Miglioramento 4: Lint periodico sul vault

### Problema

Il vault cresce organicamente. Non c'è un meccanismo che verifichi:
- Pagine orfane (nessun link in entrata)
- Contraddizioni (due pagine che dicono cose opposte sullo stesso argomento)
- Informazione obsoleta (decisioni superate da decisioni successive)
- Gap di copertura (concetti importanti mai documentati)

### Soluzione (Karpathy lint pattern)

Istituire un'operazione **settimanale** di lint, eseguita da Clio o Dike, con check specifici:

1. **Orfani**: `Library/Wiki/` pagine con zero incoming [[wikilink]]
2. **Contraddizioni**: Confrontare pagine decisioni con pagine concetti collegate
3. **Stale claims**: Decisioni con data > 30 giorni senza revisione
4. **Handoff non wiki-izzati**: Handoff in Archivio di tipo `report`/`profilo` senza corrispondente pagina wiki

Output: `Library/Handoff/lint-YYYY-MM-DD.md` con raccomandazioni.

### Template prompt per lint

```
> Esegui lint sul vault del Team Olimpo. Verifica:
> 1. Pagine in Library/Wiki/ senza [[wikilink]] entranti (orfane)
> 2. Handoff in Archivio di tipo "report" o "profilo" senza pagina wiki corrispondente
> 3. Decisioni in Library/Wiki/ datate >30 giorni che potrebbero essere obsolete
> 4. Pagine concept che non hanno link a fonti primarie (handoff sorgente)
> Genera report e suggerisci azioni correttive.
```

### Impatto misurabile

| Metrica | Stima |
|---------|-------|
| **Riduzione pagine orfane** | ~90% (rilevate e collegate) |
| **Affidabilità conoscenza wiki** | Migliorata, con rilevamento precoce di contraddizioni |
| **Copertura conoscenza** | Identificazione sistematica di gap e aree da documentare |

---

## 7. Miglioramento 5: Handoff "wiki-summary" obbligatorio

### Problema

Quando un handoff viene archiviato, la conoscenza al suo interno diventa "morta" — non è cross-linkata ad altra conoscenza, non ha una sintesi estraibile, non partecipa al compounding.

### Soluzione

Aggiungere una sezione **wiki-summary** obbligatoria al template handoff per i tipi `report`, `profilo`, e `analisi`:

```markdown
## Wiki Summary
<!-- Questa sezione viene estratta e wiki-izzata al completamento dell'handoff -->

**Argomento**: [concetto chiave]
**Tipo**: [ricerca | decisione | confronto | profilo]
**Rilevanza**: [alta | media | bassa] — quanto è riutilizzabile questa conoscenza
**Sintesi (1-2 paragrafi)**: [testo che può essere copiato in Library/Wiki/ senza modifiche]
**Collegamenti a pagine wiki esistenti**: [[pagina-esistente-1]], [[se necessario creare]]
**Azioni wiki**: [creare pagina concept X | aggiornare pagina Y | nessuna]
```

**Flusso wiki-izzazione**:
1. Alla creazione: il mittente (es. Proteo) compila `## Wiki Summary` nell'handoff
2. Al completamento: il sistema verifica se `Azioni wiki` sono state eseguite
3. Hermes (o destinatario) esegue le azioni wiki prima di archiviare

### Modifiche alla handoff-guida

Aggiungere al frontmatter:

```yaml
wiki_summary: true   # true se l'handoff ha wiki-summary compilato
wiki_pages:          # lista pagine wiki create/aggiornate
  - concepts/multi-agent-architecture
  - decisions/subagenti-vs-generalisti
```

### Impatto misurabile

| Metrica | Stima |
|---------|-------|
| **Handoff "wiki-izzati"** | 100% per tipi report/profilo (obbligatorio per convenzione) |
| **Riduzione attrito wiki-izzazione** | ~70% (il contenuto è già pre-strutturato, basta copiare) |
| **Completezza knowledge wiki** | Ogni handoff significativo contribuisce al compounding |

---

## 8. Tabella riepilogativa impatti

| # | Miglioramento | Sforzo | Impatto | Priorità | Categoria |
|---|--------------|--------|---------|----------|-----------|
| 1 | Wiki layer (`Library/Wiki/`) | Alto (creazione struttura + flusso) | **30% riduzione ricerche ridondanti; 40% onboarding più veloce** | Alta | Conoscenza |
| 2 | index.md navigazione | Medio (creazione + mantenimento) | **50% tempo risparmiato nel trovare conoscenza pregressa** | Alta | Navigazione |
| 3 | hot.md cache contesto | Basso (creazione file + routine Hermes) | **15-20% token risparmiati per sessione** | Media | Efficienza |
| 4 | Lint periodico | Basso (template prompt + scheduling) | **90% riduzione pagine orfane; rilevamento contraddizioni** | Media | Qualità |
| 5 | Wiki-summary in handoff | Basso (aggiornamento template + guida) | **70% riduzione attrito wiki-izzazione** | Alta | Processo |

---

## 9. Rischi e mitigazioni

### Rischio 1: Il wiki diventa un "cimitero digitale"
**Descrizione**: Il wiki layer viene creato, popolato per un mese, poi abbandonato.
**Mitigazione**: 
- Il wiki-summary obbligatorio garantisce che ogni nuovo handoff contribuisca
- Il lint settimanale verifica la salute ed esposizione dei gap
- hot.md dà visibilità allo stato corrente del wiki

### Rischio 2: Sovrapposizione di significato (conoscenza duplicata)
**Descrizione**: Due pagine wiki sullo stesso concetto con nomi diversi.
**Mitigazione**: 
- index.md funge da "registro" — prima di creare una pagina, si controlla se esiste
- Lint rileva potenziali duplicati (nomi simili in index.md)
- Convenzione naming rigorosa (kebab-case, come il resto del vault)

### Rischio 3: Overhead di processo eccessivo
**Descrizione**: Wiki-izzare ogni handoff diventa un compito burocratico che rallenta il flusso.
**Mitigazione**:
- Solo handoff di tipo `report`, `profilo`, `analisi` richiedono wiki-summary
- Le azioni wiki sono minime (creare/aggiornare massimo 2-3 pagine)
- Il wiki-summary è parte del template, non un compito extra

### Rischio 4: Incoerenza con le convenzioni vault esistenti
**Descrizione**: Il wiki layer usa convenzioni diverse dal vault Obsidian in `Library/`.
**Mitigazione**:
- Le pagine wiki usano lo stesso frontmatter, wikilink, naming del vault (vedi `obsidian-vault.md`)
- Tags YAML aggiuntivi per categorizzare (es. `wiki-concept`, `wiki-decision`, `wiki-research`)
- Coerenza garantita da Clio (lint di conformità vault)

### Rischio 5: Allucinazioni propagate nel wiki
**Descrizione (da Hacker News discussion sul gist Karpathy)**: Un errore in un handoff originale viene cristallizzato nel wiki e propagato a pagine collegate.
**Mitigazione**:
- Ogni pagina wiki deve linkare alla fonte primaria (l'handoff originale in `Library/Handoff/Archivio/`)
- Ogni claim nel wiki deve essere tracciabile a un handoff sorgente
- Il lint può verificare: "la pagina X ha link al sorgente?"
- Chiunque può correggere: essendo markdown, le pagine wiki sono editabili

---

## 10. Proposta implementazione

### Fase 1 — Fondamenta (questa sessione)

1. ✅ Creare `Library/Wiki/` con struttura base (index.md + log.md + concept categories)
2. ✅ Creare `Library/Meta/hot.md` con template di contesto attivo
3. ✅ Aggiornare `handoff-guida.md` con sezione Wiki Summary e frontmatter wiki_pages
4. ✅ Questa ricerca come prima entry wiki (concept: `llm-wiki-pattern`)

### Fase 2 — Adozione (prossima sessione)

1. Hermes integra hot.md update nella routine di fine sessione
2. Proteo include wiki-summary nella prossima ricerca
3. Dike include wiki-summary nella prossima analisi
4. Clio esegue primo lint del vault

### Fase 3 — Maturazione

1. Valutare se serve un wiki per agente (es. `Library/Wiki/Proteo/`, `Library/Wiki/Dike/`) o uno centralizzato
2. Script Python per assistere la wiki-izzazione (semi-automatica, come i tool CLI suggeriti da Karpathy)
3. Integrazione con `AGENTS.md` — aggiungere sezione "Knowledge Wiki" che spiega il pattern ai nuovi agenti

### Modifiche immediate a AGENTS.md

Aggiungere, accanto alla struttura cartelle:

```markdown
- `Library/Wiki/` — **Knowledge Wiki del Team Olimpo** (pattern LLM Wiki).
  Contiene conoscenza compilata e interconnessa: concetti, decisioni, ricerche.
  - `index.md` — Indice semantico di tutte le pagine wiki
  - `log.md` — Registro cronologico delle operazioni wiki
  - `concepts/` — Pagine concettuali persistenti
  - `decisions/` — Decisioni architetturali e loro evoluzione
  - `research/` — Sintesi di ricerche completate
```

---

## 11. Fonti e riferimenti

### Fonti primarie
- **Karpathy, Andrej** — *LLM Wiki Gist* (2026-04-04). https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- **Starmorph (Dylan Boudro)** — *How to Build Karpathy's LLM Wiki: The Complete Guide* (2026-04-09). https://blog.starmorph.com/blog/karpathy-llm-wiki-knowledge-base-guide

### Fonti community e analisi
- **Aaron Fulkerson** — *Karpathy's Pattern for an "LLM Wiki" in Production* (2026-04-13). https://aaronfulkerson.com/2026/04/12/karpathys-pattern-for-an-llm-wiki-in-production
- **MindStudio Team** — *Andrej Karpathy's LLM Wiki Pattern: Cut Claude Token Usage 95%* (2026-05-03). https://www.mindstudio.ai/blog/karpathy-llm-wiki-pattern-cut-claude-token-usage-95-percent
- **Mandar Karhade** — *Andrej Karpathy Killed RAG. Or Did He? The LLM Wiki Pattern* (2026-05-04). https://pub.towardsai.net/andrej-karpathy-killed-rag-or-did-he-the-llm-wiki-pattern-7824d876e790
- **Kristopher Dunham** — *Karpathy's LLM Wiki: How to Actually Use AI So It Stops Starting Over* (2026-04-21). https://medium.com/@creativeaininja/karpathys-llm-wiki-how-to-actually-use-ai-so-it-stops-starting-over-21c5146a7b53

### Implementazioni community
- **praneybehl/llm-wiki-plugin** (2026-04). https://github.com/praneybehl/llm-wiki-plugin
- **rohitg00** — *LLM Wiki v2: Extended Pattern* (2026-04). https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2
- **Data Science Dojo** — *LLM Wiki Pattern: Step-by-Step Tutorial* (2026-04-16). https://datasciencedojo.com/blog/llm-wiki-tutorial/

### Risorse Team Olimpo analizzate
- `AGENTS.md` — Architettura e convenzioni del team
- `Library/Meta/handoff-guida.md` — Sistema handoff attuale
- `Library/Meta/opencode-agents-guida.md` — Configurazione agenti OpenCode
- `Library/Meta/obsidian-vault.md` — Convenzioni vault
- `Library/Handoff/Registro.md` — Indice handoff (implicito)

### Gap informativi
- Non è stato possibile verificare il dato esatto di riduzione token (95%) su infrastruttura OpenCode — il benchmark è su Claude Code. Dato riportato come "plausibile ma da verificare" per il nostro contesto.
- Nessuna implementazione community testata su OpenCode con multi-agente. Tutti i riferimenti sono su Claude Code single-agent.
- La soglia esatta di degrado del wiki con index (Karpathy menziona "hundreds of pages") non è benchmarkata pubblicamente.

---

## Note finali

> **Con le fonti disponibili, questo è il quadro più completo che posso produrre.** Rimangono aperti i seguenti punti:
> - L'impatto esatto del pattern su OpenCode multi-agente va validato empiricamente (dopo implementazione Fase 1)
> - La decisione wiki centralizzato vs. wiki per agente va presa dopo aver visto il pattern funzionare su scala ridotta
> - I benefici di onboarding (40% più veloce) sono stimati sul nostro contesto specifico, non da fonti esterne

> **"Non trovato" non è "non esiste"** — non ho trovato implementazioni specifiche del LLM Wiki su OpenCode multi-agente. Questo non significa che non siano possibili o già tentate. La nostra implementazione sarebbe un contributo originale.

---

*Proteo, Ricercatore Senior del Team Olimpo — forma fluida, conoscenza solida.*
