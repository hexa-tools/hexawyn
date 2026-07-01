from __future__ import annotations

from hexawyn.application.ports.driving.policy_get.policy_get_command import (
    PolicyGetCommand,
)
from hexawyn.application.ports.driving.policy_get.policy_get_response import (
    PolicyGetResponse,
)
from hexawyn.application.ports.driving.policy_get.policy_get_service_port import (
    PolicyGetServicePort,
)


class PolicyGetUseCase:
    def __init__(self, service: PolicyGetServicePort) -> None:
        self._service = service

    def execute(self, command: PolicyGetCommand) -> PolicyGetResponse:
        return self._service.get_policy(command)
