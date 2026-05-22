---
tipo: handoff
da: Efesto
a: Clio
data: AAAA-MM-DD
strumento: <nome-tool>
stato: nuovo | aggiornato
priorita: alta | normale
tags: [handoff, efesto, clio]
quality_score: ~
verifica_esterna: false
note_completamento: ~
deviazione: ~
  # tipo: "output_incompleto" | "tool_failure" | "timeout" | "errore_formato" | "altro"
  # descrizione: "breve descrizione della deviazione"
  # causa: "causa identificata"
  # azione_correttiva: "cosa fatto per risolvere"
  # esito: "risolto" | "non_risolto" | "workaround"
  # impatto_utente: false
---

# Handoff da Efesto — [Strumento]

<!-- ISTRUZIONI PER EFESTO (AQF — Handoff v2):
1. Compila il frontmatter: data (ISO 8601), strumento, stato, priorita.
2. **AQF campi obbligatori** al completamento:
   - quality_score: 1-5 (vedi handoff-guida per significato)
   - note_completamento: cosa fatto e dove trovare l'output
   - verifica_esterna: true se un altro membro ha verificato
   - deviazione: SOLO se l'handoff ha avuto anomalie/errori
3. Rispondi a ogni sezione sottostante in modo conciso e specifico.
4. Se una sezione non pertiene (es. "Comandi rimossi" per strumento nuovo), rispondi "Nessuno" o "Non applicabile".
5. Salva il file come: Library/Handoff/YYYY/MM/efesto-handoff-<strumento>-AAAA-MM-DD.md
6. Se la modifica è complessa o ambigua, aggiungi note dettagliate nella sezione "Note per Clio".
Riferimenti: [[handoff-guida]], [[deviation-log-guida]]
-->

## Cosa ho fatto

<!-- Descrizione in prosa libera (max 5-6 righe) di cosa è stato implementato o modificato.
Usa un linguaggio colloquiale come parleresti a un collega.
Esempio: "Ho aggiunto un parser per il formato CSV raw del KBA e un filtro di deduplica
che riconosce documenti già presenti per titolo+autore. Refactor del comando convert per
usare il nuovo parser. Tutto backwards-compatible."
-->

## Comandi nuovi o modificati

<!-- Se questo handoff introduce o modifica comandi della CLI, compila la tabella sottostante.
Se non ci sono comandi toccati (es. solo refactoring interno), scrivi "Nessuno".
Formato: | Comando | Flag | Cosa fa | Esempio d'uso |
-->

| Comando | Flag | Cosa fa | Esempio d'uso |
|---------|------|---------|--------------|
| | | | |

<!-- Rimuovi la riga con celle vuote e usa una riga per comando/flag combination. -->

## Comandi rimossi o rinominati

<!-- Lista di comandi che non esistono più o che hanno cambiato nome.
Se nessuno, scrivi: "Nessuno" -->

Nessuno

## Dipendenze

<!-- Librerie aggiunte a pyproject.toml o requirements.
Se nessuna modifica alle dipendenze, scrivi: "Nessuna"
Formato: - libreria==versione (se aggiunti specifici) o - libreria (se versionato nel toml) -->

Nessuna

## File toccati

<!-- Lista dei file principali modificati. Non serve l'elenco completo di ogni singolo file,
solo quelli rilevanti per capire la portata della modifica.
Formato: - tools/nomegruppo/file.py (breve descrizione del cambio) -->

- tools/nomegruppo/file.py — descrizione della modifica

## Cosa NON ha cambiato

<!-- Elenco esplicito di comportamenti, comandi, formati output che rimangono invariati.
Aiuta Clio a capire cosa non deve riscrivere nella documentazione.
Esempio:
- Il comando `list` continua a sortare per data
- Il formato dei metadati YAML rimane invariato
- La cartella di input/output non cambia
-->

-

## Note per Clio

<!-- Spazio libero per comunicazioni specifiche a Clio:
- Quale guida aggiornare (es. "aggiorna Library/Meta/pdf-converter-guida.md sezione Comandi")
- Se è necessaria una nuova guida o documentazione
- Se c'è ambiguità nel comportamento che Clio dovrebbe chiarire prima di scrivere
- Se ci sono edge case o limitazioni note che meritano una nota nella docs
- Risorse utili per comprendere la modifica (es. commit, link interni, issue)
Esempio:
"Aggiorna la sezione 'Comandi' della guida principale. Non serve creare nuova doc.
La funzione parse_csv è pubblica ma interna — non documentare come API esterna.
Verificare che i test di integrazione passino prima di chiudere."
-->

