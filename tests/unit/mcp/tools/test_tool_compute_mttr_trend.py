"""Unit tests for MCP tool: compute_mttr_trend."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestComputeMttrTrendTool:
    def test_compute_mttr_trend_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compute_mttr_trend import compute_mttr_trend

        mock_result = MagicMock()
        mock_result.trend = "improving"
        mock_result.recommendation = "keep improving"
        mock_result.per_month = {}
        mock_result.slowest_incidents = []
        mock_response = MagicMock()
        mock_response.result = mock_result
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.tools.compute_mttr_trend.ComputeMTTRTrendUseCase",
                return_value=mock_uc,
            ),
            patch("hexawyn.mcp.server.build_mttr_trend_adapter", return_value=MagicMock()),
        ):
            result = compute_mttr_trend()

        assert isinstance(result, dict)
        assert result.get("trend") == "improving"
        assert result.get("error") is None

    def test_compute_mttr_trend_handles_error(self) -> None:
        from hexawyn.mcp.tools.compute_mttr_trend import compute_mttr_trend

        with patch(
            "hexawyn.mcp.server.build_mttr_trend_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = compute_mttr_trend()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("trend") == "error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_mttr_trend")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
