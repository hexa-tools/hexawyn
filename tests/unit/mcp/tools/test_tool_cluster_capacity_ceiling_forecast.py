"""Unit tests for MCP tool: cluster_capacity_ceiling_forecast."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestClusterCapacityCeilingForecastTool:
    def test_cluster_capacity_ceiling_forecast_returns_dict(self) -> None:
        from hexawyn.mcp.tools.cluster_capacity_ceiling_forecast import (
            cluster_capacity_ceiling_forecast,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_capacity_forecast_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
                return_value=MagicMock(),
            ),
        ):
            result = cluster_capacity_ceiling_forecast()

        assert isinstance(result, dict)

    def test_cluster_capacity_ceiling_forecast_handles_error(self) -> None:
        from hexawyn.mcp.tools.cluster_capacity_ceiling_forecast import (
            cluster_capacity_ceiling_forecast,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_capacity_forecast_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_cluster_resource_metrics_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = cluster_capacity_ceiling_forecast()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.cluster_capacity_ceiling_forecast")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
