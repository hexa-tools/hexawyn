from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.compute_slo_error_budget.compute_slo_error_budget_command import (
    ComputeSLOErrorBudgetCommand,
)
from hexawyn.application.ports.driving.compute_slo_error_budget.compute_slo_error_budget_response import (
    ComputeSLOErrorBudgetResponse,
)


class ComputeSLOErrorBudgetServicePort(ABC):
    @abstractmethod
    def compute_slo_error_budget(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse: ...
