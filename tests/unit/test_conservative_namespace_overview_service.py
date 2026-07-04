"""Unit tests for ConservativeNamespaceOverviewService (mocks NamespaceOverviewPort + K8sPort)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_command import (
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.service.conservative_namespace_overview_service import (
    ConservativeNamespaceOverviewService,
)
from hexawyn.domain.errors import ResourceNotFoundError


def _raw_data() -> dict:
    return {
        "namespace_status": "Active",
        "pods": [{"name": "pod-a", "status": "Running"}],
        "deployments": [],
        "services_count": 1,
        "hpas": [],
    }


def _make_service(
    port: MagicMock | None = None, k8s_port: MagicMock | None = None
) -> ConservativeNamespaceOverviewService:
    if port is None:
        port = MagicMock()
        port.get_namespace_overview_data.return_value = _raw_data()
    if k8s_port is None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "staging", "status": "Active", "age": "10d"}
        ]
    return ConservativeNamespaceOverviewService(port=port, k8s_port=k8s_port)


class TestNamespaceValidation:
    def test_raises_when_namespace_missing(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [{"name": "other", "status": "Active", "age": "1d"}]
        service = _make_service(k8s_port=k8s_port)

        with pytest.raises(ResourceNotFoundError):
            service.get_overview(ConservativeNamespaceOverviewCommand(namespace="ghost"))


class TestBulkFetch:
    def test_calls_port_once_in_bulk(self) -> None:
        port = MagicMock()
        port.get_namespace_overview_data.return_value = _raw_data()
        service = _make_service(port=port)

        response = service.get_overview(ConservativeNamespaceOverviewCommand(namespace="staging"))

        port.get_namespace_overview_data.assert_called_once_with("staging")
        assert response.error is None
        assert response.namespace == "staging"
        assert response.health_status == "Healthy"

    def test_max_tokens_passed_through_to_domain(self) -> None:
        port = MagicMock()
        port.get_namespace_overview_data.return_value = {
            "namespace_status": "Active",
            "pods": [
                {"name": f"failing-pod-{i}", "status": "CrashLoopBackOff"} for i in range(200)
            ],
            "deployments": [],
            "services_count": 0,
            "hpas": [],
        }
        service = _make_service(port=port)

        response = service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace="staging", max_tokens=200)
        )

        assert response.estimated_tokens <= 200
        assert response.has_more_unhealthy is True
