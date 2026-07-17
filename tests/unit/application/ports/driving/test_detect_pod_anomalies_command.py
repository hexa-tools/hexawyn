from __future__ import annotations

from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_command import (
    DetectPodAnomaliesCommand,
)


class TestDetectPodAnomaliesCommand:
    def test_defaults(self) -> None:
        cmd = DetectPodAnomaliesCommand(namespace="production")
        assert cmd.baseline_window_days == 7

    def test_explicit_value(self) -> None:
        cmd = DetectPodAnomaliesCommand(namespace="production", baseline_window_days=14)
        assert cmd.baseline_window_days == 14
