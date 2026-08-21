"""Hexawyn MCP server over stdio — spawned by coding agents.

`python -m hexawyn.mcp.stdio` exposes the same tool set as the HTTP server
(`python -m hexawyn.mcp.server`) but over the stdio transport, letting coding
agents such as Claude Code spawn the server for each session.
"""

from __future__ import annotations

from hexawyn.mcp.server import mcp


def main() -> None:
    mcp.run()


if __name__ == "__main__":  # pragma: no cover
    main()
