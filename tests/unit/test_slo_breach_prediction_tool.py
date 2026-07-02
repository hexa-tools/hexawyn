from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.slo_breach_prediction_port import (
    SLOBreachPredictionPort,
)


class TestSLOBreachPredictionTool:
    def test_returns_risks(self) -> None:
        from hexawyn.mcp.tools.slo_breach_prediction import slo_breach_prediction

        with patch("hexawyn.mcp.server.build_slo_breach_prediction_adapter") as m:
            a = MagicMock(spec=SLOBreachPredictionPort)
            a.fetch_trend_metrics.return_value = [
                {"service": "auth-service", "current_p99": 320.0, "slo": 500.0, "slope": 8.2},
                {"service": "payment-service", "current_p99": 200.0, "slo": 500.0, "slope": 0.0},
            ]
            m.return_value = a
            r = slo_breach_prediction(prediction_window_minutes=60)
        assert r["error"] is None
        assert len(r["at_risk"]) == 1
        assert r["safe_count"] == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.slo_breach_prediction import slo_breach_prediction

        with patch(
            "hexawyn.mcp.server.build_slo_breach_prediction_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = slo_breach_prediction()
        assert r["error"] == "boom"


class TestBuildSLOBreachPredictionAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.slo_breach_prediction_port import (
            SLOBreachPredictionPort,
        )
        from hexawyn.mcp.server import build_slo_breach_prediction_adapter

        assert isinstance(build_slo_breach_prediction_adapter(), SLOBreachPredictionPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.slo_breach_prediction")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
