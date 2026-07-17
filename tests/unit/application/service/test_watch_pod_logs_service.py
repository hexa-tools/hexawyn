from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.alert_notification_port import AlertNotificationPort
from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort
from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_command import (
    WatchPodLogsCommand,
)
from hexawyn.application.service.watch_pod_logs_service import WatchPodLogsService
from hexawyn.domain.models.analyze_pod_logs import PodLogLine


def _line(message: str, level: str = "INFO", timestamp: str = "T1") -> PodLogLine:
    return PodLogLine(timestamp=timestamp, level=level, message=message, run_index=0, is_json=False)


class TestWatchPodLogsServiceCriticalAlert:
    """TC1: OOM error appears -> alert triggered immediately with context."""

    def test_oom_triggers_alert_with_context(self) -> None:
        watch_port = MagicMock(spec=PodLogWatchPort)
        watch_port.watch.return_value = iter(
            [_line("pod healthy") for _ in range(500)] + [_line("OOMKilled memory limit exceeded")]
        )
        watch_port.pod_exists.return_value = True
        alert_port = MagicMock(spec=AlertNotificationPort)
        alert_port.send_alert.return_value = True

        service = WatchPodLogsService(watch_port=watch_port, alert_port=alert_port)
        response = service.watch(
            WatchPodLogsCommand(pod_name="payment-service-7f9b", namespace="prod")
        )

        assert len(response.alerts) == 1
        alert = response.alerts[0]
        assert alert["category"] == "oom"
        assert alert["pod_name"] == "payment-service-7f9b"
        assert alert["log_line"] == "OOMKilled memory limit exceeded"
        alert_port.send_alert.assert_called_once()
        assert response.lines_observed == 501

    def test_alert_pushed_at_detection_time_not_after_loop(self) -> None:
        """'immediately' -> the push happens as soon as the match is processed."""
        watch_port = MagicMock(spec=PodLogWatchPort)
        watch_port.watch.return_value = iter(
            [_line("OOMKilled memory limit exceeded")] + [_line("pod healthy") for _ in range(10)]
        )
        watch_port.pod_exists.return_value = True
        alert_port = MagicMock(spec=AlertNotificationPort)
        call_order: list[str] = []
        alert_port.send_alert.side_effect = lambda _msg: call_order.append("alert") or True

        service = WatchPodLogsService(watch_port=watch_port, alert_port=alert_port)
        service.watch(WatchPodLogsCommand(pod_name="p", namespace="ns"))

        assert call_order == ["alert"]


class TestWatchPodLogsServiceNoAnomalies:
    """TC2: No critical errors within the timeout -> heartbeat, no alerts."""

    def test_timeout_returns_heartbeat(self) -> None:
        def infinite_healthy_lines() -> object:
            while True:
                yield _line("pod healthy")

        watch_port = MagicMock(spec=PodLogWatchPort)
        watch_port.watch.return_value = infinite_healthy_lines()
        alert_port = MagicMock(spec=AlertNotificationPort)

        service = WatchPodLogsService(watch_port=watch_port, alert_port=alert_port)
        response = service.watch(
            WatchPodLogsCommand(pod_name="p", namespace="ns", timeout_seconds=0)
        )

        assert response.stop_reason == "timeout"
        assert response.alerts == []
        alert_port.send_alert.assert_not_called()


class TestWatchPodLogsServicePodDeleted:
    """TC3: Pod deleted mid-stream -> graceful stop with 'pod_deleted' reason."""

    def test_stream_ends_and_pod_no_longer_exists(self) -> None:
        watch_port = MagicMock(spec=PodLogWatchPort)
        watch_port.watch.return_value = iter([_line("pod healthy") for _ in range(5)])
        watch_port.pod_exists.return_value = False
        alert_port = MagicMock(spec=AlertNotificationPort)

        service = WatchPodLogsService(watch_port=watch_port, alert_port=alert_port)
        response = service.watch(WatchPodLogsCommand(pod_name="p", namespace="ns"))

        assert response.stop_reason == "pod_deleted"

    def test_stream_ends_and_pod_still_exists_is_session_ended(self) -> None:
        watch_port = MagicMock(spec=PodLogWatchPort)
        watch_port.watch.return_value = iter([_line("pod healthy") for _ in range(5)])
        watch_port.pod_exists.return_value = True
        alert_port = MagicMock(spec=AlertNotificationPort)

        service = WatchPodLogsService(watch_port=watch_port, alert_port=alert_port)
        response = service.watch(WatchPodLogsCommand(pod_name="p", namespace="ns"))

        assert response.stop_reason == "session_ended"


class TestWatchPodLogsServiceSamplingAndDedup:
    def test_high_volume_sampling_bounds_memory(self) -> None:
        """Edge case: 10000 lines/second -> sampling applied, no memory overflow."""
        watch_port = MagicMock(spec=PodLogWatchPort)
        watch_port.watch.return_value = iter([_line("pod healthy") for _ in range(50000)])
        watch_port.pod_exists.return_value = True
        alert_port = MagicMock(spec=AlertNotificationPort)

        service = WatchPodLogsService(watch_port=watch_port, alert_port=alert_port)
        response = service.watch(WatchPodLogsCommand(pod_name="p", namespace="ns", sample_rate=100))

        assert response.lines_observed == 50000
        assert response.lines_sampled < 1000

    def test_multiple_criticals_within_a_second_are_deduplicated(self) -> None:
        """Edge case: multiple critical errors in 1 second -> deduplicated, not flooded."""
        watch_port = MagicMock(spec=PodLogWatchPort)
        watch_port.watch.return_value = iter(
            [_line("OOMKilled memory limit exceeded") for _ in range(5)]
        )
        watch_port.pod_exists.return_value = True
        alert_port = MagicMock(spec=AlertNotificationPort)

        service = WatchPodLogsService(watch_port=watch_port, alert_port=alert_port)
        response = service.watch(WatchPodLogsCommand(pod_name="p", namespace="ns"))

        assert len(response.alerts) == 1
        alert_port.send_alert.assert_called_once()

    def test_empty_stream_no_alerts(self) -> None:
        watch_port = MagicMock(
            spec=__import__(
                "hexawyn.application.ports.driven.pod_log_watch_port", fromlist=["PodLogWatchPort"]
            ).PodLogWatchPort
        )
        watch_port.watch.return_value = iter([])
        watch_port.pod_exists.return_value = True
        alert_port = MagicMock(
            spec=__import__(
                "hexawyn.application.ports.driven.alert_notification_port",
                fromlist=["AlertNotificationPort"],
            ).AlertNotificationPort
        )
        service = WatchPodLogsService(watch_port=watch_port, alert_port=alert_port)
        response = service.watch(WatchPodLogsCommand(pod_name="p", namespace="ns"))
        assert response.alerts == []


class TestWatchPodLogsServiceEdgeCases:
    def test_watch_port_failure_propagates(self) -> None:
        import pytest

        watch_port = MagicMock(spec=PodLogWatchPort)
        watch_port.watch.side_effect = RuntimeError("stream connection lost")
        alert_port = MagicMock(spec=AlertNotificationPort)

        service = WatchPodLogsService(watch_port=watch_port, alert_port=alert_port)

        with pytest.raises(RuntimeError, match="stream connection lost"):
            service.watch(WatchPodLogsCommand(pod_name="p", namespace="ns"))
