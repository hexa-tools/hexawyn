from __future__ import annotations

from hexawyn.application.ports.driving.latency_diagnostic.latency_diagnostic_command import (
    LatencyDiagnosticCommand,
)
from hexawyn.application.ports.driving.latency_diagnostic.latency_diagnostic_response import (
    LatencyDiagnosticResponse,
)
from hexawyn.application.ports.driving.latency_diagnostic.latency_diagnostic_service_port import (
    LatencyDiagnosticServicePort,
)


class LatencyDiagnosticUseCase:
    def __init__(self, service: LatencyDiagnosticServicePort) -> None:
        self._svc = service

    def execute(self, cmd: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        return self._svc.diagnose(cmd)
