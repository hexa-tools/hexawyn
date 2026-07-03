"""Unit tests for SemanticLogSearchService (mocks LogSearchPort + K8sPort)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_command import (
    SemanticLogSearchCommand,
)
from hexawyn.application.service.semantic_log_search_service import SemanticLogSearchService
from hexawyn.domain.errors import InsufficientPermissionsError, ResourceNotFoundError


def _pod(name: str, status: str = "Running") -> dict:
    return {
        "name": name,
        "namespace": "production",
        "status": status,
        "restarts": 0,
        "age": "1d",
        "node": "n1",
    }


def _container_log(container: str = "app", lines: list[str] | None = None) -> dict:
    return {
        "container": container,
        "lines": lines or ["2024-01-01T10:32:15Z connection refused to postgres"],
        "truncated": False,
    }


def _make_service(
    port: MagicMock | None = None, k8s_port: MagicMock | None = None
) -> SemanticLogSearchService:
    if port is None:
        port = MagicMock()
        port.fetch_pod_container_logs.return_value = [_container_log()]
    if k8s_port is None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "production", "status": "Active", "age": "10d"}
        ]
        k8s_port.list_pods.return_value = [_pod("checkout-pod-abc12")]
    return SemanticLogSearchService(port=port, k8s_port=k8s_port)


class TestNamespaceValidation:
    def test_raises_when_namespace_missing(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [{"name": "other", "status": "Active", "age": "1d"}]
        service = _make_service(k8s_port=k8s_port)

        with pytest.raises(ResourceNotFoundError):
            service.search(
                SemanticLogSearchCommand(pattern="connection refused", namespace="ghost")
            )

    def test_valid_namespace_scopes_scan_to_that_namespace_only(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "production", "status": "Active", "age": "10d"},
            {"name": "staging", "status": "Active", "age": "5d"},
        ]
        k8s_port.list_pods.return_value = []
        service = _make_service(k8s_port=k8s_port)

        response = service.search(
            SemanticLogSearchCommand(pattern="connection refused", namespace="production")
        )

        assert response.namespaces_total == 1
        assert response.scanned_namespaces == ["production"]
        k8s_port.list_pods.assert_called_once_with(namespace="production")

    def test_no_namespace_scans_all_namespaces(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "production", "status": "Active", "age": "10d"},
            {"name": "staging", "status": "Active", "age": "5d"},
        ]
        k8s_port.list_pods.return_value = []
        service = _make_service(k8s_port=k8s_port)

        response = service.search(SemanticLogSearchCommand(pattern="connection refused"))

        assert response.namespaces_total == 2
        assert set(response.scanned_namespaces) == {"production", "staging"}


class TestPendingPodPreFilter:
    def test_pending_pod_skipped_without_port_call(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "production", "status": "Active", "age": "10d"}
        ]
        k8s_port.list_pods.return_value = [_pod("pending-pod", status="Pending")]
        port = MagicMock()
        service = _make_service(port=port, k8s_port=k8s_port)

        response = service.search(SemanticLogSearchCommand(pattern="connection refused"))

        port.fetch_pod_container_logs.assert_not_called()
        assert len(response.skipped_pods) == 1
        assert "Pending" in response.skipped_pods[0]["reason"]


class TestRbacDeniedNamespace:
    def test_namespace_skipped_others_still_scanned(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "kube-system", "status": "Active", "age": "10d"},
            {"name": "production", "status": "Active", "age": "10d"},
        ]

        def _list_pods(namespace: str | None = None) -> list:
            if namespace == "kube-system":
                raise InsufficientPermissionsError("RBAC denied")
            return [_pod("checkout-pod-abc12")]

        k8s_port.list_pods.side_effect = _list_pods
        service = _make_service(k8s_port=k8s_port)

        response = service.search(SemanticLogSearchCommand(pattern="connection refused"))

        assert len(response.skipped_namespaces) == 1
        assert response.skipped_namespaces[0]["namespace"] == "kube-system"
        assert "production" in response.scanned_namespaces


class TestPerPodFetchFailure:
    def test_pod_fetch_error_skips_pod_not_whole_scan(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "production", "status": "Active", "age": "10d"}
        ]
        k8s_port.list_pods.return_value = [_pod("gone-pod"), _pod("healthy-pod")]
        port = MagicMock()
        port.fetch_pod_container_logs.side_effect = [
            ResourceNotFoundError("pod gone"),
            [_container_log()],
        ]
        service = _make_service(port=port, k8s_port=k8s_port)

        response = service.search(SemanticLogSearchCommand(pattern="connection refused"))

        assert len(response.skipped_pods) == 1
        assert response.skipped_pods[0]["pod_name"] == "gone-pod"
        assert response.pods_affected == 1

    def test_empty_container_logs_marks_pod_skipped(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "production", "status": "Active", "age": "10d"}
        ]
        k8s_port.list_pods.return_value = [_pod("evicted-pod")]
        port = MagicMock()
        port.fetch_pod_container_logs.return_value = []
        service = _make_service(port=port, k8s_port=k8s_port)

        response = service.search(SemanticLogSearchCommand(pattern="connection refused"))

        assert len(response.skipped_pods) == 1
        assert response.no_matches is True


class TestHappyPath:
    def test_returns_response_with_matched_pods(self) -> None:
        service = _make_service()

        response = service.search(
            SemanticLogSearchCommand(pattern="connection refused to postgres")
        )

        assert response.error is None
        assert response.pods_affected == 1
        assert len(response.groups) == 1
