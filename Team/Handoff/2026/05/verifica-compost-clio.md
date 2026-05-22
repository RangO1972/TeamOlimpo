---
tags: [verifica, compost, tucson]
---

# Verifica Conformità — `projects/tucson/specifiche/compost.md`

**Data verifica**: 2026-05-10  
**Documento**: `projects/tucson/specifiche/compost.md` (311 righe)  
**Riferimento**: `Library/Meta/obsidian-vault.md` — Convenzioni vault Obsidian  

---

## Conforme?

**NO** — il documento presenta 3 discrepanze rispetto alle convenzioni vault Obsidian.

---

## Errori trovati

### E1 — Campo `data` con virgolette (viola Regola 9)

- **Riga**: 4 del frontmatter
- **Contenuto**: `data: "2026-05-09"`
- **Convenzione**: le date in ISO 8601 vanno **senza virgolette**. Citazione testuale da `obsidian-vault.md` (Regola 9 rapida, riga 201):
  > Date in ISO 8601 senza virgolette — `data: 2026-03-25`
- **Perché è un problema**: In YAML, le virgolette trasformano la data in una stringa, impedendo a Obsidian di interpretarla come tipo `date` per ordinamenti cronologici e plugin di timeline. La forma corretta è:
  ```yaml
  data: 2026-05-09
  ```

---

### E2 — Assenza del campo `title` (viola § Frontmatter YAML)

- **Riga**: 3 del frontmatter
- **Contenuto**: `titolo: "Produzione Compost — Specifica Tecnica (Feedstock, Metodi, Dimensionamento)"`
- **Convenzione**: il campo standard per il titolo visualizzato nel graph view e nella navigazione è **`title`**, non `titolo`. Citazione da `obsidian-vault.md` (riga 129):
  > | `title` | stringa | Titolo visualizzato nel graph view |
- **Perché è un problema**: Obsidian cerca il campo `title` per la visualizzazione nel graph view e nella breadcrumb. Il campo `titolo` in italiano non viene riconosciuto, quindi il nodo del graph view mostrerebbe il nome file (`compost.md`) invece del titolo descrittivo.
- **Nota**: il campo `titolo` può essere preservato come metadato personalizzato, ma deve essere affiancato dal campo standard `title`.

---

### E3 — Riferimenti interni non in formato wikilink (viola Regole 3 e 5)

- **Sezioni coinvolte**:
  - Frontmatter, campo `basato_su` (righe 9-12): path di file come stringhe YAML
  - Sezione 10 "Riferimenti" (righe 295-298): path di file scritti come testo inline tra backtick
- **Convenzione** (Regola 3, riga 36-38):
  > Obsidian usa i **wikilink** come formato nativo. Usare sempre questa sintassi per i link interni al vault: `[[nome-file]]`
- **Regola 5** (riga 56):
  > I link Markdown standard `[testo](url)` vanno usati **solo per URL esterni**.
- **Dettaglio violazioni**:

  **Frontmatter `basato_su`** — i path sono stringhe YAML. In questa sede i wikilink non sono supportati nativamente da YAML. La soluzione è aggiungere link nella sezione "Riferimenti" o usare un plugin Obsidian che interpreti wikilink in YAML. Considerazione: **falso positivo parziale** — il frontmatter non può contenere wikilink puri, ma il contenuto della nota può compensare.

  **Sezione 10 (righe 295-298)** — i riferimenti sono scritti come testo monospace:
  ```
  - Ricerca feedstock e metodi (Proteo): `Library/Handoff/2026-05-09_proteo-hermes_compost-ricerca_tucson.md`
  - Specifica Triceee: `projects/tucson/specifiche/triceee.md`
  - Specifica Biochar: `projects/tucson/specifiche/biochar.md`
  - Specifica Funghi: `projects/tucson/specifiche/funghi.md`
  ```
  Questi **dovrebbero essere wikilink** cliccabili:
  ```
  - Ricerca feedstock e metodi (Proteo): `[[2026-05-09_proteo-hermes_compost-ricerca_tucson]]
  - Specifica Triceee: `[[triceee]]`
  - Specifica Biochar: `[[biochar]]`
  - Specifica Funghi: `[[funghi]]`
  ```
  (Nota: i file `triceee.md`, `biochar.md`, `funghi.md` sono nella stessa cartella `projects/tucson/specifiche/` e sono univoci nel vault, quindi il path minimo — solo nome file — è sufficiente per Regola 6.)

---

## Suggerimenti

| # | Correzione proposta | Gravità | Sforzo |
|---|---------------------|---------|--------|
| S1 | Rimuovere le virgolette da `data: "2026-05-09"` → `data: 2026-05-09` | Media | 1 riga |
| S2 | Aggiungere `title: "Produzione Compost — Specifica Tecnica (Feedstock, Metodi, Dimensionamento)"` sopra o in sostituzione di `titolo` (o mantenere entrambi) | Media | 1 riga |
| S3 | Convertire i 4 riferimenti interni della sezione 10 in wikilink (es. `[[triceee]]` invece di `` `projects/tucson/specifiche/triceee.md` ``) | Bassa | 4 righe |
| S4 | (Opzionale) Aggiungere una sezione "Vedi anche" con wikilink per i documenti correlati, come compensazione per i path nel frontmatter `basato_su` che non possono essere wikilink | Molto bassa | ~5 righe |

**Nota**: il nome file `compost.md` è conforme (slug valido, lowercase, senza spazi).  
**Nota**: il campo `tags` è al plurale ✅ e in formato lista inline ✅ — conforme.  
**Nota**: la prima riga è `---` ✅ — conforme.

---

## Riepilogo

| Criterio | Esito |
|----------|-------|
| Frontmatter plurale (`tags`, `aliases`, `cssclasses`) | ✅ Conforme |
| Prima riga `---` | ✅ Conforme |
| Nome file in formato slug | ✅ Conforme |
| Date ISO 8601 senza virgolette | ❌ **Non conforme** (E1) |
| Campo `title` presente | ❌ **Non conforme** (E2) |
| Wikilink per link interni | ❌ **Non conforme** (E3) |
| Path immagini relativi | N/A (nessuna immagine) |
| Link Markdown solo per URL esterni | ✅ Conforme *(i riferimenti interni non sono link, sono testo — inattivi ma non violano la sintassi dei link)* |
