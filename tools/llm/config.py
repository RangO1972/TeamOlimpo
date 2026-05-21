"""
Configurazione centralizzata per il tool llm.

Gestisce:
- Caricamento del file .env dalla root del progetto
- Lettura delle API key dalle variabili d'ambiente
- Costanti (provider default, modelli default, versione)

Le API key NON vengono mai hardcoded qui — vengono lette
esclusivamente da variabili d'ambiente dopo il caricamento di .env.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Root del progetto — due livelli su rispetto a tools/llm/
# ---------------------------------------------------------------------------
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent.parent

# ---------------------------------------------------------------------------
# Caricamento .env
# ---------------------------------------------------------------------------
# python-dotenv non fallisce se .env non esiste — si limita a non caricare nulla.
# Questo e' il comportamento corretto: l'utente potrebbe usare variabili
# d'ambiente dirette senza file .env.
try:
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=PROJECT_ROOT / ".env", override=False)
except ImportError:
    # Se python-dotenv non e' installato, l'errore verra' segnalato
    # quando si tenta di usare una API key mancante.
    pass

# ---------------------------------------------------------------------------
# Costanti operative
# ---------------------------------------------------------------------------

# Provider usato se --provider non viene specificato
DEFAULT_PROVIDER: str = "grok"

# Versione del tool (usata nell'output --verbose)
TOOL_VERSION: str = "0.2.0"

# Nomi delle variabili d'ambiente per le API key
ENV_KEY_GROK: str = "XAI_API_KEY"
ENV_KEY_GEMINI: str = "GEMINI_API_KEY"

# Mappa provider -> variabile d'ambiente attesa
PROVIDER_ENV_KEYS: dict[str, str] = {
    "grok": ENV_KEY_GROK,
    "gemini": ENV_KEY_GEMINI,
}


# ---------------------------------------------------------------------------
# Funzione di recupero API key
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Prezzi noti per modello (aggiornabili a mano)
# Formato: model_id -> (input_usd_per_million, output_usd_per_million)
# ---------------------------------------------------------------------------

KNOWN_PRICES: dict[str, tuple[float, float]] = {
    # xAI / Grok — prezzi aprile 2026
    "grok-4-1-fast-non-reasoning":   (0.20, 0.50),
    "grok-4-1-fast-reasoning":       (0.20, 0.50),
    "grok-4-0709":                   (3.00, 15.00),
    "grok-code-fast-1":              (0.20, 1.50),
    "grok-3":                        (3.00, 15.00),
    "grok-3-mini":                   (0.30, 0.50),
    "grok-4.20-0309-non-reasoning":  (2.00, 6.00),
    "grok-4.20-0309-reasoning":      (2.00, 6.00),
    "grok-4.20-multi-agent-0309":    (2.00, 6.00),
    # Google / Gemini — prezzi aprile 2026
    "gemini-2.5-flash":              (0.15, 0.60),
    "gemini-2.5-flash-lite":         (0.10, 0.40),
    "gemini-2.5-pro":                (1.25, 10.00),
}

# ---------------------------------------------------------------------------
# Directory prompt predefinita
# ---------------------------------------------------------------------------

PROMPTS_DIR: Path = PROJECT_ROOT / "Library" / "Prompts"


def get_api_key(provider: str) -> str:
    """
    Legge e ritorna la API key per il provider specificato.

    La chiave viene cercata nelle variabili d'ambiente (dopo il caricamento
    di .env). Se non trovata, stampa un messaggio di errore esplicativo
    su stderr ed esce con codice 1.

    Args:
        provider: Nome del provider ("grok" o "gemini")

    Returns:
        La API key come stringa non vuota

    Raises:
        SystemExit(1): Se la chiave non e' presente nelle variabili d'ambiente
    """
    env_var = PROVIDER_ENV_KEYS.get(provider)
    if env_var is None:
        print(
            f"Errore: provider '{provider}' non riconosciuto. "
            f"Provider disponibili: {', '.join(PROVIDER_ENV_KEYS)}",
            file=sys.stderr,
        )
        sys.exit(1)

    api_key = os.environ.get(env_var, "").strip()
    if not api_key:
        _print_missing_key_error(provider, env_var)
        sys.exit(1)

    return api_key


def _print_missing_key_error(provider: str, env_var: str) -> None:
    """
    Stampa su stderr un messaggio di errore dettagliato per chiave mancante.

    Args:
        provider: Nome del provider
        env_var: Nome della variabile d'ambiente attesa
    """
    env_file = PROJECT_ROOT / ".env"
    lines = [
        f"Errore: API key per '{provider}' non trovata.",
        f"",
        f"La variabile d'ambiente richiesta e': {env_var}",
        f"",
        f"Come configurarla:",
        f"  1. Crea (o modifica) il file: {env_file}",
        f"  2. Aggiungi la riga:",
        f"         {env_var}=la-tua-chiave-api",
        f"",
    ]

    if provider == "grok":
        lines += [
            "  3. Ottieni la chiave da: https://console.x.ai",
        ]
    elif provider == "gemini":
        lines += [
            "  3. Ottieni la chiave da: https://aistudio.google.com/apikey",
        ]

    lines += [
        "",
        "Nota: il file .env e' escluso da git (.gitignore) — non verra' mai committato.",
    ]

    print("\n".join(lines), file=sys.stderr)
