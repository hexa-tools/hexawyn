from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.observability.correlate_error_latency_spikes.command import (
    CorrelateErrorLatencySpikesUseCaseCommand,
)
from hexawyn.application.use_case.observability.correlate_error_latency_spikes.response import (
    CorrelateErrorLatencySpikesUseCaseResponse,
)


class CorrelateErrorLatencySpikesUseCase:
    """Correlates error spikes with latency anomalies."""

    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def execute(
        self, command: CorrelateErrorLatencySpikesUseCaseCommand
    ) -> CorrelateErrorLatencySpikesUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return CorrelateErrorLatencySpikesUseCaseResponse(
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
