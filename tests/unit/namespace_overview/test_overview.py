"""Unit tests for build_namespace_overview — pure domain orchestration.

Test data mirrors the ticket's own fixture: staging namespace, 12 pods (9 running,
3 failed), 4 deployments (3 ready), 5 services, checkout-pod-abc CrashLoopBackOff,
payment-deploy 0/2 replicas ready → Degraded overall (per the ticket's own example).
"""

from __future__ import annotations

from hexawyn.application.ports.driven.namespace_overview_port import (
    DeploymentStatusRaw,
    HpaStatusRaw,
    NamespaceOverviewRawData,
    PodStatusRaw,
)
from hexawyn.domain.models.namespace_overview import NamespaceHealthStatus, NamespaceOverviewRequest
from hexawyn.domain.services.namespace_overview.overview import build_namespace_overview


def _raw(
    namespace_status: str = "Active",
    pods: list[PodStatusRaw] | None = None,
    deployments: list[DeploymentStatusRaw] | None = None,
    services_count: int = 0,
    hpas: list[HpaStatusRaw] | None = None,
) -> NamespaceOverviewRawData:
    return NamespaceOverviewRawData(
        namespace_status=namespace_status,
        pods=pods or [],
        deployments=deployments or [],
        services_count=services_count,
        hpas=hpas or [],
    )


def _request(max_tokens: int = 2000) -> NamespaceOverviewRequest:
    return NamespaceOverviewRequest(namespace="staging", max_tokens=max_tokens)


class TestAllHealthy:
    """TC1: namespace with 10 pods all Running → Healthy score, no issues listed."""

    def test_healthy_no_issues(self) -> None:
        raw = _raw(pods=[PodStatusRaw(name=f"pod-{i}", status="Running") for i in range(10)])

        report = build_namespace_overview(_request(), raw)

        assert report.health_status == NamespaceHealthStatus.HEALTHY
        assert report.unhealthy_resources == []
        assert report.root_cause == ""


class TestDegradedPods:
    """TC2: 3 pods in CrashLoopBackOff → Degraded, only failing pods named."""

    def test_only_failing_pods_named(self) -> None:
        raw = _raw(
            pods=[PodStatusRaw(name=f"pod-{i}", status="Running") for i in range(7)]
            + [PodStatusRaw(name=f"failing-pod-{i}", status="CrashLoopBackOff") for i in range(3)]
        )

        report = build_namespace_overview(_request(), raw)

        assert report.health_status == NamespaceHealthStatus.DEGRADED
        assert len(report.unhealthy_resources) == 3
        assert all(r.kind == "Pod" for r in report.unhealthy_resources)

    def test_partially_ready_deployment_is_degraded(self) -> None:
        raw = _raw(
            deployments=[
                DeploymentStatusRaw(name="checkout-deploy", ready_replicas=1, desired_replicas=3)
            ]
        )

        report = build_namespace_overview(_request(), raw)

        assert report.health_status == NamespaceHealthStatus.DEGRADED
        assert any(r.name == "checkout-deploy" for r in report.unhealthy_resources)


class TestCriticalDeployment:
    """TC3: deployment with 0/3 replicas ready → Critical, deployment name surfaced."""

    def test_deployment_named_and_critical(self) -> None:
        raw = _raw(
            deployments=[
                DeploymentStatusRaw(name="payment-deploy", ready_replicas=0, desired_replicas=3)
            ]
        )

        report = build_namespace_overview(_request(), raw)

        assert report.health_status == NamespaceHealthStatus.CRITICAL
        assert any(r.name == "payment-deploy" for r in report.unhealthy_resources)
        assert "payment-deploy" in report.root_cause


class TestEmptyNamespace:
    """TC5: empty namespace → 'namespace exists but has no workloads'."""

    def test_empty_namespace_message(self) -> None:
        raw = _raw()

        report = build_namespace_overview(_request(), raw)

        assert report.is_empty is True
        assert "no workloads" in report.summary.lower()
        assert report.health_status == NamespaceHealthStatus.HEALTHY


class TestTerminatingNamespace:
    """Edge case: namespace being terminated → status shows Terminating,
    separate from the health score."""

    def test_terminating_status_surfaced_separately(self) -> None:
        raw = _raw(
            namespace_status="Terminating",
            pods=[PodStatusRaw(name="pod-a", status="Running")],
        )

        report = build_namespace_overview(_request(), raw)

        assert report.namespace_status == "Terminating"
        assert report.health_status == NamespaceHealthStatus.HEALTHY


class TestHpaSoftWarning:
    """Edge case: HPA at max replicas → noted as a soft warning, doesn't
    escalate the health score."""

    def test_hpa_at_max_is_warning_not_unhealthy(self) -> None:
        raw = _raw(
            pods=[PodStatusRaw(name="pod-a", status="Running")],
            hpas=[HpaStatusRaw(name="checkout-hpa", current_replicas=10, max_replicas=10)],
        )

        report = build_namespace_overview(_request(), raw)

        assert report.health_status == NamespaceHealthStatus.HEALTHY
        assert len(report.warnings) == 1
        assert "checkout-hpa" in report.warnings[0]
        assert report.unhealthy_resources == []

    def test_hpa_below_max_is_not_a_warning(self) -> None:
        raw = _raw(hpas=[HpaStatusRaw(name="checkout-hpa", current_replicas=5, max_replicas=10)])

        report = build_namespace_overview(_request(), raw)

        assert report.warnings == []


class TestMultipleFailingResourceTypes:
    """Edge case: multiple failing resources of different types simultaneously."""

    def test_critical_wins_and_both_kinds_listed(self) -> None:
        raw = _raw(
            pods=[PodStatusRaw(name="checkout-pod-abc", status="CrashLoopBackOff")],
            deployments=[
                DeploymentStatusRaw(name="payment-deploy", ready_replicas=0, desired_replicas=2)
            ],
        )

        report = build_namespace_overview(_request(), raw)

        assert report.health_status == NamespaceHealthStatus.CRITICAL
        kinds = {r.kind for r in report.unhealthy_resources}
        assert kinds == {"Pod", "Deployment"}
        assert "payment-deploy" in report.root_cause


class TestTokenBudgetIntegration:
    """TC4: large number of unhealthy resources → output stays under token budget."""

    def test_truncation_reflected_in_report(self) -> None:
        raw = _raw(
            pods=[
                PodStatusRaw(name=f"failing-pod-{i}", status="CrashLoopBackOff") for i in range(200)
            ]
        )

        report = build_namespace_overview(_request(max_tokens=200), raw)

        assert report.estimated_tokens <= 200
        assert report.has_more_unhealthy is True
        assert report.remaining_unhealthy_count > 0
