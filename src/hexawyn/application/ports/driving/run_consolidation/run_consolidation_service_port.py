from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.run_consolidation.command import (
    RunConsolidationCommand,
)
from hexawyn.application.use_case.cluster.run_consolidation.response import (
    RunConsolidationResponse,
)


class RunConsolidationServicePort(ABC):
    @abstractmethod
    def execute(self, command: RunConsolidationCommand) -> RunConsolidationResponse: ...
