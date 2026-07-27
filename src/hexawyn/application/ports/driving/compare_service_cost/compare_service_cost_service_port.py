from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.compare_service_cost.command import (  # noqa: E501
    CompareServiceCostCommand,
)
from hexawyn.application.use_case.finops.compare_service_cost.response import (  # noqa: E501
    CompareServiceCostResponse,
)


class CompareServiceCostServicePort(ABC):
    @abstractmethod
    def compare(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse: ...
