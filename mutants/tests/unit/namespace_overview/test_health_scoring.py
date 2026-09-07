"""Unit tests for is_pod_unhealthy / classify_deployment / compute_health_status /
build_root_cause — pure health-scoring logic."""

from __future__ import annotations

from hexawyn.domain.models.namespace_overview import NamespaceHealthStatus, UnhealthyResource
from hexawyn.domain.services.namespace_overview.health_scoring import (
    build_root_cause,
    classify_deployment,
    compute_health_status,
    is_pod_unhealthy,
)


class TestIsPodUnhealthy:
    def test_running_is_healthy(self) -> None:
        assert is_pod_unhealthy("Running") is False

    def test_crashloopbackoff_is_unhealthy(self) -> None:
        """TC2."""
        assert is_pod_unhealthy("CrashLoopBackOff") is True

    def test_pending_is_unhealthy(self) -> None:
        """Edge case: Pending pod (unschedulable) → flagged."""
        assert is_pod_unhealthy("Pending") is True


class TestClassifyDeployment:
    def test_zero_ready_of_nonzero_desired_is_critical(self) -> None:
        """TC3: 0/3 replicas ready → Critical."""
        assert classify_deployment(ready=0, desired=3) == "critical"

    def test_partially_ready_is_degraded(self) -> None:
        assert classify_deployment(ready=1, desired=3) == "degraded"

    def test_fully_ready_is_none(self) -> None:
        assert classify_deployment(ready=3, desired=3) is None

    def test_zero_desired_is_none(self) -> None:
        """A deployment intentionally scaled to 0 isn't an issue."""
        assert classify_deployment(ready=0, desired=0) is None


class TestComputeHealthStatus:
    def test_no_issues_is_healthy(self) -> None:
        """TC1."""
        assert compute_health_status(has_critical=False, has_degraded=False) == (
            NamespaceHealthStatus.HEALTHY
        )

    def test_degraded_only_is_degraded(self) -> None:
        """TC2."""
        assert compute_health_status(has_critical=False, has_degraded=True) == (
            NamespaceHealthStatus.DEGRADED
        )

    def test_critical_wins_over_degraded(self) -> None:
        """Edge case: multiple failing resources of different types simultaneously —
        critical (deployment down) must win over degraded (pod issues)."""
        assert compute_health_status(has_critical=True, has_degraded=True) == (
            NamespaceHealthStatus.CRITICAL
        )


class TestBuildRootCause:
    def test_empty_list_returns_empty_string(self) -> None:
        assert build_root_cause([]) == ""

    def test_single_issue_states_it_directly(self) -> None:
        resource = UnhealthyResource(name="checkout-pod-abc", kind="Pod", reason="CrashLoopBackOff")

        cause = build_root_cause([resource])

        assert "checkout-pod-abc" in cause
        assert "CrashLoopBackOff" in cause

    def test_deployment_issue_prioritized_over_pod_issue(self) -> None:
        pod_issue = UnhealthyResource(
            name="checkout-pod-abc", kind="Pod", reason="CrashLoopBackOff"
        )
        deployment_issue = UnhealthyResource(
            name="payment-deploy", kind="Deployment", reason="0/2 replicas ready"
        )

        cause = build_root_cause([pod_issue, deployment_issue])

        assert "payment-deploy" in cause

    def test_multiple_issues_note_additional_count(self) -> None:
        resources = [
            UnhealthyResource(name="pod-a", kind="Pod", reason="CrashLoopBackOff"),
            UnhealthyResource(name="pod-b", kind="Pod", reason="CrashLoopBackOff"),
        ]

        cause = build_root_cause(resources)

        assert "1 more" in cause or "+1" in cause
