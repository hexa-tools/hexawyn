from hexawyn.domain.models.budget_intelligence import BudgetIntelligenceReport


class TestComputeBudgetIntelligenceResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.use_case.finops.compute_budget_intelligence.response import (  # noqa: E501
            ComputeBudgetIntelligenceResponse,
        )

        report = BudgetIntelligenceReport(period_label="2026-06")
        response = ComputeBudgetIntelligenceResponse(result=report)

        assert response.result is report
