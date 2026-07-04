"""Unit tests for compute_total_workload_needs / find_unschedulable_workloads
— pure aggregation and per-pod-vs-largest-node checks."""

from __future__ import annotations

import pytest
from hexawyn.domain.models.headroom_simulation import ProposedWorkload
from hexawyn.domain.services.headroom_simulation.workload_sizing import (
    compute_total_workload_needs,
    find_unschedulable_workloads,
)


def _ticket_workloads() -> list[ProposedWorkload]:
    return [
        ProposedWorkload(
            name="notification-service",
            cpu_request_per_pod="250m",
            memory_request_per_pod="256Mi",
            replicas=2,
        ),
        ProposedWorkload(
            name="analytics-service",
            cpu_request_per_pod="500m",
            memory_request_per_pod="512Mi",
            replicas=2,
        ),
        ProposedWorkload(
            name="reporting-service",
            cpu_request_per_pod="250m",
            memory_request_per_pod="256Mi",
            replicas=2,
        ),
    ]


class TestComputeTotalWorkloadNeeds:
    def test_matches_ticket_test_data(self) -> None:
        total_cpu, total_memory = compute_total_workload_needs(_ticket_workloads())

        assert total_cpu == pytest.approx(2.0)
        assert total_memory == pytest.approx(2.0)

    def test_default_replicas_applied_when_unspecified(self) -> None:
        """Edge case: no replicas specified → default 2 replicas per service."""
        workload = ProposedWorkload(
            name="solo-service", cpu_request_per_pod="500m", memory_request_per_pod="512Mi"
        )

        total_cpu, total_memory = compute_total_workload_needs([workload])

        assert total_cpu == pytest.approx(1.0)
        assert total_memory == pytest.approx(1.0)

    def test_empty_workload_list_returns_zero(self) -> None:
        total_cpu, total_memory = compute_total_workload_needs([])

        assert total_cpu == 0.0
        assert total_memory == 0.0


class TestFindUnschedulableWorkloads:
    def test_flags_workload_exceeding_largest_node_cpu(self) -> None:
        """Edge case: proposed workload requests exceed largest single node."""
        huge = ProposedWorkload(
            name="huge-service", cpu_request_per_pod="16", memory_request_per_pod="1Gi"
        )

        unschedulable = find_unschedulable_workloads(
            [huge], largest_node_cpu_cores=8.0, largest_node_memory_gb=32.0
        )

        assert unschedulable == ["huge-service"]

    def test_flags_workload_exceeding_largest_node_memory(self) -> None:
        huge = ProposedWorkload(
            name="memory-hog", cpu_request_per_pod="1", memory_request_per_pod="64Gi"
        )

        unschedulable = find_unschedulable_workloads(
            [huge], largest_node_cpu_cores=8.0, largest_node_memory_gb=32.0
        )

        assert unschedulable == ["memory-hog"]

    def test_fitting_workloads_are_not_flagged(self) -> None:
        unschedulable = find_unschedulable_workloads(
            _ticket_workloads(), largest_node_cpu_cores=8.0, largest_node_memory_gb=32.0
        )

        assert unschedulable == []
