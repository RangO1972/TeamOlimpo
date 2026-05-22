---
data: '2026-05-21'
timestamp: '2026-05-21T14:31:59'
agent: proteo
invocation: 28
type: analysis
status: completed
priority: high
title: Proteo - Analisi HW Sandy Bridge per inferenza LLM
task_id: T-ANALISI-005
---

# Technical Analysis: LLM Inference via Ollama on Intel Xeon E5-2620 v1 (Sandy Bridge-EP)

## Executive Summary

**System:** 2x Intel Xeon E5-2620 v1 (6C/12T per socket, 2.0/2.5 GHz)
**Memory:** DDR3-1333 ECC, 4 channels per socket, ~236 GB total
**ISA:** AVX only — **no** AVX2, FMA, F16C, AVX-512
**Inference engine:** Ollama → llama.cpp GGUF backend (CPU-only)

**Bottom line:** Token generation is severely bandwidth-constrained. Expect **2.5–5.5 tok/s** for 7–8B Q4 models on single-socket binding, and **4–9 tok/s** with NUMA interleaving. Prompt processing (prefill) will be disproportionately slower due to missing AVX2/FMA — expect minutes-waiting before first token for any context >2K.

---

## 1. Impact of Missing AVX2 on LLM Inference

### 1.1 How Ollama/llama.cpp handles CPUs without AVX2

Ollama ships pre-compiled CPU backends for multiple x86 ISA levels (from `ggml-cpu-sapphirerapids.so` down through `ggml-cpu-haswell.so`, `ggml-cpu-alderlake.so`, etc.). The runner auto-detects CPU features at load time and selects the most advanced compatible backend. On Sandy Bridge E5-2620 v1, Ollama will load the **AVX-only** variant. Confirmed by the detection flags in the ggml-cpu backend (Ollama issue #9087):

```
SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 0 | FMA = 0 | F16C = 0 | AVX512 = 0
```

Sandy Bridge-EP (2012) supports:
- ✅ SSE4.1/4.2
- ✅ AVX (128-bit and 256-bit vectors)
- ❌ AVX2 (integer FMA, gather, vector shifts — introduced Haswell 2013)
- ❌ FMA (Fused Multiply-Add — Haswell 2013)
- ❌ F16C (half-precision conversion — Ivy Bridge 2012)
- ❌ AVX-512 (Xeon Phi / Skylake-SP 2017)

### 1.2 Quantitative AVX vs AVX2 Performance Difference

**Key reference data from GGML development (PR #617, #996):**

| Operation | AVX-only | AVX2 | Ratio | Source |
|-----------|----------|------|-------|--------|
| `ggml_vec_dot_q4_0` (7B inference) | ~679 ns | ~590 ns | 1.15x | PR #617 |
| GEMV K=8, N=8192 | 15,194 FLOPS/us | 27,149 FLOPS/us | 1.79x | PR #996 |
| GEMV K=16, N=8192 | 8,224 FLOPS/us | 20,128 FLOPS/us | 2.45x | PR #996 |
| GEMV K=32, N=8192 | 9,397 FLOPS/us | 13,127 FLOPS/us | 1.40x | PR #996 |
| LoRA matmul K=16 | 9,831 ms | 5,142 ms | 1.91x | PR #996 |

**Impact by inference phase:**

| Phase | AVX penalty | Rationale |
|-------|-------------|-----------|
| **Token generation (GEMV)** | **10–20%** | Memory-bandwidth-bound; dequant + matmul is secondary. Small matrices in later layers see larger AVX impact. No FMA further hurts. |
| **Prompt processing (GEMM)** | **25–50%** | Compute-bound for batch >1. GEMM relies heavily on AVX2/FMA for tiled matmul. F16C adds ~8% to dequant overhead when missing. |
| **KV cache dequant** | **15–25%** | Q8_0 dequant uses F16C for scale conversion; software fallback significantly slower on Sandy Bridge. |

**Overall estimate:** Sandy Bridge E5-2620 v1 is approximately **15–20% slower** than Ivy Bridge (AVX2+F16C) at equal memory bandwidth, and **25–35% slower** than Haswell (AVX2+FMA+F16C).

**Sources:**
- PR #617: https://github.com/ggerganov/llama.cpp/pull/617
- PR #996: https://github.com/ggml-org/llama.cpp/pull/996
- PR #933: https://github.com/ggerganov/llama.cpp/pull/933 (AVX512 vs AVX2 benchmarks)

---

## 2. Realistic Sustainable Memory Bandwidth

### 2.1 Theoretical vs Real Bandwidth

**Per-socket specs (Intel ARK):**
- Channels: 4x DDR3-1333
- Theoretical peak: 4 x 8 B x 1333 MT/s = **42.6 GB/s**
- QPI: 2 links at 7.2 GT/s (each direction ~16 GB/s theoretical)

**Real-world measurements from published benchmarks:**

| Source | System | Memory | Measured BW | % of Peak |
|--------|--------|--------|-------------|-----------|
| CERN Open Lab (2012) | 2S E5-2680 (8C, DDR3-1600) | 4-ch DDR3-1600 | 42.2 GB/s local (8 threads) | 82.4% |
| CERN Open Lab | Same | Cross-socket QPI (8 GT/s) | 23.6 GB/s | 73.75% of QPI |
| TechReport Geekbench | E5-2620 @2.0 GHz | 4-ch DDR3-1333 | ~11.8 GB/s (STREAM vector, 1 core) | — |
| ADMIN Magazine (K. Rupp) | 2S SB-EP (general) | 4-ch DDR3 | ~78 GB/s total dual-socket | — |
| Dell whitepaper | 2S E5-2665 (8C, DDR3-1600) | 8-ch total (4/socket) | ~78 GB/s STREAM Triad | ~76% |

**Derived estimates for 2x E5-2620 v1 with DDR3-1333:**

| Scenario | Estimated Real BW | Basis |
|----------|-------------------|-------|
| **Single socket, local access** | **30–34 GB/s** | CERN's 42.2 GB/s @1600 MHz scaled by 1333/1600: 35.1 GB/s, minus lower clock |
| **Dual socket, NUMA interleaved** | **48–56 GB/s** | Local socket BW (~32) + QPI-limited remote (~19-22 GB/s via 7.2 GT/s) |
| **Single socket, LLM TG effective** | **14–18 GB/s** | ~50% utilization of STREAM BW (compute overhead + dequant + AVX penalty) |
| **Dual socket, LLM TG effective** | **22–28 GB/s** | Lower utilization due to QPI latency + access pattern inefficiency |

**Confidence:** Medium-High for per-socket BW (+/- 15%); Medium for dual-socket effective (+/- 25%).

### 2.2 NUMA Penalty: Cross-Socket Access via QPI

**The QPI bottleneck is severe for LLM inference.** Key evidence:

1. **CERN paper**: Cross-socket BW is 23.6 GB/s even at 8 GT/s QPI. Our 7.2 GT/s QPI yields ~21 GB/s.
2. **GitHub issue #19037**: Dual Xeon 8580 (16-ch DDR5, 563 GB/s theoretical) only 15% faster than single-socket w7-3565X for DeepSeek-V3 decode. Dual-socket efficiency dropped to 35%.
3. **GitHub issue #1437 discussion**: "llama.cpp doesn't really scale well with NUMA... using a single socket is best."
4. **CraftRigs guide**: "40-60% performance loss with cross-socket memory access on EPYC."

**Why cross-socket access hurts LLM inference:**
- Token generation reads ~5 GB of weights per token
- With NUMA interleaving, ~50% of reads hit the remote socket
- Remote reads traverse QPI with ~21 GB/s effective BW (vs ~32 GB/s local)
- Average BW = 0.5 x 32 + 0.5 x 21 = 26.5 GB/s — only 83% of local-only
- QPI adds latency (~100-150ns vs ~70ns local), further degrading effective utilization for small matrices (MoE)

### 2.3 Mitigation Strategies

| Strategy | Effective BW | Pros | Cons |
|----------|-------------|------|------|
| **NUMA binding** (`numactl --cpunodebind=0 --membind=0`) | ~30-34 GB/s (one socket) | No QPI penalty; best single-request perf | Only ~118 GB usable RAM |
| **NUMA interleaving** (`numactl --interleave=all`) | ~48-56 GB/s total | Full RAM available | QPI bottleneck; 15-25% worse than sum of parts |
| **NUMA distribute** (`--numa distribute`) | Variable | Distributes threads | Often worse than interleave; threads may mismatch memory nodes |
| **NUMA migrate** (PR #14232, June 2025) | Up to 33% uplift vs distribute | Migrates pages to local node | Not in Ollama; requires custom llama.cpp build |
| **NUMA mirror** (PR #14969, July 2025) | 64.6% uplift vs distribute | Mirrors model per NUMA node | Requires 2x RAM; experimental |

**Recommendation for this system:** `numactl --cpunodebind=0 --membind=0` for all models <=118 GB (all target models fit). This avoids the crippling QPI bottleneck entirely. For models needing both sockets (>118 GB), use `numactl --interleave=all` with `--numa numactl`.

**Sources:**
- CERN paper: https://openlab-archive-iv-v.web.cern.ch/...
- Issue #19037: https://github.com/ggml-org/llama.cpp/discussions/19037
- Issue #1437: https://github.com/ggerganov/llama.cpp/issues/1437
- CraftRigs guide: https://craftrigs.com/troubleshooting/llama-cpp-numa-warning-speed-fix-multi-socket/
- PR #14232: https://github.com/ggml-org/llama.cpp/pull/14232
- PR #14969: https://github.com/ggml-org/llama.cpp/pull/14969

---

## 3. Performance Estimates by Model (Tokens/Second)

### Methodology

**Reference anchor:** Xeon Gold 6312U (1S, 24C, 8-ch DDR4-3200, ~170 GB/s, AVX-512) achieves **21.25 tok/s** on 8B Q4_K_M (Source: ahelpme.com).

**Scaling logic:**
1. Gold 6312U LLM effective BW utilization: 21.25 tok/s x 4.92 GB = 104.5 GB/s
2. Our single-socket effective LLM BW: ~16 GB/s (50% of STREAM ~32 GB/s, adjusted for LLM access patterns)
3. BW ratio: 16/104.5 = 0.153
4. AVX penalty for TG: multiplier 0.82 (18% slower than AVX-512 reference)
5. Model size scaling: inversely proportional to model GB

**Single-socket formula for dense models:**
tok/s = 21.25 x (16 / 104.5) x (4.92 / model_GB) x 0.82

**Interleaved dual-socket:** ~24 GB/s effective → tok/s = 21.25 x (24/104.5) x (4.92 / model_GB) x 0.82

### Generation Speed Table (Q4_K_M quantization)

| Model | Params | Q4_K_M Size | Tok/s (Single Socket) | Tok/s (Interleaved) |
|-------|--------|-------------|----------------------|---------------------|
| **Qwen2.5-Coder 3B** | 3B | ~2.5 GB | **5.3 +/- 0.8** | **8.0 +/- 1.2** |
| **Qwen2.5-Coder 7B** | 7B | ~4.7 GB | **2.8 +/- 0.4** | **4.2 +/- 0.6** |
| **Qwen2.5-Coder 14B** | 14B | ~9 GB | **1.5 +/- 0.2** | **2.2 +/- 0.3** |
| **Qwen2.5-Coder 32B** | 32B | ~20 GB | **0.65 +/- 0.1** | **1.0 +/- 0.15** |
| **DeepSeek Coder V2 Lite 16B (MoE)** | 16B/2.4B active | ~10 GB | **2.2 +/- 0.5** | **3.2 +/- 0.7** |
| **Qwen3-Coder-30B-A3B (MoE)** | 30B/3.3B active | ~18 GB | **2.5 +/- 0.5** | **3.5 +/- 0.8** |
| **Qwen3 8B** | 8B | ~5 GB | **2.7 +/- 0.4** | **4.0 +/- 0.6** |

**MoE model penalty:** MoE models underperform bandwidth math by 3-5x on CPU due to small expert matrices (2048x7168 for DeepSeek). These have low arithmetic intensity and poor cache utilization. Based on issue #19480 (7.74 tok/s observed vs 20-30+ expected on DDR5-5600). On our slower DDR3 with higher latency, the penalty is even more severe. Estimates derived from:
- Active parameter bandwidth math: data_per_token = active_params x bytes_per_param
- Divided by 4-6x "MoE small-matrix penalty"
- DeepSeek Coder V2 Lite: 2.4B active x 0.5 bytes (Q4) = 1.2 GB/token → BW math ~13 tok/s, / 6x = ~2.2 tok/s
- Qwen3-Coder-30B-A3B: 3.3B active x 0.5 bytes = 1.65 GB/token → BW math ~10 tok/s, / 4x = ~2.5 tok/s

### Confidence Levels

| Category | Confidence | Reason |
|----------|-----------|--------|
| Dense models | **Medium** (+/- 25%) | BW scaling reliable; AVX penalty estimated from limited published data |
| MoE models | **Low-Medium** (+/- 35%) | CPU MoE behavior poorly documented; high variance across implementations |
| Prompt prefill | **Low** (+/- 40%) | GEMM on AVX-only is model- and implementation-dependent |

**Sources:**
- Gold 6312U: https://ahelpme.com/ai/llm-inference-benchmarks-with-llamacpp-and-xeon-gold-6312u-cpu/
- MoE CPU issue: https://github.com/ggml-org/llama.cpp/issues/19480
- CPU inference guide: https://llmhardware.io/guides/cpu-only-llm-inference
- InsiderLLM: https://insiderllm.com/guides/cpu-only-llms-what-actually-works/

---

## 4. Prompt Eval (Prefill) Speed

### Why Prefill is Disproportionately Slow

Prompt processing uses GEMM (compute-bound, batch_size = prompt length). Unlike token generation (bandwidth-bound), GEMM scales with FLOPS capacity. Sandy Bridge E5-2620 v1 is severely limited:
- Theoretical peak: 6 cores x 2.0 GHz x 8 FLOP/cycle (AVX 256-bit) = **96 GFLOPS**
- Without FMA: effective ~48 GFLOPS for most operations
- With Q4_K_M dequant overhead: only ~10-20% of peak achievable (~5-10 GFLOPS)

For comparison, the Gold 6312U achieves ~1,200-1,800 tok/s on pp512 for 8B Q4_K_M. Our Sandy Bridge is ~50-200x slower in GEMM throughput.

### Estimated Prefill Speed (Single Socket, AVX-only)

| Model | 1K tokens | 8K tokens | 32K tokens |
|-------|-----------|-----------|------------|
| Qwen2.5-Coder 3B | 30-50 tok/s | 15-25 tok/s | 8-12 tok/s |
| Qwen2.5-Coder 7B | 8-15 tok/s | 5-10 tok/s | 3-6 tok/s |
| Qwen2.5-Coder 14B | 4-7 tok/s | 2-5 tok/s | 1.5-3 tok/s |
| Qwen2.5-Coder 32B | 1.5-3 tok/s | 1-2 tok/s | 0.5-1 tok/s |
| Qwen3 8B | 8-14 tok/s | 5-9 tok/s | 3-5 tok/s |

**Time to first token (TTFT) for 8K prompt on 7B Q4:**
~1,143 seconds at 7 tok/s prefill ≈ **19 minutes** before generation starts.

**This is the single biggest usability problem on this hardware.** Any chat with >2K context history will have crippling prefill latency.

### Recommendations for Prefill
- Minimize context window: `--ctx-size 4096` or lower
- Use `--batch-size 128` (smaller batches reduce compute waste; default 2048 is GPU-oriented)
- Flash attention: **OFF** on CPU (adds overhead, no benefit)
- For RAG: truncate context to 2K-4K tokens; re-rank aggressively
- Pre-process documents offline; store embeddings, not raw text

---

## 5. KV Cache and Context Impact

### 5.1 KV Cache Size (f16, per token)

| Model | n_layers | n_kv_heads | d_head | KV per token |
|-------|----------|------------|--------|-------------|
| Qwen2.5-Coder 3B | 24 | 4 | 128 | ~96 KB |
| Qwen2.5-Coder 7B | 28 | 8 | 128 | ~224 KB |
| Qwen2.5-Coder 14B | 40 | 8 | 128 | ~320 KB |
| Qwen2.5-Coder 32B | 64 | 8 | 128 | ~512 KB |
| DeepSeek Coder V2 Lite MoE | 27 | 4 | 128 | ~108 KB |
| Qwen3-Coder-30B-A3B MoE | 62 | 10 | 128 | ~496 KB |
| Qwen3 8B | 32 | 8 | 128 | ~256 KB |

### 5.2 Impact of Context on Generation Speed

With f16 KV cache, for a 7B model (4.7 GB weights):

| Context | KV size | Total data/token | Speed loss vs 4K |
|---------|---------|-----------------|-----------------|
| 4K | 0.88 GB | ~5.6 GB | baseline |
| 8K | 1.75 GB | ~6.5 GB | -14% |
| 32K | 7 GB | ~11.7 GB | -52% |
| 128K | 28 GB | ~32.7 GB | -83% |

At 128K context, 7B Q4 on single socket would drop to ~0.8 tok/s.

### 5.3 KV Cache Compression

| Cache type | Bits/elem | Size vs f16 | CPU TG speed | CPU PP speed | Quality |
|------------|-----------|-------------|-------------|-------------|---------|
| **f16** (default) | 16 | 1x | baseline | baseline | baseline |
| **q8_0** | 8 | **0.5x** | +5-10% (less BW) | -1-2% | Near-lossless |
| q4_0 | 4 | 0.25x | +10-15% | **-35% to -92%** (long ctx) | Noticeable |

**Critical finding:** q4_0 KV cache is dangerous on CPU. DGX Spark benchmarks (March 2026) showed **92.5% collapse** in prompt processing speed at 64K context with q4_0 vs f16 (Source: NVIDIA Forums). On Sandy Bridge without F16C, the dequant overhead is even worse.

**Recommendation:** Use `--cache-type-k q8_0 --cache-type-v q8_0` for any context >8K. Never use q4_0 KV cache on this CPU.

**Sources:**
- DGX Spark KV cache: https://wiki.charleschen.ai/Review/Research/kv-cache-q8_0-llamacpp-spark
- PR #2969: https://github.com/ggerganov/llama.cpp/pull/2969
- KV quant arXiv paper: https://arxiv.org/pdf/2601.14277

---

## 6. Technical Recommendations for Ollama

### 6.1 Thread Configuration

**OLLAMA_NUM_THREADS = 6** (physical cores of one socket). SMT/hyperthreading **degrades** memory-bandwidth-bound workloads.

From Ollama PR #6264: "one thread per physical core is optimal." From Ollama PR #7322: on dual-socket systems without proper NUMA support, default to physical cores of one socket. Never exceed 12 (total physical cores across both sockets).

**OLLAMA_NUM_PARALLEL = 1.** Multiple parallel requests destroy single-request throughput on CPU. Source: llmhardware.io optimization guide.

### 6.2 Flash Attention: OFF

Flash attention in llama.cpp is optimized for CUDA (GPU). On CPU it adds overhead with no throughput benefit. Multiple GitHub discussions confirm this. Leave disabled.

Exception: theoretically useful at very long context (>32K) for memory reduction, but the dequant overhead on Sandy Bridge would negate any benefit.

### 6.3 Batch Size

Start with `--batch-size 128`, benchmark against 64 and 256. The default 512-2048 range targets GPU; on CPU it causes excessive memory allocation without throughput gain. Source: Ollama Tuning Guide.

### 6.4 Optimal Ollama Configuration

```bash
# Environment variables
export OLLAMA_NUM_THREADS=6
export OLLAMA_MLOCK=1
export OLLAMA_NUM_PARALLEL=1

# NUMA: bind to single socket
numactl --cpunodebind=0 --membind=0 ollama serve

# Modelfile for each model
FROM qwen2.5-coder:7b-base-q4_K_M
PARAMETER num_thread 6
PARAMETER batch_size 128
PARAMETER num_ctx 4096
```

### 6.5 OS-Level Tuning

```bash
# Disable NUMA balancing (reduces page migration overhead)
echo 0 | sudo tee /proc/sys/kernel/numa_balancing

# Set CPU governor to performance
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

# Reduce swappiness (keep model pages in RAM, avoid swap)
echo 10 | sudo tee /proc/sys/vm/swappiness

# Reduce dirty page ratios (less background IO during inference)
echo 10 | sudo tee /proc/sys/vm/dirty_ratio
echo 5 | sudo tee /proc/sys/vm/dirty_background_ratio

# Lock model in RAM via mlock
export OLLAMA_MLOCK=1
```

### 6.6 Alternative: llama.cpp Direct (for ~10-20% more speed)

Ollama adds ~5-15% overhead vs raw llama.cpp (Source: DeployBase comparison). For maximum performance:

```bash
./llama-cli \
  -m qwen2.5-coder-7b-q4_k_m.gguf \
  -t 6 \
  -c 4096 \
  -b 128 \
  --mlock \
  --numa isolate \
  --cache-type-k q8_0 \
  --cache-type-v q8_0 \
  --temp 0.7
```

### 6.7 Quick Benchmarking Command

To establish a real baseline on the actual hardware:

```bash
# Install Ollama, pull a small model
ollama pull llama3.2:3b-q4_k_m

# Warm-up run
ollama run llama3.2:3b-q4_k_m "Hello" > /dev/null

# Timed benchmark
time ollama run llama3.2:3b-q4_k_m "Write a 100-word paragraph about artificial intelligence." --verbose 2>&1 | grep -E "eval rate|prompt eval"

# For raw llama.cpp benchmark
./llama-bench -m llama3.2-3b-q4_k_m.gguf -t 6 -p 512 -n 128
```

**Sources:**
- Ollama thread selection: PR #6264 (https://github.com/ollama/ollama/pull/6264)
- NUMA refinement: PR #7322 (https://github.com/ollama/ollama/pull/7322)
- OLLAMA_NUM_THREADS env: PR #15421 (https://github.com/ollama/ollama/pull/15421)
- CPU tuning guide: https://github.com/jameschrisa/Ollama_Tuning_Guide
- llama.cpp vs Ollama: https://deploybase.ai/articles/llama-cpp-vs-ollama
- InsiderLLM guide: https://insiderllm.com/guides/cpu-only-llms-what-actually-works/

---

## 7. Overall Assessment

### Summary Table

| Metric | Value | Usability Rating |
|--------|-------|-----------------|
| 7B Q4_K_M gen (single socket) | **2.8 tok/s** | Yellow: marginal for chat, OK for batch |
| 7B Q4_K_M gen (interleaved) | **4.2 tok/s** | Yellow: barely usable for interactive |
| 3B Q4_K_M gen (single socket) | **5.3 tok/s** | Green: acceptable for simple Q&A |
| 14B Q4_K_M gen (single socket) | **1.5 tok/s** | Red: painfully slow |
| 32B Q4_K_M gen (single socket) | **0.65 tok/s** | Red: impractical |
| 8K prompt prefill (7B) | **19 min TTFT** | Red: unusable for chat |

### Key Takeaways

1. **Only 3B models are comfortably usable.** 7B models are marginal with very short contexts.
2. **Prompt processing is the dominant bottleneck**, not token generation — expect minutes of prefill for any non-trivial context.
3. **Single-socket NUMA binding is mandatory.** Using both sockets degrades performance vs one socket due to QPI bottleneck.
4. **Never exceed 4K context** unless you can tolerate 2-3x slowdown in generation and 10x+ in prefill.
5. **AVX2/FMA/F16C absence is a secondary issue** — DDR3-1333 bandwidth is the primary bottleneck.
6. **MoE models do NOT deliver their theoretical advantage** on this hardware. Small matrix operations kill bandwidth utilization.

### Explicit Gaps (Unverifiable)

- **No direct Ollama benchmark on E5-2620 v1 was found anywhere.** All estimates are scaled from architecturally similar systems (E5-2680, E5-2665, E5-2670) with appropriate adjustments for clock speed, memory frequency, and core count.
- **AVX vs AVX2 gap in the current Q4_K_M path** is estimated from 2023-era vec_dot benchmarks (PR #617, #996). The current llama.cpp codebase may have diverged.
- **DDR3 latency impact on MoE small-matrix efficiency** is extrapolated from DDR5 data (issue #19480), not independently measured on DDR3.
- **Ollama backend auto-detection behavior** on this specific CPU has not been confirmed in published community tests. A real `ollama run` test is needed to verify which backend .so is selected.
- **Actual scaling between single-socket and interleaved** depends on the specific NUMA topology of the motherboard, which varies by vendor implementation (Supermicro, Dell, HP, etc.).

### Recommended Next Steps

1. Run `ollama run llama3.2:3b-q4_k_m` to establish a real baseline on this hardware.
2. Verify which CPU backend Ollama selects: `journalctl -u ollama --no-pager | grep "load_backend"`
3. Benchmark single-socket (numactl bind) vs interleaved: the difference will confirm QPI penalty magnitude for this specific system.
4. If performance is <2 tok/s on 7B, consider using llama.cpp directly for the ~10-20% overhead reduction.
5. For production use: consider an Ivy Bridge or Haswell Xeon upgrade (E5-2690 v2, DDR3-1866) which adds AVX2+F16C and higher memory bandwidth for ~2x performance improvement at minimal eBay cost.
