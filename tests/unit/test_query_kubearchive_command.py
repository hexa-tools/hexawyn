from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.kubearchive_port import (
    HistoricalComparisonResult,
    HistoricalPodInfo,
)
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_command import (
    QueryKubeArchiveCommand,
)
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_response import (
    QueryKubeArchiveResponse,
)
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_service_port import (
    QueryKubeArchiveServicePort,
)


class TestQueryKubeArchiveCommand:
    def test_is_frozen(self) -> None:
        cmd = QueryKubeArchiveCommand(
            namespace="payment",
            resource_type="pods",
            timestamp="2026-06-09T10:00:00Z",
        )
        with pytest.raises(AttributeError):
            cmd.namespace = "other"  # type: ignore[misc]

    def test_all_fields_required(self) -> None:
        cmd = QueryKubeArchiveCommand(
            namespace="payment",
            resource_type="pods",
            timestamp="2026-06-09T10:00:00Z",
        )
        assert cmd.namespace == "payment"
        assert cmd.resource_type == "pods"
        assert cmd.timestamp == "2026-06-09T10:00:00Z"

    def test_compare_with_current_defaults_to_false(self) -> None:
        cmd = QueryKubeArchiveCommand(
            namespace="ns",
            resource_type="pods",
            timestamp="t",
        )
        assert cmd.compare_with_current is False

    def test_compare_with_current_set_to_true(self) -> None:
        cmd = QueryKubeArchiveCommand(
            namespace="ns",
            resource_type="pods",
            timestamp="t",
            compare_with_current=True,
        )
        assert cmd.compare_with_current is True


class TestQueryKubeArchiveResponse:
    def test_defaults(self) -> None:
        resp = QueryKubeArchiveResponse()
        assert resp.total_resources == 0
        assert resp.pods == []
        assert resp.error is None
        assert resp.comparison is None

    def test_with_pods(self) -> None:
        pod: HistoricalPodInfo = {
            "name": "pod-a",
            "namespace": "ns",
            "phase": "Running",
            "restart_count": 0,
            "queried_timestamp": "t",
        }
        resp = QueryKubeArchiveResponse(
            total_resources=8,
            pods=[pod],
            queried_timestamp="2026-06-09T10:00:00Z",
        )
        assert resp.total_resources == 8
        assert len(resp.pods) == 1
        assert resp.queried_timestamp == "2026-06-09T10:00:00Z"

    def test_with_error(self) -> None:
        resp = QueryKubeArchiveResponse(error="KubeArchive not installed")
        assert resp.error == "KubeArchive not installed"
        assert resp.total_resources == 0

    def test_with_comparison(self) -> None:
        comparison: HistoricalComparisonResult = {
            "historical_count": 8,
            "current_count": 3,
            "pods_added": 0,
            "pods_removed": 5,
            "added_pod_names": [],
            "removed_pod_names": ["pod-a"],
            "delta_message": "−5 pods removed",
        }
        resp = QueryKubeArchiveResponse(comparison=comparison)
        assert resp.comparison is not None
        assert resp.comparison["pods_removed"] == 5


class TestQueryKubeArchiveServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(QueryKubeArchiveServicePort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            QueryKubeArchiveServicePort()  # type: ignore[abstract]

    def test_has_query_method(self) -> None:
        assert hasattr(QueryKubeArchiveServicePort, "query")
        method = QueryKubeArchiveServicePort.query
        assert getattr(method, "__isabstractmethod__", False)
