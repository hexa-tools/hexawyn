from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.compute_slo_error_budget.command import (
    ComputeSLOErrorBudgetCommand,
)
from hexawyn.application.use_case.workloads.compute_slo_error_budget.response import (
    ComputeSLOErrorBudgetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ComputeSLOErrorBudgetServicePort(ABC):
    @abstractmethod
    def compute_slo_error_budget(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse: ...
