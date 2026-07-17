import builtins
import sys
from unittest.mock import patch

from hexawyn.application.ports.driven.plan_port import PlanPort
from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort
from hexawyn.domain.models.quota import LicenseTier


class TestPricingPlanAdapter:
    def test_implements_plan_port(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert isinstance(adapter, PlanPort)

    def test_get_limit_investigations_starter(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.get_limit("investigations") == 50

    def test_get_limit_investigations_team(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.TEAM)
        assert adapter.get_limit("investigations") == 500

    def test_get_limit_investigations_scale_up(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.SCALE_UP)
        assert adapter.get_limit("investigations") is None

    def test_get_limit_unknown_resource_returns_none(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.get_limit("nonexistent") is None

    def test_is_available_always_true_for_investigations(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.is_available("investigations") is True

    def test_tier_required_for_returns_none_when_available(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.tier_required_for("investigations") is None

    def test_starter_clusters_limit(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.get_limit("clusters") == 1

    def test_team_clusters_limit(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.TEAM)
        assert adapter.get_limit("clusters") == 3

    def test_scale_up_users_limit(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.SCALE_UP)
        assert adapter.get_limit("users") == 20

    def test_scale_up_unlimited_main_resources(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.SCALE_UP)
        for resource in ["investigations", "slack_alerts", "clusters", "slack_channels"]:
            assert adapter.get_limit(resource) is None, f"{resource} should be unlimited"

    def test_starter_billing_api_limit(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.get_limit("billing_api") == 2

    def test_team_billing_api_unlimited(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.TEAM)
        assert adapter.get_limit("billing_api") is None

    def test_default_tier_is_starter(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.pricing_plan_adapter._resolve_tier",
            return_value=LicenseTier.STARTER,
        ):
            from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

            adapter = PricingPlanAdapter()
            assert adapter.get_limit("investigations") == 50

    def test_is_available_returns_true_when_limit_positive(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.is_available("investigations") is True

    def test_is_available_returns_true_when_unlimited(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.SCALE_UP)
        assert adapter.is_available("investigations") is True

    def test_tier_required_for_returns_none(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.tier_required_for("investigations") is None

    def test_tier_required_for_unknown_resource_returns_none(self) -> None:
        from hexawyn.adapters.secondary.pricing_plan_adapter import PricingPlanAdapter

        adapter = PricingPlanAdapter(tier=LicenseTier.STARTER)
        assert adapter.tier_required_for("nonexistent") is None

    def test_resolve_tier_returns_from_license_manager(self) -> None:
        from unittest.mock import patch

        with patch(
            "hexawyn.infrastructure.config.license_manager.get_license_tier",
            return_value=LicenseTier.TEAM,
        ):
            from hexawyn.adapters.secondary.pricing_plan_adapter import _resolve_tier

            result = _resolve_tier()
            assert result == LicenseTier.TEAM

    def test_resolve_tier_falls_back_to_starter_on_import_error(self) -> None:
        saved = sys.modules.pop("hexawyn.infrastructure.config.license_manager", None)
        try:
            original_import = builtins.__import__

            def selective_import(name: str, *args: object, **kwargs: object) -> object:
                if name == "hexawyn.infrastructure.config.license_manager":
                    raise ImportError("Mocked import failure")
                return original_import(name, *args, **kwargs)

            with patch("builtins.__import__", side_effect=selective_import):
                from hexawyn.adapters.secondary.pricing_plan_adapter import _resolve_tier

                assert _resolve_tier() == LicenseTier.STARTER
        finally:
            if saved is not None:
                sys.modules["hexawyn.infrastructure.config.license_manager"] = saved


class TestUsageMeterAdapter:
    def test_implements_usage_meter_port(self) -> None:
        from hexawyn.adapters.secondary.usage_meter_adapter import UsageMeterAdapter

        adapter = UsageMeterAdapter()
        assert isinstance(adapter, UsageMeterPort)

    def test_get_usage_returns_investigations_count(self) -> None:
        from hexawyn.adapters.secondary.usage_meter_adapter import UsageMeterAdapter

        adapter = UsageMeterAdapter()
        adapter.set_usage("investigations", 23)
        assert adapter.get_usage("investigations") == 23

    def test_get_usage_defaults_to_zero(self) -> None:
        from hexawyn.adapters.secondary.usage_meter_adapter import UsageMeterAdapter

        adapter = UsageMeterAdapter()
        assert adapter.get_usage("unknown_resource") == 0

    def test_set_usage_overwrites(self) -> None:
        from hexawyn.adapters.secondary.usage_meter_adapter import UsageMeterAdapter

        adapter = UsageMeterAdapter()
        adapter.set_usage("clusters", 1)
        adapter.set_usage("clusters", 3)
        assert adapter.get_usage("clusters") == 3

    def test_get_usage_multiple_resources(self) -> None:
        from hexawyn.adapters.secondary.usage_meter_adapter import UsageMeterAdapter

        adapter = UsageMeterAdapter()
        adapter.set_usage("investigations", 45)
        adapter.set_usage("slack_alerts", 3)

        assert adapter.get_usage("investigations") == 45
        assert adapter.get_usage("slack_alerts") == 3
        assert adapter.get_usage("clusters") == 0
