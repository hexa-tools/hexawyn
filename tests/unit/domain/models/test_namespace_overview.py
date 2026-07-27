"""Unit tests for conservative-namespace-overview domain models (pure dataclasses)."""

from __future__ import annotations

from hexawyn.domain.models.namespace_overview import (
    NamespaceCounts,
    NamespaceHealthStatus,
    NamespaceOverviewReport,
    NamespaceOverviewRequest,
    UnhealthyResource,
)


class TestNamespaceHealthStatus:
    def test_expected_members(self) -> None:
        assert NamespaceHealthStatus.HEALTHY.value == "Healthy"
        assert NamespaceHealthStatus.DEGRADED.value == "Degraded"
        assert NamespaceHealthStatus.CRITICAL.value == "Critical"


class TestNamespaceCounts:
    def test_fields(self) -> None:
        counts = NamespaceCounts(
            pods_total=12,
            pods_running=9,
            pods_failed=3,
            deployments_total=4,
            deployments_ready=3,
            services_total=5,
        )
        assert counts.pods_total == 12  # noqa: PLR2004
        assert counts.deployments_ready == 3  # noqa: PLR2004


class TestUnhealthyResource:
    def test_fields(self) -> None:
        resource = UnhealthyResource(name="checkout-pod-abc", kind="Pod", reason="CrashLoopBackOff")
        assert resource.kind == "Pod"


class TestNamespaceOverviewRequest:
    def test_defaults(self) -> None:
        request = NamespaceOverviewRequest(namespace="staging")
        assert request.max_tokens == 2000  # noqa: PLR2004

    def test_custom_max_tokens(self) -> None:
        request = NamespaceOverviewRequest(namespace="staging", max_tokens=500)
        assert request.max_tokens == 500  # noqa: PLR2004


class TestNamespaceOverviewReport:
    def test_defaults(self) -> None:
        counts = NamespaceCounts(
            pods_total=0,
            pods_running=0,
            pods_failed=0,
            deployments_total=0,
            deployments_ready=0,
            services_total=0,
        )
        report = NamespaceOverviewReport(
            namespace="staging",
            namespace_status="Active",
            counts=counts,
            health_status=NamespaceHealthStatus.HEALTHY,
        )
        assert report.root_cause == ""
        assert report.unhealthy_resources == []
        assert report.warnings == []
        assert report.has_more_unhealthy is False
        assert report.remaining_unhealthy_count == 0
        assert report.estimated_tokens == 0
        assert report.is_empty is False
        assert report.summary == ""

    def test_with_unhealthy_resources(self) -> None:
        counts = NamespaceCounts(
            pods_total=12,
            pods_running=9,
            pods_failed=3,
            deployments_total=4,
            deployments_ready=3,
            services_total=5,
        )
        resource = UnhealthyResource(name="checkout-pod-abc", kind="Pod", reason="CrashLoopBackOff")
        report = NamespaceOverviewReport(
            namespace="staging",
            namespace_status="Active",
            counts=counts,
            health_status=NamespaceHealthStatus.DEGRADED,
            unhealthy_resources=[resource],
        )
        assert len(report.unhealthy_resources) == 1
        assert report.health_status == NamespaceHealthStatus.DEGRADED
