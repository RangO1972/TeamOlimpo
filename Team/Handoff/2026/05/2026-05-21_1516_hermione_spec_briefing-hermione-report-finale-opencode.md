---
data: '2026-05-21'
timestamp: '2026-05-21T15:16:47'
agent: hermione
invocation: 1
type: spec
status: in_progress
priority: high
title: Briefing Hermione — Report finale OpenCode su Sandy Bridge
task_id: T-ANALISI-008
---

# Briefing: Report Finale — OpenCode su Xeon E5-2620 Sandy Bridge

## Compito
Scrivere un **report finale completo in stile saggistico** che sintetizzi l'analisi hardware + benchmark modelli per l'utilizzo di OpenCode con Ollama su un sistema **CPU-only con 2× Intel Xeon E5-2620 v1 (Sandy Bridge-EP, DDR3-1333, no AVX2)**.

Il report deve essere un documento autonomo, vault-ready, salvato in `Library/deliverables/`.

## Fonti (handoff già completati)

### 1. Proteo — Analisi HW Sandy Bridge (`Team/Handoff/2026/05/2026-05-21_1431_proteo_analysis_proteo-analisi-hw-sandy-bridge.md`)
Copre:
- Architettura Sandy Bridge-EP vs ISA moderne (no AVX2/FMA/F16C)
- Stime bandwidth realistica: ~30-34 GB/s single-socket, ~48-56 GB/s interleaved
- Stime tok/s per modello (Q4_K_M): 7B ~2.8 tok/s, 14B ~1.5 tok/s, 32B ~0.65 tok/s
- Impacto NUMA: QPI bottleneck analysis — raccomandazione `numactl --cpunodebind=0 --membind=0`
- KV cache analysis: contesto >4K penalizza pesantemente, raccomandazione Q8_0 KV cache
- Config ottimale Ollama: OLLAMA_NUM_THREADS=6, batch_size=128, ctx_size=4096
- Prompt prefill (bottleneck principale): 8K prompt = ~19 minuti TTFT su 7B
- Raccomandazioni OS tuning (NUMA balancing, governor, swappiness)

### 2. Pythagoras — Benchmark modelli coding (`Team/Handoff/2026/05/2026-05-21_1428_pythagoras_report_pythagoras-benchmark-modelli-coding-e.md`)
Copre:
- OpenCode technical requirements (tool_call_format, context window)
- HumanEval/MBPP/LiveCodeBench per serie Qwen, DeepSeek, Codestral, Gemma 4
- BFCL tool calling benchmarks
- Analisi MoE vs Dense su CPU bandwidth-limited (MoE è PEGGIO su CPU)
- Raccomandazioni quantizzazione: Q5_K_M sweet spot, Q4_K_M fallback
- Modelli raccomandati per target: Qwen2.5-Coder 7B/14B/32B, Qwen3 8B
- Modelli da evitare: MoE (Qwen3-Coder-30B-A3B, DeepSeek-Coder-V2-Lite), DeepSeek-R1 distill (thinking tokens rompono tool calling)

## Struttura richiesta per il report

Il report dovrebbe essere un documento **saggistico completo e autonomo** (non una semplice sintesi). Stile: tecnico ma scorrevole, adatto a un lettore tecnico che deve decidere se e come usare OpenCode su questa macchina.

### Sezioni suggerite:

1. **Premessa / Contesto** — Obiettivo: valutare OpenCode + modelli locali su server Xeon E5-2620 v1
2. **Hardware** — Architettura, bandwidth, ISA limitation, NUMA topology, stime performance
3. **Modelli** — Benchmark coding, tool calling, MoE vs Dense, quantizzazione
4. **Prestazioni stimate** — Tabella tok/s per modello (single-socket e interleaved), prefill TTFT
5. **Configurazione raccomandata** — Ollama config, OS tuning, NUMA binding, KV cache
6. **Raccomandazioni finali** — Quali modelli usare, cosa evitare, trade-off qualità/velocità, possibili upgrade
7. **Appendice** — Comandi benchmark, riferimenti

### Tono e stile
- Italiano tecnico, chiaro e autorevole
- Dati e fonti citati (con riferimenti)
- Giudizio franco su cosa FUNZIONA vs cosa NON FUNZIONA su questo hardware
- Tabella riassuntiva finale "Modello → Tok/s → Giudizio"

## Output
Salva il report in `Library/deliverables/report-opencode-sandy-bridge-2026-05-21.md`

## Note
- Questo report è destinato all'utente finale. Deve essere completo, autonomo e professionale.
- Non è richiesta nuova ricerca — tutto il necessario è nelle due fonti sopra.
- Il report deve riflettere la realtà di questo hardware: nessun abbellimento, nessun ottimismo ingiustificato.
