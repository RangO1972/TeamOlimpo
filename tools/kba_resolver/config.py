"""Costanti di configurazione per kba_resolver."""

from pathlib import Path

# tools/kba_resolver/config.py  →  3 livelli su = PROJECT_ROOT
PROJECT_ROOT: Path = Path(__file__).parent.parent.parent

RECORDS_DIR: Path = PROJECT_ROOT / "Library" / "data" / "kba_catalog" / "records"
DOCUMENTS_DIR: Path = PROJECT_ROOT / "Library" / "documents"
LOG_FILE: Path = PROJECT_ROOT / "Library" / "data" / "kba_resolver.log"
