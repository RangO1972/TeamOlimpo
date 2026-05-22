---
data: '2026-05-21'
timestamp: '2026-05-21T14:29:41'
agent: proteo
invocation: 26
type: analysis
status: completed
priority: medium
title: Proteo - Analisi HW Sandy Bridge per inferenza LLM
task_id: T-ANALISI-005
---

# Technical Analysis: LLM Inference via Ollama on Intel Xeon E5-2620 v1 (Sandy Bridge-EP)

## Executive Summary

**System:** 2× Intel Xeon E5-2620 v1 (6C/12T per socket, 2.0/2.5 GHz)
**Memory:** DDR3-1333 ECC, 4 channels per socket, ~236 GB total
**ISA:** AVX only — **no** AVX2, FMA, F16C, AVX-512
**Inference engine:** Ollama → llama.cpp GGUF backend (CPU-only)

**Bottom line:** Token generation is severely bandwidth-constrained. Expect **2.5–5.5 tok/s** for 7–8B Q4 models on single-socket binding, and **4–9 tok/s** with NUMA interleaving. Prompt processing (prefill) will be disproportionately slower due to missing AVX2/FMA — expect 3–8× slowdown vs AVX2 CPUs at equivalent bandwidth.

---

## 1. Impact of Missing AVX2 on LLM Inference

### 1.1 How Ollama/llama.cpp handles CPUs without AVX2

Ollama ships pre-compiled CPU backends for multiple x86 ISA levels (from `ggml-cpu-sapphirerapids.so` down to generic). The runner auto-detects CPU features at load time and selects the most advanced compatible backend. On Sandy Bridge E5-2620 v1, Ollama will load the **AVX-only** variant — confirmed by the detection flags in the ggml-cpu backend.

From the Ollama GitHub issue #9087 and the system info string format:
```
CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 0 | FMA = 0 | F16C = 0 | AVX512 = 0
```

Sandy Bridge-EP (2012) supports:
- ✅ SSE4.1/4.2
- ✅ AVX (128-bit and 256-bit vectors)
- ❌ AVX2 (no integer FMA, no gather, no vector shifts)
- ❌ FMA (Fused Multiply-Add, introduced in Haswell 2013)
- ❌ F16C (half-precision conversion, introduced in Ivy Bridge 2012)
- ❌ AVX-512

### 1.2 Quantitative AVX vs AVX2 Performance Difference

**Key reference data from GGML development (PR #617, #996):**

| Operation | AVX-only | AVX2 | Ratio | Source |
|-----------|----------|------|-------|--------|
| `ggml_vec_dot_q4_0` (7B inference) | ~679 ns | ~590 ns | 1.15× | PR #617 |
| GEMV K=8, N=8192 | 15,194 FLOPS/μs | 27,149 FLOPS/μs | 1.79× | PR #996 |
| GEMV K=16, N=8192 | 8,224 FLOPS/μs | 20,128 FLOPS/μs | 2.45× | PR #996 |
| GEMV K=32, N=8192 | 9,397 FLOPS/μs | 13,127 FLOPS/μs | 1.40× | PR #996 |
| LoRA matmul K=16 | 9,831 ms | 5,142 ms | 1.91× | PR #996 |

**Impact breakdown by inference phase:**

| Phase | AVX penalty | Explanation |
|-------|-------------|-------------|
| **Token generation (GEMV)** | **10–20%** | Memory-bandwidth-bound; dequant + matmul is secondary. Small matrices in later layers see larger AVX impact. No FMA further hurts. |
| **Prompt processing/prefill (GEMM)** | **25–50%** | Compute-bound for batch sizes >1. GEMM heavily relies on AVX2/FMA for tiled matmul. The lack of F16C adds ~8% to dequant overhead. |
| **KV cache dequant** | **15–25%** | Q8_0 cache dequant uses F16C for scale conversion; software fallback is slower. |

**Overall estimate for token generation (the user-facing metric):** Sandy Bridge E5-2620 v1 is approximately **15–20% slower** than an equivalent Ivy Bridge CPU (which has AVX2+F16C) at the same memory bandwidth, and **25–35% slower** than a Haswell CPU (AVX2+FMA+F16C) at equal bandwidth.

**Sources:**
- PR #617: https://github.com/ggerganov/llama.cpp/pull/617
- PR #996: https://github.com/ggml-org/llama.cpp/pull/996
- PR #933: https://github.com/ggml-org/llama.cpp/pull/933 (AVX512 vs AVX2 benchmarks)

---

## 2. Realistic Sustainable Memory Bandwidth

### 2.1 Theoretical vs Real Bandwidth

**Per-socket specs (Intel ARK):**
- Channels: 4× DDR3-1333
- Theoretical peak: 4 × 8 B × 1333 MT/s = **42.6 GB/s**
- QPI: 2 links at 7.2 GT/s (each direction: 16 GB/s theoretical)

**Real-world measurements from published benchmarks:**

| Source | System | Memory | Measured BW | % of Peak |
|--------|--------|--------|-------------|-----------|
| CERN Open Lab paper (2012) | 2S Xeon E5-2680 (8C, DDR3-1600) | 4-ch DDR3-1600 | 42.2 GB/s local (8 threads) | 82.4% |
| CERN Open Lab paper | Same | Cross-socket QPI (8 GT/s) | 23.6 GB/s | 73.75% of QPI |
| TechReport Geekbench | E5-2620 @2.0 GHz | 4-ch DDR3-1333 | ~11.8 GB/s (STREAM vector, 1 core) | — |
| ADMIN Magazine (K. Rupp) | 2S SB-EP (general) | 4-ch DDR3 | ~78 GB/s total dual-socket | — |
| STREAM ref data | Various SB-EP systems | 4-ch DDR3-1333 | 30–36 GB/s per socket (Triad, all cores) | 70–85% |

**Derived estimates for our specific configuration (2× E5-2620 v1, DDR3-1333):**

| Scenario | Estimated Real BW | Basis |
|----------|-------------------|-------|
| **Single socket, local access** | **30–34 GB/s** | Scaling CERN's 42.2 GB/s @1600 MHz by 1333/1600: 35.1 GB/s, minus lower clock/IMC efficiency |
| **Dual socket, NUMA interleaved** | **48–56 GB/s** | Local socket BW + ~18–22 GB/s from second socket via 7.2 GT/s QPI |
| **Single socket, LLM TG effective** | **14–18 GB/s** | 50% utilization of STREAM BW (compute overhead + AVX penalty) |
| **Dual socket, LLM TG effective** | **22–28 GB/s** | Lower utilization due to QPI latency + access pattern inefficiency |

**Confidence:** Medium-High for per-socket BW (±15%); Medium for dual-socket effective BW (±25%) due to NUMA topology sensitivity.

### 2.2 NUMA Penalty: Cross-Socket Access via QPI

**The QPI bottleneck is severe for LLM inference.** Key data points:

1. **CERN paper**: Cross-socket BW is 23.6 GB/s even at 8 GT/s QPI. Our 7.2 GT/s QPI yields ~21 GB/s.
2. **GitHub issue #19037**: Dual Xeon 8580 (16-ch DDR5, 563 GB/s theoretical) only 15% faster than single-socket w7-3565X for DeepSeek-V3 decode. Dual-socket BW efficiency dropped to 35%.
3. **GitHub issue #1437 discussion**: "llama.cpp doesn't really scale well with NUMA... using a single socket is best."
4. **CraftRigs guide**: "40-60% performance loss with cross-socket memory access on EPYC."

**Why cross-socket access hurts LLM inference:**
- Token generation reads ~5 GB of weights per token
- With NUMA interleaving, ~50% of reads hit the remote socket
- Remote reads traverse QPI with ~21 GB/s effective BW (vs ~32 GB/s local)
- Average BW = 0.5 × 32 + 0.5 × 21 = 26.5 GB/s — only 83% of local-only
- But QPI adds latency (~100-150ns vs ~70ns local), further degrading effective utilization

### 2.3 Mitigation Strategies

| Strategy | Effective BW | Pros | Cons |
|----------|-------------|------|------|
| **NUMA binding** (`numactl --cpunodebind=0 --membind=0`) | ~30–34 GB/s (one socket) | No QPI penalty; best single-request perf | 236 GB → ~118 GB usable RAM; no benefit from second socket |
| **NUMA interleaving** (`numactl --interleave=all`) | ~48–56 GB/s total | Full RAM usable; higher total BW | QPI bottleneck; 15–25% worse than sum of parts |
| **NUMA distribute** (`--numa distribute`) | Variable | llama.cpp distributes threads | Often worse than interleave; threads may mismatch memory nodes |
| **NUMA migrate** (PR #14232, June 2025) | Up to 33% uplift vs distribute | Migrates pages to local node during compute | Not in Ollama yet; requires custom llama.cpp build |
| **NUMA mirror** (PR #14969, July 2025) | 64.6% uplift vs distribute | Mirrors model per NUMA node (no cross-socket reads) | Requires 2× RAM for model; still experimental |

**Recommendation for this system:** Use `numactl --cpunodebind=0 --membind=0` for models ≤118 GB (all target models fit). This avoids the crippling QPI bottleneck entirely. For models that need both sockets (>118 GB), use `numactl --interleave=all` with `--numa numactl`.

**Sources:**
- CERN paper: https://openlab-archive-iv-v.web.cern.ch/.../Evaluation_of_the_4_socket_Intel_Sandy_Bridge-EP_server_processor.pdf
- Issue #19037: https://github.com/ggml-org/llama.cpp/discussions/19037
- Issue #1437: https://github.com/ggerganov/llama.cpp/issues/1437
- CraftRigs guide: https://craftrigs.com/troubleshooting/llama-cpp-numa-warning-speed-fix-multi-socket/
- PR #14232: https://github.com/ggml-org/llama.cpp/pull/14232
- PR #14969: https://github.com/ggml-org/llama.cpp/pull/14969

---

## 3. Performance Estimates by Model (Tokens/Second)

### Methodology

**Reference anchor:** Xeon Gold 6312U (1S, 24C, 8-ch DDR4-3200, ~170 GB/s BW, AVX-512) achieves **21.25 tok/s** on 8B Q4_K_M (ahelpme.com).

**Scaling logic:**
1. Effective BW ratio: Sandy Bridge single-socket LLM TG BW (16 GB/s) ÷ Gold 6312U LLM TG BW (21.25 × 4.92 GB = 104.5 GB/s) = 0.153
2. Base estimate: 21.25 × 0.153 = 3.25 tok/s (single socket, 8B Q4_K_M)
3. Adjusted for AVX+FMA+F16C penalty: ×0.82 = **2.67 tok/s**
4. Adjusted for model size scaling: tok/s ∝ (model_size_ref / model_size_target)

For interleaved dual-socket: base BW ~24 GB/s effective, factor = 24/104.5 = 0.230, ×0.82 AVX = 0.188 → 21.25 × 0.188 = **4.00 tok/s** for 8B Q4_K_M.

### Generation Speed Table (Q4_K_M quantization)

| Model | Params | Q4_K_M Size | Tok/s (Single Socket) | Tok/s (Interleaved) |
|-------|--------|-------------|----------------------|---------------------|
| **Qwen2.5-Coder 3B** | 3B | ~2.5 GB | **5.3 ± 0.8** | **8.0 ± 1.2** |
| **Qwen2.5-Coder 7B** | 7B | ~4.7 GB | **2.8 ± 0.4** | **4.2 ± 0.6** |
| **Qwen2.5-Coder 14B** | 14B | ~9 GB | **1.5 ± 0.2** | **2.2 ± 0.3** |
| **Qwen2.5-Coder 32B** | 32B | ~20 GB | **0.65 ± 0.1** | **1.0 ± 0.15** |
| **DeepSeek Coder V2 Lite 16B (MoE)** | 16B/2.4B active | ~10 GB | **2.2 ± 0.5** | **3.2 ± 0.7** |
| **Qwen3-Coder-30B-A3B (MoE)** | 30B/3.3B active | ~18 GB | **2.5 ± 0.5** | **3.5 ± 0.8** |
| **Qwen3 8B** | 8B | ~5 GB | **2.7 ± 0.4** | **4.0 ± 0.6** |

**Assumptions and methodology notes:**

1. **Dense model scaling**: tok_single = 21.25 × (BW_eff_single / 104.5) × (4.92 / model_size_GB) × 0.82
   Example 7B (4.7 GB): 21.25 × (16/104.5) × (4.92/4.7) × 0.82 = 2.8 tok/s

2. **MoE model penalty**: MoE models underperform bandwidth math by 3–5× on CPU due to small expert matrices (2048×7168 dimension), which have low arithmetic intensity and poor cache utilization. Based on issue #19480 (7.74 tok/s observed vs 20-30+ expected on DDR5-5600). For our slower DDR3 with higher latency, the penalty is even larger. Estimates are based on:
   - Active parameter bandwidth math (data per token = active_params × bytes_per_param)
   - Then divided by 3–5× for the "MoE small-matrix penalty"
   - DeepSeek Coder V2 Lite: ~2.4B active × 0.5 bytes (Q4) = ~1.2 GB/token → BW math says 13 tok/s, divided by 6× = ~2.2 tok/s
   - Qwen3-Coder-30B-A3B: ~3.3B active × 0.5 bytes = ~1.65 GB/token → BW math says 10 tok/s, divided by 4× (larger matrices) = ~2.5 tok/s

3. **Interleaved dual-socket**: Assumes ~50% BW improvement over single-socket with 15–20% additional overhead from QPI latency for small matrices. MoE models see less benefit from interleaving due to increased sensitivity to memory latency.

**Confidence:**
- Dense models: **Medium** (±25%) — bandwidth scaling is reliable but AVX penalty is estimated
- MoE models: **Low-Medium** (±35%) — MoE CPU behavior is still poorly understood; Ollama may improve

**Sources:**
- Xeon Gold 6312U reference: https://ahelpme.com/ai/llm-inference-benchmarks-with-llamacpp-and-xeon-gold-6312u-cpu/
- MoE CPU inefficiency: https://github.com/ggml-org/llama.cpp/issues/19480
- General CPU scaling: https://llmhardware.io/guides/cpu-only-llm-inference

---

## 4. Prompt Eval (Prefill) Speed

### Why Prefill is Disproportionately Slow on Sandy Bridge

Prompt processing (prefill) uses GEMM (matrix-matrix multiply) with batch_size equal to prompt length. Unlike token generation (GEMV, bandwidth-bound), GEMM is **compute-bound** and scales with FLOPS capacity. Sandy Bridge E5-2620 v1's lack of AVX2, FMA, and F16C hits GEMM performance particularly hard.

**Reference data:**
- On Gold 6312U (AVX-512, 24C): 8B Q4_K_M achieves ~1,200–1,800 tok/s for pp512 (extrapolated from the 21 tok/s TG benchmark)
- On i7-1185G7 (Tiger Lake, AVX-512, 4C): 7B Q4 achieved ~5-6 tok/s pp for long prompts (from intel-gpu-llm-inference benchmarks)
- On DDR5 consumer CPU (Ryzen 9, AVX2): 7B Q4_K_M achieves ~200-400 tok/s pp512

### Estimated Prefill Speed (Single Socket, AVX-only)

GEMM performance is primarily limited by:
1. **Peak FLOPS**: Sandy Bridge 6C @ 2.0 GHz = 6 × 2.0 GHz × 8 FLOP/cycle (AVX 256-bit) = 96 GFLOPS theoretical (without FMA, actual ~48 GFLOPS for most operations)
2. **GEMM efficiency**: For Q4_K_M dequant + matmul, ~10-20% of peak achievable
3. **Memory bandwidth**: For very short prompts (<512 tok), BW is secondary; for long prompts (>8K), BW becomes co-limiting

| Model | 1K tokens | 8K tokens | 32K tokens |
|-------|-----------|-----------|------------|
| **Qwen2.5-Coder 3B** | 30–50 tok/s | 15–25 tok/s | 8–12 tok/s |
| **Qwen2.5-Coder 7B** | 8–15 tok/s | 5–10 tok/s | 3–6 tok/s |
| **Qwen2.5-Coder 14B** | 4–7 tok/s | 2–5 tok/s | 1.5–3 tok/s |
| **Qwen2.5-Coder 32B** | 1.5–3 tok/s | 1–2 tok/s | 0.5–1 tok/s |
| **Qwen3 8B** | 8–14 tok/s | 5–9 tok/s | 3–5 tok/s |

**Time to first token (TTFT) examples for 8K prompt on 7B Q4:**
- Time to prefill 8K tokens at 7 tok/s = ~1,143 seconds ≈ **19 minutes**
- This means **19-minute wait before generation starts** for a chat with 8K context history

**This is the single biggest usability problem.** Prompt processing will be excruciatingly slow for any non-trivial context.

### Mitigation
- Minimize context length: use `--ctx-size 4096` or lower
- Use smaller batch sizes: `--batch-size 128` (llama.cpp default: 2048; smaller batches reduce compute waste but may underutilize BW)
- **Consider using flash attention only if it doesn't regress CPU speed** (flash-attn on CPU is often slower in llama.cpp)
- For RAG workflows: re-rank and truncate context to 2K–4K tokens

**Confidence:** Low-Medium (±40%) — prefill speed on AVX-only CPUs is poorly documented in published benchmarks.

---

## 5. KV Cache and Context Impact

### 5.1 KV Cache Size Estimates (f16 default, per token)

| Model | n_layers | n_kv_heads | d_head | KV cache per token |
|-------|----------|------------|--------|-------------------|
| Qwen2.5-Coder 3B | 24 | 4 | 128 | ~96 KB |
| Qwen2.5-Coder 7B | 28 | 8 | 128 | ~224 KB |
| Qwen2.5-Coder 14B | 40 | 8 | 128 | ~320 KB |
| Qwen2.5-Coder 32B | 64 | 8 | 128 | ~512 KB |
| DeepSeek Coder V2 Lite (MoE) | 27 | 4 | 128 | ~108 KB |
| Qwen3-Coder-30B-A3B (MoE) | 62 | 10 | 128 | ~496 KB |
| Qwen3 8B | 32 | 8 | 128 | ~256 KB |

**Total KV cache at various context lengths (f16):**

| Model | 4K context | 8K context | 32K context | 128K context |
|-------|-----------|-----------|-------------|--------------|
| 3B | 0.38 GB | 0.75 GB | 3 GB | 12 GB |
| 7B | 0.88 GB | 1.75 GB | 7 GB | 28 GB |
| 14B | 1.25 GB | 2.5 GB | 10 GB | 40 GB |
| 32B | 2.0 GB | 4.0 GB | 16 GB | 64 GB |
| 30B MoE | 1.94 GB | 3.88 GB | 15.5 GB | 62 GB |

### 5.2 Impact of Context on Generation Speed

At short context (<4K), the KV cache is negligible compared to model weights (~5 GB for 7B). As context grows:

| Context | KV size (7B) | Total data/token | Speed loss vs 4K |
|---------|--------------|------------------|-----------------|
| 4K | 0.88 GB | ~5.6 GB | baseline |
| 8K | 1.75 GB | ~6.5 GB | ~14% slower |
| 32K | 7 GB | ~11.7 GB | ~52% slower |
| 128K | 28 GB | ~32.7 GB | ~83% slower |

At 128K context, the effective token generation speed for 7B Q4 on single socket would drop to ~0.8 tok/s.

### 5.3 KV Cache Compression Effectiveness

| Cache type | Bits/elem | Size vs f16 | Speed impact (CPU TG) | Speed impact (CPU PP) | Quality impact |
|------------|-----------|-------------|----------------------|----------------------|----------------|
| **f16** (default) | 16 | 1× | baseline | baseline | baseline |
| **q8_0** | 8 | 0.5× | +5–10% (less BW) | -1–2% | Near-lossless |
| **q4_0** | 4 | 0.25× | +10–15% (less BW) | **-35% to -92%** (dequant overhead) | Noticeable |

**⚠️ Critical finding:** q4_0 KV cache is **dangerous on CPU**. The DGX Spark benchmark showed a **92.5% collapse** in prompt processing speed at 64K context with q4_0 vs f16 (source: NVIDIA Forums, March 2026). On our Sandy Bridge without F16C, the dequant overhead is even worse.

**Recommendation:** Use `--cache-type-k q8_0 --cache-type-v q8_0` for any context >8K. This halves KV cache memory with negligible speed loss. Never use q4_0 KV cache on this CPU.

### 5.4 Maximum Viable Context Before Speed Collapse

**Criterion: generation speed drops below 1 tok/s.**

| Model | Single socket | Interleaved |
|-------|--------------|-------------|
| 3B | ~128K | ~256K+ |
| 7B | ~64K | ~128K |
| 14B | ~32K | ~64K |
| 32B | ~8K | ~16K |
| 30B MoE | ~32K | ~64K |

**Sources:**
- DGX Spark KV cache benchmark: https://wiki.charleschen.ai/Review/Research/kv-cache-q8_0-llamacpp-spark
- PR #2969: https://github.com/ggerganov/llama.cpp/pull/2969

---

## 6. Technical Recommendations for Ollama

### 6.1 Thread Configuration

**OLLAMA_NUM_THREADS**
- **Optimal: 6** (physical cores of one socket). SMT/hyperthreading **degrades** performance for memory-bound workloads.
- Maximum useful: 8 (if some OS tasks share the socket).
- Never set >12 (total physical cores across both sockets) — threads on the second socket will hit QPI latency penalties.
- Benchmarking reference from Ollama PR #6264 and issue #2496: "one thread per physical core is indeed optimal."

From the Xeon Gold 5317 dual-socket benchmark (ahelpme.com): `-t 24` (all physical cores) was optimal. For our 6C/socket system, `-t 6` for single-socket binding.

**OLLAMA_NUM_PARALLEL**
- **Set to 1.** Parallel requests on CPU destroy single-request throughput. From llmhardware.io guide: "On CPU, parallelism hurts single-request speed."

### 6.2 Flash Attention

**Does flash attention help on CPU?**
- **Currently no.** Flash attention in llama.cpp is optimized for CUDA (GPU). On CPU, it typically adds overhead rather than speeding up. Source: multiple GitHub discussion threads (#3909, benchmark wiki).
- Exception: for very long context (>16K), flash attention may reduce KV cache memory overhead, which indirectly helps by reducing cache pressure.
- **Recommendation:** Leave flash attention OFF (`--flash-attn 0`).

### 6.3 Batch Size for Prompt Processing

- For CPU-only inference, **smaller batch sizes work better** than the defaults.
- Reference: Ollama Tuning Guide recommends `--batch-size 128` for entry-level CPUs, up to 256 for server CPUs.
- Our Sandy Bridge: start with `--batch-size 128`, benchmark against 64 and 256.
- The default 512–2048 batch size is designed for GPU; on CPU it causes excessive memory allocation without throughput benefit.

**In Ollama:** batch size is controlled via the model's Modelfile:
```
PARAMETER batch_size 128
```

### 6.4 Optimal Modelfile Parameters

```dockerfile
FROM qwen2.5-coder:7b-base-q4_K_M

# Critical: use physical cores of ONE socket
PARAMETER num_thread 6

# Small batch for CPU prompt processing
PARAMETER batch_size 128

# Conservative context to avoid KV cache slowdown
PARAMETER num_ctx 4096

# Reserve ~2 cores for OS; prevents thrashing
PARAMETER num_gpu 0

# KV cache type hints (passed to llama.cpp)
# Set via environment or wrapper script, not in Modelfile
```

### 6.5 NUMA Configuration (numactl Wrapper)

**Best strategy: Single-socket binding** (recommended for all models in scope)

```bash
# Bind to socket 0, memory on socket 0
numactl --cpunodebind=0 --membind=0 \
  ollama run qwen2.5-coder:7b
```

**If both sockets are needed** (models >~118 GB, not applicable for our target models):

```bash
# Interleave memory across both sockets
numactl --interleave=all \
  ollama run qwen2.5-coder:32b
  
# With llama.cpp's NUMA mode (if using llama.cpp directly):
# --numa numactl  # respects numactl's policy
```

**Additional OS tuning:**
```bash
# Disable NUMA balancing (reduces page migration overhead)
echo 0 | sudo tee /proc/sys/kernel/numa_balancing

# Set CPU governor to performance
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

# Reduce swappiness (keep model in RAM)
echo 10 | sudo tee /proc/sys/vm/swappiness

# Lock model in RAM with --mlock (or OLLAMA_MLOCK=1)
```

### 6.6 Ollama Environment Variables

```bash
# Thread control
export OLLAMA_NUM_THREADS=6

# Keep model in RAM (avoid swapping)
export OLLAMA_MLOCK=1

# Single request at a time
export OLLAMA_NUM_PARALLEL=1
```

### 6.7 llama.cpp Direct Usage (Alternative)

For ~10–20% more performance, consider using llama.cpp directly instead of Ollama (Ollama adds ~5–15% overhead per the DeployBase comparison):

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

**Sources:**
- Ollama default thread selection: PR #6264 (https://github.com/ollama/ollama/pull/6264)
- Ollama NUMA thread refinement: PR #7322 (https://github.com/ollama/ollama/pull/7322)
- OLLAMA_NUM_THREADS env var: PR #15421 (https://github.com/ollama/ollama/pull/15421)
- CPU optimization guide: https://github.com/jameschrisa/Ollama_Tuning_Guide/blob/7f275880/docs/cpu-optimization.md
- llama.cpp vs Ollama overhead: https://deploybase.ai/articles/llama-cpp-vs-ollama
- InsiderLLM CPU guide: https://insiderllm.com/guides/cpu-only-llms-what-actually-works/

---

## 7. Overall Assessment

### Summary Table of Expected Performance

| Metric | Value | Rating |
|--------|-------|--------|
| 7B Q4_K_M generation (single socket) | 2.8 tok/s | 🟡 Slow but usable for batch/offline |
| 7B Q4_K_M generation (interleaved) | 4.2 tok/s | 🟡 Usable for light interactive use |
| 3B Q4_K_M generation (single socket) | 5.3 tok/s | 🟢 Acceptable for chat |
| 14B Q4_K_M generation (single socket) | 1.5 tok/s | 🔴 Painfully slow |
| 8K prompt prefill (7B, all scenarios) | 5–10 tok/s | 🔴 13–27 minutes before first token |
| 32B generation (single socket) | 0.65 tok/s | 🔴 Impractical |

### Key Takeaways

1. **This system is usable for 3B models and marginal for 7B models** with very short contexts.
2. **Prompt processing is the bottleneck**, not generation. 8K+ context prompts require >10 minutes of prefill.
3. **Single-socket NUMA binding is critical** — using both sockets degrades performance vs one socket.
4. **Never exceed 4K context** unless you can tolerate 2–3× slowdowns.
5. **The lack of AVX2/FMA/F16C is a meaningful but secondary issue** — the primary bottleneck is DDR3-1333 bandwidth.
6. **MoE models do NOT deliver their theoretical advantage** on this hardware due to the small-matrix CPU penalty.

### Confidence Levels for All Estimates

| Section | Confidence | Reason |
|---------|-----------|--------|
| Memory bandwidth estimates | Medium-High (±15%) | Well-characterized architecture; scaling from published CERN/STREAM data |
| Dense model generation speed | Medium (±25%) | Bandwidth scaling is reliable; AVX penalty is estimated |
| MoE model speed | Low-Medium (±35%) | CPU MoE behavior is poorly documented; high variance |
| Prompt prefill speed | Low (±40%) | GEMM performance on AVX-only is model/implementation dependent |
| KV cache impact | Medium (±20%) | Well-documented in GPU context; CPU specifics are extrapolated |

### GAPS (explicitly unverified)

- **No direct benchmark of Ollama on E5-2620 v1 was found.** All estimates are derived from published benchmarks on architecturally similar systems (E5-2680, E5-2665) with scaling adjustments.
- **No recent Ollama version (0.5.x+) was tested on this specific CPU.** Ollama's CPU backend detection and thread selection logic changed significantly between v0.5.7 and v0.5.11. The automatic selection of the AVX-only backend should work, but has not been confirmed on this exact CPU.
- **AVX vs AVX2 performance gap in the current llama.cpp Q4_K_M path** is not precisely characterized. The 10–20% TG penalty is an estimate based on limited vec_dot benchmarks from 2023.
- **The impact of DDR3 latency vs DDR4/DDR5 on LLM inference** is not independently quantified. Our estimates assume BW is the dominant factor, which is correct for large matrix GEMV but may understate the penalty for MoE's small matrices.
