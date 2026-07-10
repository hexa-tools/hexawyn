from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_command import (  # noqa: E501
    CheckMachineConfigPoolStatusCommand,
)
from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_response import (  # noqa: E501
    CheckMachineConfigPoolStatusResponse,
)


class CheckMachineConfigPoolStatusServicePort(ABC):
    @abstractmethod
    def check(
        self, command: CheckMachineConfigPoolStatusCommand
    ) -> CheckMachineConfigPoolStatusResponse: ...
