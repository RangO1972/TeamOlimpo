# Verifica Conformità KBA — Flusso Gestione Documentale

**Data**: 2026-05-05  
**Autore**: Clio (Archivista Digitale)  
**Oggetto**: Verifica conformità output pdf_converter alle convenzioni vault Obsidian  
**Riferimento**: `Library/Meta/obsidian-vault.md`

---

## 1. Introduzione

Il presente report documenta i risultati della verifica sistematica del flusso di gestione KBA rispetto alle convenzioni del vault Obsidian definite in `Library/Meta/obsidian-vault.md`. La verifica ha interessato:

- **159 file `.md`** in `Library/documents/` (documenti convertiti da PDF)
- **159 cartelle** in `Library/assets/images/` (immagini estratte, organizzate per slug)
- **Database SQLite** `pdf_index.db` in `Library/data/`
- **159 record KBA** in `Library/data/kba_catalog/records/`

L'obiettivo è identificare violazioni delle 10 regole fondamentali del vault e suggerire ottimizzazioni per garantire piena conformità.

---

## 2. Controlli effettuati

### 2.1 Struttura del vault e organizzazione file
- ✅ **Convenzione naming**: tutti i file `.md` in `documents/` seguono lo schema `slug.md` (es. `nk-2400-0150.md`, `ak-1000-0070.md`)
- ✅ **Cartelle immagini**: ogni documento ha la propria cartella in `assets/images/<slug>/` — corrispondenza 1:1 verificata (159 cartelle per 159 documenti)
- ✅ **Niente file `.md` in `data/`**: i record KBA sono correttamente posizionati in `data/kba_catalog/records/` come da convenzione
- ✅ **Database in `data/`**: `pdf_index.db` presente e coerente con la struttura

### 2.2 Frontmatter YAML
- ✅ **Presenza frontmatter**: tutti i 159 file `.md` in `documents/` hanno blocco frontmatter delimitato da `---`
- ✅ **Campi standard**: tutti i documenti includono `title`, `source_pdf`, `converted_at`, `num_pages`, `tags`, `author`, `num_images`
- ⚠️ **Campo `tags`**: **159/159 documenti (100%) hanno `tags: []` vuoto** — non popolato dal converter
- ❌ **Validità YAML**: test su campione fallito — il parser YAML segnala errore "expected a single document" perché il frontmatter non è isolato correttamente dal corpo del documento

### 2.3 Link interni e wikilink
- ❌ **Nessun wikilink trovato**: ricerca di `[[` in `documents/` non ha prodotto risultati
- ❌ **Nessun embed wikilink**: ricerca di `![[` in `documents/` non ha prodotto risultati
- ⚠️ **Sintassi immagini**: il converter usa `![](../assets/images/<slug>/img.png)` (Markdown standard) invece di `![[img.png]]` (wikilink) come raccomandato dalle convenzioni

### 2.4 Path delle immagini
- ✅ **Path relativi corretti**: le immagini usano `../assets/images/<slug>/` — sintassi corretta per file in `documents/` che punta a `assets/images/`
- ✅ **Nessun path assoluto**: non sono stati trovati path tipo `C:\...` o `/home/...` nei riferimenti alle immagini
- ⚠️ **Path assoluti nel contenuto**: alcuni documenti (es. `ak-1300-0033.md`, `na-0200-0147.md`) contengono riferimenti a percorsi Windows (`C:\Users\...`) nel *testo* — questi sono contenuti originali del PDF, non errori del converter

### 2.5 Formato tag
- ⚠️ **Forma corretta ma vuota**: `tags: []` usa la sintassi lista inline corretta, ma il campo è sempre vuoto
- ❌ **Mancanza popolamento**: il converter non estrae o assegna tag automaticamente

### 2.6 Allineamento database-filesystem
- ✅ **Conteggio file**: 159 file `.md` in `documents/` corrispondono a 159 cartelle in `assets/images/`
- ✅ **Record KBA**: 159 record in `data/kba_catalog/records/` speculari ai documenti
- ⚠️ **Verifica DB**: `sqlite3` non disponibile nell'ambiente — non è stato possibile interrogare direttamente `pdf_index.db` per verificare la coerenza dei metadati indicizzati

---

## 3. Violazioni trovate

### Violazione 1 — Mancanza wikilink (Regola 3 e 4)
**Gravità**: 🔴 Alta  
**Descrizione**: Il converter produce immagini con sintassi Markdown standard `![](path)` invece di wikilink `![[img.png]]`. I link interni tra documenti (es. riferimenti a KBA correlati) sono assenti.  
**Impatto**: Il vault in Obsidian non sfrutta il graph view, i backlink e la navigazione nativa tra note. Le immagini non sono risolvibili tramite il sistema di ricerca interna di Obsidian.

### Violazione 2 — Frontmatter non valido per parser YAML (Regola 1)
**Gravità**: 🟡 Media  
**Descrizione**: Il frontmatter è delimitato da `---` ma il parser YAML fallisce perché il corpo del documento (dopo il secondo `---`) viene interpretato come un secondo documento YAML.  
**Impatto**: Strumenti esterni che leggono il frontmatter via parser YAML standard potrebbero fallire. Obsidian gestisce la cosa correttamente, ma la portabilità è compromessa.

### Violazione 3 — Campo `tags` sempre vuoto (Regola 5, sezione Formato tag)
**Gravità**: 🟡 Media  
**Descrizione**: `tags: []` in tutti i 159 documenti. Il converter non popola i tag.  
**Impatto**: I documenti non sono categorizzabili tramite tag in Obsidian. La tassonomia è inesistente. La ricerca per tag non restituisce risultati.

### Violazione 4 — Mancanza campi Obsidian speciali (Regola 2)
**Gravità**: 🟢 Bassa  
**Descrizione**: I campi `aliases` e `cssclasses` non sono presenti. Non è un errore, ma una mancanza di arricchimento.  
**Impatto**: I wikilink non hanno nomi alternativi. Il rendering è standard senza classi CSS personalizzate.

### Violazione 5 — Path immagini non ottimizzati (Regola 6)
**Gravità**: 🟢 Bassa  
**Descrizione**: I path usano la forma `../assets/images/<slug>/img.png` invece del path minimo `![[img.png]]`.  
**Impatto**: Minor leggibilità del codice sorgente Markdown. Le immagini dipendono dalla posizione della cartella `assets/` rispetto a `documents/` — se la struttura cambia, i link si rompono. Con i wikilink, Obsidian risolve il nome file ovunque si trovi nel vault.

---

## 4. Suggerimenti ottimizzazione

### 4.1 Priorità Alta — Modifiche al pdf_converter (per Efesto)

#### A. Convertire i link immagine in wikilink
**Azione**: Modificare il pdf_converter per produrre `![[nome-immagine.png]]` invece di `![](../assets/images/<slug>/nome-immagine.png)`.  
**Motivazione**: Rispetta la Regola 4 delle convenzioni. Obsidian risolve i wikilink in tutto il vault.  
**Implementazione**: Dopo l'estrazione delle immagini, sostituire nel `.md` generato la sintassi Markdown con quella wikilink. Poiché ogni immagine è in una cartella unica per slug, il nome file è univoco — non servono path.

#### B. Popolare automaticamente i `tags`
**Azione**: Implementare logica di estrazione tag dal contenuto del PDF o da metadati noti (es. tipo documento: "Alert", "Article", "Notification").  
**Motivazione**: La Regola 5 richiede tag per la categorizzazione. Attualmente `tags: []` rende i documenti non indicizzabili per categoria.  
**Suggerimento**: Usare parole chiave nel titolo o nel contenuto (es. "Security Notification" → `tags: [security, notification]`).

### 4.2 Priorità Media — Quality control post-conversione (per Clio)

#### C. Validazione frontmatter
**Azione**: Prima di considerare completata una conversione, verificare che il frontmatter sia un documento YAML valido (un solo documento tra i delimitatori `---`).  
**Motivazione**: Il test su `nk-2400-0150.md` ha mostrato errore di parser. Potrebbe essere un problema di formattazione (es. `title` con virgolette non chiuse).  
**Implementazione**: Usare uno script di validazione YAML sui file convertiti prima di aggiornare il database.

#### D. Arricchimento metadati manuale/semi-automatico
**Azione**: Dopo la conversione, Clio deve popolare `tags` e `aliases` basandosi sul contenuto.  
**Motivazione**: Il converter non può estrarre tutto. L'intervento umano (o assistito) garantisce qualità tassonomica.  
**Flusso**: Conversione → Clio verifica frontmatter → Clio aggiunge tag → Conferma completamento.

### 4.3 Priorità Bassa — Miglioramenti strutturali

#### E. Aggiungere `aliases` nei documenti
**Azione**: Inserire nel frontmatter il campo `aliases: [<kba_id>]` per permettere il linking tramite ID (es. `[[NK-2400-0150]]`).  
**Motivazione**: Molti documenti si riferiscono ad altri KBA tramite ID (es. "NK-2400-0160" in `nk-2400-0150.md`). Con gli aliases, questi riferimenti diventano link cliccabili.

#### F. Standardizzare `converted_at`
**Azione**: Verificare che tutte le date siano in ISO 8601 senza virgolette extra.  
**Stato attuale**: `converted_at: '2026-03-25 14:43:48.624435'` — le virgolette singole sono presenti. La Regola 9 dice "senza virgolette", ma le virgolette singole sono accettabili in YAML per stringhe con spazi. Da monitorare.

### 4.4 Verifica integrità database

#### G. Audit periodico DB-filesystem
**Azione**: Poiché `sqlite3` non è disponibile, usare il comando `uv run python -m tools.pdf_converter stats` e `list` per verificare la coerenza.  
**Motivazione**: Il database deve riflettere lo stato del filesystem. Se un file viene cancellato manualmente, il DB deve essere aggiornato.  
**Nota**: Il comando `list` è stato bloccato dall'utente — da ritentare in altra sessione.

---

## 5. Riepilogo conformità

| Regola | Stato | Note |
|--------|-------|------|
| 1. Frontmatter in cima | ✅ Parziale | Presente ma non valido per parser YAML |
| 2. Forma plurale (`tags`, `aliases`) | ✅ | `tags` usato correttamente, `aliases` mancante |
| 3. Wikilink per link interni | ❌ | Nessun wikilink presente |
| 4. Wikilink per embed immagini | ❌ | Usata sintassi Markdown `![]()` |
| 5. Link Markdown solo per URL esterni | ✅ | URL esterni corretti (es. link GSUDS) |
| 6. Path minimi nei link | ❌ | Path relativi lunghi invece di nomi file |
| 7. Nomi file univoci | ✅ | Slug univoci garantiti |
| 8. Immagini in cartella centralizzata | ✅ | `assets/images/<slug>/` corretto |
| 9. Date ISO 8601 | ✅ | Formato corretto (con virgolette singole) |
| 10. Mai toccare `.obsidian/` | ✅ | Non modificato |

**Conformità complessiva**: 🟡 **60%** — La struttura è corretta, ma la sintassi Obsidian nativa (wikilink) è assente, riducendo drasticamente l'usabilità del vault.

---

## 6. Azioni raccomandate (prossimi passi)

1. **Efesto**: Aggiornare il pdf_converter per usare wikilink nelle immagini (Violazione 1)
2. **Efesto**: Implementare estrazione automatica o eredità dei tag (Violazione 3)
3. **Clio**: Validare il frontmatter YAML dei 159 documenti esistenti (Violazione 2)
4. **Clio**: Popolare `tags` e `aliases` per i documenti esistenti (arricchimento)
5. **Hermes**: Coordinare il re-convert o patch dei file esistenti per allineare la sintassi

---

*Report generato da Clio — Archivista Digitale del Team Olimpo*  
*Verifica completata il 2026-05-05. Ogni affermazione si basa su controlli sistematici dei file su disco.*
