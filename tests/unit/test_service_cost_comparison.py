"""RED → GREEN — Layer 1: Service Cost Comparison domain models."""

from hexawyn.domain.models.service_cost_comparison import (
    MonthCost,
    ServiceCostBreakdown,
    ServiceCostComparison,
)


class TestServiceCostBreakdown:
    def test_is_frozen(self) -> None:
        import pytest

        b = ServiceCostBreakdown(
            pod_name="pod-1", namespace="prod", cpu_cost=10.0, memory_cost=20.0, total_cost=30.0
        )
        with pytest.raises(Exception):
            b.cpu_cost = 5.0  # type: ignore[misc]


class TestMonthCost:
    def test_is_frozen(self) -> None:
        import pytest

        m = MonthCost(
            month="2026-07", total_cost=100.0, cpu_cost=60.0, memory_cost=40.0, pod_breakdown=[]
        )
        with pytest.raises(Exception):
            m.total_cost = 50.0  # type: ignore[misc]


class TestServiceCostComparison:
    def test_default_values(self) -> None:
        c = ServiceCostComparison()
        assert c.service_name == ""
        assert c.trend == "stable"

    def test_can_populate(self) -> None:
        c = ServiceCostComparison(
            service_name="payment-service",
            cost_delta=50.0,
            cost_delta_pct=25.0,
            trend="increasing",
            recommendation="Review scaling",
        )
        assert c.cost_delta == 50.0
        assert c.trend == "increasing"
