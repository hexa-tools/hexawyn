from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
from hexawyn.domain.models.latency_diagnostic import TraceSpan


class TestLatencyDiagnosticTool:
    def test_returns_bottleneck(self) -> None:
        from hexawyn.mcp.tools.latency_diagnostic import latency_diagnostic

        with patch("hexawyn.mcp.server.build_trace_query_adapter") as m:
            a = MagicMock(spec=TraceQueryPort)
            a.fetch_slow_spans.return_value = [
                [
                    TraceSpan(trace_id="abc", span_name="postgres.query", duration_ms=580.0),
                    TraceSpan(trace_id="abc", span_name="redis.get", duration_ms=12.0),
                ],
                [
                    TraceSpan(trace_id="def", span_name="postgres.query", duration_ms=520.0),
                ],
            ]
            a.fetch_total_traces.return_value = 1500
            m.return_value = a
            r = latency_diagnostic(service_name="payment-api")
        assert r["error"] is None
        assert r["slow_trace_count"] == 2
        assert len(r["bottlenecks"]) >= 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.latency_diagnostic import latency_diagnostic

        with patch(
            "hexawyn.mcp.server.build_trace_query_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = latency_diagnostic(service_name="x")
        assert r["error"] == "boom"


class TestBuildTraceQueryAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
        from hexawyn.mcp.server import build_trace_query_adapter

        assert isinstance(build_trace_query_adapter(), TraceQueryPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.latency_diagnostic")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
