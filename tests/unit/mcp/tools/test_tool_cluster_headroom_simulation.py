"""Unit tests for MCP tool: cluster_headroom_simulation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestClusterHeadroomSimulationTool:
    def test_cluster_headroom_simulation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.cluster_headroom_simulation import cluster_headroom_simulation

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
                return_value=MagicMock(),
            ),
            patch("hexawyn.mcp.server.build_headroom_simulation_adapter", return_value=MagicMock()),
        ):
            result = cluster_headroom_simulation()

        assert isinstance(result, dict)

    def test_cluster_headroom_simulation_handles_error(self) -> None:
        from hexawyn.mcp.tools.cluster_headroom_simulation import cluster_headroom_simulation

        with (
            patch(
                "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_headroom_simulation_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = cluster_headroom_simulation()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.cluster_headroom_simulation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
