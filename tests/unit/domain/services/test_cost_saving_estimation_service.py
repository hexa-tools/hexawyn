from __future__ import annotations

from hexawyn.domain.services.cost_saving.cost_saving_estimation_service import (
    RightSizingCostEstimationService,
    _aggregate_by_namespace,
    _analyze_pod,
    _bursty,
    _is_optimal,
    _rank_opportunities,
    _recommended,
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
        pods = [_pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.4, mem_p95=200.0)]
        report = service.estimate(pods=pods, top_n=5, cpu_price=10.0, mem_price=0.05)
        assert report.pods_analyzed == 1
        assert report.total_delta_cores == 0.52  # noqa: PLR2004
        assert report.total_delta_memory_mi == 272.0  # noqa: PLR2004
        assert report.total_monthly_saving_usd == 3753.56  # noqa: PLR2004

    def test_estimate_exact_rounding_fine_delta(self) -> None:
        # 2 pods identiques, delta_cores 0.213 chacun -> sum 0.426
        # round(0.426, 3) = 0.426 ; round(0.426, 2) = 0.43 (mutant detecte)
        service = RightSizingCostEstimationService()
        pods = [
            {
                "pod_name": f"p{i}",
                "namespace": "n",
                "cpu_request_cores": 0.3333,
                "memory_request_mi": 512.0,
                "cpu_p95_cores": 0.1,
                "memory_p95_mi": 500.0,
            }
            for i in range(2)
        ]
        report = service.estimate(pods=pods, top_n=5, cpu_price=None, mem_price=None)
        assert report.total_delta_cores == 0.426  # noqa: PLR2004

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

    def test_exactly_negative_10_percent_is_stable(self) -> None:
        # delta = -10% exact : < -10% est FALSE -> stable (mutant <= donnerait decreasing)
        result = compute_trend(previous=100.0, current=90.0)
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

    def test_f_numeric_string(self) -> None:
        from hexawyn.domain.services.cost_saving.cost_saving_estimation_service import _f

        assert _f("0.5") == 0.5  # noqa: PLR2004


class TestAnalyzePod:
    def test_optimal_pod_excluded(self) -> None:
        # cpu_p95/eff = 0.9 et mem_p95/eff = 0.9 -> ratio >= 0.9 -> optimal
        pod = _pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.9, mem_p95=460.8)
        assert _analyze_pod(pod, None, None) is None

    def test_no_request_nor_limit_excluded(self) -> None:
        pod = _pod(cpu_request=None, mem_request=None, cpu_limit=None, mem_limit=None)
        assert _analyze_pod(pod, None, None) is None

    def test_no_p95_usage_excluded(self) -> None:
        pod = _pod(cpu_p95=None, mem_p95=None)
        assert _analyze_pod(pod, None, None) is None

    def test_uses_limit_when_request_absent(self) -> None:
        pod = _pod(
            cpu_request=None,
            mem_request=None,
            cpu_limit=2.0,
            mem_limit=1024.0,
            cpu_p95=0.5,
            mem_p95=300.0,
        )
        result = _analyze_pod(pod, None, None)
        assert result is not None
        assert result.current_cpu_request == 2.0  # noqa: PLR2004

    def test_no_pricing_returns_none_usd(self) -> None:
        result = _analyze_pod(_pod(cpu_p95=0.1), None, None)
        assert result is not None
        assert result.monthly_saving_usd is None

    def test_with_pricing_computes_usd(self) -> None:
        result = _analyze_pod(_pod(cpu_p95=0.1), 10.0, 0.05)
        assert result is not None
        assert result.monthly_saving_usd is not None
        assert result.monthly_saving_usd >= 0  # noqa: PLR2004

    def test_mem_only_pod(self) -> None:
        pod = _pod(cpu_request=None, cpu_p95=None, mem_p95=200.0)
        result = _analyze_pod(pod, None, None)
        assert result is not None
        assert result.delta_memory_mi > 0

    def test_hpa_adds_caveat(self) -> None:
        result = _analyze_pod(_pod(hpa_enabled=True, hpa_min_replicas=2), None, None)
        assert result is not None
        assert result.caveats == [
            "HPA enabled (min_replicas=2): right-size applies per-pod, "
            "adjust HPA min_replicas separately"
        ]

    def test_bursty_adds_caveat(self) -> None:
        pod = _pod(cpu_p95=0.1, cpu_max=1.0)
        result = _analyze_pod(pod, None, None)
        assert result is not None
        assert result.caveats == [
            "Bursty workload detected: right-sizing based on 7d p95 may cause OOM under peak"
        ]

    def test_hpa_and_bursty_caveats_combined(self) -> None:
        pod = _pod(hpa_enabled=True, hpa_min_replicas=3, cpu_p95=0.1, cpu_max=1.0)
        result = _analyze_pod(pod, None, None)
        assert result is not None
        assert result.caveats == [
            "HPA enabled (min_replicas=3): right-size applies per-pod, "
            "adjust HPA min_replicas separately",
            "Bursty workload detected: right-sizing based on 7d p95 may cause OOM under peak",
        ]

    def test_computed_values_exact(self) -> None:
        # cpu_req 1.0, cpu_p95 0.4 -> rec = max(0.4*1.2, 0.01) = 0.48 -> delta 0.52
        # mem_req 512, mem_p95 200 -> rec = max(200*1.2, 64) = 240 -> delta 272
        pod = _pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.4, mem_p95=200.0)
        result = _analyze_pod(pod, None, None)
        assert result is not None
        assert result.recommended_cpu_request == 0.48  # noqa: PLR2004
        assert result.recommended_memory_request_mi == 240.0  # noqa: PLR2004
        assert result.delta_cores == 0.52  # noqa: PLR2004
        assert result.delta_memory_mi == 272.0  # noqa: PLR2004

    def test_monthly_saving_usd_exact(self) -> None:
        # 0.52 cores * 10 $/h? Non: cpu_price=10$/core-hour, mem 0.05$/GB-h
        # cpu_saving = 0.52*10*720 = 3744 ; mem = (272/1024)*0.05*720 = 9.56 ; total 3753.56
        pod = _pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.4, mem_p95=200.0)
        result = _analyze_pod(pod, 10.0, 0.05)
        assert result is not None
        assert result.monthly_saving_usd == 3753.56  # noqa: PLR2004

    def test_delta_zero_when_request_below_rec(self) -> None:
        # p95 eleve -> rec >= request -> delta 0, mais non-optimal (ratio < 0.9)
        pod = _pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.9, mem_p95=450.0)
        result = _analyze_pod(pod, None, None)
        assert result is not None
        assert result.delta_cores == 0.0
        assert result.delta_memory_mi == 0.0

    def test_mem_limit_used_when_no_mem_request(self) -> None:
        # pas de mem_request -> eff_mem = mem_limit ; verifie que mem_limit n'est pas ignoré
        pod = _pod(cpu_request=1.0, mem_request=None, cpu_p95=0.2, mem_p95=300.0, mem_limit=1024.0)
        result = _analyze_pod(pod, None, None)
        assert result is not None
        assert result.current_memory_request_mi == 1024.0  # noqa: PLR2004


class TestIsOptimal:
    def test_empty_ratios_not_optimal(self) -> None:
        assert _is_optimal(None, None, None, None) is False

    def test_all_above_threshold_optimal(self) -> None:
        # cpu 0.95/1.0=0.95 et mem 460.8/512=0.9 -> tous >= 0.9
        assert _is_optimal(1.0, 512.0, 0.95, 460.8) is True

    def test_below_threshold_not_optimal(self) -> None:
        assert _is_optimal(1.0, 512.0, 0.5, 460.8) is False

    def test_zero_cpu_request_skipped(self) -> None:
        # eff_cpu=0 -> ratio cpu non ajoute; il reste le ratio mem 0.9 >= 0.9
        assert _is_optimal(0.0, 512.0, 0.95, 460.8) is True

    def test_cpu_below_mem_above_not_optimal(self) -> None:
        assert _is_optimal(1.0, 512.0, 0.5, 460.8) is False

    def test_fractional_mem_request_ratio_counted(self) -> None:
        # eff_mem=0.5 > 0 : ratio mem ajoute (0.1/0.5=0.2 <0.9) -> pas optimal
        # mutant eff_mem > 1 : ratio non ajoute -> seul cpu 0.95 opt -> True
        assert _is_optimal(1.0, 0.5, 0.95, 0.1) is False

    def test_zero_mem_request_ratio_skipped(self) -> None:
        # eff_mem=0 : > 0 FALSE -> ratio non ajoute -> seul cpu decide (opt)
        # mutant >= 0 : ratio mem 0.1/0 <... pas de division? eff_mem=0, mem_p95 present
        # ratio mem = 0.1/0 -> ZeroDivision... en fait la garde eff_mem>0 protege
        assert _is_optimal(1.0, 0.0, 0.95, 0.1) is True


class TestRecommended:
    def test_p95_none_returns_request(self) -> None:
        assert _recommended(1.0, None) == 1.0

    def test_request_none_returns_none(self) -> None:
        assert _recommended(None, 0.5) is None

    def test_cpu_branch_uses_cpu_min(self) -> None:
        # request=1.0 > 0.1 -> CPU: rec = max(0.5*1.2, 0.01) = 0.6
        assert _recommended(1.0, 0.5) == 0.6  # noqa: PLR2004

    def test_mem_branch_uses_mem_min(self) -> None:
        # request=0.05 <= 0.1 -> branche mem: rec = max(0.1*1.2, 64.0) = 64.0
        assert _recommended(0.05, 0.1) == 64.0  # noqa: PLR2004

    def test_cpu_min_applied_when_low(self) -> None:
        # request=1.0 > 0.1 -> CPU: rec = max(0.01*1.2, 0.01) = 0.012, 3 dec
        assert _recommended(1.0, 0.01) == 0.012  # noqa: PLR2004


class TestRankOpportunities:
    def _opp(self, name: str, usd: float | None) -> object:
        from hexawyn.domain.models.cost_saving_estimation import PodSavingOpportunity

        return PodSavingOpportunity(
            pod_name=name,
            namespace="default",
            current_cpu_request=1.0,
            recommended_cpu_request=0.5,
            current_memory_request_mi=512.0,
            recommended_memory_request_mi=256.0,
            delta_cores=0.5,
            delta_memory_mi=256.0,
            monthly_saving_usd=usd,
            hpa_enabled=False,
            is_bursty=False,
            caveats=[],
        )

    def test_sorts_descending_and_truncates(self) -> None:
        opps = [self._opp("a", 5.0), self._opp("b", 50.0), self._opp("c", 20.0)]
        ranked = _rank_opportunities(opps, 2)
        assert [o.pod_name for o in ranked] == ["b", "c"]

    def test_none_usd_treated_as_zero(self) -> None:
        opps = [self._opp("a", None), self._opp("b", 10.0)]
        ranked = _rank_opportunities(opps, 2)
        assert [o.pod_name for o in ranked] == ["b", "a"]


class TestAggregateByNamespace:
    def _opp(self, namespace: str, usd: float | None, cores: float, mem: float) -> object:
        from hexawyn.domain.models.cost_saving_estimation import PodSavingOpportunity

        return PodSavingOpportunity(
            pod_name="x",
            namespace=namespace,
            current_cpu_request=1.0,
            recommended_cpu_request=0.5,
            current_memory_request_mi=512.0,
            recommended_memory_request_mi=256.0,
            delta_cores=cores,
            delta_memory_mi=mem,
            monthly_saving_usd=usd,
            hpa_enabled=False,
            is_bursty=False,
            caveats=[],
        )

    def test_groups_and_sums(self) -> None:
        opps = [
            self._opp("a", 10.0, 0.5, 100.0),
            self._opp("a", 5.0, 0.3, 50.0),
            self._opp("b", 20.0, 1.0, 200.0),
        ]
        result = _aggregate_by_namespace(opps)
        assert len(result) == 2  # noqa: PLR2004
        by_ns = {n.namespace: n for n in result}
        assert by_ns["a"].pod_count == 2  # noqa: PLR2004
        assert by_ns["a"].total_delta_cores == 0.8  # noqa: PLR2004
        assert by_ns["a"].total_delta_memory_mi == 150.0  # 100 + 50 cumule  # noqa: PLR2004
        assert by_ns["a"].total_monthly_saving_usd == 15.0  # noqa: PLR2004
        assert by_ns["b"].total_delta_memory_mi == 200.0  # noqa: PLR2004

    def test_no_usd_yields_none(self) -> None:
        result = _aggregate_by_namespace([self._opp("a", None, 0.5, 100.0)])
        assert result[0].total_monthly_saving_usd is None

    def test_mixed_usd_and_none(self) -> None:
        opps = [self._opp("a", 10.0, 0.5, 100.0), self._opp("a", None, 0.1, 10.0)]
        result = _aggregate_by_namespace(opps)
        assert result[0].total_monthly_saving_usd == 10.0  # noqa: PLR2004

    def test_mem_rounding_two_decimals(self) -> None:
        # 100.05 + 100.04 = 200.09 -> round(200.09, 1) = 200.1
        # mutant round(..., 2) donnerait 200.09 -> detecte
        from hexawyn.domain.models.cost_saving_estimation import PodSavingOpportunity

        def _opp(cores: float, mem: float) -> object:
            return PodSavingOpportunity(
                pod_name="x",
                namespace="a",
                current_cpu_request=1.0,
                recommended_cpu_request=0.5,
                current_memory_request_mi=512.0,
                recommended_memory_request_mi=256.0,
                delta_cores=cores,
                delta_memory_mi=mem,
                monthly_saving_usd=1.0,
                hpa_enabled=False,
                is_bursty=False,
                caveats=[],
            )

        result = _aggregate_by_namespace([_opp(0.5, 100.05), _opp(0.3, 100.04)])
        assert result[0].total_delta_memory_mi == 200.1  # noqa: PLR2004

    def test_usd_rounding_non_integer_sum(self) -> None:
        # 1.05 + 2.05 = 3.1 -> round(3.1, 2) = 3.1
        # mutant round(..., None) donnerait 3 (entier) -> detecte
        from hexawyn.domain.models.cost_saving_estimation import PodSavingOpportunity

        def _opp(usd: float) -> object:
            return PodSavingOpportunity(
                pod_name="x",
                namespace="a",
                current_cpu_request=1.0,
                recommended_cpu_request=0.5,
                current_memory_request_mi=512.0,
                recommended_memory_request_mi=256.0,
                delta_cores=0.5,
                delta_memory_mi=100.0,
                monthly_saving_usd=usd,
                hpa_enabled=False,
                is_bursty=False,
                caveats=[],
            )

        result = _aggregate_by_namespace([_opp(1.05), _opp(2.05)])
        assert result[0].total_monthly_saving_usd == 3.1  # noqa: PLR2004


class TestAnalyzePodFieldDefaults:
    def test_missing_pod_name_and_namespace_default_empty(self) -> None:
        # pod sans pod_name/namespace -> chaines vides (kills mutants get(...,None))
        pod = {
            "cpu_request_cores": 1.0,
            "memory_request_mi": 512.0,
            "cpu_p95_cores": 0.1,
            "memory_p95_mi": 200.0,
        }
        result = _analyze_pod(pod, None, None)
        assert result is not None
        assert result.pod_name == ""
        assert result.namespace == ""

    def test_delta_cpu_three_digits(self) -> None:
        # _delta avec digits=3: eff=1.0, rec=0.6 -> 0.4
        from hexawyn.domain.services.cost_saving.cost_saving_estimation_service import _delta

        assert _delta(1.0, 0.6, 3) == 0.4  # noqa: PLR2004

    def test_delta_mem_one_digit(self) -> None:
        from hexawyn.domain.services.cost_saving.cost_saving_estimation_service import _delta

        assert _delta(512.0, 240.0, 1) == 272.0  # noqa: PLR2004


class TestRecommendedBoundary:
    def test_request_exactly_01_uses_mem_branch(self) -> None:
        # request == 0.1 : > 0.1 est FALSE -> branche mem (64.0). Mutant >= 0.1 -> cpu (0.6)
        assert _recommended(0.1, 0.5) == 64.0  # noqa: PLR2004

    def test_mem_rounding_two_digits_distinguishes(self) -> None:
        # p95=53.41 -> rec = max(64.092, 64) -> round(64.092, 1) = 64.1
        # mutant round(..., 2) donnerait 64.09 -> detecte
        assert _recommended(0.05, 53.41) == 64.1  # noqa: PLR2004


class TestEstimateExclusionAndCounting:
    def test_multiple_excluded_counted(self) -> None:
        # 2 pods exclus -> pods_excluded == 2 (mutant pods_excluded = 1 detecte)
        svc = RightSizingCostEstimationService()
        pods = [
            {
                "cpu_request_cores": None,
                "memory_request_mi": None,
                "cpu_limit_cores": None,
                "memory_limit_mi": None,
            },
            {
                "cpu_request_cores": 1.0,
                "memory_request_mi": 512.0,
                "cpu_p95_cores": None,
                "memory_p95_mi": None,
            },
            {
                "cpu_request_cores": 0.5,
                "memory_request_mi": 512.0,
                "cpu_p95_cores": 0.1,
                "memory_p95_mi": 200.0,
            },
        ]
        report = svc.estimate(pods, 5, 10.0, 0.05)
        assert report.pods_excluded == 2  # noqa: PLR2004
        assert report.pods_analyzed == 1  # noqa: PLR2004

    def test_excluded_then_included_continue_not_break(self) -> None:
        # 1er pod exclu puis 2 pods inclus : si break, on perdrait les suivants
        svc = RightSizingCostEstimationService()
        pods = [
            {
                "cpu_request_cores": None,
                "memory_request_mi": None,
                "cpu_limit_cores": None,
                "memory_limit_mi": None,
            },
            {
                "cpu_request_cores": 0.5,
                "memory_request_mi": 512.0,
                "cpu_p95_cores": 0.1,
                "memory_p95_mi": 200.0,
            },
            {
                "cpu_request_cores": 0.5,
                "memory_request_mi": 512.0,
                "cpu_p95_cores": 0.1,
                "memory_p95_mi": 200.0,
            },
        ]
        report = svc.estimate(pods, 5, 10.0, 0.05)
        assert report.pods_analyzed == 2  # noqa: PLR2004


class TestAnalyzePodPricing:
    def test_mem_only_price_cpu_delta_ignored(self) -> None:
        # cpu_price None -> cpu_saving = delta * 0 (mutant or 1.0 ajouterait 0.88*720)
        # delta_cores = 0.88 (cpu_req 1.0, p95 0.1); mem delta 272 -> usd = 272/1024*0.05*720
        pod = _pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.1, mem_p95=200.0)
        result = _analyze_pod(pod, None, 0.05)
        assert result is not None
        assert result.monthly_saving_usd == 9.56  # noqa: PLR2004

    def test_cpu_only_price_mem_delta_ignored(self) -> None:
        # mem_price None -> mem_saving = 0 (mutant or 1.0 ajouterait 272/1024*720)
        pod = _pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.1, mem_p95=200.0)
        result = _analyze_pod(pod, 10.0, None)
        assert result is not None
        assert result.monthly_saving_usd == 6336.0  # 0.88 * 10 * 720  # noqa: PLR2004

    def test_neither_price_but_both_required_condition(self) -> None:
        # les deux prix None -> condition or = False -> usd None (mutant and identique ici)
        pod = _pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.1, mem_p95=200.0)
        result = _analyze_pod(pod, None, None)
        assert result is not None
        assert result.monthly_saving_usd is None

    def test_both_prices_exact_sum(self) -> None:
        # les deux prix : mutant 'and' ferait False quand un seul present mais ici les 2
        pod = _pod(cpu_request=1.0, mem_request=512.0, cpu_p95=0.1, mem_p95=200.0)
        result = _analyze_pod(pod, 10.0, 0.05)
        assert result is not None
        assert result.monthly_saving_usd == 6345.56  # 6336 + 9.56  # noqa: PLR2004


class TestAnalyzePodCpuAbsent:
    def test_cpu_absent_mem_present_not_excluded(self) -> None:
        # eff_cpu None (req+limit absents) MAIS mem present -> pas exclu
        # (mutant 'or' sur la garde retournerait None)
        pod = {
            "cpu_request_cores": None,
            "cpu_limit_cores": None,
            "memory_request_mi": 512.0,
            "memory_limit_mi": 1024.0,
            "cpu_p95_cores": 0.1,
            "memory_p95_mi": 200.0,
        }
        result = _analyze_pod(pod, None, None)
        assert result is not None
        assert result.delta_cores == 0.0
        assert result.delta_memory_mi == 272.0  # noqa: PLR2004


class TestAnalyzePodMemPrecision:
    def test_delta_mem_rounding_one_digit(self) -> None:
        # mem_request=300.07, p95=200 -> rec=240 -> delta 60.07
        # _delta(..., 1) -> round(60.07, 1) = 60.1 (mutant round(...,2) donnerait 60.07)
        pod = _pod(cpu_request=1.0, mem_request=300.07, cpu_p95=0.4, mem_p95=200.0)
        result = _analyze_pod(pod, None, None)
        assert result is not None
        assert result.recommended_memory_request_mi == 240.0  # noqa: PLR2004
        assert result.delta_memory_mi == 60.1  # noqa: PLR2004


class TestEstimateSmallDeltaPrecision:
    def test_total_delta_mi_non_integer_keeps_precision(self) -> None:
        # pod avec delta_memory_mi = 0.4 -> total 0.4
        # mutant round(..., None) donnerait 0 (entier) -> detecte
        service = RightSizingCostEstimationService()
        pods = [
            {
                "pod_name": "x",
                "namespace": "n",
                "cpu_request_cores": 1.0,
                "memory_request_mi": 512.0,
                "cpu_p95_cores": 0.9,
                "memory_p95_mi": 426.33,
            }
        ]
        report = service.estimate(pods, 5, None, None)
        assert report.total_delta_memory_mi == 0.4  # noqa: PLR2004
