---
tags: [verifica, asp, ibridato, tucson]
---

# Verifica conformità — `projects/tucson/specifiche/asp-ibridato.md`

**Data**: 2026-05-10  
**File esaminato**: `projects/tucson/specifiche/asp-ibridato.md`  
**Riferimento convenzioni**: `Library/Meta/obsidian-vault.md`  
**Esito**: Conforme con osservazioni

---

## Conforme?

**Sì**, il file è sostanzialmente conforme ai criteri specificati.  
Non emerge alcuna violazione bloccante. Le osservazioni riguardano prevalentemente convenzioni stilistiche e best practice, non errori funzionali.

---

## Errori trovati

Nessun errore critico. Di seguito le anomalie e le atipicità rilevate:

### 1. Campo `data` in italiano (riga 3) — incoerenza linguistica
- Riga 3: `data: 2026-05-10`
- Il vault utilizza `date` (inglese) nei campi condivisi della guida (`converted_at`, `author`). L'uso di `data` (italiano) è una scelta lessicale che rompe la coerenza con gli altri documenti del vault e con i campi standard documentati in `obsidian-vault.md` (§ "Campi standard per i documenti convertiti da PDF").

### 2. Campo `autore` in italiano (riga 4) — stessa incoerenza
- Riga 4: `autore: Hermes (Team Olimpo)`
- Il vault adotta `author` per il campo autore nei documenti convertiti. `autore` segue la stessa deroga di `data`.

### 3. Wikilink annidati nel frontmatter YAML (righe 6–11) — uso atipico
- `basato_su` contiene wikilink (`[[ibridazione-compost-metis]]`, `[[compost]]`, ecc.) in un campo del frontmatter.
- Tecnicamente valido in YAML (sono stringhe letterali), ma Obsidian **non risolve i wikilink nel frontmatter**: non appariranno nella graph view, non saranno clickabili, e non contribuiranno al collegamento tra note. La pratica è documentata come atipica e non raccomandata dalla guida del vault.

### 4. `versione: 1.0` non quotato (riga 14) — tipo YAML ambiguo
- Riga 14: `versione: 1.0`
- In YAML, `1.0` è interpretato come numero in virgola mobile (float), non come stringa. Se in futuro si volesse usare `"1.0.1"` o confrontare con pattern semantici, il tipo cambierebbe. Per coerenza, le versioni dovrebbero essere stringhe (`versione: "1.0"`).

### 5. Posizione del file fuori dal vault Obsidian — non coperto dalle convenzioni
- Il file risiede in `projects/tucson/specifiche/`, non in `Library/`. Le convenzioni di `obsidian-vault.md` si applicano strettamente ai file `.md` all'interno del vault (`Library/`). I criteri di frontmatter plurale, wikilink e slug sono comunque verificati per buona pratica, ma la loro applicazione a questo file è **extraterritoriale** rispetto al documento di riferimento.

---

## Suggerimenti

| # | Suggerimento | Rilevanza | Azione proposta |
|---|-------------|-----------|-----------------|
| 1 | Uniformare `data` → `date` | Media | Se il file è destinato a risiedere permanentemente fuori dalla Library, mantenere `data` è accettabile. Se venisse spostato in `Library/`, rinominare in `date` per coerenza con le convenzioni. |
| 2 | Uniformare `autore` → `author` | Media | Stessa valutazione del punto 1. |
| 3 | Spostare i wikilink dal frontmatter al corpo del documento | Bassa | I riferimenti in `basato_su` potrebbero essere spostati in una sezione "Fonti" nel corpo del documento (es. riga 77), dove Obsidian li risolverebbe correttamente. In alternativa, mantenerli come metadati informativi non risolti — è una scelta consapevole. |
| 4 | Quotare la versione: `versione: "1.0"` | Bassa | Previene ambiguità di tipo YAML se la versione dovesse evolvere in schema semantico (es. `"1.0.1"`). |
| 5 | Nessuna azione per la posizione | — | Se il file deve stare in `projects/tucson/specifiche/`, è fuori dal perimetro delle convenzioni del vault. Nessuna correzione necessaria. |

---

## Checklist riepilogativa

| Criterio | Esito | Note |
|----------|-------|------|
| Frontmatter presente (prima riga `---`) | ✅ | Riga 1 |
| Frontmatter plurale (`tags`, `aliases`, `cssclasses`) | ✅ | `tags` usato correttamente in forma plurale (riga 5) |
| Wikilink interni (`[[...]]`) | ✅ | Tutti i link interni nel corpo del documento usano sintassi wikilink |
| Path immagini relativi | N/A | Nessuna immagine presente nel documento |
| Nome file in formato slug | ✅ | `asp-ibridato.md` — lowercase, trattini, nessuno spazio |
| YAML frontmatter valido | ✅ | Parsing YAML corretto |
| Date in ISO 8601 | ✅ | `2026-05-10` (riga 3) |

---

*Report generato da Clio — Archivistra Digitale del Team Olimpo.*
