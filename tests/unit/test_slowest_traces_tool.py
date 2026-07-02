from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort
from hexawyn.domain.models.slowest_traces import SlowTrace


class TestSlowestTracesTool:
    def test_returns_top_n(self) -> None:
        from hexawyn.mcp.tools.slowest_traces import slowest_traces

        with patch("hexawyn.mcp.server.build_slow_trace_search_adapter") as m:
            a = MagicMock(spec=SlowTraceSearchPort)
            a.search_pod_traces.return_value = [
                SlowTrace(
                    trace_id="tr003", duration_ms=2100.0, operation="GET /cart", span_count=15
                ),
                SlowTrace(
                    trace_id="tr001", duration_ms=4200.0, operation="POST /checkout", span_count=42
                ),
            ]
            m.return_value = a
            r = slowest_traces(pod_name="checkout-7d")
        assert r["error"] is None
        assert len(r["slowest_traces"]) == 2
        assert r["slowest_traces"][0]["trace_id"] == "tr001"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.slowest_traces import slowest_traces

        with patch(
            "hexawyn.mcp.server.build_slow_trace_search_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = slowest_traces(pod_name="x")
        assert r["error"] == "boom"


class TestBuildSlowTraceSearchAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.slow_trace_search_port import (
            SlowTraceSearchPort,
        )
        from hexawyn.mcp.server import build_slow_trace_search_adapter

        assert isinstance(build_slow_trace_search_adapter(), SlowTraceSearchPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.slowest_traces")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
