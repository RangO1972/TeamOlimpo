"""
Configurazione centralizzata per il tool kba.indexer.

Tutti i path sono relativi alla root del progetto PKM.
La root viene determinata automaticamente risalendo dal file corrente.
"""

from __future__ import annotations

from pathlib import Path

# ---------------------------------------------------------------------------
# Root del progetto — quattro livelli su rispetto a tools/kba/indexer/
# ---------------------------------------------------------------------------
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent.parent.parent

# ---------------------------------------------------------------------------
# Path del catalogo KBA (gestito da Dike)
# ---------------------------------------------------------------------------
CATALOG_DIR: Path = PROJECT_ROOT / "Library" / "data" / "kba_catalog"
RECORDS_DIR: Path = CATALOG_DIR / "records"
INDEX_FILE: Path = CATALOG_DIR / "index.yaml"

# ---------------------------------------------------------------------------
# Path dei file batch prodotti da tools.consulto
# ---------------------------------------------------------------------------
BATCH_DIR: Path = PROJECT_ROOT / "Library" / "Handoff" / "kba_batch"

# ---------------------------------------------------------------------------
# Path dei documenti Markdown convertiti da tools.pdf_converter
# ---------------------------------------------------------------------------
DOCUMENTS_DIR: Path = PROJECT_ROOT / "Library" / "documents"

# ---------------------------------------------------------------------------
# Cartella Inbox dell'utente (output finali)
# ---------------------------------------------------------------------------
INBOX_DIR: Path = PROJECT_ROOT / "Library" / "deliverables"

# ---------------------------------------------------------------------------
# File di log
# ---------------------------------------------------------------------------
LOG_FILE: Path = PROJECT_ROOT / "Library" / "data" / "kba_indexer.log"
