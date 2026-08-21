"""Hexawyn MCP stdio launch command — derived from the running interpreter.

Coding agents (Claude Code, ...) spawn the Hexawyn MCP server as a subprocess
over stdio, so the server lifecycle follows the client. The launch command
uses the module entrypoint (python -m) with the interpreter currently running
the `hexa` CLI — `sys.executable` — so it works no matter how the package was
installed (pip, pipx, venv, poetry) or on which operating system.
"""

from __future__ import annotations

import sys

MCP_STDIO_MODULE = "hexawyn.mcp.stdio"


def mcp_stdio_command() -> list[str]:
    return [sys.executable, "-m", MCP_STDIO_MODULE]
