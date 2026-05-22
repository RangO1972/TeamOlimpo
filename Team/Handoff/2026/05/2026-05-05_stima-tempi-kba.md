---
title: "Stima Tempi per Patching/Installazione KBA"
tags: [stima, tempi, kba]
aliases: [Stima Tempi Patching KBA]
---

# Stima Tempi per Patching/Installazione KBA

## Introduzione e Assunzioni
Analisi strategica delle 30 KBA univoche che richiedono azioni di patching/installazione, basata su report Proteo. Stima tempi in ore considerando complessità (simple: 1h/sito, medium: 2h/sito) e logistica (+0.5h per sito remoto).

- **Tempo base**: 1 ora per patch simple per sito, 2 ore per medium per sito (include preparazione, esecuzione batch su nodi, verifica).
- **Scalabilità**: Non scalato per numero nodi individuali (applicazione batch automatica).
- **Logistica**: +0.5h per sito remoto (Montecchio, Lonigo); Termoli centrale (0).
- **Calcolo**: Totale KBA = somma tempi per siti in cui presente.

## Tabella KBA (Dettaglio)

| KBA | Tipo | Siti | Calcolo (ore base + logistica) | Totale KBA |
|-----|------|------|-------------------------------|------------|
| NK-1800-0831 | medium | Montecchio | 2×1 + 0.5 | 2.5 |
| AK-1300-0005 | medium | T, M, L | 2×3 + 0.5×2 | 7.0 |
| AK-1200-0033 | medium | Lonigo | 2×1 + 0.5 | 2.5 |
| NK-2000-0562 | medium | M, L | 2×2 + 0.5×2 | 5.0 |
| NK-2300-0446 | medium | T, M, L | 2×3 + 0.5×2 | 7.0 |
| NK-2200-0460 | medium | T, M | 2×2 + 0.5×1 | 4.5 |
| NK-2600-0129 | simple | T, M, L | 1×3 + 0.5×2 | 4.0 |
| NK-2600-0071 | simple | T, M, L | 1×3 + 0.5×2 | 4.0 |
| NK-2600-0097 | simple | T, M, L | 1×3 + 0.5×2 | 4.0 |
| NK-2300-0379 | medium | Termoli | 2×1 + 0 | 2.0 |
| NK-2500-0143 | medium | Termoli | 2×1 + 0 | 2.0 |
| NK-2400-0329 | medium | Termoli | 2×1 + 0 | 2.0 |
| NK-2400-0193 | simple | Termoli | 1×1 + 0 | 1.0 |
| NK-2300-0291 | medium | Montecchio | 2×1 + 0.5 | 2.5 |
| NK-1900-1197 | medium | Termoli | 2×1 + 0 | 2.0 |
| NK-2000-0197 | medium | Termoli | 2×1 + 0 | 2.0 |
| NK-2400-0177 | medium | Termoli | 2×1 + 0 | 2.0 |
| NK-2600-0096 | simple | T, M, L | 1×3 + 0.5×2 | 4.0 |
| NK-2200-0138 | medium | Montecchio | 2×1 + 0.5 | 2.5 |
| NK-2500-0646 | medium | T, M, L | 2×3 + 0.5×2 | 7.0 |
| NK-1700-0089 | medium | Termoli | 2×1 + 0 | 2.0 |
| NK-2600-0005 | medium | Montecchio | 2×1 + 0.5 | 2.5 |
| NK-2500-0638 | medium | T, M | 2×2 + 0.5×1 | 4.5 |
| NK-2500-0045 | medium | Termoli | 2×1 + 0 | 2.0 |
| NK-2500-0639 | medium | T, M | 2×2 + 0.5×1 | 4.5 |
| NK-2500-0189 | medium | Lonigo | 2×1 + 0.5 | 2.5 |
| NK-2400-0257 | medium | Lonigo | 2×1 + 0.5 | 2.5 |
| NK-2300-0470 | medium | Lonigo | 2×1 + 0.5 | 2.5 |
| NK-2300-0351 | medium | Montecchio | 2×1 + 0.5 | 2.5 |
| NK-2300-0102 | medium | Montecchio | 2×1 + 0.5 | 2.5 |

## Aggregati per Sito

| Sito | # KBA | Simple | Medium | Ore base | Logistica | Totale sito |
|------|-------|--------|--------|----------|-----------|-------------|
| Termoli (centrale) | 19 | 5 | 14 | 33h | 0 | 33.0h |
| Montecchio (remoto) | 17 | 4 | 13 | 30h | 8.5h | 38.5h |
| Lonigo (remoto) | 12 | 4 | 8 | 20h | 6h | 26.0h |

## Totale Complessivo

**97.5 ore**

## Osservazioni

- Logica applicata correttamente, ma verificare se tempo sottostimato per KBA con molti nodi.
- KBA NK-2000-0197 ubicazione da confermare.
- Colli di bottiglia: Montecchio più oneroso (38.5h totali).
- Ottimizzazioni: sequenzializzazione per sito/tipo, raggruppamento visite remote.
- Domanda aperta: stima per KBA per sito o scalare per numero nodi?
