from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.workloads.compute_slo_error_budget.command import (
    ComputeSLOErrorBudgetCommand,
)
from hexawyn.application.use_case.workloads.compute_slo_error_budget.compute_slo_error_budget_use_case import (  # noqa: E501
    ComputeSLOErrorBudgetUseCase,
)
from hexawyn.application.use_case.workloads.compute_slo_error_budget.response import (
    ComputeSLOErrorBudgetResponse,
)


class TestComputeSloErrorBudgetUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_success_rate.return_value = {
            "success_rate": 99.9,
            "total_requests": 10000,
            "error_count": 10,
        }

        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=port)
        result = use_case.compute_slo_error_budget(
            ComputeSLOErrorBudgetCommand(
                service_name="api",
                slo_target=99.9,
                rolling_window_days=30,
            )
        )

        assert isinstance(result, ComputeSLOErrorBudgetResponse)
