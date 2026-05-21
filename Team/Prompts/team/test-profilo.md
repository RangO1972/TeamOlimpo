---
title: "Prompt — Test profilo agente esistente"
aliases: [test profilo, audit profilo agente]
tags: [prompts, team, test, profilo, grok]
versione: "1.0"
autore: "Hermes"
invocato_da: "Hermes — audit periodico o dopo modifiche puntuali a un agente"
placeholder: "{{kba_text}}"
---

# Prompt — Test profilo agente esistente

Usa questo prompt per testare un profilo agente già operativo senza passare per il flusso
completo di creazione. Utile per audit periodici o dopo modifiche puntuali.

## Comando

```powershell
uv run python -m tools.consulto `
  --provider grok `
  --model grok-4.20-0309-reasoning `
  --prompt "Library/Prompts/team/test-profilo.md" `
  --input ".claude/agents/MEMBRO.md" `
  --output "Library/deliverables/"
```

Sostituire `MEMBRO` con il nome del membro in minuscolo (es. `proteo`, `atena`, `efesto`).

## Prompt

Sei un esperto di system prompt design, AI agent architecture e progettazione di assistenti AI operativi.

Ti viene fornito il profilo operativo completo di un agente AI del Team Olimpo. Il tuo compito è valutarlo criticamente come se lo stessi leggendo per la prima volta — senza conoscere la storia del membro, solo il file.

---

### PROFILO DA TESTARE

{{kba_text}}

---

### ISTRUZIONI DI VALUTAZIONE

### 1. Test di chiarezza operativa

Rispondi a queste domande leggendo solo il profilo:

- **Chi è questo agente?** Riesci a capire la sua identità in meno di 30 secondi?
- **Cosa fa esattamente?** I task principali sono descritti in modo operativo o restano vaghi?
- **Cosa NON fa?** I confini del ruolo sono espliciti e non ambigui?
- **Come lavora?** Ci sono flussi di lavoro o processi numerati da seguire?
- **Con chi interagisce?** Le relazioni con gli altri membri del team sono chiare?

### 2. Test di coerenza interna

Identifica eventuali contraddizioni:
- La personalità dichiarata è coerente con le istruzioni operative?
- Ci sono sezioni che si contraddicono?
- Ci sono istruzioni duplicate o ridondanti?

### 3. Test dei casi limite

Proponi 3 scenari concreti di utilizzo di questo agente. Per ciascuno:
- Descrivi il task
- Indica se il profilo fornisce istruzioni sufficienti per gestirlo
- Indica cosa manca se il profilo è insufficiente

### 4. Test di completezza

Verifica la presenza di questi elementi fondamentali:
- [ ] Identità e archetipo chiari
- [ ] Elenco competenze core operative (non solo etichette)
- [ ] Confini espliciti (cosa non fa)
- [ ] Almeno un flusso di lavoro con passi numerati
- [ ] Gestione dei casi ambigui o delle situazioni limite
- [ ] Regole di handoff o interazione con altri membri
- [ ] Lingua di risposta specificata

### OUTPUT RICHIESTO

Rispondi in italiano con questa struttura:

### Identità del profilo
[Nome agente e ruolo — come li hai capiti dal file]

### Test chiarezza operativa
| Domanda | Risposta | Giudizio |
|---------|----------|---------|
| Chi è? | ... | ... |
| Cosa fa? | ... | ... |
| Cosa non fa? | ... | ... |
| Come lavora? | ... | ... |
| Con chi interagisce? | ... | ... |

### Contraddizioni rilevate
[Lista — o "Nessuna" se il profilo è coerente]

### Scenari di test
**Scenario 1**: [descrizione task]
- Profilo sufficiente: sì/no
- Gap: [cosa manca]

**Scenario 2**: [descrizione task]
- Profilo sufficiente: sì/no
- Gap: [cosa manca]

**Scenario 3**: [descrizione task]
- Profilo sufficiente: sì/no
- Gap: [cosa manca]

### Checklist completezza
[Riproponi la checklist con spunte reali basate sul contenuto del profilo]

### Punti di forza
[Max 3 — le cose che funzionano bene]

### Lacune prioritarie
[Max 3 — le lacune più critiche, in ordine di impatto operativo]

### Giudizio complessivo
**SOLIDO** / **MIGLIORABILE** / **DA RIVEDERE**
Motivazione in 2-3 righe.

### Raccomandazioni specifiche
[Cosa aggiungere, modificare o rimuovere — con indicazione della sezione]
