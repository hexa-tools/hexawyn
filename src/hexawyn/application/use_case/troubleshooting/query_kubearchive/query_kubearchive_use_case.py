from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.kubearchive_port import KubeArchivePort
from hexawyn.application.use_case.troubleshooting.query_kubearchive.command import (
    QueryKubearchiveCommand,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.response import (
    QueryKubearchiveResponse,
)


class QueryKubeArchiveUseCase:
    def __init__(self, kubearchive_port: KubeArchivePort, k8s_port: K8sPort) -> None:
        self._kubearchive_port = kubearchive_port
        self._k8s_port = k8s_port

    def execute(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )
