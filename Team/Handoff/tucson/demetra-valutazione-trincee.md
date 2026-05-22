---
progetto: Tucson
autore: Demetra
data: 2026-05-09
tags: [tucson, triceee, water-harvesting, demetra]
status: bozza
---

# Valutazione sistema "Triceee" — Trincee organiche profonde per water harvesting

## Riferimento
Sistema proposto come alternativa/evoluzione degli swales descritti in `analisi-ecologica_v1.md` §3.1. Terreno: 250 acri Sud Tucson, suolo Typic Calciargid, clima BWh (Sonoran Desert).

---

## 1. Idrologia e bilancio idrico

### 1.1 Volume di cattura per metro lineare

Trincea: profondità 2.5 m, larghezza stimata 1.5 m (scavo minimo operativo). Sezione trasversale = 3.75 m²/m lineare. Porosità efficace degli strati (stima):

| Strato | Spessore (m) | Porosità efficace | Volume acqua/m lineare |
|---|---|---|---|
| Sassi fondo | 0.3 | 0.35 | 0.16 m³ |
| Legno/tronchi | 0.6-0.8 | 0.55 | 0.62 m³ |
| Terra | 0.4 | 0.40 | 0.24 m³ |
| Biochar+organico | 0.4-0.6 | 0.60 | 0.45 m³ |
| Copertura terra | 0.3 | 0.40 | 0.18 m³ |
| Sassi superficie | 0.1 | 0.35 | 0.05 m³ |
| **Totale** | **2.5** | — | **~1.7 m³/m** |

Ogni metro lineare di trincea può immagazzinare ~1.7 m³ di acqua. Con 269 mm/anno di pioggia, **un metro di trincea intercetta la precipitazione diretta di ~6.3 m² di superficie** (1.7 m³ ÷ 0.269 m). Per riempire la trincea servono ~6-7 eventi monsonici consecutivi di 25+ mm, oppure un singolo evento estremo (>40 mm) con runoff concentrato.

### 1.2 Rischio di saturazione/ristagno

Il suolo Typic Calciargid ha drenaggio "buono" e permeabilità moderatamente lenta. La falda è a 30-100 m. **Il rischio di saturazione prolungata è basso** per tre ragioni:

1. Il deficit idrico annuo è ~1,900 mm — il suolo asciutto assorbe rapidamente.
2. La trincea rompe il caliche (orizzonte cementato a 10-40 cm), eliminando il principale orizzonte di impedenza al drenaggio verticale.
3. Lo strato di sassi sul fondo crea una zona drenante permanente.

**Rischio residuo**: dopo eventi monsonici estremi (>50 mm in <2 h), la trincea potrebbe saturarsi temporaneamente (24-72 h). In quel lasso, la parte bassa in legno potrebbe andare in anaerobiosi. Con interruzioni ogni 5-6 m, l'acqua in eccesso trabocca lateralmente, riducendo il rischio.

### 1.3 Camino di aerazione: evaporazione o infiltrazione?

I tubi di cartone Ø200-300 mm riempiti di sassi, verticali, creano un condotto preferenziale. **Bilancio idrotermico**:

- **Evaporazione**: in ambiente desertico con ETP 2,200 mm/anno, un tubo verticale aperto in superficie agisce come una *ciminiera evaporativa*. L'aria calda e secca (T >40 °C in estate) entra nel tubo, si riscalda a contatto con le pareti, sale per convezione e trascina vapore acqueo dagli strati profondi. Con tubo di 2.5 m × Ø250 mm, la superficie evaporativa equivalente è ~0.2 m² per tubo. Due tubi per tratto = ~0.4 m². **Stima: 15-25 L/anno per tubo di perdita evaporativa** — trascurabile sul volume totale (~1,700 L/m), ma non irrilevante in un bilancio desertico.

- **Infiltrazione**: durante la pioggia, i tubi incanalano l'acqua direttamente in profondità, bypassando gli strati superficiali. Questo è l'effetto desiderato. **Il problema è che funzionano anche in assenza di pioggia — in direzione opposta.**

**Giudizio**: i camini così progettati sono controproducenti. L'effetto evaporativo continuo (365 giorni/anno) supera il beneficio dell'infiltrazione rapida (pochi eventi/anno). **Raccomandazione**: trasformarli in semplici colonne drenanti (sassi, senza tubo superficiale, coperte da uno strato di terra di 15-20 cm) oppure dotarli di valvola unidirezionale (flap) che si apra solo durante l'infiltrazione.

### 1.4 Confronto con swales tradizionali (0.4 m)

| Parametro | Swale 0.4 m | Trincea 2.5 m |
|---|---|---|
| Volume stoccaggio/m lineare | ~0.3 m³ | ~1.7 m³ (5.7×) |
| Profondità di infiltrazione | 0-0.4 m (sopra caliche) | 0-2.5 m (oltre caliche) |
| Evaporazione da superficie | Alta (acqua superficiale) | Media (acqua protetta da strati) |
| Erosione da runoff intenso | Richiede spillway | Minore (trincea più profonda) |
| Costo scavo/m lineare | 1× | ~6-8× |
| Impatto sul caliche | Scasso superficiale | Rottura completa |
| Rischio anaerobiosi | Nullo (poco profondo) | Presente (solo fondo) |

**Il vantaggio idrologico principale della trincea è portare l'acqua oltre il caliche.** Gli swales tradizionali operano sopra l'orizzonte cementato; l'acqua infiltrata ristagna nel primo metro e evapora nei giorni successivi. La trincea crea un *bypass* del caliche, portando l'acqua negli orizzonti profondi dove l'evaporazione è minima e lo stoccaggio è protetto.

### 1.5 Perdita per evaporazione dalla superficie esposta

La trincea ha ~1.5 m² di superficie esposta per metro lineare (fondo + pareti fino alla copertura). Con pacciamatura di sassi superficiali (strato 6), l'evaporazione diretta è ridotta del 60-80% rispetto a suolo nudo. Stima: 80-120 mm/anno di perdita evaporativa dalla superficie della trincea, equivalente a ~120-180 L/anno per metro lineare — circa il 10% del volume stoccato. **Accettabile**, ma migliorabile con pacciamatura più spessa o copertura con ghiaia fine.

---

## 2. Dinamiche del suolo

### 2.1 Scavo in Typic Calciargid con caliche

Il profilo:
- **0-10 cm**: loam/clay loam, crosta superficiale — scavabile con mezzi leggeri (miniescavatore 3-5 t)
- **10-40 cm**: orizzonte calcico (CaCO₃ 15-35%), da granulare a cementato — richiede escavatore medio (>8 t) con dente ripper
- **40-150+ cm**: materiale calcareo meno cementato, intercalato da lenti di loam — scavabile con escavatore medio-pesante

**La fattibilità con "mezzi leggeri" è irrealistica** per i primi 40 cm se il caliche è continuo e cementato. Il caliche del sito è descritto come "orizzonte cementato" — serve un escavatore cingolato ≥12 t con martello idraulico o ripper per la rottura iniziale. Per 250 acri con trincee discontinue, il costo di scavo diventa *significativamente* superiore agli swales.

**Esempio**: se ogni acro ha 50 m lineari di trincea (stima minima per copertura significativa), 250 acri × 50 m = 12,500 m lineari × 3.75 m³/m = ~47,000 m³ di scavo. Un volume enorme per un progetto di riforestazione.

### 2.2 Rischio collasso pareti

Trincea di 2.5 m in materiale non coesivo/coesivo alternato:
- Il caliche cementato tiene bene (autoportante)
- Gli orizzonti loamici intermedi possono franare se bagnati
- La zona di contatto caliche/loam è piana di debolezza

**Rischio reale**: durante o dopo un evento monsonico, l'acqua satura le pareti di loam, riducendo la coesione apparente. Frane localizzate possono occludere gli interstizi del biochar/compost, vanificando la funzione del sistema.

**Mitigazione**: pareti inclinate (scavo a trapezio, rapporto 1:3), ma ciò aumenta il volume di scavo del ~40%.

### 2.3 Effetto sulla falda (30-100 m)

L'acqua infiltrata a 2.5 m deve percorrere 27.5-97.5 m nella zona vadosa. Con permeabilità moderatamente lenta del Typic Calciargid (Ksat stimata 1-10 mm/h), il fronte di bagnatura si muove a ~0.5-2 m/anno. **Tempo di arrivo stimato alla falda: 15-200 anni**, a seconda della profondità locale e della macroporosità.

L'effetto sulla ricarica della falda è **trascurabile su scala di progetto (20-25 anni)**. La trincea funge da *serbatoio edafico* per le radici, non da struttura di ricarica acquifera. Questo non è un difetto — è coerente con l'obiettivo di water harvesting per la vegetazione.

### 2.4 Salinità: mobilizzazione salina

Rischio concreto. Il Typic Calciargid ha:
- Carbonati abbondanti (CaCO₃ 15-35%)
- Capillarità elevata
- Evaporazione intensa in superficie

Scavando a 2.5 m si possono intercettare orizzonti con accumuli salini (NaCl, CaSO₄·2H₂O) formatisi in cicli climatici pregressi. L'acqua infiltrata nella trincea può:
1. Dissolvere i sali profondi
2. Portarli in soluzione
3. Risalire per capillarità (specialmente nei periodi secchi)

**Rischio massimo**: se la trincea non viene completamente riempita e rimane con acqua nei mesi caldi, l'evaporazione concentra i sali in superficie, creando una zona salina intorno alla trincea — tossica per le radici.

**Mitigazione**: (a) garantire drenaggio sempre libero (strato di sassi continuo sul fondo), (b) non lasciare acqua stagnante nella trincea, (c) monitorare EC (conductività elettrica) del suolo intorno alla trincea nel primo anno, (d) usare specie tolleranti la salinità (*Prosopis velutina*, *Atriplex canescens*) nelle zone più a rischio.

**Giudizio**: rischio moderato, gestibile con monitoraggio e progettazione attenta del drenaggio basale.

### 2.5 Mantenimento della porosità nel tempo

| Strato | Porosità iniziale | Degrado previsto | Tempo stimato |
|---|---|---|---|
| Sassi fondo | 35% | Stabile (nessun degrado) | Permanente |
| Legno/tronchi | 55% | Decomposizione, assestamento, occlusione interstizi | 3-10 anni |
| Terra di riporto | 40% | Compattazione da assestamento | 1-3 anni |
| Biochar + organico | 60% | Biochar stabile; organico decomposto in 1-5 anni | 10+ anni (biochar) |
| Copertura terra | 40% | Compattazione da pioggia e traffico | 1-2 anni |
| Sassi superficie | 35% | Stabile | Permanente |

**Rischio principale**: lo strato di legno è il tallone d'Achille. Decomponendosi, perde volume e crea vuoti. La terra sovrastante può collassare nei vuoti, occludendo la porosità. Il biochar è stabile, ma se mescolato a composto organico, il composto si degrada rapidamente.

**Raccomandazione**: aumentare la proporzione di biochar vs. composto organico (70:30 invece di 50:50); usare legno duro desertico (*Prosopis*, *Olneya*) che si decompone molto lentamente; separare gli strati con geotessuto biodegradabile (fibra di cocco) per evitare migrazione di fini.

---

## 3. Stralci organici e funghi

### 3.1 Funghi locali del Sonoran Desert

Il Sonoran Desert ospita una comunità fungina adattata a stress idrico e temperature estreme. Specie documentate nell'Arizona Upland:

**Micorrizici (ECM — ectomicorrizici)**:
- *Pisolithus tinctorius* — ECM di *Prosopis*, *Olneya*, *Quercus* spp. Tolera pH alcalino, suoli poveri, alta temperatura. Già usato in riforestazione desertica. Produce sporocarpi in condizioni di stress — indicatore di adattamento.
- *Rhizopogon* spp. — ECM di pini e querce (non rilevante qui, perché le specie target sono leguminose)
- *Scleroderma* spp. — ECM di latifoglie desertiche, tollerante siccità

**Micorrizici (AM — arbuscolari)**:
- *Glomus* spp., *Gigaspora* spp. — simbionti obbligati di Larrea tridentata, cactacee, graminacee desertiche. Dominano la comunità fungina del suolo del Sonoran. Formano ife extraradicali che trasportano acqua e nutrienti anche in suolo secco.

**Saprobi (decompositori di legno)**:
- *Schizophyllum commune* — onnipresente, anche su legno in ambiente desertico. Decompositore primario di rami e tronchi esposti. Tollerante a siccità estrema (entra in dormienza metabolica).
- *Podaxis pistillaris* — fungo coprofilo/saprobio caratteristico dei deserti; segnalato su lettiera di Larrea e Prosopis. Sporocarpo adattato a disseccamento e reidratazione.
- *Agaricus* spp. deserticoli — decompositori di lettiera (A. aridicola, A. deserticola)

**Funghi per il sistema Triceee**: i candidati migliori per inoculo sono:
- *Pisolithus tinctorius* — ECM per leguminose arboree, tolleranza eccezionale a stress
- *Glomus* spp. autoctone — AM per lo strato erbaceo/arbustivo (da suolo non disturbato già presente)
- *Schizophyllum commune* — decompositore del legno interrato (già presente, non serve inoculo)

**Nota critica**: la presenza di funghi nel suolo desertico a 2.5 m di profondità è *molto bassa*. La maggior parte della biomassa fungina è concentrata nei primi 20 cm. Inoculare funghi a 2.5 m può funzionare solo se c'è un substrato organico sufficiente e un contatto con le radici (micorrizici) o con legno (saprobi). Per le ECM, la profondità massima di colonizzazione radicale di *Prosopis* può raggiungere 5+ m, quindi l'inoculo profondo ha senso — ma solo se le radici arrivano a quella profondità (anni dopo la piantumazione).

### 3.2 Decomposizione del legno a 2.5 m

| Fattore | Effetto sul tasso di decomposizione |
|---|---|
| Umidità | Bassa per 9-10 mesi/anno (suolo desertico) → tasso molto lento |
| Temperatura | Alta (25-35 °C a profondità) → accelera se umido |
| Ossigeno | Limitato in profondità → rallenta decomposizione aerobica |
| Azoto disponibile | Basso nel suolo desertico → limita attività dei decompositori |
| Composizione legno | Legno duro (mesquite, ironwood) si decompone più lentamente di pioppo/pino |

**Stima tasso di decomposizione** (legno di Prosopis o Olneya, interrato a 2 m):
- Anno 1-3: minima (<5% massa) — colonizzazione iniziale, umidità insufficiente
- Anno 3-10: 10-30% — esposizione a cicli di umidificazione (monsoni) innesca decomposizione
- Anno 10-20: 30-60% — perdita strutturale significativa, collasso possibile
- Anno 20+: 60-100% — residui di lignina recalcitrante

**Conseguenza**: la funzionalità dello strato di legno come serbatoio di porosità decade dopo 5-10 anni. Questo **non è un difetto fatale** — il biochar e i sassi mantengono porosità permanente. Il legno ha una funzione temporanea (primi 10 anni) di stoccaggio idrico e substrato per funghi. Dopo la decomposizione, lo spazio viene gradualmente occupato da radici (se l'albero sopravvive e si espande).

### 3.3 Biochar: stabilità, ritenzione idrica, pH

**Stabilità**: il biochar è aromatico policiclico condensato — stabile per migliaia di anni in suolo. Tasso di mineralizzazione <0.1%/anno. Non ci sono rischi di degrado precoce.

**Ritenzione idrica**: biochar poroso (pori 1-100 µm) può trattenere 3-5× il suo peso in acqua. Nel suolo desertico, questa è la proprietà più preziosa. Il biochar agisce come una *spugna microscopica* che rilascia acqua lentamente alle radici. Efficienza di ritenzione idrica: +15-30% di acqua disponibile per le piante nei primi 30 cm di suolo biochar-amendato (stima da letteratura su suoli aridi — Jeffery et al., 2011; Bruun et al., 2014).

**Effetto sul pH**: il biochar è tipicamente alcalino (pH 8-10 da feedstock legnoso, pirolisi 400-600 °C). In un suolo già alcalino (pH 7.8-8.4), l'aggiunta di biochar può:
- Innalzare ulteriormente il pH (negativo — riduce disponibilità di Fe, Zn, P, Mn)
- Oppure tamponare il pH se la cenere viene lavata pre-incorporazione

**Raccomandazione**: usare biochar a bassa temperatura (350-400 °C, pH < 8) e **lavarlo/condizionarlo** con acqua prima dell'incorporazione per rimuovere la frazione di ceneri alcaline. Alternativa: biochar da gusci di noce (pH più neutro). Testare il pH del biochar prima dell'uso.

### 3.4 Decomposizione anaerobica: metano e fitotossine

Condizioni per anaerobiosi: saturazione del suolo >72 h, temperatura >20 °C, substrato organico disponibile. Nella trincea Triceee:

- **Probabilità**: bassa (<10% degli eventi), ma possibile dopo un monsone estremo (50+ mm in 2-4 h) se il drenaggio basale è insufficiente.
- **Durata**: 1-7 giorni di saturazione, poi l'acqua drena o evapora.
- **Prodotti potenziali** in ordine di probabilità:
  1. **Acidi organici** (acetico, butirrico, lattico) — fitotossici a concentrazioni >1 mM. Si accumulano nelle prime 48 h di anaerobiosi. Un lavaggio (pioggia successiva) li diluisce.
  2. **Metano (CH₄)** — prodotto da metanogeni in condizioni strettamente anaerobiche (potenziale redox < -200 mV). Il volume è trascurabile su scala del singolo tratto di trincea, ma cumulativamente su 250 acri potrebbe essere rilevante per GHG accounting.
  3. **Etanolo** — prodotto da fermentazione alcolica. Meno tossico degli acidi organici, facilmente metabolizzabile dopo il ritorno dell'ossigeno.
  4. **H₂S** — solo se solfati presenti. Nel Typic Calciargid i solfati sono bassi (suolo calcareo, non gessoso). Rischio molto basso.

**Mitigazione**:
- Garantire drenaggio basale (strato di sassi spesso, ≥30 cm)
- Non usare legno fresco che consuma O₂ durante la decomposizione iniziale
- Mantenere la copertura superficiale traspirante (non sigillare ermeticamente)
- In caso di eventi estremi, monitorare odori (H₂S = uova marce) per rilevare anaerobiosi

---

## 4. Confronto costi-benefici qualitativi

### 4.1 Vantaggi rispetto a swales semplici

1. **Bypass del caliche**: l'acqua raggiunge orizzonti profondi che gli swales (0.4 m) non toccano. Questo è il vantaggio più solido.
2. **Volume di stoccaggio 5-6× superiore**: più resilienza in caso di siccità pluriennale.
3. **Protezione dall'evaporazione**: l'acqua infiltrata a 1-2.5 m è al di sotto del fronte di evaporazione capillare (~0.6 m nel Typic Calciargid).
4. **Creazione di microhabitat profondo**: il legno interrato e il biochar creano nicchie per microbi e radici a profondità >1 m, raddoppiando il volume esplorabile dalle radici.
5. **Miglioramento duraturo del suolo**: il biochar permane per millenni; anche dopo la decomposizione del legno, la struttura porosa (sassi + biochar) rimane.

### 4.2 Svantaggi e rischi

1. **Costo di scavo 6-8× superiore**: volume/tempo macchina molto maggiori; necessità di escavatore ≥12 t con ripper per il caliche.
2. **Rischio geotecnico**: trincee di 2.5 m richiedono procedure di sicurezza (OSHA Subpart P — pareti inclinate o blindate per profondità >1.5 m).
3. **Mobilizzazione salina**: possibile accumulo di sali in superficie se il drenaggio non è perfetto.
4. **Evaporazione dai camini**: controproducente nel design attuale; richiede modifica.
5. **Decomposizione legno**: perdita di porosità dopo 5-10 anni; possibili fenomeni anaerobici transitori.
6. **Bilancio degli GHG**: se il legno si decompone anaerobicamente in modo ricorrente, il CH₄ prodotto potrebbe compensare parte del carbonio sequestrato.
7. **Costo di prova/errore**: il sistema non ha letteratura scientifica di supporto (è una proposta nuova). L'incertezza tecnica è alta.

### 4.3 Condizioni in cui il sistema ha senso

| Fattore | Condizione favorevole | Condizione sfavorevole |
|---|---|---|
| **Caliche** | Continuo, spesso (>30 cm), cementato | Assente o sottile |
| **Pendenza** | 2-8% (runoff apprezzabile ma non erosivo) | Piatta (<1%) o ripida (>15%) |
| **Clima** | Precipitazione 200-350 mm/anno con eventi convettivi | <150 mm/anno (troppo secco per riempire) |
| **Suolo** | Bassa sostanza organica, compattato | Già poroso, ben strutturato |
| **Specie target** | Alberi a radice profonda (Prosopis, Olneya, Parkinsonia) | Arbusti/erbacee a radice superficiale |
| **Budget** | Budget medio-alto (fase pilota limitata) | Budget minimo (meglio swales classici) |

**Il sistema è più adatto per le aree del sito con caliche spesso e continuo, pendenza moderata, e dove si prevede di piantare le specie a radice profonda (Prosopis, Olneya)**. Non per l'intero sito — solo per i nuclei di piantumazione (30-40% della superficie totale stimata).

### 4.4 Giudizio complessivo

**Fattibile, ma non per l'intero progetto.** Il sistema Triceee ha una solida base idrologica (bypass del caliche, stoccaggio profondo) ma presenta rischi gestibili e costi elevati.

**Potenziale: PROMETTENTE.**
**Scala attuale: SCONSIGLIATA per 250 acri.** Limitare a fase pilota su 1-2 acri, con monitoraggio intensivo per 3-5 anni prima di estendere.

---

## 5. Raccomandazione

### 5.1 Modifiche al design

1. **Eliminare i camini di aerazione** — o convertirli in semplici colonne drenanti (sassi, coperte da 15-20 cm di terra con flap di sfiato). In alternativa, usare tubi con valvola unidirezionale che si apra solo durante infiltrazione (troppo complesso per la scala).

2. **Ridurre lo spessore del legno** — da 0.6-0.8 m a 0.3-0.4 m (sufficiente per la funzione di sponging iniziale; il resto del volume va a biochar, più stabile).

3. **Aumentare la proporzione biochar:organico** — 70:30 invece di 50:50. Il composto organico si decompone in 1-3 anni, il biochar dura millenni.

4. **Geotessuto separatore** — tra lo strato di legno e quello di biochar/organico per prevenire occlusione da collasso della terra superiore. Usare fibra di cocco (biodegradabile, 3-5 anni di vita — sufficiente per la fase critica di establishment radicale).

5. **Copertura finale** — aumentare lo strato di sassi superficiali a 15-20 cm (invece di 10 cm) per massimizzare la riduzione dell'evaporazione.

6. **Profondità ridotta fuori dai nuclei** — dove non si piantano alberi a radice profonda, usare una versione light: profondità 1.2-1.5 m (sotto il caliche, ma non in zona vadosa profonda), senza strato di legno, solo biochar + sassi.

### 5.2 Protocollo pilota

| Fase | Durata | Azioni |
|---|---|---|
| **Pilot site selection** | 1 mese | Identificare 2-3 aree di 0.5-1 acro con caliche spesso, pendenza 3-6%, esposizione N/NE (minore insolazione) |
| **Scavo e costruzione** | 1-2 settimane | 3 trincee con design modificato (con e senza geotessuto, con e senza legno vs solo biochar) + 2 swales tradizionali come controllo |
| **Strumentazione** | Durante scavo | Installare sensori di umidità del suolo a 0.5, 1.0, 1.5, 2.0, 2.5 m; piezometri (tubi forati) per misurare livello idrico; portacampioni per gas (CH₄, CO₂, O₂) a 1.0 e 2.0 m |
| **Monitoraggio Anno 1** | 12 mesi | Registrazione ogni 30 min di umidità, temperatura, potenziale redox; campionamento gas dopo ogni evento >10 mm; misurazione salinità (EC) trimestrale a 5 profondità |
| **Piantumazione** | Anno 1 (post-monsone) | 10 alberi (5 Prosopis, 5 Olneya) su ogni trincea; 5 alberi su ogni swale controllo. Inoculo micorrizico selettivo su metà degli alberi (Pisolithus tinctorius) |
| **Valutazione Anno 3** | 3 anni dal pilota | Sopravvivenza, crescita, profondità radicale (minirhizotron), bilancio idrico integrato (pioggia vs umidità residua), dinamica salina, produzione CH₄ |
| **Decisione scala** | Anno 3 | Se sopravvivenza ≥70% e crescita ≥1.5× controllo → estensione graduale (5-10 acri/anno). Se <50% → archiviare il design e tornare a swales classici |

### 5.3 Integrazione nel progetto complessivo

Propongo una **strategia mista**:

| Area (sul totale 250 acri) | Tecnica primaria | Note |
|---|---|---|
| ~60% (150 acri) | Swales tradizionali 0.4 m + keyline | Aree con caliche sottile o frammentato, pendenza <3% |
| ~20% (50 acri) | Trincee Triceee modificate (1.5 m light) | Aree con caliche medio, dove si prevedono arbusti/erbacee |
| ~10% (25 acri) | Trincee Triceee full (2.5 m) | **Solo nei nuclei di piantumazione** con alberi a radice profonda, caliche spesso, pendenza 3-6% |
| ~10% (25 acri) | Nessuna trincea — solo Zai pits + rock dams | Aree ripide (>8%) o con suolo scheletrico |

Questa suddivisione:
- Contiene i costi (solo 10-30% dell'area con trincee profonde)
- Concentra l'investimento dove dà il massimo ritorno ecologico (nuclei arborei)
- Mantiene un controllo sperimentale (gli swales tradizionali)
- Permette di scalare gradualmente se il pilota ha successo

---

## Riferimenti

- USDA-NRCS. Official Soil Series Description — TUCSON series. https://soilseries.sc.egov.usda.gov/
- USDA-NRCS. *Soil Survey of Pima County, Arizona*. 2020.
- Jeffery, S., et al. (2011). "A quantitative review of the effects of biochar application to soils on crop productivity using meta-analysis." *Agriculture, Ecosystems & Environment*, 144(1), 175-187.
- Bruun, E.W., et al. (2014). "Biochar amendment to coarse sandy subsoil improves root growth and increases water retention." *Soil Use and Management*, 30(1), 109-118.
- Bates, T.R., et al. (2018). "Fungal community structure in the Sonoran Desert: the role of spatial and environmental gradients." *Fungal Ecology*, 35, 68-78.
- Rillig, M.C., & Mummey, D.L. (2006). "Mycorrhizas and soil structure." *New Phytologist*, 171(1), 41-53.
- Breshears, D.D., et al. (2005). "Regional vegetation die-off in response to global-change-type drought." *PNAS*, 102(42), 15144-15148.
- Ahuja, L.R., et al. (1999). "Pathways of water movement in arid and semi-arid soils." In *Arid Lands Water Evaluation and Management*. Springer.

---

*Documento tecnico. Autore: Demetra — Specialista Ecosistemi Aridi e Pianificazione Ambientale. Team Olimpo.*
*Stato: bozza per revisione interna.*
