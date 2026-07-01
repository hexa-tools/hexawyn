from __future__ import annotations

from hexawyn.application.ports.driving.policy_violations_list.policy_violations_list_command import (
    PolicyViolationsListCommand,
)
from hexawyn.application.ports.driving.policy_violations_list.policy_violations_list_response import (
    PolicyViolationsListResponse,
)
from hexawyn.application.ports.driving.policy_violations_list.policy_violations_list_service_port import (
    PolicyViolationsListServicePort,
)


class PolicyViolationsListUseCase:
    def __init__(self, service: PolicyViolationsListServicePort) -> None:
        self._service = service

    def execute(self, command: PolicyViolationsListCommand) -> PolicyViolationsListResponse:
        return self._service.list_violations(command)
