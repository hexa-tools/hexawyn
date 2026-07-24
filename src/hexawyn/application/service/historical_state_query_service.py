from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.ports.driven.kubearchive_port import (
    HistoricalComparisonResult,
    HistoricalPodInfo,
    KubeArchivePort,
    KubeArchiveQuery,
)
from hexawyn.application.use_case.query_kubearchive.command import (
    QueryKubeArchiveCommand,
)
from hexawyn.application.use_case.query_kubearchive.response import (
    QueryKubeArchiveResponse,
)
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_service_port import (
    QueryKubeArchiveServicePort,
)
from hexawyn.domain.models.historical_pod import (
    HistoricalPod,
    StateComparison,
)


class HistoricalStateQueryService(QueryKubeArchiveServicePort):
    def __init__(self, kubearchive_port: KubeArchivePort, k8s_port: K8sPort) -> None:
        self._kubearchive = kubearchive_port
        self._k8s = k8s_port

    def query(self, command: QueryKubeArchiveCommand) -> QueryKubeArchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubeArchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubeArchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=pods,
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=result,
            )

        return QueryKubeArchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=pods,
            queried_timestamp=archive_response["queried_timestamp"],
        )

    @staticmethod
    def _pod_exists_in_current(pod_name: str, current_pods: list[PodInfo]) -> bool:
        return any(p["name"] == pod_name for p in current_pods)

    @staticmethod
    def _build_delta_message(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed > 0:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"
            )
        if comparison.pods_added > 0:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if not parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "; ".join(parts)
