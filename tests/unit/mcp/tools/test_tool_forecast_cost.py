"""Unit tests for MCP tool: forecast_cost."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestForecastCostTool:
    def test_forecast_cost_returns_dict(self) -> None:
        from hexawyn.mcp.tools.forecast_cost import forecast_cost

        with patch("hexawyn.mcp.server.build_cost_forecast_adapter", return_value=MagicMock()):
            result = forecast_cost()

        assert isinstance(result, dict)
        assert "error" in result

    def test_forecast_cost_handles_error(self) -> None:
        from hexawyn.mcp.tools.forecast_cost import forecast_cost

        with patch(
            "hexawyn.mcp.server.build_cost_forecast_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = forecast_cost()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_forecast_cost_success_path(self) -> None:
        from hexawyn.mcp.tools.forecast_cost import forecast_cost

        mock_driver = MagicMock()
        mock_driver.name = "test-pod"
        mock_driver.kind = "Pod"
        mock_driver.monthly_cost_usd = 100.0
        mock_driver.percentage = 25.0
        mock_forecast = MagicMock()
        mock_forecast.cluster_name = "test-cluster"
        mock_forecast.month = "2024-01"
        mock_forecast.days_elapsed = 15
        mock_forecast.days_remaining = 16
        mock_forecast.current_spend_usd = 500.0
        mock_forecast.projected_total_usd = 1000.0
        mock_forecast.previous_month_usd = 900.0
        mock_forecast.month_over_month_delta = 11.1
        mock_forecast.trend_factor = 1.1
        mock_forecast.top_cost_drivers = [mock_driver]
        mock_forecast.forecast_confidence = "medium"
        mock_forecast.historical_days_used = 7
        mock_forecast.data_source = "prometheus"
        mock_response = MagicMock()
        mock_response.forecast = mock_forecast
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_cost_forecast_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.forecast_cost.ForecastCostUseCase",
                return_value=mock_uc,
            ),
        ):
            result = forecast_cost()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.forecast_cost")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
