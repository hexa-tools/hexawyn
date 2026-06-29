from abc import ABC, abstractmethod

from hexawyn.domain.models.mcp_tool import MCPToolRegistry


class MCPDiscoveryPort(ABC):
    """Driven port — discovers available MCP tools."""

    @abstractmethod
    def discover(self) -> MCPToolRegistry:
        """Discover MCP tools at startup. Result cached in memory."""
