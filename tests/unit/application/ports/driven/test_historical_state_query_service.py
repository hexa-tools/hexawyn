from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.ports.driven.kubearchive_port import (
    HistoricalPodInfo,
    KubeArchivePort,
    KubeArchiveResponse,
)
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_command import (
    QueryKubeArchiveCommand,
)
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_service_port import (
    QueryKubeArchiveServicePort,
)
from hexawyn.application.service.historical_state_query_service import (
    HistoricalStateQueryService,
)
from hexawyn.domain.errors import KubeArchiveUnavailableError


def _make_historical_pod(
    name: str, phase: str = "Running", restart_count: int = 0
) -> HistoricalPodInfo:
    return HistoricalPodInfo(
        name=name,
        namespace="payment",
        phase=phase,
        restart_count=restart_count,
        queried_timestamp="2026-06-09T10:00:00Z",
        currently_exists=True,
        status_changed_since=False,
    )


class TestHistoricalStateQueryService:
    def test_implements_service_port(self) -> None:
        service = HistoricalStateQueryService(
            kubearchive_port=MagicMock(spec=KubeArchivePort),
            k8s_port=MagicMock(spec=K8sPort),
        )
        assert isinstance(service, QueryKubeArchiveServicePort)

    def test_query_returns_pods_from_kubearchive(self) -> None:
        kubearchive = MagicMock(spec=KubeArchivePort)
        kubearchive.query_historical_state.return_value = KubeArchiveResponse(
            namespace="payment",
            resource_type="pods",
            queried_timestamp="2026-06-09T10:00:00Z",
            total_resources=8,
            pods=[
                _make_historical_pod("payment-pod-abc", "Running", 0),
                _make_historical_pod("payment-pod-def", "Running", 8),
                _make_historical_pod("payment-worker-xyz", "CrashLoopBackOff", 23),
            ],
            kubearchive_available=True,
            error=None,
        )

        service = HistoricalStateQueryService(
            kubearchive_port=kubearchive,
            k8s_port=MagicMock(spec=K8sPort),
        )
        result = service.query(
            QueryKubeArchiveCommand(
                namespace="payment",
                resource_type="pods",
                timestamp="2026-06-09T10:00:00Z",
            )
        )

        assert result.total_resources == 8
        assert len(result.pods) == 3
        assert result.error is None

    def test_flag_restarting_pods(self) -> None:
        kubearchive = MagicMock(spec=KubeArchivePort)
        kubearchive.query_historical_state.return_value = KubeArchiveResponse(
            namespace="payment",
            resource_type="pods",
            queried_timestamp="2026-06-09T10:00:00Z",
            total_resources=8,
            pods=[
                _make_historical_pod("payment-pod-abc", "Running", 0),
                _make_historical_pod("payment-pod-def", "Running", 8),
                _make_historical_pod("payment-worker-xyz", "CrashLoopBackOff", 23),
            ],
            kubearchive_available=True,
            error=None,
        )

        service = HistoricalStateQueryService(
            kubearchive_port=kubearchive,
            k8s_port=MagicMock(spec=K8sPort),
        )
        result = service.query(
            QueryKubeArchiveCommand(
                namespace="payment",
                resource_type="pods",
                timestamp="2026-06-09T10:00:00Z",
            )
        )

        pod_names = {p["name"] for p in result.pods}
        assert len(pod_names) == 3

    def test_empty_namespace(self) -> None:
        kubearchive = MagicMock(spec=KubeArchivePort)
        kubearchive.query_historical_state.return_value = KubeArchiveResponse(
            namespace="empty-ns",
            resource_type="pods",
            queried_timestamp="2026-06-09T10:00:00Z",
            total_resources=0,
            pods=[],
            kubearchive_available=True,
            error=None,
        )

        service = HistoricalStateQueryService(
            kubearchive_port=kubearchive,
            k8s_port=MagicMock(spec=K8sPort),
        )
        result = service.query(
            QueryKubeArchiveCommand(
                namespace="empty-ns",
                resource_type="pods",
                timestamp="2026-06-09T10:00:00Z",
            )
        )

        assert result.total_resources == 0
        assert result.pods == []

    def test_kubearchive_unavailable(self) -> None:
        kubearchive = MagicMock(spec=KubeArchivePort)
        kubearchive.query_historical_state.side_effect = KubeArchiveUnavailableError()

        service = HistoricalStateQueryService(
            kubearchive_port=kubearchive,
            k8s_port=MagicMock(spec=K8sPort),
        )
        result = service.query(
            QueryKubeArchiveCommand(
                namespace="payment",
                resource_type="pods",
                timestamp="2026-06-09T10:00:00Z",
            )
        )

        assert result.error is not None
        assert "KubeArchive" in str(result.error)

    def test_compare_with_current_mode(self) -> None:
        kubearchive = MagicMock(spec=KubeArchivePort)
        kubearchive.query_historical_state.return_value = KubeArchiveResponse(
            namespace="payment",
            resource_type="pods",
            queried_timestamp="2026-06-09T10:00:00Z",
            total_resources=8,
            pods=[
                _make_historical_pod("payment-pod-abc", "Running", 0),
                _make_historical_pod("payment-pod-def", "Running", 8),
            ],
            kubearchive_available=True,
            error=None,
        )

        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [
            PodInfo(
                name="payment-pod-abc",
                namespace="payment",
                status="Running",
                restarts=1,
                age="1d",
                node="n1",
            ),
        ]

        service = HistoricalStateQueryService(
            kubearchive_port=kubearchive,
            k8s_port=k8s,
        )
        result = service.query(
            QueryKubeArchiveCommand(
                namespace="payment",
                resource_type="pods",
                timestamp="2026-06-09T10:00:00Z",
                compare_with_current=True,
            )
        )

        k8s.list_pods.assert_called_once_with(namespace="payment")
        assert result.comparison is not None
        assert result.comparison["pods_removed"] == 1
        assert "payment-pod-def" in result.comparison["removed_pod_names"]

    def test_compare_with_added_pods(self) -> None:
        kubearchive = MagicMock(spec=KubeArchivePort)
        kubearchive.query_historical_state.return_value = KubeArchiveResponse(
            namespace="payment",
            resource_type="pods",
            queried_timestamp="2026-06-09T10:00:00Z",
            total_resources=1,
            pods=[
                _make_historical_pod("payment-pod-abc", "Running", 0),
            ],
            kubearchive_available=True,
            error=None,
        )

        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [
            PodInfo(
                name="payment-pod-abc",
                namespace="payment",
                status="Running",
                restarts=0,
                age="1d",
                node="n1",
            ),
            PodInfo(
                name="payment-pod-new",
                namespace="payment",
                status="Running",
                restarts=0,
                age="1d",
                node="n1",
            ),
        ]

        service = HistoricalStateQueryService(
            kubearchive_port=kubearchive,
            k8s_port=k8s,
        )
        result = service.query(
            QueryKubeArchiveCommand(
                namespace="payment",
                resource_type="pods",
                timestamp="2026-06-09T10:00:00Z",
                compare_with_current=True,
            )
        )

        assert result.comparison is not None
        assert result.comparison["pods_added"] == 1
        assert "+1 pod" in result.comparison["delta_message"]
