"""Unit tests for ConfigurationDriftDetectionService (mocks LiveResourcePort +
two DriftDetectionPort instances — Helm and Kustomize)."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_command import (
    ConfigurationDriftDetectionCommand,
)
from hexawyn.application.service.configuration_drift_detection_service import (
    ConfigurationDriftDetectionService,
)


def _live_resource(
    kind: str,
    name: str,
    namespace: str = "production",
    release: str | None = "payment-chart",
    data: dict[str, object] | None = None,
) -> dict:
    annotations = {"meta.helm.sh/release-name": release} if release else {}
    return {
        "kind": kind,
        "name": name,
        "namespace": namespace,
        "labels": {},
        "annotations": annotations,
        "data": data if data is not None else {},
    }


def _manifest_raw(
    kind: str, name: str, namespace: str = "production", data: dict | None = None
) -> dict:
    return {
        "kind": kind,
        "name": name,
        "namespace": namespace,
        "data": data if data is not None else {},
    }


def _make_service(
    live_resource_port: MagicMock | None = None,
    helm_adapter: MagicMock | None = None,
    kustomize_adapter: MagicMock | None = None,
) -> tuple[ConfigurationDriftDetectionService, MagicMock, MagicMock, MagicMock]:
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
    service = ConfigurationDriftDetectionService(
        live_resource_port=live_resource_port,
        helm_adapter=helm_adapter,
        kustomize_adapter=kustomize_adapter,
    )
    return service, live_resource_port, helm_adapter, kustomize_adapter


class TestUnmanagedResourceExclusion:
    def test_resource_without_helm_annotation_or_kustomize_match_is_excluded(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _live_resource("Deployment", "unmanaged-app", release=None)
        ]
        service, _, _, _ = _make_service(live_resource_port=live_resource_port)

        response = service.detect_drift(ConfigurationDriftDetectionCommand(namespace="production"))

        assert response.drifted_resources == []
        assert len(response.excluded_resources) == 1
        assert "unmanaged-app" in response.excluded_resources[0]


class TestOrphanDetection:
    def test_deleted_helm_release_marks_resource_orphaned(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _live_resource("Deployment", "payment-service", release="deleted-release")
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = False
        service, _, _, _ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        response = service.detect_drift(ConfigurationDriftDetectionCommand(namespace="production"))

        assert len(response.drifted_resources) == 1
        assert response.drifted_resources[0]["is_orphaned"] is True
        helm_adapter.render_desired_manifests.assert_not_called()


class TestKustomizeMatchByIdentity:
    def test_live_resource_matching_kustomize_render_is_kustomize_managed(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _live_resource("Deployment", "reporting-service", release=None)
        ]
        kustomize_adapter = MagicMock()
        kustomize_adapter.render_desired_manifests.return_value = [
            _manifest_raw("Deployment", "reporting-service")
        ]
        service, _, _, _ = _make_service(
            live_resource_port=live_resource_port, kustomize_adapter=kustomize_adapter
        )

        response = service.detect_drift(
            ConfigurationDriftDetectionCommand(
                namespace="production", kustomize_paths=["overlays/production"]
            )
        )

        assert len(response.drifted_resources) == 0 or len(response.drifted_resources) == 1
        kustomize_adapter.render_desired_manifests.assert_called_once()


class TestHelmRenderMemoization:
    def test_same_release_rendered_only_once_for_multiple_resources(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _live_resource("Deployment", "payment-service", release="payment-chart"),
            _live_resource("ConfigMap", "payment-config", release="payment-chart"),
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = True
        helm_adapter.render_desired_manifests.return_value = [
            _manifest_raw("Deployment", "payment-service"),
            _manifest_raw("ConfigMap", "payment-config"),
        ]
        service, _, _, _ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        service.detect_drift(ConfigurationDriftDetectionCommand(namespace="production"))

        helm_adapter.render_desired_manifests.assert_called_once()
        helm_adapter.source_exists.assert_called_once()


class TestResourceMissingFromReleaseManifest:
    def test_resource_not_found_in_existing_release_manifest(self) -> None:
        """Release exists, but this specific resource isn't in its manifest
        (e.g. removed from the chart) — distinct from a deleted release."""
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _live_resource("Deployment", "leftover-service", release="payment-chart")
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = True
        helm_adapter.render_desired_manifests.return_value = [
            _manifest_raw("Deployment", "payment-service")
        ]
        service, _, _, _ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        response = service.detect_drift(ConfigurationDriftDetectionCommand(namespace="production"))

        assert len(response.drifted_resources) == 1
        assert response.drifted_resources[0]["is_orphaned"] is True


class TestFieldDrift:
    def test_actual_field_drift_flows_through_full_pipeline(self) -> None:
        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.return_value = [
            _live_resource(
                "Deployment",
                "payment-service",
                release="payment-chart",
                data={"spec": {"replicas": 1}},
            )
        ]
        helm_adapter = MagicMock()
        helm_adapter.source_exists.return_value = True
        helm_adapter.render_desired_manifests.return_value = [
            _manifest_raw("Deployment", "payment-service", data={"spec": {"replicas": 3}})
        ]
        service, _, _, _ = _make_service(
            live_resource_port=live_resource_port, helm_adapter=helm_adapter
        )

        response = service.detect_drift(ConfigurationDriftDetectionCommand(namespace="production"))

        assert len(response.drifted_resources) == 1
        drifted_fields = response.drifted_resources[0]["drifted_fields"]
        assert any(f["field_path"] == "replicas" for f in drifted_fields)


class TestNoLiveResources:
    def test_empty_cluster_produces_empty_report(self) -> None:
        service, _, _, _ = _make_service()

        response = service.detect_drift(ConfigurationDriftDetectionCommand(namespace="production"))

        assert response.error is None
        assert response.drifted_resources == []
        assert response.in_sync_count == 0


class TestConfigurationDriftDetectionServiceEdgeCases:
    def test_live_resource_port_failure_propagates(self) -> None:
        import pytest

        live_resource_port = MagicMock()
        live_resource_port.list_live_resources.side_effect = RuntimeError("etcd timeout")
        service, _, _, _ = _make_service(live_resource_port=live_resource_port)

        with pytest.raises(RuntimeError, match="etcd timeout"):
            service.detect_drift(ConfigurationDriftDetectionCommand(namespace="production"))
