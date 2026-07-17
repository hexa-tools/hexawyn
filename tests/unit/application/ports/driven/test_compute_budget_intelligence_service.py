from unittest.mock import MagicMock

from hexawyn.application.ports.driven.budget_intelligence_port import (
    BudgetIntelligenceData,
    BudgetIntelligencePort,
)
from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_command import (  # noqa: E501
    ComputeBudgetIntelligenceCommand,
)


def _data() -> BudgetIntelligenceData:
    return BudgetIntelligenceData(
        current_spend_eur=4000.0, projected_spend_eur=16000.0, budget_monthly_eur=12000.0
    )


class TestComputeBudgetIntelligenceService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_service_port import (  # noqa: E501
            ComputeBudgetIntelligenceServicePort,
        )
        from hexawyn.application.service.compute_budget_intelligence_service import (
            ComputeBudgetIntelligenceService,
        )

        service = ComputeBudgetIntelligenceService(
            budget_intelligence_port=MagicMock(spec=BudgetIntelligencePort)
        )

        assert isinstance(service, ComputeBudgetIntelligenceServicePort)

    def test_compute_returns_report(self) -> None:
        from hexawyn.application.service.compute_budget_intelligence_service import (
            ComputeBudgetIntelligenceService,
        )

        port = MagicMock(spec=BudgetIntelligencePort)
        port.get_budget_intelligence_data.return_value = _data()
        service = ComputeBudgetIntelligenceService(budget_intelligence_port=port)

        response = service.compute(ComputeBudgetIntelligenceCommand(period="current"))

        assert response.result.budget_exceeded is True
        assert len(response.result.recommendations) == 3
