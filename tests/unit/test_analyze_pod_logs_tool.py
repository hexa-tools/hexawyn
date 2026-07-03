from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.domain.models.analyze_pod_logs import PodLogLine


class TestAnalyzePodLogsTool:
    def test_returns_analysis(self) -> None:
        from hexawyn.mcp.tools.analyze_pod_logs import analyze_pod_logs

        with patch("hexawyn.mcp.server.build_pod_logs_adapter") as build:
            adapter = MagicMock(spec=PodLogsPort)
            adapter.fetch_logs.return_value = [
                PodLogLine(
                    timestamp="T1",
                    level="ERROR",
                    message="connection refused",
                    run_index=0,
                    is_json=False,
                )
                for _ in range(3)
            ]
            build.return_value = adapter

            result = analyze_pod_logs(pod_name="api-gateway-7f9b", namespace="prod")

        assert result["error"] is None
        assert result["pod_name"] == "api-gateway-7f9b"
        assert result["total_lines"] == 3
        assert result["strategy_used"] == "smart_summary"
        assert len(result["connection_refused"]) == 1
        assert len(result["ranked_events"]) == 1
        assert result["ranked_events"][0]["count"] == 3

    def test_returns_hybrid_reduction_metrics(self) -> None:
        from hexawyn.mcp.tools.analyze_pod_logs import analyze_pod_logs

        with patch("hexawyn.mcp.server.build_pod_logs_adapter") as build:
            adapter = MagicMock(spec=PodLogsPort)
            adapter.fetch_logs.return_value = [
                PodLogLine(
                    timestamp="T1",
                    level="ERROR",
                    message="connection refused to redis:6379",
                    run_index=0,
                    is_json=False,
                )
                for _ in range(5000)
            ]
            build.return_value = adapter

            result = analyze_pod_logs(pod_name="mid-pod", namespace="prod")

        assert result["strategy_used"] == "hybrid"
        assert result["token_reduction_percentage"] > 90.0
        assert result["degraded"] is False

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.analyze_pod_logs import analyze_pod_logs

        with patch(
            "hexawyn.mcp.server.build_pod_logs_adapter",
            side_effect=RuntimeError("Pod 'ghost' not found in namespace 'prod'"),
        ):
            result = analyze_pod_logs(pod_name="ghost", namespace="prod")

        assert result["error"] == "Pod 'ghost' not found in namespace 'prod'"


class TestBuildPodLogsAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.mcp.server import build_pod_logs_adapter

        assert isinstance(build_pod_logs_adapter(), PodLogsPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.analyze_pod_logs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
