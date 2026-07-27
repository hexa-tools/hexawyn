from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.observability.get_pod_logs.command import (
    GetPodLogsUseCaseCommand,
)
from hexawyn.application.use_case.observability.get_pod_logs.response import (
    GetPodLogsUseCaseResponse,
)


class GetPodLogsUseCase:
    """Retrieves logs for a specific pod."""

    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def execute(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )
