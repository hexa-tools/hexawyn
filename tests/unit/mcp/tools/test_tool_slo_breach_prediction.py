"""Unit tests for MCP tool: slo_breach_prediction."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestSloBreachPredictionTool:
    def test_slo_breach_prediction_returns_dict(self) -> None:
        from hexawyn.mcp.tools.slo_breach_prediction import slo_breach_prediction

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_slo_breach_prediction_adapter", return_value=MagicMock()
            ),
        ):
            result = slo_breach_prediction()

        assert isinstance(result, dict)

    def test_slo_breach_prediction_handles_error(self) -> None:
        from hexawyn.mcp.tools.slo_breach_prediction import slo_breach_prediction

        with (
            patch(
                "hexawyn.mcp.server.build_slo_breach_prediction_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = slo_breach_prediction()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.slo_breach_prediction")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
