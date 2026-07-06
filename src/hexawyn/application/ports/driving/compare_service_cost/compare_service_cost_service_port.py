from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.compare_service_cost.compare_service_cost_command import (
    CompareServiceCostCommand,
)
from hexawyn.application.ports.driving.compare_service_cost.compare_service_cost_response import (
    CompareServiceCostResponse,
)


class CompareServiceCostServicePort(ABC):
    @abstractmethod
    def compare(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse: ...
