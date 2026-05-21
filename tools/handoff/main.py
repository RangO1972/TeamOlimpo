"""Entry point: python -m tools.handoff

Convenience alias for ``__main__.py`` — kept for backward compatibility with
imports referencing ``tools.handoff.main``.
"""

from tools.handoff.cli import app

app()
