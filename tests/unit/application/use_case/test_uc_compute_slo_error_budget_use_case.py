"""Unit tests for ComputeSLOErrorBudgetUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.compute_slo_error_budget.compute_slo_error_budget_service_port import (
    ComputeSLOErrorBudgetServicePort,
)
from hexawyn.application.use_case.compute_slo_error_budget.compute_slo_error_budget_use_case import (
    ComputeSLOErrorBudgetUseCase,
)


class TestComputeSLOErrorBudgetUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ComputeSLOErrorBudgetServicePort)
        use_case = ComputeSLOErrorBudgetUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compute_slo_error_budget.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ComputeSLOErrorBudgetServicePort)
        mock_service.compute_slo_error_budget.side_effect = RuntimeError("test error")
        use_case = ComputeSLOErrorBudgetUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
