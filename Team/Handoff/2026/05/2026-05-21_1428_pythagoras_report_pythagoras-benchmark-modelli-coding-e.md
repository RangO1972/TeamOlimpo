---
data: '2026-05-21'
timestamp: '2026-05-21T14:28:16'
agent: pythagoras
invocation: 3
type: report
status: completed
priority: high
title: Pythagoras - Benchmark modelli coding e requisiti OpenCode
task_id: T-ANALISI-006
---

# Coding LLM Benchmarks & OpenCode Technical Requirements

**Date:** 2026-05-21  
**Agent:** Pythagoras (Academic Web Researcher)  
**Target hardware:** 2× Intel Xeon E5-2620 v1 (Sandy Bridge, 12C, DDR3-1333, no AVX2), 236 GB RAM, CPU-only via Ollama

---

## 1. OpenCode.ai — Technical Requirements for Local Models

### 1.1 Context Window Requirements
OpenCode requires a **minimum context window of 64K tokens** for reliable operation, per the official Ollama integration docs ([Ollama docs — OpenCode](https://docs.ollama.com/integrations/opencode)). Community guides recommend "at least 8K, 32K is even better" ([Sonu Sahani blog](https://sonusahani.com/blogs/opencode-ollama)).

### 1.2 Ollama Provider Configuration
The OpenCode config file (`~/.config/opencode/opencode.json` or `config.toml`) requires:

```json
{
  "provider": {
    "ollama": {
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://127.0.0.1:11434/v1"
      },
      "models": {
        "qwen3-coder:30b": {
          "name": "Qwen 3 Coder 30B"
        }
      }
    }
  }
}
```

**Critical setting for local models:** `tool_call_format = "json_fallback"` — tells OpenCode to parse JSON tool-call blocks from models that lack native function-calling support ([OpenCode Ollama adapter docs](https://opencode.gr.com/opencode-ollama.html)).

### 1.3 Known Issues with Local Models
- **Tool call failures:** Models may generate tool-call JSON but OpenCode doesn't execute it — often due to missing `tool_call_format` setting ([GitHub Issue #1034](https://github.com/anomalyco/opencode/issues/1034)).
- **Loop behavior:** Models with thinking mode (DeepSeek-R1 distill) may dump reasoning tokens into tool-call fields, breaking parsing.
- **Model compatibility:** Only models trained for structured output / function calling work reliably (Qwen series, Llama 3.1, Dolphin 3) ([OpenCode Ollama setup guide](https://sonusahani.com/blogs/opencode-ollama)).

### 1.4 OpenCode Recommended Model Tiers
From [opencode.gr.com](https://opencode.gr.com/opencode-ollama.html):

| Tier | Model class | Quant | RAM | Use case |
|------|-------------|-------|-----|----------|
| Small | 7B-8B class | Q4_K_M | 8-10 GB | Everyday edits, small refactors |
| Medium | 14B-20B class | Q4_K_M | 16-22 GB | Multi-file changes, plan mode |
| Large | 32B-70B class | Q4_K_M | 32-48 GB | Hard refactors, long contexts |

---

## 2. Coding LLM Benchmarks (2025-2026)

### 2.1 HumanEval & MBPP (CodeSOTA, April 2026)
Source: [CodeSOTA HumanEval/MBPP Leaderboard](https://www.codesota.com/llm/humaneval-mbpp)

| Model | HumanEval pass@1 | MBPP pass@1 | Source |
|-------|-----------------|-------------|--------|
| Qwen2.5-Coder 32B Instruct | **92.7%** | **90.2%** | CodeSOTA, Apr 2026 |
| DeepSeek-Coder-V2-Instruct (236B) | 90.2% | 89.4% | CodeSOTA, Apr 2026 |
| Gemma-3-27B | 87.8% | 74.4% | CodeSOTA, Mar 2025 |
| Codestral 25.01 (Mistral) | 85.3% | 91.2% (alt source) | CodeSOTA, Apr 2026 |
| Gemma 3 12B IT | 85.4% | 73.0% | CodeSOTA, Mar 2025 |
| DeepSeek-Coder-V2-Lite-Instruct (16B) | 81.1% | 68.8% (MBPP+) | DeepSeek-Coder-V2 README |
| Codestral 22B | 81.1% | 75.4% | CodeSOTA, Mar 2026 |
| DeepSeek-Coder-33B-Instruct | 79.3% | — | CodeSOTA, Apr 2026 |
| Gemma 3 4B IT | 71.3% | 63.2% | CodeSOTA, Mar 2025 |

### 2.2 Qwen-Specific Benchmarks

**Qwen2.5-Coder Series** ([Qwen Blog](https://qwenlm.github.io/blog/qwen2.5-coder-family/), [arXiv:2409.12186](https://arxiv.org/abs/2409.12186)):

| Model | HumanEval | MBPP | LiveCodeBench | FIM (avg) | SWE-bench Verified |
|-------|-----------|------|---------------|-----------|-------------------|
| Qwen2.5-Coder 7B | ~77%* | 83.5% | — | **57.5%** | — |
| Qwen2.5-Coder 14B | ~83%* | 85.0% | — | **59.9%** | — |
| Qwen2.5-Coder 32B | **92.7%** | **90.2%** | **47.8%** | **63.9%** | 28.7% (full) |

\* Estimated from Qwen blog charts; exact pass@1 varies by decoding strategy.

**Qwen3 8B** ([InsiderLLM Qwen Guide](https://insiderllm.com/guides/qwen-models-guide/)):
- HumanEval: **72.0%** (vs Llama 3.1 8B: 62.2%)
- MMLU: 73.8%
- MATH: 62.8%
- GSM8K: 84.2%
- Context: 32K (native) / 128K (YaRN)

**Qwen3-Coder-30B-A3B** (MoE: 30B total, 3B active):
- Release: July 31, 2025
- Context: 160K native, 256K-1M extensible
- Designed for agentic coding, function calling, tool use
- Supports function calling + structured output ([Qwen3-Coder GitHub](https://github.com/QwenLM/Qwen3-Coder))
- Pricing (API): $0.07/M input, $0.27/M output
- No standalone HumanEval found; benchmarks expected at ~90%+ HumanEval class

**Qwen3 30B A3B** (MoE: 30.5B total, 3B active):
- BFCL score: **69.1%** ([LLM Stats BFCL](https://llm-stats.com/benchmarks/bfcl))
- Coding accuracy: 94.0% (Benchable)
- Reasoning: 96.0%
- 100% reliability across 8 benchmarks ([Benchable](https://benchable.ai/models/qwen/qwen3-30b-a3b-04-28))

### 2.3 DeepSeek Model Benchmarks

**DeepSeek-Coder-V2-Lite-Instruct** (16B MoE, 2.4B active):
| Metric | Score | Source |
|--------|-------|--------|
| HumanEval | 81.1% | DeepWiki / DeepSeek-Coder-V2 README |
| MBPP+ | 68.8% | DeepWiki |
| LiveCodeBench | 24.3% | DeepWiki |
| HumanEval-FIM | 86.4% | DeepWiki (Base variant) |
| Context | 128K | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct) |

**DeepSeek-R1-Distill-Qwen-14B**:
- 14.8B dense parameters
- Release: Jan 20, 2025
- License: MIT
- Context: 128K
- HumanEval: ~83-87% (estimated from R1 family; exact 14B distill not independently verified on CodeSOTA)
- Note: DeepSeek-R1-0528 added tool calling support (May 28, 2025)
- **Known issue:** Tool calling with thinking mode produces `<think>` tokens in response, breaking structured parsing. Community workaround: custom Ollama templates needed ([GitHub Issue #10935](https://github.com/ollama/ollama/issues/10935), [MFDoom/deepseek-r1-tool-calling](https://registry.ollama.com/MFDoom/deepseek-r1-tool-calling))

### 2.4 Gemma 4 Benchmarks
Source: [Gemma 4 Benchmarks](https://gemma4-ai.com/blog/gemma4-benchmark), [Gemma 4 Technical Report](https://gemma4.online/benchmark)

| Model | Parameters | HumanEval | MBPP | LiveCodeBench v6 |
|-------|-----------|-----------|------|-----------------|
| Gemma 4 31B (dense) | 31B | **76.8%** | **82.4%** | 80.0% |
| Gemma 4 26B A4B (MoE) | 25.2B / 3.8B active | **73.2%** | **79.6%** | 77.1% |
| Gemma 4 E4B | 8B total / 4.5B effective | 62.1% | 68.9% | 52.0% |
| Gemma 4 E2B | 5.1B total / 2.3B effective | 54.3% | 59.3% | 44.0% |

Note: The user's table requests "Gemma 4 8B". The closest match is **Gemma 4 E4B** (~8B total, ~4.5B effective MoE). There is no Gemma 4 8B dense model — the Gemma 4 lineup has E2B, E4B, 26B MoE, and 31B dense.

### 2.5 Codestral Series Benchmarks
Source: [Analytics Vidhya comparison](https://www.analyticsvidhya.com/blog/2025/02/codestral-25-01-vs-qwen2-5-coder-32b-instruct), [CodeSOTA](https://www.codesota.com/llm/humaneval-mbpp)

| Model | HumanEval | MBPP | LiveCodeBench |
|-------|-----------|------|---------------|
| Codestral 25.01 (22B) | **86.6%** | 91.2% (alt source) / 80.2% | 37.9% |
| Codestral 22B (v1) | 81.1% | 75.4% | 29.5% |

### 2.6 Fill-in-the-Middle (FIM) Benchmarks
From Qwen2.5-Coder Technical Report ([arXiv PDF](https://arxiv.org/pdf/2409.12186)):

| Model | Python FIM | Java FIM | JavaScript FIM | Average |
|-------|-----------|---------|---------------|---------|
| Qwen2.5-Coder-7B-Base | 61.6% | 62.1% | 53.2% | **57.5%** |
| Qwen2.5-Coder-14B-Base | 64.0% | 69.6% | 46.8% | **59.9%** |
| Qwen2.5-Coder-32B-Base | 65.9% | 68.3% | 70.9% | **63.9%** |
| DeepSeek-Coder-V2-Lite-Base (16B MoE) | 50.0% | 59.6% | 50.0% | 51.8% |
| DeepSeek-Coder-33B-Base | 56.1% | 58.4% | 51.9% | 50.3% |

Qwen2.5-Coder-32B-Base leads on FIM with **88.3% overall** on HumanEval-FIM + SAFIM + CrossCodeEval + RepoEval combined.

---

## 3. Tool Calling (Function Calling) Benchmarks

### 3.1 BFCL (Berkeley Function Calling Leaderboard)
Source: [LLM Stats BFCL](https://llm-stats.com/benchmarks/bfcl), updated May 2026

| Model | BFCL Score | Size | Notes |
|-------|-----------|------|-------|
| Llama 3.1 405B Instruct | **88.5%** | 405B | SOTA |
| Llama 3.1 70B Instruct | 84.8% | 70B | |
| Llama 3.1 8B Instruct | 76.1% | 8B | Strong for size |
| Qwen3 235B A22B | 70.8% | 235B MoE | |
| Qwen3 32B | 70.3% | 32B | |
| **Qwen3 30B A3B** | **69.1%** | 30B MoE | |
| QwQ-32B | 66.4% | 32B | Reasoning model |

From [InsiderLLM Function Calling Guide](https://insiderllm.com/guides/function-calling-local-llms) (Feb 2026):
- **Qwen 2.5 7B** achieves **0.933 F1** for tool selection — "best function-calling model for most local setups"
- Qwen 2.5 14B recommended for anything agentic (multi-step)
- Models at 7B are usable for single-tool calls. Multi-step chains need 14B+

### 3.2 Tool Calling Reliability by Model Size

| Size Range | Reliability | Best Models | Notes |
|-----------|-------------|-------------|-------|
| 1.5B-3B | Unreliable | — | Cannot handle complex schemas |
| 7B | Good for single calls | Qwen2.5 7B (0.933 F1) | Reliable single-tool calling |
| 14B | Good for multi-step | Qwen2.5-Coder 14B | Reliable chains |
| 32B+ | Excellent | Qwen3 32B (70.3% BFCL) | Complex agentic workflows |

### 3.3 Known Tool Call Failures by Model

| Model | Issue | Reference |
|-------|-------|-----------|
| DeepSeek-R1 distill (all sizes) | Thinking tokens (`<think>`) leak into tool calls, breaking JSON parsing | [Ollama Issue #10935](https://github.com/ollama/ollama/issues/10935), [HuggingFace Discussion](https://huggingface.co/deepseek-ai/DeepSeek-R1/discussions/122) |
| DeepSeek-R1-0528 official Ollama | Missing tool call template in official registry; community mods available | [MFDoom/deepseek-r1-tool-calling](https://registry.ollama.com/MFDoom/deepseek-r1-tool-calling) |
| Llama 3.2 3B | Cannot handle nested JSON schemas | InsiderLLM |
| Models <7B | Generally unreliable for structured tool calling | Consensus |

---

## 4. MoE vs Dense Architecture for CPU Inference

### 4.1 Technical Analysis for Bandwidth-Limited Systems

**Key point:** MoE advantages that work on GPU do NOT translate to CPU-only inference.

**Why MoE helps on GPU:**
- All expert weights stored in fast VRAM
- Only active experts compute; inactive ones consume zero compute
- Memory bandwidth not the bottleneck (VRAM bandwidth ~900 GB/s+ on modern GPUs)

**Why MoE HURTS on CPU (especially DDR3-1333):**
- ALL parameters (including inactive experts) must be **loaded from RAM into CPU cache** for every forward pass — the router needs to evaluate all experts
- Memory bandwidth on the target hardware: **~42 GB/s per socket** (DDR3-1333, 3 channels × 2 CPUs)
- MoE models have ~2-10× more total parameters than equivalent-quality dense models
- Even though only ~10% of params compute, **100% must be read from RAM**
- Result: **MoE is strictly worse on CPU bandwidth-limited hardware**

Source: [treeru.com MoE vs Dense Analysis](https://treeru.com/en/blog/moe-vs-dense-qwen3-30b-14b-comparison): "Dense wins for local deployment... on CPU bandwidth-limited systems, MoE structural overhead — massive memory footprint, memory bandwidth bottleneck — makes MoE strictly worse than a well-optimized Dense model."

### 4.2 Quantitative Impact

| Architecture | Total Params | Active Params | RAM Read/Token | Compute | CPU Winner? |
|-------------|-------------|---------------|----------------|---------|-------------|
| Dense 7B | 7B | 7B | ~14 GB (FP16) / ~4 GB (Q4) | Full | **Yes** (for fitting) |
| Dense 14B | 14B | 14B | ~28 GB (FP16) / ~8 GB (Q4) | Full | **Yes** (for quality) |
| MoE 16B (DS-Coder-V2-Lite) | 16B | 2.4B | ~32 GB (FP16) / ~9 GB (Q4) | Low | **No** (wasted bandwidth) |
| MoE 30B (Qwen3-30B-A3B) | 30.5B | 3B | ~61 GB (FP16) / ~17 GB (Q4) | Very low | **No** (bandwidth bottleneck) |

**Recommendation for target hardware (2× E5-2620 v1, 236 GB RAM, DDR3-1333):**
- Dense models are preferred over MoE
- Q4 quantized 7B-14B dense models are optimal
- MoE models like Qwen3-Coder-30B-A3B (17 GB Q4) will be **slower** than dense 14B (8 GB Q4) because memory bandwidth saturation punishes the larger total parameter load

---

## 5. Quantization Analysis

### 5.1 GGUF Quantization Levels — Quality vs. Speed (CPU-focused)
Sources: [Presenc AI Benchmarks 2026](https://presenc.ai/research/local-llm-quantization-quality-benchmarks-2026), [bmdpat.com quantization guide](https://bmdpat.com/blog/gguf-quantization-q4-q5-q8-explained-2026), [LocalClaw guide](https://localclaw.io/blog/quantization-guide)

| Quant | Bits/Param | Size (7B model) | Quality vs FP16 | Speed on CPU | Best for |
|-------|-----------|-----------------|-----------------|-------------|----------|
| Q8_0 | 8.0 | ~7.7 GB | ~99.5% | Fast | Quality-critical tasks, ample RAM |
| Q6_K | 6.6 | ~5.9 GB | ~99% | Fast | Quality-first |
| **Q5_K_M** | 5.3 | ~5.1 GB | **~97-98%** | Faster | **Sweet spot for most users** |
| Q5_K_S | 5.0 | ~4.8 GB | ~97.5% | Faster | Slightly smaller Q5 |
| **Q4_K_M** | 4.5 | ~4.4 GB | **~96.5%** | Fastest | **Best balance for limited RAM** |
| Q4_K_S | 4.3 | ~4.1 GB | ~95.5% | Fastest | When every MB counts |
| Q3_K_M | 3.3 | ~3.5 GB | ~92% | Fastest | Not recommended for coding |
| Q2_K | 2.6 | ~2.8 GB | ~85% | Fastest | Experimental only |

### 5.2 Impact on Coding Accuracy
From [Presenc AI benchmarks](https://presenc.ai/research/local-llm-quantization-quality-benchmarks-2026):

| Quant | Perplexity delta (vs FP16) | GSM8K drop | Coding quality impact |
|-------|---------------------------|-------------|----------------------|
| Q8_0 | +0.2% | Minimal | Essentially lossless |
| Q6_K | +0.4% | Minimal | Safe for all coding |
| Q5_K_M | +1.0% | <1% | Safe for coding |
| Q4_K_M | +1.9% | 1-2% | Acceptable for most coding |
| Q3_K_M | +5.0% | 5-8% | **Significant regression** |
| Q2_K | +14% | 20%+ | Unusable for coding |

**Key recommendation for target hardware:** On CPU-only with DDR3-1333 bandwidth constraint:
- **Q5_K_M** is the sweet spot if RAM allows (best quality-per-bandwidth ratio)
- **Q4_K_M** is the fallback when RAM is tight (only ~1.5% additional quality loss vs Q5)
- **Q8_0** not recommended — 2× memory traffic for marginal quality gain
- **Q3_K_M and below avoid** — coding accuracy degrades non-linearly below 4-bit

### 5.3 Quantization Overhead on CPU
- GGUF on CPU uses llama.cpp with inline dequantization + FP32 accumulation
- Lower quantization = less data to read from RAM = higher token throughput
- On DDR3-1333 (42 GB/s per socket): Q4_K_M reads ~50% less data per token than Q8_0
- For a 7B model: Q4_K_M (~4.4 GB loaded per token) vs Q8_0 (~7.7 GB)
- **Throughput scales approximately linearly with quantization level** on bandwidth-bound CPU

---

## 6. Community Best Practices

### 6.1 Recommended Models for OpenCode + Ollama
Based on community guides and GitHub discussions:

| Source | Recommended Model | Reason |
|--------|------------------|--------|
| OpenCode maintainers (opencode.gr.com) | Qwen 3 Coder 30B (large), Qwen2.5-Coder 14B (medium), Qwen2.5-Coder 7B (small) | Balanced speed/quality |
| Sonu Sahani (Jan 2026) | Qwen 3 Coder 30B with Ollama | Verified working with tool calls |
| SynapticSage GitHub | qwen2.5-coder:14b, qwen2.5-coder:7b, llama3.1:8b | All verified tool-capable |
| InsiderLLM (Feb 2026) | Qwen 2.5 7B (best local FC), 14B for agentic | Function calling focus |
| Community consensus (2026) | **Qwen2.5-Coder / Qwen3-Coder series** | Best tool-calling + coding quality for local |

### 6.2 Common Problems and Solutions

| Problem | Solution | Source |
|---------|----------|--------|
| Tool calls not executing | Set `tool_call_format = "json_fallback"` | OpenCode Ollama docs |
| Model outputs thinking in tool calls | Use non-thinking mode or Qwen3-Coder (no thinking) | InsiderLLM |
| "401 unauthorized" on Ollama | Run `ollama signin`, check keys | Ollama troubleshooting |
| DeepSeek-R1 distill tool call fails | Use community mod (MFDoom/deepseek-r1-tool-calling) with custom template | GitHub Issue #10935 |
| JSON schema validation errors | Validate tool definitions have correct `type: "object"` wrapper | Markaicode guide |
| Slow on CPU | Use Q4_K_M quant, reduce context window, avoid MoE models | Consensus |

### 6.3 Context Window Tradeoffs
- Larger context = more KV cache memory = less RAM for model
- On 236 GB RAM target: context is not the limiting factor
- **Recommended:** 32K-64K context for tool-calling workflows
- Each token of context consumes ~2-4 MB of KV cache (Q4 quant, depending on model)

---

## 7. Specific Recommendations for Target Hardware

### Hardware Profile
- **CPU:** 2× Xeon E5-2620 v1 (6C/12T each = 12C/24T total)
- **ISA:** AVX only, **no AVX2**, **no AVX-512**
- **RAM:** 236 GB DDR3-1333
- **Memory bandwidth:** ~42 GB/s per socket (dual-socket: ~51 GB/s aggregate)
- **GPU:** None (CPU-only via Ollama)

### Critical Constraints

1. **No AVX2** → llama.cpp falls back to AVX kernels; ~2-3× slower than AVX2-capable CPUs
2. **DDR3-1333 bandwidth** → 42 GB/s per socket is the binding bottleneck
3. **CPU-only** → No GPU offloading; all computation + memory access on CPU
4. **Large RAM (236 GB)** → Can load models up to ~200 GB Q4

### Recommended Models (ranked)

| Priority | Model | Size (Q5_K_M) | Why |
|----------|-------|----------------|-----|
| **1** | Qwen2.5-Coder 7B | ~5 GB | Fits comfortably, good quality, fast on CPU |
| **2** | Qwen2.5-Coder 14B | ~9.5 GB | Best quality-per-bandwidth ratio for coding |
| **3** | Qwen3 8B | ~5.5 GB | Newer architecture, thinking mode toggle |
| **4** | Qwen2.5-Coder 32B | ~20 GB | Max quality, but ~2× slower than 14B |
| **Avoid** | Qwen3-Coder-30B-A3B | ~17 GB | MoE: all 30B read per token despite 3B active |
| **Avoid** | DeepSeek-Coder-V2-Lite | ~10 GB | MoE: 16B read per token despite 2.4B active |
| **Avoid** | DeepSeek-R1-Distill-14B | ~8.5 GB | Thinking tokens break tool calling |

### Throughput Estimates (CPU-only, Q5_K_M, DDR3-1333)
Based on extrapolation from known llama.cpp benchmarks on AVX-only CPUs:
- 7B model: ~2-4 tok/s
- 14B model: ~1-2 tok/s
- 32B model: ~0.5-1 tok/s
- MoE 30B: ~0.3-0.5 tok/s (worse than dense 14B despite higher active compute)

---

## 8. References

### OpenCode Documentation
- OpenCode Ollama adapter: https://opencode.gr.com/opencode-ollama.html
- Ollama OpenCode integration: https://docs.ollama.com/integrations/opencode
- OpenCode providers docs: https://opencode.ai/docs/providers/
- OpenCode custom tools: https://opencode.ai/docs/custom-tools
- GitHub Issue #1034 (tool calling): https://github.com/anomalyco/opencode/issues/1034

### Benchmark Sources
- CodeSOTA HumanEval/MBPP: https://www.codesota.com/llm/humaneval-mbpp
- CodeSOTA LiveCodeBench/SWE-bench: https://www.codesota.com/llm/coding-benchmarks
- Qwen2.5-Coder Technical Report (arXiv): https://arxiv.org/abs/2409.12186
- Qwen3 Technical Report: https://arxiv.org/pdf/2505.09388
- DeepSeek-Coder-V2 Benchmarks (DeepWiki): https://deepwiki.com/deepseek-ai/DeepSeek-Coder-V2/5-performance-benchmarks
- Gemma 4 Benchmarks: https://gemma4-ai.com/blog/gemma4-benchmark
- LLM Stats BFCL Leaderboard: https://llm-stats.com/benchmarks/bfcl
- Artificial Analysis: https://artificialanalysis.ai
- Epoch AI SWE-bench: https://epoch.ai/benchmarks/swe-bench-verified

### Quantization
- Presenc AI Quantization Benchmarks: https://presenc.ai/research/local-llm-quantization-quality-benchmarks-2026
- bmdpat.com GGUF Guide: https://bmdpat.com/blog/gguf-quantization-q4-q5-q8-explained-2026
- LocalClaw Quantization Guide: https://localclaw.io/blog/quantization-guide
- Youngju.dev GPTQ/AWQ/GGUF: https://www.youngju.dev/blog/llm/2026-03-03-llm-quantization-gptq-awq-gguf.en

### MoE vs Dense
- treeru.com MoE vs Dense: https://treeru.com/en/blog/moe-vs-dense-qwen3-30b-14b-comparison
- n1n.ai MoE vs Dense: https://explore.n1n.ai/blog/moe-vs-dense-35b-benchmark-8gb-vram-2026-03-31

### Community Guides
- Sonu Sahani OpenCode+Ollama: https://sonusahani.com/blogs/opencode-ollama
- InsiderLLM Function Calling Guide: https://insiderllm.com/guides/function-calling-local-llms
- InsiderLLM Qwen Guide: https://insiderllm.com/guides/qwen-models-guide
- SynapticSage OpenCode setup: https://github.com/SynapticSage/setup_opencode_ollama
- Markaicode Ollama tool calling fix: https://markaicode.com/fix-ollama-tool-calling-errors-debugging-guide
- Alex CloudStar local models 2026: https://www.alexcloudstar.com/blog/local-ai-models-coding-ollama-2026
- Will It Run AI Qwen3Coder vs DeepSeek: https://willitrunai.com/blog/qwen-3-coder-vs-deepseek-coding

### Tool Calling / Function Calling
- BFCL Paper (ICML 2025): https://proceedings.mlr.press/v267/patil25a.html
- BFCL GitHub: https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard
- DeepSeek-R1 tool calling issue: https://github.com/ollama/ollama/issues/10935
- DeepSeek-R1 tool calling community mod: https://registry.ollama.com/MFDoom/deepseek-r1-tool-calling
