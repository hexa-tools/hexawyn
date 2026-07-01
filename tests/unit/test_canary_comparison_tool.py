from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.canary_comparison_port import CanaryComparisonPort
from hexawyn.domain.models.canary_comparison import (
    VersionMetrics,
)


class TestCanaryComparisonTool:
    def test_returns_regression(self) -> None:
        from hexawyn.mcp.tools.canary_comparison import canary_comparison

        with patch("hexawyn.mcp.server.build_canary_comparison_adapter") as m:
            a = MagicMock(spec=CanaryComparisonPort)
            a.fetch_stable_metrics.return_value = VersionMetrics(
                version="v2.3",
                request_count=9500,
                p50_ms=10.0,
                p95_ms=150.0,
                p99_ms=210.0,
                error_rate_pct=0.1,
            )
            a.fetch_canary_metrics.return_value = VersionMetrics(
                version="v2.4",
                request_count=500,
                p50_ms=15.0,
                p95_ms=380.0,
                p99_ms=480.0,
                error_rate_pct=2.1,
            )
            m.return_value = a
            r = canary_comparison(service_name="order-service")
        assert r["error"] is None
        assert r["verdict"] == "regression"
        assert r["confidence"] == "medium"
        assert r["p99_delta_pct"] > 100
        assert r["canary_count"] == 500

    def test_returns_safe(self) -> None:
        from hexawyn.mcp.tools.canary_comparison import canary_comparison

        with patch("hexawyn.mcp.server.build_canary_comparison_adapter") as m:
            a = MagicMock(spec=CanaryComparisonPort)
            a.fetch_stable_metrics.return_value = VersionMetrics(
                version="v2.3",
                request_count=9500,
                p50_ms=10.0,
                p95_ms=150.0,
                p99_ms=210.0,
                error_rate_pct=0.1,
            )
            a.fetch_canary_metrics.return_value = VersionMetrics(
                version="v2.4",
                request_count=8000,
                p50_ms=9.0,
                p95_ms=145.0,
                p99_ms=205.0,
                error_rate_pct=0.1,
            )
            m.return_value = a
            r = canary_comparison(service_name="order-service", traffic_split_pct=50.0)
        assert r["verdict"] == "safe"
        assert r["confidence"] == "high"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.canary_comparison import canary_comparison

        with patch(
            "hexawyn.mcp.server.build_canary_comparison_adapter", side_effect=RuntimeError("boom")
        ):
            r = canary_comparison(service_name="x")
        assert r["error"] == "boom"


class TestBuildCanaryComparisonAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.canary_comparison_port import (
            CanaryComparisonPort,
        )
        from hexawyn.mcp.server import build_canary_comparison_adapter

        assert isinstance(build_canary_comparison_adapter(), CanaryComparisonPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.canary_comparison")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
