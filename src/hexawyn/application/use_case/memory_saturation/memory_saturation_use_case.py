from __future__ import annotations

from hexawyn.application.ports.driving.memory_saturation.memory_saturation_command import (
    MemorySaturationCommand,
)
from hexawyn.application.ports.driving.memory_saturation.memory_saturation_response import (
    MemorySaturationResponse,
)
from hexawyn.application.ports.driving.memory_saturation.memory_saturation_service_port import (
    MemorySaturationServicePort,
)


class MemorySaturationUseCase:
    def __init__(self, service: MemorySaturationServicePort) -> None:
        self._svc = service

    def execute(self, cmd: MemorySaturationCommand) -> MemorySaturationResponse:
        return self._svc.predict(cmd)
