"""Unit tests for SearchResourcesByLabelsService (mocks ResourceSearchPort + K8sPort)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.service.search_resources_by_labels_service import (
    SearchResourcesByLabelsService,
)
from hexawyn.domain.errors import ResourceNotFoundError


def _raw(name: str, namespace: str = "production", kind: str = "pod") -> dict:
    return {
        "name": name,
        "namespace": namespace,
        "kind": kind,
        "node": "worker-1" if kind == "pod" else None,
        "phase": "Running" if kind == "pod" else None,
        "ready": True if kind == "pod" else None,
        "labels": {"app": "payment"},
    }


def _make_service(
    port: MagicMock | None = None, k8s_port: MagicMock | None = None
) -> SearchResourcesByLabelsService:
    if port is None:
        port = MagicMock()
        port.search_pods.return_value = []
        port.search_deployments.return_value = []
        port.search_services.return_value = []
        port.search_configmaps.return_value = []
    if k8s_port is None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "production", "status": "Active", "age": "10d"}
        ]
    return SearchResourcesByLabelsService(port=port, k8s_port=k8s_port)


class TestNamespaceValidation:
    def test_raises_when_namespace_missing(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [{"name": "other", "status": "Active", "age": "1d"}]
        service = _make_service(k8s_port=k8s_port)

        with pytest.raises(ResourceNotFoundError):
            service.search(
                SearchResourcesByLabelsCommand(label_selector="app=payment", namespace="ghost")
            )

    def test_no_validation_when_namespace_not_given(self) -> None:
        k8s_port = MagicMock()
        service = _make_service(k8s_port=k8s_port)

        service.search(SearchResourcesByLabelsCommand(label_selector="app=payment"))

        k8s_port.list_namespaces.assert_not_called()


class TestResourceTypeDispatch:
    def test_calls_only_requested_resource_type_methods(self) -> None:
        port = MagicMock()
        port.search_pods.return_value = [_raw("payment-pod-abc12")]
        service = _make_service(port=port)

        response = service.search(
            SearchResourcesByLabelsCommand(label_selector="app=payment", resource_types=["pods"])
        )

        port.search_pods.assert_called_once_with(label_selector="app=payment", namespace=None)
        port.search_deployments.assert_not_called()
        port.search_services.assert_not_called()
        port.search_configmaps.assert_not_called()
        assert response.total_matched == 1

    def test_default_calls_all_four_resource_type_methods(self) -> None:
        port = MagicMock()
        port.search_pods.return_value = []
        port.search_deployments.return_value = []
        port.search_services.return_value = []
        port.search_configmaps.return_value = []
        service = _make_service(port=port)

        service.search(SearchResourcesByLabelsCommand(label_selector="app=payment"))

        port.search_pods.assert_called_once()
        port.search_deployments.assert_called_once()
        port.search_services.assert_called_once()
        port.search_configmaps.assert_called_once()

    def test_mixed_kinds_aggregated_into_one_response(self) -> None:
        """TC3: single label matches pods and services → both returned."""
        port = MagicMock()
        port.search_pods.return_value = [_raw("payment-pod-abc12")]
        port.search_deployments.return_value = []
        port.search_services.return_value = [_raw("payment-service", kind="service")]
        port.search_configmaps.return_value = []
        service = _make_service(port=port)

        response = service.search(SearchResourcesByLabelsCommand(label_selector="app=payment"))

        assert response.total_matched == 2
        kinds = {resource["kind"] for group in response.groups for resource in group["resources"]}
        assert kinds == {"pod", "service"}


class TestNamespaceScopedSearch:
    """Edge case: namespace-scoped search combined with cluster-wide label."""

    def test_namespace_passed_through_to_port(self) -> None:
        port = MagicMock()
        port.search_pods.return_value = []
        port.search_deployments.return_value = []
        port.search_services.return_value = []
        port.search_configmaps.return_value = []
        service = _make_service(port=port)

        service.search(
            SearchResourcesByLabelsCommand(label_selector="app=payment", namespace="production")
        )

        port.search_pods.assert_called_once_with(
            label_selector="app=payment", namespace="production"
        )
