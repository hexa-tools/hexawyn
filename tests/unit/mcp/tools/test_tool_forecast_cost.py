"""Unit tests for MCP tool: forecast_cost."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestForecastCostTool:
    def test_forecast_cost_returns_dict(self) -> None:
        from hexawyn.mcp.tools.forecast_cost import forecast_cost

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_cost_forecast_adapter", return_value=MagicMock()),
        ):
            result = forecast_cost()

        assert isinstance(result, dict)

    def test_forecast_cost_handles_error(self) -> None:
        from hexawyn.mcp.tools.forecast_cost import forecast_cost

        with (
            patch(
                "hexawyn.mcp.server.build_cost_forecast_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = forecast_cost()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.forecast_cost")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
