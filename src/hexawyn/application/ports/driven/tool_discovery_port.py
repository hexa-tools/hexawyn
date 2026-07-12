from abc import ABC, abstractmethod

from hexawyn.domain.models.tool_registry import ToolRegistry


class ToolDiscoveryPort(ABC):
    """Driven port — discovers the MCP tools available in the local installation."""

    @abstractmethod
    def discover(self) -> ToolRegistry: ...
