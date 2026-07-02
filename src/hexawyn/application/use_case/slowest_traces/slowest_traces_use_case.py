from __future__ import annotations

from hexawyn.application.ports.driving.slowest_traces.slowest_traces_command import (
    SlowestTracesCommand,
)
from hexawyn.application.ports.driving.slowest_traces.slowest_traces_response import (
    SlowestTracesResponse,
)
from hexawyn.application.ports.driving.slowest_traces.slowest_traces_service_port import (
    SlowestTracesServicePort,
)


class SlowestTracesUseCase:
    def __init__(self, service: SlowestTracesServicePort) -> None:
        self._svc = service

    def execute(self, cmd: SlowestTracesCommand) -> SlowestTracesResponse:
        return self._svc.find_slowest(cmd)
