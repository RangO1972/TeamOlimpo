"""
Analisi KBA nk-2500-0342 con Dike via Grok reasoning.

Modello: grok-4.20-0309-reasoning
Output: Team/Handoff/grok-reasoning-nk-2500-0342.md
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from loguru import logger

from tools.consulto.providers.grok import GrokProvider

MODEL = "grok-4.20-0309-reasoning"


def strip_frontmatter(text: str) -> str:
    """Rimuove il frontmatter YAML dal testo."""
    pattern = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
    return pattern.sub("", text, count=1)


def main() -> None:
    """Punto di ingresso principale."""
    logger.remove()
    logger.add(sys.stderr, level="INFO", format="{time:HH:mm:ss} | {level} | {message}")

    dike_path = ROOT / ".claude" / "agents" / "dike.md"
    kba_path = ROOT / "Library" / "documents" / "nk-2500-0342.md"
    output_path = ROOT / "Team" / "Handoff" / "grok-reasoning-nk-2500-0342.md"

    logger.info(f"Lettura system prompt da: {dike_path}")
    raw_dike = dike_path.read_text(encoding="utf-8")
    system_prompt = strip_frontmatter(raw_dike).strip()
    logger.info(f"System prompt: {len(system_prompt)} caratteri")

    logger.info(f"Lettura KBA da: {kba_path}")
    kba_content = kba_path.read_text(encoding="utf-8")
    logger.info(f"Contenuto KBA: {len(kba_content)} caratteri")

    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        raise RuntimeError("Variabile d'ambiente XAI_API_KEY non trovata.")

    logger.info("Inizializzazione GrokProvider...")
    provider = GrokProvider(api_key=api_key)

    logger.info(f"Chiamata a Grok con modello: {MODEL}...")
    response = provider.chat(
        prompt=kba_content,
        system=system_prompt,
        model=MODEL,
    )
    logger.info(
        f"Risposta ricevuta in {response.elapsed_seconds:.1f}s — "
        f"token input={response.input_tokens}, output={response.output_tokens}"
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(response.text, encoding="utf-8")
    logger.info(f"Output salvato in: {output_path}")

    print("\n" + "=" * 80)
    print(f"FILE: {output_path}")
    print("=" * 80 + "\n")
    print(response.text)


if __name__ == "__main__":
    main()
