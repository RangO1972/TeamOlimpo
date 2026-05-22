---
data: '2026-05-21'
timestamp: '2026-05-21T01:51:20'
agent: efesto
invocation: 17
type: analysis
status: completed
priority: high
title: Claude Context chunker deep analysis
---

## Analisi completata: Claude Context (Zilliz) — Chunker & Motore di Indicizzazione

**Repo**: `/home/stra/TeamOlimpo/Team/Fucina/repos/claude-context/`
**Report**: `/home/stra/TeamOlimpo/Team/Fucina/claude-context-chunker-analysis.md`

### Risultati principali

1. **AST Splitter**: `AstCodeSplitter` con tree-sitter per 9 linguaggi (JS, TS, Python, Java, C++, Go, Rust, C#, Scala). ChunkSize=2500, Overlap=300. Fallback automatico a `LangChainCodeSplitter` (1000/200).

2. **Merkle Tree**: Implementato come DAG con SHA-256 in `MerkleDAG`, ma usato SOLO per change detection a livello di file, non per chunk differenziali. Sync incrementale cancella e reindicizza file interi.

3. **Hybrid Search**: BM25 (Milvus FunctionType.BM25) + dense vector (FloatVector). Rerank con RRF (k=100). Attivo per default (`HYBRID_MODE=true`).

4. **MCP Tools**: 4 tool esposti — `index_codebase`, `search_code`, `clear_index`, `get_indexing_status`. Indexing in background asincrono con AbortController.

5. **Bug rilevato**: `AstCodeSplitter.getSupportedLanguages()` chiamato in `context.ts` ma inesistente (solo `isLanguageSupported()` esiste). Causerebbe runtime error.

### Output reference
- `Team/Fucina/claude-context-chunker-analysis.md`
