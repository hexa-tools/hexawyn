from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.compute_budget_intelligence.command import (
    ComputeBudgetIntelligenceCommand,
)
from hexawyn.application.use_case.finops.compute_budget_intelligence.compute_budget_intelligence_use_case import (  # noqa: E501
    ComputeBudgetIntelligenceUseCase,
)
from hexawyn.application.use_case.finops.compute_budget_intelligence.response import (  # noqa: E501
    ComputeBudgetIntelligenceResponse,
)


class TestComputeBudgetIntelligenceUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_budget_intelligence_data.return_value = {
            "budget_monthly_eur": 5000.0,
            "current_spend_eur": 3000.0,
            "projected_spend_eur": 6000.0,
        }

        use_case = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=port,
        )
        result = use_case.execute(ComputeBudgetIntelligenceCommand(period="2025-Q1"))

        assert isinstance(result, ComputeBudgetIntelligenceResponse)
        assert result.result is not None
