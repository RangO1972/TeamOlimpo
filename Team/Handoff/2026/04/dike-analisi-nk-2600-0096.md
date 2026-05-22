---
kba: NK-2600-0096
analista: dike
data: 2026-04-02
risk_level: Advisory
risk_score: 6.0
siti: [Termoli, Montecchio, Lonigo]
---

# Analisi NK-2600-0096 — Dike

## Sintesi tecnica

Il blocco ECTLSL (Enhanced Control) quando contiene una discrepanza tra il numero di parametri estensibili e il valore di `NOF_USED_SEL`, se embedato in un composite, non viene validato correttamente dal software. Durante il download del modulo, questa configurazione invalida provoca un reset software-generato sul nodo, con conseguente perdita della ridondanza (standby controller non failover) e necessità di Total download.

**Punto critico**: La stessa configurazione errata in un blocco ECTLSL standalone viene catturata da validazione e rifiutata. In composite, la validazione è bypassata.

---

## Scoring dettagliato

### Severita' — 7/10

Il reset software durante download è un evento operativamente significativo: interrompe il controllo del processo e impedisce il failover automatico del controller. Tuttavia non causa corruzione dati, non è safety-related diretto, e il problema è rilevabile durante engineering phase (prima del deployment in produzione). Non è una situazione che mette il plant in pericolo istantaneo, ma è un "blocco di deployment" che va risolto.

### Probabilita' — 4/10

Il problema non si manifesta spontaneamente. Richiede una configurazione **specifica e errata**: discrepanza tra parametri extensibili e NOF_USED_SEL, **e** il blocco deve essere in composite, **e** l'utente deve downloadare il modulo. È un errore di configurazione, non un bug dello stack software. Non accade "sempre" — accade solo quando questa precisa condizione esiste.

### Rilevabilita' inversa — 4/10

Il manifestarsi è **visibile e immediato**: il reset appare durante il download, DeltaV Explorer mostra triangolo giallo sul nodo, l'evento è tracciato. Non è un problema silenzioso. Bassa difficoltà di rilevazione.

### Calcolo

```
Risk Score base = (7 × 0.5) + (4 × 0.3) + (4 × 0.2) = 5.5

Moltiplicatore: Numero versioni affette > 3 (sono 9) = +0.5

Risk Score finale = 6.0
```

---

## Prodotti coinvolti

| Aspetto | Dettaglio |
|---------|-----------|
| **Famiglia prodotto** | DeltaV Controller Software |
| **Modulo specifico** | VE3101-03 Logic Software — Function Blocks |
| **Versioni affette** | v14.FP1, v14.FP2, v14.FP3, v14.LTS, v15.FP1, v15.FP2, v15.FP3, v15.LTS, v16.LTS |
| **Scope** | 9 versioni attive di supporto Emerson |
| **Livello architetturale** | 1 (controller, software critico) |

---

## Workaround

**Disponibile**: SÌ

**Procedura**:
1. Aprire il blocco ECTLSL in Control Studio
2. Modificare il parametro `NOF_USED_SEL` affinché corrisponda al numero di parametri estensibili
3. Salvare il modulo
4. Downloadare il nodo normalmente

**Complessità**: Bassa (azione di configurazione singola)

**Efficacia**: Previene il reset — risolve il problema alla radice durante engineering.

---

## Fix/Patch

**Disponibile**: NO

Lo stato della KBA dichiara: "This issue is being investigated. This KBA will be updated when new information becomes available."

Nessuna patch anticipata, nessun workaround alternativo documentato.

---

## Raccomandazione operativa

**Azione**: Monitorare + Verificare configurazione nei 3 siti

1. Durante le prossime revisioni di moduli ECTLSL nei 3 siti (Termoli, Montecchio, Lonigo), verificare che nessun blocco ECTLSL in composite presenti discrepanza tra parametri estensibili e `NOF_USED_SEL`
2. Se la discrepanza è presente, applicare il workaround prima di qualunque download
3. Monitorare i release notes di Emerson per la disponibilità di una patch (attesa nel breve-medio termine)
4. Documentare il workaround nei processi di engineering dei 3 siti per prevenzione futura

---

## Note

- **Confidence**: High — Documento esplicito, ben strutturato, problema descritto con precisione tecnica
- **Divergenza da Emerson**: Non indicata classificazione Emerson (Alert/Advisory/Informational). Basandomi su severita', scope, e disponibilità workaround, assegno **Advisory** come classificazione coerente
- **Recenza**: Pubblicato 30 Mar 2026 — recentissimo, impianto non ancora ha tempo di incontrarlo diffusamente
