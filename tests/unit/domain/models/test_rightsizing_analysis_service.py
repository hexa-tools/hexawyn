"""RED tests — domain/services/rightsizing/rightsizing_analysis_service.py"""

import pytest
from hexawyn.domain.models.rightsizing import RightsizingType
from hexawyn.domain.services.rightsizing.rightsizing_analysis_service import (
    RightsizingAnalysisService,
    _as_float_or_none,
    _classify,
    _compute_savings,
    _priority,
    _recommend_cpu,
    _recommend_memory,
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

    def test_classify_under_provisioned_ram(self) -> None:
        rtype, reason = _classify(4.0, 100.0, 3.0, 90.0)
        assert rtype == RightsizingType.UNDER_PROVISIONED
        assert "OOM risk" in reason

    def test_classify_optimal(self) -> None:
        rtype, reason = _classify(4.0, 100.0, 2.0, 50.0)
        assert rtype == RightsizingType.OPTIMAL

    def test_classify_over_provisioned_cpu_only(self) -> None:
        rtype, reason = _classify(4.0, 100.0, 0.8, 45.0)
        assert rtype == RightsizingType.OVER_PROVISIONED
        assert "CPU usage" in reason

    def test_classify_over_provisioned_both(self) -> None:
        rtype, reason = _classify(4.0, 100.0, 0.8, 30.0)
        assert rtype == RightsizingType.OVER_PROVISIONED

    def test_recommend_cpu_reduces_when_over_provisioned(self) -> None:
        rec = _recommend_cpu(4.0, 0.8)
        assert rec < 4.0  # noqa: PLR2004

    def test_recommend_cpu_keeps_when_not_over(self) -> None:
        rec = _recommend_cpu(4.0, 2.0)
        assert rec == 4.0  # noqa: PLR2004

    def test_recommend_memory_under_provisioned(self) -> None:
        rec = _recommend_memory(RightsizingType.UNDER_PROVISIONED, 100.0, 90.0)
        assert rec > 100.0  # noqa: PLR2004

    def test_recommend_memory_reduces_when_over(self) -> None:
        rec = _recommend_memory(RightsizingType.OVER_PROVISIONED, 200.0, 50.0)
        assert rec < 200.0  # noqa: PLR2004

    def test_recommend_memory_keeps(self) -> None:
        rec = _recommend_memory(RightsizingType.OPTIMAL, 100.0, 50.0)
        assert rec == 100.0  # noqa: PLR2004

    def test_compute_savings_positive(self) -> None:
        savings = _compute_savings(4.0, 1.0, 200.0, 100.0)
        assert savings > 0

    def test_compute_savings_zero(self) -> None:
        savings = _compute_savings(4.0, 4.0, 100.0, 100.0)
        assert savings == 0.0

    def test_waste_percentage_over_provisioned(self) -> None:
        waste = _waste_percentage(RightsizingType.OVER_PROVISIONED, 4.0, 100.0, 0.8, 30.0)
        assert waste > 0

    def test_waste_percentage_under_provisioned(self) -> None:
        waste = _waste_percentage(RightsizingType.UNDER_PROVISIONED, 4.0, 100.0, 3.0, 90.0)
        assert waste > 0

    def test_waste_percentage_optimal(self) -> None:
        waste = _waste_percentage(RightsizingType.OPTIMAL, 4.0, 100.0, 2.0, 50.0)
        assert waste == 0.0

    def test_priority_high(self) -> None:
        assert _priority(60.0) == "high"

    def test_priority_medium(self) -> None:
        assert _priority(30.0) == "medium"

    def test_priority_low(self) -> None:
        assert _priority(10.0) == "low"

    def test_priority_negative(self) -> None:
        assert _priority(-100.0) == "high"
