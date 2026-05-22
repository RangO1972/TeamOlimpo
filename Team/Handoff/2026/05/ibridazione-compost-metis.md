---
autore: Metis
destinatario: Hermes (per forwarding a team)
data: 2026-05-10
stato: completato
tags: [ibridazione, compost, asp, tucson]
tipo: analisi-tecnica
dominio: compostaggio-arido
basato_su:
  - "Library/Handoff/2026-05-10_proteo-hermes_ricerca-progetti-compost-proteo.md"
  - "projects/tucson/specifiche/compost.md"
  - "projects/tucson/specifiche/biochar.md"
  - "projects/tucson/specifiche/triceee.md"
---

# Ibridazione Sistema ASP Desertico — Progetto Tucson

> **Obiettivo**: Ibridare componenti da Phoenix TAP (swamp cooler), Quivira ASP (piping diagram) e biochar co-composting Tucson per un sistema ASP scalabile, desertico, orientato alla produzione di compost AMF-grade. Calcolo volumi per 10 trincee/settimana con 45 giorni di maturazione e 2 ASP simultanei.

---

## 1. Ibridazione Sistema

### 1.1 Matrice dei Componenti Ibridati

| # | Componente | Fonte Progetto | Funzione nel Sistema Tucson | Adattamento Necessario |
|---|-----------|---------------|-----------------------------|----------------------|
| 1 | **Swamp cooler su blower** | Phoenix TAP (GMT design, BioCycle Mar 2019) | Precondizionamento aria: saturare l'aria in ingresso con nebulizzazione per abbassare T di 18-30°F e prevenire disidratazione pile | Ridimensionare da 33,000 cfm a 0.5-1 HP (fattore ~1:50). Misting ring artigianale con venturi o pompa 12V |
| 2 | **Aeration reversing** | Phoenix TAP | Ciclo positivo/negativo per condensare umidità dall'exhaust e recuperarla | Timer programmabile ART-DNe già in lista materiali Quivira; aggiungere logica reversing |
| 3 | **Piping manifold 4"-6"** | Quivira ASP (Issuu pag 39-42) | Distribuzione aria sotto la pila con PVC perforato, tee, elbow, dry fittings | Stesso design ma scalato: 7 pile per ASP invece di 2. Manifold con valvole di zona |
| 4 | **Plenum layer 6"** | Quivira ASP | Strato basale di mesquite chips/wood mulch per aerazione uniforme senza rivoltamento | Feedstock locale (mesquite chips clearance) sostituisce wood chips standard |
| 5 | **Timer + ciclo** | Quivira ASP (15-30 sec ogni 30 min) | Minima perdita d'acqua, massima efficienza aerazione | Stesso ciclo; aggiungere override manuale per giorni >105°F |
| 6 | **Copertura pile** | Quivira (mulch) + Phoenix (biocover) + specifica Tucson (geotessile) | Geotessile traspirante + shade 70% in estate. Riduce evaporazione 50-70% | Geotessile come layer primario, shade stagionale sopra |
| 7 | **Co-composting biochar 5-10%** | Tucson (specifica biochar.md, IBI protocol) | Accelerazione maturazione (-20-30%), riduzione CH₄ (-60-70%), caricamento nutrienti biochar | Aggiungere biochar in fase mesofila (giorno 0-3), non in fase termofila |
| 8 | **Kon-Tiki biochar production** | Tucson (specifica biochar.md) | Produzione in loco da mesquite clearance, $100-160/m³ vs $300-500 acquisto | Integrazione logistica: programmare batch Kon-Tiki 1-2 settimane prima del mixing ASP |
| 9 | **Feedstock a basso P** | Tucson (specifica compost.md) | Gusci pecan (P 0.14%) + mesquite chips (P 0.05-0.15%) come diluenti strutturali per compost AMF-grade | Nessuno — feedstock già disponibili in Southern Arizona |
| 10 | **Aeration floor** | Phoenix TAP (concrete slab with nozzles) | Base per pile multiple con manifold interrato | Versione economica: ghiaia compattata + piping aereo (modello Quivira). Concrete slab in fase 2 |

### 1.2 Diagramma di Flusso del Sistema Ibridato

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SISTEMA ASP IBRIDATO — TUCSON                     │
│          (Phoenix TAP × Quivira ASP × Tucson Biochar)               │
└─────────────────────────────────────────────────────────────────────┘

 FEEDSTOCK IN
 ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
 │ Yard waste   │    │ Gusci pecan  │    │ Mesquite     │
 │ (50% vol.)   │    │ (15% vol.)   │    │ chips (25%)  │
 └──────┬───────┘    └──────┬───────┘    └──────┬───────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    ┌──────▼──────┐    ┌──────────────────┐
                    │   MIXER /   │◄───│ Biochar 5-10%    │
                    │  BATCH SET  │    │ (da Kon-Tiki)    │
                    └──────┬──────┘    │ + Manure 10%     │
                           │           └──────────────────┘
                           │
                    ┌──────▼─────────────────────────────────┐
                    │       ASP SYSTEM (×2 paralleli)        │
                    │                                         │
                    │  ┌─── Swamp Cooler ──────────────────┐  │
                    │  │  (nebulizzatore su intake blower) │  │  ← da Phoenix TAP
                    │  └───────────────────────────────────┘  │
                    │                                         │
                    │  ┌─── Piping Manifold 4"-6" ─────────┐  │
                    │  │  (PVC perforato, valvole di zona)  │  │  ← da Quivira ASP
                    │  └───────────────────────────────────┘  │
                    │                                         │
                    │  ┌─── 7 Pile Staggered ──────────────┐  │
                    │  │  (una pila ogni 6.4 giorni)        │  │
                    │  │  Plenum: mesquite chips 6"         │  │
                    │  │  Cover: geotessile + shade 70%     │  │
                    │  └───────────────────────────────────┘  │
                    └─────────────────────────────────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  CURING 2-4  │
                    │  settimane   │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │  CRIBLATURA  │
                    │   (3/4")     │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
     ┌────────────┐ ┌───────────┐ ┌──────────┐
     │ Trincee    │ │ Grow bag  │ │ Zai pits │
     │ Triceee    │ │ AMF 1:4   │ │ & swales │
     │ (70:30     │ │ (metodo   │ │          │
     │ biochar:   │ │ Douds)    │ │          │
     │ compost)   │ │           │ │          │
     └────────────┘ └───────────┘ └──────────┘
```

### 1.3 Logica delle Scelte di Ibridazione

| Scelta | Perché questa fonte | Rischio di incompatibilità |
|--------|---------------------|---------------------------|
| **Swamp cooler da Phoenix, non da altri progetti** | Phoenix è l'unico progetto documentato in clima Sonoran identico (stesso deserto, stesse T estive >110°F). Benchmarked da BioCycle e GMT. | Basso — il principio è indipendente dalla scala. Un misting ring su blower 0.5-1 HP è più semplice del sistema Phoenix 33,000 cfm. |
| **Piping da Quivira, non da Phoenix** | Quivira è scala appropriata (DIY, $542). Phoenix usa concrete slab + HDPE interrato — costo e complessità non giustificati per scala Tucson. | Basso — Quivira usa dry fittings che permettono disassemblaggio e riposizionamento. Per 7 pile per ASP, aggiungere manifold con valvole di zona. |
| **Biochar co-composting da Tucson (unico)** | Nessun progetto esistente integra biochar in ASP. Benefici documentati: -20-30% tempo, -60-70% CH₄, -35-40% NH₃. | Medio — il biochar adsorbe NH₄⁺ e PO₄³⁻, riducendo N disponibile. Compensare con N extra nel feedstock o ridurre dosaggio a 5%. |
| **Feedstock gusci pecan (unico)** | Nessun progetto comparabile usa pecan shells. P 0.14%, EC bassissima — ideale per target AMF-grade. | Basso — C:N molto alto (200+:1). Bilanciare con manure (10%) e yard waste (50%). |

---

## 2. Calcolo Volumi ASP

### 2.1 Assunzioni di Base

| Parametro | Valore | Fonte / Note |
|-----------|--------|--------------|
| **Trenches per week** | 10 | Dato utente |
| **Compost per trench** | 5 m³ | Dato utente (include frazione compost nello strato attivo Triceee) |
| **Maturation time** | 45 days | Accelerato da biochar co-composting (standard 60 gg → -25%) |
| **ASP systems** | 2 | Costruiti simultaneamente, operazione parallela |
| **Volume reduction (feedstock → compost)** | 40% | Tipico per ASP con materiale lignocellulosico. Range: 35-50% |
| **Biochar dosage** | 7.5% v/v | Midpoint del range IBI (5-10%). Aggiunto in fase mesofila |
| **Density feedstock (bulk)** | ~400 kg/m³ | Media ponderata: yard waste ~300, manure ~600, chips ~250 |
| **Density compost finito** | ~550 kg/m³ | Compost maturo con struttura aggregata |
| **Pile height (ASP)** | 2.5 m | Plenum 15 cm + feedstock 2.0 m + geotessile + copertura |
| **Pile base width** | 4.0 m | Sezione trapezoidale stabile per ASP senza rivoltamento |
| **Timer cycle** | 30 sec on / 30 min off | Modello Quivira. 1 min on in estate >105°F |
| **Swamp cooler water flow** | 0.15-0.25 gpm | Scalato da Phoenix (7.5-8 gpm su 33,000 cfm → ~0.2 gpm su 500 cfm) |

### 2.2 Formule e Calcoli

#### 2.2.1 Flusso Settimanale

```
Compost output settimanale (Cₒ):
  Cₒ = 10 trincee × 5 m³/trincea = 50 m³/settimana

Feedstock input settimanale (Fᵢ):
  Fᵢ = Cₒ / (1 - 0.40) = 50 / 0.60 = 83.3 m³/settimana
```

#### 2.2.2 Pipeline Volume (In-Process Inventory)

```
Maturation in settimane: 45 / 7 = 6.43 settimane

Pipeline volume totale (Vₚ):
  Vₚ = Fᵢ × 6.43 = 83.3 × 6.43 = 535.6 m³ feedstock in process

Pipeline compost equivalente:
  Vₚ_compost = 50 × 6.43 = 321.5 m³ compost equivalente
```

**Interpretazione**: In ogni momento ci sono ~536 m³ di materiale in fase attiva di compostaggio nei 2 ASP combinati. Questo equivale a ~322 m³ di compost finito una volta completato il ciclo.

#### 2.2.3 Per-ASP Sizing (2 Sistemi Paralleli)

```
Feedstock per ASP a settimana:
  Fᵢ_ASP = 83.3 / 2 = 41.7 m³/settimana

Pipeline per ASP:
  Vₚ_ASP = 535.6 / 2 = 267.8 m³ feedstock
```

#### 2.2.4 Pile Sizing e Scheduling

Con 45 giorni di ciclo e carico settimanale, ogni ASP ospita **7 pile** in fasi staggerate (settimane 1-7). Alla settimana 8, la pila della settimana 1 viene raccolta.

```
Volume per pila (Vₚile):
  Vₚile = 41.7 m³ feedstock (una settimana di produzione per ASP)

Dimensioni pila (sezione trapezoidale):
  Larghezza base (W_b): 4.0 m
  Larghezza top (W_t): 2.5 m
  Altezza (H):        2.5 m
  Area sezione (A):   ((4.0 + 2.5) / 2) × 2.5 = 8.125 m²

Lunghezza pila per batch settimanale (L):
  L = Vₚile / A = 41.7 / 8.125 = 5.1 m
```

**Risultato**: Ogni ASP ha 7 pile da ~41.7 m³ ciascuna, dimensioni 4.0 m (base) × 2.5 m (H) × 5.1 m (L). Le pile sono affiancate con spacing di 1 m per accesso.

#### 2.2.5 Area Richiesta

```
Per ASP (7 pile):
  Area pile: 7 × (4.0 m × 5.1 m) = 142.8 m²
  Area accesso/spacing (1m tra pile): 6 × (4.0 × 1.0) = 24.0 m²
  Area manifold + blower: 3.0 × 4.0 = 12.0 m²
  Area circolazione perimetrale: 1.5 m × (8.0 + 15.0) × 2 = ~70 m²
  Subtotale per ASP: ~249 m²

Feedstock storage (coperto, 2 settimane buffer):
  2 × 83.3 = 166.6 m³ → area ~80 m² (a 2.5 m altezza cumulo)

Biochar production & storage:
  Area Kon-Tiki (2 kiln): 10 × 10 m = 100 m²
  Area stoccaggio biochar: ~40 m²

Curing area (2-4 settimane post-ASP):
  ~160 m³ compost in curing → area ~65 m² a 2.5 m

Totale area ASP (2 sistemi + servizi):
  ~790 m² (~0.2 acri)
```

#### 2.2.6 Feedstock Breakdown Settimanale

Basato sulla ricetta AMF-grade dal specifica compost.md (yard waste 50%, pecan 15%, mesquite 25%, manure 10% + biochar 7.5%).

| Feedstock | % Volume | Volume/sett (m³) | Volume/ASP/sett (m³) | Note approvvigionamento |
|-----------|----------|------------------|---------------------|------------------------|
| Yard waste trinciato | 50% | 41.7 | 20.8 | Compost Cats / Los Reales — continuativo |
| Gusci pecan triturati | 15% | 12.5 | 6.3 | Green Valley Pecan (20 mi) — stagionale autunno-inverno; stockpile per anno |
| Mesquite chips | 25% | 20.8 | 10.4 | Clearance sito + municipale — continuativo |
| Horse manure | 10% | 8.3 | 4.2 | Scuderie Tucson area — continuativo |
| **Subtotale feedstock** | **100%** | **83.3** | **41.7** | |
| Biochar (co-composting) | 7.5% add-on | 6.25 | 3.1 | Da Kon-Tiki in loco |

#### 2.2.7 Biochar Production Schedule

```
Biochar necessario: 6.25 m³/settimana
Kon-Tiki output: 1-2 m³/batch, 1-2 batch/giorno

Scenario 1 Kon-Tiki:
  Produzione: 1-4 m³/giorno
  Giorni necessari: 6.25 / 1.5 (media) = ~4.2 giorni/settimana
  → 1 Kon-Tiki basta con margine

Scenario 2 Kon-Tiki in parallelo (raccomandato):
  Produzione: 2-8 m³/giorno
  Giorni necessari: 6.25 / 3 (media combinata) = ~2 giorni/settimana
  → Batch di 2 giorni ogni settimana, flessibilità programmazione
```

**Nota**: Il biochar per il co-composting va prodotto **1-2 settimane prima** del batch ASP, per permettere condizionamento (lavaggio/ammollo 24-48h) e stagionatura breve.

#### 2.2.8 Stima Consumo Idrico

```
Fabbisogno irriguo pile (target 55% umidità):
  Acqua da aggiungere al mixing: ~18,500 L/settimana (18.5 m³)
  ≈ 2,640 L/giorno

Swamp cooler (solo in estate >95°F, ~90 giorni/anno):
  0.2 gpm × 60 min × 24 ore × 90 giorni × 3.785 L/gal = ~980 L/anno per ASP
  (Trascurabile rispetto all'acqua di mixing)

Acqua totale annua stimata:
  18.5 m³/sett × 52 sett = 962 m³/anno ≈ 254,000 gal/anno
```

#### 2.2.9 Tabella Riepilogativa Volumi

| Voce | Valore | Unità |
|------|--------|-------|
| **Output compost/settimana** | 50.0 | m³ |
| **Input feedstock/settimana** | 83.3 | m³ |
| **Pipeline totale (entrambi ASP)** | 535.6 | m³ feedstock |
| **Pipeline per ASP** | 267.8 | m³ feedstock |
| **Pile per ASP** | 7 | n° |
| **Volume per pila** | 41.7 | m³ feedstock |
| **Dimensioni pila (L×W×H)** | 5.1 × 4.0 × 2.5 | m |
| **Biochar/settimana** | 6.25 | m³ |
| **Kon-Tiki giorni/settimana** | 2-4 | giorni |
| **Area totale sistema** | ~790 | m² (~0.2 acri) |
| **Acqua/settimana (mixing)** | 18.5 | m³ |

---

## 3. Raccomandazioni

### 3.1 Setup Consigliato

#### Fase 1 — Pilota Ibridato (Mes 0-3)
Validare l'ibridazione prima di scalare.

| Elemento | Specifica | Costo stimato |
|----------|-----------|--------------|
| 1 ASP system (Quivira piping + swamp cooler) | 2 pile, PVC 4" manifold, blower 1 HP, timer ART-DNe | $800-1,200 |
| Swamp cooler artigianale | Misting ring 4-6 nozzle su intake blower, pompa 12V | $100-250 |
| Geotessile + shade 70% | Copertura 2 pile (5×5 m cad.) | $200-400 |
| Batch di prova (20 m³ feedstock) | Yard waste 10 m³ + pecan 3 m³ + mesquite 5 m³ + manure 2 m³ | $200-400 (materiali) |
| Biochar batch (Kon-Tiki 1 m³) | Mesquite clearance, 1 batch | $100-150 (manodopera) |
| **Totale Fase 1** | | **~$1,400-2,400** |

Validazione: dopo 45 giorni, testare P, EC, C:N, Solvita. Target: P < 0.5%, EC < 5 dS/m.

#### Fase 2 — Ibridazione Completa (Mes 3-6)
Costruzione 2° ASP, scala 10 trincee/settimana.

| Elemento | Specifica | Costo stimato |
|----------|-----------|--------------|
| 2° ASP system (stesso design Fase 1) | 7 pile manifold, piping 4"-6", valvole zona | $2,500-3,500 |
| 2° blower + swamp cooler | 1 HP, timer, misting ring | $500-800 |
| 7 coperture geotessile | 6×8 m cad., con shade sovrapposto | $800-1,500 |
| Feedstock storage coperto | Struttura leggera (pali + lamiera) 80 m² | $2,000-4,000 |
| 2° Kon-Tiki kiln | Per produrre 6.25 m³/sett con 2 gg lavoro | $1,500-2,500 |
| **Totale Fase 2** | | **~$7,300-12,300** |

#### Layout Spaziale Consigliato

```
┌──────────────────────────────────────────────────────────────┐
│                    LAYOUT SISTEMA ASP × 2                     │
│                                                              │
│  ┌──────────┐  ┌──────────────────────┐  ┌──────────┐       │
│  │ Kon-Tiki │  │      ASP 1           │  │ Curing   │       │
│  │ Kiln 1   │  │  P1 P2 P3 P4 P5 P6 P7│  │ Area     │       │
│  ├──────────┤  │  ───blower/manifold── │  │ (160 m³) │       │
│  │ Kon-Tiki │  └──────────────────────┘  └──────────┘       │
│  │ Kiln 2   │  ┌──────────────────────┐  ┌──────────┐       │
│  └──────────┘  │      ASP 2           │  │Finished  │       │
│  [Biochar      │  P1 P2 P3 P4 P5 P6 P7│  │Compost   │       │
│   Storage]     │  ───blower/manifold── │  │Storage   │       │
│                └──────────────────────┘  └──────────┘       │
│                                                              │
│  ┌──────────────────────────────────────────────────┐       │
│  │         Feedstock Storage (coperto)              │       │
│  │  Yard Waste | Pecan Shells | Mesquite | Manure   │       │
│  └──────────────────────────────────────────────────┘       │
│                                                              │
│  ← 30 m →                                                   │
└──────────────────────────────────────────────────────────────┘
```

### 3.2 Costi Stimati — Scenario Completo (2 ASP)

#### Capex (Una Tantum)

| Voce | Costo (USD) | Note |
|------|-------------|------|
| Piping + manifold (×2) | $1,600-2,400 | PVC 4"-6", valvole, dry fittings |
| Blower 1 HP (×2) | $600-1,000 | B-Air Koala o equivalente |
| Timer ART-DNe (×2) | $200-400 | Cicli 30 sec/30 min, reversing option |
| Swamp cooler system (×2) | $400-800 | Misting ring, pompa, tubing |
| Geotessile copertura (14 pile) | $1,200-2,000 | Tagliato su misura, 6×8 m cad. |
| Shade cloth 70% (14 pile) | $800-1,600 | Stagionale (maggio-ottobre) |
| Feedstock storage (coperto) | $2,000-4,000 | Pali legno + lamiera ondulata |
| Cippatrice (usata) | $15,000-40,000 | Opzionale, Vermeer BC o equivalente |
| Vagliatore trommel (usato) | $25,000-50,000 | Opzionale, Kooima o equivalente |
| Kon-Tiki kiln (×2) | $3,000-6,000 | Autocostruzione o Finger Lakes |
| Piazzale ghiaia + drenaggio | $5,000-15,000 | 800 m², ghiaia 10 cm su geotessile |
| Struttura ombreggiante perm. | $5,000-15,000 | Opzionale, per area curing |
| **Capex Totale** | **~$60,000-138,000** | |
| **Capex "essenziale" (senza cippatrice/vagliatore)** | **~$15,000-33,000** | Noleggio cippatrice, vagliatura manuale |

#### Opex (Annui)

| Voce | Costo (USD/anno) | Note |
|------|------------------|------|
| Manodopera (0.5 FTE) | $15,000-25,000 | Mixing, carico pile, monitoraggio, raccolta |
| Elettricità blower | $300-600 | 2 blower × 1 HP × 8760 × 0.016 ore/h |
| Acqua | $1,500-3,000 | ~962 m³/anno a $1.5-3/m³ (Tucson Water) |
| Manutenzione attrezzatura | $1,000-2,000 | Kon-Tiki, pompe, blower, piping |
| Test laboratorio qualità | $1,000-2,000 | P, EC, C:N, Solvita — ogni batch |
| Carburante movimentazione | $1,500-3,000 | Trattore/carrello per feedstock |
| **Opex Totale** | **~$20,300-35,600/anno** | |
| **Costo per m³ compost** | **~$8-12/m³** | 50 m³/sett × 52 sett = 2,600 m³/anno |

**Confronto**: Compost acquistato in Arizona: $25-50/m³ (qualità standard), $40-80/m³ (AMF-grade certificato). Risparmio: **$17-68/m³** = **$44,000-177,000/anno** a regime.

### 3.3 Rischi dell'Ibridazione

| Rischio | Probabilità | Impatto | Mitigazione |
|---------|-------------|---------|-------------|
| **Swamp cooler non scaled correttamente** | Media | Medio | Testare rapporto cfm/gpm nel pilota (Fase 1). Regolare nozzle count e pressione |
| **Biochar adsorbe N, rallentando compost** | Media | Medio | Dosaggio 5% (non 7.5-10%) nel primo batch; testare N finale; aggiungere extra manure se necessario |
| **Piping Quivira non sufficiente per 7 pile** | Bassa | Medio | Calcolare caduta di pressione su manifold esteso. Potrebbe servire blower 1.5-2 HP invece di 1 HP |
| **Gusci pecan stock insufficienti** | Alta | Medio | Stockpile autunnale per copertura annuale; sostituire con mesquite chips extra se necessario |
| **Evaporazione eccessiva in estate** | Alta | Medio | Swamp cooler + shade + copertura = tripla mitigazione. Se insuff., ridurre ciclo timer a 15 sec/20 min |

### 3.4 Prossimi Passi Immediati

- [ ] **Fase 1 — Pilota** (Mes 0-3): Costruire 1 ASP ibridato (Quivira piping + swamp cooler artigianale). Produrre 41.7 m³ batch. Validare qualità compost (P, EC, C:N). Testare dosaggio biochar 5% vs 7.5%.
- [ ] **Feedstock supply chain**: Contattare Compost Cats, Green Valley Pecan, scuderie Tucson. Verificare quantità e costi effettivi. Stockpile gusci pecan in autunno.
- [ ] **Biochar production**: Costruire Kon-Tiki (autocostruzione). Produrre ~7 m³ biochar per pilota. Testare qualità (pH < 8.0, carbonio fisso > 70%).
- [ ] **Permessi**: Verificare necessità permessi Pima County DEQ per compostaggio su scala 50 m³/settimana.
- [ ] **Design definitivo**: Validare layout spaziale (790 m²) nel sito Tucson. Verificare accesso acqua, ombreggiamento naturale, distanza da residence (buffer odori).

---

*Analisi di ibridazione e dimensionamento v1 — Metis, Team Olimpo. Basata su ricerca Proteo e specifiche progetto Tucson. Date: 2026-05-10.*
