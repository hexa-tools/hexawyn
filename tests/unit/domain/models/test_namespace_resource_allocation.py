from __future__ import annotations

from hexawyn.domain.models.namespace_resource_allocation import (
    NamespaceResourceAllocation,
    NamespaceResourceAllocationReport,
)


class TestNamespaceResourceAllocationModel:
    def test_typed_dict_fields_accessible(self) -> None:
        allocation: NamespaceResourceAllocation = {
            "namespace": "test-ns",
            "total_cpu_cores": 4.0,
            "total_memory_gb": 8.0,
            "pod_count": 6,
        }
        assert allocation["namespace"] == "test-ns"
        assert allocation["total_cpu_cores"] == 4.0  # noqa: PLR2004
        assert allocation["total_memory_gb"] == 8.0  # noqa: PLR2004
        assert allocation["pod_count"] == 6  # noqa: PLR2004

    def test_typed_dict_float_conversion(self) -> None:
        allocation: NamespaceResourceAllocation = {
            "namespace": "float-test",
            "total_cpu_cores": 3.5,
            "total_memory_gb": 7.25,
            "pod_count": 3,
        }
        assert isinstance(allocation["total_cpu_cores"], float)
        assert isinstance(allocation["total_memory_gb"], float)
        assert isinstance(allocation["pod_count"], int)

    def test_zero_values_accepted(self) -> None:
        allocation: NamespaceResourceAllocation = {
            "namespace": "zero-ns",
            "total_cpu_cores": 0.0,
            "total_memory_gb": 0.0,
            "pod_count": 0,
        }
        assert allocation["total_cpu_cores"] == 0.0
        assert allocation["pod_count"] == 0

    def test_report_initializes_empty_allocations(self) -> None:
        report = NamespaceResourceAllocationReport()
        assert report.allocations == []

    def test_report_accepts_custom_allocations(self) -> None:
        allocations: list[NamespaceResourceAllocation] = [
            {"namespace": "ns1", "total_cpu_cores": 2.0, "total_memory_gb": 4.0, "pod_count": 2},
        ]
        report = NamespaceResourceAllocationReport(allocations=allocations)
        assert len(report.allocations) == 1
        assert report.allocations[0]["namespace"] == "ns1"
