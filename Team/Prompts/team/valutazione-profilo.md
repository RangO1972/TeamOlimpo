---
title: "Prompt — Valutazione profilo Atena"
aliases: [valutazione profilo, test profilo atena]
tags: [prompts, team, valutazione, atena, grok]
versione: "1.0"
autore: "Hermes"
invocato_da: "Hermes — flusso creazione membro, step 6"
placeholder: "{{kba_text}}"
---

# Prompt — Valutazione profilo Atena

Usato nello step 6 del flusso di creazione membro per valutare il nuovo profilo agent
prodotto da Atena, confrontandolo con il precedente.

## Comando

```powershell
uv run python -m tools.consulto `
  --provider grok `
  --model grok-4.20-0309-reasoning `
  --prompt "Team/Prompts/team/valutazione-profilo.md" `
  --input ".claude/agents/MEMBRO.md" "Library/Fucina/YYYY-MM-DD_profilo_MEMBRO_vN.md" `
  --merge `
  --output "Library/Fucina/"
```

## Prompt

Sei un esperto di system prompt design, AI agent architecture e progettazione di assistenti AI operativi.

Ti vengono forniti due file concatenati: il profilo operativo attuale di un agente AI (file 1) e il nuovo profilo proposto (file 2). Il tuo compito è valutare il nuovo profilo in modo critico, confrontandolo con il precedente.

---

## FILE RICEVUTI

{{kba_text}}

---

## ISTRUZIONI DI VALUTAZIONE

Valuta il NUOVO profilo (file 2) sui seguenti criteri. Per ciascuno assegna un punteggio da 1 a 10.

1. **Coerenza identità/istruzioni** — La personalità dichiarata si riflette nelle istruzioni operative? Ci sono contraddizioni?
2. **Chiarezza operativa** — Un agente AI che legge questo profilo sa esattamente cosa fare in ogni situazione tipica?
3. **Confini del ruolo** — Il "cosa NON fa" è presente, specifico e non ambiguo?
4. **Copertura dei casi d'uso** — I flussi di lavoro coprono i task reali che questo agente dovrà svolgere?
5. **Progressione** — Il nuovo profilo è migliorativo rispetto al vecchio? Cosa è stato guadagnato e cosa eventualmente perso?
6. **Assenza di ridondanze** — Ci sono sezioni duplicate o istruzioni che si contraddicono?

## OUTPUT RICHIESTO

Rispondi in italiano con questa struttura:

### Punteggi
| Criterio | Score (1-10) | Note |
|----------|-------------|------|
| Coerenza identità/istruzioni | X | ... |
| Chiarezza operativa | X | ... |
| Confini del ruolo | X | ... |
| Copertura casi d'uso | X | ... |
| Progressione | X | ... |
| Assenza ridondanze | X | ... |
| **Media** | **X.X** | |

### Delta vecchio → nuovo
[3-5 punti: cosa è cambiato in meglio, cosa in peggio, cosa manca ancora]

### Rischi residui
[comportamenti ambigui o lacune che potrebbero causare problemi operativi]

### Raccomandazioni
[cosa dovrebbe correggere Atena se il profilo viene rimandato]

### Giudizio complessivo
**APPROVATO** / **RIVEDERE** / **RIFARE**
Motivazione in 2-3 righe.
