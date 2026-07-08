from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort
from hexawyn.domain.models.cost_profiling import EndpointCPUProfile


class TestCostProfilingTool:
    def test_returns_ranking(self) -> None:
        from hexawyn.mcp.tools.cost_profiling import cost_profiling

        with patch("hexawyn.mcp.server.build_cost_profiling_adapter") as m:
            a = MagicMock(spec=CostProfilingPort)
            a.fetch_endpoint_cpu_metrics.return_value = [
                EndpointCPUProfile(
                    endpoint="POST /generate-report",
                    avg_cpu_ms_per_request=450.0,
                    request_count=200,
                    total_cpu_ms=90000.0,
                ),
                EndpointCPUProfile(
                    endpoint="POST /search",
                    avg_cpu_ms_per_request=180.0,
                    request_count=1500,
                    total_cpu_ms=270000.0,
                ),
                EndpointCPUProfile(
                    endpoint="GET /status",
                    avg_cpu_ms_per_request=2.0,
                    request_count=10000,
                    total_cpu_ms=20000.0,
                ),
            ]
            m.return_value = a
            r = cost_profiling(time_window_minutes=60, top_n=5)
        assert r["error"] is None
        assert len(r["ranked_endpoints"]) == 3
        assert r["ranked_endpoints"][0]["endpoint"] == "POST /search"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.cost_profiling import cost_profiling

        with patch(
            "hexawyn.mcp.server.build_cost_profiling_adapter", side_effect=RuntimeError("boom")
        ):
            r = cost_profiling()
        assert r["error"] == "boom"


class TestBuildCostProfilingAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort
        from hexawyn.mcp.server import build_cost_profiling_adapter

        assert isinstance(build_cost_profiling_adapter(), CostProfilingPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.cost_profiling")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
