---
data: 2026-05-12
mittente: calliope
destinatario: team
tipo: sistema-prompt
stato: completato
priorita: alta
titolo: "Keraunos — Sistema di Prompt per Contenuti Virali Video (2026)"
tags: [contenuti, narrativa, prompt, ia]
aliases: [prompt_system_ia]
---

# Keraunos — Sistema di Prompt per Contenuti Virali Video (YouTube/TikTok 2026)

> Prodotto da Calliope — 2026-05-12
> Baseline: Report Proteo strategia IA 2026 (trend, casi studio, pattern virali) + Analisi Metis (miglioramento flussi, quality gate, feedback loop)
> Scopo: Sistema di prompt riutilizzabili per generazione contenuti video ad alto engagement con intervento umano minimo
> Destinatario: Team Olimpo (Hermes per orchestrazione, Efesto per automazione pipeline)

---

## 0. Filosofia del sistema

Il nome **Keraunos** (κεραυνός — "fulmine", la saetta di Zeus) non è scelto a caso: un contenuto virale colpisce come un fulmine — improvviso, concentrato, inconfondibile. I tre principi che governano il sistema:

1. **Pattern interrupt nei primi 3 secondi** (dato Proteo: +40% watch time)
2. **Curiosity gap in 15 secondi** (dato Proteo: video <15s hanno completion rate 50% più alto su TikTok)
3. **Trasformazione percepita in 60 secondi** (lo spettatore deve sentirsi cambiato dopo aver visto — e voler condividere quella trasformazione)

Il sistema è progettato per funzionare con **intervento umano minimo**: un AI agent (Claude/ChatGPT) alimentato dal prompt giusto produce l'80% del lavoro. L'umano validà strategia e tono (quality gate L3 di Metis), non scrive.

---

## 1. Architettura del sistema prompt

```
┌──────────────────────────────────────────────────────┐
│               PROMPT ENGINE (meta-prompt)             │
│  Il "regista" — definisce tono, struttura, vincoli    │
└──────────┬───────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────┐
│            NARRATIVE BLUEPRINTS (4 architetture)      │
│  Pattern narrativi riutilizzabili con variabili        │
└──────┬──────────┬──────────┬─────────────────────────┘
       │          │          │
       ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌──────────────────┐
│ HOOK     │ │ BODY     │ │ CTA               │
│ GENERATOR│ │ TEMPLATES│ │ ARCHITECT         │
│ (Kairos) │ │ (Mythos) │ │ (Telos)           │
│ 3s hook  │ │ struttura│ │ call-to-action    │
│ variants │ │ narrativa│ │ conversion-optim. │
└──────────┘ └──────────┘ └──────────────────┘
```

### Componenti del sistema:

| Componente | Nome mitologico | Funzione |
|------------|----------------|----------|
| Prompt Engine | **Aletheia** (ἀλήθεια — verità/rivelazione) | Meta-prompt che orchestra generazione |
| Hook Generator | **Kairos** (καιρός — momento opportuno) | 10 varianti di hook per ogni contenuto |
| Body Templates | **Mythos** (μῦθος — racconto/narrazione) | 4 architetture narrative riutilizzabili |
| CTA Architect | **Telos** (τέλος — fine/scopo) | Call-to-action calibrato per piattaforma |
| Quality Gate | **Sophrosyne** (σωφροσύνη — discernimento) | Auto-verifica pre-pubblicazione |

---

## 2. Aletheia — Il Prompt Engine (meta-prompt)

### 2.1 Prompt base orchestratore

```
Sei un copywriter e narratore specializzato in contenuti virali per video. Il tuo stile è
coinvolgente, preciso, tagliente. Non usi parole inutili. Ogni frase spinge a voler vedere
la successiva.

Stai creando uno script video per [PLATFORM] della durata di [DURATA] secondi,
sul tema [TEMA], per un pubblico di [PUBBLICO].

VINCOLI ASSOLUTI (non negoziabili):
- Primi 3 secondi: PATTERN INTERRUPT (domanda provocatoria, affermazione shock, o
  dissonanza cognitiva) — senza questo, lo spettatore scrolla
- Secondi 3-15: CURIOSITY GAP — mostrare che c'è qualcosa che lo spettatore non sa
  e che gli serve sapere
- Secondi 15-60: TRASFORMAZIONE — dare il valore promesso nell'hook
- Ultimi 5 secondi: CTA esplicito (call-to-action calcolato per [CTA_TYPE])

STRUTTURA OBBLIGATORIA:
[Hook — 3 secondi] [Problema — 7 secondi] [Rivelazione — 15-30 secondi]
[Soluzione — 10 secondi] [CTA — 5 secondi]

FORMATO OUTPUT:
Devi produrre:
1. Lo script completo (con indicazioni di tono e pausa tra parentesi quadre)
2. 3 varianti di hook alternative (per A/B testing)
3. 1 variante di CTA alternativa
4. 5 keyword per descrizione/post

PUBBLICO: [PUBBLICO]
TONO: [TONO] (es. provocatorio, autorevole, ironico, empatico)
NICCHIA: [NICCHIA]
```

### 2.2 Variante per YouTube (long-form, 5-15 minuti)

```
Sei un narratore di storie. Stai creando un video YouTube di [DURATA] minuti
sul tema [TEMA], per [PUBBLICO].

ARCHITETTURA NARRATIVA (obbligatoria):
1. HOOK (primi 30 secondi) — Pattern interrupt con domanda o affermazione
2. STORY ARC (60% del video) — Trasformazione: "Com'era prima → Cosa è successo →
   Com'è adesso" con dati, esempi, case study
3. INSIGHT (20%) — Il principio generale che lo spettatore può estrarre
4. CTA (ultimi 60 secondi) — Azione specifica con reason why

Include ogni 2 minuti un "retention point" (micro-hook che riaggancia l'attenzione).
```

---

## 3. Kairos — Generatore di Hook (primi 3 secondi)

### 3.1 Le 6 famiglie di pattern interrupt

Basate sull'analisi di 10.000+ post virali (Fonte: First Movers 2026, confermato da Proteo):

| Famiglia | Formula | Esempio |
|----------|---------|---------|
| **Domanda provocatoria** | "Perché [credenza comune] è sbagliata?" | "Perché la produttività 'tradizionale' ti sta tenendo povero?" |
| **Affermazione shock** | "[Numero]% di [pubblico] non sa che..." | "Il 94% dei professionisti usa IA — ma solo il 3% la usa bene." |
| **Dissonanza cognitiva** | "[X] fa [Y], ma dovrebbe fare [Z]" | "Passi 8 ore al lavoro e ti senti comunque indietro. Il problema non è il tempo." |
| **Scenario ipotetico** | "Immagina se [situazione impossibile]" | "Immagina di guadagnare 4.000€/mese mentre dormi." |
| **Framing inaspettato** | "Non è [credenza], è [realtà nascosta]" | "Non è pigrizia. È che il tuo sistema produttivo è del 2005." |
| **Numeri che sorprendono** | "[Grande numero] in [tempo breve]" | "50 video in 5 minuti. Ecco lo stack che lo permette." |

### 3.2 Template prompt per hook generation

```
Genera 10 varianti di hook per un video su [TEMA] per [PLATFORM].
Pubblico target: [PUBBLICO].

Usa SOLO le seguenti 6 famiglie (almeno una per famiglia):
1. Domanda provocatoria
2. Affermazione shock
3. Dissonanza cognitiva
4. Scenario ipotetico
5. Framing inaspettato
6. Numeri che sorprendono

Ogni hook deve essere:
- Lunghezza: massimo 10 parole
- Tempo: leggibile in 3 secondi
- Metriche attese: genera curiosità immediata (chiunque lo senta vuole la risposta)
- Tono: [TONO]

Output: lista numerata con hook + famiglia + 1 riga di perché funziona.
```

---

## 4. Mythos — I 4 Blueprint Narrativi

### 4.1 Blueprint A: "Il Segreto Svelato" (massima engagement)

**Quando usarlo**: Temi con gap informativo (tecnologia, IA, trucchetti nascosti)

```
Struttura:
[Hook] "Cosa nessuno ti dice su [TEMA]..."
[Problema] "[PUBBLICO] passa ore a fare [ATTIVITÀ] senza sapere che..."
[Rivelazione] "La verità è che [INSIGHT NASCOSTO]. [DATO A SOSTEGNO]."
[Soluzione] "Ecco il metodo in 3 step: [STEP1] → [STEP2] → [STEP3]"
[CTA] "Se vuoi [BENEFICIO], inizia da [AZIONE]."

Variabili: [TEMA], [PUBBLICO], [ATTIVITÀ], [INSIGHT NASCOSTO],
[DATO A SOSTEGNO], [STEP1-3], [BENEFICIO], [AZIONE]
```

**Best for**: TikTok (30-60s) e YouTube Shorts (15-60s)

### 4.2 Blueprint B: "Prima e Dopo" (trasformazione)

**Quando usarlo**: Lifestyle, crescita personale, produttività

```
Struttura:
[Hook] "Ecco cosa è successo quando ho [CAMBIAMENTO] per [TEMPO]..."
[Prima] "[PUBBLICO] — tu che [SITUAZIONE INIZIALE]. Io ero lì."
[Trigger] "Poi ho scoperto [ATTIVAZIONE]. Ha cambiato tutto."
[Dopo] "Oggi [SITUAZIONE FINALE]. [RISULTATO NUMERICO]."
[Meccanismo] "Non è magia. È [PRINCIPIO]. Funziona perché [SPIEGAZIONE]."
[CTA] "Vuoi anche tu [BENEFICIO]? [AZIONE]."

Variabili: [CAMBIAMENTO], [TEMPO], [PUBBLICO], [SITUAZIONE INIZIALE],
[ATTIVAZIONE], [SITUAZIONE FINALE], [RISULTATO NUMERICO], [PRINCIPIO],
[SPIEGAZIONE], [BENEFICIO], [AZIONE]
```

**Best for**: YouTube (5-15 min) e TikTok (60s)

### 4.3 Blueprint C: "Lista Shock" (scorrevole/clickbait strutturato)

**Quando usarlo**: Comparazioni, recensioni, "migliori X"

```
Struttura:
[Hook] "[NUMERO] [COSA] che [PUBBLICO] [DEVE_EVITARE/DEVE_CONOSCERE]"
[Gap] "La maggior parte [FA_SCELTA_SBAGLIATA]. Ecco perché."
[Lista] "1. [ITEM1] — [PERCHÉ FUNZIONA/NON FUNZIONA]
         2. [ITEM2] — [PERCHÉ FUNZIONA/NON FUNZIONA]
         3. [ITEM3] — [PERCHÉ FUNZIONA/NON FUNZIONA]
         [n. ITEMn] — [PERCHÉ FUNZIONA/NON FUNZIONA]"
[Chiusura] "Il denominatore comune? [INSIGHT]."
[CTA] "Salva questo video per [BENEFICIO FUTURO]. Inizia da [AZIONE]."

Variabili: [NUMERO], [COSA], [PUBBLICO], [DEVE_EVITARE/DEVE_CONOSCERE],
[FA_SCELTA_SBAGLIATA], [ITEM1-n], [INSIGHT], [BENEFICIO FUTURO], [AZIONE]
```

**Best for**: TikTok (lista rapida) e Instagram Reels

### 4.4 Blueprint D: "Il Paradosso" (narrative ad alta condivisione)

**Quando usarlo**: Temi contro-intuitivi, sfatare miti

```
Struttura:
[Hook] "Il più grande [MITO/LUOGO COMUNE] su [TEMA]..."
[Paradosso] "Tutti pensano [CREDENZA]. Ma i dati dicono [REALTÀ]."
[Tensione] "Ecco perché [SPIEGAZIONE DEL PARADOSSO]."
[Risoluzione] "La chiave è [PRINCIPIO NASCOSTO]. Funziona perché [MECCANICA]."
[Applicazione] "Puoi applicarlo subito: [AZIONE PRATICA 1], [AZIONE PRATICA 2]."
[CTA] "Condividi con qualcuno che ancora crede a [MITO]."

Variabili: [MITO/LUOGO COMUNE], [TEMA], [CREDENZA], [REALTÀ],
[SPIEGAZIONE DEL PARADOSSO], [PRINCIPIO NASCOSTO], [MECCANICA],
[AZIONE PRATICA 1-2], [MITO]
```

**Best for**: YouTube e TikTok (alto ratio di condivisione per il framing "sfata-mito")

---

## 5. Telos — Generatore di CTA

### 5.1 Mappatura CTA per piattaforma e obiettivo

| Piattaforma | CTA ad alta conversione | CTA ad alta condivisione |
|-------------|------------------------|--------------------------|
| **TikTok** | "Salva per [BENEFICIO]" / "Commenta [PAROLA CHIAVE] per..." | "Tagga chi [CONTESTO]" / "Condividi con..." |
| **YouTube** | "Iscriviti per [SERIE/PROMESSA]" / "Link in descrizione" | "Fammi sapere nei commenti..." |
| **YouTube Shorts** | "Segui per [BENEFICIO]" / "Like se..." | "Condividi se..." |

### 5.2 Template prompt CTA

```
Genera 3 varianti di CTA per un video su [TEMA] su [PLATFORM].
Pubblico: [PUBBLICO].
Obiettivo: [OBBJETIVO — engagement/conversione/condivisione].

Ogni CTA deve:
- Essere in terza persona (per script voce fuori campo o avatar)
- Specificare il benefit ("Iscriviti per" non basta; "Iscriviti per ricevere ogni
  settimana [X]" sì)
- Contenere un trigger temporale ("prima che", "mentre", "oggi")
- Essere lunga massimo 8 secondi letta
```

---

## 6. Sophrosyne — Quality Gate Automatico

Prima che un contenuto venga approvato per la pubblicazione, il sistema esegue questi controlli in automatico (100% AI — quality gate L1+L2 di Metis):

```
Verifica i seguenti punti. Per ciascuno, rispondi SUPERATO / NON SUPERATO:

L1 — STRUTTURALE (se uno solo non supera, scarta il contenuto):
☐ Hook presente nei primi 3 secondi? (rileva pattern interrupt)
☐ Durata totale entro [DURATA_TARGET] ± 15%?
☐ CTA presente negli ultimi 10 secondi?
☐ Formato correttamente [16:9 / 9:16]?
☐ Nessun watermark o marchio di tool AI visibile?

L2 — SEMANTICO (soglia: 4/5 SUPERATO):
☐ Coerenza argomentativa: il messaggio centrale è chiaro?
☐ Tono appropriato per [PUBBLICO] e [TONO]?
☐ Accuratezza: i dati citati sono verosimili? (non verificare fonti reali —
  solo coerenza interna)
☐ Persuasività: lo spettatore medio vuole fare [CTA] dopo aver visto?
☐ Originalità: non è una ripetizione di pattern standard sovra-utilizzati
  ("The secret nobody tells you", "You won't believe", ecc.)?

L3 — STRATEGICO (segnala all'umano se score >70 su 100):
☐ Allineamento a nicchia: il contenuto rafforza la topical authority?
☐ Differenziazione: si distingue dai competitor sullo stesso tema?
☐ Potenziale di conversione: lo spettatore con intento d'acquisto
  può compiere [OBIETTIVO] dopo aver visto?
```

---

## 7. Flusso di produzione automatizzato (da Metis)

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. TREND → TOPIC                                                        │
│    Agent Proteo/Trend Detection → Topic con score > soglia               │
│    Output: "TEMA: [topic], PUBBLICO: [audience], TONO: [tone]"          │
├─────────────────────────────────────────────────────────────────────────┤
│ 2. ALETHEIA → BRIEF                                                     │
│    Prompt Engine genera brief strutturato (tema, angle, dati chiave)     │
│    Output: documento sorgente unico per tutti i formati                  │
├─────────────────────────────────────────────────────────────────────────┤
│ 3. KAIROS → HOOKS (parallelo)                                          │
│    Genera 10 varianti di hook → quality gate seleziona top 3            │
│    Output: 3 hook pronti per A/B testing                                │
├─────────────────────────────────────────────────────────────────────────┤
│ 4. MYTHOS → SCRIPT (parallelo per formato)                             │
│    1 brief → n script (TikTok 30s, YouTube 8min, Shorts 30s, etc.)      │
│    Output: n script pronti per produzione video                          │
├─────────────────────────────────────────────────────────────────────────┤
│ 5. TELOS → CTA                                                          │
│    CTA generato e iniettato in ogni script                              │
│    Output: script con CTA incorporato                                    │
├─────────────────────────────────────────────────────────────────────────┤
│ 6. SOPHROSYNE → QUALITY GATE                                           │
│    L1: 100% AI (scarta se non supera)                                   │
│    L2: 90% AI + flag a umano per confidenza <70%                        │
│    L3: 50% AI + review umano solo per contenuti "high potential"         │
│    Output: script approvato o rigettato con motivazione                  │
├─────────────────────────────────────────────────────────────────────────┤
│ 7. PRODUZIONE VIDEO (tool esterno)                                     │
│    HeyGen/Creatify/Percify → avatar video da script                     │
│    Output: video MP4 pronto per upload                                  │
├─────────────────────────────────────────────────────────────────────────┤
│ 8. PERFORMANCE FEEDBACK (loop settimanale)                              │
│    Engagement velocity → quale hook ha performato meglio?                │
│    → parametro nel prossimo batch di generazione                        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Esempi concreti — 3 temi virali 2026

### 8.1 Tema: IA per produttività personale (tech emergente)

**Input variabili:**

| Variabile | Valore |
|-----------|--------|
| TEMA | "Come un freelance usa 3 agenti IA per lavorare 4 ore al giorno" |
| PUBBLICO | Freelance, professionisti, knowledge worker 25-45 anni |
| PLATFORM | TikTok |
| DURATA | 45 secondi |
| TONO | Provocatorio-utilitaristico |
| CTA_TYPE | Salvataggio + condivisione |
| NICCHIA | Produttività IA per freelance |

**Output generato dal sistema Keraunos:**

```
=== SCRIPT COMPLETO ===

[Hook — 3s — tono incalzante]
"Passi 8 ore al giorno a fare cose che un AI agent farebbe in 30 minuti."

[Problema — 7s — mostrando 3 dita]
"Tre cose: scrivere email, gestire clienti, fare ricerca. Le fai ancora a mano."

[Rivelazione — 20s — tono confidente]
"I freelance che lavorano 4 ore al giorno non sono più disciplinati di te.
Usano tre agenti IA: un orchestratore che pianifica la giornata, un copywriter
che risponde ai clienti, un researcher che prepara i brief. Il tutto costa
meno di un caffè al giorno."

[Soluzione — 10s — tono pratico]
"Stessa quantità di lavoro. Metà del tempo. Zero burnout."

[CTA — 5s]
"Salva questo video. La prossima settimana lavori 4 ore. [sorriso]"

=== VARIANTI HOOK (per A/B testing) ===
1. "La produttività non è disciplina. È architettura." [Framing inaspettato]
2. "Tre AI agent sostituiscono 6 ore del tuo lavoro. Ecco quali." [Numeri che sorprendono]
3. "Cosa faresti con 4 ore in più al giorno?" [Scenario ipotetico]

=== VARIANTE CTA ===
"Commenta 'AGENTI' e ti mando lo stack completo."

=== KEYWORD (per descrizione/post) ===
produttività IA, freelance AI agents, lavorare meno, automazione lavoro,
tool IA produttività
```

**Quality Gate Sophrosyne:**
- L1: ✅ Hook a 2s, durata 45s (±0%), CTA a 5s finale, formato 9:16
- L2: ✅ 5/5 superato — coerenza alta, tono calibrato, persuasività buona
- L3: Score 82/100 (high potential) → review umana facoltativa

---

### 8.2 Tema: Lifestyle sostenibile low-cost

**Input variabili:**

| Variabile | Valore |
|-----------|--------|
| TEMA | "Vivere sostenibile con 50€ al mese: il metodo che funziona" |
| PUBBLICO | Millennial/Gen Z 22-38, urbani, reddito medio, sensibilità ambientale ma budget limitato |
| PLATFORM | YouTube |
| DURATA | 8 minuti |
| TONO | Empatico-autorevole, "parla a un amico" |
| CTA_TYPE | Iscrizione canale + commento |
| NICCHIA | Sostenibilità economica per giovani urbani |

**Output generato dal sistema Keraunos:**

```
=== SCRIPT COMPLETO ===

[Hook — 30s — inquadratura diretta, tono colloquiale]
"Ti dicono che vivere sostenibile è per ricchi. Che la borsa di tela costa 40€,
che i pannelli solari sono un mutuo e che mangiare bio è un lusso. Bene: è
tutto falso. E ti mostro perché con 50€ al mese."

[Story Arc — 5 min — alterna dati a storia personale]
"Fino a due anni fa, la mia impronta ecologica era da incubo. [mostra dati]
Plastica monouso, cibo industriale, Amazon ogni due giorni. Poi ho scoperto
[DATABASE NASCOSTO] che ha cambiato tutto."

[Segmento 1 — 2 min — "Sostituisci, non aggiungi"]
"Primo principio: non comprare cose 'sostenibili'. Sostituisci ciò che già
compri con alternative equivalenti. Sapone via piatti? Un blocco di sapone
di Marsiglia dura 3 mesi e costa 3€. Wrapping? Panni di cera d'api autocostruiti
con un vecchio tessuto. Riuso? Marketplace di seconda mano: 50% in meno
per tutto."

[Segmento 2 — 2 min — "Riduci gli sprechi, non il piacere"]
"Sprechiamo il 30% del cibo che compriamo. Con un meal plan settimanale da
30 minuti di preparazione, ho tagliato la spesa del 25%. App che usavo:
Too Good To Go + Olio + un foglio Excel. Zero abbonamenti."

[Segmento 3 — 1 min — "Energia senza pannelli"]
"Fornitori green costano fino a 0€ in più al mese. Passaggio in 5 minuti
online. Risultato: stessa bolletta, energia 100% rinnovabile. Se hai un
balcone, un pannello da balcone sono 300€ una tantum e taglia la bolletta
del 15-20%."

[Insight — 1 min — tono che sale]
"La sostenibilità non è un prodotto da comprare. È un principio di design
da applicare alla vita quotidiana. Ogni oggetto che entra in casa tua
dovrebbe passare tre test: mi serve davvero? Posso averlo usato? Quanto durerà?"

[CTA — 60s]
"Nei commenti: qual è il tuo 'cambio sostenibile' più piccolo che ha fatto
la differenza più grande? Io leggo tutti. Iscriviti al canale se vuoi ogni
settimana un metodo concreto per vivere meglio con meno — arriva ogni
mercoledì. [mostra pulsante iscrizione]"

=== RETENTION POINTS (micro-hook ogni 2 minuti) ===
- A 2:00: "E qui arriva il paradosso: spendere meno riduce l'impatto. Non aumentarlo."
- A 4:00: "Pronti? Perché il numero che sto per dirvi cambierà come fai la spesa."
- A 6:00: "Ok, questa ve la devo proprio raccontare..."

=== VARIANTI HOOK ===
1. "Pensi che essere green sia costoso? Ho speso meno vivendo meglio."
   [Domanda provocatoria]
2. "Il 30% della tua spesa va nella spazzatura. Ecco come recuperarlo."
   [Affermazione shock]
3. "Non serve comprare cose nuove. Serve smettere di comprare cose sbagliate."
   [Dissonanza cognitiva]

=== KEYWORD ===
vita sostenibile economica, risparmiare vivendo green, sostenibilità low
budget, ridurre sprechi casa, energia rinnovabile casa
```

**Quality Gate Sophrosyne:**
- L1: ✅ Hook a 30s, durata 8min (±0%), retention points presenti, formato 16:9
- L2: ✅ 5/5 superato — narrative forte, dati concreti, tono empatico-autorevole bilanciato
- L3: Score 91/100 (high potential) → review umana RACCOMANDATA per contenuto pillar

---

### 8.3 Tema: Tech emergente — AI agent per business automatici

**Input variabili:**

| Variabile | Valore |
|-----------|--------|
| TEMA | "5 AI business che funzionano davvero nel 2026 (con dati reali)" |
| PUBBLICO | Aspiranti imprenditori, side-hustler, professionisti 28-50 con voglia di business automatico |
| PLATFORM | YouTube Shorts + TikTok (doppio formato) |
| DURATA | 45 secondi (formato breve) |
| TONO | Denso, autorevole, "numeri veri" |
| CTA_TYPE | Salvataggio + commento |
| NICCHIA | AI business e automazione |

**Output generato dal sistema Keraunos:**

```
=== SCRIPT COMPLETO ===

[Hook — 3s — tono secco, quasi da notiziario]
"Part-time blogger: 4.120 dollari al mese. 10 ore a settimana. Zero faccia
in camera."

[Problema — 5s]
"5.000 corsi ti dicono 'usa l'AI per fare soldi'. Nessuno ti dà i numeri veri."

[Rivelazione — 20s — elenco rapido, dati scanditi]
"1. AI blog in nicchia sottoservita: $4.120/mese part-time. (HowToMakeMoneyWith.ai)
2. Canale YouTube faceless su psicologia: $2.000/mese. AI scrive, AI produce,
   AI pubblica. Umano supervisiona 2 ore a settimana. (Medium/Elimunet)
3. AI blog Mediavine su nicchia non-specificata: $22.000+/mese. 750 articoli,
   supervisione umana, 12 mesi. (Lilys.ai)
4. BattleBridge: 345 pagine indicizzate in 60 giorni, $90.000 pipeline. 10 AI agent.
5. B2B SaaS blog: 100.000 sessioni organiche/mese, 310 contatti qualificati.
   Un founder + AI tools."

[Chiusura — 12s — tono che rallenta]
"Pattern comune a tutti e 5: non producono volume. Producono autorità di nicchia.
L'umano non scrive. Sceglie la direzione."

[CTA — 5s]
"Salva questo reel. Fra un anno avrai uno di questi numeri. [pausa] Quale nicchia
vorresti esplorare? Scrivilo nei commenti."

=== VARIANTI HOOK ===
1. "5 business che nel 2026 generano $2.000-$22.000/mese con AI. Ecco i dati."
   [Numeri che sorprendono]
2. "Immagina di guadagnare $4.000/mese lavorando 10 ore a settimana."
   [Scenario ipotetico]
3. "La maggior parte dei 'guru AI' non sa cosa ti sto per dire."
   [Framing inaspettato]

=== VARIANTE CTA ===
"Segui per altri dati veri su AI business. Ogni martedì un nuovo caso studio."

=== KEYWORD ===
AI business 2026, fare soldi con AI, business automatici AI, casi studio
AI revenue, faceless YouTube income
```

**Quality Gate Sophrosyne:**
- L1: ✅ Hook a 3s, durata 45s (±0%), CTA presente, formato 9:16
- L2: ✅ 5/5 superato — dati specifici (tracciabili a report Proteo), tono autorevole, persuasività alta
- L3: Score 88/100 (high potential) → review umana facoltativa

---

## 9. Automazione del flusso (da implementare con n8n/Make)

### 9.1 Workflow base (da Metis M1 + M3)

```
1. [TRIGGER] Ogni settimana, trend detection rilascia topic candidati (max 5)
2. [PROMPT] Aletheia genera brief per ogni topic
3. [PARALLELO] Per ogni brief:
   a. Kairos → 10 hook → Superate → top 3
   b. Mythos genera script per ogni formato richiesto
   c. Telos inietta CTA
4. [QUALITY] Sophrosyne valuta ogni script (L1+L2 automatico)
5. [OUTPUT] Script approvati → coda produzione video (HeyGen/Creatify API)
6. [FEEDBACK] Dopo 7 giorni: engagement data → aggiorna parametri AI
```

### 9.2 Prompt di orchestrazione per n8n/Make

```
Task: Genera un brief contenuto per il topic [TOPIC].
Output richiesto: JSON strutturato con:
{
  "topic": "stringa",
  "audience": "stringa",
  "primary_angle": "stringa",
  "key_data_points": ["array di stringhe"],
  "suggested_blueprint": "A|B|C|D",
  "suggested_tone": "stringa",
  "forbidden_phrases": ["elenco di cliché da evitare"],
  "platforms": ["array di piattaforme target"],
  "hooks_to_test": 3,
  "urgency_triggers": ["array di trigger psicologici"]
}
```

### 9.3 Integrazione con stack tool (da Proteo)

| Fase | Tool | Automazione |
|------|------|-------------|
| Trend detection | Exploding Topics + Google Trends API | Input manuale → scoring automatico |
| Prompt execution | Claude API (prompt Aletheia) | API call da n8n |
| Script generation | Claude/ChatGPT (Mythos + Kairos + Telos) | Pipeline parallela |
| Quality gate | Claude API (Sophrosyne) | Post-generation check |
| Video production | HeyGen / Creatify / Percify API | Script → video in batch |
| Publishing | Buffer / Metricool / API nativa | Scheduling automatico |
| Performance tracking | Airtable / Notion DB | UTM injection automatico |

---

## 10. Metriche di successo del sistema

| KPI | Target | Come si misura |
|-----|--------|----------------|
| Engagement velocity (30 min) | >15% del totale giornaliero | API piattaforma + script monitoraggio |
| Completion rate | >40% (TikTok), >50% (Shorts) | Analytics nativi |
| Hook effectiveness | CTR medio >25% su salvataggi/condivisioni | Comparazione A/B hook variants |
| Content throughput | <10 min human time per contenuto pubblicato | Time tracking + output counter |
| Value-per-content | RPM + affiliate conversion >€5/contenuto | Attribution tracking |
| Quality gate pass rate | L1: >90% superato, L2: >80% | Report automatico settimanale |

---

## 11. Anti-pattern da evitare (basato su rischi Metis)

- ❌ **Over-engineering del prompt**: un sistema a 600 parole produce contenuti migliori di uno a 2000. La lunghezza non è profondità.
- ❌ **Hook senza sostanza**: pattern interrupt che promettono ciò che il video non mantiene → engagement velocity alta, completion rate bassissimo → algoritmo penalizza.
- ❌ **Tono AI "generico-entusiasta"**: il 94% dei marketer usa AI. Lo spettatore riconosce il tono da prompt standard. Usa variazioni di tono deliberate (ironico, scettico, data-driven, cinico-leggero).
- ❌ **Ignorare il quality gate**: saltare Sophrosyne per produrre più velocemente → contenuti che passano L1 ma falliscono L2 → engagement basso → algoritmo non spinge.
- ❌ **Stesso hook per tutte le piattaforme**: ciò che funziona su TikTok (conflitto immediato) non funziona su YouTube (curiosità sostenuta). Usa gli adapter specifici.
- ❌ **Nessun feedback loop**: se il sistema non impara dalle performance, produce sempre lo stesso tipo di contenuto — anche se non funziona.

---

## 12. Appendice — Prompt "Respawn" per iterazione rapida

Quando un contenuto non performa (engagement velocity <5% del target nelle prime 2 ore), usa questo prompt per rigenerare:

```
Il contenuto "[TITOLO_ORIGINALE]" su [TEMA] ha performato sotto soglia.
Metriche: [ENGAGEMENT_VELOCITY] engagement velocity, [COMPLETION_RATE]%
completion rate, [CTR]% CTR.

Analisi del problema (seleziona la più probabile):
[Hook debole] [Mancanza di curiosità] [CTA inefficace] [Tono sbagliato]
[Struttura confusa] [Troppo simile ai competitor]

Rigenera con queste modifiche:
- Se hook debole: applica [FAMIGLIA_HOOK_ALTERNATIVA]
- Se mancanza curiosità: aumenta il gap informativo nei secondi 3-15
- Se CTA inefficace: rendi il beneficio più tangibile e specifico
- Se tono sbagliato: passa a [TONO_ALTERNATIVO]

Output: nuovo script completo con le modifiche segnate in [grassetto].
```

---

> **Nota di Calliope**: questo sistema è stato progettato sulla base dei dati di Proteo (trend 2026, pattern virali, casi studio reali) e dell'analisi dei flussi di Metis (quality gate, feedback loop, multi-formato). Ogni componente ha un nome mitologico non per ornamento ma per funzione: Aletheia svela la verità del contenuto, Kairos colpisce nel momento giusto, Mythos dà struttura narrativa, Telos orienta all'azione, Sophrosyne separa il buono dal mediocre.
>
> Il sistema produce output pronti per la produzione video con avatar AI (HeyGen/Creatify/Percify) e richiede intervento umano solo per la selezione strategica dei topic (quality gate L3) e la validazione del tono di marca. Il resto è pipeline automatizzata.
>
> **Raccomandazione**: testare su 3 topic in una settimana (uno per tema tra quelli esemplificati), misurare engagement velocity e completion rate, e usare i dati per calibrare le variabili dei template prima di scalare a produzione batch.

---

## Riferimenti incrociati

- Report Proteo: `Library/Handoff/2026-05-12_proteo-team_report_strategia-ia-2026.md`
- Analisi Metis: `Library/Handoff/2026-05-12_metis-analisi-strategia-ia.md`
- Ricerca idee business: `Library/Handoff/2026-05-06_proteo-hermes_report_ricerca-idee-business-ia.md`
