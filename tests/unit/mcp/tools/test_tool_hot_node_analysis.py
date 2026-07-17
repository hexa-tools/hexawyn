"""Unit tests for MCP tool: hot_node_analysis."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestHotNodeAnalysisTool:
    def test_hot_node_analysis_returns_dict(self) -> None:
        from hexawyn.mcp.tools.hot_node_analysis import hot_node_analysis

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
                return_value=MagicMock(),
            ),
            patch("hexawyn.mcp.server.build_node_analysis_adapter", return_value=MagicMock()),
        ):
            result = hot_node_analysis()

        assert isinstance(result, dict)

    def test_hot_node_analysis_handles_error(self) -> None:
        from hexawyn.mcp.tools.hot_node_analysis import hot_node_analysis

        with (
            patch(
                "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_node_analysis_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = hot_node_analysis()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.hot_node_analysis")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
