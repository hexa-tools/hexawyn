from __future__ import annotations

from hexawyn.application.ports.driven.budget_intelligence_port import (
    BudgetIntelligenceData,
    BudgetIntelligencePort,
)


class _FakeSource:
    def __init__(self, data: BudgetIntelligenceData) -> None:
        self._data = data

    def fetch_budget_intelligence_data(self, period: str) -> BudgetIntelligenceData:
        return self._data


class TestPortImplementation:
    def test_is_budget_intelligence_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_intelligence_adapter import (
            BudgetIntelligenceAdapter,
        )

        data = BudgetIntelligenceData(
            current_spend_eur=0.0, projected_spend_eur=0.0, budget_monthly_eur=None
        )
        assert isinstance(
            BudgetIntelligenceAdapter(source=_FakeSource(data)), BudgetIntelligencePort
        )

    def test_delegates(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_intelligence_adapter import (
            BudgetIntelligenceAdapter,
        )

        data = BudgetIntelligenceData(
            current_spend_eur=4000.0, projected_spend_eur=16000.0, budget_monthly_eur=12000.0
        )
        adapter = BudgetIntelligenceAdapter(source=_FakeSource(data))

        result = adapter.get_budget_intelligence_data("current")

        assert result["budget_monthly_eur"] == 12000.0
