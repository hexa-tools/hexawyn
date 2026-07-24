from hexawyn.application.ports.driven.error_budget_port import ErrorBudgetPort
from hexawyn.application.use_case.compute_slo_error_budget.command import (
    ComputeSloErrorBudgetCommand,
)
from hexawyn.application.use_case.compute_slo_error_budget.response import (
    ComputeSloErrorBudgetResponse,
)


class ComputeSLOErrorBudgetUseCase:
    def __init__(self, port: ErrorBudgetPort) -> None:
        self._port = port

    def execute(self, command: ComputeSloErrorBudgetCommand) -> ComputeSloErrorBudgetResponse:
        return ComputeSloErrorBudgetResponse()
