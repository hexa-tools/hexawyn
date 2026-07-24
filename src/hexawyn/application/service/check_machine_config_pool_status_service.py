from __future__ import annotations

from hexawyn.application.ports.driven.machine_config_pool_port import (
    MachineConfigPoolPort,
)
from hexawyn.application.use_case.check_machine_config_pool_status.command import (  # noqa: E501
    CheckMachineConfigPoolStatusCommand,
)
from hexawyn.application.use_case.check_machine_config_pool_status.response import (  # noqa: E501
    CheckMachineConfigPoolStatusResponse,
)
from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_service_port import (  # noqa: E501
    CheckMachineConfigPoolStatusServicePort,
)
from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
    MachineConfigPoolStatusService,
)


class CheckMachineConfigPoolStatusService(CheckMachineConfigPoolStatusServicePort):
    def __init__(self, machine_config_pool_port: MachineConfigPoolPort) -> None:
        self._port = machine_config_pool_port
        self._engine = MachineConfigPoolStatusService()

    def check(
        self, command: CheckMachineConfigPoolStatusCommand
    ) -> CheckMachineConfigPoolStatusResponse:
        pools = self._port.list_machine_config_pools()
        result = self._engine.evaluate(pools)
        return CheckMachineConfigPoolStatusResponse(result=result)
