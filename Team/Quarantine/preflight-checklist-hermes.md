---
title: Pre-flight Checklist — Hermes
aliases: [preflight, checklist, pre-flight, readiness check]
tags: [meta, hermes, workflow, checklist, operativo]
---

# Pre-flight Checklist — Hermes

Scorri in **30 secondi**. Se un check fallisce → vai a [[#Se un check fallisce]].

## Pre-flight base

- [ ] LLM raggiungibile? (fai una domanda di test — "ping")
- [ ] Spazio disco > 500 MB? (`df -h /home/stra/TeamOlimpo`)
- [ ] Scrittura su `Library/Fucina/Handoff/` e `Library/deliverables/`? (`touch` di prova)
- [ ] Connessione internet? (`ping 8.8.8.8` — solo se task richiede web)

## Pre-flight specifico per tool

Se il task usa un tool specifico, verifica quello — ignora il resto.

- [ ] Python + dipendenze? (`uv run python -m tools.<nome> --help` esce con 0)
- [ ] Vault Obsidian accessibile? (`ls Library/documents/` non vuoto)
- [ ] API key presenti? (`.env` ha le credenziali necessarie — [[consulto-guida]] per Grok/Gemini)
- [ ] Web search funzionante? (se task richiede ricerca live)

## Se un check fallisce

1. **Annota in scratchpad** sezione "Blocchi": `[data] BLOCCO: <cosa non va>`
2. **Decidi**: il task può procedere comunque? (es. manca web → task offline ok. Manca scrittura → stop.)
3. **Se stop**: scrivi in scratchpad `[data] BLOCCATO: <task> — causa: <motivo>`

## Stato vault (ogni 3-4 sessioni)

- [ ] Scratchpad riflette l'attuale carico di lavoro?
- [ ] Task in corso da > 3 gg senza aggiornamenti? ([[Handoff/Registro]] — cerca `in-corso` datati)
- [ ] Handoff bloccati da > 24h? ([[Handoff/Registro]] — cerca `bloccato`)
