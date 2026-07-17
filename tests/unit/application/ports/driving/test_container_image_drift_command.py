from __future__ import annotations


class TestContainerImageDriftCommand:
    def test_defaults_kustomize_paths_to_empty_list(self) -> None:
        from hexawyn.application.ports.driving.container_image_drift.container_image_drift_command import (
            ContainerImageDriftCommand,
        )

        command = ContainerImageDriftCommand(namespace="production")

        assert command.namespace == "production"
        assert command.kustomize_paths == []

    def test_accepts_custom_kustomize_paths(self) -> None:
        from hexawyn.application.ports.driving.container_image_drift.container_image_drift_command import (
            ContainerImageDriftCommand,
        )

        command = ContainerImageDriftCommand(
            namespace="production", kustomize_paths=["overlays/production"]
        )

        assert command.kustomize_paths == ["overlays/production"]
