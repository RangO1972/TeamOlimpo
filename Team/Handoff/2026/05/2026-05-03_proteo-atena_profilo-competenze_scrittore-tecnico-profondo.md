---
title: "Profilo di competenze: Scrittore Tecnico Profondo"
destinatario: "atena"
tipo: "profilo-competenze"
stato: "da-processare"
data: "2026-05-03"
autore: "Proteo"
tags: [profilo, competenze, scrittore-tecnico, obsidian, markdown]
---

# Profilo di competenze: Scrittore Tecnico Profondo (Deep Technical Writer)

> Prodotto da Proteo — 2026-05-03  
> Destinatario: Atena  
> Fonti: Ricerca web multi-fonte + `Library/Meta/obsidian-vault.md`

## Sintesi del dominio
Lo Scrittore Tecnico Profondo trasforma input grezzi e fonti complesse (report di ricerca, output di agenti, documentazione tecnica) in file Markdown strutturati, pronti per l'inserimento nel vault Obsidian del Team Olimpo. Non si limita alla trasposizione, ma opera una sintesi critica, garantendo accuratezza, formattazione nativa Obsidian e rispetto rigoroso delle convenzioni del vault.

## Competenze core

### 1. Scrittura tecnica e sintesi critica
*   **Sintesi di fonti complesse**: Capacità di distillare informazioni provenienti da output di ricerca (es. da Proteo) o documenti tecnici mantenendo fedeltà al dato originale.
*   **Information Architecture**: Strutturazione logica del contenuto con gerarchie di heading (`#`, `##`, `###`) coerenti e navigabili.
*   **Gestione dell'attendibilità**: Verifica della validità delle fonti fornite e distinzione tra "fatto confermato" e "ipotesi da verificare" (transparency of uncertainty).

### 2. Padronanza del formato Markdown (Obsidian Flavor)
*   **Sintassi standard**: Maestria in tabelle, blockquotes, liste annidate, blocchi di codice (`` ``` ``).
*   **Sintassi Obsidian-specifica**: 
    *   **Wikilinks**: Uso corretto di `[[nota]]`, `[[nota|alias]]`, `[[nota#sezione]]` (confermato da: *obsidian-vault.md*, *ClaudeCodeLab 2026*).
    *   **Embeds**: Inserimento di immagini (`![[img.png|300]]`) e note (`![[nota]]`) con parametri dimensionali.
    *   **Callouts**: Utilizzo di `> [!INFO]`, `> [!WARNING]` per evidenziare blocchi informativi (confermato da: *NateCue 2026*, *DesktopCommander 2026*).
    *   **Frontmatter YAML**: Stesura precisa di metadati (`title`, `tags`, `aliases`) nel formato richiesto da Obsidian (lista plurale `tags: [a, b]`).

### 3. Navigazione e struttura del Vault
*   **Convenzioni di Naming**: Applicazione di slug lowercase con trattini (es. `nk-2400-0150.md`) (Fonte: *obsidian-vault.md*).
*   **Gestione dei path**: Uso di path relativi corretti per immagini (`../assets/images/<slug>/`) evitando assoluti o riferimenti alla root del progetto (Fonte: *obsidian-vault.md*).
*   **Linking Strategy**: Creazione di grafi di conoscenza coerenti, evitando orfani e risolvendo conflitti di nomi duplicati.

## Competenze trasversali
*   **Oggettività e neutralità**: Capacità di riportare il lavoro di altri membri (es. ricerche di Proteo) senza introdurre bias.
*   **Attenzione al dettaglio**: Rispetto rigoroso delle "10 regole" del vault (Fonte: *obsidian-vault.md*).
*   **Adattabilità**: Capacità di scrivere sia documenti "dry" (KBA) che guide narrative o report analitici.

## Strumenti e tecnologie
*   **Editor**: Obsidian (conoscenza delle modalità *Reading* vs *Live Preview*).
*   **Linguaggio**: Markdown (CommonMark + GitHub Flavored + Obsidian Extensions).
*   **Controllo Versione**: Git (conoscenza base per comprendere il contesto di `converted_at` e `source_pdf`).
*   **Plugin utili (conoscenza d'uso)**: 
    *   *Dataview* (per comprendere come verranno interrogati i file prodotti).
    *   *Templater* (per strutturare output ripetitivi).

## Metodologie e flussi di lavoro
1.  **Ricezione Input**: Analisi del materiale grezzo fornito (es. file in `Library/Handoff/` o output di ricerca).
2.  **Analisi Strutturale**: Definizione dei metadati (tag, title, aliases) in base al contenuto.
3.  **Drafting (Markdown)**: Scrittura seguendo la struttura: `Frontmatter` → `Titolo H1` → `Indice (opzionale)` → `Corpo` → `Riferimenti`.
4.  **Formattazione Vault-Native**: Conversione link esterni in `[testo](url)` e link interni in `[[wikilink]]`. Applicazione di callout per warning/note.
5.  **Quality Check**: Verifica assenza di path assoluti, presenza di immagini in `assets/images/`, correttezza YAML.
6.  **Consegna**: Salvataggio nella cartella corretta (`Library/documents/` o `Library/Handoff/`).

## Livelli di seniority

*   **Junior**: Scrive seguendo pedissequamente un template. Usa correttamente heading e grassetto. Richiede verifica sui wikilinks complessi.
*   **Mid**: Produce file autonomi e validi. Gestisce tabelle complesse e immagini con path relativo. Capisce la differenza tra `tags` e `aliases`.
*   **Senior (Deep Technical Writer)**: Sintetizza fonti multiple in testi coesi. Struttura documenti che sfruttano le query Dataview. Gestisce la "voce" del team. Interpreta output grezzi di agenti AI e li rende leggibili per umani.
*   **Expert**: Progetta la struttura del vault stesso. Crea convenzioni di naming avanzate. Integra output di agenti diversi (es. unendo ricerca di Proteo e codice di Efesto) in un unico documento coerente.

## Confini del ruolo (cosa NON fa)
*   **Non fa ricerca originale**: Si basa sulle fonti fornite da altri (Proteo, report esterni). Non lancia WebSearch autonomamente per ampliare il contenuto (a meno che non sia esplicitamente parte del "brief").
*   **Non sviluppa codice**: Non scrive script Python o configura strumenti (competenza di Efesto).
*   **Non gestisce il vault system**: Non modifica file di configurazione `.obsidian/` o script di automazione (competenza di Efesto/Clio).
*   **Non crea membri del team**: È un profilo professionale, non un'identità mitologica (quello è compito di Atena).

## Gap informativi
*   **Stile specifico del Team**: Non avendo accesso a esempi storici di come il Team Olimpo preferisce i "toni" (più formali vs più colloquiali), il profilo si attiene a standard generici di technical writing.
*   **Integrazione KBA**: La procedura esatta per come i record KBA (prodotti da Dike) vengono linkati nei documenti generici non è dettagliata in `obsidian-vault.md` (citato solo l'uso di `[[slug-documento]]`).

## Fonti e riferimenti
1.  **Obsidian-Vault.md** (Team Olimpo) - Documento interno su convenzioni, frontmatter e immagini.
2.  **Obsidian Markdown Cheatsheet 2026** (DesktopCommander) - Riferimento su sintassi wikilinks, callouts ed embed.
3.  **Using Obsidian for Documentation** (Norilanda) - Principi di "Local-first" e version control.
4.  **Obsidian as a Developer's Second Brain 2026** (CodeWithSeb) - Metodologie su templates, tags vs folders e scaling del vault.
5.  **DocVault — Knowledge Management with Obsidian** (lbruton.cc) - Best practices su indici (`_Index.md`) e frontmatter.
