from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.metric_correlation_port import MetricCorrelationPort
from hexawyn.domain.models.metric_correlation import TimeSeries


class TestMetricCorrelationTool:
    def test_returns_correlated(self) -> None:
        from hexawyn.mcp.tools.metric_correlation import metric_correlation

        with patch("hexawyn.mcp.server.build_metric_correlation_adapter") as m:
            a = MagicMock(spec=MetricCorrelationPort)
            a.fetch_primary_series.return_value = TimeSeries(
                label="api-gateway-5xx",
                data_points=[0.01, 0.01, 0.45, 0.82, 0.91, 0.30, 0.02],
            )
            a.fetch_correlated_series.return_value = TimeSeries(
                label="auth-latency",
                data_points=[80.0, 85.0, 320.0, 750.0, 820.0, 410.0, 90.0],
            )
            m.return_value = a
            r = metric_correlation(primary_service="api-gateway", correlated_service="auth-service")
        assert r["error"] is None
        assert r["status"] == "correlated"
        assert r["coefficient"] > 0.9

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.metric_correlation import metric_correlation

        with patch(
            "hexawyn.mcp.server.build_metric_correlation_adapter", side_effect=RuntimeError("boom")
        ):
            r = metric_correlation(primary_service="a", correlated_service="b")
        assert r["error"] == "boom"


class TestBuildMetricCorrelationAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.metric_correlation_port import (
            MetricCorrelationPort,
        )
        from hexawyn.mcp.server import build_metric_correlation_adapter

        assert isinstance(build_metric_correlation_adapter(), MetricCorrelationPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.metric_correlation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
