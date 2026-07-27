from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.check_machine_config_pool_status.command import (  # noqa: E501
    CheckMachineConfigPoolStatusCommand,
)
from hexawyn.application.use_case.cluster.check_machine_config_pool_status.response import (  # noqa: E501
    CheckMachineConfigPoolStatusResponse,
)


class CheckMachineConfigPoolStatusServicePort(ABC):
    @abstractmethod
    def check(
        self, command: CheckMachineConfigPoolStatusCommand
    ) -> CheckMachineConfigPoolStatusResponse: ...
