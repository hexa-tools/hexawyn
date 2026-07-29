from __future__ import annotations


class TestFinancialImpact:
    def test_none_when_pricing_not_configured(self) -> None:
        from hexawyn.domain.services.platform_reliability.financial_impact import (
            compute_financial_impact,
        )

        result = compute_financial_impact(total_downtime_minutes=120, cost_per_minute=None)

        assert result is None

    def test_computed_when_pricing_configured(self) -> None:
        from hexawyn.domain.services.platform_reliability.financial_impact import (
            compute_financial_impact,
        )

        result = compute_financial_impact(total_downtime_minutes=120, cost_per_minute=10.0)

        assert result == 1200.0  # noqa: PLR2004

    def test_zero_downtime_zero_impact(self) -> None:
        from hexawyn.domain.services.platform_reliability.financial_impact import (
            compute_financial_impact,
        )

        result = compute_financial_impact(total_downtime_minutes=0, cost_per_minute=10.0)

        assert result == 0.0

    def test_zero_cost_configured_is_zero_not_none(self) -> None:
        from hexawyn.domain.services.platform_reliability.financial_impact import (
            compute_financial_impact,
        )

        result = compute_financial_impact(total_downtime_minutes=120, cost_per_minute=0.0)

        assert result == 0.0
