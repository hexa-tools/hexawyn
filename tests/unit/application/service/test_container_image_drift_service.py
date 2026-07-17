"""Unit tests for ContainerImageDriftService (mocks LiveResourcePort,
DriftDetectionPort x2 (Helm/Kustomize), and ImageDriftPort)."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.container_image_drift.container_image_drift_command import (
    ContainerImageDriftCommand,
)
from hexawyn.application.service.container_image_drift_service import ContainerImageDriftService


def _deployment(
    name: str,
    containers: list[dict],
    namespace: str = "production",
    release: str | None = "payment-chart",
) -> dict:
    annotations = {"meta.helm.sh/release-name": release} if release else {}
    return {
        "kind": "Deployment",
        "name": name,
        "namespace": namespace,
        "labels": {},
        "annotations": annotations,
        "data": {"spec": {"template": {"spec": {"containers": containers}}}},
    }


def _manifest_raw(name: str, containers: list[dict], namespace: str = "production") -> dict:
    return {
        "kind": "Deployment",
        "name": name,
        "namespace": namespace,
        "data": {"spec": {"template": {"spec": {"containers": containers}}}},
    }


def _resolved_image(
    deployment: str, container: str, image_id: str, namespace: str = "production"
) -> dict:
    return {
        "deployment": deployment,
        "namespace": namespace,
        "container": container,
        "image_id": image_id,
    }


def _make_service(
    live_resource_port: MagicMock | None = None,
    helm_adapter: MagicMock | None = None,
    kustomize_adapter: MagicMock | None = None,
    image_drift_port: MagicMock | None = None,
) -> tuple[ContainerImageDriftService, MagicMock, MagicMock, MagicMock, MagicMock]:
    if live_resource_port is None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = []
    if helm_adapter is None:
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = True
        helm_adapter.render_desired_manifests.return_value = []
    if kustomize_adapter is None:
        kustomize_adapter = MagicMock()
        kustomize_adapter.render_desired_manifests.return_value = []
    if image_drift_port is None:
        image_drift_port = MagicMock()
        image_drift_port.list_resolved_container_images.return_value = []
    service = ContainerImageDriftService(
        live_resource_port=live_resource_port,
        helm_adapter=helm_adapter,
        kustomize_adapter=kustomize_adapter,
        image_drift_port=image_drift_port,
    )
    return service, live_resource_port, helm_adapter, kustomize_adapter, image_drift_port


class TestTagMismatch:
    def test_tc1_payment_service_tag_mismatch_via_helm(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _deployment(
                "payment-service",
                [{"name": "payment-app", "image": "payment:v1.3-hotfix"}],
                release="payment-chart",
            )
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = True
        helm_adapter.render_desired_manifests.return_value = [
            _manifest_raw("payment-service", [{"name": "payment-app", "image": "payment:v1.2"}])
        ]
        service, *_ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        response = service.detect_image_drift(ContainerImageDriftCommand(namespace="production"))

        assert response.error is None
        assert len(response.out_of_sync) == 1
        drift = response.out_of_sync[0]
        assert drift["deployment"] == "payment-service"
        assert drift["drift_type"] == "tag_mismatch"
        assert drift["severity"] == "critical"
        assert drift["source_of_truth"] == "helm-release:payment-chart"
        assert drift["running_image"] == "payment:v1.3-hotfix"
        assert drift["declared_image"] == "payment:v1.2"


class TestAllInSync:
    def test_tc2_running_image_matches_declared(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _deployment("app", [{"name": "app", "image": "app:v1.0"}])
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = True
        helm_adapter.render_desired_manifests.return_value = [
            _manifest_raw("app", [{"name": "app", "image": "app:v1.0"}])
        ]
        service, *_ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        response = service.detect_image_drift(ContainerImageDriftCommand(namespace="production"))

        assert response.out_of_sync == []
        assert response.in_sync_count == 1


class TestDigestMismatch:
    def test_tc3_resolved_image_id_digest_differs_from_kustomize_declared_digest(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _deployment(
                "analytics-worker", [{"name": "worker", "image": "analytics:v2.0"}], release=None
            )
        ]
        kustomize_adapter = MagicMock()
        kustomize_adapter.render_desired_manifests.return_value = [
            _manifest_raw(
                "analytics-worker",
                [{"name": "worker", "image": "analytics:sha256:def456"}],
            )
        ]
        image_drift_port = MagicMock()
        image_drift_port.list_resolved_container_images.return_value = [
            _resolved_image("analytics-worker", "worker", "analytics@sha256:abc123")
        ]
        service, *_ = _make_service(
            live_resource_port=live_resource_port,
            kustomize_adapter=kustomize_adapter,
            image_drift_port=image_drift_port,
        )

        response = service.detect_image_drift(
            ContainerImageDriftCommand(
                namespace="production", kustomize_paths=["overlays/production"]
            )
        )

        assert len(response.out_of_sync) == 1
        drift = response.out_of_sync[0]
        assert drift["drift_type"] == "digest_mismatch"
        assert drift["severity"] == "critical"
        assert drift["source_of_truth"] == "kustomize:overlays/production"


class TestFiveOutOfSync:
    def test_tc4_five_out_of_sync_deployments_all_listed(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _deployment(f"app-{i}", [{"name": "app", "image": f"app:v{i}-hotfix"}])
            for i in range(5)
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = True
        helm_adapter.render_desired_manifests.return_value = [
            _manifest_raw(f"app-{i}", [{"name": "app", "image": f"app:v{i}"}]) for i in range(5)
        ]
        service, *_ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        response = service.detect_image_drift(ContainerImageDriftCommand(namespace="production"))

        assert len(response.out_of_sync) == 5


class TestLatestTagExcluded:
    def test_tc5_latest_tag_excluded_from_comparison(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _deployment("app", [{"name": "app", "image": "app:latest"}])
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = True
        helm_adapter.render_desired_manifests.return_value = [
            _manifest_raw("app", [{"name": "app", "image": "app:v1.0"}])
        ]
        service, *_ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        response = service.detect_image_drift(ContainerImageDriftCommand(namespace="production"))

        assert response.out_of_sync == []
        assert response.in_sync_count == 0
        assert response.excluded_count == 1


class TestMultipleContainers:
    def test_each_container_checked_individually(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _deployment(
                "app",
                [
                    {"name": "main", "image": "app:v1.3-hotfix"},
                    {"name": "sidecar", "image": "envoy:v1.20"},
                ],
            )
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = True
        helm_adapter.render_desired_manifests.return_value = [
            _manifest_raw(
                "app",
                [
                    {"name": "main", "image": "app:v1.2"},
                    {"name": "sidecar", "image": "envoy:v1.20"},
                ],
            )
        ]
        service, *_ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        response = service.detect_image_drift(ContainerImageDriftCommand(namespace="production"))

        assert len(response.out_of_sync) == 1
        assert response.out_of_sync[0]["container"] == "main"
        assert response.in_sync_count == 1


class TestKustomizeMatchesBeforeHelm:
    def test_kustomize_identity_match_takes_priority(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _deployment("app", [{"name": "app", "image": "app:v1.0"}], release="some-chart")
        ]
        kustomize_adapter = MagicMock()
        kustomize_adapter.render_desired_manifests.return_value = [
            _manifest_raw("app", [{"name": "app", "image": "app:v1.0"}])
        ]
        helm_adapter = MagicMock()
        service, _, helm_adapter, kustomize_adapter, _ = _make_service(
            live_resource_port=live_resource_port,
            kustomize_adapter=kustomize_adapter,
            helm_adapter=helm_adapter,
        )

        response = service.detect_image_drift(
            ContainerImageDriftCommand(
                namespace="production", kustomize_paths=["overlays/production"]
            )
        )

        assert response.in_sync_count == 1
        helm_adapter.source_exists.assert_not_called()
        helm_adapter.render_desired_manifests.assert_not_called()


class TestHelmMemoization:
    def test_same_release_rendered_only_once_for_multiple_deployments(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _deployment("app-one", [{"name": "app", "image": "app:v1.0"}], release="shared-chart"),
            _deployment("app-two", [{"name": "app", "image": "app:v1.0"}], release="shared-chart"),
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = True
        helm_adapter.render_desired_manifests.return_value = [
            _manifest_raw("app-one", [{"name": "app", "image": "app:v1.0"}]),
            _manifest_raw("app-two", [{"name": "app", "image": "app:v1.0"}]),
        ]
        service, *_ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        service.detect_image_drift(ContainerImageDriftCommand(namespace="production"))

        helm_adapter.render_desired_manifests.assert_called_once()
        helm_adapter.source_exists.assert_called_once()


class TestOrphanedHelmReleaseSkipped:
    def test_deleted_helm_release_is_skipped_not_reported(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _deployment("app", [{"name": "app", "image": "app:v1.0"}], release="deleted-release")
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = False
        service, *_ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        response = service.detect_image_drift(ContainerImageDriftCommand(namespace="production"))

        assert response.out_of_sync == []
        assert response.in_sync_count == 0
        helm_adapter.render_desired_manifests.assert_not_called()


class TestUnmanagedDeploymentSkipped:
    def test_no_helm_annotation_and_no_kustomize_match_is_skipped(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _deployment("unmanaged-app", [{"name": "app", "image": "app:v1.0"}], release=None)
        ]
        service, *_ = _make_service(live_resource_port=live_resource_port)

        response = service.detect_image_drift(ContainerImageDriftCommand(namespace="production"))

        assert response.out_of_sync == []
        assert response.in_sync_count == 0


class TestContainerNotInDeclaredSkipped:
    def test_container_missing_from_desired_manifest_is_skipped(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _deployment("app", [{"name": "extra-sidecar", "image": "sidecar:v1.0"}])
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = True
        helm_adapter.render_desired_manifests.return_value = [_manifest_raw("app", [])]
        service, *_ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        response = service.detect_image_drift(ContainerImageDriftCommand(namespace="production"))

        assert response.out_of_sync == []
        assert response.in_sync_count == 0


class TestHelmManifestMissingDeployment:
    def test_deployment_not_found_in_release_manifest_is_skipped(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _deployment("app", [{"name": "app", "image": "app:v1.0"}], release="some-chart")
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = True
        helm_adapter.render_desired_manifests.return_value = [
            _manifest_raw("other-app", [{"name": "app", "image": "app:v1.0"}])
        ]
        service, *_ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        response = service.detect_image_drift(ContainerImageDriftCommand(namespace="production"))

        assert response.out_of_sync == []
        assert response.in_sync_count == 0


class TestEmptyNamespace:
    def test_no_deployments_produces_empty_report(self) -> None:
        service, *_ = _make_service()

        response = service.detect_image_drift(ContainerImageDriftCommand(namespace="production"))

        assert response.error is None
        assert response.out_of_sync == []
        assert response.in_sync_count == 0
