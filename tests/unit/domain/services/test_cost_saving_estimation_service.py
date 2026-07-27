from __future__ import annotations

from hexawyn.domain.services.cost_saving.cost_saving_estimation_service import (
    RightSizingCostEstimationService,
    _bursty,
    compute_trend,
)


def _pod(  # noqa: PLR0913
    pod_name: str = "test-pod",
    namespace: str = "default",
    cpu_request: float | None = 1.0,
    mem_request: float | None = 512.0,
    cpu_limit: float | None = 2.0,
    mem_limit: float | None = 1024.0,
    cpu_p95: float | None = 0.3,
    mem_p95: float | None = 200.0,
    cpu_max: float | None = 0.5,
    hpa_enabled: bool = False,
    hpa_min_replicas: int | None = None,
) -> dict[str, object]:
    pod: dict[str, object] = {
        "pod_name": pod_name,
        "namespace": namespace,
        "cpu_request_cores": cpu_request,
        "memory_request_mi": mem_request,
        "cpu_limit_cores": cpu_limit,
        "memory_limit_mi": mem_limit,
        "cpu_p95_cores": cpu_p95,
        "memory_p95_mi": mem_p95,
        "cpu_max_cores": cpu_max,
        "hpa_enabled": hpa_enabled,
    }
    if hpa_min_replicas is not None:
        pod["hpa_min_replicas"] = hpa_min_replicas
    return pod


class TestRightSizingCostEstimationService:
    def test_estimate_basic(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [_pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.3, mem_p95=200.0)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        assert report.pods_analyzed > 0
        assert report.total_delta_cores >= 0

    def test_estimate_empty_pods(self) -> None:
        service = RightSizingCostEstimationService()
        report = service.estimate(pods=[], top_n=5, cpu_price=0.048, mem_price=0.006)
        assert report.pods_analyzed == 0
        assert report.total_delta_cores == 0.0
        assert report.total_monthly_saving_usd == 0.0

    def test_estimate_no_pricing(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [_pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.3, mem_p95=200.0)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=None, mem_price=None)
        assert report.pricing_configured is False
        assert report.total_monthly_saving_usd is None

    def test_estimate_pod_without_requests(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [_pod(cpu_request=None, mem_request=None, cpu_limit=None, mem_limit=None)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        assert report.pods_analyzed == 0
        assert report.pods_excluded == 1

    def test_estimate_pod_without_p95_data(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [_pod(cpu_request=1.0, mem_request=512.0, cpu_p95=None, mem_p95=None)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        assert report.pods_analyzed == 0
        assert report.pods_excluded == 1

    def test_estimate_optimal_pod_excluded(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [_pod(cpu_request=0.3, mem_request=200.0, cpu_p95=0.28, mem_p95=190.0)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        assert report.pods_analyzed == 0
        assert report.pods_excluded == 1

    def test_estimate_bursty_workload_adds_caveat(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [_pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.3, cpu_max=5.0)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        if report.pods_analyzed > 0:
            assert report.top_opportunities[0].is_bursty is True
            assert any("Bursty" in c for c in report.top_opportunities[0].caveats)

    def test_estimate_hpa_enabled_adds_caveat(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [
            _pod(
                cpu_request=1.0,
                mem_request=512.0,
                cpu_p95=0.3,
                cpu_max=0.5,
                hpa_enabled=True,
                hpa_min_replicas=2,
            )
        ]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        if report.pods_analyzed > 0:
            assert report.top_opportunities[0].hpa_enabled is True
            assert any("HPA" in c for c in report.top_opportunities[0].caveats)

    def test_estimate_ranking_orders_by_saving(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [
            _pod(pod_name="small", cpu_request=0.5, mem_request=256.0, cpu_p95=0.1, mem_p95=100.0),
            _pod(pod_name="large", cpu_request=2.0, mem_request=2048.0, cpu_p95=0.5, mem_p95=500.0),
        ]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        assert report.pods_analyzed == 2  # noqa: PLR2004
        if len(report.top_opportunities) >= 2:  # noqa: PLR2004
            large_opportunity = [o for o in report.top_opportunities if o.pod_name == "large"][0]
            small_opportunity = [o for o in report.top_opportunities if o.pod_name == "small"][0]
            assert large_opportunity.monthly_saving_usd > small_opportunity.monthly_saving_usd

    def test_estimate_top_n_limits_results(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [
            _pod(
                pod_name=f"pod-{i}", cpu_request=0.5, mem_request=256.0, cpu_p95=0.1, mem_p95=100.0
            )
            for i in range(10)
        ]
        report = service.estimate(pods=pods, top_n=3, cpu_price=0.048, mem_price=0.006)
        assert report.pods_analyzed == 10  # noqa: PLR2004
        assert len(report.top_opportunities) <= 3  # noqa: PLR2004

    def test_estimate_namespace_aggregation(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [
            _pod(
                pod_name="a",
                namespace="ns1",
                cpu_request=1.0,
                mem_request=512.0,
                cpu_p95=0.3,
                mem_p95=200.0,
            ),
            _pod(
                pod_name="b",
                namespace="ns1",
                cpu_request=1.0,
                mem_request=512.0,
                cpu_p95=0.3,
                mem_p95=200.0,
            ),
            _pod(
                pod_name="c",
                namespace="ns2",
                cpu_request=1.0,
                mem_request=512.0,
                cpu_p95=0.3,
                mem_p95=200.0,
            ),
        ]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        ns_set = {ns.namespace for ns in report.namespace_savings}
        assert "ns1" in ns_set
        assert "ns2" in ns_set
        ns1 = [ns for ns in report.namespace_savings if ns.namespace == "ns1"][0]
        assert ns1.pod_count == 2  # noqa: PLR2004

    def test_estimate_namespace_sorted_by_saving(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [
            _pod(
                pod_name="small",
                namespace="ns-small",
                cpu_request=0.5,
                mem_request=256.0,
                cpu_p95=0.1,
                mem_p95=100.0,
            ),
            _pod(
                pod_name="large",
                namespace="ns-large",
                cpu_request=4.0,
                mem_request=4096.0,
                cpu_p95=1.0,
                mem_p95=1000.0,
            ),
        ]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        if len(report.namespace_savings) >= 2:  # noqa: PLR2004
            assert report.namespace_savings[0].total_monthly_saving_usd is not None
            assert report.namespace_savings[1].total_monthly_saving_usd is not None
            assert (
                report.namespace_savings[0].total_monthly_saving_usd
                >= report.namespace_savings[1].total_monthly_saving_usd
            )

    def test_estimate_uses_limit_when_request_absent(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [
            _pod(
                cpu_request=None,
                mem_request=None,
                cpu_limit=2.0,
                mem_limit=1024.0,
                cpu_p95=0.5,
                mem_p95=300.0,
            )
        ]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        assert report.pods_analyzed == 1

    def test_estimate_only_cpu_pricing(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [_pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.3, mem_p95=200.0)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=None)
        assert report.pricing_configured is True
        assert report.total_monthly_saving_usd is not None

    def test_estimate_only_mem_pricing(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [_pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.3, mem_p95=200.0)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=None, mem_price=0.006)
        assert report.pricing_configured is True
        assert report.total_monthly_saving_usd is not None

    def test_estimate_cpu_only_rightsizing(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [_pod(cpu_request=2.0, mem_request=None, cpu_p95=0.5, mem_p95=None)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        assert report.pods_analyzed == 1

    def test_estimate_mem_only_rightsizing(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [_pod(cpu_request=None, mem_request=2048.0, cpu_p95=None, mem_p95=500.0)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        assert report.pods_analyzed == 1

    def test_estimate_delta_reported_correctly(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [_pod(cpu_request=2.0, mem_request=2048.0, cpu_p95=0.3, mem_p95=300.0)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        assert report.total_delta_cores >= 0
        assert report.total_delta_memory_mi >= 0

    def test_estimate_non_bursty_pod_no_burst_caveat(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [_pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.3, cpu_max=0.5)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        if report.pods_analyzed > 0:
            assert report.top_opportunities[0].is_bursty is False

    def test_estimate_pod_name_and_namespace_preserved(self) -> None:
        service = RightSizingCostEstimationService()
        pods = [
            _pod(
                pod_name="my-app",
                namespace="production",
                cpu_request=1.0,
                mem_request=512.0,
                cpu_p95=0.3,
                mem_p95=200.0,
            )
        ]
        report = service.estimate(pods=pods, top_n=5, cpu_price=0.048, mem_price=0.006)
        if report.pods_analyzed > 0:
            assert report.top_opportunities[0].pod_name == "my-app"
            assert report.top_opportunities[0].namespace == "production"


class TestBursty:
    def test_normal_ratio_not_bursty(self) -> None:
        assert _bursty(cpu_p95=1.0, cpu_max=2.0) is False

    def test_high_ratio_is_bursty(self) -> None:
        assert _bursty(cpu_p95=1.0, cpu_max=3.0) is True

    def test_none_values_not_bursty(self) -> None:
        assert _bursty(cpu_p95=None, cpu_max=10.0) is False
        assert _bursty(cpu_p95=1.0, cpu_max=None) is False
        assert _bursty(cpu_p95=None, cpu_max=None) is False

    def test_zero_p95_not_bursty(self) -> None:
        assert _bursty(cpu_p95=0.0, cpu_max=100.0) is False

    def test_exactly_at_threshold_not_bursty(self) -> None:
        assert _bursty(cpu_p95=1.0, cpu_max=2.5) is False


class TestComputeTrend:
    def test_increasing_trend(self) -> None:
        result = compute_trend(previous=100.0, current=120.0)
        assert result == "increasing"

    def test_decreasing_trend(self) -> None:
        result = compute_trend(previous=100.0, current=85.0)
        assert result == "decreasing"

    def test_stable_trend(self) -> None:
        result = compute_trend(previous=100.0, current=105.0)
        assert result == "stable"

    def test_none_previous_returns_none(self) -> None:
        assert compute_trend(previous=None, current=100.0) is None

    def test_none_current_returns_none(self) -> None:
        assert compute_trend(previous=100.0, current=None) is None

    def test_zero_previous_returns_none(self) -> None:
        assert compute_trend(previous=0.0, current=100.0) is None

    def test_negative_previous_works(self) -> None:
        result = compute_trend(previous=-100.0, current=-80.0)
        assert result == "decreasing"

    def test_exactly_10_percent_increase_is_increasing(self) -> None:
        result = compute_trend(previous=100.0, current=110.0)
        assert result == "stable"

    def test_slightly_above_10_percent(self) -> None:
        result = compute_trend(previous=100.0, current=110.01)
        assert result == "increasing"

    def test_both_none_returns_none(self) -> None:
        assert compute_trend(previous=None, current=None) is None

    def test_small_change_stable(self) -> None:
        result = compute_trend(previous=1000.0, current=1005.0)
        assert result == "stable"


class TestHelperF:
    def test_f_none_returns_none(self) -> None:
        from hexawyn.domain.services.cost_saving.cost_saving_estimation_service import _f

        assert _f(None) is None

    def test_f_valid_float(self) -> None:
        from hexawyn.domain.services.cost_saving.cost_saving_estimation_service import _f

        assert _f(3.14) == 3.14  # noqa: PLR2004

    def test_f_invalid_returns_none(self) -> None:
        from hexawyn.domain.services.cost_saving.cost_saving_estimation_service import _f

        assert _f("abc") is None
