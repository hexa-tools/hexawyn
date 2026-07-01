from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
from hexawyn.domain.models.span_bottleneck import SpanBreakdown


class TestSpanBottleneckAnalysisTool:
    def test_returns_db_bottleneck(self) -> None:
        from hexawyn.mcp.tools.span_bottleneck_analysis import span_bottleneck_analysis

        with patch("hexawyn.mcp.server.build_span_bottleneck_adapter") as m:
            a = MagicMock(spec=SpanBottleneckPort)
            a.fetch_db_spans.return_value = SpanBreakdown(
                category="db",
                avg_ms=380.0,
                p95_ms=650.0,
                max_ms=1200.0,
                slowest_operation="SELECT * FROM orders WHERE user_id = ? LIMIT 1000",
            )
            a.fetch_redis_spans.return_value = SpanBreakdown(
                category="redis",
                avg_ms=6.0,
                p95_ms=15.0,
                max_ms=45.0,
                slowest_operation="HGETALL session:user:123",
            )
            m.return_value = a
            r = span_bottleneck_analysis(time_window_minutes=30)
        assert r["error"] is None
        assert r["bottleneck"] == "db"
        assert r["confidence"] == "high"
        assert r["db_slowest"] is not None

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.span_bottleneck_analysis import span_bottleneck_analysis

        with patch(
            "hexawyn.mcp.server.build_span_bottleneck_adapter", side_effect=RuntimeError("boom")
        ):
            r = span_bottleneck_analysis()
        assert r["error"] == "boom"


class TestBuildSpanBottleneckAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
        from hexawyn.mcp.server import build_span_bottleneck_adapter

        assert isinstance(build_span_bottleneck_adapter(), SpanBottleneckPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.span_bottleneck_analysis")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
