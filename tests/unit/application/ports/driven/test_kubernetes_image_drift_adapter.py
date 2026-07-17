"""Unit tests for KubernetesImageDriftAdapter — mocks kubernetes.client
AppsV1Api/CoreV1Api, joining Pods to Deployments via label-selector match."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.image_drift_port import ImageDriftPort
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _deployment(name: str, match_labels: dict) -> MagicMock:
    deployment = MagicMock()
    deployment.metadata.name = name
    deployment.spec.selector.match_labels = match_labels
    return deployment


def _deployment_list(*deployments: MagicMock) -> MagicMock:
    result = MagicMock()
    result.items = list(deployments)
    return result


def _container_status(name: str, image_id: str | None) -> MagicMock:
    status = MagicMock()
    status.name = name
    status.image_id = image_id
    return status


def _pod(labels: dict, container_statuses: list | None) -> MagicMock:
    pod = MagicMock()
    pod.metadata.labels = labels
    pod.status.container_statuses = container_statuses
    return pod


def _pod_list(*pods: MagicMock) -> MagicMock:
    result = MagicMock()
    result.items = list(pods)
    return result


class TestKubernetesImageDriftAdapterIsPort:
    def test_is_image_drift_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
            KubernetesImageDriftAdapter,
        )

        assert isinstance(KubernetesImageDriftAdapter(), ImageDriftPort)


class TestListResolvedContainerImages:
    def test_joins_pod_to_deployment_via_label_selector(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
            KubernetesImageDriftAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list(
            _deployment("payment-service", {"app": "payment"})
        )
        core_api = MagicMock()
        core_api.list_namespaced_pod.return_value = _pod_list(
            _pod({"app": "payment"}, [_container_status("payment-app", "payment@sha256:abc123")])
        )

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            adapter = KubernetesImageDriftAdapter()
            results = adapter.list_resolved_container_images("production")

        assert len(results) == 1
        assert results[0]["deployment"] == "payment-service"
        assert results[0]["container"] == "payment-app"
        assert results[0]["image_id"] == "payment@sha256:abc123"

    def test_multiple_containers_in_one_pod(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
            KubernetesImageDriftAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list(
            _deployment("app", {"app": "main"})
        )
        core_api = MagicMock()
        core_api.list_namespaced_pod.return_value = _pod_list(
            _pod(
                {"app": "main"},
                [
                    _container_status("main", "app@sha256:aaa"),
                    _container_status("sidecar", "envoy@sha256:bbb"),
                ],
            )
        )

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            adapter = KubernetesImageDriftAdapter()
            results = adapter.list_resolved_container_images("production")

        containers = {r["container"] for r in results}
        assert containers == {"main", "sidecar"}

    def test_pod_not_matching_selector_is_excluded(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
            KubernetesImageDriftAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list(
            _deployment("app", {"app": "main"})
        )
        core_api = MagicMock()
        core_api.list_namespaced_pod.return_value = _pod_list(
            _pod({"app": "other"}, [_container_status("main", "app@sha256:aaa")])
        )

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            adapter = KubernetesImageDriftAdapter()
            results = adapter.list_resolved_container_images("production")

        assert results == []

    def test_no_matching_pods_returns_empty_not_an_error(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
            KubernetesImageDriftAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list(
            _deployment("app", {"app": "main"})
        )
        core_api = MagicMock()
        core_api.list_namespaced_pod.return_value = _pod_list()

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            adapter = KubernetesImageDriftAdapter()
            results = adapter.list_resolved_container_images("production")

        assert results == []

    def test_container_status_missing_image_id_is_skipped(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
            KubernetesImageDriftAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list(
            _deployment("app", {"app": "main"})
        )
        core_api = MagicMock()
        core_api.list_namespaced_pod.return_value = _pod_list(
            _pod({"app": "main"}, [_container_status("main", None)])
        )

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            adapter = KubernetesImageDriftAdapter()
            results = adapter.list_resolved_container_images("production")

        assert results == []

    def test_pod_with_no_container_statuses_is_skipped(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
            KubernetesImageDriftAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = _deployment_list(
            _deployment("app", {"app": "main"})
        )
        core_api = MagicMock()
        core_api.list_namespaced_pod.return_value = _pod_list(_pod({"app": "main"}, None))

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            adapter = KubernetesImageDriftAdapter()
            results = adapter.list_resolved_container_images("production")

        assert results == []

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
            KubernetesImageDriftAdapter,
        )

        apps_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        apps_api.list_namespaced_deployment.side_effect = error

        with patch("kubernetes.client.AppsV1Api", return_value=apps_api):
            adapter = KubernetesImageDriftAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_resolved_container_images("production")

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
            KubernetesImageDriftAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.side_effect = Exception("connection refused")

        with patch("kubernetes.client.AppsV1Api", return_value=apps_api):
            adapter = KubernetesImageDriftAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.list_resolved_container_images("production")
