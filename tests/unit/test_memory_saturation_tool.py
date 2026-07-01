from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort


class TestMemorySaturationTool:
    def test_returns_critical_pods(self) -> None:
        from hexawyn.mcp.tools.memory_saturation import memory_saturation

        with patch("hexawyn.mcp.server.build_memory_saturation_adapter") as m:
            a = MagicMock(spec=MemorySaturationPort)
            a.fetch_memory_metrics.return_value = [
                {
                    "name": "checkout-pod-abc",
                    "namespace": "production",
                    "current_mb": 850.0,
                    "limit_mb": 1024.0,
                    "growth_rate_mb_per_min": 8.5,
                },
                {
                    "name": "auth-pod",
                    "namespace": "production",
                    "current_mb": 300.0,
                    "limit_mb": 1024.0,
                    "growth_rate_mb_per_min": 0.0,
                },
            ]
            a.correlate_with_otel.return_value = "DB query returning 15MB on each /checkout"
            m.return_value = a
            r = memory_saturation(prediction_window_minutes=30)
        assert r["error"] is None
        assert len(r["critical_pods"]) == 1
        assert r["critical_pods"][0]["pod_name"] == "checkout-pod-abc"
        assert r["critical_pods"][0]["otel_root_cause"] is not None
        assert r["safe_pod_count"] == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.memory_saturation import memory_saturation

        with patch(
            "hexawyn.mcp.server.build_memory_saturation_adapter", side_effect=RuntimeError("boom")
        ):
            r = memory_saturation()
        assert r["error"] == "boom"


class TestBuildMemorySaturationAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort
        from hexawyn.mcp.server import build_memory_saturation_adapter

        assert isinstance(build_memory_saturation_adapter(), MemorySaturationPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.memory_saturation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
