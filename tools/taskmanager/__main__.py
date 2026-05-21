"""Entry point: python -m tools.taskmanager

Starts the taskmanager MCP server on stdio transport.
"""

from tools.taskmanager.server import main_server

main_server()
