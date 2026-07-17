from __future__ import annotations

from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_command import (
    AnalyzePodLogsCommand,
)


class TestAnalyzePodLogsCommand:
    def test_defaults(self) -> None:
        cmd = AnalyzePodLogsCommand(pod_name="api-gateway-7f9b", namespace="prod")
        assert cmd.time_window_minutes == 30

    def test_explicit_window(self) -> None:
        cmd = AnalyzePodLogsCommand(
            pod_name="api-gateway-7f9b", namespace="prod", time_window_minutes=60
        )
        assert cmd.time_window_minutes == 60
