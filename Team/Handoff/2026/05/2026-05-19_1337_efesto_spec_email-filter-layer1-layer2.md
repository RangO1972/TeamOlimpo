---
data: 2026-05-19
timestamp: 2026-05-19T13:37:00
agent: efesto
task_id: T-052
invocation: 1
type: spec
status: completed
priority: high
title: "Filtro intelligente email_processor — Layer 1 & 2"
completion_notes: >
  Implementati Layer 1 (Discovery Tool) e Layer 2 (Runtime Engine) del
  filtro intelligente per email_processor. Nessuna modifica a file
  esistenti oltre cli.py e __init__.py. Il filter_rules.yaml esistente
  (con 21 regole predefinite) non viene sovrascritto da --generate senza
  conferma.
output_refs:
  - tools/email_processor/discovery.py
  - tools/email_processor/filter.py
  - tools/email_processor/aggregator.py
  - tools/email_processor/filter_rules.yaml
  - tools/email_processor/cli.py
  - tools/email_processor/__init__.py
quality_score: 5
external_review: false
next_action: "Output pronto. Nessuna azione necessaria. Il Layer 3 (Feedback) può essere pianificato in futuro."
---

## Riepilogo implementazione

### File creati (4)

| File | Descrizione |
|---|---|
| `tools/email_processor/discovery.py` | Layer 1 — Discovery Tool. Scansiona note Markdown, normalizza subject, clusterizza per pattern, genera suggerimenti. Include `Pattern`, `PatternDiscovery`, `YAMLGenerator`. |
| `tools/email_processor/filter.py` | Layer 2 — Rule Engine. Carica `filter_rules.yaml`, classifica email con first-match-wins su priorità. Supporta operatori: `contains`, `starts_with`, `ends_with`, `contains_regex`, `not_contains`. Include `RuleEngine`, `ClassificationResult`. |
| `tools/email_processor/aggregator.py` | Layer 2 — Aggregator. Bufferizza email aggregate e scrive riepiloghi giornalieri in `_review/daily/`. Deduplica per device+problema. Include `Aggregator`. |
| `tools/email_processor/filter_rules.yaml` | 21 regole predefinite: 10 discard, 6 aggregate, 5 keep con label. Ordinate per priorità. |

### File modificati (2)

| File | Modifica |
|---|---|
| `tools/email_processor/cli.py` | Aggiunto comando `discover` con flag `--interactive`, `--generate`, `--days`, `--verbose`. Modificata `_run_import()` per integrare filtro e aggregatore nel flusso di import. Aggiunte statistiche filtro nel report finale. |
| `tools/email_processor/__init__.py` | Versione 0.5.0 → 0.6.0 con changelog. |

### Comandi disponibili

```bash
# Discovery — analisi pattern
uv run python -m tools.email_processor discover               # tutto il vault
uv run python -m tools.email_processor discover -d 7           # ultimi 7 giorni
uv run python -m tools.email_processor discover -d 7 -i        # interattivo
uv run python -m tools.email_processor discover -d 7 -g        # genera YAML (chiede conferma se file esiste)

# Import con filtro (automatico se filter_rules.yaml presente)
uv run python -m tools.email_processor import

# Pipeline completa
uv run python -m tools.email_processor pipeline
```

### Risultati test su dati reali (6198 note)

- **Scan 7 giorni**: 484 email → 88 pattern unici
- **Scan 365 giorni**: 6174 email → 698 pattern unici
- **Pattern top**: `mm-*: the integrated nic * port * network link is down.` (417 email)
- **RuleEngine**: 21/21 regole caricate, classificazione funzionante
- **Aggregator**: scrive file in `_review/daily/{tipo}-{date}.md` con deduplica

### Decisioni tecniche

1. **Normalizzazione subject**: applicata su originale (prima del lower()) per catturare device name uppercase, poi lower() per raggruppamento.
2. **Pattern device**: regex larga che matcha token con separatori (underscore, hyphen, dot) o misti uppercase+digit.
3. **--generate sicuro**: non sovrascrive `filter_rules.yaml` senza conferma esplicita.
4. **Filtro opzionale**: se `filter_rules.yaml` non esiste, `_run_import()` funziona come prima (nessuna regressione).
5. **Fallback safe**: email non classificate → `keep` + `flag: unchecked`.

### Limiti noti

- Il clustering per pattern non usa ML — può raggruppare in modo imperfetto subject molto diversi ma con device name simile.
- L'estrazione device/problema nell'aggregator usa pattern heuristici — potrebbe non coprire tutti i formati subject.
- Non implementato Layer 3 (Feedback Loop) — previsto per fase successiva.
