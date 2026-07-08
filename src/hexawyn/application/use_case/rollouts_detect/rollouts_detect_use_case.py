from __future__ import annotations

from hexawyn.application.ports.driving.rollouts_detect.rollouts_detect_command import (
    RolloutsDetectCommand,
)
from hexawyn.application.ports.driving.rollouts_detect.rollouts_detect_response import (
    RolloutsDetectResponse,
)
from hexawyn.application.ports.driving.rollouts_detect.rollouts_detect_service_port import (
    RolloutsDetectServicePort,
)


class RolloutsDetectUseCase:
    def __init__(self, service: RolloutsDetectServicePort) -> None:
        self._service = service

    def execute(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        return self._service.detect(command)
