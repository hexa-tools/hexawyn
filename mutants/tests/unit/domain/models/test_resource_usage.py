from __future__ import annotations

from hexawyn.domain.models.resource_usage import (
    NamespaceResourceUsageSummary,
    PodResourceUsage,
    ResourceUsageReport,
)


class TestResourceUsageModels:
    def test_pod_resource_usage_fields_accessible(self) -> None:
        pod: PodResourceUsage = {
            "name": "test-pod-abc",
            "namespace": "dev",
            "cpu_requested_cores": 2.0,
            "cpu_used_cores": 0.35,
            "cpu_utilization_pct": 17.5,
            "memory_requested_gb": 4.0,
            "memory_used_gb": 1.5,
            "memory_utilization_pct": 37.5,
        }
        assert pod["name"] == "test-pod-abc"
        assert pod["cpu_utilization_pct"] == 17.5  # noqa: PLR2004

    def test_pod_resource_usage_negative_utilization_for_no_requests(self) -> None:
        pod: PodResourceUsage = {
            "name": "bare-pod",
            "namespace": "ns",
            "cpu_requested_cores": 0.0,
            "cpu_used_cores": 0.5,
            "cpu_utilization_pct": -1.0,
            "memory_requested_gb": 0.0,
            "memory_used_gb": 0.3,
            "memory_utilization_pct": -1.0,
        }
        assert pod["cpu_utilization_pct"] == -1.0
        assert pod["memory_utilization_pct"] == -1.0

    def test_namespace_summary_aggregates(self) -> None:
        summary: NamespaceResourceUsageSummary = {
            "namespace": "dev",
            "pod_count": 3,
            "total_cpu_requested_cores": 6.0,
            "total_cpu_used_cores": 1.05,
            "total_cpu_utilization_pct": 17.5,
            "total_memory_requested_gb": 12.0,
            "total_memory_used_gb": 4.5,
            "total_memory_utilization_pct": 37.5,
        }
        assert summary["pod_count"] == 3  # noqa: PLR2004
        assert summary["total_cpu_requested_cores"] == 6.0  # noqa: PLR2004

    def test_report_defaults(self) -> None:
        report = ResourceUsageReport()
        assert report.pods == []
        assert report.namespace_summary == []
        assert report.metrics_server_available is False
        assert report.source == ""

    def test_report_populated_with_usage_entries(self) -> None:
        pods: list[PodResourceUsage] = [
            {
                "name": "p1",
                "namespace": "ns",
                "cpu_requested_cores": 1.0,
                "cpu_used_cores": 0.3,
                "cpu_utilization_pct": 30.0,
                "memory_requested_gb": 2.0,
                "memory_used_gb": 0.8,
                "memory_utilization_pct": 40.0,
            },
        ]
        summary: list[NamespaceResourceUsageSummary] = [
            {
                "namespace": "ns",
                "pod_count": 1,
                "total_cpu_requested_cores": 1.0,
                "total_cpu_used_cores": 0.3,
                "total_cpu_utilization_pct": 30.0,
                "total_memory_requested_gb": 2.0,
                "total_memory_used_gb": 0.8,
                "total_memory_utilization_pct": 40.0,
            },
        ]
        report = ResourceUsageReport(
            pods=pods,
            namespace_summary=summary,
            metrics_server_available=True,
            source="metrics-server",
        )
        assert len(report.pods) == 1
        assert report.metrics_server_available is True
        assert report.source == "metrics-server"
