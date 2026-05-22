---
title: "Review Parallela: [Titolo Oggetto della Review]"
date: '2026-05-04'
tags: [review, parallela, metis, proteo, team-olimpo]
reviewer1: "Metis"
reviewer2: "Proteo"
output_id: "REV-[YYYYMMDD]-[TIPO]-[ID]"
status: "in-corso"
priority: "media"
---

# Review Parallela: [Titolo Oggetto]

> **Scopo**: Documento strutturato per analisi parallela da parte di due reviewer (tipicamente Metis per strategia/processi e Proteo per ricerca/analisi dominio). Integrato con checklist per validazione vault Obsidian (Clio).

---

## 📋 Metadati Operativi

| Campo | Valore | Note |
|-------|--------|------|
| **Oggetto della Review** | [Es. Script Python Efesto / Profilo Nuovo Membro / Guida pdf_converter] | |
| **Richiesto da** | [Hermes / Atena / Efesto] | |
| **Data inizio** | `{{date}}` | |
| **Scadenza** | [YYYY-MM-DD] | |
| **Output atteso** | [Decisione Finale / Merge / Revisione] | |

---

## 🎯 Executive Summary

> **Istruzioni**: Sintesi unificata delle conclusioni dei due reviewer. Massimo 5-7 righe.

### Sintesi Metis (Strategia & Processi)
- **Obiettivo**: [Obiettivo strategico dell'oggetto]
- **Coerenza Team**: [Valutazione coerenza con architettura Team Olimpo]
- **Rischi strategici**: [Eventuali rischi di posizionamento o flusso]

### Sintesi Proteo (Ricerca & Dominio)
- **Dominio analizzato**: [Es. Python CLI, HR Profiling, PDF Processing]
- **Completezza**: [Grado di copertura del dominio]
- **Fonti consultate**: [Lista fonti o metodologia di ricerca]

### Sintesi Unificata
[Sintesi congiunta: il lavoro è pronto per l'integrazione? Quali sono i punti chiave emersi?]

---

## ✅ Punti di Forza

> **Istruzioni**: Elencare i punti di forza emersi dall'analisi parallela. Usare checkbox per tracciabilità.

### Metis (Strategia)
- [ ] **Allineamento Architetturale**: [Es. "Rispetta il pattern orchestrator-workers"]
- [ ] **Scalabilità**: [Es. "Facilita l'integrazione di nuovi agenti"]
- [ ] **Efficienza Processi**: [Es. "Riduce i passaggi in Handoff"]

### Proteo (Ricerca & Contenuto)
- [ ] **Accuratezza Tecnica**: [Es. "Uso corretto di Typer per CLI"]
- [ ] **Completezza Profilo**: [Es. "Tutte le competenze chiave sono coperte"]
- [ ] **Chiarezza Documentale**: [Es. "Istruzioni operative chiare per l'agente"]

### Punti di Forza Trasversali
- [ ] [Punto comune a entrambi gli analisti]

---

## ⚠️ Criticità

> **Istruzioni**: Evidenziare problemi, gap o aree di miglioramento. Priorità: 🔴 Alta, 🟡 Media, 🟢 Bassa.

### Metis (Strategia)
- 🔴 **[Criticità alta]**: [Descrizione e impatto sul team]
- 🟡 **[Criticità media]**: [Descrizione]
- 🟢 **[Criticità bassa]**: [Descrizione]

### Proteo (Ricerca & Contenuto)
- 🔴 **[Criticità alta]**: [Es. "Manca gestione errori in CLI"]
- 🟡 **[Criticità media]**: [Es. "Alcune competenze sono sovrapposte"]
- 🟢 **[Criticità bassa]**: [Es. "Formattazione Markdown non uniforme"]

### Criticità Trasversali
- [ ] [Criticità rilevata da entrambi]

---

## 🛠️ Raccomandazioni

> **Istruzioni**: Azioni concrete per risolvere le criticità o migliorare l'oggetto.

### Priorità Metis
1. **[Azione 1]**: [Descrizione dettagliata]
2. **[Azione 2]**: [Descrizione dettagliata]

### Priorità Proteo
1. **[Azione 1]**: [Es. "Aggiungere flag --verbose a tutti i subcommand"]
2. **[Azione 2]**: [Es. "Includere esempi pratici nel profilo"]

### Piano di Azione Integrato
| ID | Azione | Responsabile | Priorità | Stato |
|----|--------|--------------|----------|-------|
| 1 | [Descrizione azione] | [Metis/Proteo/Efesto] | Alta/Media/Bassa | Da fare/In corso/Fatto |

---

## ⚔️ Conflitti tra Reviewer

> **Istruzioni**: Se i due reviewer hanno opinioni divergenti, documentarle qui per la risoluzione.

| Tema | Posizione Metis | Posizione Proteo | Stato Risoluzione |
|------|----------------|------------------|-------------------|
| **[Tema 1: Es. Uso di argparse vs Typer]** | [Positivo/Negativo + motivazione] | [Positivo/Negativo + motivazione] | 🟡 In attesa di Hermes |
| **[Tema 2]** | [...] | [...] | [...]

**Note sulla risoluzione**: [Spazio per commenti di Hermes o Atena per mediare]

---

## 🏁 Decisione Finale

> **Istruzioni**: Compilato da Hermes o Atena dopo aver esaminato il report.

### Verdetto
- [ ] ✅ **Approvato così com'è**
- [ ] 🔄 **Approvato con modifiche minori** (vedi Raccomandazioni)
- [ ] 🔴 **Rigettato / Da rifare**
- [ ] ⏸️ **In attesa di chiarimenti**

### Autorizzazione al rilascio
- **Approvato da**: [Nome approvatore]
- **Data**: [YYYY-MM-DD]
- **Note finali**: [Eventuali note prima dell'integrazione in `.opencode/agents/` o `tools/`]

---

## 📚 Integrazione Checklist Clio (Vault Obsidian)

> **Istruzioni**: Compilare questa sezione per garantire che l'output sia compatibile con il vault Obsidian secondo le convenzioni di [[obsidian-vault]]. Questa parte viene tipicamente validata da Clio.

### Validazione Struttura
- [ ] **Frontmatter YAML**: Presente, con `title`, `tags`, `aliases` (forme plurali).
- [ ] **Wikilink**: Tutti i link interni usano la sintassi `[[nota]]` o `[[nota|alias]]`.
- [ ] **Path Immagini**: Se presenti, usano il percorso relativo `../assets/images/<slug>/`.
- [ ] **Naming Convention**: Il file rispetta lo slug (lowercase, trattini).
- [ ] **Block IDs**: Se servono riferimenti precisi, usare ` ^block-id` (senza `[[` attorno al `^`).

### Check Specifico per Tipologia

#### Se è uno Script Efesto (tools/)
- [ ] Documentazione in `Library/Meta/` o `tools/<nome>/README.md`
- [ ] Esempi d'uso inclusi nel file `.md`
- [ ] Compatibilità con Typer verificata

#### Se è un Profilo Nuovo Membro (Team/ o .opencode/agents/)
- [ ] Frontmatter include `nome`, `ruolo`, `archetipo` (vedi [[AGENTS.md]])
- [ ] Istruzioni operative chiare e non ambigue
- [ ] Link a fonti di riferimento (es. [[obsidian-vault]])

#### Se è una Guida (Library/Meta/)
- [ ] Sezioni ben definite con headings (`##`)
- [ ] Eventuali screenshot in `assets/images/<slug-guida>/`
- [ ] Link a documenti correlati nel vault

---

## 📝 Esempi Pratici di Compilazione

### Caso 1: Review Script Efesto (es. `pdf_converter`)
```markdown
**Oggetto**: `tools/pdf_converter/` refactoring da argparse a Typer
**Sintesi Unificata**: Lo script è pronto per la migrazione. Metis conferma che il nuovo flusso Typer si integra meglio con gli altri tool. Proteo nota che mancano esempi per il subcommand `batch`.
**Criticità**: 🟡 Mancano test automatici post-migrazione.
**Decisione**: ✅ Approvato con modifiche minori (aggiungere esempi e test).
```

### Caso 2: Review Profilo Nuovo Membro (es. "Clio")
```markdown
**Oggetto**: Profilo "Clio" - Esperta Documentazione
**Sintesi Unificata**: Profilo completo. Competenze in Obsidian e Markdown eccellenti. Metis suggerisce di aggiungere un flusso di handoff specifico con Efesto.
**Raccomandazioni**: Includere sezione su gestione dei metadati YAML complessi.
**Checklist Clio**: ✅ Frontmatter valido, wikilink pronti.
```

### Caso 3: Review Guida (es. `pdf-converter-guida.md`)
```markdown
**Oggetto**: Guida all'uso di `pdf_converter`
**Sintesi Unificata**: Guida chiara, copre tutti i casi d'uso. Proteo segnala che la sezione "Troubleshooting" è scarsa.
**Criticità**: 🟢 Alcuni path delle immagini usano Markdown instead di Wikilink.
**Azioni**: Aggiornare path immagini a `![[assets/images/pdf-converter/...]]`.
```

---

## 📎 Allegati e Riferimenti

- **Documento sorgente**: [[nome-file-sorgente]]
- **Link esterni**: [Documentazione Typer](https://typer.tiangolo.com/)
- **Registro Team**: [[AGENTS.md]]
- **Vault Guide**: [[obsidian-vault]]

---
*Template creato per il Team Olimpo - Uso interno*
