# Analisi KBA — Processi, Tracciamento e Trasparenza

**Data**: 05 Maggio 2026  
**Analista**: Dike  
**KBA analizzate**: 5 documenti Markdown da `Library/documents/`

---

## Obiettivo dell'analisi

Rileggere i documenti per estrarre:
1. Evoluzione dei processi descritti (come il problema è stato identificato, come cambia la soluzione nel tempo)
2. Tracciamento delle modifiche (revision history)
3. Trasparenza operativa (chiarezza delle informazioni, workaround, limiti dichiarati)
4. Pattern ricorrenti tra le cinque KBA

---

## 1. NK-2600-0129 — Silent Upgrade IPM .NET Exception

| Campo | Valore |
|---|---|
| **ID** | NK-2600-0129 |
| **Titolo** | .NET Framework Exception Error during Silent Upgrade of Root Upstream Server in IPM |
| **Pubblicazione** | 17 Apr 2026 |
| **Stato** | Approved |
| **Tipo** | Product Issues |
| **Azione richiesta** | Next Service Interval |

### 1.1 Evoluzione del processo

Il problema è introdotto dalla **nuova funzionalità** "silent upgrade" in IPM v1.4.0. L'evoluzione qui non è temporale ma funzionale: un nuovo processo (silent upgrade engine) causato dalla nuova feature.
- L'utente esegue silent upgrade → errore .NET displayed → upgrade continua in background

**Causa radice**: terminazione inattesa dell'IIS Worker Process che gestisce la richiesta di upgrade.

### 1.2 Tracciamento modifiche

| Data | Tipo | Descrizione |
|---|---|---|
| 17 Apr 2026 | Original Release | Prima pubblicazione |

**Nota**: Una sola entry. Nessuna revisione precedente. KBA appena rilasciata.

### 1.3 Trasparenza operativa

**Alta trasparenza**:
- Spiega che l'errore è **cosmetic** (display shows "Upgrade failed" ma l'upgrade completa)
- Fornisce recovery step-by-step (IISRESET)
- Dichiara esplicitamente: "There is no software solution for this issue"

**Limiti dichiarati**: Nessun fix software disponibile.

---

## 2. NK-2600-0071 — Download Fail Alarm Group Name

| Campo | Valore |
|---|---|
| **ID** | NK-2600-0071 |
| **Titolo** | Downloads fail con "Unable to Get Block Name Belonging to Alarm Group" e "Unable to Open Download List" |
| **Pubblicazione** | 14 Apr 2026 |
| **Stato** | Approved |
| **Tipo** | Product Issues |
| **Azione richiesta** | Next Service Interval |

### 2.1 Evoluzione del processo

Il problema emerge dall'**interazione tra due sistemi**: 
1. SIF ALARM_GROUP (Safety Instrumented Function)
2. External reference (riferimento esterno nella configurazione)

**Catena logica**:
- Utente crea SIF con ALARM_GROUP name "FIC-101" → sistema protegge quel nome
- Utente importa (o digita manualmente) external reference con root = "FIC-101" → il sistema importa lo stesso se l'errore è generato
- Result: name collision → download bloccato

**Nota sull'evoluzione**: Il problema è "legacy" — esiste da quando esistono le due funzionalità (SIF e external reference). Non è un bug Newly Introduced ma un edge case mai gestito.

### 2.2 Tracciamento modifiche

| Data | Tipo | Descrizione |
|---|---|---|
| 14 Apr 2026 | Original Release | Prima pubblicazione |

**Nota**: Una sola entry. Problema esistente ma KBA rilasciata solo ora.

### 2.3 Trasparenza operativa

**Trasparenza media**:
- Spiega il meccanismo (name collision)
- Fornisce workaround: identificare e risolvere riferimenti irrisolti
- Dichiara per DeltaV 14.x: "software solution not available" → raccomanda upgrade a v15+
- Per v15.x e v16: "being investigated"

**Limiti dichiarati**: 
- Per DeltaV 14.x: nessuna soluzione
- Per v15+: in fase di indagine

**Opacità**: Non specifica come il problema possa essere stato generato oltre all'import (manual typing mostrato nelle figure), non offre dettagli su quando/come il problema sia stato scoperto.

---

## 3. NK-2600-0097 — SQL Server 2019 Hotfix in IPM

| Campo | Valore |
|---|---|
| **ID** | NK-2600-0097 |
| **Titolo** | SQL Server 2019 Hotfix incorrectly shown in Available Updates List for IPM |
| **Pubblicazione** | 13 Apr 2026 |
| **Stato** | Approved |
| **Tipo** | Product Issues |
| **Azione richiesta** | Next Service Interval |

### 3.1 Evoluzione del processo

Il problema è un **content filtering bug** in IPM:
- IPM non supporta SQL Server updates
- Il content server invia hotfix che IPM non può installare
- L'hotfix rimane bloccato nella coda "Available Updates"

**Evoluzione**: Problema introdotto quando l'hotfix SQL (Hotfix 4455, KB50684804) è stato rilasciato da Microsoft → IPM lo ha matchingato ma non puòProcess.

### 3.2 Tracciamento modifiche

| Data | Tipo | Descrizione |
|---|---|---|
| 13 Apr 2026 | Original Release | Prima pubblicazione |

**Nota**: Una sola entry.

### 3.3 Trasparenza operativa

**Alta trasparenza**:
- Identifica l'hotfix specifico: "Hotfix 4455 for SQL Server 2019 (KB50684804) (64-bit)"
- Spiega il limitation: "IPM does not currently support SQL updates"
- Fornisce azione: non tentare l'installazione
- Indica la soluzione: hotfix rimosso dal content server, siClear automaticamente con prossimo Microsoft update

**Limiti dichiarati**: IPM non supporta SQL updates (limitation nota, non bug)

---

## 4. NK-2600-0082 — CIOC/CIOC2 to PK Controller Loss

| Campo | Valore |
|---|---|
| **ID** | NK-2600-0082 |
| **Titolo** | Temporary Loss of Data from CIOC/CIOC2 to PK Controller — Module Errors and Process Trips |
| **Pubblicazione** | 08 Apr 2026 |
| **Stato** | Approved |
| **Tipo** | Product Issues |
| **Azione richiesta** | Next Service Interval |

### 4.1 Evoluzione del processo

Problema di **comunicazione hardware** tra CIOC (Communication I/O Controller) e PK Controller:
- CIOC lose comunica col PK Controller
- Tutti i CHARMs sulla CIOC failed a update entro il tempo atteso
- Risultato: "I/O Input Failure" + "I/O Output Failure" → loops in **IMAN** mode

**Evoluzione**: È un problema di comunicazione che esiste nelle versioni elencate. Non è un NEW bug ma un problema noto tracciato con **TFSB1395629**.

### 4.2 Tracciamento modifiche

| Data | Tipo | Descrizione |
|---|---|---|
| 08 Apr 2026 | Original Release | Prima pubblicazione |

### 4.3 Trasparenza operativa

**Alta trasparenza**:
- Molto dettagliata nelle version-specific recommendations
- Elenca specificamente quale hotfix bundle per ogni versione:
  - v14.LTS → KBA NK-1900-0840
  - v14.FP3 → KBA NK-2200-0045
  - v15.FP3 → KBA NK-2400-0598
- Dichiara: "no work-around for this issue"
- Indica il TFS ticket number per tracciabilità interna (TFSB1395629)

**Limiti dichiarati**:
- Per v14.FP1, v14.FP2: no solution → upgrade
- Per v15.LTS, 15.FP1, 15.FP2: "being developed"

**Trasparenza eccellente**: Version-specific actions chiare e azionabili.

---

## 5. NK-2300-0428 — DeltaV Zones Abnormal Parameter Status

| Campo | Valore |
|---|---|
| **ID** | NK-2300-0428 |
| **Titolo** | DeltaV Zones — Abnormal Module Parameter Status Between Systems |
| **Pubblicazione** | 15 Maggio 2025 (originale: Ott 2023) |
| **Stato** | Approved |
| **Tipo** | Product Issues |
| **Azione richiesta** | Next Service Interval |

### 5.1 Evoluzione del processo

Problema di **Inter-Zone networking**:
- Remote Zone modules display Magenta + Asterisks (****)
- Status: **RT_READ_ACCESS_DENIED** (vedi WatchIt)
- Trigger: post-download, opening non-cached graphic, server redundancy switchover

L'articolo ha **tre revisioni**:
1. **20 Oct 2023**: Original Release
2. **29 Feb 2024**: Major KBA revision
3. **15 May 2025**: Updated — applicabilità a v13.3.1, v13.3.2, v14.LTS, v14.FPx; updated solution section

### 5.2 Tracciamento modifiche

| Data | Tipo | Descrizione |
|---|---|---|
| 15 May 2025 | Updated | Applicabilità a v13.3.1, v13.3.2, v14.LTS, v14.FPx |
| 29 Feb 2024 | Major revision | Evoluzione significativa |
| 20 Oct 2023 | Original Release | Prima pubblicazione |

**Nota**: KBA piu' matura con 3 revisioni. Dimostra evoluzione nel tempo.

### 5.3 Trasparenza operativa

**Molto alta trasparenza**:
- Quattro workaround dettagliati (1-4)
- Spiega il comportamento (RT_READ_ACCESS_DENIED)
- Indica che "Emerson has created an In-Analysis Logging Patch Hotfix for v14.LTS" — pro-active investigation
- Fornisce complete revision history

**Limitazioni**: ancora "no software solution" per le versioni elencate → raccomanda upgrade a v15.LTS+

**Nota**: Tracciamento TFS assente (forse prima di quando è stato aggiunto il pattern).

---

## 6. Conclusioni — Pattern Ricorrenti

### 6.1 Pattern strutturali

| Pattern | presenza |
|---|---|
| **Article Type = Product Issues** | 5/5 |
| **Required Action = Next Service Interval** | 5/5 |
| **Sezioni standard**: Introduction, Description, Work-around/Solution, Contact | 5/5 |

### 6.2 Pattern nelle soluzioni

| Pattern | KBA |
|---|---|
| **"No software solution" — raccomanda upgrade** | NK-2600-0129, NK-2600-0071, NK-2600-0082, NK-2300-0428 (4 versioni) |
| **"Being investigated / being developed"** | NK-2600-0071, NK-2600-0082 |
| **Content hotfix removed from server** | NK-2600-0097 |
| **Version-specific hotfix bundles** | NK-2600-0082 (4 diverse KBA referenziate) |

### 6.3 Pattern nel tracciamento

| KBA | Revisioni | Note |
|---|---|---|
| NK-2300-0428 | 3 | Piu' matura, dimostra evoluzione |
| NK-2600-0082 | 1 | ma referenzia TFS (bug tracking interno) |
| NK-2600-0129 | 1 | Nessun TFS |
| NK-2600-0071 | 1 | Nessun TFS |
| NK-2600-0097 | 1 | Nessun TFS |

**Deduzione**: KBA piu' vecchie (NK-2300-0428) hanno piu' revisioni. KBA piu' recenti (2026) ancora fresh. Presenza di TFS number indica integrazione con bug tracking interno.

### 6.4 Pattern di trasparenza

| Livello | KBA | Indicatori |
|---|---|---|
| **Alta** | NK-2600-0129, NK-2600-0097, NK-2600-0082, NK-2300-0428 | Recovery steps dettagliati, workaround list, limiti dichiarati |
| **Media** | NK-2600-0071 | Meccanismo spiegato ma alcune assunzioni non verificate |

### 6.5 Pattern evolutivi

| Tipo di evoluzione | KBA |
|---|---|
| **Nuova feature** | NK-2600-0129 (silent upgrade nuovo in v1.4) |
| **Legacy bug newly documented** | NK-2600-0071, NK-2600-0082 (esistevano, ora documentati) |
| **Content mismatch** | NK-2600-0097 (Microsoft update) |
| **Long-standing issue** | NK-2300-0428 (anni, multiple revisioni) |

### 6.6 Sintesi livelli di maturità

| KBA | Maturità | Score trasparenza |
|---|---|---|
| NK-2300-0428 | Alta (3 revisioni) | 9/10 |
| NK-2600-0082 | Media (TFS number, version-specific) | 8/10 |
| NK-2600-0129 | Media | 7/10 |
| NK-2600-0097 | Media | 7/10 |
| NK-2600-0071 | Bassa (nessun TFS, info parziale) | 6/10 |

---

## 7. Raccomandazioni

1. **Standardizzare la presenza di TFS/CASE numbers** —Solo NK-2600-0082 li include; utile per tracciabilità interna.

2. **Mantenere revision history completo** — La struttura per le KBA è presente ma non sempre popolata.

3. **Dichiarare sempre workaround** — NK-2600-0082 dichiara "no work-around" esplicitamente; questo è trasparente e corretto.

4. **Version-specific recommendations** — NK-2600-0082 è l'esempio migliore: ogni versione haaction chiara.

5. **Verificare coerenza con pattern esistenti** —Le KBA piu' recenti (2026) dovrebbero ereditare le best practices dalla NK-2300-0428.

---

*Fine report*