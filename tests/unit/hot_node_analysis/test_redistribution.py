"""Unit tests for find_redistribution_target — greedy partial-fit
redistribution feasibility."""

from __future__ import annotations

from hexawyn.domain.models.hot_node_analysis import ClusterNodeSnapshot, TopConsumer
from hexawyn.domain.services.hot_node_analysis.redistribution import find_redistribution_target


def _consumer(name: str, cpu: float) -> TopConsumer:
    return TopConsumer(
        pod_name=name, namespace="production", cpu_usage_cores=cpu, memory_usage_gb=1.0
    )


def _node(name: str, allocatable_cpu: float, used_cpu: float = 0.0) -> ClusterNodeSnapshot:
    pods = [_consumer(f"{name}-existing", used_cpu)] if used_cpu else []
    return ClusterNodeSnapshot(
        node_name=name,
        cordoned=False,
        allocatable_cpu_cores=allocatable_cpu,
        allocatable_memory_gb=64.0,
        pods=pods,
    )


class TestFindRedistributionTarget:
    def test_tc2_partial_fit_two_of_three_pods(self) -> None:
        """TC2: worker-1 has 3 large pods, worker-3 has capacity for 2 of
        them → redistribute recommended."""
        top_consumers = [_consumer("pod-a", 1.0), _consumer("pod-b", 1.0), _consumer("pod-c", 1.0)]
        candidates = [_node("worker-3", allocatable_cpu=10.0, used_cpu=8.0)]  # 2.0 headroom

        result = find_redistribution_target(top_consumers, candidates)

        assert result.feasible is True
        assert result.target_node == "worker-3"
        assert result.moved_pod_count == 2

    def test_tc3_no_candidates_is_infeasible(self) -> None:
        """TC3: all nodes above 80% → no candidate targets remain → infeasible."""
        top_consumers = [_consumer("pod-a", 1.0)]

        result = find_redistribution_target(top_consumers, [])

        assert result.feasible is False
        assert result.target_node is None
        assert result.moved_pod_count == 0

    def test_candidate_with_insufficient_headroom_moves_nothing(self) -> None:
        top_consumers = [_consumer("huge-pod", 5.0)]
        candidates = [_node("worker-3", allocatable_cpu=10.0, used_cpu=9.0)]  # 1.0 headroom

        result = find_redistribution_target(top_consumers, candidates)

        assert result.feasible is False
        assert result.moved_pod_count == 0

    def test_selects_candidate_with_most_headroom(self) -> None:
        top_consumers = [_consumer("pod-a", 1.0), _consumer("pod-b", 1.0)]
        candidates = [
            _node("worker-low-headroom", allocatable_cpu=10.0, used_cpu=9.0),  # 1.0 headroom
            _node("worker-high-headroom", allocatable_cpu=10.0, used_cpu=2.0),  # 8.0 headroom
        ]

        result = find_redistribution_target(top_consumers, candidates)

        assert result.target_node == "worker-high-headroom"
        assert result.moved_pod_count == 2

    def test_no_top_consumers_is_infeasible(self) -> None:
        result = find_redistribution_target([], [_node("worker-3", allocatable_cpu=10.0)])

        assert result.feasible is False
