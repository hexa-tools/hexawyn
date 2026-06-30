"""Unit tests for NamespaceOverProvisioningService (domain — pure computation)."""

import pytest
from hexawyn.application.ports.driven.namespace_waste_port import NamespaceRawData
from hexawyn.domain.models.namespace_waste import ExcludedNamespace, NamespaceWaste
from hexawyn.domain.services.namespace_waste.namespace_over_provisioning_service import (
    NamespaceOverProvisioningService,
)


def _raw(
    namespace: str,
    cpu_req: float | None = 4.0,
    mem_req: float | None = 8.0,
    cpu_actual: float | None = 2.0,
    mem_actual: float | None = 4.0,
    age_hours: float = 48.0,
    has_requests: bool = True,
) -> NamespaceRawData:
    return {
        "namespace": namespace,
        "cpu_requested_cores": cpu_req,
        "memory_requested_gb": mem_req,
        "cpu_actual_avg_cores": cpu_actual,
        "memory_actual_avg_gb": mem_actual,
        "age_hours": age_hours,
        "has_resource_requests": has_requests,
    }


_SERVICE = NamespaceOverProvisioningService()


class TestWasteRatioComputation:
    """waste = (requested - actual) / requested * 100."""

    def test_dev_namespace_94_pct_cpu_waste(self) -> None:
        raw = [_raw("dev", cpu_req=8.0, cpu_actual=0.45, mem_req=16.0, mem_actual=1.2)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        ns = report.namespaces[0]
        assert ns.namespace == "dev"
        assert round(ns.cpu_waste_pct, 1) == pytest.approx(94.4, abs=0.2)

    def test_dev_namespace_cpu_wasted_cores(self) -> None:
        raw = [_raw("dev", cpu_req=8.0, cpu_actual=0.45, mem_req=16.0, mem_actual=1.2)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        ns = report.namespaces[0]
        assert round(ns.cpu_wasted_cores, 2) == pytest.approx(7.55, abs=0.01)

    def test_dev_namespace_memory_waste_pct(self) -> None:
        raw = [_raw("dev", cpu_req=8.0, cpu_actual=0.45, mem_req=16.0, mem_actual=1.2)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        ns = report.namespaces[0]
        assert round(ns.memory_waste_pct, 1) == pytest.approx(92.5, abs=0.2)

    def test_production_namespace_12_pct_waste(self) -> None:
        raw = [_raw("production", cpu_req=4.0, cpu_actual=3.5, mem_req=8.0, mem_actual=7.5)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        ns = report.namespaces[0]
        assert round(ns.cpu_waste_pct, 1) == pytest.approx(12.5, abs=0.1)

    def test_cpu_and_memory_waste_computed_independently(self) -> None:
        raw = [_raw("mixed", cpu_req=10.0, cpu_actual=1.0, mem_req=4.0, mem_actual=3.8)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        ns = report.namespaces[0]
        assert round(ns.cpu_waste_pct, 0) == pytest.approx(90.0, abs=1.0)
        assert round(ns.memory_waste_pct, 0) == pytest.approx(5.0, abs=1.0)

    def test_wasted_memory_gb_correct(self) -> None:
        raw = [_raw("staging", cpu_req=4.0, cpu_actual=2.0, mem_req=16.0, mem_actual=1.2)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        ns = report.namespaces[0]
        assert round(ns.memory_wasted_gb, 2) == pytest.approx(14.8, abs=0.01)


class TestOverProvisionedFlagging:
    """Namespaces with max(cpu_waste, mem_waste) > 50% are flagged."""

    def test_dev_94pct_waste_is_flagged(self) -> None:
        raw = [_raw("dev", cpu_req=8.0, cpu_actual=0.45)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert report.namespaces[0].is_over_provisioned is True

    def test_production_12pct_is_not_flagged(self) -> None:
        raw = [_raw("production", cpu_req=4.0, cpu_actual=3.5)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert report.namespaces[0].is_over_provisioned is False

    def test_exactly_50pct_waste_is_not_flagged(self) -> None:
        raw = [_raw("boundary", cpu_req=4.0, cpu_actual=2.0)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert report.namespaces[0].is_over_provisioned is False

    def test_above_50pct_waste_is_flagged(self) -> None:
        raw = [_raw("over", cpu_req=4.0, cpu_actual=1.9)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert report.namespaces[0].is_over_provisioned is True


class TestRanking:
    """Top-N sorted by max(cpu_waste_pct, memory_waste_pct) descending."""

    def test_ranking_dev_before_staging_before_prod(self) -> None:
        raw = [
            _raw("production", cpu_req=4.0, cpu_actual=3.5),
            _raw("dev", cpu_req=8.0, cpu_actual=0.45),
            _raw("staging", cpu_req=4.0, cpu_actual=1.2),
        ]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        names = [ns.namespace for ns in report.namespaces]
        assert names.index("dev") < names.index("staging")
        assert names.index("staging") < names.index("production")

    def test_top_n_limits_result(self) -> None:
        raw = [_raw(f"ns-{i}", cpu_req=float(i + 1), cpu_actual=0.1) for i in range(10)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert len(report.namespaces) == 5

    def test_top_5_most_wasteful_returned(self) -> None:
        raw = [_raw(f"ns-{i}", cpu_req=float(i + 1), cpu_actual=0.1) for i in range(10)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        waste_pcts = [ns.cpu_waste_pct for ns in report.namespaces]
        assert waste_pcts == sorted(waste_pcts, reverse=True)


class TestExclusions:
    """Namespaces excluded from waste analysis."""

    def test_no_resource_requests_excluded(self) -> None:
        raw = [_raw("burstable", has_requests=False, cpu_req=None, mem_req=None)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert report.namespaces == []
        assert len(report.excluded) == 1
        assert report.excluded[0].namespace == "burstable"
        assert "requests" in report.excluded[0].reason.lower()

    def test_recently_created_namespace_excluded(self) -> None:
        raw = [_raw("new-ns", age_hours=12.0)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert report.namespaces == []
        excluded_names = [e.namespace for e in report.excluded]
        assert "new-ns" in excluded_names

    def test_excluded_reason_mentions_insufficient_data(self) -> None:
        raw = [_raw("new-ns", age_hours=12.0)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        reason = report.excluded[0].reason.lower()
        assert "24h" in reason or "insufficient" in reason or "recent" in reason

    def test_namespace_with_zero_requests_excluded(self) -> None:
        raw = [_raw("zero-req", cpu_req=0.0, mem_req=0.0, has_requests=False)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert report.namespaces == []

    def test_eligible_and_excluded_together(self) -> None:
        raw = [
            _raw("dev", cpu_req=8.0, cpu_actual=0.5),
            _raw("new-ns", age_hours=6.0),
            _raw("burstable", has_requests=False, cpu_req=None, mem_req=None),
        ]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert len(report.namespaces) == 1
        assert report.namespaces[0].namespace == "dev"
        assert len(report.excluded) == 2


class TestAggregates:
    """Total wasted cores and GB summed across returned namespaces."""

    def test_total_wasted_cpu_cores_summed(self) -> None:
        raw = [
            _raw("dev", cpu_req=8.0, cpu_actual=0.45),
            _raw("staging", cpu_req=4.0, cpu_actual=1.2),
        ]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        expected = (8.0 - 0.45) + (4.0 - 1.2)
        assert round(report.total_wasted_cpu_cores, 2) == pytest.approx(expected, abs=0.01)

    def test_total_wasted_memory_gb_summed(self) -> None:
        raw = [
            _raw("dev", mem_req=16.0, mem_actual=1.2),
            _raw("staging", mem_req=8.0, mem_actual=3.0),
        ]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        expected = (16.0 - 1.2) + (8.0 - 3.0)
        assert round(report.total_wasted_memory_gb, 2) == pytest.approx(expected, abs=0.01)

    def test_analysis_window_days_preserved(self) -> None:
        raw = [_raw("dev")]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert report.analysis_window_days == 7

    def test_empty_input_returns_empty_report(self) -> None:
        report = _SERVICE.analyze([], top_n=5, analysis_window_days=7)

        assert report.namespaces == []
        assert report.total_wasted_cpu_cores == 0.0
        assert report.total_wasted_memory_gb == 0.0


class TestPrometheusUnavailable:
    """When Prometheus data is missing, waste computed from K8s only."""

    def test_namespace_included_when_no_prometheus_data(self) -> None:
        raw = [_raw("dev", cpu_req=8.0, cpu_actual=None, mem_req=16.0, mem_actual=None)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert len(report.namespaces) == 1
        assert report.namespaces[0].cpu_actual_avg_cores == 0.0

    def test_waste_pct_zero_when_no_actual_data(self) -> None:
        raw = [_raw("dev", cpu_req=8.0, cpu_actual=None, mem_req=16.0, mem_actual=None)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert report.namespaces[0].cpu_waste_pct == 0.0
        assert report.namespaces[0].memory_waste_pct == 0.0

    def test_namespace_not_flagged_when_no_prometheus(self) -> None:
        raw = [_raw("dev", cpu_req=8.0, cpu_actual=None)]
        report = _SERVICE.analyze(raw, top_n=5, analysis_window_days=7)

        assert report.namespaces[0].is_over_provisioned is False


class TestNamespaceWasteModel:
    def test_max_waste_pct_returns_larger_of_cpu_memory(self) -> None:
        waste = NamespaceWaste(
            namespace="dev",
            cpu_requested_cores=8.0,
            cpu_actual_avg_cores=0.45,
            cpu_waste_pct=94.4,
            cpu_wasted_cores=7.55,
            memory_requested_gb=16.0,
            memory_actual_avg_gb=1.2,
            memory_waste_pct=92.5,
            memory_wasted_gb=14.8,
            is_over_provisioned=True,
        )
        assert waste.max_waste_pct == 94.4

    def test_excluded_namespace_has_namespace_and_reason(self) -> None:
        exc = ExcludedNamespace(namespace="burstable", reason="No resource requests set")
        assert exc.namespace == "burstable"
        assert exc.reason == "No resource requests set"
