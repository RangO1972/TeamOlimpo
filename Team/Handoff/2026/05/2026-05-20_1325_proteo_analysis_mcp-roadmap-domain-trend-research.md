---
data: '2026-05-20'
timestamp: '2026-05-20T13:25:17'
agent: proteo
invocation: 19
type: analysis
status: completed
priority: medium
title: MCP Roadmap Domain & Trend Research (MCP-R-1)
task_id: MCP-R-1
---

# MCP Roadmap — Proteo Research Report

**Task ID:** MCP-R-1
**Date:** 2026-05-20
**Confidence:** High (multiple independent sources, including official MCP spec, industry blogs, and open-source repositories)
**Information Gaps:** No verified data on OpenCode-specific MCP usage in multi-agent teams; OpenCode MCP documentation still maturing.

---

## Executive Summary

The Model Context Protocol (MCP) has solidified as the de facto standard for AI agent-tool integration, surpassing 97M monthly SDK downloads and 200+ server implementations by Q2 2026. MCP acts as a universal "USB-C for AI" — providing standardized Tools, Resources, and Prompts primitives over JSON-RPC 2.0. For Team Olimpo, MCP can serve as the **execution backbone** for all state interaction: task state (replacing the 25k-token Scratchpad), knowledge base queries, orchestration routing, and quality gates. The ecosystem has mature patterns for multi-agent handoffs, tool chaining, and gateway architectures (e.g., Lasso MCP Gateway, FastMCP). The key insight: MCP handles transport and tool-calling mechanics; orchestration logic stays in the orchestrator (Hermes). This separation of concerns is the emerging industry standard.

---

## 1. MCP Patterns Found

### 1.1 Orchestrator-Subagent Handoff Pattern

- **Description:** A primary orchestrator agent delegates sub-tasks to specialized sub-agents via MCP tool calls. Each sub-agent is exposed as a callable tool with standardized input/output schemas. Handoffs carry workflow IDs, context metadata, and structured results. This mirrors the Team Olimpo Hermes → worker agents pattern exactly.
- **Source/Link:** [Knit — MCP Agent Orchestration: Chaining, Handoffs](https://www.getknit.dev/blog/advanced-mcp-agent-orchestration-chaining-and-handoffs); [Dev.to complete MCP guide](https://dev.to/x4nent/complete-guide-to-mcp-model-context-protocol-in-2026-architecture-implementation-and-4a11)
- **Applicability to Team Olimpo:** **Directly applicable.** Our existing Hermes-as-orchestrator pattern fits naturally. Each agent (Proteo, Atena, Efesto, etc.) could be wrapped as an MCP server with their specific tools. Hermes calls them as MCP tools instead of relying on the Scratchpad as the sole state mechanism.

### 1.2 Token-Based Tool Orchestration Pattern

- **Description:** Enforces execution order for MCP tools using dependency tokens. Each tool returns a token that must be passed to the next tool in sequence. Prevents out-of-order execution and ensures deterministic workflows.
- **Source/Link:** [AWS Blog — Flexibility to Framework: Building MCP Servers with Controlled Tool Orchestration](https://aws.amazon.com/blogs/devops/flexibility-to-framework-building-mcp-servers-with-controlled-tool-orchestration); [YouTube — MCP Tool Orchestration](https://www.youtube.com/watch?v=v5nLs35_pcg)
- **Applicability:** Relevant for quality gates and pipeline workflows where tool execution order matters (e.g., research → design → build → verify). The token pattern could enforce our handoff → review → merge pipeline.

### 1.3 Agent Graph / Complex Topology Pattern

- **Description:** Agents arranged in non-linear graphs with bi-directional communication, feedback loops, and dynamic routing. MCP provides namespaced tool definitions and consistent invocation semantics for this.
- **Source/Link:** [Knit — MCP Agent Orchestration (Agent Graphs section)](https://www.getknit.dev/blog/advanced-mcp-agent-orchestration-chaining-and-handoffs)
- **Applicability:** Useful if Team Olimpo grows beyond linear chains. For now, the simpler handoff pattern suffices, but the architecture should allow graph topologies.

### 1.4 MCP Gateway / Proxy Pattern

- **Description:** A centralized gateway layer (like Lasso's MCP Gateway) sits between LLMs and MCP servers, providing unified auth, rate-limiting, guardrails, and observability. The gateway reads a config file, manages server lifecycles, and intercepts all requests/responses.
- **Source/Link:** [Lasso MCP Gateway](https://github.com/lasso-security/mcp-gateway); [IBM Enterprise MCP Architecture](https://www.aigl.blog/architecting-secure-enterprise-ai-agents-with-mcp-ibm-oct-2025)
- **Applicability:** Medium-term. A Team Olimpo Gateway could centralize MCP server management, provide unified auth, and add monitoring. Not an immediate need but valuable for production-hardening.

### 1.5 MCP + A2A Complementary Pattern

- **Description:** MCP handles agent→tool connections; A2A (Agent-to-Agent protocol by Google) handles agent→agent collaboration. Both are governed by the Agentic AI Foundation (Linux Foundation) since Dec 2025. They work together: MCP for tool access, A2A for peer agent delegation.
- **Source/Link:** [Dev.to Complete Guide — MCP vs A2A table](https://dev.to/x4nent/complete-guide-to-mcp-model-context-protocol-in-2026-architecture-implementation-and-4a11); [Google ADK + A2A](https://dev.to/x4nent/google-adk-10-a2a-protocol-pythongojavatypescript-ga-agentcard-task-and-sse-redefining-58e5)
- **Applicability:** A2A is still maturing (v1.0 released). Monitor for Q3 2026 when MCP spec adds native agent-to-agent coordination primitives. Not needed now but architect for it.

---

## 2. Ecosystem Analysis

### 2.1 Common MCP Server Types

| Category | Major MCP Servers | Capabilities |
|----------|------------------|--------------|
| **Dev Tools** | GitHub, GitLab, Sentry | Issue/PR management, code search, error tracking |
| **Collaboration** | Slack, Notion, Google Drive, Gmail | Message search, document read/write, file management |
| **Databases** | PostgreSQL, MongoDB, Redis, SQLite | Schema exploration, query execution, data analysis |
| **Cloud/Infra** | AWS (Bedrock, Cloud Control), Kubernetes, Terraform | Resource inspection, cluster management, IaC validation |
| **CRM/Business** | Salesforce, Jira, HubSpot, Linear | Lead management, ticket handling, pipeline analysis |
| **Task Management** | mcp-tasks, task-manager-mcp, Taskade, Notion | Task CRUD, project tracking, status workflows |
| **Web/Content** | Firecrawl, Brave Search, Tavily, Jina AI | Web scraping, search, URL-to-markdown conversion |
| **Memory/RAG** | Chroma MCP, Knowledge Graph Memory, Supabase | Vector search, persistent agent memory, semantic retrieval |
| **IDE Integration** | Claude Code, Cursor, Cline, Windsurf | Code editing, terminal execution, filesystem access |
| **Filesystem** | @modelcontextprotocol/server-filesystem | Read/write files with path-based access control |

**Sources:**
- [Awesome MCP Servers — punkpeye (5.2k stars)](https://github.com/punkpeye/awesome-mcp-servers)
- [TokenMix — MCP Servers List 2026](https://tokenmix.ai/blog/mcp-servers-list-2026-complete-directory)
- [MCP Awesome — 1200+ verified servers](https://mcp-awesome.com/)
- [Dev.to Complete Guide — Ecosystem table](https://dev.to/x4nent/complete-guide-to-mcp-model-context-protocol-in-2026-architecture-implementation-and-4a11)

### 2.2 Official MCP Spec Analysis

**Key findings from [modelcontextprotocol.io](https://modelcontextprotocol.io/) and spec:**

1. **Three core primitives:**
   - **Tools** — executable functions the AI model can invoke (like our `handoff_create`, `handoff_list`)
   - **Resources** — read-only data entities (files, API responses, DB snapshots)
   - **Prompts** — standardized templates for consistent AI behavior

2. **Transport evolution:**
   - **stdio** — local IPC, default for desktop agents
   - **Streamable HTTP** (Nov 2025) — replaces legacy SSE; enables remote MCP servers, horizontal scaling, stateless operation
   - Q2 2026: stateless session management for true horizontal scaling

3. **Security model:**
   - OAuth 2.1 + PKCE for remote servers (June 2025 spec)
   - SAML/OIDC IdP integration coming Q2 2026
   - MCP Server Cards (`.well-known` URL) for discovery Q2-Q3 2026

4. **2026 Roadmap milestones:**
   - Q1-Q2: Streamable HTTP stateless operation, session migration
   - Q2: Enterprise auth GA
   - Q2-Q3: MCP Server Cards (`.well-known`)
   - Q3: Agent-to-agent coordination primitives (A2A integration)
   - Q4: MCP Registry — verified server directory with security audits

5. **SDK Ecosystem:** Python (FastMCP 3.0), TypeScript, Java, Kotlin, Go, Rust, C#, PHP, Ruby, Swift — all actively maintained.

**Sources:**
- [modelcontextprotocol.io](https://modelcontextprotocol.io/)
- [modelcontextprotocol GitHub org](https://github.com/modelcontextprotocol) (47k+ followers)
- [Dev.to Complete Guide](https://dev.to/x4nent/complete-guide-to-mcp-model-context-protocol-in-2026-architecture-implementation-and-4a11)

---

## 3. State Management Comparison

| Approach | Pros | Cons | Best For |
|----------|------|------|----------|
| **In-Memory State** | Fastest (<1ms access); zero I/O; simple to implement | Lost on restart/crash; no persistence across sessions; limited by context window size | Single-session agents, stateless operations |
| **File-Based State (current)** | Persistent across restarts; human-readable (Markdown); version-controllable (git); no infrastructure needed | Token-inefficient (read+parse+edit cycles); no concurrent access safety; grows unbounded (25k tokens); AI can corrupt files; no query capability | Small projects, prototyping, human-in-the-loop review |
| **Database-Backed State** | ACID transactions; concurrent access safe; efficient queries; backup/restore; scales horizontally | Infrastructure overhead; schema migrations; latency (5-50ms); serialization/deserialization cost | Long-running tasks, multi-agent coordination, production deployments |
| **MCP-Based State** | Standardized interface; tool-calling instead of file editing; structured I/O; built-in logging/observability; model-agnostic | Must build/maintain MCP servers; initial development cost; network overhead for remote servers | **Team Olimpo's sweet spot** — replaces Scratchpad with structured tools |
| **Hybrid (MCP + DB)** | Combines MCP's standardized interface with DB's persistence; best of both worlds | More complex architecture; two systems to maintain | Enterprise production systems, high-reliability deployments |

### Key State Management Insights from Research

1. **The handoff message pattern** is the #1 most important artifact for state continuity. GetATeam's research from 1000+ production tasks confirms: a structured handoff message the current process writes for the next process is the foundation of reliable agent state.
   - *Source:* [GetATeam — State Management in AI Agents](https://blog.geta.team/state-management-in-ai-agents-lessons-from-1000-tasks)

2. **Explicit state schemas beat implicit state.** LangGraph's approach of typed, reducer-driven state schemas prevents data loss in multi-agent systems. State should be structured, not free-form.
   - *Source:* [LangGraph State Management — Raj Gupta](https://medium.com/@rajgpt630/langgraph-agent-state-management-building-deterministic-ai-agents-772da55e3fc1)

3. **MCP context-passing is for short-term state; persistent state needs external storage.** MCP handles transport of context between chained agents, but long-term state must live in a dedicated store (DB, memory layer, or file system).
   - *Source:* [Knit — FAQ on MCP State Management](https://www.getknit.dev/blog/advanced-mcp-agent-orchestration-chaining-and-handoffs)

4. **The Scratchpad anti-pattern is well-documented.** Reading+parsing+editing cycles for file-based state consume far more tokens than structured tool calls with clear inputs/outputs. AI can accidentally corrupt file-based state.
   - *Source:* [mcp-tasks README — Why not let AI edit files directly](https://github.com/flesler/mcp-tasks)

---

## 4. Concrete Examples (5 MCP Servers)

### Example 1: mcp-tasks (flesler/mcp-tasks)

- **Repo/Link:** [github.com/flesler/mcp-tasks](https://github.com/flesler/mcp-tasks) — ⭐45
- **Tools exposed (5 total):**
  - `tasks_setup` — Initialize a task file (.md/.json/.yml)
  - `tasks_search` — Search tasks with status/text/ID filtering
  - `tasks_add` — Add tasks (batch, with duplicate prevention)
  - `tasks_update` — Update task status or position
  - `tasks_summary` — Get task counts and WIP status
- **Architecture pattern:** TypeScript + @modelcontextprotocol/sdk. Reads/writes local files via MCP tools. stdio transport. 5 minimal tools designed to minimize AI confusion and token usage.
- **Lessons for Team Olimpo:**
  - *Ultra-efficient design:* Only 5 tools, all prefixed with `tasks_` to prevent confusion. We should follow this "minimal surface area" approach.
  - *File-based persistence is OK for now:* Stores state in Markdown/JSON files but access is through tools, not raw file editing. The tools handle parsing, validation, and atomic updates.
  - *Auto WIP management:* Automatically moves tasks between statuses when limits are reached. Shows how deterministic state transitions can be encoded in tools.
  - *Safety by design:* AI cannot rewrite or delete tasks — only add and move them. This is a key design principle.

### Example 2: Task Manager MCP (tradesdontlie/task-manager-mcp)

- **Repo/Link:** [github.com/tradesdontlie/task-manager-mcp](https://github.com/tradesdontlie/task-manager-mcp) — ⭐35
- **Tools exposed (10+):**
  - Task CRUD: `create_task_file`, `add_task`, `update_task_status`, `get_next_task`
  - Project Planning: `parse_prd`, `expand_task`, `estimate_task_complexity`, `get_task_dependencies`
  - Dev Support: `generate_task_file`, `suggest_next_actions`
- **Architecture pattern:** Python + FastMCP. Supports both SSE and stdio transport. Uses an LLM provider for AI-powered features (complexity estimation, PRD parsing). Docker-ready.
- **Lessons for Team Olimpo:**
  - *AI-powered tools:* Some tools (like `suggest_next_actions`) internally call an LLM. We could build similar "smart tools" that wrap Hermes-level reasoning.
  - *PRD-to-tasks pipeline:* Shows how to convert unstructured documents into structured tasks automatically — applicable for converting Hermes briefs into agent tasks.
  - *SSE transport support:* Good reference for adding HTTP transport to our handoff server.

### Example 3: Agent-MCP (rinadelph/Agent-MCP)

- **Repo/Link:** [github.com/rinadelph/Agent-MCP](https://github.com/rinadelph/Agent-MCP) — ⭐1,200
- **Tools exposed:**
  - Agent Management: `create_agent`, `list_agents`, `terminate_agent`
  - Task Orchestration: `assign_task`, `view_tasks`, `update_task_status`
  - Knowledge Management: `ask_project_rag`, `update_project_context`, `view_project_context`
  - Communication: `send_agent_message`, `broadcast_message`, `request_assistance`
- **Architecture pattern:** Python + Node dual implementation. Multi-agent framework with shared knowledge graph (RAG), dashboard UI, and file-locking for conflict prevention.
- **Lessons for Team Olimpo:**
  - *Most relevant example for our architecture.* Agent-MCP mirrors our orchestrator-workers pattern exactly — admin agent coordinates specialized worker agents, each focused on linear tasks.
  - *Short-lived, focused agents:* Each agent lives only for its task, starts with minimal context, documents output in shared memory, then terminates. Directly applicable to our "one handoff per invocation" pattern.
  - *Shared knowledge graph:* Uses RAG for persistent memory across agent sessions — potential replacement for our Library vault search.
  - *Dashboard visualization:* Real-time view of agent status, tasks, and collaboration network.

### Example 4: Lasso MCP Gateway

- **Repo/Link:** [github.com/lasso-security/mcp-gateway](https://github.com/lasso-security/mcp-gateway) — ⭐368
- **Tools exposed:** Acts as proxy/gateway. Exposes all proxied MCP servers' tools through a unified interface. Plus:
  - `get_metadata` — Introspect proxied servers
  - Plugin-based guardrails (PII detection, prompt injection, rate limiting)
- **Architecture pattern:** Python intermediary proxy. Reads `mcp.json` config, manages server lifecycles, intercepts requests/responses. Plugin system for security and observability.
- **Lessons for Team Olimpo:**
  - *Gateway pattern*: A single entry point for all MCP interactions could centralize auth, rate-limiting, and monitoring for our handoff and email servers.
  - *Plugin-based security:* Each request/response goes through configurable filters. We could add validation plugins that check handoff schema compliance before writing.
  - *MCP lifecycle management:* Automatically starts/stops MCP server processes — useful if we grow to many servers.

### Example 5: Chroma MCP / Knowledge Graph Memory

- **Repo/Link:** [github.com/chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp) — part of Chroma ecosystem
- **Tools exposed:**
  - Embedding and semantic search over team documentation
  - Long-term memory across agent sessions
  - Architecture Decision Records (ADR) search
- **Architecture pattern:** Vector database (Chroma) exposed as MCP server. Agents query semantic memory instead of loading everything into context.
- **Lessons for Team Olimpo:**
  - *Team knowledge retrieval*: Our Library/ vault contains a growing knowledge base. A Chroma MCP server could make it semantically searchable by any agent.
  - *Persistent agent memory*: Agents could store "what they learned" in vector memory, making it accessible to future agent invocations — effectively a persistent cross-session memory system.

---

## 5. Recommendations for Team Olimpo

### Top 5 MCP Servers Worth Building (Priority Ranking)

| Priority | MCP Server | Rationale | Estimated Effort |
|----------|-----------|-----------|-----------------|
| **P0** | **Task/State Manager MCP** | Replace Scratchpad with structured task tools (like mcp-tasks). This is the highest-impact change: eliminates the 25k-token file, provides safe CRUD, enables deterministic task lifecycle tracking. | 2-3 days |
| **P1** | **Orchestration MCP** | Expose Hermes's orchestration logic (task routing, agent selection, parallel dispatch) as MCP tools. Enables programmatic workflow control. | 3-5 days |
| **P1** | **Knowledge Base MCP** | Wrap vault search (Library/Wiki) as MCP resources. Agents query wiki content without reading entire files. Could use grep-based or vector-based retrieval. | 2-4 days |
| **P2** | **Quality Gate MCP** | Validate handoff outputs against schema rules, check agent output compliance, enforce handoff-guide.md rules programmatically. Clio's QC checks as MCP tools. | 2-3 days |
| **P3** | **Team Olimpo Gateway** | Unified MCP gateway that aggregates all our servers, provides auth, monitoring, and server lifecycle management. Based on Lasso pattern. | 4-5 days |

### Architecture Blueprint (Recommended)

```
                   ┌─────────────────────────────┐
                   │     Hermes (Orchestrator)    │
                   │  (MCP Client — calls tools)  │
                   └──────────┬──────────────────┘
                              │ MCP stdio/HTTP
          ┌───────────────────┼───────────────────┐
          │                   │                   │
   ┌──────▼──────┐   ┌──────▼──────┐   ┌──────▼──────┐
   │ Task/State  │   │ Knowledge   │   │   Quality   │
   │ MCP Server  │   │ Base MCP    │   │ Gate MCP    │
   │ (state)     │   │ (wiki)      │   │ (QC checks) │
   └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
          │                 │                 │
   ┌──────▼──────┐   ┌──────▼──────┐   ┌──────▼──────┐
   │ Local files │   │ Library/    │   │ Handoff     │
   │ (tasks.md)  │   │ Wiki+Vault  │   │ files (FS)  │
   └─────────────┘   └─────────────┘   └─────────────┘

   ┌────────────────────────────────────────────────┐
   │ Existing MCP Servers (keep: handoff, email)    │
   │ - handoff: handoff_create, handoff_list        │
   │ - email_processor: status, search, discover... │
   └────────────────────────────────────────────────┘
```

### What to Avoid

1. **❌ Building an A2A layer now.** A2A is still maturing; MCP alone handles our needs for the next 3-6 months. Monitor Q3 2026 for native MCP agent-to-agent primitives.

2. **❌ Replacing all file storage with databases immediately.** File-based MCP (like mcp-tasks) works well for mid-scale. Move to DB-backed state only when file-based MCP becomes a bottleneck.

3. **❌ Over-engineering the gateway.** A gateway is useful but not necessary at our current scale (2 MCP servers). Wait until we have 5+ servers.

4. **❌ Mixing orchestration logic into MCP servers.** MCP is for standardized tool interfaces, not for workflow decisions. Keep orchestration logic in Hermes (the planner), not in the tool layer.

5. **❌ Proliferating too many small MCP servers.** Each MCP server adds startup time and config complexity. Prefer one coherent server per domain (e.g., one Task server with 5-8 tools, not 3 separate task servers).

### OpenCode-Specific Integration Notes

Based on research into OpenCode's MCP support:
- OpenCode supports both local (stdio) and remote (HTTP) MCP servers via `opencode.json`'s `mcp` section.
- MCP servers can be enabled globally **or on a per-agent basis** — critical for Team Olimpo where different agents need different tools.
- Environment variables can be passed securely using the `env:` prefix pattern.
- Context budget management is important: servers like GitHub MCP add many tokens and can exceed limits. Design tools to minimize token overhead.

*Sources:*
- [Setting Up MCP in OpenCode](https://ayodele.dev/blog/mcp-opencode-setup)
- [OpenCode MCP Integration Guide](https://lushbinary.com/blog/opencode-mcp-server-integration-extend-ai-tools-guide/)
- [OpenCode MCP Configuration Guide](https://blog.wenhaofree.com/en/posts/articles/opencode-mcp-configuration-guide/)

---

## Immediate Next Steps (for Hermes/Atena)

1. **Phase 1 (Week 1):** Build a Task/State Manager MCP server that replaces the Scratchpad. Model it on mcp-tasks but adapted for Team Olimpo's workflow states (planned → active → review → done). The handoff system itself provides the persistence layer.
2. **Phase 2 (Week 2):** Extend the handoff server with Resources (read handoff files by type/agent/date) and a query tool. This turns the handoff archive into a queryable knowledge base.
3. **Phase 3 (Week 3):** Build a Knowledge Base MCP server that wraps Library/Wiki searches. Start with simple grep/find-based search; add vector search (Chroma) later.
4. **Phase 4 (Future):** Quality Gate MCP server that validates handoff compliance programmatically, then the unified Gateway.

---

## Sources (Full URLs)

1. https://modelcontextprotocol.io/ — Official MCP documentation
2. https://github.com/modelcontextprotocol — MCP GitHub organization (47k+ followers)
3. https://github.com/punkpeye/awesome-mcp-servers — Awesome MCP Servers (5.2k stars)
4. https://github.com/flesler/mcp-tasks — mcp-tasks server (45 stars)
5. https://github.com/tradesdontlie/task-manager-mcp — Task Manager MCP (35 stars)
6. https://github.com/rinadelph/Agent-MCP — Agent-MCP multi-agent framework (1.2k stars)
7. https://github.com/lasso-security/mcp-gateway — Lasso MCP Gateway (368 stars)
8. https://github.com/chroma-core/chroma-mcp — Chroma MCP for vector memory
9. https://dev.to/x4nent/complete-guide-to-mcp-model-context-protocol-in-2026-architecture-implementation-and-4a11 — Complete 2026 MCP guide
10. https://www.getknit.dev/blog/advanced-mcp-agent-orchestration-chaining-and-handoffs — MCP orchestration patterns
11. https://aws.amazon.com/blogs/devops/flexibility-to-framework-building-mcp-servers-with-controlled-tool-orchestration — AWS tool orchestration pattern
12. https://blog.geta.team/state-management-in-ai-agents-lessons-from-1000-tasks — State management in production
13. https://www.aigl.blog/architecting-secure-enterprise-ai-agents-with-mcp-ibm-oct-2025 — IBM enterprise MCP architecture
14. https://medium.com/@rajgpt630/langgraph-agent-state-management-building-deterministic-ai-agents-772da55e3fc1 — LangGraph deterministic state
15. https://blog.wenhaofree.com/en/posts/articles/opencode-mcp-configuration-guide/ — OpenCode MCP configuration
16. https://lushbinary.com/blog/opencode-mcp-server-integration-extend-ai-tools-guide/ — OpenCode MCP integration guide
17. https://ayodele.dev/blog/mcp-opencode-setup — OpenCode MCP setup guide
18. https://tokenmix.ai/blog/mcp-servers-list-2026-complete-directory — MCP servers directory 2026
19. https://mcp-awesome.com/ — 1200+ verified MCP servers
20. https://flocker.md/blog/anthropic-openai-agent-orchestration/ — Anthropic vs OpenAI orchestration
