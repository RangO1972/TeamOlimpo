---
data: '2026-05-21'
timestamp: '2026-05-21T18:15:08'
agent: hermes
invocation: 9
type: report
status: completed
priority: medium
title: OpenCode Plugin Ecosystem Analysis — Taskmanager Replacement Path
task_id: T-RESEARCH-006
completion_notes: 'Research complete. Report linked to Chimera project (T-PROGETTO-001).
  Next step: deep analysis of Chimera + new learnings — deferred.'
---

# OpenCode Plugin Ecosystem Analysis — Taskmanager Replacement Path

## Context

Research commissioned to explore the possibility of creating an OpenCode skill/plugin
with deterministic startup that replaces or complements the current **taskmanager MCP server**
(Python subprocess via `uv run python -m tools.taskmanager.server`).

## Current Architecture (Team Olimpo)

| Component | Implementation | Status |
|-----------|---------------|--------|
| Taskmanager | MCP server: `tools/taskmanager/server.py` (6 tools) | Active |
| Skills | None (`/home/stra/TeamOlimpo/.opencode/skills/` absent) | Empty |
| Plugins | None (no `.opencode/plugins/` or `.opencode/plugin/`) | Empty |
| Config | `opencode.json` with 4 MCP entries (handoff, email_processor, taskmanager, knowledge_base) | Current |

## Key Discovery: Skills vs Plugins

| Aspect | Skills | Plugins |
|--------|--------|---------|
| Format | Markdown (`SKILL.md`) | TypeScript/JavaScript |
| Startup | Passive (loaded on demand via `skill` tool) | Deterministic (`config()` hook at init) |
| Can register tools? | No | Yes (`tool: { ... }`) |
| Can modify system prompt? | Via content only | Yes (`experimental.chat.system.transform`) |
| Can intercept tool calls? | No | Yes (`tool.execute.before/after`) |

**Conclusion: Only plugins can replace/complement the taskmanager because they have
startup hooks and can register native tools.**

## Ecosystem Landscape

### 1. Superpowers (obra/superpowers) — ⭐201k GitHub stars
**The gold standard.** Single JS plugin (135 lines) that:
- Uses `config(cfg)` hook to auto-register its skills path at startup
- Uses `experimental.chat.messages.transform` to inject bootstrap into every session
- Ships 30+ skills: brainstorming, TDD, code review, git worktrees, writing-plans, etc.
- Zero MCP dependencies — pure plugin architecture

Install: `"plugin": ["superpowers@git+https://github.com/obra/superpowers.git"]`

### 2. Oh My OpenAgent / oh-my-openagent (code-yeongyu) — ⭐58.7k
Multi-agent orchestration framework with:
- 11 specialized agents (Sisyphus, Oracle, Librarian, etc.)
- 40+ lifecycle hooks, ultrawork autonomous mode
- Built-in skill-loader system with MCP extraction from skill YAML
- Hashline edit tool, LSP/AST integration

### 3. Other Notable Plugins
| Plugin | Purpose |
|--------|---------|
| opencode-skills-collection | 1000+ pre-bundled skills (34k npm weekly) |
| opencode-agent-skills | Dynamic multi-directory skill discovery |
| opencode-mem | Persistent memory via vector DB across sessions |
| opencode-snippets | Inline text expansion for prompts |
| opencode-sessions | Session management + multi-agent collaboration |
| opencode-workspace | 16-component multi-agent orchestration |

## Recommended Architecture for Taskmanager Replacement

Based on the analysis, the optimal approach is:

### Plugin (`.opencode/plugins/task-manager.ts`)
```typescript
export default async () => ({
  config: async (cfg) => {
    // Startup deterministic: load persisted state
    loadTasks()  // Async read from state.json
  },
  'experimental.chat.system.transform': async (output) => {
    // Inject current task state into system prompt
    // Replaces current "State Management" section in Hermes prompt
  },
  tool: {
    task_create: { /* ... TypeScript impl ... */ },
    task_update_status: { /* ... */ },
    task_query: { /* ... */ },
    task_summary: { /* ... */ },
    task_log_event: { /* ... */ },
    task_export: { /* ... */ },
  }
})
```

### Skill (`.opencode/skills/task-manager/SKILL.md`)
Markdown instructions telling Hermes how to use the tools,
replacing the "Mandatory task pattern" and "State Management" sections
currently in Hermes's system prompt.

### Benefits over current MCP approach
1. **No Python subprocess** — tools run in OpenCode's Node.js runtime
2. **Startup deterministic** — `config()` hook fires at init, guaranteed
3. **Faster** — no IPC/stdio overhead, no process spawn
4. **Lighter** — no dependency on `uv`, Python, MCP SDK
5. **Cleaner** — plugin auto-discovers, no config changes needed

## Links to Chimera Project (T-PROGETTO-001)

This research feeds into the broader Chimera architecture redesign.
Previously explored tools with high GitHub stars under Chimera;
this report extends that analysis to the plugin/skill layer.

## Next Steps (deferred)
1. Deep analysis of existing Chimera project research
2. Cross-reference with new learnings from Superpowers/OMO
3. Design document for plugin-based taskmanager replacement with checklist
