"""RED → GREEN — Service Cost Comparison domain logic."""

from hexawyn.domain.services.service_cost.service_cost_comparison_engine import (
    ServiceCostComparisonEngine,
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
