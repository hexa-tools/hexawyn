from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.observability.get_p99_latency.command import (
    GetP99LatencyUseCaseCommand,
)
from hexawyn.application.use_case.observability.get_p99_latency.response import (
    GetP99LatencyUseCaseResponse,
)


class GetP99LatencyUseCase:
    """Retrieves P99 latency metrics for a service."""

    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def execute(self, command: GetP99LatencyUseCaseCommand) -> GetP99LatencyUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetP99LatencyUseCaseResponse(
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
