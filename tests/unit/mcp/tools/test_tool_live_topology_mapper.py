"""Unit tests for MCP tool: live_topology_mapper."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestLiveTopologyMapperTool:
    def test_live_topology_mapper_returns_dict(self) -> None:
        from hexawyn.mcp.tools.live_topology_mapper import live_topology_mapper

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_istio_topology_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_kubernetes_topology_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_topology_snapshot_adapter", return_value=MagicMock()),
        ):
            result = live_topology_mapper()

        assert isinstance(result, dict)

    def test_live_topology_mapper_handles_error(self) -> None:
        from hexawyn.mcp.tools.live_topology_mapper import live_topology_mapper

        with (
            patch(
                "hexawyn.mcp.server.build_istio_topology_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_kubernetes_topology_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_topology_snapshot_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = live_topology_mapper()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.live_topology_mapper")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
