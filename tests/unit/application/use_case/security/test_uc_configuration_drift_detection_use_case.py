from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.configuration_drift_detection.command import (
    ConfigurationDriftDetectionCommand,
)
from hexawyn.application.use_case.security.configuration_drift_detection.response import (  # noqa: E501
    ConfigurationDriftDetectionResponse,
)


def _live_resource(kind: str, name: str, namespace: str = "default") -> dict[str, object]:
    return {
        "kind": kind,
        "name": name,
        "namespace": namespace,
        "data": {"spec": {"replicas": 1}},
        "annotations": {},
    }


class TestConfigurationDriftDetectionUseCase:
    def test_execute_returns_response(self) -> None:
        from hexawyn.application.use_case.security.configuration_drift_detection.configuration_drift_detection_use_case import (  # noqa: E501
            ConfigurationDriftDetectionUseCase,
        )

        live = MagicMock()
        live.list_live_resources.return_value = []
        helm = MagicMock()
        helm.render_desired_manifests.return_value = []
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = []

        use_case = ConfigurationDriftDetectionUseCase(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
        )
        result = use_case.detect_drift(
            ConfigurationDriftDetectionCommand(
                namespace="default",
                kustomize_paths=[],
            )
        )

        assert isinstance(result, ConfigurationDriftDetectionResponse)
        assert result.total_checked == 0

    def test_execute_excludes_unmanaged_resources(self) -> None:
        from hexawyn.application.use_case.security.configuration_drift_detection.configuration_drift_detection_use_case import (  # noqa: E501
            ConfigurationDriftDetectionUseCase,
        )

        live = MagicMock()
        live.list_live_resources.return_value = [
            _live_resource("Deployment", "unmanaged-app"),
        ]
        helm = MagicMock()
        helm.render_desired_manifests.return_value = []
        helm.source_exists.return_value = False
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = []

        use_case = ConfigurationDriftDetectionUseCase(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
        )
        result = use_case.detect_drift(
            ConfigurationDriftDetectionCommand(
                namespace="default",
                kustomize_paths=[],
            )
        )

        assert result.summary
