from __future__ import annotations

from hexawyn.application.ports.driving.compute_slo_error_budget.compute_slo_error_budget_command import (
    ComputeSLOErrorBudgetCommand,
)
from hexawyn.application.ports.driving.compute_slo_error_budget.compute_slo_error_budget_response import (
    ComputeSLOErrorBudgetResponse,
)
from hexawyn.application.ports.driving.compute_slo_error_budget.compute_slo_error_budget_service_port import (
    ComputeSLOErrorBudgetServicePort,
)


class ComputeSLOErrorBudgetUseCase:
    def __init__(self, service: ComputeSLOErrorBudgetServicePort) -> None:
        self._service = service

    def execute(self, command: ComputeSLOErrorBudgetCommand) -> ComputeSLOErrorBudgetResponse:
        return self._service.compute_slo_error_budget(command)
