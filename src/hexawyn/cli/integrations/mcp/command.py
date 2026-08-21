"""Hexawyn MCP stdio launch command — derived from existing configuration.

Coding agents (Claude Code, ...) spawn the Hexawyn MCP server as a subprocess
over stdio, so the server lifecycle follows the client. The launch command
uses the module entrypoint (python -m) so it works regardless of the
installation location of the hexawyn package.
"""

from __future__ import annotations

MCP_STDIO_MODULE = "hexawyn.mcp.stdio"


def mcp_stdio_command() -> list[str]:
    return ["python", "-m", MCP_STDIO_MODULE]
