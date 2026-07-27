from __future__ import annotations

from hexawyn.domain.models.namespace_waste import NamespaceRawData
from hexawyn.domain.services.namespace_waste.namespace_over_provisioning_service import (
    NamespaceOverProvisioningService,
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
