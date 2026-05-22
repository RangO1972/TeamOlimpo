---
data: '2026-05-20'
timestamp: '2026-05-20T15:55:15'
agent: pythagoras
invocation: 2
type: report
status: completed
priority: medium
title: Grep-First Knowledge Retrieval MCP Research
---

## Research Summary

### Task
Academic and technical research on knowledge retrieval patterns for AI agents, focusing on lightweight grep-first implementations for Team Olimpo's Knowledge Base MCP server design.

### Output File
`Library/documents/knowledge-retrieval-patterns-grep-first-mcp.md`

### Key Findings

1. **Grep beats vector retrieval in agentic settings**: Paper "Is Grep All You Need?" (arXiv:2605.15184) shows grep yields higher accuracy than vector across all tested agent harnesses for fact-location tasks.

2. **98.9% of queries resolve via substring matching**: SmartSearch (arXiv:2603.15599) proves that only 1% of queries truly need semantic search — an index-free grep-only pipeline matches full indexed retrieval.

3. **>90% of RAG performance without vector DB**: Tool-augmented keyword search achieves over 90% of traditional RAG metrics at zero indexing cost (arXiv:2602.23368).

4. **Team Olimpo is firmly in the "grep-only zone"**: At ~3.5MB / 500 files, the corpus is orders of magnitude below the threshold where indexing becomes beneficial (~50MB).

5. **Dedicated MCP server (Option B) recommended** over extending the handoff server, following MCP best practices of single responsibility and tool list separation.

6. **MCP Resource + Tool dual pattern**: Resources (`wiki://` URIs) for client-side discovery and caching; Tools (`kb_search`, `kb_read`, `kb_list`) for agent-driven search.

7. **Token savings estimated at 90-95%**: Replacing full-file loads with targeted search snippets.

### Key Sources
- arXiv:2605.15184 — Is Grep All You Need?
- arXiv:2603.15599 — SmartSearch
- arXiv:2602.23368 — RAG vs Tool-based KB
- arXiv:2601.23254 — GrepRAG
- MCP Official Specification (Resources)
- Vercel Knowledge Agent Template
- grepika, code-index-mcp, llm-wiki-mcp (GitHub)
