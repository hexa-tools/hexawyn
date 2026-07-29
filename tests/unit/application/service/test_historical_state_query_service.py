from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.service.historical_state_query_service import (
    HistoricalStateQueryService,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.command import (
    QueryKubearchiveCommand,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.response import (
    QueryKubearchiveResponse,
)


class TestHistoricalStateQueryService:
    def test_query_returns_response_without_comparison(self) -> None:
        kubearchive = MagicMock()
        kubearchive.query_historical_state.return_value = {
            "namespace": "default",
            "resource_type": "pods",
            "queried_timestamp": "2024-01-01T00:00:00Z",
            "total_resources": 3,
            "pods": [],
            "kubearchive_available": True,
            "error": None,
        }
        k8s = MagicMock()

        service = HistoricalStateQueryService(kubearchive_port=kubearchive, k8s_port=k8s)
        result = service.query(
            QueryKubearchiveCommand(
                namespace="default",
                resource_type="pods",
                timestamp="2024-01-01T00:00:00Z",
            )
        )

        assert isinstance(result, QueryKubearchiveResponse)
        assert result.total_resources == 3  # noqa: PLR2004
        assert result.queried_timestamp == "2024-01-01T00:00:00Z"
        assert result.comparison is None

    def test_query_with_comparison_returns_comparison_result(self) -> None:
        kubearchive = MagicMock()
        kubearchive.query_historical_state.return_value = {
            "namespace": "default",
            "resource_type": "pods",
            "queried_timestamp": "2024-01-01T00:00:00Z",
            "total_resources": 2,
            "pods": [
                {
                    "name": "old-pod",
                    "namespace": "default",
                    "phase": "Running",
                    "restart_count": 0,
                    "queried_timestamp": "2024-01-01T00:00:00Z",
                },
                {
                    "name": "removed-pod",
                    "namespace": "default",
                    "phase": "Running",
                    "restart_count": 1,
                    "queried_timestamp": "2024-01-01T00:00:00Z",
                },
            ],
            "kubearchive_available": True,
            "error": None,
        }
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {
                "name": "old-pod",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "age": "30d",
            },
            {
                "name": "new-pod",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "age": "1d",
            },
        ]

        service = HistoricalStateQueryService(kubearchive_port=kubearchive, k8s_port=k8s)
        result = service.query(
            QueryKubearchiveCommand(
                namespace="default",
                resource_type="pods",
                timestamp="2024-01-01T00:00:00Z",
                compare_with_current=True,
            )
        )

        assert result.comparison is not None
        comparison = result.comparison
        assert comparison is not None
        assert comparison["historical_count"] == 2  # noqa: PLR2004
        assert comparison["current_count"] == 2  # noqa: PLR2004
        assert comparison["pods_added"] == 1  # noqa: PLR2004
        assert comparison["pods_removed"] == 1  # noqa: PLR2004

    def test_query_handles_exception_gracefully(self) -> None:
        kubearchive = MagicMock()
        kubearchive.query_historical_state.side_effect = ValueError("connection failed")
        k8s = MagicMock()

        service = HistoricalStateQueryService(kubearchive_port=kubearchive, k8s_port=k8s)
        result = service.query(QueryKubearchiveCommand(namespace="default"))

        assert result.error == "connection failed"
        assert result.total_resources == 0  # noqa: PLR2004

    def test_query_empty_pods_list(self) -> None:
        kubearchive = MagicMock()
        kubearchive.query_historical_state.return_value = {
            "namespace": "default",
            "resource_type": "pods",
            "queried_timestamp": "2024-01-01T00:00:00Z",
            "total_resources": 0,
            "pods": [],
            "kubearchive_available": True,
            "error": None,
        }
        k8s = MagicMock()

        service = HistoricalStateQueryService(kubearchive_port=kubearchive, k8s_port=k8s)
        result = service.query(QueryKubearchiveCommand(namespace="default"))

        assert result.total_resources == 0  # noqa: PLR2004
        assert result.pods == []

    def test_query_compare_no_changes_delta_message(self) -> None:
        kubearchive = MagicMock()
        kubearchive.query_historical_state.return_value = {
            "namespace": "default",
            "resource_type": "pods",
            "queried_timestamp": "2024-01-01T00:00:00Z",
            "total_resources": 1,
            "pods": [
                {
                    "name": "stable-pod",
                    "namespace": "default",
                    "phase": "Running",
                    "restart_count": 0,
                    "queried_timestamp": "2024-01-01T00:00:00Z",
                },
            ],
            "kubearchive_available": True,
            "error": None,
        }
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {
                "name": "stable-pod",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "age": "30d",
            },
        ]

        service = HistoricalStateQueryService(kubearchive_port=kubearchive, k8s_port=k8s)
        result = service.query(
            QueryKubearchiveCommand(
                namespace="default",
                compare_with_current=True,
                timestamp="2024-01-01T00:00:00Z",
            )
        )

        assert result.comparison is not None
        comparison = result.comparison
        assert comparison is not None
        assert comparison["pods_added"] == 0  # noqa: PLR2004
        assert comparison["pods_removed"] == 0  # noqa: PLR2004
        assert "No changes" in comparison["delta_message"]

    def test_query_compare_all_historical_pods_removed(self) -> None:
        kubearchive = MagicMock()
        kubearchive.query_historical_state.return_value = {
            "namespace": "default",
            "resource_type": "pods",
            "queried_timestamp": "2024-01-01T00:00:00Z",
            "total_resources": 2,
            "pods": [
                {
                    "name": "dead-pod-a",
                    "namespace": "default",
                    "phase": "Running",
                    "restart_count": 0,
                    "queried_timestamp": "2024-01-01T00:00:00Z",
                },
                {
                    "name": "dead-pod-b",
                    "namespace": "default",
                    "phase": "Failed",
                    "restart_count": 5,
                    "queried_timestamp": "2024-01-01T00:00:00Z",
                },
            ],
            "kubearchive_available": True,
            "error": None,
        }
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        service = HistoricalStateQueryService(kubearchive_port=kubearchive, k8s_port=k8s)
        result = service.query(
            QueryKubearchiveCommand(
                namespace="default",
                compare_with_current=True,
                timestamp="2024-01-01T00:00:00Z",
            )
        )

        assert result.comparison is not None
        comparison = result.comparison
        assert comparison is not None
        assert comparison["pods_removed"] == 2  # noqa: PLR2004

    def test_query_compare_all_current_pods_are_new(self) -> None:
        kubearchive = MagicMock()
        kubearchive.query_historical_state.return_value = {
            "namespace": "default",
            "resource_type": "pods",
            "queried_timestamp": "2024-01-01T00:00:00Z",
            "total_resources": 0,
            "pods": [],
            "kubearchive_available": True,
            "error": None,
        }
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {
                "name": "brand-new-pod",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "age": "1h",
            },
        ]

        service = HistoricalStateQueryService(kubearchive_port=kubearchive, k8s_port=k8s)
        result = service.query(
            QueryKubearchiveCommand(
                namespace="default",
                compare_with_current=True,
                timestamp="2024-01-01T00:00:00Z",
            )
        )

        assert result.comparison is not None
        comparison = result.comparison
        assert comparison is not None
        assert comparison["pods_added"] == 1  # noqa: PLR2004

    def test_query_compare_long_delta_message(self) -> None:
        kubearchive = MagicMock()
        kubearchive.query_historical_state.return_value = {
            "namespace": "default",
            "resource_type": "pods",
            "queried_timestamp": "2024-01-01T00:00:00Z",
            "total_resources": 3,
            "pods": [
                {
                    "name": "pod-a",
                    "namespace": "default",
                    "phase": "Running",
                    "restart_count": 0,
                    "queried_timestamp": "2024-01-01T00:00:00Z",
                },
                {
                    "name": "pod-b",
                    "namespace": "default",
                    "phase": "Running",
                    "restart_count": 0,
                    "queried_timestamp": "2024-01-01T00:00:00Z",
                },
                {
                    "name": "pod-c",
                    "namespace": "default",
                    "phase": "Running",
                    "restart_count": 0,
                    "queried_timestamp": "2024-01-01T00:00:00Z",
                },
            ],
            "kubearchive_available": True,
            "error": None,
        }
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {
                "name": "pod-d",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "age": "1h",
            },
        ]

        service = HistoricalStateQueryService(kubearchive_port=kubearchive, k8s_port=k8s)
        result = service.query(
            QueryKubearchiveCommand(
                namespace="default",
                compare_with_current=True,
                timestamp="2024-01-01T00:00:00Z",
            )
        )

        assert result.comparison is not None
        comparison = result.comparison
        assert comparison is not None
        assert comparison["pods_added"] == 1  # noqa: PLR2004
        assert comparison["pods_removed"] == 3  # noqa: PLR2004
        assert "\u22123" in comparison["delta_message"]
        assert "+1" in comparison["delta_message"]
