---
title: Agent Design Methodology
aliases: [agent-design-methodology, agent-design]
tags: [sops, agenti, design]
---

# Agent Design Methodology

Reference for Atena when designing agent files for Team Olimpo.

---

## Agent file structure

1. **Frontmatter** — technical identity: `description`, `mode`, `model`, `permission`. No custom fields.
2. **Header comment** — 2-3 lines readable by humans: who the agent is, what they do, what they don't do.
3. **Identity** — mission in the team (2-4 sentences)
4. **Communication style** — tone, rhythm, language rule
5. **Operating rules** — non-negotiable constraints, protocols
6. **Competencies** — by domain, not flat list. Each with context for when/how to use.
7. **Workflows** — numbered steps with input/output per step
8. **Interactions** — direction (receive/produce) and format. No agent names — Hermes manages routing.
9. **Limitations** — what the agent does NOT do, explicit boundaries
10. **References** — external docs (methodology, vault conventions, handoff guide)

Mandatory: frontmatter, header comment, identity, communication style, operating rules, competencies, workflows, limitations.

---

## Model

Default: `opencode/big-pickle`. Change only if explicitly specified in the brief.

---

## Description field

The `description` selects which agent to invoke. Critical.

**Rules:**
- Contains role AND usage trigger ("Use when...")
- Operational, not poetic
- One line, ~150-200 chars
- Uniquely distinguishes this agent from all others
- Never mention specific agent names

**Anti-patterns:** vague ("Helps with various things"), too restrictive ("Only for YAML files"), duplicate of another agent's description.

---

## Permission / tool selection

| Role type | Recommended permissions |
|-----------|------------------------|
| Writes code/files | `read`, `write`, `edit`, `bash` |
| Research and analysis | `read`, `write`, `websearch`, `webfetch` |
| Delegates to other agents | `read`, `write`, `edit`, `task` |
| Read-only consultation | `read` |

`bash` = code execution — don't grant unless needed. `task` = agent delegation — only for orchestrators or collaborators.

---

## Depth calibration

- Narrow, procedural domain: detailed and concise instructions.
- Wide domain requiring judgment: richer instructions with principles, frameworks, anti-patterns.
- Prompt length consumes context. Same thing in fewer words without precision loss → do it.

---

## Common anti-patterns

- **Decorative personality**: describing tone without operative instructions that reflect it. "Concise" + verbose output = contradiction.
- **Vague limitations**: "Don't do things outside your scope" says nothing. List explicitly.
- **Process without steps**: "Analyze and produce output" is not a process. Each step needs input, action, output.
- **Competency list**: listing capabilities without explaining how and when to use them.
- **Custom frontmatter fields**: non-standard fields belong in the body, not frontmatter.
- **Member name references**: agent files must not reference other team members by name. The orchestrator manages routing.

---

## Member identity file (`Team/Members/<name>.md`)

Every agent has two files: `Team/Members/<name>.md` (identity, human-facing) and `.opencode/agents/<name>.md` (operational, system-facing). Created together, kept in sync.

### Structure

1. **Frontmatter** — `type: member`, `agent: <name>`, `role: <role>` (all lowercase, hyphenated).
2. **`# <Name> — Team Olimpo`** — title.
3. **`## Identity`** — who this agent is, their mission in a single paragraph.
4. **`## Values`** — 3-5 operational principles. Each is a decision-making rule, not an aspiration.
5. **`## Boundaries`** — explicit list of what this agent does NOT do.
6. **`## Dependencies`** — tools, data sources, SOPs this agent relies on. **Never list other agents by name.** The orchestrator handles routing; agents do not know each other.

### Rules
- **English only**
- **No agent names in Dependencies** — list tools, data paths, SOPs, technologies. Not people.
- One file per agent

---

## Prompt Minimal Standard

Every line in an agent file carries operational weight. No filler, no decoration.

**Self-review after drafting:**
- Does this sentence tell the agent what to do or how to decide? No → remove.
- Can I say the same in fewer words? Yes → compress.
- Decorative adjectives ("comprehensive", "accurate", "professional")? → remove.
- Is `description` operational or descriptive? Must be operational — it selects the agent.

**Prompt length consumes context.** Same meaning in fewer words, always.
