from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.trace_log_correlation_port import (
    TraceLogCorrelationPort,
)
from hexawyn.domain.models.trace_log_correlation import (
    CorrelatedLog,
    TraceLogSpan,
)


class TestTraceLogCorrelationTool:
    def test_returns_correlation(self) -> None:
        from hexawyn.mcp.tools.trace_log_correlation import trace_log_correlation

        with patch("hexawyn.mcp.server.build_trace_log_correlation_adapter") as m:
            a = MagicMock(spec=TraceLogCorrelationPort)
            a.fetch_error_spans.return_value = [
                TraceLogSpan(
                    span_name="inventory-service.checkStock",
                    error_message="timeout after 1500ms",
                    timestamp="10:32:14.100",
                    trace_id="abc-def-123",
                ),
                TraceLogSpan(
                    span_name="order-service.createOrder",
                    error_message="ValidationException: invalid SKU",
                    timestamp="10:32:15.421",
                    trace_id="abc-def-123",
                ),
            ]
            a.fetch_correlated_logs.return_value = [
                CorrelatedLog(
                    timestamp="10:32:14.100",
                    level="ERROR",
                    message="timeout connecting to postgres",
                ),
                CorrelatedLog(
                    timestamp="10:32:15.421",
                    level="ERROR",
                    message="ValidationException: invalid SKU abc-123",
                ),
            ]
            m.return_value = a
            r = trace_log_correlation(operation="POST /order")
        assert r["error"] is None
        assert r["trace_id"] == "abc-def-123"
        assert r["error_span_count"] == 2
        assert r["correlated_log_count"] == 2

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.trace_log_correlation import trace_log_correlation

        with patch(
            "hexawyn.mcp.server.build_trace_log_correlation_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = trace_log_correlation(operation="POST /x")
        assert r["error"] == "boom"


class TestBuildTraceLogCorrelationAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.trace_log_correlation_port import (
            TraceLogCorrelationPort,
        )
        from hexawyn.mcp.server import build_trace_log_correlation_adapter

        assert isinstance(build_trace_log_correlation_adapter(), TraceLogCorrelationPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.trace_log_correlation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
