from hexawyn.application.ports.driven.machine_config_pool_port import MachineConfigPoolPort
from hexawyn.application.use_case.check_machine_config_pool_status.command import (
    CheckMachineConfigPoolStatusCommand,
)
from hexawyn.application.use_case.check_machine_config_pool_status.response import (
    CheckMachineConfigPoolStatusResponse,
)
from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (
    MachineConfigPoolStatusService,
)


class CheckMachineConfigPoolStatusUseCase:
    def __init__(self, machine_config_pool_port: MachineConfigPoolPort) -> None:
        self._port = machine_config_pool_port
        self._engine = MachineConfigPoolStatusService()

    def execute(
        self, command: CheckMachineConfigPoolStatusCommand
    ) -> CheckMachineConfigPoolStatusResponse:
        pools = self._port.list_machine_config_pools()
        result = self._engine.evaluate(pools)
        return CheckMachineConfigPoolStatusResponse(result=result)
