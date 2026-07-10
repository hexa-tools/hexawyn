from __future__ import annotations

from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_command import (  # noqa: E501
    CheckMachineConfigPoolStatusCommand,
)
from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_response import (  # noqa: E501
    CheckMachineConfigPoolStatusResponse,
)
from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_service_port import (  # noqa: E501
    CheckMachineConfigPoolStatusServicePort,
)


class CheckMachineConfigPoolStatusUseCase:
    def __init__(self, service: CheckMachineConfigPoolStatusServicePort) -> None:
        self._service = service

    def execute(
        self, command: CheckMachineConfigPoolStatusCommand
    ) -> CheckMachineConfigPoolStatusResponse:
        return self._service.check(command)
