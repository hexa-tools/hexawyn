from __future__ import annotations

from hexawyn.application.ports.driving.detect_zombies.detect_zombies_command import (
    DetectZombiesCommand,
)
from hexawyn.application.ports.driving.detect_zombies.detect_zombies_response import (
    DetectZombiesResponse,
)
from hexawyn.application.ports.driving.detect_zombies.detect_zombies_service_port import (
    DetectZombiesServicePort,
)


class DetectZombiesUseCase:
    def __init__(self, service: DetectZombiesServicePort) -> None:
        self._service = service

    def execute(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        return self._service.detect_zombies(command)
