"""Entry point for ``python tools/knowledge_base/main.py``.

Registers the module so it can also be run as::

    python -m tools.knowledge_base.main
"""

from tools.knowledge_base.server import main_server

if __name__ == "__main__":
    main_server()
