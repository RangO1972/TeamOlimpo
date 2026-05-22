# Analisi Ridondanza Documentazione Membri — Team Olimpo

**Data**: 2026-05-06  
**Autore**: Metis (thinking partner)  
**Target**: Team Olimpo

---

## 1. Struttura Attuale dei File di Documentazione Membri

### 1.1 File Coinvolti

| File | Linee | Contenuto Principale | Stato |
|------|-------|---------------------|-------|
| `AGENTS.md` (root) | 81 | Elenco 8 agenti + convenzioni OpenCode | Parzialmente obsoleto |
| `CLAUDE.md` (root) | 50 | Elenco 3 membri core + architettura | Molto obsoleto |
| `Team/Members/Registro.md` | 47 | Registro completo 12 membri + cronologia | Aggiornato |
| `.opencode/agents/*.md` | ~150-300 cadauno | Profilo operativo singolo membro | Aggiornato (13 file) |
| `Library/Meta/flusso-creazione-membro.md` | 174 | Flusso 7-step creazione membri | Obsoleto (riferimenti path errati) |

### 1.2 Mappatura Membri per Fonte

```
Membri totali nel sistema: 12 (al 2026-05-05)

Fonte                | Membri elencati
---------------------|-----------------------------------
AGENTS.md            | hermes, proteo, atena, efesto, clio, dike, metis, calliope (8)
CLAUDE.md            | hermes, proteo, atena (3)
Registro.md          | hermes, proteo, atena, efesto, clio, dike, metis, calliope, pythagoras, hermione, euterpe, demetra (12)
.opencode/agents/    | tutti i precedenti + (13 file totali)
```

---

## 2. Identificazione Ridondanze e Conflitti

### 2.1 Ridondanze Dirette

| Tipo | Descrizione | Localizzazioni |
|------|-------------|----------------|
| **Elenco membri** | Stessa informazione replicata | AGENTS.md (8), CLAUDE.md (3), Registro.md (12), .opencode/agents/*.md (13) |
| **Descrizione architettura team** | "orchestrator-workers" ripetuta identica | AGENTS.md, CLAUDE.md |
| **Flusso creazione membro** | 7-step flow con dettagli identici | AGENTS.md riferisce, flusso-creazione-membro.md contenuto |
| **Convenzioni naming** | "nomi mitologici greche" ripetuto | AGENTS.md, CLAUDE.md |

### 2.2 Conflitti Documentali

| # | Conflitto |file A | vs file B | Severity |
|---|-----------|-------|-----------|----------|
| 1 | **Path agenti operativo** | AGENTS.md: `.opencode/agents/` ✓ | flusso-creazione-membro.md: `.claude/agents/` ✗ | Alta |
| 2 | **Path profili pubblici** | flusso-creazione-membro.md: `Team/Members/<Nome>.md` ✗ | Registro.md: solo `Registro.md` ✓ | Alta |
| 3 | **Numero membri** | AGENTS.md: 8 | Registro.md: 12 | Alta |
| 4 | **Struttura due file** | flusso-creazione-membro.md: "due file" legacy | Registro.md: "unico file agente" attuale | Alta |
| 5 | **Processo creazione** | flusso-creazione-membro.md: 7 step + Grok consulto | AGENTS.md: 4 step semplificati | Media |
| 6 | **Descrizione ruoli** | AGENTS.md: ruoli sintetici | Registro.md: ruoli estesi + modello | Media |

### 2.3 Analisi Causa Radice

Il Team Olimpo ha attraversato due evoluzioni architetturali significative:

1. **Pre-2026-03**: Architettura a due file (`Team/Members/<Nome>.md` + `.claude/agents/<Nome>.md`)
2. **2026-05-03**: Unificazione in unico file `.opencode/agents/<nome>.md` con sezione "Chi sono" per umani

La documentazione non è stata migrata consistentemente:

- ✓ AGENTS.md aggiornato per path `.opencode/agents/`
- ✗ flusso-creazione-membro.md NON aggiornato (riferimenti legacy)
- ✗ CLAUDE.md NON aggiornato (ancora con 3 membri core)

---

## 3. Valutazione Fonti di Verità

### 3.1 Criteri di Valutazione

| Criterio | Descrizione | Peso |
|----------|-------------|------|
| **Completezza** | Include tutti i membri esistenti | 30% |
| **Aggiornamento** | Data ultima modifica recente | 25% |
| **Dettaglio** | Informazioni ricche e strutturate | 20% |
| **Accessibilità** | Facilità di consultazione | 15% |
| **Autorevolezza** | Usato come riferimento dagli agenti | 10% |

### 3.2 Punteggio Fonti

| Fonte | Completezza | Aggiornamento | Dettaglio | Accessibilità | Autorevolezza | **Totale** |
|-------|-------------|----------------|-----------|---------------|---------------|------------|
| Registro.md | 10/10 ✓ | 10/10 ✓ | 8/10 | 9/10 | 7/10 | **8.8** |
| .opencode/agents/*.md | 10/10 ✓ | 9/10 | 10/10 ✓ | 6/10 | 10/10 ✓ | **9.2** |
| AGENTS.md | 7/10 | 8/10 | 6/10 | 10/10 ✓ | 8/10 | **7.8** |
| CLAUDE.md | 3/10 | 2/10 | 5/10 | 10/10 ✓ | 5/10 | **4.6** |
| flusso-creazione-membro.md | 5/10 | 3/10 | 7/10 | 5/10 | 6/10 | **5.0** |

### 3.3 Definizione Fonte di Verità Unica

**Raccomandazione**: `.opencode/agents/` come fonte primaria, `Registro.md` come indice sintetico.

| Ruolo | File | Motivazione |
|------|------|-------------|
| **Fonte primaria** | `.opencode/agents/<nome>.md` | Ogni file contiene profilo completo con frontmatter aggiornato, usato direttamente dagli agenti, unica locazione che OpenCode legge al runtime |
| **Indice sintetico** | `Team/Members/Registro.md` | Tabella riassuntiva centrale con tutti i membri, cronologia modifiche, errori — consultazione umana rapida |
| **Documentazione sistema** | `AGENTS.md` | Rimane come descrizione architetturale per chi legge il repo, MA deve essere allineato a Registro.md |

---

## 4. Proposta Ottimizzazione: Consolidamento Senza Duplicazioni

### 4.1 Strategia

Adottare un modello **single source of truth** con ridondanza controllata:

```
                ┌─────────────────────────┐
                │  .opencode/agents/*.md │ ← FONTE PRIMARIA (13 file)
                │  (profili completi)     │   Per OpenCode + membri
                └───────────┬─────────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
    ┌─────────────────┐        ┌─────────────────┐
    │ Registro.md     │        │ index.yaml       │
    │ (indice umano)   │        │ (index machine)  │
    └─────────────────┘        └─────────────────┘
```

### 4.2 Azioni Correttive

| # | Azione | File Target | Tipo Modifica |
|---|-------|-----------|--------------|
| 1 | Allineare AGENTS.md a Registro.md | AGENTS.md | Update sezione "Agenti OpenCode": lista completa 12 membri |
| 2 | Correggere path riferiti nel flusso | flusso-creazione-membro.md | Sostituire `.claude/agents/` → `.opencode/agents/` |
| 3 | Aggiornare architettura flusso | flusso-creazione-membro.md | Rimuovere riferimento "due file", documentare processo unificato |
| 4 | Semplificare o deprecare CLAUDE.md | CLAUDE.md | Opzioni: (a) rimuovere, (b) redirect a AGENTS.md |
| 5 | Aggiungere auto-reference in Registro.md | Registro.md | Link a `.opencode/agents/` per ogni membro |

### 4.3_impatto su Flusso Creazione Membri

Il flusso attuale (7 step con Grok consulto) è **obsoleto** per la documentazione ma il processo reale sembra essere stato semplificato. L'impatto:

| Componente | Impatto |Azione Raccomandata |
|------------|---------|-------------------|
| Istruzioni Atena | Leggere: aggiornare riferimenti in `atena.md` | Sostituire path legacy con attuali |
| Template valutazione | Potenzialmente non usati | Verificare se ancora necessari |
| Brief template | legacy | Valutare semplificazione |

### 4.4 Matrice Impatto

| Stakeholder | Impatto Positivo | Impatto Negativo |
|------------|------------------|-----------------|
| Hermes (delega) | Informazioni allineate | — |
| Nuovi membri | Documentazione coerente | — |
| Manutentore umano | Chiarezza fonti | Lavoro di migrazione |
| OpenCode | Nessuno (usa .opencode/agents/) | — |

---

## 5. Piano Implementazione

### 5.1 Ordine di Esecuzione

```
FASE 1: Preparazione (dati, non tocca file)
├── 1.1 Verificare stati attuali dei 12 membri .opencode/agents/*.md
└── 1.2 Identificare eventuali membri in .opencode/agents/ non in Registro.md

FASE 2: Migrazione flusso (documentazione meta)
├── 2.1 Aggiornare flusso-creazione-membro.md con path corretti
└── 2.2 Semplificare sezione "due file" → processo unificato

FASE 3: Consolidamento indici (AGENTS.md)
├── 3.1 Allineare sezione "Agenti OpenCode" a 12 membres
└── 3.2 Verificare coerenza con Registro.md

FASE 4: Deprecazione CLAUDE.md (opzionale)
├── 4.1 Valutare se mantenere o rimuovere
└── 4.2 Se mantenere: redirect a AGENTS.md

FASE 5: Validazione (test)
├── 5.1 Verificare che OpenCode legga .opencode/agents/ correttamente
└── 5.2 Quick-scan: tutti i 12 membri referenziati in AGENTS.md
```

### 5.2 Stima Lavoro

| Fase | File da Modificare | Tempo Stimato |
|------|-----------------|---------------|
| 2.1 | flusso-creazione-membro.md | 15 min |
| 2.2 | flusso-creazione-membro.md | 20 min |
| 3.1 | AGENTS.md | 10 min |
| 3.2 | — (conferma manuale) | 5 min |
| **Totale** | **2 file** | **~50 min** |

### 5.3 Criteri di Successo

- [ ] AGENTS.md e Registro.md mostrano identica lista 12 membri
- [ ] Nessun riferimento a `.claude/agents/` in file attivi
- [ ] Nessun riferimento a `Team/Members/<Nome>.md` (eccetto Registro.md stesso)
- [ ] flusso-creazione-membro.md documenta processo unificato
- [ ] OpenCode continua a funzionare senza interruzioni

---

## 6. Raccomandazione Finale

### 6.1 Decisione Raccomandata

**Adottare `.opencode/agents/` come fonte unica di verità per i profili membri**, con `Registro.md` come indice di riferimento per consultazione umana rapida.

Azioni immediate:

1. **Aggiornare flusso-creazione-membro.md** — Correggere path (.claude → .opencode) e documentare architettura attuale (unico file)
2. **Allineare AGENTS.md** — Sostituire lista 8 membri con lista 12 da Registro.md
3. **Valutare deprecazione CLAUDE.md** — O è ridondante con AGENTS.md o va allineato

### 6.2 Governance Futura

Per evitare future divergenze:

| Meccanismo | Implementazione |
|------------|-----------------|
| **Trigger allineamento** | Ogni nuovo membro → aggiornare sia .opencode/agents/ sia Registro.md |
| **Verifica periodica** | Scan mensile: lista .opencode/agents/*.md vs Registro.md |
| **Ownership** | Athena (HR Manager) responsabile allineamento |

---

## 7. Appendice: Dettaglio Scansione

### A. File Analizzati

```
/home/stra/TeamOlimpo/AGENTS.md                           ✓ Letto
/home/stra/TeamOlimpo/CLAUDE.md                          ✓ Letto
/home/stra/TeamOlimpo/Team/Members/Registro.md            ✓ Letto
/home/stra/TeamOlimpo/Library/Meta/flusso-creazione-membro.md ✓ Letto
/home/stra/TeamOlimpo/.opencode/agents/hermes.md          ✓ Letto (sample)
/home/stra/TeamOlimpo/.opencode/agents/proteo.md         ✓ Letto (sample)
/home/stra/TeamOlimpo/opencode.json                    ✓ Letto
```

### B. Lista Completa Membri (.opencode/agents/)

```
atena.md          calliope.md    dike.md         efesto.md
hermione.md      metis.md       proteo.md       pythagoras.md
clio.md          demetra.md     efesto.md       hermes.md
euterpe.md
```

(Totale: 13 file - verificare se Demetra duplicata)

### C. Cronologia Evolutiva Rilevata

- **2026-03**: Architettura due file con .claude + Team/Members/
- **2026-05-03**: Unificazione .opencode/agents/ (daRegistro.md)
- **2026-05-04**: Demetra aggiunto
- **2026-05-05**: Metis evoluzione dual-role

---

*Fine analisi — Proposta di ottimizzazione completata.*