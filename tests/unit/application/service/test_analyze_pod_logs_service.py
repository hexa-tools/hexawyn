from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_command import (
    AnalyzePodLogsCommand,
)
from hexawyn.application.service.analyze_pod_logs_service import AnalyzePodLogsService
from hexawyn.domain.models.analyze_pod_logs import PodLogLine


class TestAnalyzePodLogsService:
    def test_analyze_returns_response_from_domain_computation(self) -> None:
        port = MagicMock(spec=PodLogsPort)
        port.fetch_logs.return_value = [
            PodLogLine(
                timestamp="T1",
                level="ERROR",
                message="connection refused",
                run_index=0,
                is_json=False,
            )
            for _ in range(3)
        ]
        service = AnalyzePodLogsService(port=port)

        response = service.analyze(
            AnalyzePodLogsCommand(pod_name="api-gateway-7f9b", namespace="prod")
        )

        assert response.pod_name == "api-gateway-7f9b"
        assert response.namespace == "prod"
        assert response.total_lines == 3
        assert response.error_count == 3
        assert response.strategy_used == "smart_summary"
        assert len(response.connection_refused) == 1
        assert response.connection_refused[0]["count"] == 3
        assert response.error is None
        assert len(response.ranked_events) == 1
        assert response.ranked_events[0]["count"] == 3

    def test_analyze_passes_time_window_to_port(self) -> None:
        port = MagicMock(spec=PodLogsPort)
        port.fetch_logs.return_value = []
        service = AnalyzePodLogsService(port=port)

        service.analyze(
            AnalyzePodLogsCommand(pod_name="pod-x", namespace="ns", time_window_minutes=60)
        )

        called_request = port.fetch_logs.call_args.args[0]
        assert called_request.time_window_minutes == 60

    def test_analyze_no_anomalies(self) -> None:
        port = MagicMock(spec=PodLogsPort)
        port.fetch_logs.return_value = []
        service = AnalyzePodLogsService(port=port)

        response = service.analyze(AnalyzePodLogsCommand(pod_name="quiet-pod", namespace="prod"))

        assert response.summary == "No anomalies detected"
        assert response.patterns == []

    def test_analyze_propagates_hybrid_reduction_metrics(self) -> None:
        port = MagicMock(spec=PodLogsPort)
        port.fetch_logs.return_value = [
            PodLogLine(
                timestamp="T1",
                level="ERROR",
                message="connection refused to redis:6379",
                run_index=0,
                is_json=False,
            )
            for _ in range(5000)
        ]
        service = AnalyzePodLogsService(port=port)

        response = service.analyze(AnalyzePodLogsCommand(pod_name="mid-pod", namespace="prod"))

        assert response.strategy_used == "hybrid"
        assert response.token_reduction_percentage > 90.0
        assert response.degraded is False

    def test_port_unreachable_propagates(self) -> None:
        import pytest

        port = MagicMock()
        port.fetch_logs.side_effect = RuntimeError("connection refused")
        service = AnalyzePodLogsService(port=port)
        with pytest.raises(RuntimeError, match="connection refused"):
            service.analyze(
                AnalyzePodLogsCommand(pod_name="app", namespace="prod", time_window_minutes=60)
            )


class TestAnalyzePodLogsServiceEdgeCases:
    def test_time_window_zero_boundary(self) -> None:
        port = MagicMock(spec=PodLogsPort)
        port.fetch_logs.return_value = []
        service = AnalyzePodLogsService(port=port)

        response = service.analyze(
            AnalyzePodLogsCommand(pod_name="pod", namespace="ns", time_window_minutes=0)
        )

        assert response.pod_name == "pod"
        assert response.time_window_minutes == 0

    def test_very_long_error_message_handled(self) -> None:
        port = MagicMock(spec=PodLogsPort)
        port.fetch_logs.return_value = [
            PodLogLine(
                timestamp="T1",
                level="ERROR",
                message="err" * 500,
                run_index=0,
                is_json=False,
            )
        ]
        service = AnalyzePodLogsService(port=port)

        response = service.analyze(AnalyzePodLogsCommand(pod_name="verbose-pod", namespace="prod"))

        assert response.pod_name == "verbose-pod"
        assert response.total_lines == 1

    def test_mixed_severity_logs(self) -> None:
        port = MagicMock(spec=PodLogsPort)
        port.fetch_logs.return_value = [
            PodLogLine(timestamp="T1", level="ERROR", message="err", run_index=0, is_json=False),
            PodLogLine(timestamp="T2", level="WARN", message="warn", run_index=0, is_json=False),
            PodLogLine(timestamp="T3", level="INFO", message="info", run_index=0, is_json=False),
        ]
        service = AnalyzePodLogsService(port=port)

        response = service.analyze(AnalyzePodLogsCommand(pod_name="mixed-pod", namespace="prod"))

        assert response.total_lines == 3
        assert response.error_count == 1
        assert response.warning_count == 1
