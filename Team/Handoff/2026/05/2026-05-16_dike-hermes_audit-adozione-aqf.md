---
title: "Audit di Adozione — Criteri AQF per Handoff"
date: 2026-05-16
author: Dike
tags: [audit, handoff, adozione, aqf]
status: completato
---

# Audit di Adozione — Criteri AQF per Handoff

> Prodotto da Dike — 2026-05-16
> Destinatario: Hermes
> Scopo: Verificare l'adozione dei nuovi campi nei file handoff

---

## Premessa

L'AQF (Agent Qualification Framework) include criteri di completamento standardizzati per gli handoff:
- `quality_score` — punteggio 1-5 per valutare la qualità dell'handoff
- `verifica_esterna` — flag booleano per indicare se la verifica è stata fatta da un membro diverso dall'autore
- `note_completamento` — note informative sul completamento

Questo audit verifica se i file handoff recenti rispettano questi criteri.

---

## File esaminati

Ho esaminato 5 file handoff dalla cartella `Library/Handoff/` (root e `2026/05/`):

| # | File | quality_score | verifica_esterna | note_completamento | Note |
|---|------|:--------------:|:----------------:|:------------------:|------|
| 1 | `2026-05-16_metis-hermes_agent-qualification-framework.md` | ❌ | ❌ | ❌ | Nessun frontmatter YAML |
| 2 | `2026-05-16_proteo-hermes_iqoq-ricerca.md` | ❌ | ❌ | ❌ | Nessun frontmatter YAML |
| 3 | `2026-05-16_dike-hermes_mappatura-processi.md` | ❌ | ❌ | ❌ | Frontmatter parziale (title, date, author, tags, status) |
| 4 | `2026-05-13_integrazione-email-working.md` | ❌ | ❌ | ❌ | Nessun frontmatter YAML |
| 5 | `2026-05-12_proteo_xai-terafactory-report.md` | ❌ | ❌ | ❌ | Nessun frontmatter YAML |

**Tasso di conformità: 0/5 (0%)**

---

## Verifica storica

Ho cercato nei file handoff più vecchi per verificare se i criteri fossero mai stati adottati in precedenza:

- `quality_score`: mai trovato nei frontmatter (solo menzioni nel contenuto del framework AQF)
- `verifica_esterna`: mai trovato nei frontmatter
- `note_completamento`: **trovato in 1 caso** — `2026-03-26_efesto-team_nota_consulto-flag-merge.md`

L'unico file con un campo simile è una nota tecnica di Efesto del marzo 2026, ma non è stato ripreso nei file successivi.

---

## Problemi identificati

### 1. Template non aggiornato
Il template ufficiale `Library/Handoff/templates/efesto-handoff-template.md` **non include** i nuovi campi richiesti. Nessun membro ha un riferimento-guida per compilarli.

### 2. Inconsistenza strutturale
- Alcuni file usano frontmatter YAML
- Altri usano solo metadata in-line (es. `> Prodotto da: ...`)
- Nessuno standard percepito

### 3. Nessuna enforcement
Non c'è un processo che richieda la presenza dei campi. Gli autori non sono tenuti a compilarli.

---

## Raccomandazioni

### Azioni prioritarie

1. **Aggiornare il template** — Inserire i campi mancanti nel template `efesto-handoff-template.md`:
   ```yaml
   quality_score: 1-5
   verifica_esterna: true/false
   note_completamento: "..."
   ```

2. **Comunicare l'obbligo** — Hermes dovrebbe comunicare a tutti i membri la nuova convenzione (via chat o memo)

3. **Validation leggera** — Clio può verificare la presenza dei campi durante il review dei file

### Cosa lasciare com'è

- I contenuti dei file esaminati sono buoni — solo la forma del frontmatter va aggiornata
- Non serve rifare i file vecchi — solo i nuovi handoff dovranno seguire la convenzione

---

## Nota sulla deviazione

Come previsto, nessun file ha il campo `deviazione` — questo è corretto perché tale campo è riservato agli handoff bloccati/fermi, non a quelli in corso.

---

## Conclusioni

**L'adozione dei criteri AQF per gli handoff è bloccata.** I nuovi campi non sono presenti in alcun file recente, il template non li include, e nessun processo ne garantisce la compilazione.

La situazione è risolvibile con un intervento semplice (aggiornamento template + comunicazione), ma senza azione non cambierà.

> [!tip]
> Prossimo passo: Hermes aggiorna il template e comunica la nuova convenzione ai membri del team.

---

*Audit completato da Dike — 2026-05-16*