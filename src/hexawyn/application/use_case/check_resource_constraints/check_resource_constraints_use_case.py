from __future__ import annotations

from hexawyn.application.ports.driving.check_resource_constraints.check_resource_constraints_command import (
    CheckResourceConstraintsCommand,
)
from hexawyn.application.ports.driving.check_resource_constraints.check_resource_constraints_response import (
    CheckResourceConstraintsResponse,
)
from hexawyn.application.ports.driving.check_resource_constraints.check_resource_constraints_service_port import (
    CheckResourceConstraintsServicePort,
)


class CheckResourceConstraintsUseCase:
    def __init__(self, service: CheckResourceConstraintsServicePort) -> None:
        self._service = service

    def execute(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        return self._service.check_resource_constraints(command)
