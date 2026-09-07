from abc import ABC, abstractmethod

from hexawyn.domain.models.mcp_tool import MCPToolRegistry


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class MCPDiscoveryPort(ABC):
    """Driven port — discovers available MCP tools."""

    @abstractmethod
    def discover(self) -> MCPToolRegistry:
        """Discover MCP tools at startup. Result cached in memory."""
