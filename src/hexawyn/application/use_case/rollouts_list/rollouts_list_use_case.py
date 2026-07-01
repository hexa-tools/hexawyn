from __future__ import annotations

from hexawyn.application.ports.driving.rollouts_list.rollouts_list_command import (
    RolloutsListCommand,
)
from hexawyn.application.ports.driving.rollouts_list.rollouts_list_response import (
    RolloutsListResponse,
)
from hexawyn.application.ports.driving.rollouts_list.rollouts_list_service_port import (
    RolloutsListServicePort,
)


class RolloutsListUseCase:
    def __init__(self, service: RolloutsListServicePort) -> None:
        self._service = service

    def execute(self, command: RolloutsListCommand) -> RolloutsListResponse:
        return self._service.list_rollouts(command)
