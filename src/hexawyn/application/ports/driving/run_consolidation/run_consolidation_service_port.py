from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.run_consolidation.run_consolidation_command import (
    RunConsolidationCommand,
)
from hexawyn.application.ports.driving.run_consolidation.run_consolidation_response import (
    RunConsolidationResponse,
)


class RunConsolidationServicePort(ABC):
    @abstractmethod
    def execute(self, command: RunConsolidationCommand) -> RunConsolidationResponse: ...
