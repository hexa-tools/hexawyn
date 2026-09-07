"""Unit tests for simulate_headroom — pure orchestration of workload sizing,
utilization projection, verdict tiering, binding constraint, and node
recommendation."""

from __future__ import annotations

import pytest
from hexawyn.domain.models.headroom_simulation import (
    ClusterHeadroomSnapshot,
    HeadroomSimulationReport,
    HeadroomSimulationRequest,
    ProposedWorkload,
)
from hexawyn.domain.services.headroom_simulation.headroom_builder import (
    _binding_constraint,
    _build_summary,
    _determine_verdict,
    _recommend_additional_nodes,
    _utilization_percent,
    simulate_headroom,
)


def _snapshot(  # noqa: PLR0913
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

        assert report.current_cpu_utilization_percent == 60.0  # noqa: PLR2004
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

        assert report.current_cpu_utilization_percent == 85.0  # noqa: PLR2004
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

        assert report.post_cpu_utilization_percent == 97.5  # noqa: PLR2004
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


class TestUtilizationPercent:
    def test_zero_total_returns_zero(self) -> None:
        assert _utilization_percent(used=5.0, total=0.0) == 0.0

    def test_fractional_total_below_one_computes_percent(self) -> None:
        assert _utilization_percent(used=0.25, total=0.5) == 50.0  # noqa: PLR2004

    def test_used_above_total_clamps_to_percent(self) -> None:
        assert _utilization_percent(used=120.0, total=100.0) == 120.0  # noqa: PLR2004


class TestDetermineVerdictBoundaries:
    def test_has_unschedulable_forces_needs_nodes(self) -> None:
        assert _determine_verdict(1.0, 1.0, has_unschedulable=True) == "needs_nodes"

    def test_exactly_ninety_five_is_needs_nodes(self) -> None:
        assert _determine_verdict(95.0, 50.0, has_unschedulable=False) == "needs_nodes"

    def test_exactly_eighty_is_tight(self) -> None:
        assert _determine_verdict(80.0, 50.0, has_unschedulable=False) == "tight"

    def test_below_eighty_is_fits(self) -> None:
        assert _determine_verdict(79.0, 50.0, has_unschedulable=False) == "fits"

    def test_uses_worst_of_cpu_and_memory(self) -> None:
        assert _determine_verdict(40.0, 96.0, has_unschedulable=False) == "needs_nodes"


class TestBindingConstraintBoundaries:
    def test_no_workloads_returns_none(self) -> None:
        assert _binding_constraint([], 80.0, 20.0) == "None"

    def test_cpu_memory_tie_picks_cpu(self) -> None:
        workload = _workload("1", "1Gi", name="svc")
        assert _binding_constraint([workload], 50.0, 50.0) == "CPU"

    def test_memory_higher_is_binding(self) -> None:
        workload = _workload("1", "1Gi", name="svc")
        assert _binding_constraint([workload], 40.0, 60.0) == "Memory"


class TestRecommendAdditionalNodes:
    def test_zero_node_count_returns_one(self) -> None:
        snapshot = _snapshot(node_count=0)
        assert _recommend_additional_nodes(90.0, 90.0, snapshot) == 1

    def test_zero_node_count_with_memory_over_target_returns_one(self) -> None:
        snapshot = _snapshot(node_count=0, total_cpu=100.0, total_memory=100.0)
        assert _recommend_additional_nodes(10.0, 90.0, snapshot) == 1

    def test_usage_below_target_returns_one(self) -> None:
        snapshot = _snapshot()
        assert _recommend_additional_nodes(20.0, 100.0, snapshot) == 1

    def test_uses_worst_of_cpu_and_memory(self) -> None:
        snapshot = _snapshot(total_cpu=40.0, used_cpu=36.0, node_count=5)
        assert _recommend_additional_nodes(39.0, 20.0, snapshot) == 1

    def test_rounds_partial_node_up(self) -> None:
        snapshot = _snapshot(total_cpu=40.0, used_cpu=36.0, node_count=5)
        result = _recommend_additional_nodes(38.0, 200.0, snapshot)
        assert result >= 1

    def _small_snapshot(self, total: float, node_count: int) -> ClusterHeadroomSnapshot:
        return ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=total,
            total_allocatable_memory_gb=total,
            used_cpu_cores=0.0,
            used_memory_gb=0.0,
            node_count=node_count,
            largest_node_cpu_cores=total,
            largest_node_memory_gb=total,
            autoscaler_enabled=False,
        )

    def test_cpu_driven_recommendation_uses_cpu_shortfall(self) -> None:
        snapshot = self._small_snapshot(total=1000.0, node_count=100)
        assert _recommend_additional_nodes(818.0, 0.0, snapshot) == 2  # noqa: PLR2004

    def test_memory_driven_recommendation_uses_memory_shortfall(self) -> None:
        snapshot = self._small_snapshot(total=1000.0, node_count=100)
        assert _recommend_additional_nodes(0.0, 818.0, snapshot) == 2  # noqa: PLR2004

    def test_single_node_recommendation_cpu(self) -> None:
        snapshot = self._small_snapshot(total=10.0, node_count=1)
        assert _recommend_additional_nodes(28.0, 0.0, snapshot) == 2  # noqa: PLR2004

    def test_single_node_recommendation_memory(self) -> None:
        snapshot = self._small_snapshot(total=10.0, node_count=1)
        assert _recommend_additional_nodes(0.0, 28.0, snapshot) == 2  # noqa: PLR2004

    def test_sub_one_average_node_size_recommendation_cpu(self) -> None:
        snapshot = self._small_snapshot(total=4.0, node_count=10)
        assert _recommend_additional_nodes(4.0, 0.0, snapshot) == 2  # noqa: PLR2004

    def test_sub_one_average_node_size_recommendation_memory(self) -> None:
        snapshot = self._small_snapshot(total=4.0, node_count=10)
        assert _recommend_additional_nodes(0.0, 4.0, snapshot) == 2  # noqa: PLR2004

    def test_memory_ceil_uses_division_not_multiplication(self) -> None:
        snapshot = self._small_snapshot(total=400.0, node_count=100)
        assert _recommend_additional_nodes(0.0, 328.0, snapshot) == 2  # noqa: PLR2004

    def test_memory_ceil_uses_shortfall_not_sum(self) -> None:
        snapshot = self._small_snapshot(total=400.0, node_count=1600)
        assert _recommend_additional_nodes(0.0, 322.0, snapshot) == 8  # noqa: PLR2004


class TestBuildSummaryStrings:
    def test_no_workloads_exact_string(self) -> None:
        result = _build_summary(
            has_workloads=False,
            verdict="fits",
            binding_constraint="None",
            post_cpu_pct=50.0,
            post_memory_pct=50.0,
            recommended_nodes=0,
            autoscaler_enabled=False,
            unschedulable=[],
        )
        assert result == "No new workloads proposed — current headroom shown."

    def test_fits_exact_string(self) -> None:
        result = _build_summary(
            has_workloads=True,
            verdict="fits",
            binding_constraint="CPU",
            post_cpu_pct=51.5,
            post_memory_pct=50.0,
            recommended_nodes=0,
            autoscaler_enabled=False,
            unschedulable=[],
        )
        assert result == "Fits comfortably within current cluster capacity."

    def test_needs_nodes_exact_string(self) -> None:
        result = _build_summary(
            has_workloads=True,
            verdict="needs_nodes",
            binding_constraint="CPU",
            post_cpu_pct=97.5,
            post_memory_pct=10.0,
            recommended_nodes=2,
            autoscaler_enabled=False,
            unschedulable=[],
        )
        assert result == (
            "Needs nodes — projected utilization would reach 97.5%. "
            "Recommend adding 2 node(s). CPU is the binding constraint."
        )

    def test_tight_exact_string(self) -> None:
        result = _build_summary(
            has_workloads=True,
            verdict="tight",
            binding_constraint="Memory",
            post_cpu_pct=40.0,
            post_memory_pct=83.3,
            recommended_nodes=0,
            autoscaler_enabled=False,
            unschedulable=[],
        )
        assert result == (
            "Tight — projected utilization would reach 83.3%. Monitor closely. "
            "Memory is the binding constraint."
        )

    def test_unschedulable_exact_string(self) -> None:
        result = _build_summary(
            has_workloads=True,
            verdict="needs_nodes",
            binding_constraint="None",
            post_cpu_pct=40.0,
            post_memory_pct=10.0,
            recommended_nodes=0,
            autoscaler_enabled=False,
            unschedulable=["huge-service"],
        )
        assert result == (
            "Unschedulable: huge-service — request(s) exceed the largest available node; "
            "a larger node type is needed, not just more of the current size."
        )

    def test_autoscaler_appended_exactly(self) -> None:
        result = _build_summary(
            has_workloads=True,
            verdict="fits",
            binding_constraint="CPU",
            post_cpu_pct=51.5,
            post_memory_pct=50.0,
            recommended_nodes=0,
            autoscaler_enabled=True,
            unschedulable=[],
        )
        assert result == (
            "Fits comfortably within current cluster capacity. "
            "Cluster autoscaler is enabled as a safety net."
        )

    def test_no_binding_constraint_appended_when_verdict_fits(self) -> None:
        result = _build_summary(
            has_workloads=True,
            verdict="fits",
            binding_constraint="CPU",
            post_cpu_pct=51.5,
            post_memory_pct=50.0,
            recommended_nodes=0,
            autoscaler_enabled=False,
            unschedulable=[],
        )
        assert "binding constraint" not in result


class TestExactReportPayload:
    def test_full_report_matches_expected_payload(self) -> None:
        snapshot = _snapshot()
        request = HeadroomSimulationRequest(
            proposed_workloads=[_workload("750m", "256Mi", replicas=2, name="svc")]
        )

        report = simulate_headroom(request, snapshot)

        assert report == HeadroomSimulationReport(
            current_cpu_utilization_percent=60.0,
            current_memory_utilization_percent=60.0,
            total_new_cpu_cores=1.5,
            total_new_memory_gb=0.5,
            post_cpu_utilization_percent=61.88,
            post_memory_utilization_percent=60.16,
            binding_constraint="CPU",
            verdict="fits",
            recommended_additional_nodes=0,
            autoscaler_enabled=False,
            unschedulable_workloads=[],
            summary="Fits comfortably within current cluster capacity.",
        )

    def test_report_rounds_percent_to_two_decimals(self) -> None:
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=7.0,
            total_allocatable_memory_gb=7.0,
            used_cpu_cores=3.0,
            used_memory_gb=3.0,
            node_count=2,
            largest_node_cpu_cores=7.0,
            largest_node_memory_gb=7.0,
            autoscaler_enabled=False,
        )
        request = HeadroomSimulationRequest(
            proposed_workloads=[_workload("1", "1Gi", replicas=1, name="a")]
        )

        report = simulate_headroom(request, snapshot)

        assert report.current_cpu_utilization_percent == 42.86  # noqa: PLR2004
        assert report.current_memory_utilization_percent == 42.86  # noqa: PLR2004
        assert report.post_cpu_utilization_percent == 57.14  # noqa: PLR2004
        assert report.post_memory_utilization_percent == 57.14  # noqa: PLR2004

    def test_report_with_needs_nodes_payload(self) -> None:
        snapshot = _snapshot(
            total_cpu=40.0, total_memory=200.0, used_cpu=36.0, used_memory=20.0, node_count=5
        )
        request = HeadroomSimulationRequest(
            proposed_workloads=[_workload("1500m", "256Mi", replicas=2, name="svc")]
        )

        report = simulate_headroom(request, snapshot)

        assert report == HeadroomSimulationReport(
            current_cpu_utilization_percent=90.0,
            current_memory_utilization_percent=10.0,
            total_new_cpu_cores=3.0,
            total_new_memory_gb=0.5,
            post_cpu_utilization_percent=97.5,
            post_memory_utilization_percent=10.25,
            binding_constraint="CPU",
            verdict="needs_nodes",
            recommended_additional_nodes=1,
            autoscaler_enabled=False,
            unschedulable_workloads=[],
            summary=(
                "Needs nodes — projected utilization would reach 97.5%. "
                "Recommend adding 1 node(s). CPU is the binding constraint."
            ),
        )

    def test_report_no_workloads_payload(self) -> None:
        report = simulate_headroom(HeadroomSimulationRequest(), _snapshot())

        assert report == HeadroomSimulationReport(
            current_cpu_utilization_percent=60.0,
            current_memory_utilization_percent=60.0,
            total_new_cpu_cores=0.0,
            total_new_memory_gb=0.0,
            post_cpu_utilization_percent=60.0,
            post_memory_utilization_percent=60.0,
            binding_constraint="None",
            verdict="fits",
            recommended_additional_nodes=0,
            autoscaler_enabled=False,
            unschedulable_workloads=[],
            summary="No new workloads proposed — current headroom shown.",
        )

    def test_multiple_unschedulable_workloads_summary_payload(self) -> None:
        snapshot = _snapshot(
            total_cpu=40.0,
            total_memory=200.0,
            used_cpu=10.0,
            used_memory=10.0,
            node_count=5,
            largest_node_cpu=8.0,
            largest_node_memory=32.0,
            autoscaler_enabled=True,
        )
        request = HeadroomSimulationRequest(
            proposed_workloads=[
                _workload("16", "1Gi", replicas=1, name="alpha"),
                _workload("12", "1Gi", replicas=1, name="beta"),
            ]
        )

        report = simulate_headroom(request, snapshot)

        assert report.verdict == "needs_nodes"
        assert report.unschedulable_workloads == ["alpha", "beta"]
        assert report.summary == (
            "Unschedulable: alpha, beta — request(s) exceed the largest available node; "
            "a larger node type is needed, not just more of the current size. "
            "CPU is the binding constraint. Cluster autoscaler is enabled as a safety net."
        )
