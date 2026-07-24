from __future__ import annotations

from hexawyn.application.ports.driven.error_budget_port import ErrorBudgetPort
from hexawyn.application.use_case.compute_slo_error_budget.command import (
    ComputeSLOErrorBudgetCommand,
)
from hexawyn.application.use_case.compute_slo_error_budget.response import (
    ComputeSLOErrorBudgetResponse,
)
from hexawyn.application.ports.driving.compute_slo_error_budget.compute_slo_error_budget_service_port import (
    ComputeSLOErrorBudgetServicePort,
)
from hexawyn.domain.services.error_budget.slo_error_budget_engine import (
    SLOErrorBudgetBurnRateEngine,
)


class ComputeSLOErrorBudgetService(ComputeSLOErrorBudgetServicePort):
    def __init__(self, error_budget_port: ErrorBudgetPort) -> None:
        self._port = error_budget_port
        self._engine = SLOErrorBudgetBurnRateEngine()

    def compute_slo_error_budget(
        self, command: ComputeSLOErrorBudgetCommand
    ) -> ComputeSLOErrorBudgetResponse:
        raw = self._port.fetch_success_rate(command.service_name, command.rolling_window_days)
        raw_dict: dict[str, object] = dict(raw)
        result = self._engine.compute(
            slo_target=command.slo_target,
            rolling_window_days=command.rolling_window_days,
            raw_success_rate=raw_dict,
        )
        return ComputeSLOErrorBudgetResponse(result=result)
