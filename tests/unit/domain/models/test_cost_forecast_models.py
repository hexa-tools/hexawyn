"""RED — Layer 1: CostForecast domain models."""

from hexawyn.domain.models.cost_forecast import BillingEvent, CostForecast, ResourceCost


class TestResourceCost:
    def test_is_frozen(self) -> None:
        rc = ResourceCost(
            name="payments", kind="namespace", monthly_cost_usd=340.0, percentage=27.3
        )
        try:
            rc.name = "other"  # type: ignore[misc]
            assert False, "should be frozen"
        except Exception:
            pass

    def test_fields(self) -> None:
        rc = ResourceCost(
            name="payments", kind="namespace", monthly_cost_usd=340.0, percentage=27.3
        )
        assert rc.name == "payments"
        assert rc.kind == "namespace"
        assert rc.monthly_cost_usd == 340.0
        assert rc.percentage == 27.3


class TestBillingEvent:
    def test_is_frozen(self) -> None:
        ev = BillingEvent(
            date="2026-06-30", description="spot expiry", cost_impact_usd=200.0, provider="aws"
        )
        try:
            ev.date = "other"  # type: ignore[misc]
            assert False, "should be frozen"
        except Exception:
            pass

    def test_fields(self) -> None:
        ev = BillingEvent(
            date="2026-06-30", description="spot expiry", cost_impact_usd=200.0, provider="aws"
        )
        assert ev.date == "2026-06-30"
        assert ev.cost_impact_usd == 200.0
        assert ev.provider == "aws"


class TestCostForecast:
    def _make(self) -> CostForecast:
        return CostForecast(
            cluster_name="prod",
            month="2026-06",
            days_elapsed=22,
            days_remaining=8,
            current_spend_usd=1247.0,
            projected_total_usd=1703.0,
            previous_month_usd=1367.0,
            month_over_month_delta=24.6,
            trend_factor=1.12,
            top_cost_drivers=[],
            billing_events=[],
            forecast_confidence="low",
            historical_days_used=7,
            data_source="estimated",
        )

    def test_fields(self) -> None:
        f = self._make()
        assert f.cluster_name == "prod"
        assert f.days_elapsed == 22
        assert f.days_remaining == 8
        assert f.projected_total_usd == 1703.0
        assert f.previous_month_usd == 1367.0
        assert f.trend_factor == 1.12
        assert f.forecast_confidence == "low"
        assert f.data_source == "estimated"

    def test_previous_month_can_be_none(self) -> None:
        f = self._make()
        f.previous_month_usd = None
        assert f.previous_month_usd is None

    def test_billing_events_default_empty(self) -> None:
        f = self._make()
        assert f.billing_events == []

    def test_top_cost_drivers_accepts_list(self) -> None:
        rc = ResourceCost(
            name="ml-worker", kind="namespace", monthly_cost_usd=387.0, percentage=22.7
        )
        f = self._make()
        f.top_cost_drivers = [rc]
        assert len(f.top_cost_drivers) == 1
