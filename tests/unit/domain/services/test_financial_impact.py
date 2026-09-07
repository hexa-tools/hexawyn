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


class TestRoundingDiscriminants:
    def test_rounds_to_two_decimals_when_third_differs(self) -> None:
        from hexawyn.domain.services.platform_reliability.financial_impact import (
            compute_financial_impact,
        )

        assert compute_financial_impact(1, 10.55) == 10.55  # noqa: PLR2004

    def test_two_decimal_rounding_not_three(self) -> None:
        from hexawyn.domain.services.platform_reliability.financial_impact import (
            compute_financial_impact,
        )

        assert compute_financial_impact(3, 10.331) == 30.99  # noqa: PLR2004
