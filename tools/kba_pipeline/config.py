"""
Configurazione centralizzata per il tool kba_pipeline.

Tutti i path sono relativi alla root del progetto PKM.
"""

from __future__ import annotations

from pathlib import Path

# ---------------------------------------------------------------------------
# Root del progetto — tre livelli su rispetto a tools/kba_pipeline/
# ---------------------------------------------------------------------------
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent.parent

# ---------------------------------------------------------------------------
# Path dei documenti Markdown convertiti
# ---------------------------------------------------------------------------
DOCUMENTS_DIR: Path = PROJECT_ROOT / "Library" / "documents"

# ---------------------------------------------------------------------------
# Path dei record del catalogo KBA
# ---------------------------------------------------------------------------
RECORDS_DIR: Path = PROJECT_ROOT / "Library" / "data" / "kba_catalog" / "records"

# ---------------------------------------------------------------------------
# Path della cartella batch (file batch prodotti dallo step 2)
# ---------------------------------------------------------------------------
BATCH_DIR: Path = PROJECT_ROOT / "Library" / "Fucina" / "Handoff" / "kba_batch"

# ---------------------------------------------------------------------------
# Prompt per l'analisi AI dei documenti KBA
# ---------------------------------------------------------------------------
PROMPT_ANALYZE: Path = PROJECT_ROOT / "Team" / "Prompts" / "kba" / "analisi-rischio-kba.md"

# ---------------------------------------------------------------------------
# File di log del pipeline
# ---------------------------------------------------------------------------
LOG_FILE: Path = PROJECT_ROOT / "Library" / "data" / "kba_pipeline.log"
