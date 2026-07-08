from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.domain.models.analyze_pod_logs import PodLogLine


def _line(minute: str, message: str = "heartbeat ok") -> PodLogLine:
    return PodLogLine(
        timestamp=f"2024-01-01T09:{minute}:00Z",
        level="INFO",
        message=message,
        run_index=0,
        is_json=False,
    )


class TestDetectLogAnomaliesTool:
    def test_returns_no_anomalies_for_normal_logs(self) -> None:
        from hexawyn.mcp.tools.detect_log_anomalies import detect_log_anomalies

        with patch("hexawyn.mcp.server.build_pod_logs_adapter") as build:
            adapter = MagicMock(spec=PodLogsPort)
            adapter.fetch_logs.return_value = [
                _line(f"{m:02d}") for m in range(20) for _ in range(5)
            ]
            build.return_value = adapter

            result = detect_log_anomalies(pod_name="inventory-service", namespace="prod")

        assert result["error"] is None
        assert result["pod_name"] == "inventory-service"
        assert result["total_lines"] == 100
        assert result["summary"] == "no anomalies detected"
        assert result["anomalies"] == []

    def test_returns_insufficient_data_warning(self) -> None:
        from hexawyn.mcp.tools.detect_log_anomalies import detect_log_anomalies

        with patch("hexawyn.mcp.server.build_pod_logs_adapter") as build:
            adapter = MagicMock(spec=PodLogsPort)
            adapter.fetch_logs.return_value = [_line("00") for _ in range(42)]
            build.return_value = adapter

            result = detect_log_anomalies(pod_name="inventory-service", namespace="prod")

        assert result["insufficient_data"] is True
        assert result["summary"] == "insufficient data for statistical analysis"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_log_anomalies import detect_log_anomalies

        with patch(
            "hexawyn.mcp.server.build_pod_logs_adapter",
            side_effect=RuntimeError("Pod 'ghost' not found in namespace 'prod'"),
        ):
            result = detect_log_anomalies(pod_name="ghost", namespace="prod")

        assert result["error"] == "Pod 'ghost' not found in namespace 'prod'"


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_log_anomalies")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
