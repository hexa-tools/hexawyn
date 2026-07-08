from __future__ import annotations

from hexawyn.application.ports.driving.rollout_get.rollout_get_command import (
    RolloutGetCommand,
)
from hexawyn.application.ports.driving.rollout_get.rollout_get_response import (
    RolloutGetResponse,
)
from hexawyn.application.ports.driving.rollout_get.rollout_get_service_port import (
    RolloutGetServicePort,
)


class RolloutGetUseCase:
    def __init__(self, service: RolloutGetServicePort) -> None:
        self._service = service

    def execute(self, command: RolloutGetCommand) -> RolloutGetResponse:
        return self._service.get_rollout(command)
