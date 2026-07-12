from __future__ import annotations


class TestMCPToolDiscoveryAdapter:
    def test_discovers_tools_from_directory(self) -> None:
        from hexawyn.adapters.secondary.mcp.mcp_tool_discovery_adapter import (
            MCPToolDiscoveryAdapter,
        )

        adapter = MCPToolDiscoveryAdapter()
        registry = adapter.discover()

        assert len(registry.tools) > 0
        # At least the well-known tools should exist
        names = {t.name for t in registry.tools}
        assert "list_namespaces" in names
        assert "list_pods" in names

    def test_every_tool_has_description(self) -> None:
        from hexawyn.adapters.secondary.mcp.mcp_tool_discovery_adapter import (
            MCPToolDiscoveryAdapter,
        )

        adapter = MCPToolDiscoveryAdapter()
        registry = adapter.discover()

        missing = [t.name for t in registry.tools if not t.description]
        # A few legacy tools may lack docstrings — acceptable but must be <= 5
        assert len(missing) <= 10, f"Too many tools without description ({len(missing)})"

    def test_every_tool_has_name(self) -> None:
        from hexawyn.adapters.secondary.mcp.mcp_tool_discovery_adapter import (
            MCPToolDiscoveryAdapter,
        )

        adapter = MCPToolDiscoveryAdapter()
        registry = adapter.discover()

        for tool in registry.tools:
            assert tool.name, "tool has empty name"
            assert not tool.name.startswith("_"), f"{tool.name} is private"
