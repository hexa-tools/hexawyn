from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.compare_service_cost.command import (  # noqa: E501
    CompareServiceCostCommand,
)
from hexawyn.application.use_case.finops.compare_service_cost.response import (  # noqa: E501
    CompareServiceCostResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CompareServiceCostServicePort(ABC):
    @abstractmethod
    def compare(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse: ...
