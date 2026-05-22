---
kba: [AP-0600-0029, NK-2600-0089]
data: 2026-04-01
analisi_originale: batch-grok
revisione: dike
siti: [Termoli, Montecchio]
---

# Sintesi KBA per discussione cliente

## AP-0600-0029 — Cavi extender danneggiati (parte 12P1795)

**Rischio**: Critico | **Siti**: Termoli

### Il problema
Alcuni cavi di collegamento interni agli armadi DeltaV (parte numero 12P1795), prodotti tra ottobre 2005 e gennaio 2006, sono stati costruiti con materiale non idoneo. Mancano la schermatura interna e non resistono alle temperature specificate. Nel tempo, questo può causare comunicazioni instabili tra le schede di I/O e perdita di integrità del cavo stesso.

### A quali componenti è associata
- Cavi extender locali (12P1795X032)
- Carrier per I/O 8-wide (VE4050)
- Sistemi con ridondanza di comunicazione o configurazione simplex

### Condizioni in cui si manifesta
- Durante il normale funzionamento, specialmente in ambienti con rumore elettromagnetico
- Progressivamente nel tempo, se i cavi trasportano corrente continua massima su linee simplex
- I cavi difettosi hanno marcature specifiche: inchiostro blu scuro con codice data D4005 a D0106

### Cosa si chiede al cliente
1. **Verificare immediatamente** se l'impianto Termoli contiene cavi con le marcature specificate (leggere l'etichetta del cavo)
2. **Pianificare la sostituzione** — per sistemi ridondanti, i cavi possono essere cambiati uno alla volta senza fermare la produzione; per sistemi simplex occorre uno shutdown programmato
3. **Contattare Emerson** per fornire i cavi di ricambio corretti (Commscope, con marcature rosa)
4. Se si osservano **rallentamenti nelle comunicazioni I/O o riavvii delle schede**, potrebbe essere un sintomo

---

## NK-2600-0089 — Switchover ridondanza durante aggiornamento sistema

**Rischio**: Advisory | **Siti**: Termoli, Montecchio

### Il problema
Durante l'aggiornamento software del sistema DeltaV (versioni v15 e v16), in rare circostanze il sistema di controllo principale (ProPlus) può ricevere molta comunicazione di rete non relativa a DeltaV (es. backup di altri sistemi, aggiornamenti Windows). Se questo accade durante l'aggiornamento, i controller ridondanti potrebbero fare uno switchover (passaggio al backup) per errore di comunicazione temporaneo. Il sistema si recupera automaticamente, ma per alcuni secondi/minuti i dispositivi di controllo potrebbero comportarsi in modo inaspettato.

### A quali componenti è associata
- Controller principali
- Moduli CIOC e EIOC (unità di ingresso/uscita intelligenti)
- Rete Ethernet del sistema DeltaV
- Software v15.FP1, v15.FP2, v15.FP3, v15.LTS, v16.LTS

### Condizioni in cui si manifesta
- Durante un download/aggiornamento ProPlus
- Se il ProPlus sta elaborando traffico di rete molto elevato e anomalo
- Non relato a DeltaV diretto (es. altre macchine scaricano dati sulla stessa rete, autenticazione fallita ripetuta)
- Scenario raro e specifico

### Cosa si chiede al cliente
1. **Prima di qualunque aggiornamento ProPlus**, verificare con il team IT che non ci siano grossi trasferimenti dati sulla rete DeltaV (backup, aggiornamenti di sistema)
2. **Controllare in Gestione Attività di Windows** il carico di rete del ProPlus — se è anomalamente alto, rinviare l'aggiornamento
3. **Disabilitare SMB Multichannel** su tutte le workstation (dettagli in KBA NK-1900-0360)
4. Se accade uno switchover, il sistema si recupera automaticamente — non richiede intervento, ma sarà registrato nel log eventi DeltaV

---

## Nota — Relazione tra AP-0600-0029 e NK-2600-0089

**Scenario combinato rilevante per Termoli e Montecchio:**

Se un impianto ha cavi defettosi (AP-0600-0029) E durante uno aggiornamento sistema la rete è congestionata (NK-2600-0089), i sintomi potrebbero confondersi: il rumore I/O dai cavi cattivi potrebbe essere interpretato come una perdita di comunicazione dal sistema, scatenando switchover ridondanti anche se la causa è fisica (il cavo), non di rete. 

**Azione integrata consigliata:**
- Affrontare prima il problema dei cavi (AP-0600-0029) in una finestra di manutenzione
- Poi pianificare gli aggiornamenti software (NK-2600-0089) con rete pulita

Questo elimina una fonte di confusione diagnostica e riduce il rischio di eventi sovrapposti.

---

## Valutazione delle analisi Grok

### AP-0600-0029
- **Completezza**: Alta. Problema, componenti, marcature e procedura di sostituzione ben documentati.
- **Accuratezza dello score**: Confermato. Risk 8.6 (Critical) è appropriato per un difetto hardware con nessun workaround.
- **Utilita' per il cliente**: Buona. Istruzioni chiare su come identificare i cavi e quando agire.

### NK-2600-0089
- **Completezza**: Accettabile. Il KBA è recente (marzo 2026) e descrive uno scenario raro ma plausibile.
- **Accuratezza dello score**: Confermato. Risk 5.4 (Advisory) riflette la rarità e la capacità di recupero automatico.
- **Utilita' per il cliente**: Moderata. Richiede azione preparatoria (disabilitazione SMB, monitoraggio rete) ma non intervento diretto durante il download.
- **Nota**: Per v15.x non è disponibile una patch — upgrade a v16+ è l'unica soluzione definitiva.
