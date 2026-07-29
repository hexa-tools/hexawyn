from __future__ import annotations

from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter, _resolve_tier
from hexawyn.domain.models.quota import LicenseTier


class TestPricingPlanAdapter:
    def test_get_limit_investigations(self) -> None:
        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        limit = adapter.get_limit("investigations")
        assert limit is not None
        assert limit > 0

    def test_get_limit_clusters(self) -> None:
        adapter = PricingPlanAdapter(tier=LicenseTier.TEAM)
        limit = adapter.get_limit("clusters")
        assert limit is not None

    def test_get_limit_unknown(self) -> None:
        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.get_limit("unknown_feature") is None

    def test_is_available(self) -> None:
        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.is_available("investigations") is True

    def test_is_available_unknown_is_true(self) -> None:
        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.is_available("unknown") is True

    def test_tier_required_returns_none(self) -> None:
        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.tier_required_for("investigations") is None

    def test_tier_required_unknown_returns_none(self) -> None:
        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.tier_required_for("unknown") is None

    def test_resolve_tier_returns_license_tier(self) -> None:
        tier = _resolve_tier()
        assert isinstance(tier, LicenseTier)
