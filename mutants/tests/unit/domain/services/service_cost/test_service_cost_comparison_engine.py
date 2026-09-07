"""RED → GREEN — Service Cost Comparison domain logic."""

import pytest
from hexawyn.domain.models.service_cost_comparison import (
    MonthCost,
    ServiceCostBreakdown,
    ServiceCostComparison,
)
from hexawyn.domain.services.service_cost.service_cost_comparison_engine import (
    ServiceCostComparisonEngine,
    _compute_month_cost,
)


def _pod_data(
    pod_name: str = "payment-service-abc123",
    namespace: str = "production",
    month: str = "2026-07",
    cpu_cores: float = 2.0,
    memory_gb: float = 4.0,
) -> dict[str, object]:
    return {
        "pod_name": pod_name,
        "namespace": namespace,
        "month": month,
        "cpu_cores": cpu_cores,
        "memory_gb": memory_gb,
    }


class TestCostCalculation:
    def test_stable_service_consistent_cost(self) -> None:
        engine = ServiceCostComparisonEngine()
        current = [
            _pod_data(cpu_cores=2.0, memory_gb=4.0),
            _pod_data(pod_name="payment-service-def456", cpu_cores=2.0, memory_gb=4.0),
            _pod_data(pod_name="payment-service-ghi789", cpu_cores=2.0, memory_gb=4.0),
        ]
        previous = [
            _pod_data(month="2026-06", cpu_cores=2.0, memory_gb=4.0),
            _pod_data(
                month="2026-06",
                pod_name="payment-service-def456",
                cpu_cores=2.0,
                memory_gb=4.0,
            ),
            _pod_data(
                month="2026-06",
                pod_name="payment-service-ghi789",
                cpu_cores=2.0,
                memory_gb=4.0,
            ),
        ]

        result = engine.compute(
            service_name="payment-service",
            current_month="2026-07",
            current_days=30,
            previous_month="2026-06",
            previous_days=30,
            current_pods=current,
            previous_pods=previous,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result.current_month.total_cost > 0
        assert abs(result.cost_delta_pct) < 1.0
        assert result.trend == "stable"

    def test_service_scaled_up_cost_increases(self) -> None:
        engine = ServiceCostComparisonEngine()
        current = [_pod_data(cpu_cores=2.0, memory_gb=4.0) for _ in range(10)]
        previous = [_pod_data(month="2026-06", cpu_cores=2.0, memory_gb=4.0) for _ in range(2)]

        result = engine.compute(
            service_name="payment-service",
            current_month="2026-07",
            current_days=31,
            previous_month="2026-06",
            previous_days=30,
            current_pods=current,
            previous_pods=previous,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result.trend == "increasing"
        assert result.cost_delta_pct > 0
        assert len(result.current_month.pod_breakdown) == 10  # noqa: PLR2004

    def test_service_deleted_mid_month_prorated(self) -> None:
        engine = ServiceCostComparisonEngine()
        current = []
        previous = [_pod_data(month="2026-06", cpu_cores=2.0, memory_gb=4.0)]

        result = engine.compute(
            service_name="payment-service",
            current_month="2026-07",
            current_days=31,
            previous_month="2026-06",
            previous_days=30,
            current_pods=current,
            previous_pods=previous,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result.current_month.total_cost == 0.0
        assert result.trend == "decreasing"

    def test_no_data_from_prometheus_fallback(self) -> None:
        engine = ServiceCostComparisonEngine()
        result = engine.compute(
            service_name="payment-service",
            current_month="2026-07",
            current_days=31,
            previous_month="2026-06",
            previous_days=30,
            current_pods=[],
            previous_pods=[],
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result.trend == "no_data"
        assert "No metrics" in result.recommendation

    def test_cost_breakdown_by_pod(self) -> None:
        engine = ServiceCostComparisonEngine()
        pods = [
            _pod_data(pod_name="pod-a", cpu_cores=1.0, memory_gb=2.0),
            _pod_data(pod_name="pod-b", cpu_cores=2.0, memory_gb=4.0),
        ]

        result = engine.compute(
            service_name="test",
            current_month="2026-07",
            current_days=31,
            previous_month="2026-06",
            previous_days=30,
            current_pods=pods,
            previous_pods=[],
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert len(result.current_month.pod_breakdown) == 2  # noqa: PLR2004
        assert result.current_month.pod_breakdown[0].pod_name == "pod-a"
        assert result.current_month.pod_breakdown[1].pod_name == "pod-b"


class TestEdgeCases:
    def test_multiple_namespaces_aggregated(self) -> None:
        engine = ServiceCostComparisonEngine()
        current = [
            _pod_data(namespace="production", pod_name="prod-pod"),
            _pod_data(namespace="staging", pod_name="staging-pod"),
        ]

        result = engine.compute(
            service_name="payment-service",
            current_month="2026-07",
            current_days=31,
            previous_month="2026-06",
            previous_days=30,
            current_pods=current,
            previous_pods=[],
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result.current_month.total_cost > 0

    def test_pod_rescheduled_across_node_pools(self) -> None:
        engine = ServiceCostComparisonEngine()
        pods = [
            _pod_data(cpu_cores=2.0, memory_gb=8.0, pod_name="expensive-pod"),
        ]

        result = engine.compute(
            service_name="test",
            current_month="2026-07",
            current_days=31,
            previous_month="2026-06",
            previous_days=30,
            current_pods=pods,
            previous_pods=[],
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result.current_month.pod_breakdown[0].cpu_cost > 0
        assert result.current_month.pod_breakdown[0].memory_cost > 0

    def test_no_data_when_both_zero(self) -> None:
        engine = ServiceCostComparisonEngine()
        current: list[dict[str, object]] = [
            {
                "pod_name": "empty",
                "namespace": "default",
                "cpu_cores": 0.0,
                "memory_gb": 0.0,
            },
        ]
        previous: list[dict[str, object]] = []
        result = engine.compute(
            service_name="empty-service",
            current_month="2026-07",
            current_days=31,
            previous_month="2026-06",
            previous_days=30,
            current_pods=current,
            previous_pods=previous,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )
        assert result.trend == "no_data"
        assert "No metrics data available" in result.recommendation

    def test_decreasing_trend(self) -> None:
        engine = ServiceCostComparisonEngine()
        current = [_pod_data(cpu_cores=1.0, memory_gb=2.0)]
        previous = [_pod_data(month="2026-06", cpu_cores=10.0, memory_gb=20.0)]
        result = engine.compute(
            service_name="shrinking-service",
            current_month="2026-07",
            current_days=31,
            previous_month="2026-06",
            previous_days=30,
            current_pods=current,
            previous_pods=previous,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )
        assert result.trend == "decreasing"
        assert result.cost_delta < 0

    def test_no_previous_cost_new_service(self) -> None:
        engine = ServiceCostComparisonEngine()
        current = [_pod_data(cpu_cores=2.0, memory_gb=4.0)]
        previous: list[dict[str, object]] = []
        result = engine.compute(
            service_name="new-service",
            current_month="2026-07",
            current_days=31,
            previous_month="2026-06",
            previous_days=30,
            current_pods=current,
            previous_pods=previous,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )
        assert result.trend == "increasing"
        assert result.cost_delta_pct == 100.0  # noqa: PLR2004

    def test_no_previous_cost_both_zero(self) -> None:
        engine = ServiceCostComparisonEngine()
        empty: list[dict[str, object]] = []
        result = engine.compute(
            service_name="dead-service",
            current_month="2026-07",
            current_days=31,
            previous_month="2026-06",
            previous_days=30,
            current_pods=empty,
            previous_pods=empty,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )
        assert result.trend == "no_data"


class TestHelperFunctions:
    def test_as_float_none_returns_zero(self) -> None:
        from hexawyn.domain.services.service_cost.service_cost_comparison_engine import (
            _as_float,
        )

        assert _as_float(None) == 0.0

    def test_as_float_invalid_returns_zero(self) -> None:
        from hexawyn.domain.services.service_cost.service_cost_comparison_engine import (
            _as_float,
        )

        assert _as_float([1, 2]) == 0.0

    def test_current_month_str(self) -> None:
        from hexawyn.domain.services.service_cost.service_cost_comparison_engine import (
            current_month_str,
        )

        result = current_month_str()
        assert "-" in result

    def test_previous_month_str(self) -> None:
        from hexawyn.domain.services.service_cost.service_cost_comparison_engine import (
            previous_month_str,
        )

        result = previous_month_str()
        assert "-" in result

    def test_previous_month_str_format(self) -> None:
        from hexawyn.domain.services.service_cost.service_cost_comparison_engine import (
            previous_month_str,
        )

        result = previous_month_str()
        parts = result.split("-")
        assert len(parts) == 2  # noqa: PLR2004
        assert 2000 <= int(parts[0]) <= 2100  # noqa: PLR2004
        assert 1 <= int(parts[1]) <= 12  # noqa: PLR2004

    def test_previous_month_str_january_rolls_back_year(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        import datetime as datetime_module
        from types import SimpleNamespace

        from hexawyn.domain.services.service_cost.service_cost_comparison_engine import (
            previous_month_str,
        )

        monkeypatch.setattr(
            datetime_module,
            "datetime",
            type(
                "FrozenDatetime",
                (),
                {"now": staticmethod(lambda: SimpleNamespace(year=2026, month=1))},
            ),
        )

        assert previous_month_str() == "2025-12"

    def test_previous_month_str_non_january_subtracts_month(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        import datetime as datetime_module
        from types import SimpleNamespace

        from hexawyn.domain.services.service_cost.service_cost_comparison_engine import (
            previous_month_str,
        )

        monkeypatch.setattr(
            datetime_module,
            "datetime",
            type(
                "FrozenDatetime",
                (),
                {"now": staticmethod(lambda: SimpleNamespace(year=2026, month=9))},
            ),
        )

        assert previous_month_str() == "2026-08"


class TestExactMonthCostPayload:
    def test_single_pod_with_long_decimals(self) -> None:
        result = _compute_month_cost(
            "2026-07",
            1,
            [{"pod_name": "p1", "namespace": "ns", "cpu_cores": 0.1, "memory_gb": 0.07}],
            0.03,
            0.01,
        )

        assert result == MonthCost(
            month="2026-07",
            total_cost=0.09,
            cpu_cost=0.07,
            memory_cost=0.02,
            pod_breakdown=[
                ServiceCostBreakdown(
                    pod_name="p1",
                    namespace="ns",
                    cpu_cost=0.07,
                    memory_cost=0.02,
                    total_cost=0.09,
                )
            ],
        )

    def test_standard_pod_full_month(self) -> None:
        result = _compute_month_cost(
            "2026-07",
            30,
            [{"pod_name": "p1", "namespace": "ns", "cpu_cores": 2.0, "memory_gb": 4.0}],
            0.03,
            0.01,
        )

        assert result == MonthCost(
            month="2026-07",
            total_cost=72.0,
            cpu_cost=43.2,
            memory_cost=28.8,
            pod_breakdown=[
                ServiceCostBreakdown(
                    pod_name="p1",
                    namespace="ns",
                    cpu_cost=43.2,
                    memory_cost=28.8,
                    total_cost=72.0,
                )
            ],
        )

    def test_empty_pods_zero_payload(self) -> None:
        result = _compute_month_cost("2026-07", 30, [], 0.03, 0.01)

        assert result == MonthCost(
            month="2026-07",
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    def test_multiple_pods_sum_costs(self) -> None:
        result = _compute_month_cost(
            "2026-07",
            1,
            [
                {"pod_name": "a", "namespace": "ns", "cpu_cores": 0.1, "memory_gb": 0.07},
                {"pod_name": "b", "namespace": "ns", "cpu_cores": 0.1, "memory_gb": 0.07},
            ],
            0.03,
            0.01,
        )

        assert result == MonthCost(
            month="2026-07",
            total_cost=0.18,
            cpu_cost=0.14,
            memory_cost=0.04,
            pod_breakdown=[
                ServiceCostBreakdown(
                    pod_name="a",
                    namespace="ns",
                    cpu_cost=0.07,
                    memory_cost=0.02,
                    total_cost=0.09,
                ),
                ServiceCostBreakdown(
                    pod_name="b",
                    namespace="ns",
                    cpu_cost=0.07,
                    memory_cost=0.02,
                    total_cost=0.09,
                ),
            ],
        )

    def test_missing_pod_name_and_namespace_default_to_empty(self) -> None:
        result = _compute_month_cost(
            "2026-07",
            1,
            [{"cpu_cores": 0.1, "memory_gb": 0.07}],
            0.03,
            0.01,
        )

        assert result == MonthCost(
            month="2026-07",
            total_cost=0.09,
            cpu_cost=0.07,
            memory_cost=0.02,
            pod_breakdown=[
                ServiceCostBreakdown(
                    pod_name="",
                    namespace="",
                    cpu_cost=0.07,
                    memory_cost=0.02,
                    total_cost=0.09,
                )
            ],
        )

    def test_non_string_pod_fields_coerced(self) -> None:
        result = _compute_month_cost(
            "2026-07",
            1,
            [{"pod_name": 42, "namespace": None, "cpu_cores": 0.1, "memory_gb": 0.07}],
            0.03,
            0.01,
        )

        assert result.pod_breakdown[0].pod_name == "42"
        assert result.pod_breakdown[0].namespace == "None"


class TestExactComparisonPayload:
    def test_exact_scaled_up_payload(self) -> None:
        engine = ServiceCostComparisonEngine()
        current = [
            {"pod_name": "p", "namespace": "prod", "cpu_cores": 0.1, "memory_gb": 0.07},
        ]
        previous = [
            {"pod_name": "p", "namespace": "prod", "cpu_cores": 0.05, "memory_gb": 0.03},
        ]

        result = engine.compute(
            service_name="svc",
            current_month="2026-07",
            current_days=1,
            previous_month="2026-06",
            previous_days=1,
            current_pods=current,
            previous_pods=previous,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result.cost_delta > 0
        assert result.trend == "increasing"
        assert result.service_name == "svc"
        assert result.current_month.month == "2026-07"
        assert result.previous_month.month == "2026-06"

    def test_exactly_ten_percent_increase_is_increasing(self) -> None:
        engine = ServiceCostComparisonEngine()
        current = [
            {"pod_name": f"p{i}", "namespace": "prod", "cpu_cores": 1.0, "memory_gb": 1.0}
            for i in range(11)
        ]
        previous = [
            {"pod_name": f"p{i}", "namespace": "prod", "cpu_cores": 1.0, "memory_gb": 1.0}
            for i in range(10)
        ]

        result = engine.compute(
            service_name="svc",
            current_month="2026-07",
            current_days=1,
            previous_month="2026-06",
            previous_days=1,
            current_pods=current,
            previous_pods=previous,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result.cost_delta_pct == 10.0  # noqa: PLR2004
        assert result.trend == "increasing"

    def test_exactly_ten_percent_decrease_is_decreasing(self) -> None:
        engine = ServiceCostComparisonEngine()
        current = [
            {"pod_name": f"p{i}", "namespace": "prod", "cpu_cores": 1.0, "memory_gb": 1.0}
            for i in range(9)
        ]
        previous = [
            {"pod_name": f"p{i}", "namespace": "prod", "cpu_cores": 1.0, "memory_gb": 1.0}
            for i in range(10)
        ]

        result = engine.compute(
            service_name="svc",
            current_month="2026-07",
            current_days=1,
            previous_month="2026-06",
            previous_days=1,
            current_pods=current,
            previous_pods=previous,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result.cost_delta_pct == -10.0  # noqa: PLR2004
        assert result.trend == "decreasing"

    def test_no_data_exact_recommendation(self) -> None:
        engine = ServiceCostComparisonEngine()
        result = engine.compute(
            service_name="svc",
            current_month="2026-07",
            current_days=31,
            previous_month="2026-06",
            previous_days=30,
            current_pods=[],
            previous_pods=[],
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result.recommendation == (
            "No metrics data available — check Prometheus connectivity"
        )

    def test_new_service_with_sub_unit_cost_counts_as_increasing(self) -> None:
        engine = ServiceCostComparisonEngine()
        result = engine.compute(
            service_name="svc",
            current_month="2026-07",
            current_days=1,
            previous_month="2026-06",
            previous_days=1,
            current_pods=[
                {"pod_name": "p", "namespace": "prod", "cpu_cores": 0.1, "memory_gb": 0.07}
            ],
            previous_pods=[],
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result.previous_month.total_cost == 0.0
        assert result.cost_delta_pct == 100.0  # noqa: PLR2004
        assert result.trend == "increasing"

    def test_no_data_full_payload(self) -> None:
        engine = ServiceCostComparisonEngine()
        result = engine.compute(
            service_name="svc",
            current_month="2026-07",
            current_days=31,
            previous_month="2026-06",
            previous_days=30,
            current_pods=[],
            previous_pods=[],
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result == ServiceCostComparison(
            service_name="svc",
            current_month=MonthCost(
                month="2026-07",
                total_cost=0.0,
                cpu_cost=0.0,
                memory_cost=0.0,
                pod_breakdown=[],
            ),
            previous_month=MonthCost(
                month="2026-06",
                total_cost=0.0,
                cpu_cost=0.0,
                memory_cost=0.0,
                pod_breakdown=[],
            ),
            cost_delta=0.0,
            cost_delta_pct=0.0,
            trend="no_data",
            recommendation="No metrics data available — check Prometheus connectivity",
        )

    def test_increasing_full_payload_with_rounding(self) -> None:
        engine = ServiceCostComparisonEngine()
        result = engine.compute(
            service_name="svc",
            current_month="2026-07",
            current_days=1,
            previous_month="2026-06",
            previous_days=1,
            current_pods=[
                {"pod_name": "p", "namespace": "prod", "cpu_cores": 1.0, "memory_gb": 1.0}
            ],
            previous_pods=[
                {"pod_name": "p", "namespace": "prod", "cpu_cores": 0.9, "memory_gb": 0.9}
            ],
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result == ServiceCostComparison(
            service_name="svc",
            current_month=MonthCost(
                month="2026-07",
                total_cost=0.96,
                cpu_cost=0.72,
                memory_cost=0.24,
                pod_breakdown=[
                    ServiceCostBreakdown(
                        pod_name="p",
                        namespace="prod",
                        cpu_cost=0.72,
                        memory_cost=0.24,
                        total_cost=0.96,
                    )
                ],
            ),
            previous_month=MonthCost(
                month="2026-06",
                total_cost=0.87,
                cpu_cost=0.65,
                memory_cost=0.22,
                pod_breakdown=[
                    ServiceCostBreakdown(
                        pod_name="p",
                        namespace="prod",
                        cpu_cost=0.65,
                        memory_cost=0.22,
                        total_cost=0.87,
                    )
                ],
            ),
            cost_delta=0.09,
            cost_delta_pct=10.3,
            trend="increasing",
            recommendation="Cost increased by 10% — review scaling decisions",
        )

    def test_decreasing_full_payload(self) -> None:
        engine = ServiceCostComparisonEngine()
        result = engine.compute(
            service_name="svc",
            current_month="2026-07",
            current_days=1,
            previous_month="2026-06",
            previous_days=1,
            current_pods=[
                {"pod_name": "p", "namespace": "prod", "cpu_cores": 1.0, "memory_gb": 1.0}
            ],
            previous_pods=[
                {"pod_name": "p", "namespace": "prod", "cpu_cores": 2.0, "memory_gb": 2.0}
            ],
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result == ServiceCostComparison(
            service_name="svc",
            current_month=MonthCost(
                month="2026-07",
                total_cost=0.96,
                cpu_cost=0.72,
                memory_cost=0.24,
                pod_breakdown=[
                    ServiceCostBreakdown(
                        pod_name="p",
                        namespace="prod",
                        cpu_cost=0.72,
                        memory_cost=0.24,
                        total_cost=0.96,
                    )
                ],
            ),
            previous_month=MonthCost(
                month="2026-06",
                total_cost=1.92,
                cpu_cost=1.44,
                memory_cost=0.48,
                pod_breakdown=[
                    ServiceCostBreakdown(
                        pod_name="p",
                        namespace="prod",
                        cpu_cost=1.44,
                        memory_cost=0.48,
                        total_cost=1.92,
                    )
                ],
            ),
            cost_delta=-0.96,
            cost_delta_pct=-50.0,
            trend="decreasing",
            recommendation="Cost decreased by 50% — optimization efforts paying off",
        )

    def test_stable_full_payload(self) -> None:
        engine = ServiceCostComparisonEngine()
        pods = [{"pod_name": "p", "namespace": "prod", "cpu_cores": 1.0, "memory_gb": 1.0}]

        result = engine.compute(
            service_name="svc",
            current_month="2026-07",
            current_days=1,
            previous_month="2026-06",
            previous_days=1,
            current_pods=pods,
            previous_pods=pods,
            cpu_price_per_core_hour=0.03,
            memory_price_per_gb_hour=0.01,
        )

        assert result == ServiceCostComparison(
            service_name="svc",
            current_month=MonthCost(
                month="2026-07",
                total_cost=0.96,
                cpu_cost=0.72,
                memory_cost=0.24,
                pod_breakdown=[
                    ServiceCostBreakdown(
                        pod_name="p",
                        namespace="prod",
                        cpu_cost=0.72,
                        memory_cost=0.24,
                        total_cost=0.96,
                    )
                ],
            ),
            previous_month=MonthCost(
                month="2026-06",
                total_cost=0.96,
                cpu_cost=0.72,
                memory_cost=0.24,
                pod_breakdown=[
                    ServiceCostBreakdown(
                        pod_name="p",
                        namespace="prod",
                        cpu_cost=0.72,
                        memory_cost=0.24,
                        total_cost=0.96,
                    )
                ],
            ),
            cost_delta=0.0,
            cost_delta_pct=0.0,
            trend="stable",
            recommendation="Cost is stable month-over-month",
        )
