"""
Script one-shot: analisi KBA nk-2500-0342 con Dike via Grok.

Workflow:
1. Legge .claude/agents/dike.md, rimuove il frontmatter YAML
2. Legge Library/documents/nk-2500-0342.md come contenuto da analizzare
3. Chiama Grok con system prompt = Dike, user prompt = contenuto KBA
4. Salva l'output in Team/Handoff/grok-dike-nk-2500-0342.md
5. Stampa il contenuto finale
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

# Assicura che il root del progetto sia in sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from loguru import logger

from tools.consulto.providers.grok import GrokProvider


def strip_frontmatter(text: str) -> str:
    """
    Rimuove il frontmatter YAML dal testo.

    Il frontmatter e' il blocco tra i primi due '---' all'inizio del file.

    Args:
        text: Testo completo del file Markdown

    Returns:
        Testo senza il frontmatter iniziale
    """
    pattern = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
    return pattern.sub("", text, count=1)


def main() -> None:
    """Punto di ingresso principale."""
    logger.remove()
    logger.add(sys.stderr, level="INFO", format="{time:HH:mm:ss} | {level} | {message}")

    # Percorsi
    dike_path = ROOT / ".claude" / "agents" / "dike.md"
    kba_path = ROOT / "Library" / "documents" / "nk-2500-0342.md"
    output_path = ROOT / "Team" / "Handoff" / "grok-dike-nk-2500-0342.md"

    # 1. Leggi e prepara il system prompt
    logger.info(f"Lettura system prompt da: {dike_path}")
    raw_dike = dike_path.read_text(encoding="utf-8")
    system_prompt = strip_frontmatter(raw_dike).strip()
    logger.info(f"System prompt: {len(system_prompt)} caratteri (frontmatter rimosso)")

    # 2. Leggi il contenuto KBA
    logger.info(f"Lettura KBA da: {kba_path}")
    kba_content = kba_path.read_text(encoding="utf-8")
    logger.info(f"Contenuto KBA: {len(kba_content)} caratteri")

    # 3. Recupera API key e chiama Grok
    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        raise RuntimeError("Variabile d'ambiente XAI_API_KEY non trovata.")

    logger.info("Inizializzazione GrokProvider...")
    provider = GrokProvider(api_key=api_key)

    logger.info(f"Chiamata a Grok (modello: {provider.default_model})...")
    response = provider.chat(
        prompt=kba_content,
        system=system_prompt,
    )
    logger.info(
        f"Risposta ricevuta in {response.elapsed_seconds:.1f}s — "
        f"token input={response.input_tokens}, output={response.output_tokens}"
    )

    # 4. Salva l'output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(response.text, encoding="utf-8")
    logger.info(f"Output salvato in: {output_path}")

    # 5. Stampa il contenuto completo
    print("\n" + "=" * 80)
    print(f"FILE: {output_path}")
    print("=" * 80 + "\n")
    print(response.text)


if __name__ == "__main__":
    main()
