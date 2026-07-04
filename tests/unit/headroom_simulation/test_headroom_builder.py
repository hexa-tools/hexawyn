"""Unit tests for simulate_headroom — pure orchestration of workload sizing,
utilization projection, verdict tiering, binding constraint, and node
recommendation."""

from __future__ import annotations

import pytest
from hexawyn.domain.models.headroom_simulation import (
    ClusterHeadroomSnapshot,
    HeadroomSimulationRequest,
    ProposedWorkload,
)
from hexawyn.domain.services.headroom_simulation.headroom_builder import simulate_headroom


def _snapshot(
    total_cpu: float = 80.0,
    total_memory: float = 320.0,
    used_cpu: float = 48.0,
    used_memory: float = 192.0,
    node_count: int = 10,
    largest_node_cpu: float = 8.0,
    largest_node_memory: float = 32.0,
    autoscaler_enabled: bool = False,
) -> ClusterHeadroomSnapshot:
    return ClusterHeadroomSnapshot(
        total_allocatable_cpu_cores=total_cpu,
        total_allocatable_memory_gb=total_memory,
        used_cpu_cores=used_cpu,
        used_memory_gb=used_memory,
        node_count=node_count,
        largest_node_cpu_cores=largest_node_cpu,
        largest_node_memory_gb=largest_node_memory,
        autoscaler_enabled=autoscaler_enabled,
    )


def _workload(cpu: str, memory: str, replicas: int = 2, name: str = "svc") -> ProposedWorkload:
    return ProposedWorkload(
        name=name, cpu_request_per_pod=cpu, memory_request_per_pod=memory, replicas=replicas
    )


class TestFits:
    def test_tc1_sixty_percent_plus_small_load_fits(self) -> None:
        """TC1: current CPU 60%, 3 services need 1.5 cores total, 10 nodes → fits (62% after)."""
        request = HeadroomSimulationRequest(
            proposed_workloads=[_workload("750m", "256Mi", replicas=2, name="svc")]
        )

        report = simulate_headroom(request, _snapshot())

        assert report.current_cpu_utilization_percent == 60.0
        assert report.post_cpu_utilization_percent == pytest.approx(62.0, abs=0.2)
        assert report.verdict == "fits"


class TestTight:
    def test_tc2_eighty_five_percent_plus_small_load_is_tight(self) -> None:
        """TC2: current CPU 85%, +1.5 cores → tight (87% after)."""
        request = HeadroomSimulationRequest(
            proposed_workloads=[_workload("750m", "256Mi", replicas=2, name="svc")]
        )
        snapshot = _snapshot(used_cpu=68.0)

        report = simulate_headroom(request, snapshot)

        assert report.current_cpu_utilization_percent == 85.0
        assert report.post_cpu_utilization_percent == pytest.approx(87.0, abs=0.2)
        assert report.verdict == "tight"


class TestNeedsNodes:
    def test_tc3_ninety_percent_plus_large_load_needs_one_node(self) -> None:
        """TC3: current CPU 90%, 3 services need 3 cores total → needs nodes,
        recommend +1 node (40-core/5-node cluster)."""
        request = HeadroomSimulationRequest(
            proposed_workloads=[_workload("1500m", "256Mi", replicas=2, name="svc")]
        )
        snapshot = _snapshot(
            total_cpu=40.0, total_memory=200.0, used_cpu=36.0, used_memory=20.0, node_count=5
        )

        report = simulate_headroom(request, snapshot)

        assert report.post_cpu_utilization_percent == 97.5
        assert report.verdict == "needs_nodes"
        assert report.recommended_additional_nodes == 1


class TestBindingConstraint:
    def test_tc4_memory_abundant_cpu_tight_binding_is_cpu(self) -> None:
        """TC4: memory headroom abundant but CPU tight → CPU is binding constraint."""
        request = HeadroomSimulationRequest(
            proposed_workloads=[_workload("375m", "10Mi", replicas=2, name="svc")]
        )
        snapshot = _snapshot(used_cpu=68.0, used_memory=10.0)

        report = simulate_headroom(request, snapshot)

        assert report.post_cpu_utilization_percent > report.post_memory_utilization_percent
        assert report.binding_constraint == "CPU"


class TestNoWorkloadsProposed:
    def test_tc5_zero_workloads_is_current_state_summary(self) -> None:
        """TC5: 0 new workloads proposed → current headroom summary only."""
        report = simulate_headroom(HeadroomSimulationRequest(), _snapshot())

        assert report.total_new_cpu_cores == 0.0
        assert report.total_new_memory_gb == 0.0
        assert report.post_cpu_utilization_percent == report.current_cpu_utilization_percent
        assert report.binding_constraint == "None"
        assert "no new workloads" in report.summary.lower()


class TestAutoscalerPassthrough:
    def test_autoscaler_enabled_noted_but_does_not_change_verdict(self) -> None:
        """Edge case: autoscaler enabled → simulation still runs, noted as safety net."""
        request = HeadroomSimulationRequest(
            proposed_workloads=[_workload("1500m", "256Mi", replicas=2, name="svc")]
        )
        snapshot = _snapshot(total_cpu=40.0, used_cpu=36.0, node_count=5, autoscaler_enabled=True)

        report = simulate_headroom(request, snapshot)

        assert report.verdict == "needs_nodes"
        assert report.autoscaler_enabled is True
        assert "autoscaler" in report.summary.lower()


class TestUnschedulableWorkload:
    def test_workload_exceeding_largest_node_forces_needs_nodes(self) -> None:
        """Edge case: proposed workload requests exceed largest single node."""
        request = HeadroomSimulationRequest(
            proposed_workloads=[_workload("16", "1Gi", replicas=1, name="huge-service")]
        )

        report = simulate_headroom(request, _snapshot())

        assert report.verdict == "needs_nodes"
        assert report.unschedulable_workloads == ["huge-service"]


class TestFreshCluster:
    def test_zero_current_usage_all_workloads_fit_easily(self) -> None:
        """Edge case: current usage at 0% (fresh cluster) → headroom=100%."""
        request = HeadroomSimulationRequest(
            proposed_workloads=[_workload("500m", "512Mi", replicas=2, name="svc")]
        )
        snapshot = _snapshot(used_cpu=0.0, used_memory=0.0)

        report = simulate_headroom(request, snapshot)

        assert report.current_cpu_utilization_percent == 0.0
        assert report.verdict == "fits"
