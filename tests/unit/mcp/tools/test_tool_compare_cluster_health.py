"""Unit tests for MCP tool: compare_cluster_health."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCompareClusterHealthTool:
    def test_compare_cluster_health_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compare_cluster_health import compare_cluster_health

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_fleet_health_adapter", return_value=MagicMock()),
        ):
            result = compare_cluster_health(cluster_a="test", cluster_b="test")

        assert isinstance(result, dict)

    def test_compare_cluster_health_handles_error(self) -> None:
        from hexawyn.mcp.tools.compare_cluster_health import compare_cluster_health

        with (
            patch(
                "hexawyn.mcp.server.build_fleet_health_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = compare_cluster_health(cluster_a="test", cluster_b="test")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compare_cluster_health")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
