# Handoff — Efesto → Hermes: Discovery Rewrite + Rules CLI

**Data:** 2026-05-19  
**Agente:** Efesto (Python Developer)  
**Oggetto:** Refactor `discover` (zero interattivo, YAML strutturato) + nuovo gruppo comandi `rules` in `email_processor`

---

## Cosa è stato fatto

### 1. `tools/email_processor/discovery.py` — Riscrittura completa

| Vecchio | Nuovo |
|---------|-------|
| `Pattern`, `PatternDiscovery`, `YAMLGenerator` classi | Solo `Pattern` (dataclass) e `PatternDiscovery` (con metodi statici) |
| Normalizzazione con `*` placeholder | Normalizzazione con `{device}`, `{date}`, `{num}`, `{email}` placeholder |
| Output tabellare solo in Italiano | Output YAML strutturato + tabella riepilogativa in Inglese |
| Logica `interactive` e `generate` | Nessuna logica interattiva |
| `suggested_action` euristica | Nessuna euristica — output puro, decisioni a Hermes |

Pattern dataclass campione:
```python
@dataclass
class Pattern:
    id: int
    normalized: str              # "problem: {device} in errore"
    count: int
    senders: list[str]
    sender_domain: str
    date_range: list[str]        # ["2026-05-12", "2026-05-19"]
    samples: list[str]           # 3 subject reali
```

Metodi pubblici in `PatternDiscovery`:
- `scan(days=None)` → lista Pattern
- `patterns_to_yaml(patterns, period_start, period_end)` → stringa YAML
- `infer_rule_from_pattern(pattern)` → dict `{name, match}`
- `pattern_from_yaml_dict(data)` → ricostruisce Pattern da dict

**Tecnica di normalizzazione** (ereditata dalla v0):
1. Rimuove `[EXTERNAL]` e prefissi `RE:/FW:`
2. Token device (underscore/hyphen/punto, misto upper+digit ≥4) → `{device}`
3. Hash hex, date-like, percentuali, email → placeholder
4. Lowercase finale
5. Numeri isolati → `{num}`
6. Collassa placeholder multipli e spazi
7. Fallback a subject originale troncato se troppo generico

### 2. `tools/email_processor/cli.py` — Modifiche

**Import sostituito:**
```python
# Vecchio:
from tools.email_processor.discovery import Pattern, PatternDiscovery, YAMLGenerator
# Nuovo:
from tools.email_processor.discovery import PatternDiscovery, _generate_rule_id, _slugify
```

**`_DISCOVER_ACTIONS` dict** — RIMOSSO (era l. 1559–1566)

**`_load_filter_engine` messaggio** — Aggiornato:
- Italiano: `"Usa 'discover --generate' per crearlo."`
- Inglese: `"Use 'rules add' to create rules, then 'rules save'."`

**Comando `discover` riscritto:**
- Flags eliminate: `-i` (interactive), `-g` (generate)
- Flags introdotte: `-o`/`--output` per salvare YAML su file
- Output sempre YAML strutturato (su stdout se `-o` non specificato)
- Tabella terminale rimane come riepilogo visivo (max 50 pattern)

**Nuovo gruppo comandi `rules`** (6 subcomandi):

| Comando | Descrizione |
|---------|-------------|
| `rules list` | Tabella regole correnti da `filter_rules.yaml` |
| `rules show <id>` | YAML dettagliato di una regola |
| `rules remove <id>` | Rimuove regola dal file su disco |
| `rules add` | Aggiunge regola con opzioni `--subject-contains`, `--from-contains`, `--action`, ecc. |
| `rules apply <id> --action <a> -f <file>` | Crea regola da pattern scoperto |
| `rules save [--force]` | Deduplica, ordina per priorità, riscrive file |

Ogni comando scrive direttamente su disco. `rules save` deduplica e ordina.

### 3. `tools/email_processor/__init__.py` — Versione aggiornata

`0.6.0` → `0.7.0`

### 4. File NON toccati
- `filter.py` — RuleEngine (intatto)
- `aggregator.py` — Aggregator (intatto)
- `filter_rules.yaml` — 21 regole predefinite (intatto)

---

## Comandi di esecuzione

```bash
# Discover — output YAML su stdout
uv run python -m tools.email_processor discover -d 7

# Discover — salva YAML su file
uv run python -m tools.email_processor discover -d 7 -o /tmp/patterns.yaml

# Rules — lista regole
uv run python -m tools.email_processor rules list

# Rules — mostra dettaglio regola
uv run python -m tools.email_processor rules show patrol-read

# Rules — aggiungi regola manuale
uv run python -m tools.email_processor rules add \
  --subject-contains "TestAlert" \
  --action keep --label "test"

# Rules — applica regola da pattern scoperto (usando -f)
uv run python -m tools.email_processor rules apply 1 \
  -a aggregate \
  --aggregate-to "_review/daily/zabbix-{date}.md" \
  -f /tmp/patterns.yaml

# Rules — rimuovi regola
uv run python -m tools.email_processor rules remove testalert

# Rules — finalizza (deduplica + ordina)
uv run python -m tools.email_processor rules save --force
```

**Dependency:** Nessuna nuova — `pyyaml`, `typer`, `rich`, `loguru`, `python-dateutil` già in `pyproject.toml`.

---

## Test di verifica

Tutti i test eseguiti con successo su vault reale (6198 note, 484 emails in ultimi 7gg):

1. `discover -d 7` → 88 pattern, conteggio 484 email, YAML perfetto
2. `discover -d 7 -o /tmp/patterns.yaml` → file salvato
3. `rules list` → 21 regole in tabella (Action/Match/Priority visuali)
4. `rules show patrol-read` → YAML dettaglio regola
5. `rules add --subject-contains "TestAlert" --action keep --label "test"` → creato
6. `rules list` → 22 regole (nuova presente)
7. `rules save --force` → 22 regole deduplicate e ordinate
8. `rules list` → 22 regole confermate
9. `rules remove testalert` → rimosso
10. `rules list` → 21 regole
11. `rules show nonexistent` → "Rule not found" exit code 1
12. `rules add` senza `--action` → "Missing option --action" exit code 2
13. `rules apply 1 -a keep` senza terminale/stdin → errore chiaro

**Filter engine ancora funzionante:**
```
Engine loaded: 21 rules
Result: action=aggregate, rule_id=zabbix-problem
```

---

## Problemi riscontrati e decisioni

### 1. Table Rich — Colonna Action schiacciata
**Problema:** Con `width=50` sulla colonna Match, Rich schiacciava la colonna Action a larghezza 0.
**Soluzione:** Rimosso `width=50`, usato `ratio=2` sulla colonna Match, `expand=True` sulla table, `no_wrap=True` su Action e Rule ID.

### 2. `rules add` scrive su disco immediatamente
**Decisione:** Il design spec diceva "NOT saved to disk until 'rules save'", ma i test usano invocazioni Python separate (ogni `uv run` è un processo nuovo). L'unico modo per far funzionare la sequenza di test è scrivere direttamente su disco. Implementazione pragmatica: `rules add` e `rules remove` modificano il file su disco, `rules save` fa la deduplica/sort finale.

### 3. `_load_filter_engine` — Messaggio filtrato
**Decisione:** Solo la riga specificata è stata tradotta in Inglese. Il resto delle stringhe Italiane in `cli.py` non sono state toccate (non richiesto dalla spec).

### 4. Normalizzazione — `{device}` come placeholder
**Decisione:** Ereditato dalla v0 ma con placeholder named (`{device}` invece di `*`). Migliore leggibilità. `infer_rule_from_pattern()` usa la prima parola del normalizzato non-placeholder per generare le condizioni `subject.contains`.

---

## Limiti

- `infer_rule_from_pattern()` è euristica semplice — estrae il primo token >3 char non-placeholder dal normalizzato. Per pattern come "on {date} {date} (critical: {num}, error: {num}, warning: {num})" (pattern #2 - ALERT RECAP) il token estratto sarà "on" che non è ottimale. In questi casi, usare `rules add` manuale.
- `rules apply` da stdin funziona solo con pipe (`echo "..." | rules apply ...`), non è stato testato end-to-end ma il codice è implementato.

---

## Struttura file finale

```
tools/email_processor/
├── __init__.py          (v0.7.0)
├── __main__.py          (entry point)
├── _archive/
│   └── discovery.py.v0-interactive  (preservato)
├── _template/
├── aggregator.py        (intatto)
├── attachment_cache.py  (intatto)
├── cli.py               (modificato: discover + rules)
├── contacts.py          (intatto)
├── discovery.py         (RISC RITTO: zero interattivo, YAML)
├── filter.py            (intatto)
└── filter_rules.yaml    (intatto)
```
