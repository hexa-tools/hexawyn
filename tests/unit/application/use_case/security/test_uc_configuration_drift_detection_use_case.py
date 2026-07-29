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


def _helm_live_resource(
    kind: str, name: str, release: str, namespace: str = "default"
) -> dict[str, object]:
    return {
        "kind": kind,
        "name": name,
        "namespace": namespace,
        "data": {"spec": {"replicas": 1}},
        "annotations": {"meta.helm.sh/release-name": release},
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

    def test_detect_drift_with_kustomize_match(self) -> None:
        from hexawyn.application.use_case.security.configuration_drift_detection.configuration_drift_detection_use_case import (  # noqa: E501
            ConfigurationDriftDetectionUseCase,
        )

        live = MagicMock()
        live.list_live_resources.return_value = [
            _live_resource("Deployment", "my-app"),
        ]
        helm = MagicMock()
        helm.render_desired_manifests.return_value = []
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = [
            {
                "kind": "Deployment",
                "name": "my-app",
                "namespace": "default",
                "data": {"spec": {"replicas": 2}},
            },
        ]

        use_case = ConfigurationDriftDetectionUseCase(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
        )
        result = use_case.detect_drift(
            ConfigurationDriftDetectionCommand(
                namespace="default",
                kustomize_paths=["overlays/prod"],
            )
        )

        assert isinstance(result, ConfigurationDriftDetectionResponse)
        assert result.total_checked == 1

    def test_detect_drift_with_helm_resource(self) -> None:
        from hexawyn.application.use_case.security.configuration_drift_detection.configuration_drift_detection_use_case import (  # noqa: E501
            ConfigurationDriftDetectionUseCase,
        )

        live = MagicMock()
        live.list_live_resources.return_value = [
            _helm_live_resource("Deployment", "helm-app", "my-release"),
        ]
        helm = MagicMock()
        helm.source_exists.return_value = True
        helm.render_desired_manifests.return_value = [
            {
                "kind": "Deployment",
                "name": "helm-app",
                "namespace": "default",
                "data": {"spec": {"replicas": 1}},
            },
        ]
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
        assert result.total_checked == 1

    def test_detect_drift_helm_source_missing(self) -> None:
        from hexawyn.application.use_case.security.configuration_drift_detection.configuration_drift_detection_use_case import (  # noqa: E501
            ConfigurationDriftDetectionUseCase,
        )

        live = MagicMock()
        live.list_live_resources.return_value = [
            _helm_live_resource("Deployment", "orphan-app", "missing-release"),
        ]
        helm = MagicMock()
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

        assert isinstance(result, ConfigurationDriftDetectionResponse)
        assert result.total_checked == 1


class TestConfigurationDriftMapper:
    def test_find_matching_returns_match(self) -> None:
        from hexawyn.application.use_case.security.configuration_drift_detection.mapper import (
            find_matching,
        )

        manifests: list[dict[str, object]] = [
            {"kind": "Deployment", "name": "my-app", "namespace": "default", "data": {}},
            {"kind": "Service", "name": "my-svc", "namespace": "default", "data": {}},
        ]
        result = find_matching(manifests, "Deployment", "my-app")

        assert result is not None
        assert result["kind"] == "Deployment"
        assert result["name"] == "my-app"

    def test_find_matching_returns_none_for_no_match(self) -> None:
        from hexawyn.application.use_case.security.configuration_drift_detection.mapper import (
            find_matching,
        )

        manifests: list[dict[str, object]] = [
            {"kind": "Deployment", "name": "my-app", "namespace": "default", "data": {}},
        ]
        result = find_matching(manifests, "Deployment", "other-app")

        assert result is None

    def test_find_matching_returns_none_for_empty_manifest_list(self) -> None:
        from hexawyn.application.use_case.security.configuration_drift_detection.mapper import (
            find_matching,
        )

        result = find_matching([], "Deployment", "my-app")

        assert result is None

    def test_to_manifest_converts_raw_to_domain(self) -> None:
        from hexawyn.application.use_case.security.configuration_drift_detection.mapper import (
            to_manifest,
        )
        from hexawyn.domain.models.configuration_drift import ResourceManifest

        raw: dict[str, object] = {
            "kind": "Deployment",
            "name": "my-app",
            "namespace": "default",
            "data": {"spec": {"replicas": 1}},
        }
        result = to_manifest(raw)

        assert isinstance(result, ResourceManifest)
        assert result.kind == "Deployment"
        assert result.name == "my-app"
        assert result.namespace == "default"
        assert result.data == {"spec": {"replicas": 1}}

    def test_to_live_manifest_converts_raw_to_domain(self) -> None:
        from hexawyn.application.use_case.security.configuration_drift_detection.mapper import (
            to_live_manifest,
        )
        from hexawyn.domain.models.configuration_drift import ResourceManifest

        raw: dict[str, object] = {
            "kind": "Service",
            "name": "my-svc",
            "namespace": "prod",
            "data": {"spec": {"ports": [80]}},
            "annotations": {"meta.helm.sh/release-name": "my-release"},
        }
        result = to_live_manifest(raw)

        assert isinstance(result, ResourceManifest)
        assert result.kind == "Service"
        assert result.name == "my-svc"
        assert result.namespace == "prod"
        assert result.data == {"spec": {"ports": [80]}}
