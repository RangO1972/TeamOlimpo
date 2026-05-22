---
data: '2026-05-21'
timestamp: '2026-05-21T14:30:30'
agent: proteo
invocation: 27
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

**Bottom line:** Token generation is severely bandwidth-constrained. Expect **2.5–5.5 tok/s** for 7–8B Q4 models on single-socket binding, and **4–9 tok/s** with NUMA interleaving. Prompt processing (prefill) will be disproportionately slower due to missing AVX2/FMA — expect minutes of waiting before first token for any context >2K.

---

## 1. Impact of Missing AVX2 on LLM Inference

### 1.1 How Ollama/llama.cpp handles CPUs without AVX2

Ollama ships pre-compiled CPU backends for multiple x86 ISA levels (`ggml-cpu-*.so`). The runner auto-detects CPU features at load time and selects the most advanced compatible backend. On Sandy Bridge E5-2620 v1, Ollama will load the **AVX-only** variant. The detection vector confirmed by Ollama GitHub issue #9087 and the ggml-cpu codebase:

```
SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 0 | FMA = 0 | F16C = 0 | AVX512 = 0
```

Sandy Bridge-EP (2012) supports:
- ✅ SSE4.1/4.2
- ✅ AVX (128-bit and 256-bit vectors)
- ❌ AVX2 (integer FMA, gather, vector shifts — introduced Haswell 2013)
- ❌ FMA (Fused Multiply-Add — Haswell 2013)
- ❌ F16C (half-precision conversion — Ivy Bridge 2012)
- ❌ AVX-512

### 1.2 Quantitative AVX vs AVX2 Performance Difference

**Key reference data from GGML development (PR #617, #996):**

| Operation | AVX-only | AVX2 | Ratio | Source |
|-----------|----------|------|-------|--------|
| `ggml_vec_dot_q4_0` (7B inference) | ~679 ns | ~590 ns | 1.15x | PR #617 |
| GEMV K=8, N=8192 | 15,194 FLOPS/us | 27,149 FLOPS/us | 1.79x | PR #996 |
| GEMV K=16, N=8192 | 8,224 FLOPS/us | 20,128 FLOPS/us | 2.45x | PR #996 |
| LoRA matmul K=16 | 9,831 ms | 5,142 ms | 1.91x | PR #996 |

**Impact by inference phase:**

| Phase | AVX penalty | Rationale |
|-------|-------------|-----------|
| **Token generation (GEMV)** | **10–20%** | Memory-bandwidth-bound; dequant + matmul is secondary. No FMA adds further overhead. |
| **Prompt processing (GEMM)** | **25–50%** | Compute-bound for batch >1. GEMM relies heavily on AVX2/FMA for tiled matmul. |
| **KV cache dequant** | **15–25%** | Q8_0 dequant uses F16C for scale conversion; software fallback slower. |

**Overall:** Sandy Bridge E5-2620 v1 is ~15–20% slower than Ivy Bridge (AVX2+F16C) and ~25–35% slower than Haswell (AVX2+FMA+F16C) at equal memory bandwidth.

**Sources:**
- PR #617: https://github.com/ggerganov/llama.cpp/pull/617
- PR #996: https://github.com/ggml-org/llama.cpp/pull/996
- PR #933: https://github.com/ggerganov/llama.cpp/pull/933 (AVX512 vs AVX2)

---

## 2. Realistic Sustainable Memory Bandwidth

### 2.1 Theoretical vs Real Bandwidth

**Per-socket specs (Intel ARK):** 4-ch DDR3-1333 → 42.6 GB/s theoretical peak

**Real-world measurements:**

| Source | System | Memory | Measured BW | % of Peak |
|--------|--------|--------|-------------|-----------|
| CERN Open Lab (2012) | 2S E5-2680 (8C, DDR3-1600) | 4-ch DDR3-1600 | 42.2 GB/s local (8 threads) | 82.4% |
| CERN Open Lab | Same | Cross-socket QPI (8 GT/s) | 23.6 GB/s | 73.75% of QPI BW |
| ADMIN Magazine (K.Rupp) | 2S SB-EP (general) | 4-ch DDR3 | ~78 GB/s total dual-socket | — |
| Dell whitepaper | 2S E5-2665 (8C, DDR3-1600) | 8-ch total (4/socket) | ~78 GB/s STREAM Triad | ~76% |

**Derived estimates for our system (2x E5-2620 v1, DDR3-1333):**

| Scenario | Estimated Real BW | Basis |
|----------|-------------------|-------|
| **Single socket, local access** | **30–34 GB/s** | CERN's 42.2 GB/s @1600 MHz scaled by 1333/1600 = 35 GB/s, minus IMC efficiency |
| **Dual socket, NUMA interleaved** | **48–56 GB/s** | Local ~32 + QPI-limited remote ~19-22 GB/s |
| **Single socket, LLM TG effective** | **14–18 GB/s** | ~50% utilization of STREAM BW (compute + AVX overhead) |
| **Dual socket, LLM TG effective** | **22–28 GB/s** | Lower utilization due to QPI latency |

### 2.2 NUMA Penalty: Cross-Socket Access via QPI

**The QPI bottleneck is severe for LLM inference.**

Key evidence:
1. **CERN paper**: Cross-socket BW is 23.6 GB/s even at 8 GT/s QPI. Our 7.2 GT/s QPI yields ~21 GB/s.
2. **GitHub #19037**: Dual Xeon 8580 (16-ch DDR5, 563 GB/s theor.) only 15% faster than single-socket w7-3565X for DeepSeek-V3. Dual-socket efficiency dropped to 35%.
3. **GitHub #1437**: "llama.cpp doesn't really scale well with NUMA... using a single socket is best."
4. **CraftRigs guide**: "40-60% performance loss with cross-socket memory access on EPYC."

**Why it hurts:** With NUMA interleaving, ~50% of memory reads hit the remote socket via QPI (~21 GB/s, ~100-150ns latency) instead of local (~32 GB/s, ~70ns). Average BW drops to ~26.5 GB/s — only 83% of local-only — plus latency penalties reduce effective utilization further.

### 2.3 Mitigation Strategies

| Strategy | Effective BW | Pros | Cons |
|----------|-------------|------|------|
| **NUMA binding** (`numactl --cpunodebind=0 --membind=0`) | ~30-34 GB/s (1 socket) | No QPI penalty; best single-request perf | Only ~118 GB usable RAM |
| **NUMA interleaving** (`numactl --interleave=all`) | ~48-56 GB/s total | Full RAM usable | QPI bottleneck; 15-25% worse than sum |
| **NUMA migrate** (PR #14232) | Up to 33% uplift vs distribute | Migrates pages to local node | Not in Ollama; needs custom build |
| **NUMA mirror** (PR #14969) | 64.6% uplift vs distribute | Eliminates cross-socket reads | Needs 2x RAM; experimental |

**Recommendation:** `numactl --cpunodebind=0 --membind=0` for all models ≤118 GB (all targets fit). This avoids the QPI bottleneck entirely.

**Sources:**
- CERN paper: https://openlab-archive-iv-v.web.cern.ch/...
- Issue #19037: https://github.com/ggml-org/llama.cpp/discussions/19037
- Issue #1437: https://github.com/ggerganov/llama.cpp/issues/1437
- CraftRigs guide: https://craftrigs.com/troubleshooting/llama-cpp-numa-warning-speed-fix-multi-socket/

---

## 3. Performance Estimates by Model (Tokens/Second)

### Methodology

**Reference anchor:** Xeon Gold 6312U (1S, 24C, 8-ch DDR4-3200, ~170 GB/s, AVX-512) → **21.25 tok/s** on 8B Q4_K_M (Source: ahelpme.com).

**Scaling:** tok/s ∝ (effective BW / model_size) × AVX_penalty × utilization_factor.

**Single-socket anchor calculation:**
- Gold 6312U LLM TG BW utilization: 21.25 tok/s × 4.92 GB = 104.5 GB/s
- Our single-socket effective LLM BW: ~16 GB/s (50% of STREAM ~32 GB/s)
- BW ratio: 16/104.5 = 0.153
- AVX penalty (TG): 0.82 (18% slower than AVX-512 reference)
- 8B estimate: 21.25 × 0.153 × 0.82 = 2.67 tok/s

**Interleaved anchor:** Dual-socket effective ~24 GB/s → 21.25 × (24/104.5) × 0.82 = 4.00 tok/s for 8B.

### Generation Speed Table (Q4_K_M quantization)

| Model | Params | Q4_K_M Size | Tok/s (Single Socket) | Tok/s (Interleaved) |
|-------|--------|-------------|----------------------|---------------------|
| Qwen2.5-Coder 3B | 3B | ~2.5 GB | **5.3 +/- 0.8** | **8.0 +/- 1.2** |
| Qwen2.5-Coder 7B | 7B | ~4.7 GB | **2.8 +/- 0.4** | **4.2 +/- 0.6** |
| Qwen2.5-Coder 14B | 14B | ~9 GB | **1.5 +/- 0.2** | **2.2 +/- 0.3** |
| Qwen2.5-Coder 32B | 32B | ~20 GB | **0.65 +/- 0.1** | **1.0 +/- 0.15** |
| DeepSeek Coder V2 Lite 16B (MoE) | 16B/2.4B active | ~10 GB | **2.2 +/- 0.5** | **3.2 +/- 0.7** |
| Qwen3-Coder-30B-A3B (MoE) | 30B/3.3B active | ~18 GB | **2.5 +/- 0.5** | **3.5 +/- 0.8** |
| Qwen3 8B | 8B | ~5 GB | **2.7 +/- 0.4** | **4.0 +/- 0.6** |

**Dense model formula:** tok_single = 21.25 * (16 / 104.5) * (4.92 / model_GB) * 0.82

**MoE models penalized 3-5x vs bandwidth math** due to small expert matrix operations (2048x7168). Based on issue #19480 where Qwen3-Coder-Next (80B/3B active) achieved 7.74 tok/s on DDR5-5600 when BW math predicted 20-30+. On our slower DDR3 with higher latency, the penalty is proportionally worse.

### Confidence Levels for Estimates

| Category | Confidence | Reason |
|----------|-----------|--------|
| Dense models | **Medium** (+/- 25%) | BW scaling reliable; AVX penalty estimated |
| MoE models | **Low-Medium** (+/- 35%) | CPU MoE behavior poorly documented |
| Prompt prefill | **Low** (+/- 40%) | GEMM on AVX-only is model-dependent |

**Sources:**
- Gold 6312U: https://ahelpme.com/ai/llm-inference-benchmarks-with-llamacpp-and-xeon-gold-6312u-cpu/
- MoE issue: https://github.com/ggml-org/llama.cpp/issues/19480
- CPU scaling: https://llmhardware.io/guides/cpu-only-llm-inference
- InsiderLLM: https://insiderllm.com/guides/cpu-only-llms-what-actually-works/

---

## 4. Prompt Eval (Prefill) Speed

### Why Prefill is Disproportionately Slow

Prompt processing uses GEMM (compute-bound, batch_size = prompt length). Unlike token generation (GEMV, BW-bound), GEMM scales with FLOPS capacity. Sandy Bridge E5-2620 v1 has:
- Theoretical peak: 6 cores × 2.0 GHz × 8 FLOP/cycle (AVX 256-bit) = **96 GFLOPS**
- Without FMA: effective ~48 GFLOPS for most operations
- With Q4_K_M dequant overhead: ~10-20% of peak achievable

### Estimated Prefill Speed (Single Socket)

| Model | 1K tokens | 8K tokens | 32K tokens |
|-------|-----------|-----------|------------|
| Qwen2.5-Coder 3B | 30-50 tok/s | 15-25 tok/s | 8-12 tok/s |
| Qwen2.5-Coder 7B | 8-15 tok/s | 5-10 tok/s | 3-6 tok/s |
| Qwen2.5-Coder 14B | 4-7 tok/s | 2-5 tok/s | 1.5-3 tok/s |
| Qwen2.5-Coder 32B | 1.5-3 tok/s | 1-2 tok/s | 0.5-1 tok/s |
| Qwen3 8B | 8-14 tok/s | 5-9 tok/s | 3-5 tok/s |

**Time to first token for 8K prompt on 7B Q4:** ~1,143 seconds (19 minutes) at 7 tok/s prefill.

**This is the single biggest usability issue on this hardware.**

### Recommendations for Prefill
- Minimize context: `--ctx-size 4096` or lower
- Use `--batch-size 128` (smaller batches reduce compute waste)
- Flash attention: OFF on CPU (adds overhead; no benefit)
- For RAG: re-rank and truncate to 2K-4K tokens max
- Pre-process documents offline and store embeddings, not raw text

---

## 5. KV Cache and Context Impact

### 5.1 KV Cache Size Estimates (f16)

| Model | KV per token | 4K ctx | 8K ctx | 32K ctx | 128K ctx |
|-------|-------------|--------|--------|---------|----------|
| 3B | ~96 KB | 0.38 GB | 0.75 GB | 3 GB | 12 GB |
| 7B | ~224 KB | 0.88 GB | 1.75 GB | 7 GB | 28 GB |
| 14B | ~320 KB | 1.25 GB | 2.5 GB | 10 GB | 40 GB |
| 32B | ~512 KB | 2.0 GB | 4.0 GB | 16 GB | 64 GB |
| 30B MoE | ~496 KB | 1.94 GB | 3.88 GB | 15.5 GB | 62 GB |

### 5.2 Context Impact on Generation Speed

At short context (<4K), KV cache is negligible. As context grows:

| Context | KV (7B) | Total data/token | Speed loss vs 4K |
|---------|---------|-----------------|-----------------|
| 4K | 0.88 GB | ~5.6 GB | baseline |
| 8K | 1.75 GB | ~6.5 GB | -14% |
| 32K | 7 GB | ~11.7 GB | -52% |
| 128K | 28 GB | ~32.7 GB | -83% |

At 128K context, 7B Q4 on single socket drops to ~0.8 tok/s.

### 5.3 KV Cache Compression

| Cache type | Size vs f16 | Speed impact (CPU TG) | Speed impact (CPU PP) |
|------------|-------------|----------------------|----------------------|
| f16 (default) | 1x | baseline | baseline |
| **q8_0** | **0.5x** | +5-10% | -1-2% (near-lossless) |
| q4_0 | 0.25x | +10-15% | **-35% to -92%** at long ctx |

**Critical finding:** q4_0 KV cache is dangerous on CPU. DGX Spark benchmarks (2026) showed 92.5% PP collapse at 64K with q4_0 vs f16. On Sandy Bridge without F16C, the dequant overhead is even worse.

**Recommendation:** Use q8_0 KV cache for any context >8K. Never use q4_0 on this CPU.

**Sources:**
- DGX Spark KV cache: https://wiki.charleschen.ai/Review/Research/kv-cache-q8_0-llamacpp-spark
- PR #2969: https://github.com/ggerganov/llama.cpp/pull/2969

---

## 6. Technical Recommendations for Ollama

### 6.1 Thread Configuration

**OLLAMA_NUM_THREADS = 6** (physical cores of one socket). SMT/hyperthreading **degrades** memory-bound workloads.

From Ollama PR #6264 and #7322: "one thread per physical core is optimal for CPU inference." On dual-socket, using threads from the second socket adds QPI penalty. Never exceed 12 (total physical cores).

**OLLAMA_NUM_PARALLEL = 1.** Multiple parallel requests destroy single-request throughput on CPU.

### 6.2 Flash Attention: OFF

Flash attention in llama.cpp is optimized for CUDA. On CPU it adds overhead with no benefit. Leave disabled (`--flash-attn 0`).

### 6.3 Batch Size

Start with `--batch-size 128`, benchmark against 64 and 256. Default 512-2048 targets GPU; on CPU it causes excessive allocation.

### 6.4 Optimal Ollama Configuration

```bash
# Environment variables
export OLLAMA_NUM_THREADS=6
export OLLAMA_MLOCK=1
export OLLAMA_NUM_PARALLEL=1

# NUMA binding (single socket)
numactl --cpunodebind=0 --membind=0 ollama serve

# Modelfile for each model
FROM qwen2.5-coder:7b-base-q4_K_M
PARAMETER num_thread 6
PARAMETER batch_size 128
PARAMETER num_ctx 4096
```

### 6.5 OS-Level Tuning

```bash
# Disable NUMA balancing (reduces page migration)
echo 0 | sudo tee /proc/sys/kernel/numa_balancing

# Performance governor
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

# Reduce swappiness (keep model in RAM)
echo 10 | sudo tee /proc/sys/vm/swappiness

# Lock model in RAM
export OLLAMA_MLOCK=1
```

### 6.6 Alternative: llama.cpp Direct (for ~10-20% more speed)

```bash
./llama-cli \
  -m qwen2.5-coder-7b-q4_k_m.gguf \
  -t 6 \
  -c 4096 \
  -b 128 \
  --mlock \
  --numa isolate \
  --cache-type-k q8_0 \
  --cache-type-v q8_0
```

Ollama adds ~5-15% overhead vs raw llama.cpp per the DeployBase comparison.

**Sources:**
- Ollama thread selection: PR #6264 (https://github.com/ollama/ollama/pull/6264)
- NUMA refinement: PR #7322 (https://github.com/ollama/ollama/pull/7322)
- OLLAMA_NUM_THREADS env: PR #15421 (https://github.com/ollama/ollama/pull/15421)
- CPU tuning guide: https://github.com/jameschrisa/Ollama_Tuning_Guide
- llama.cpp vs Ollama: https://deploybase.ai/articles/llama-cpp-vs-ollama

---

## 7. Overall Assessment

### Summary

| Metric | Value | Usability |
|--------|-------|-----------|
| 7B Q4 gen (single socket) | 2.8 tok/s | Marginal for chat; OK for batch |
| 7B Q4 gen (interleaved) | 4.2 tok/s | Barely usable for interactive |
| 3B Q4 gen (single socket) | 5.3 tok/s | Acceptable for simple Q&A |
| 14B+ gen | <1.5 tok/s | Impractical |
| 8K prompt prefill (7B) | 19 min TTFT | Unusable for chat |

### Key Takeaways

1. **Usable only for 3B models and marginal for 7B** with very short contexts.
2. **Prompt processing is the dominant bottleneck**, not generation.
3. **Single-socket NUMA binding is mandatory** — using both sockets degrades performance.
4. **Never exceed 4K context** unless you can tolerate 2-3x slowdowns.
5. **AVX2/FMA absence is a secondary issue** — DDR3-1333 bandwidth is the primary bottleneck.
6. **MoE models do NOT deliver their theoretical advantage** on this hardware.

### Explicit Gaps (Unverified)

- No direct Ollama benchmark on E5-2620 v1 was found anywhere. All estimates are scaled from architecturally similar systems (E5-2680, E5-2665).
- AVX vs AVX2 gap in current Q4_K_M path is estimated from 2023-era vec_dot benchmarks.
- DDR3 latency impact on MoE small-matrix efficiency is extrapolated, not measured.
- Ollama backend auto-detection behavior on this specific CPU has not been confirmed in published tests.
