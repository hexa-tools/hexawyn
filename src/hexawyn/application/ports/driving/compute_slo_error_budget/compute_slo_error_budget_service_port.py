from abc import ABC, abstractmethod

from hexawyn.application.use_case.compute_slo_error_budget.command import (
    ComputeSLOErrorBudgetCommand,
)
from hexawyn.application.use_case.compute_slo_error_budget.response import (
    ComputeSLOErrorBudgetResponse,
)


class ComputeSLOErrorBudgetServicePort(ABC):
    @abstractmethod
    def compute_slo_error_budget(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse: ...
