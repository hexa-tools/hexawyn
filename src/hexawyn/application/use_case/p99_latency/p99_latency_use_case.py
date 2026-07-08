from __future__ import annotations

from hexawyn.application.ports.driving.p99_latency.p99_latency_command import P99LatencyCommand
from hexawyn.application.ports.driving.p99_latency.p99_latency_response import P99LatencyResponse
from hexawyn.application.ports.driving.p99_latency.p99_latency_service_port import (
    P99LatencyServicePort,
)


class P99LatencyUseCase:
    def __init__(self, service: P99LatencyServicePort) -> None:
        self._svc = service

    def execute(self, cmd: P99LatencyCommand) -> P99LatencyResponse:
        return self._svc.compute_p99(cmd)
