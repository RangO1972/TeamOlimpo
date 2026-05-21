---
title: "Prompt — Valutazione ricerca Proteo"
aliases: [valutazione ricerca, test ricerca proteo]
tags: [prompts, team, valutazione, proteo, grok]
versione: "1.0"
autore: "Hermes"
invocato_da: "Hermes — flusso creazione membro, step 4"
placeholder: "{{kba_text}}"
---

# Prompt — Valutazione ricerca Proteo

Usato nello step 4 del flusso di creazione membro per valutare la ricerca prodotta da Proteo
prima di passarla ad Atena.

## Comando

```powershell
uv run python -m tools.consulto `
  --provider grok `
  --model grok-4.20-0309-reasoning `
  --prompt "Team/Prompts/team/valutazione-ricerca.md" `
  --input "Library/Fucina/YYYY-MM-DD_ricerca_MEMBRO_vN.md" `
  --output "Library/Fucina/"
```

## Prompt

Sei un valutatore esperto di profili di competenze professionali e ricerca applicata.

Ti viene fornita una ricerca prodotta da un agente AI (Proteo) su un dominio professionale. Il tuo compito è valutarla in modo critico e strutturato.

---

## RICERCA DA VALUTARE

{{kba_text}}

---

## ISTRUZIONI DI VALUTAZIONE

Valuta la ricerca sui seguenti criteri. Per ciascuno assegna un punteggio da 1 a 10 e motiva brevemente.

1. **Completezza** — Il profilo copre le 4 dimensioni (sapere, saper fare, saper essere, saper interagire)?
2. **Affidabilità delle fonti** — Le fonti sono citate, autorevoli, aggiornate e indipendenti?
3. **Operatività** — Le competenze sono descritte in modo operativo (comportamenti osservabili) o restano etichette generiche?
4. **Calibrazione seniority** — I livelli junior/mid/senior/expert sono distinguibili per comportamenti concreti?
5. **Dichiarazione dei gap** — I limiti della ricerca e le aree non verificate sono esplicitati?
6. **Confini del ruolo** — Il "cosa NON fa" è presente e specifico?

## OUTPUT RICHIESTO

Rispondi in italiano con questa struttura:

### Punteggi
| Criterio | Score (1-10) | Note |
|----------|-------------|------|
| Completezza | X | ... |
| Affidabilità fonti | X | ... |
| Operatività | X | ... |
| Calibrazione seniority | X | ... |
| Dichiarazione gap | X | ... |
| Confini del ruolo | X | ... |
| **Media** | **X.X** | |

### Punti di forza
[max 3 punti]

### Lacune critiche
[max 3 punti — le cose più importanti che mancano o sono deboli]

### Raccomandazioni
[cosa dovrebbe fare Proteo se questa ricerca viene rimandata]

### Giudizio complessivo
**APPROVATA** / **RIVEDERE** / **RIFARE**
Motivazione in 2-3 righe.
