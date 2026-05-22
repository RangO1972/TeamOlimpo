---
data: '2026-05-21'
timestamp: '2026-05-21T01:51:34'
agent: efesto
invocation: 18
type: report
status: completed
priority: medium
title: OpenHuman chunker analysis — full report
---

## Report: OpenHuman chunking system analysis

Produced a comprehensive analysis of the OpenHuman memory tree chunking system at `/home/stra/TeamOlimpo/Team/Fucina/repos/openhuman/src/openhuman/memory/tree/`.

### Files analysed
- `chunker.rs` (814 lines) — chunking strategy, split logic, greedy packing
- `types.rs` (428 lines) — core types: Chunk, Metadata, SourceKind, DataSource, chunk_id()
- `ingest.rs` (707 lines) — ingest pipeline orchestration
- `content_store/{mod,paths,compose,atomic,read,tags,raw,obsidian}.rs` — disk persistence
- `retrieval/{search,source,topic,global}.rs` — 3-tree retrieval + entity search
- `score/{mod,signals/types,signals/ops,signals/mod}.rs` — scoring signals + thresholds
- `tree_topic/{hotness,types}.rs` — hotness tracking formula

### Key findings
1. **Hybrid chunker**: source-kind-aware dispatch (Chat: `## ` boundaries, Email: `---\nFrom:` boundaries, Document: paragraph split). Greedy packing with 3000 token default limit.
2. **Deterministic IDs**: SHA-256(source_kind | source_id | seq | content) truncated to 32 hex chars.
3. **Immutable body contract**: chunk files on disk never overwritten; SHA-256 verified on every read.
4. **Two-tier scoring**: cheap regex signals first (drop < 0.15, keep > 0.85), LLM only for borderline chunks.
5. **3 memory trees**: Source (per-source summaries), Topic (per-entity summaries, lazy via hotness), Global (time-windowed digest).
6. **Hotness formula**: ln(mentions+1) + 0.5×distinct_sources + recency_decay + centrality + 2.0×query_hits. Threshold: 10.0 for topic tree creation.

### Output
Report saved to: `/home/stra/TeamOlimpo/Team/Fucina/openhuman-chunker-analysis.md`
