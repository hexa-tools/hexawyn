from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.compute_budget_intelligence.command import (  # noqa: E501
    ComputeBudgetIntelligenceCommand,
)
from hexawyn.application.use_case.finops.compute_budget_intelligence.response import (  # noqa: E501
    ComputeBudgetIntelligenceResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ComputeBudgetIntelligenceServicePort(ABC):
    @abstractmethod
    def compute(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse: ...
