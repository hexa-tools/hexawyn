from __future__ import annotations

from hexawyn.application.ports.driving.rollout_status.rollout_status_command import (
    RolloutStatusCommand,
)
from hexawyn.application.ports.driving.rollout_status.rollout_status_response import (
    RolloutStatusResponse,
)
from hexawyn.application.ports.driving.rollout_status.rollout_status_service_port import (
    RolloutStatusServicePort,
)


class RolloutStatusUseCase:
    def __init__(self, service: RolloutStatusServicePort) -> None:
        self._service = service

    def execute(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        return self._service.get_status(command)
