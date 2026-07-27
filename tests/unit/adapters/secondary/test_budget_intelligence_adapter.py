from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.budget_intelligence_adapter import BudgetIntelligenceAdapter


class TestBudgetIntelligenceAdapter:
    def test_delegates_to_source(self) -> None:
        source = Mock()
        source.fetch_budget_intelligence_data.return_value = {
            "budget_monthly_eur": 1000.0,
            "projected_spend_eur": 800.0,
            "current_spend_eur": 500.0,
        }
        adapter = BudgetIntelligenceAdapter(source=source)
        result = adapter.get_budget_intelligence_data("2026-07")
        assert result is not None
        source.fetch_budget_intelligence_data.assert_called_once_with("2026-07")
