"""
Analisi KBA nk-2500-0342 con Dike via Gemini.

Prova i modelli in ordine:
  1. gemini-2.5-pro-preview-03-25
  2. gemini-2.5-pro
  3. gemini-2.5-flash

Output: Team/Handoff/gemini-dike-nk-2500-0342.md
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from loguru import logger

from tools.consulto.providers.gemini import GeminiProvider

MODELS_TO_TRY = [
    "gemini-2.5-pro-preview-03-25",
    "gemini-2.5-pro",
    "gemini-2.5-flash",
]


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
    output_path = ROOT / "Team" / "Handoff" / "gemini-dike-nk-2500-0342.md"

    logger.info(f"Lettura system prompt da: {dike_path}")
    raw_dike = dike_path.read_text(encoding="utf-8")
    system_prompt = strip_frontmatter(raw_dike).strip()
    logger.info(f"System prompt: {len(system_prompt)} caratteri")

    logger.info(f"Lettura KBA da: {kba_path}")
    kba_content = kba_path.read_text(encoding="utf-8")
    logger.info(f"Contenuto KBA: {len(kba_content)} caratteri")

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Variabile d'ambiente GEMINI_API_KEY non trovata.")

    logger.info("Inizializzazione GeminiProvider...")
    provider = GeminiProvider(api_key=api_key)

    response = None
    used_model = None
    for model in MODELS_TO_TRY:
        logger.info(f"Tentativo con modello: {model}...")
        try:
            response = provider.chat(
                prompt=kba_content,
                system=system_prompt,
                model=model,
            )
            used_model = model
            logger.info(
                f"Risposta ricevuta da {model} in {response.elapsed_seconds:.1f}s — "
                f"token input={response.input_tokens}, output={response.output_tokens}"
            )
            break
        except RuntimeError as exc:
            logger.warning(f"Modello {model} fallito: {exc}. Provo il successivo...")

    if response is None:
        raise RuntimeError(f"Tutti i modelli Gemini hanno fallito: {MODELS_TO_TRY}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(response.text, encoding="utf-8")
    logger.info(f"Output salvato in: {output_path} (modello: {used_model})")

    print("\n" + "=" * 80)
    print(f"FILE: {output_path}")
    print(f"MODELLO USATO: {used_model}")
    print("=" * 80 + "\n")
    print(response.text)


if __name__ == "__main__":
    main()
