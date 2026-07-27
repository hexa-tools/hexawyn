from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.detect_container_image_drift.command import (
    DetectContainerImageDriftCommand,
)
from hexawyn.application.use_case.security.detect_container_image_drift.response import (  # noqa: E501
    DetectContainerImageDriftResponse,
)


class TestDetectContainerImageDriftUseCase:
    def test_execute_returns_response(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            DetectContainerImageDriftUseCase,
        )

        live = MagicMock()
        live.list_deployments.return_value = []
        drift = MagicMock()
        drift.render_desired_manifests.return_value = []
        drift.source_exists.return_value = False
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = []

        image_drift = MagicMock()
        image_drift.list_running_images.return_value = []

        use_case = DetectContainerImageDriftUseCase(
            live_resource_port=live,
            helm_adapter=drift,
            kustomize_adapter=kustomize,
            image_drift_port=image_drift,
        )
        result = use_case.execute(
            DetectContainerImageDriftCommand(
                namespace="default",
                kustomize_paths=[],
            )
        )

        assert isinstance(result, DetectContainerImageDriftResponse)
