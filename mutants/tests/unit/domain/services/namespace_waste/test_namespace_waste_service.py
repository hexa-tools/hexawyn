from __future__ import annotations

from hexawyn.domain.models.namespace_waste import (
    ExcludedNamespace,
    NamespaceRawData,
    NamespaceWaste,
    OverProvisioningReport,
)
from hexawyn.domain.services.namespace_waste.namespace_over_provisioning_service import (
    NamespaceOverProvisioningService,
    _compute_namespace_waste,
    _exclusion_reason,
    _waste_pair,
    any_actual_usage_present,
)


def _raw(  # noqa: PLR0913
    namespace: str = "default",
    cpu_requested: float | None = 10.0,
    mem_requested: float | None = 40.0,
    cpu_actual: float | None = 2.0,
    mem_actual: float | None = 10.0,
    age_hours: float = 48.0,
    has_resource_requests: bool = True,
) -> NamespaceRawData:
    return NamespaceRawData(
        namespace=namespace,
        cpu_requested_cores=cpu_requested,
        memory_requested_gb=mem_requested,
        cpu_actual_avg_cores=cpu_actual,
        memory_actual_avg_gb=mem_actual,
        age_hours=age_hours,
        has_resource_requests=has_resource_requests,
    )


class TestExclusionReason:
    def test_no_resource_requests_excluded(self) -> None:
        reason = _exclusion_reason(_raw(has_resource_requests=False))
        assert reason is not None
        assert "No resource requests" in reason

    def test_too_recent_excluded(self) -> None:
        reason = _exclusion_reason(_raw(age_hours=10.0))
        assert reason is not None
        assert "insufficient data" in reason

    def test_eligible_no_reason(self) -> None:
        reason = _exclusion_reason(_raw(has_resource_requests=True, age_hours=48.0))
        assert reason is None


class TestWastePair:
    def test_normal_waste(self) -> None:
        pct, wasted = _waste_pair(10.0, 2.0)
        assert pct == 80.0  # noqa: PLR2004
        assert wasted == 8.0  # noqa: PLR2004

    def test_actual_none_returns_zero(self) -> None:
        pct, wasted = _waste_pair(10.0, None)
        assert pct == 0.0
        assert wasted == 0.0

    def test_requested_zero_returns_zero(self) -> None:
        pct, wasted = _waste_pair(0.0, 5.0)
        assert pct == 0.0
        assert wasted == 0.0


class TestAnyActualUsage:
    def test_with_usage_returns_true(self) -> None:
        data = [_raw(cpu_actual=1.0)]
        assert any_actual_usage_present(data) is True

    def test_all_none_returns_false(self) -> None:
        data = [_raw(cpu_actual=None, mem_actual=None)]
        assert any_actual_usage_present(data) is False


class TestNamespaceOverProvisioningService:
    def test_analyze_basic(self) -> None:
        service = NamespaceOverProvisioningService()
        data = [
            _raw(namespace="ns-1", cpu_requested=10.0, cpu_actual=2.0),
            _raw(namespace="ns-2", cpu_requested=5.0, cpu_actual=4.0),
        ]
        report = service.analyze(data, top_n=5, analysis_window_days=7)
        assert len(report.namespaces) == 2  # noqa: PLR2004
        assert report.namespaces[0].namespace == "ns-1"

    def test_analyze_excludes_ineligible(self) -> None:
        service = NamespaceOverProvisioningService()
        data = [
            _raw(namespace="ns-1", has_resource_requests=False),
            _raw(namespace="ns-2", age_hours=10.0),
        ]
        report = service.analyze(data, top_n=5, analysis_window_days=7)
        assert len(report.namespaces) == 0
        assert len(report.excluded) == 2  # noqa: PLR2004


class TestExactReportPayload:
    def test_full_report_matches_expected(self) -> None:
        service = NamespaceOverProvisioningService()
        data = [
            _raw(namespace="ns-1", cpu_requested=10.0, cpu_actual=2.0),
            _raw(namespace="ns-2", cpu_requested=5.0, cpu_actual=4.0),
            _raw(namespace="ns-3", has_resource_requests=False),
            _raw(namespace="ns-4", age_hours=10.0),
        ]

        report = service.analyze(data, top_n=5, analysis_window_days=7)

        assert report == OverProvisioningReport(
            namespaces=[
                NamespaceWaste(
                    namespace="ns-1",
                    cpu_requested_cores=10.0,
                    cpu_actual_avg_cores=2.0,
                    cpu_waste_pct=80.0,
                    cpu_wasted_cores=8.0,
                    memory_requested_gb=40.0,
                    memory_actual_avg_gb=10.0,
                    memory_waste_pct=75.0,
                    memory_wasted_gb=30.0,
                    is_over_provisioned=True,
                ),
                NamespaceWaste(
                    namespace="ns-2",
                    cpu_requested_cores=5.0,
                    cpu_actual_avg_cores=4.0,
                    cpu_waste_pct=20.0,
                    cpu_wasted_cores=1.0,
                    memory_requested_gb=40.0,
                    memory_actual_avg_gb=10.0,
                    memory_waste_pct=75.0,
                    memory_wasted_gb=30.0,
                    is_over_provisioned=True,
                ),
            ],
            excluded=[
                ExcludedNamespace(
                    namespace="ns-3",
                    reason="No resource requests set — burstable or BestEffort pods excluded",
                ),
                ExcludedNamespace(
                    namespace="ns-4",
                    reason="Namespace age < 24h — insufficient data for 7-day waste analysis",
                ),
            ],
            total_wasted_cpu_cores=9.0,
            total_wasted_memory_gb=60.0,
            analysis_window_days=7,
        )

    def test_excluded_payload_exact(self) -> None:
        service = NamespaceOverProvisioningService()
        data = [_raw(namespace="ns-x", has_resource_requests=False)]
        report = service.analyze(data, top_n=5, analysis_window_days=7)

        assert report.excluded == [
            ExcludedNamespace(
                namespace="ns-x",
                reason="No resource requests set — burstable or BestEffort pods excluded",
            )
        ]
        assert report.total_wasted_cpu_cores == 0.0
        assert report.total_wasted_memory_gb == 0.0


class TestComputeNamespaceWasteExact:
    def test_zero_requested_waste_zero(self) -> None:
        result = _compute_namespace_waste(
            _raw(cpu_requested=0.0, mem_requested=0.0, cpu_actual=5.0, mem_actual=10.0)
        )

        assert result == NamespaceWaste(
            namespace="default",
            cpu_requested_cores=0.0,
            cpu_actual_avg_cores=5.0,
            cpu_waste_pct=0.0,
            cpu_wasted_cores=0.0,
            memory_requested_gb=0.0,
            memory_actual_avg_gb=10.0,
            memory_waste_pct=0.0,
            memory_wasted_gb=0.0,
            is_over_provisioned=False,
        )

    def test_none_requested_treated_as_zero(self) -> None:
        result = _compute_namespace_waste(
            _raw(cpu_requested=None, mem_requested=None, cpu_actual=5.0, mem_actual=10.0)
        )

        assert result.cpu_requested_cores == 0.0
        assert result.memory_requested_gb == 0.0

    def test_none_actual_reports_zero_waste(self) -> None:
        result = _compute_namespace_waste(_raw(cpu_actual=None, mem_actual=None))

        assert result == NamespaceWaste(
            namespace="default",
            cpu_requested_cores=10.0,
            cpu_actual_avg_cores=0.0,
            cpu_waste_pct=0.0,
            cpu_wasted_cores=0.0,
            memory_requested_gb=40.0,
            memory_actual_avg_gb=0.0,
            memory_waste_pct=0.0,
            memory_wasted_gb=0.0,
            is_over_provisioned=False,
        )

    def test_over_provisioned_at_threshold_boundary(self) -> None:
        exact = _raw(cpu_requested=10.0, cpu_actual=5.0, mem_requested=10.0, mem_actual=5.0)
        assert _compute_namespace_waste(exact).is_over_provisioned is False

    def test_over_provisioned_above_threshold(self) -> None:
        above = _raw(cpu_requested=10.0, cpu_actual=4.9, mem_requested=10.0, mem_actual=4.9)
        assert _compute_namespace_waste(above).is_over_provisioned is True


class TestExclusionReasonBoundary:
    def test_age_exactly_24_hours_is_eligible(self) -> None:
        assert _exclusion_reason(_raw(age_hours=24.0)) is None

    def test_age_just_below_24_hours_is_excluded(self) -> None:
        reason = _exclusion_reason(_raw(age_hours=23.9))
        assert reason is not None


class TestAnyActualUsageBoundaries:
    def test_cpu_only_usage_true(self) -> None:
        data = [_raw(cpu_actual=1.0, mem_actual=0.0)]
        assert any_actual_usage_present(data) is True

    def test_zero_actual_usage_false(self) -> None:
        data = [_raw(cpu_actual=0.0, mem_actual=0.0)]
        assert any_actual_usage_present(data) is False

    def test_sub_one_cpu_usage_true(self) -> None:
        data = [_raw(cpu_actual=0.5, mem_actual=None)]
        assert any_actual_usage_present(data) is True

    def test_memory_only_usage_true(self) -> None:
        data = [_raw(cpu_actual=None, mem_actual=2.0)]
        assert any_actual_usage_present(data) is True

    def test_sub_one_memory_usage_true(self) -> None:
        data = [_raw(cpu_actual=0.0, mem_actual=0.5)]
        assert any_actual_usage_present(data) is True


class TestWastePairFractionalWaste:
    def test_waste_below_one_unit_kept_as_fraction(self) -> None:
        pct, wasted = _waste_pair(10.0, 9.5)
        assert wasted == 0.5  # noqa: PLR2004
        assert pct == 5.0  # noqa: PLR2004
