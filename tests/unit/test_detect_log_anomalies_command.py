from __future__ import annotations

from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_command import (
    DetectLogAnomaliesCommand,
)


class TestDetectLogAnomaliesCommand:
    def test_defaults(self) -> None:
        cmd = DetectLogAnomaliesCommand(pod_name="inventory-service", namespace="prod")
        assert cmd.time_window_minutes == 240
        assert cmd.zscore_threshold == 3.0

    def test_explicit_values(self) -> None:
        cmd = DetectLogAnomaliesCommand(
            pod_name="inventory-service",
            namespace="prod",
            time_window_minutes=60,
            zscore_threshold=2.0,
        )
        assert cmd.time_window_minutes == 60
        assert cmd.zscore_threshold == 2.0
