from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.observability.diagnose_latency_spike.command import (
    DiagnoseLatencySpikeUseCaseCommand,
)
from hexawyn.application.use_case.observability.diagnose_latency_spike.response import (
    DiagnoseLatencySpikeUseCaseResponse,
)


class DiagnoseLatencySpikeUseCase:
    """Diagnoses the root cause of a latency spike."""

    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def execute(
        self, command: DiagnoseLatencySpikeUseCaseCommand
    ) -> DiagnoseLatencySpikeUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return DiagnoseLatencySpikeUseCaseResponse(
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
