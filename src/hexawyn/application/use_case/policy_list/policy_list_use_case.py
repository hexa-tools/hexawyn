from __future__ import annotations

from hexawyn.application.ports.driving.policy_list.policy_list_command import (
    PolicyListCommand,
)
from hexawyn.application.ports.driving.policy_list.policy_list_response import (
    PolicyListResponse,
)
from hexawyn.application.ports.driving.policy_list.policy_list_service_port import (
    PolicyListServicePort,
)


class PolicyListUseCase:
    def __init__(self, service: PolicyListServicePort) -> None:
        self._service = service

    def execute(self, command: PolicyListCommand) -> PolicyListResponse:
        return self._service.list_policies(command)
