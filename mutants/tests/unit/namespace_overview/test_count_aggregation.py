"""Unit tests for aggregate_counts — pure count aggregation logic."""

from __future__ import annotations

from hexawyn.application.ports.driven.namespace_overview_port import (
    DeploymentStatusRaw,
    PodStatusRaw,
)
from hexawyn.domain.services.namespace_overview.count_aggregation import aggregate_counts


def _pod(name: str, status: str = "Running") -> PodStatusRaw:
    return PodStatusRaw(name=name, status=status)


def _deployment(name: str, ready: int, desired: int) -> DeploymentStatusRaw:
    return DeploymentStatusRaw(name=name, ready_replicas=ready, desired_replicas=desired)


class TestAggregateCounts:
    def test_ticket_fixture_counts(self) -> None:
        """Test Data: 12 pods (9 running, 3 failed), 4 deployments (3 ready), 5 services."""
        pods = [_pod(f"pod-{i}") for i in range(9)] + [
            _pod(f"failed-pod-{i}", status="CrashLoopBackOff") for i in range(3)
        ]
        deployments = [
            _deployment("dep-a", 2, 2),
            _deployment("dep-b", 1, 1),
            _deployment("dep-c", 3, 3),
            _deployment("payment-deploy", 0, 2),
        ]

        counts = aggregate_counts(pods, deployments, services_count=5)

        assert counts.pods_total == 12  # noqa: PLR2004
        assert counts.pods_running == 9  # noqa: PLR2004
        assert counts.pods_failed == 3  # noqa: PLR2004
        assert counts.deployments_total == 4  # noqa: PLR2004
        assert counts.deployments_ready == 3  # noqa: PLR2004
        assert counts.services_total == 5  # noqa: PLR2004

    def test_all_pods_running_no_failures(self) -> None:
        """TC1: 10 pods all Running."""
        pods = [_pod(f"pod-{i}") for i in range(10)]

        counts = aggregate_counts(pods, [], services_count=0)

        assert counts.pods_total == 10  # noqa: PLR2004
        assert counts.pods_running == 10  # noqa: PLR2004
        assert counts.pods_failed == 0

    def test_empty_namespace_all_zero(self) -> None:
        counts = aggregate_counts([], [], services_count=0)

        assert counts.pods_total == 0
        assert counts.deployments_total == 0
        assert counts.services_total == 0
