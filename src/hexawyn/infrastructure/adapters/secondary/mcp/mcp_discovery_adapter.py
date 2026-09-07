import asyncio

from hexawyn.application.ports.driven.mcp_discovery_port import MCPDiscoveryPort
from hexawyn.domain.models.mcp_tool import MCPToolRegistry, MCPToolSchema
from hexawyn.mcp.server import mcp


class MCPDiscoveryAdapter(MCPDiscoveryPort):
    """Discovers MCP tools from the local FastMCP server instance."""

    def __init__(self) -> None:
        self._cached: MCPToolRegistry | None = None

    def discover(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached
