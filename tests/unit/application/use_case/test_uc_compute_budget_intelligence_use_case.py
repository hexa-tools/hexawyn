"""Unit tests for ComputeBudgetIntelligenceUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_service_port import (
    ComputeBudgetIntelligenceServicePort,
)
from hexawyn.application.use_case.compute_budget_intelligence.compute_budget_intelligence_use_case import (
    ComputeBudgetIntelligenceUseCase,
)


class TestComputeBudgetIntelligenceUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ComputeBudgetIntelligenceServicePort)
        use_case = ComputeBudgetIntelligenceUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compute.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ComputeBudgetIntelligenceServicePort)
        mock_service.compute.side_effect = RuntimeError("test error")
        use_case = ComputeBudgetIntelligenceUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
