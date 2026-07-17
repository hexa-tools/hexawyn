from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort
from hexawyn.domain.models.p99_latency import LatencyPercentiles


class TestP99LatencyTool:
    def test_returns_percentiles(self) -> None:
        from hexawyn.mcp.tools.p99_latency import p99_latency

        with patch("hexawyn.mcp.server.build_latency_percentile_adapter") as m:
            a = MagicMock(spec=LatencyPercentilePort)
            a.fetch_percentiles.return_value = LatencyPercentiles(
                p50_ms=85.0,
                p95_ms=210.0,
                p99_ms=480.0,
                sample_count=14200,
            )
            m.return_value = a
            r = p99_latency(
                endpoint="/v1/checkout", time_window_minutes=120, slo_threshold_ms=500.0
            )
        assert r["error"] is None
        assert r["p99_ms"] == 480.0
        assert r["slo_status"] == "pass"

    def test_slo_fail(self) -> None:
        from hexawyn.mcp.tools.p99_latency import p99_latency

        with patch("hexawyn.mcp.server.build_latency_percentile_adapter") as m:
            a = MagicMock(spec=LatencyPercentilePort)
            a.fetch_percentiles.return_value = LatencyPercentiles(
                p50_ms=350.0,
                p95_ms=600.0,
                p99_ms=820.0,
                sample_count=10000,
            )
            m.return_value = a
            r = p99_latency(
                endpoint="/v1/checkout", time_window_minutes=120, slo_threshold_ms=500.0
            )
        assert r["slo_status"] == "fail"
        assert r["slo_delta_ms"] == 320.0

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.p99_latency import p99_latency

        with patch(
            "hexawyn.mcp.server.build_latency_percentile_adapter", side_effect=RuntimeError("boom")
        ):
            r = p99_latency(endpoint="/x")
        assert r["error"] == "boom"


class TestBuildLatencyPercentileAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.latency_percentile_port import (
            LatencyPercentilePort,
        )
        from hexawyn.mcp.server import build_latency_percentile_adapter

        assert isinstance(build_latency_percentile_adapter(), LatencyPercentilePort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.p99_latency")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
