from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.kubearchive_port import (
    HistoricalComparisonResult,
    HistoricalPodInfo,
    KubeArchivePort,
    KubeArchiveQuery,
    KubeArchiveResponse,
)


class TestHistoricalPodInfo:
    def test_all_fields_present(self) -> None:
        info: HistoricalPodInfo = {
            "name": "payment-pod-abc",
            "namespace": "payment",
            "phase": "Running",
            "restart_count": 0,
            "queried_timestamp": "2026-06-09T10:00:00Z",
            "currently_exists": True,
            "status_changed_since": False,
        }
        assert info["name"] == "payment-pod-abc"
        assert info["phase"] == "Running"
        assert info["restart_count"] == 0

    def test_optional_fields_can_be_omitted(self) -> None:
        info: HistoricalPodInfo = {
            "name": "pod-x",
            "namespace": "ns",
            "phase": "Running",
            "restart_count": 3,
            "queried_timestamp": "t",
        }
        assert info["name"] == "pod-x"
        assert "currently_exists" not in info
        assert "status_changed_since" not in info


class TestKubeArchiveQuery:
    def test_all_fields_required(self) -> None:
        query: KubeArchiveQuery = {
            "namespace": "payment",
            "resource_type": "pods",
            "timestamp": "2026-06-09T10:00:00Z",
        }
        assert query["namespace"] == "payment"
        assert query["resource_type"] == "pods"

    def test_accepts_comparison_mode(self) -> None:
        query: KubeArchiveQuery = {
            "namespace": "payment",
            "resource_type": "pods",
            "timestamp": "2026-06-09T10:00:00Z",
            "compare_with_current": True,
        }
        assert query["compare_with_current"] is True


class TestKubeArchiveResponse:
    def test_response_with_pods(self) -> None:
        pods: list[HistoricalPodInfo] = [
            {
                "name": "pod-a",
                "namespace": "ns",
                "phase": "Running",
                "restart_count": 2,
                "queried_timestamp": "t",
            },
        ]
        response: KubeArchiveResponse = {
            "namespace": "ns",
            "resource_type": "pods",
            "queried_timestamp": "t",
            "total_resources": 5,
            "pods": pods,
            "kubearchive_available": True,
            "error": None,
        }
        assert response["total_resources"] == 5
        assert response["kubearchive_available"] is True
        assert response["error"] is None
        assert len(response["pods"]) == 1

    def test_response_unavailable(self) -> None:
        response: KubeArchiveResponse = {
            "namespace": "ns",
            "resource_type": "pods",
            "queried_timestamp": "t",
            "total_resources": 0,
            "pods": [],
            "kubearchive_available": False,
            "error": "KubeArchive not installed",
        }
        assert response["kubearchive_available"] is False
        assert response["error"] == "KubeArchive not installed"


class TestHistoricalComparisonResult:
    def test_comparison_fields(self) -> None:
        comparison: HistoricalComparisonResult = {
            "historical_count": 8,
            "current_count": 3,
            "pods_added": 0,
            "pods_removed": 5,
            "added_pod_names": [],
            "removed_pod_names": ["pod-a", "pod-b", "pod-c", "pod-d", "pod-e"],
            "delta_message": "\u22125 pods removed since t",
        }
        assert comparison["historical_count"] == 8
        assert comparison["current_count"] == 3
        assert comparison["pods_removed"] == 5


class TestKubeArchivePort:
    def test_is_abstract_class(self) -> None:
        assert issubclass(KubeArchivePort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            KubeArchivePort()  # type: ignore[abstract]

    def test_has_query_historical_state_method(self) -> None:
        assert hasattr(KubeArchivePort, "query_historical_state")
        method = KubeArchivePort.query_historical_state
        assert getattr(method, "__isabstractmethod__", False)
