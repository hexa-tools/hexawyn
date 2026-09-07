"""RED tests — domain/services/rightsizing/rightsizing_analysis_service.py"""

import pytest
from hexawyn.domain.models.rightsizing import RightsizingType
from hexawyn.domain.services.rightsizing.rightsizing_analysis_service import (
    RightsizingAnalysisService,
    _analyze_workload,
    _as_float_or_none,
    _classify,
    _compute_savings,
    _over_waste,
    _priority,
    _recommend_cpu,
    _recommend_memory,
    _under_waste,
    _waste_percentage,
)


def _workload(  # noqa: PLR0913
    resource_name: str = "ml-worker",
    namespace: str = "production",
    kind: str = "Deployment",
    cpu_requested: float = 4.0,
    memory_requested_mi: float = 8192.0,
    cpu_actual: float | None = 0.8,
    memory_actual_mi: float | None = 2100.0,
) -> dict[str, object]:
    return {
        "resource_name": resource_name,
        "namespace": namespace,
        "kind": kind,
        "cpu_requested_cores": cpu_requested,
        "memory_requested_mi": memory_requested_mi,
        "cpu_actual_cores": cpu_actual,
        "memory_actual_mi": memory_actual_mi,
    }


class TestRightsizingAnalysisServiceOverProvisioned:
    def test_ml_worker_flagged_over_provisioned_cpu(self) -> None:
        # 0.8 / 4.0 = 20% < 30% threshold
        service = RightsizingAnalysisService()
        report = service.analyze([_workload(cpu_actual=0.8, cpu_requested=4.0)], top_n=5)
        assert len(report.recommendations) == 1
        rec = report.recommendations[0]
        assert rec.rightsizing_type == RightsizingType.OVER_PROVISIONED

    def test_over_provisioned_ram_detected(self) -> None:
        # 2.1 Gi / 8 Gi = 26% < 40% threshold
        service = RightsizingAnalysisService()
        report = service.analyze(
            [_workload(cpu_actual=3.5, memory_actual_mi=2100.0, memory_requested_mi=8192.0)],
            top_n=5,
        )
        assert len(report.recommendations) == 1
        rec = report.recommendations[0]
        assert rec.rightsizing_type == RightsizingType.OVER_PROVISIONED

    def test_waste_percentage_computed_on_worst_resource(self) -> None:
        # CPU: 20%, RAM: 26% waste → 80% CPU waste is max
        service = RightsizingAnalysisService()
        report = service.analyze(
            [
                _workload(
                    cpu_actual=0.8,
                    cpu_requested=4.0,
                    memory_actual_mi=2100.0,
                    memory_requested_mi=8192.0,
                )
            ],
            top_n=5,
        )
        rec = report.recommendations[0]
        assert rec.waste_percentage == pytest.approx(80.0, abs=0.1)

    def test_recommended_cpu_has_30pct_headroom(self) -> None:
        # actual 0.8 × 1.3 = 1.04
        service = RightsizingAnalysisService()
        report = service.analyze([_workload(cpu_actual=0.8, cpu_requested=4.0)], top_n=5)
        rec = report.recommendations[0]
        assert rec.recommended_cpu_cores == pytest.approx(1.04, abs=0.01)

    def test_recommended_memory_has_30pct_headroom(self) -> None:
        # actual 2100 × 1.3 = 2730
        service = RightsizingAnalysisService()
        report = service.analyze(
            [_workload(cpu_actual=3.5, memory_actual_mi=2100.0, memory_requested_mi=8192.0)],
            top_n=5,
        )
        rec = report.recommendations[0]
        assert rec.recommended_memory_mi == pytest.approx(2730.0, abs=1.0)

    def test_monthly_savings_positive_for_over_provisioned(self) -> None:
        service = RightsizingAnalysisService()
        report = service.analyze(
            [
                _workload(
                    cpu_actual=0.8,
                    cpu_requested=4.0,
                    memory_actual_mi=2100.0,
                    memory_requested_mi=8192.0,
                )
            ],
            top_n=5,
        )
        rec = report.recommendations[0]
        assert rec.monthly_savings_usd > 0

    def test_priority_high_when_savings_above_50(self) -> None:
        # Big workload: 8 CPU → 0.2 CPU actual → large savings
        service = RightsizingAnalysisService()
        report = service.analyze(
            [
                _workload(
                    cpu_actual=0.2,
                    cpu_requested=8.0,
                    memory_actual_mi=512.0,
                    memory_requested_mi=16384.0,
                )
            ],
            top_n=5,
        )
        rec = report.recommendations[0]
        assert rec.priority == "high"

    def test_priority_medium_when_savings_between_20_and_50(self) -> None:
        service = RightsizingAnalysisService()
        # craft savings ~$30: ~1.4 wasted cores × $21.6 = $30
        report = service.analyze(
            [
                _workload(
                    cpu_actual=0.1,
                    cpu_requested=1.6,
                    memory_actual_mi=400.0,
                    memory_requested_mi=500.0,
                )
            ],
            top_n=5,
        )
        rec = report.recommendations[0]
        assert rec.priority in ("medium", "high")

    def test_priority_low_when_savings_below_20(self) -> None:
        # CPU: 0.1/0.6 = 16.7% < 30% → over-provisioned CPU
        # RAM: 100/220 = 45.5% — not over (>40%), not under (<85%)
        service = RightsizingAnalysisService()
        report = service.analyze(
            [
                _workload(
                    cpu_actual=0.1,
                    cpu_requested=0.6,
                    memory_actual_mi=100.0,
                    memory_requested_mi=220.0,
                )
            ],
            top_n=5,
        )
        rec = report.recommendations[0]
        assert rec.priority == "low"


class TestRightsizingAnalysisServiceUnderProvisioned:
    def test_payments_api_flagged_under_provisioned_ram(self) -> None:
        # 380 / 256 = 148% > 85% threshold
        service = RightsizingAnalysisService()
        report = service.analyze(
            [
                _workload(
                    resource_name="payments-api",
                    cpu_actual=0.8,
                    cpu_requested=2.0,
                    memory_actual_mi=380.0,
                    memory_requested_mi=256.0,
                )
            ],
            top_n=5,
        )
        assert len(report.recommendations) == 1
        rec = report.recommendations[0]
        assert rec.rightsizing_type == RightsizingType.UNDER_PROVISIONED

    def test_recommended_memory_doubled_for_under_provisioned(self) -> None:
        service = RightsizingAnalysisService()
        report = service.analyze(
            [_workload(memory_actual_mi=380.0, memory_requested_mi=256.0)],
            top_n=5,
        )
        rec = report.recommendations[0]
        assert rec.recommended_memory_mi == pytest.approx(512.0, abs=1.0)

    def test_monthly_savings_negative_for_under_provisioned(self) -> None:
        # CPU fine (90% utilization), only RAM is under-provisioned → cost goes up
        service = RightsizingAnalysisService()
        report = service.analyze(
            [
                _workload(
                    cpu_actual=1.8,
                    cpu_requested=2.0,
                    memory_actual_mi=380.0,
                    memory_requested_mi=256.0,
                )
            ],
            top_n=5,
        )
        rec = report.recommendations[0]
        assert rec.monthly_savings_usd < 0


class TestRightsizingAnalysisServiceFiltering:
    def test_healthy_workload_excluded(self) -> None:
        # 80% usage → fine (70% CPU, 75% RAM — neither threshold triggered)
        service = RightsizingAnalysisService()
        report = service.analyze(
            [
                _workload(
                    cpu_actual=3.2,
                    cpu_requested=4.0,
                    memory_actual_mi=6144.0,
                    memory_requested_mi=8192.0,
                )
            ],
            top_n=5,
        )
        assert report.recommendations == []

    def test_savings_below_minimum_filtered_out(self) -> None:
        # tiny workload — savings < $5
        service = RightsizingAnalysisService()
        report = service.analyze(
            [
                _workload(
                    cpu_actual=0.01,
                    cpu_requested=0.1,
                    memory_actual_mi=10.0,
                    memory_requested_mi=30.0,
                )
            ],
            top_n=5,
        )
        assert report.recommendations == []

    def test_workload_without_metrics_counted_as_skipped(self) -> None:
        service = RightsizingAnalysisService()
        report = service.analyze(
            [_workload(cpu_actual=None, memory_actual_mi=None)],
            top_n=5,
        )
        assert report.skipped_count == 1
        assert report.recommendations == []

    def test_top_n_limits_output(self) -> None:
        workloads = [
            _workload(resource_name=f"svc-{i}", cpu_actual=0.1, cpu_requested=4.0)
            for i in range(10)
        ]
        service = RightsizingAnalysisService()
        report = service.analyze(workloads, top_n=3)
        assert len(report.recommendations) <= 3  # noqa: PLR2004


class TestRightsizingAnalysisServiceRanking:
    def test_ranked_by_savings_descending(self) -> None:
        big = _workload(
            resource_name="big",
            cpu_actual=0.1,
            cpu_requested=8.0,
            memory_actual_mi=100.0,
            memory_requested_mi=16384.0,
        )
        small = _workload(
            resource_name="small",
            cpu_actual=0.1,
            cpu_requested=1.0,
            memory_actual_mi=50.0,
            memory_requested_mi=200.0,
        )
        service = RightsizingAnalysisService()
        report = service.analyze([small, big], top_n=5)
        names = [r.resource_name for r in report.recommendations]
        assert names[0] == "big"

    def test_total_savings_is_sum_of_positive_recommendations(self) -> None:
        workloads = [
            _workload(resource_name="a", cpu_actual=0.1, cpu_requested=4.0),
            _workload(resource_name="b", cpu_actual=0.1, cpu_requested=4.0),
        ]
        service = RightsizingAnalysisService()
        report = service.analyze(workloads, top_n=5)
        expected = sum(
            r.monthly_savings_usd for r in report.recommendations if r.monthly_savings_usd > 0
        )
        assert report.total_monthly_savings_usd == pytest.approx(expected, abs=0.01)


class TestHelperFunctions:
    def test_as_float_or_none_returns_float(self) -> None:
        assert _as_float_or_none(3.14) == 3.14  # noqa: PLR2004

    def test_as_float_or_none_none_returns_none(self) -> None:
        assert _as_float_or_none(None) is None

    def test_as_float_or_none_invalid_returns_none(self) -> None:
        assert _as_float_or_none("abc") is None
        assert _as_float_or_none([1, 2]) is None

    def test_as_float_or_none_numeric_string(self) -> None:
        assert _as_float_or_none("0.5") == 0.5  # noqa: PLR2004

    def test_classify_under_provisioned_ram(self) -> None:
        rtype, reason = _classify(4.0, 100.0, 3.0, 90.0)
        assert rtype == RightsizingType.UNDER_PROVISIONED
        assert "OOM risk" in reason

    def test_classify_under_ram_exact_reason(self) -> None:
        rtype, reason = _classify(1.0, 100.0, 0.1, 90.0)
        assert rtype == RightsizingType.UNDER_PROVISIONED
        assert reason == "RAM usage 90.0% of requests — OOM risk"

    def test_classify_optimal(self) -> None:
        rtype, reason = _classify(4.0, 100.0, 2.0, 50.0)
        assert rtype == RightsizingType.OPTIMAL
        assert reason == ""

    def test_classify_over_provisioned_cpu_only(self) -> None:
        rtype, reason = _classify(4.0, 100.0, 0.8, 45.0)
        assert rtype == RightsizingType.OVER_PROVISIONED
        assert reason == "CPU usage 20.0% of requests"

    def test_classify_over_provisioned_both(self) -> None:
        rtype, reason = _classify(4.0, 100.0, 0.8, 30.0)
        assert rtype == RightsizingType.OVER_PROVISIONED

    def test_classify_over_both_exact_reason(self) -> None:
        rtype, reason = _classify(2.0, 2048.0, 0.1, 100.0)
        assert rtype == RightsizingType.OVER_PROVISIONED
        assert reason == "CPU usage 5.0% of requests · RAM usage 4.9% of requests"
        assert reason.index("CPU") < reason.index("RAM")

    def test_classify_zero_cpu_req_does_not_under(self) -> None:
        # mem ok, cpu_req=0 -> pas sous-dimensionne car mem_actual/mem_req ok
        rtype, _ = _classify(0.0, 1024.0, 0.1, 500.0)
        assert rtype == RightsizingType.OPTIMAL

    def test_recommend_cpu_reduces_when_over_provisioned(self) -> None:
        rec = _recommend_cpu(4.0, 0.8)
        assert rec == 0.8 * 1.3  # noqa: PLR2004

    def test_recommend_cpu_keeps_when_not_over(self) -> None:
        rec = _recommend_cpu(4.0, 2.0)
        assert rec == 4.0  # noqa: PLR2004

    def test_recommend_cpu_unknown_actual_keeps_request(self) -> None:
        assert _recommend_cpu(2.0, None) == 2.0  # noqa: PLR2004

    def test_recommend_cpu_zero_request_keeps_zero(self) -> None:
        assert _recommend_cpu(0.0, 0.1) == 0.0

    def test_recommend_memory_under_provisioned(self) -> None:
        rec = _recommend_memory(RightsizingType.UNDER_PROVISIONED, 1024.0, 900.0)
        assert rec == 2048.0  # noqa: PLR2004

    def test_recommend_memory_reduces_when_over(self) -> None:
        rec = _recommend_memory(RightsizingType.OVER_PROVISIONED, 2048.0, 100.0)
        assert rec == 130.0  # noqa: PLR2004

    def test_recommend_memory_keeps(self) -> None:
        rec = _recommend_memory(RightsizingType.OVER_PROVISIONED, 1024.0, 500.0)
        assert rec == 1024.0  # noqa: PLR2004

    def test_recommend_memory_unknown_actual_keeps_request(self) -> None:
        assert _recommend_memory(RightsizingType.OVER_PROVISIONED, 1024.0, None) == 1024.0  # noqa: PLR2004

    def test_compute_savings_positive(self) -> None:
        savings = _compute_savings(2.0, 0.2, 2048.0, 130.0)
        assert savings == 44.27  # noqa: PLR2004

    def test_compute_savings_zero(self) -> None:
        savings = _compute_savings(4.0, 4.0, 100.0, 100.0)
        assert savings == 0.0

    def test_waste_percentage_over_provisioned(self) -> None:
        waste = _waste_percentage(RightsizingType.OVER_PROVISIONED, 2.0, 2048.0, 0.1, 100.0)
        assert waste == 95.1  # noqa: PLR2004

    def test_waste_percentage_under_provisioned(self) -> None:
        waste = _waste_percentage(RightsizingType.UNDER_PROVISIONED, 1.0, 100.0, 0.1, 90.0)
        assert waste == 90.0  # noqa: PLR2004

    def test_waste_percentage_optimal(self) -> None:
        waste = _waste_percentage(RightsizingType.OPTIMAL, 4.0, 100.0, 2.0, 50.0)
        assert waste == 0.0

    def test_waste_percentage_no_cpu_actual_over(self) -> None:
        # cpu_req=0 -> cpu_waste=0 ; mem_waste=(1-100/2048)*100=95.1
        waste = _waste_percentage(RightsizingType.OVER_PROVISIONED, 0.0, 2048.0, None, 100.0)
        assert waste == 95.1  # noqa: PLR2004

    def test_priority_high(self) -> None:
        assert _priority(60.0) == "high"

    def test_priority_medium(self) -> None:
        assert _priority(30.0) == "medium"

    def test_priority_low(self) -> None:
        assert _priority(10.0) == "low"

    def test_priority_negative(self) -> None:
        assert _priority(-100.0) == "high"

    def test_priority_boundary_50_medium(self) -> None:
        assert _priority(50.0) == "medium"

    def test_priority_boundary_20_low(self) -> None:
        assert _priority(20.0) == "low"


class TestAnalyzeWorkload:
    def _wl(self, **overrides: object) -> dict[str, object]:
        defaults: dict[str, object] = {
            "resource_name": "deploy-1",
            "namespace": "default",
            "kind": "Deployment",
            "cpu_requested_cores": 1.0,
            "memory_requested_mi": 1024.0,
            "cpu_actual_cores": 0.1,
            "memory_actual_mi": 100.0,
        }
        return {**defaults, **overrides}

    def test_fields_preserved(self) -> None:
        rec = _analyze_workload(
            self._wl(
                resource_name="web", namespace="prod", kind="StatefulSet", memory_actual_mi=None
            )
        )
        assert rec is not None
        assert rec.resource_name == "web"
        assert rec.namespace == "prod"
        assert rec.kind == "StatefulSet"
        assert rec.current_cpu_cores == 1.0
        assert rec.current_memory_mi == 1024.0  # noqa: PLR2004
        assert rec.reason == "CPU usage 10.0% of requests"

    def test_cpu_only_actual(self) -> None:
        # cpu_actual present, mem_actual absent -> pas exclu
        rec = _analyze_workload(self._wl(memory_actual_mi=None))
        assert rec is not None
        assert rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
        assert rec.reason == "CPU usage 10.0% of requests"

    def test_mem_only_actual(self) -> None:
        # cpu_actual absent, mem_actual present -> pas exclu
        rec = _analyze_workload(self._wl(cpu_actual_cores=None))
        assert rec is not None
        assert rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
        assert rec.reason == "RAM usage 9.8% of requests"

    def test_both_absent_excluded(self) -> None:
        rec = _analyze_workload(self._wl(cpu_actual_cores=None, memory_actual_mi=None))
        assert rec is None

    def test_under_provisioned_recommendation(self) -> None:
        rec = _analyze_workload(self._wl(memory_requested_mi=100.0, memory_actual_mi=90.0))
        assert rec is not None
        assert rec.rightsizing_type == RightsizingType.UNDER_PROVISIONED
        assert rec.recommended_memory_mi == 200.0  # noqa: PLR2004


class TestExactBoundaries:
    def test_classify_mem_req_one_is_under(self) -> None:
        # mem_req=1 (>0 mais pas >1): ratio 0.9/1 > 0.85 -> UNDER. Mutant '> 1' casserait
        rtype, _ = _classify(1.0, 1.0, 0.5, 0.9)
        assert rtype == RightsizingType.UNDER_PROVISIONED

    def test_recommend_memory_mem_req_one(self) -> None:
        # mem_req=1, actual=0.3 -> ratio 0.3 < 0.40 -> OVER -> max(0.3*1.3, 128)
        result = _recommend_memory(RightsizingType.OVER_PROVISIONED, 1.0, 0.3)
        assert result == 128.0  # noqa: PLR2004

    def test_workload_missing_kind_defaults_deployment(self) -> None:
        # workload sans cles 'resource_name'/'kind' -> defauts (kills get(...,None)/XX)
        wl = {
            "cpu_requested_cores": 1.0,
            "memory_requested_mi": 1024.0,
            "cpu_actual_cores": 0.1,
            "memory_actual_mi": 100.0,
        }
        rec = _analyze_workload(wl)
        assert rec is not None
        assert rec.resource_name == ""
        assert rec.namespace == ""
        assert rec.kind == "Deployment"

    def test_analyze_skipped_count_multiple(self) -> None:
        # 2 workloads skipped -> skipped_count==2 (mutant skipped = 1 detecte)
        svc = RightsizingAnalysisService()
        wls = [
            {"cpu_actual_cores": None, "memory_actual_mi": None},
            {"cpu_actual_cores": None, "memory_actual_mi": None},
            {
                "cpu_actual_cores": 0.1,
                "memory_actual_mi": 100.0,
                "cpu_requested_cores": 1.0,
                "memory_requested_mi": 1024.0,
            },
        ]
        report = svc.analyze(wls, 5)
        assert report.skipped_count == 2  # noqa: PLR2004
        assert len(report.recommendations) == 1  # noqa: PLR2004

    def test_analyze_continue_after_skip(self) -> None:
        # 1er skipped puis 2 retenus : si break, on perdrait les suivants
        svc = RightsizingAnalysisService()
        wls = [
            {"cpu_actual_cores": None, "memory_actual_mi": None},
            {
                "cpu_actual_cores": 0.1,
                "memory_actual_mi": 100.0,
                "cpu_requested_cores": 1.0,
                "memory_requested_mi": 1024.0,
            },
            {
                "cpu_actual_cores": 0.1,
                "memory_actual_mi": 100.0,
                "cpu_requested_cores": 1.0,
                "memory_requested_mi": 1024.0,
            },
        ]
        report = svc.analyze(wls, 5)
        assert len(report.recommendations) == 2  # noqa: PLR2004


class TestWasteHelpers:
    def test_over_waste_normal(self) -> None:
        assert _over_waste(0.5, 1.0) == 50.0  # noqa: PLR2004

    def test_over_waste_none_actual_zero(self) -> None:
        assert _over_waste(None, 1.0) == 0.0

    def test_over_waste_zero_request_zero(self) -> None:
        assert _over_waste(0.5, 0.0) == 0.0

    def test_under_waste_normal(self) -> None:
        assert _under_waste(0.9, 1.0) == 90.0  # noqa: PLR2004

    def test_under_waste_none_actual_zero(self) -> None:
        assert _under_waste(None, 1.0) == 0.0

    def test_under_waste_zero_request_zero(self) -> None:
        assert _under_waste(0.9, 0.0) == 0.0


class TestWasteHelperArithmetic:
    def test_over_waste_division_not_multiplication(self) -> None:
        # actual=0.5 request=2.0 : division -> (1-0.25)*100=75
        # mutant multiplication -> (1-1.0)*100=0
        assert _over_waste(0.5, 2.0) == 75.0  # noqa: PLR2004

    def test_under_waste_division_not_multiplication(self) -> None:
        # actual=0.9 request=2.0 : division -> 45
        # mutant multiplication -> 180
        assert _under_waste(0.9, 2.0) == 45.0  # noqa: PLR2004


class TestClassifyFrontiers:
    def test_zero_mem_request_no_division(self) -> None:
        # mem_req=0 : la garde mem_req>0 protege de la division par zero
        # mutant >= 0 provoquerait mem_actual/0 -> crash
        rtype, _ = _classify(1.0, 0.0, 0.5, 0.9)
        assert rtype == RightsizingType.OPTIMAL

    def test_mem_ratio_exactly_threshold_not_under(self) -> None:
        # mem_actual/mem_req == 0.85 : > 0.85 est FALSE -> pas UNDER
        # mutant >= 0.85 donnerait UNDER
        rtype, _ = _classify(1.0, 1.0, 0.5, 0.85)
        assert rtype == RightsizingType.OPTIMAL

    def test_cpu_ratio_exactly_threshold_not_over(self) -> None:
        # cpu_actual/cpu_req == 0.30 : < 0.30 est FALSE -> pas over_cpu
        # mutant <= 0.30 donnerait OVER_PROVISIONED
        rtype, _ = _classify(1.0, 1.0, 0.30, 0.5)
        assert rtype == RightsizingType.OPTIMAL


class TestRightsizingFrontiers:
    def test_classify_mem_req_one_over_provisioned(self) -> None:
        # mem_req=1, ratio mem 0.3 < 0.40 -> OVER (mutant > 1 ne detecterait pas)
        rtype, reason = _classify(1.0, 1.0, 0.5, 0.3)
        assert rtype == RightsizingType.OVER_PROVISIONED
        assert "RAM usage" in reason

    def test_classify_over_mem_only_reason_has_no_cpu(self) -> None:
        # cpu ratio 0.5 (pas over), mem ratio 0.29 (over) -> reason RAM seulement
        # mutant 'or' ajouterait une partie CPU errone
        rtype, reason = _classify(1.0, 1024.0, 0.5, 300.0)
        assert rtype == RightsizingType.OVER_PROVISIONED
        assert "CPU" not in reason
        assert "RAM usage" in reason

    def test_recommend_memory_zero_req_no_division(self) -> None:
        # mem_req=0 : garde mem_req>0 protege (mutant >=0 ferait mem_actual/0)
        result = _recommend_memory(RightsizingType.OVER_PROVISIONED, 0.0, 0.3)
        assert result == 0.0


class TestRoundingAndGib:
    def test_under_waste_fractional_rounding(self) -> None:
        # waste sous = 33.3 -> round(33.3, 1) = 33.3 (mutant round None -> 33)
        result = _waste_percentage(RightsizingType.UNDER_PROVISIONED, 1.0, 1.0, 0.1, 0.333)
        assert result == 33.3  # noqa: PLR2004

    def test_savings_uses_1024_gib(self) -> None:
        # 2048 MiB = 2.0 GiB (division /1024). mutant /1025 donnerait 5.75
        savings = _compute_savings(0.0, 0.0, 2048.0, 0.0)
        assert savings == 5.76  # noqa: PLR2004


class TestAnalyzeSavingsFilterBreak:
    def test_low_savings_filtered_then_kept(self) -> None:
        # workload avec savings < 5 filtre (continue) puis 2 retenus savings > 5
        # mutant break sortirait apres le workload filtre -> 0 recommandations
        svc = RightsizingAnalysisService()
        low = {
            "cpu_actual_cores": 0.3,
            "memory_actual_mi": 100.0,
            "cpu_requested_cores": 1.0,
            "memory_requested_mi": 1024.0,
        }
        high = {
            "cpu_actual_cores": 0.1,
            "memory_actual_mi": 100.0,
            "cpu_requested_cores": 1.0,
            "memory_requested_mi": 1024.0,
        }
        report = svc.analyze([low, high, high], 5)
        assert len(report.recommendations) == 2  # noqa: PLR2004


class TestClassifyReasonPrecision:
    def test_cpu_reason_rounding_one_digit(self) -> None:
        # cpu_ratio 0.1235 -> 12.35% : round(12.35,1) = 12.3
        # mutant round(...,2) donnerait 12.35% -> reason different
        rtype, reason = _classify(2.0, 1024.0, 0.247, 300.0)
        assert rtype == RightsizingType.OVER_PROVISIONED
        assert reason == "CPU usage 12.3% of requests · RAM usage 29.3% of requests"
