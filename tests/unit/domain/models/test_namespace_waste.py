"""Unit tests for namespace_waste domain models."""

import pytest
from hexawyn.domain.models.namespace_waste import (
    ExcludedNamespace,
    NamespaceWaste,
    OverProvisioningReport,
)


def _waste(
    namespace: str = "dev",
    cpu_req: float = 8.0,
    cpu_actual: float = 0.45,
    cpu_waste_pct: float = 94.4,
    cpu_wasted: float = 7.55,
    mem_req: float = 16.0,
    mem_actual: float = 1.2,
    mem_waste_pct: float = 92.5,
    mem_wasted: float = 14.8,
    is_over: bool = True,
) -> NamespaceWaste:
    return NamespaceWaste(
        namespace=namespace,
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=is_over,
    )


class TestNamespaceWaste:
    def test_is_frozen(self) -> None:
        ns = _waste()
        with pytest.raises(AttributeError):
            ns.namespace = "other"  # type: ignore[misc]

    def test_max_waste_pct_returns_cpu_when_cpu_higher(self) -> None:
        ns = _waste(cpu_waste_pct=94.4, mem_waste_pct=92.5)
        assert ns.max_waste_pct == 94.4

    def test_max_waste_pct_returns_memory_when_memory_higher(self) -> None:
        ns = _waste(cpu_waste_pct=30.0, mem_waste_pct=80.0)
        assert ns.max_waste_pct == 80.0

    def test_max_waste_pct_equal_values(self) -> None:
        ns = _waste(cpu_waste_pct=50.0, mem_waste_pct=50.0)
        assert ns.max_waste_pct == 50.0

    def test_is_over_provisioned_true(self) -> None:
        ns = _waste(is_over=True)
        assert ns.is_over_provisioned is True

    def test_is_over_provisioned_false(self) -> None:
        ns = _waste(cpu_waste_pct=12.5, mem_waste_pct=12.5, is_over=False)
        assert ns.is_over_provisioned is False

    def test_all_fields_stored(self) -> None:
        ns = _waste()
        assert ns.namespace == "dev"
        assert ns.cpu_requested_cores == 8.0
        assert ns.cpu_actual_avg_cores == 0.45
        assert ns.cpu_wasted_cores == 7.55
        assert ns.memory_requested_gb == 16.0
        assert ns.memory_actual_avg_gb == 1.2
        assert ns.memory_wasted_gb == 14.8


class TestExcludedNamespace:
    def test_is_frozen(self) -> None:
        exc = ExcludedNamespace(namespace="burstable", reason="No requests")
        with pytest.raises(AttributeError):
            exc.namespace = "other"  # type: ignore[misc]

    def test_stores_namespace_and_reason(self) -> None:
        exc = ExcludedNamespace(namespace="burstable", reason="No resource requests set")
        assert exc.namespace == "burstable"
        assert exc.reason == "No resource requests set"


class TestOverProvisioningReport:
    def test_default_construction(self) -> None:
        report = OverProvisioningReport(
            namespaces=[],
            excluded=[],
            total_wasted_cpu_cores=0.0,
            total_wasted_memory_gb=0.0,
            analysis_window_days=7,
        )
        assert report.namespaces == []
        assert report.excluded == []
        assert report.total_wasted_cpu_cores == 0.0
        assert report.total_wasted_memory_gb == 0.0
        assert report.analysis_window_days == 7

    def test_stores_namespaces_list(self) -> None:
        ns = _waste()
        report = OverProvisioningReport(
            namespaces=[ns],
            excluded=[],
            total_wasted_cpu_cores=7.55,
            total_wasted_memory_gb=14.8,
            analysis_window_days=7,
        )
        assert len(report.namespaces) == 1
        assert report.namespaces[0].namespace == "dev"
