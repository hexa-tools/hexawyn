from __future__ import annotations

from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_command import (
    ConfigurationDriftDetectionCommand,
)


class TestConfigurationDriftDetectionCommand:
    def test_defaults_to_no_kustomize_paths(self) -> None:
        cmd = ConfigurationDriftDetectionCommand(namespace="production")
        assert cmd.kustomize_paths == []

    def test_accepts_kustomize_paths(self) -> None:
        cmd = ConfigurationDriftDetectionCommand(
            namespace="production", kustomize_paths=["overlays/production"]
        )
        assert cmd.kustomize_paths == ["overlays/production"]
