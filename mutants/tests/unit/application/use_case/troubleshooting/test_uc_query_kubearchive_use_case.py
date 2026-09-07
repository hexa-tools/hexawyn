from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.query_kubearchive.command import (
    QueryKubearchiveCommand,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.query_kubearchive_use_case import (  # noqa: E501
    QueryKubeArchiveUseCase,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.response import (  # noqa: E501
    QueryKubearchiveResponse,
)


class TestQueryKubeArchiveUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.query_historical_pods.return_value = []
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = QueryKubeArchiveUseCase(
            kubearchive_port=port,
            k8s_port=k8s,
        )
        result = use_case.execute(QueryKubearchiveCommand(namespace="default"))

        assert isinstance(result, QueryKubearchiveResponse)

    def test_execute_without_comparison(self) -> None:
        port = MagicMock()
        port.query_historical_pods.return_value = []
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = QueryKubeArchiveUseCase(
            kubearchive_port=port,
            k8s_port=k8s,
        )
        result = use_case.execute(
            QueryKubearchiveCommand(
                namespace="default",
                compare_with_current=False,
            )
        )

        assert result.comparison is None

    def test_execute_with_comparison_returns_diff(self) -> None:
        port = MagicMock()
        port.query_historical_state.return_value = {
            "pods": [
                {"name": "pod-a", "namespace": "default"},
                {"name": "pod-b", "namespace": "default"},
            ],
            "total_resources": 2,
            "queried_timestamp": "2026-07-01T00:00:00Z",
            "error": None,
        }

        current_pod_a = MagicMock()
        current_pod_a.name = "pod-a"
        current_pod_b = MagicMock()
        current_pod_b.name = "pod-c"

        k8s = MagicMock()
        k8s.list_pods.return_value = [current_pod_a, current_pod_b]

        use_case = QueryKubeArchiveUseCase(
            kubearchive_port=port,
            k8s_port=k8s,
        )
        result = use_case.execute(
            QueryKubearchiveCommand(
                namespace="default",
                resource_type="pods",
                compare_with_current=True,
                timestamp="2026-07-01T00:00:00Z",
            )
        )

        assert isinstance(result, QueryKubearchiveResponse)
        assert result.total_resources == 2  # noqa: PLR2004
        assert result.queried_timestamp == "2026-07-01T00:00:00Z"
        assert result.comparison is not None
        comparison = result.comparison
        assert comparison["historical_count"] == 2  # noqa: PLR2004
        assert comparison["current_count"] == 2  # noqa: PLR2004
        assert comparison["pods_added"] == 1  # noqa: PLR2004
        assert comparison["pods_removed"] == 1  # noqa: PLR2004
        assert "pod-c" in comparison["added_pod_names"]
        assert "pod-b" in comparison["removed_pod_names"]

    def test_execute_with_comparison_error_falls_back(self) -> None:
        port = MagicMock()
        port.query_historical_state.return_value = {
            "pods": [{"name": "pod-a"}],
            "total_resources": 1,
            "queried_timestamp": "2026-07-01T00:00:00Z",
            "error": None,
        }

        k8s = MagicMock()
        k8s.list_pods.side_effect = Exception("k8s unavailable")

        use_case = QueryKubeArchiveUseCase(
            kubearchive_port=port,
            k8s_port=k8s,
        )
        result = use_case.execute(
            QueryKubearchiveCommand(
                namespace="default",
                resource_type="pods",
                compare_with_current=True,
            )
        )

        assert result.comparison is None
        assert result.total_resources == 1  # noqa: PLR2004
