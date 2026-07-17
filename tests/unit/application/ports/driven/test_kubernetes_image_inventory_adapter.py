"""Unit tests for KubernetesImageInventoryAdapter — mocks kubernetes.client.CoreV1Api,
iterating init/regular/ephemeral containers to enumerate every running image."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.image_inventory_port import ImageInventoryPort
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _container(name: str, image: str) -> MagicMock:
    container = MagicMock()
    container.name = name
    container.image = image
    return container


def _pod(
    name: str,
    namespace: str = "production",
    init_containers: list | None = None,
    containers: list | None = None,
    ephemeral_containers: list | None = None,
) -> MagicMock:
    pod = MagicMock()
    pod.metadata.name = name
    pod.metadata.namespace = namespace
    pod.spec.init_containers = init_containers
    pod.spec.containers = containers or []
    pod.spec.ephemeral_containers = ephemeral_containers
    return pod


def _list_response(*items: MagicMock) -> MagicMock:
    response = MagicMock()
    response.items = list(items)
    return response


class TestKubernetesImageInventoryAdapterIsPort:
    def test_is_image_inventory_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_inventory_adapter import (
            KubernetesImageInventoryAdapter,
        )

        assert isinstance(KubernetesImageInventoryAdapter(), ImageInventoryPort)


class TestListRunningImages:
    def test_maps_regular_container_images(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_inventory_adapter import (
            KubernetesImageInventoryAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod("payment-pod-abc", containers=[_container("app", "payment:v1.2")])
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesImageInventoryAdapter().list_running_images()

        assert result == [
            {"image": "payment:v1.2", "namespace": "production", "pod_name": "payment-pod-abc"}
        ]

    def test_iterates_init_regular_and_ephemeral_containers(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_inventory_adapter import (
            KubernetesImageInventoryAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod(
                "p",
                init_containers=[_container("init", "busybox:1.36")],
                containers=[_container("app", "payment:v1.2")],
                ephemeral_containers=[_container("debugger", "debug:v1")],
            )
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesImageInventoryAdapter().list_running_images()

        images = {item["image"] for item in result}
        assert images == {"busybox:1.36", "payment:v1.2", "debug:v1"}

    def test_same_image_used_by_multiple_pods_produces_multiple_entries(self) -> None:
        """The service layer groups by image; the adapter's job is only to
        report each running (image, namespace, pod) tuple faithfully."""
        from hexawyn.adapters.secondary.gitops.kubernetes_image_inventory_adapter import (
            KubernetesImageInventoryAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod("payment-pod-abc", containers=[_container("app", "payment:v1.2")]),
            _pod("payment-pod-def", containers=[_container("app", "payment:v1.2")]),
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesImageInventoryAdapter().list_running_images()

        assert len(result) == 2
        assert {item["pod_name"] for item in result} == {"payment-pod-abc", "payment-pod-def"}

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_inventory_adapter import (
            KubernetesImageInventoryAdapter,
        )

        core_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        core_api.list_pod_for_all_namespaces.side_effect = error

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesImageInventoryAdapter().list_running_images()

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_image_inventory_adapter import (
            KubernetesImageInventoryAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.side_effect = Exception("refused")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesImageInventoryAdapter().list_running_images()
