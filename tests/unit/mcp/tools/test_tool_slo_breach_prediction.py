"""Unit tests for MCP tool: slo_breach_prediction."""

from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch


class TestSloBreachPredictionTool:
    def _mock_imports(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.workloads.slo_breach_prediction.slo_breach_prediction_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.workloads.slo_breach_prediction.command"] = (
            MagicMock()
        )

    def test_slo_breach_prediction_returns_dict(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.slo_breach_prediction import slo_breach_prediction

        with patch(
            "hexawyn.mcp.server.build_slo_breach_prediction_adapter",
            return_value=MagicMock(),
        ):
            result = slo_breach_prediction()

        assert isinstance(result, dict)
        assert "error" in result

    def test_slo_breach_prediction_handles_error(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.slo_breach_prediction import slo_breach_prediction

        with patch(
            "hexawyn.mcp.server.build_slo_breach_prediction_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = slo_breach_prediction()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        self._mock_imports()
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.slo_breach_prediction")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
