---
kba: NK-2600-0096
formato: sintesi_cliente
siti: Termoli, Montecchio, Lonigo
data: 2026-04-02
---

## NK-2600-0096 — Reset software blocchi ECTLSL in composite

**Rischio**: Warning | **Siti**: Termoli, Montecchio, Lonigo

---

### Il problema

Quando un blocco ECTLSL (Enhanced Control) è configurato con una discrepanza tra il numero di parametri estensibili e il valore del parametro `NOF_USED_SEL`, e il blocco è all'interno di un composite (struttura di controllo gerarchica), il download del modulo provoca un reset software-generato sul nodo controller. Durante il reset, il controller standby non riesce a prendere il controllo automaticamente, causando la perdita della ridondanza e l'apparizione di un triangolo giallo su DeltaV Explorer. Per ripristinare il controllo è necessaria una Total Download (azione invasiva).

**Semplice**: Il software non valida correttamente la configurazione del blocco ECTLSL quando è dentro un composite. Il reset può sorprendere durante un download di routine.

---

### Componenti coinvolti

- Blocchi ECTLSL (Enhanced Control) all'interno di composites
- Software controller: DeltaV v14.FP1 → v16.LTS (9 versioni affette)
- Sistema DeltaV sui vostri 3 impianti

---

### Quando si manifesta

**Condizioni specifiche**:
1. Avete un blocco ECTLSL dentro un composite
2. Il numero di parametri estensibili NON corrisponde al valore di `NOF_USED_SEL`
3. Fate un download del modulo

**Nota importante**: Se il blocco ECTLSL fosse standalone (non in composite), DeltaV catcaterebbe l'errore e vi impedirebbe di salvare il modulo. Ma quando è in composite, la validazione è bypassata — il software non ve lo segnala come errore, e il problema emerge solo al download.

---

### Cosa serve dal cliente

#### Verificare subito (prossime 2 settimane)

1. **Audit dei blocchi ECTLSL** — Controllare tutti i moduli con blocchi ECTLSL che sono dentro composites (revisare in DeltaV Explorer ogni progetto dove usate Enhanced Control)

2. **Confirmation della versione software** — Confermare quale versione DeltaV avete sui controller (se è v14.FP1 → v16.LTS, siete interessati)

3. **Elenco configurazioni potenzialmente a rischio** — Se trovate blocchi ECTLSL in composite, sarebbe utile che ci comunichiate quanti ne avete e in quali loop di controllo (priorità per critici first)

#### Se trovate la discrepanza

4. **Tempificazione della correzione** — Entro le prossime fermate pianificate, applicare il workaround:
   - Aprire il blocco ECTLSL in Control Studio
   - Allineare il parametro `NOF_USED_SEL` al numero di parametri estensibili effettivi
   - Salvare e downloadare il modulo

---

## Status Emerson

Emerson ha classificato questo come "Next Service Interval" — non è critico urgente, ma va gestito. Non c'è patch disponibile al momento (è in fase di indagine).

---

## Contatti per supporto

Per domande sulla configurazione degli ECTLSL nei vostri impianti, contattateci direttamente. Questo è un problema specifico di configurazione che richiede una revisione caso per caso sui vostri sistemi.
