from unittest.mock import AsyncMock, MagicMock, patch

from hexawyn.adapters.secondary.mcp.mcp_discovery_adapter import MCPDiscoveryAdapter
from hexawyn.application.ports.driven.mcp_discovery_port import MCPDiscoveryPort


class TestMCPDiscoveryAdapter:
    def test_implements_port(self) -> None:
        adapter = MCPDiscoveryAdapter()
        assert isinstance(adapter, MCPDiscoveryPort)

    def test_discover_returns_tool_registry(self) -> None:
        mock_tool = MagicMock()
        mock_tool.name = "list_namespaces"
        mock_tool.description = "List namespaces"
        mock_tool.inputSchema = {"type": "object"}

        with patch(
            "hexawyn.adapters.secondary.mcp.mcp_discovery_adapter.mcp",
            autospec=False,
        ) as mock_mcp:
            mock_mcp.list_tools = AsyncMock(return_value=[mock_tool])
            adapter = MCPDiscoveryAdapter()
            registry = adapter.discover()

        assert len(registry.tools) == 1
        tool = registry.tools[0]
        assert tool.name == "list_namespaces"

    def test_discover_caches_result(self) -> None:
        mock_tool = MagicMock()
        mock_tool.name = "health"
        mock_tool.description = "Health check"
        mock_tool.inputSchema = {}

        with patch(
            "hexawyn.adapters.secondary.mcp.mcp_discovery_adapter.mcp",
            autospec=False,
        ) as mock_mcp:
            mock_mcp.list_tools = AsyncMock(return_value=[mock_tool])
            adapter = MCPDiscoveryAdapter()

            first = adapter.discover()
            second = adapter.discover()

        assert first is second
        mock_mcp.list_tools.assert_called_once()

    def test_discover_handles_mcp_unavailable(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.mcp.mcp_discovery_adapter.mcp",
            autospec=False,
        ) as mock_mcp:
            mock_mcp.list_tools = AsyncMock(side_effect=Exception("down"))
            adapter = MCPDiscoveryAdapter()
            registry = adapter.discover()

        assert registry.tools == []

    def test_discover_empty_tools_list(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.mcp.mcp_discovery_adapter.mcp",
            autospec=False,
        ) as mock_mcp:
            mock_mcp.list_tools = AsyncMock(return_value=[])
            adapter = MCPDiscoveryAdapter()
            registry = adapter.discover()

        assert registry.tools == []
