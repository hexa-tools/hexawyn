from __future__ import annotations

from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter


class TestPricingPlanAdapterNeutral:
    def test_get_limit_is_neutral_none(self) -> None:
        adapter = PricingPlanAdapter()
        assert adapter.get_limit("investigations") is None

    def test_get_limit_unknown_is_none(self) -> None:
        adapter = PricingPlanAdapter()
        assert adapter.get_limit("unknown_feature") is None

    def test_is_available_is_true_when_neutral(self) -> None:
        adapter = PricingPlanAdapter()
        assert adapter.is_available("investigations") is True

    def test_is_available_unknown_is_true(self) -> None:
        adapter = PricingPlanAdapter()
        assert adapter.is_available("unknown") is True

    def test_tier_required_returns_none(self) -> None:
        adapter = PricingPlanAdapter()
        assert adapter.tier_required_for("investigations") is None

    def test_tier_required_unknown_returns_none(self) -> None:
        adapter = PricingPlanAdapter()
        assert adapter.tier_required_for("unknown") is None
