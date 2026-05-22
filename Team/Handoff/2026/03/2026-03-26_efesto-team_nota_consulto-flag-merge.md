---
data: 2026-03-26
mittente: efesto
destinatario: team
tipo: nota
stato: completato
priorita: media
titolo: "Tool consulto: aggiunto flag --merge per chiamata API unificata"
processato_da: efesto
processato_il: 2026-03-26
note_completamento: "Flag --merge implementato in batch.py (run_merge) e cli.py. Output: <primo-file>_merged-<provider>.md"
---

# Nota — Tool consulto: flag `--merge`

## Cosa e' stato fatto

Aggiunti due artefatti al tool `tools/llm`:

### `tools/llm/batch.py` — nuova funzione `run_merge()`

Firma:
```python
def run_merge(
    provider: ProviderProtocol,
    provider_name: str,
    template: str,
    input_files: list[Path],
    output_dir: Path | None,
    model: str | None = None,
    system: str | None = None,
) -> int:
```

Logica:
1. Legge tutti i file in `input_files` e li concatena in un unico blocco di testo, separati da `--- <nome-file> ---`.
2. Sostituisce `{{kba_text}}` nel template con il blocco unificato; `{{filename}}` usa lo stem del primo file.
3. Fa **una sola chiamata** `provider.chat()`.
4. Se `output_dir` e' fornita, scrive il risultato in `<output_dir>/<primo_stem>_merged-<provider>.md`.
5. Se `output_dir` e' None, stampa su stdout.
6. Ritorna `0` per successo, `1` per errore (lettura file o API).

### `tools/llm/cli.py` — flag `--merge` e dispatch

- Aggiunto argomento `--merge` (store_true) nel `build_parser()`.
- Nel ramo batch di `main()`, se `args.merge` e' True si chiama `run_merge()` invece di `run_batch()`.
- Il flag `--skip-existing` rimane disponibile solo per `run_batch()` (non ha senso nel caso merge).

## Comportamento verificato (manuale)

| Scenario | Risultato atteso |
|----------|-----------------|
| `--prompt X.md --input A.md B.md --merge` | 1 chiamata API, output `A_merged-grok.md` |
| `--prompt X.md --input A.md B.md` (senza `--merge`) | 2 chiamate API, output `A-grok.json` + `B-grok.json` (comportamento invariato) |
| `--merge` senza `--prompt` | Cade nel normale controllo "Errore: --prompt richiede --input" |

## File modificati

- `C:\Users\dev\Desktop\TeamOlimpo\tools\consulto\batch.py` — aggiunta `run_merge()` sopra `run_batch()`
- `C:\Users\dev\Desktop\TeamOlimpo\tools\consulto\cli.py` — aggiunto flag `--merge`, import `run_merge`, dispatch condizionale

## Note per chi usa il tool

Il nome file di output in modalita' merge e' sempre `.md` (non `.json`), perche' ci si aspetta che il modello produca un testo sintetico libero, non JSON strutturato. Se serve JSON, il template deve richiederlo esplicitamente e il consumatore fa il parse.
