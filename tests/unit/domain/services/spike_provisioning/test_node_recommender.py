from __future__ import annotations

from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot
from hexawyn.domain.services.spike_provisioning.node_recommender import (
    NodeRecommendation,
    _nodes_for_constraint,
    recommend_nodes,
)


def _snapshot(
    node_count: int = 10,
    alloc_cpu: float = 100.0,
    alloc_mem: float = 200.0,
    used_cpu: float = 70.0,
    used_mem: float = 130.0,
) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=node_count,
        allocatable_cpu_cores=alloc_cpu,
        allocatable_memory_gb=alloc_mem,
        used_cpu_cores=used_cpu,
        used_memory_gb=used_mem,
        autoscaler_enabled=False,
    )


class TestNodeCount:
    def test_no_nodes_needed_when_within_threshold(self) -> None:
        from hexawyn.domain.services.spike_provisioning.node_recommender import recommend_nodes

        result = recommend_nodes(
            _snapshot(), multiplier=1.0, binding_constraint="None", safe_threshold_pct=85.0
        )

        assert result.node_count == 0

    def test_recommends_nodes_to_return_under_threshold(self) -> None:
        from hexawyn.domain.services.spike_provisioning.node_recommender import recommend_nodes

        # 10 nodes, 70% CPU used → 3x demand = 210 cores needed vs 100 allocatable.
        result = recommend_nodes(
            _snapshot(used_cpu=70.0),
            multiplier=3.0,
            binding_constraint="CPU",
            safe_threshold_pct=85.0,
        )

        assert result.node_count >= 1

    def test_more_nodes_for_higher_multiplier(self) -> None:
        from hexawyn.domain.services.spike_provisioning.node_recommender import recommend_nodes

        low = recommend_nodes(
            _snapshot(), multiplier=2.0, binding_constraint="CPU", safe_threshold_pct=85.0
        )
        high = recommend_nodes(
            _snapshot(), multiplier=4.0, binding_constraint="CPU", safe_threshold_pct=85.0
        )

        assert high.node_count > low.node_count


class TestNodeType:
    def test_cpu_bound_recommends_compute_optimized(self) -> None:
        from hexawyn.domain.services.spike_provisioning.node_recommender import recommend_nodes

        result = recommend_nodes(
            _snapshot(), multiplier=3.0, binding_constraint="CPU", safe_threshold_pct=85.0
        )

        assert result.node_type == "compute_optimized"

    def test_memory_bound_recommends_memory_optimized(self) -> None:
        from hexawyn.domain.services.spike_provisioning.node_recommender import recommend_nodes

        result = recommend_nodes(
            _snapshot(), multiplier=3.0, binding_constraint="Memory", safe_threshold_pct=85.0
        )

        assert result.node_type == "memory_optimized"

    def test_no_constraint_recommends_balanced(self) -> None:
        from hexawyn.domain.services.spike_provisioning.node_recommender import recommend_nodes

        result = recommend_nodes(
            _snapshot(), multiplier=1.0, binding_constraint="None", safe_threshold_pct=85.0
        )

        assert result.node_type == "balanced"


class TestEdgeCases:
    def test_memory_bound_computes_from_memory(self) -> None:
        from hexawyn.domain.services.spike_provisioning.node_recommender import recommend_nodes

        result = recommend_nodes(
            _snapshot(used_mem=130.0),
            multiplier=3.0,
            binding_constraint="Memory",
            safe_threshold_pct=85.0,
        )

        assert result.node_count >= 1
        assert result.node_type == "memory_optimized"

    def test_zero_allocatable_recommends_no_nodes(self) -> None:
        from hexawyn.domain.services.spike_provisioning.node_recommender import recommend_nodes

        snapshot = ClusterCapacitySnapshot(
            node_count=0,
            allocatable_cpu_cores=0.0,
            allocatable_memory_gb=0.0,
            used_cpu_cores=0.0,
            used_memory_gb=0.0,
            autoscaler_enabled=False,
        )

        result = recommend_nodes(
            snapshot, multiplier=3.0, binding_constraint="CPU", safe_threshold_pct=85.0
        )

        assert result.node_count == 0

    def test_already_within_threshold_needs_no_nodes(self) -> None:
        from hexawyn.domain.services.spike_provisioning.node_recommender import recommend_nodes

        result = recommend_nodes(
            _snapshot(used_cpu=10.0),
            multiplier=1.5,
            binding_constraint="CPU",
            safe_threshold_pct=85.0,
        )

        assert result.node_count == 0


class TestTestDataScenario:
    def test_ticket_scenario_three_nodes(self) -> None:
        from hexawyn.domain.services.spike_provisioning.node_recommender import recommend_nodes

        # 10 nodes @70% CPU, 2.8x spike → CPU projected 196% → needs extra nodes.
        result = recommend_nodes(
            _snapshot(used_cpu=70.0),
            multiplier=2.8,
            binding_constraint="CPU",
            safe_threshold_pct=85.0,
        )

        assert result.node_count >= 3  # noqa: PLR2004
        assert result.node_type == "compute_optimized"


class TestExactNodeRecommendation:
    def test_exact_node_count_three_x_cpu(self) -> None:
        result = recommend_nodes(
            _snapshot(used_cpu=70.0),
            multiplier=3.0,
            binding_constraint="CPU",
            safe_threshold_pct=85.0,
        )

        assert result == NodeRecommendation(node_count=15, node_type="compute_optimized")

    def test_safe_fraction_threshold_sensitivity(self) -> None:
        result = _nodes_for_constraint(_snapshot(node_count=5, used_cpu=85.0), 1.2, "CPU", 85.0)
        assert result == 1

    def test_single_node_cluster_recommends_one(self) -> None:
        result = _nodes_for_constraint(
            _snapshot(node_count=1, alloc_cpu=10.0, used_cpu=9.0), 1.0, "CPU", 85.0
        )
        assert result == 1

    def test_allocatable_between_zero_and_one(self) -> None:
        snapshot = _snapshot(node_count=2, alloc_cpu=0.5, alloc_mem=0.5, used_cpu=0.4, used_mem=0.4)
        result = recommend_nodes(
            snapshot, multiplier=2.0, binding_constraint="CPU", safe_threshold_pct=85.0
        )
        assert result == NodeRecommendation(node_count=2, node_type="compute_optimized")

    def test_allocatable_equals_one(self) -> None:
        snapshot = _snapshot(node_count=1, alloc_cpu=1.0, alloc_mem=1.0, used_cpu=0.9, used_mem=0.9)
        result = recommend_nodes(
            snapshot, multiplier=2.0, binding_constraint="CPU", safe_threshold_pct=85.0
        )
        assert result == NodeRecommendation(node_count=2, node_type="compute_optimized")

    def test_zero_allocatable_with_nodes_returns_zero(self) -> None:
        assert _nodes_for_constraint(_snapshot(node_count=5, alloc_cpu=0.0), 3.0, "CPU", 85.0) == 0

    def test_zero_nodes_with_allocatable_returns_zero(self) -> None:
        assert (
            _nodes_for_constraint(_snapshot(node_count=0, alloc_cpu=100.0), 3.0, "CPU", 85.0) == 0
        )

    def test_memory_exact_node_count(self) -> None:
        result = _nodes_for_constraint(
            _snapshot(node_count=10, used_mem=130.0), 3.0, "Memory", 85.0
        )
        assert result == 13  # noqa: PLR2004


class TestUnknownBindingConstraint:
    def test_unknown_binding_falls_back_to_balanced_type(self) -> None:
        result = recommend_nodes(
            _snapshot(), multiplier=2.0, binding_constraint="GPU", safe_threshold_pct=85.0
        )

        assert result == NodeRecommendation(node_count=6, node_type="balanced")

    def test_none_binding_with_spike_stays_zero(self) -> None:
        result = recommend_nodes(
            _snapshot(), multiplier=2.0, binding_constraint="None", safe_threshold_pct=85.0
        )

        assert result == NodeRecommendation(node_count=0, node_type="balanced")
