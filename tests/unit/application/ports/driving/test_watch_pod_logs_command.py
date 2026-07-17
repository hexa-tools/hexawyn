from __future__ import annotations

from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_command import (
    WatchPodLogsCommand,
)


class TestWatchPodLogsCommand:
    def test_defaults(self) -> None:
        cmd = WatchPodLogsCommand(pod_name="payment-service-7f9b", namespace="prod")
        assert cmd.timeout_seconds == 300
        assert cmd.max_reconnect_attempts == 3
        assert cmd.sample_rate == 100

    def test_explicit_values(self) -> None:
        cmd = WatchPodLogsCommand(
            pod_name="p", namespace="ns", timeout_seconds=10, max_reconnect_attempts=1
        )
        assert cmd.timeout_seconds == 10
        assert cmd.max_reconnect_attempts == 1
