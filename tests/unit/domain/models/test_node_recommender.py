from __future__ import annotations

from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot


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

        assert result.node_count >= 3
        assert result.node_type == "compute_optimized"
