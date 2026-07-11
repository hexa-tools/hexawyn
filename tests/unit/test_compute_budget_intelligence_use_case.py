from unittest.mock import MagicMock

from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_command import (  # noqa: E501
    ComputeBudgetIntelligenceCommand,
)
from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_response import (  # noqa: E501
    ComputeBudgetIntelligenceResponse,
)
from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_service_port import (  # noqa: E501
    ComputeBudgetIntelligenceServicePort,
)
from hexawyn.domain.models.budget_intelligence import BudgetIntelligenceReport


class TestComputeBudgetIntelligenceUseCase:
    def test_delegates(self) -> None:
        from hexawyn.application.use_case.compute_budget_intelligence.compute_budget_intelligence_use_case import (  # noqa: E501
            ComputeBudgetIntelligenceUseCase,
        )

        service = MagicMock(spec=ComputeBudgetIntelligenceServicePort)
        expected = ComputeBudgetIntelligenceResponse(
            result=BudgetIntelligenceReport(period_label="current")
        )
        service.compute.return_value = expected
        use_case = ComputeBudgetIntelligenceUseCase(service=service)

        response = use_case.execute(ComputeBudgetIntelligenceCommand(period="current"))

        assert response is expected
