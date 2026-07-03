from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPrometheusQueryTool:
    def test_returns_query_results(self) -> None:
        from hexawyn.mcp.tools.prometheus_query import prometheus_query

        with patch("hexawyn.mcp.server.build_metrics_query_adapter") as build_adapter:
            adapter = MagicMock()
            adapter.instant_query.return_value = [
                {"metric": {"pod": "payment-pod-abc", "container": "app"}, "value": 0.0032}
            ]
            build_adapter.return_value = adapter

            result = prometheus_query(
                promql='rate(container_cpu_usage_seconds_total{namespace="payment"}[5m])',
                unit_hint="cores",
            )

        assert result["error"] is None
        assert result["result_count"] == 1
        assert result["results"][0]["formatted_value"] == "3.2m cores"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.prometheus_query import prometheus_query

        with patch(
            "hexawyn.mcp.server.build_metrics_query_adapter",
            side_effect=RuntimeError("Prometheus is unavailable at 'http://prometheus:9090'."),
        ):
            result = prometheus_query(promql="up")

        assert "prometheus:9090" in result["error"]


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.prometheus_query")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
