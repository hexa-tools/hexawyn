from __future__ import annotations

from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot
from hexawyn.domain.services.spike_provisioning.demand_projector import (
    DemandProjection,
    _binding_constraint,
    _utilization,
    project_demand,
)


def _snapshot(
    used_cpu: float = 70.0,
    used_mem: float = 130.0,
    alloc_cpu: float = 100.0,
    alloc_mem: float = 200.0,
) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=10,
        allocatable_cpu_cores=alloc_cpu,
        allocatable_memory_gb=alloc_mem,
        used_cpu_cores=used_cpu,
        used_memory_gb=used_mem,
        autoscaler_enabled=False,
    )


class TestProjection:
    def test_projects_cpu_and_memory_under_multiplier(self) -> None:
        from hexawyn.domain.services.spike_provisioning.demand_projector import project_demand

        result = project_demand(_snapshot(used_cpu=70.0, used_mem=130.0), multiplier=2.0)

        assert result.projected_cpu_pct == 140.0  # noqa: PLR2004
        assert result.projected_memory_pct == 130.0  # noqa: PLR2004

    def test_current_headroom_computed(self) -> None:
        from hexawyn.domain.services.spike_provisioning.demand_projector import project_demand

        result = project_demand(_snapshot(used_cpu=70.0, used_mem=130.0), multiplier=1.0)

        assert result.current_cpu_headroom_pct == 30.0  # noqa: PLR2004
        assert result.current_memory_headroom_pct == 35.0  # noqa: PLR2004


class TestBindingConstraint:
    def test_cpu_bound_when_cpu_higher(self) -> None:
        from hexawyn.domain.services.spike_provisioning.demand_projector import project_demand

        result = project_demand(_snapshot(used_cpu=80.0, used_mem=100.0), multiplier=2.0)

        assert result.binding_constraint == "CPU"

    def test_memory_bound_when_memory_higher(self) -> None:
        from hexawyn.domain.services.spike_provisioning.demand_projector import project_demand

        result = project_demand(_snapshot(used_cpu=40.0, used_mem=160.0), multiplier=2.0)

        assert result.binding_constraint == "Memory"

    def test_none_when_both_within_safe_threshold(self) -> None:
        from hexawyn.domain.services.spike_provisioning.demand_projector import project_demand

        result = project_demand(
            _snapshot(used_cpu=20.0, used_mem=40.0), multiplier=2.0, safe_threshold_pct=85.0
        )

        assert result.binding_constraint == "None"

    def test_zero_allocatable_is_safe_none(self) -> None:
        from hexawyn.domain.services.spike_provisioning.demand_projector import project_demand

        snapshot = ClusterCapacitySnapshot(
            node_count=0,
            allocatable_cpu_cores=0.0,
            allocatable_memory_gb=0.0,
            used_cpu_cores=0.0,
            used_memory_gb=0.0,
            autoscaler_enabled=False,
        )

        result = project_demand(snapshot, multiplier=3.0)

        assert result.projected_cpu_pct == 0.0
        assert result.binding_constraint == "None"


class TestExactProjectionPayload:
    def test_full_payload_matches_expected(self) -> None:
        snapshot = ClusterCapacitySnapshot(
            node_count=5,
            allocatable_cpu_cores=3.0,
            allocatable_memory_gb=3.0,
            used_cpu_cores=1.0,
            used_memory_gb=1.0,
            autoscaler_enabled=False,
        )

        result = project_demand(snapshot, multiplier=2.5)

        assert result == DemandProjection(
            current_cpu_headroom_pct=66.7,
            current_memory_headroom_pct=66.7,
            projected_cpu_pct=83.2,
            projected_memory_pct=83.2,
            binding_constraint="None",
        )

    def test_fractional_allocatable_utilization(self) -> None:
        assert _utilization(0.25, 0.5) == 50.0  # noqa: PLR2004


class TestBindingConstraintBoundaries:
    def test_exactly_at_threshold_is_not_over(self) -> None:
        snapshot = _snapshot(used_cpu=85.0, used_mem=85.0, alloc_cpu=100.0, alloc_mem=100.0)
        result = project_demand(snapshot, multiplier=1.0)
        assert result.binding_constraint == "None"

    def test_cpu_memory_tie_over_threshold_picks_cpu(self) -> None:
        assert _binding_constraint(90.0, 90.0, 85.0) == "CPU"

    def test_cpu_over_only_is_cpu(self) -> None:
        assert _binding_constraint(90.0, 80.0, 85.0) == "CPU"

    def test_memory_over_only_is_memory(self) -> None:
        assert _binding_constraint(80.0, 90.0, 85.0) == "Memory"

    def test_memory_higher_when_both_over_is_memory(self) -> None:
        assert _binding_constraint(86.0, 92.0, 85.0) == "Memory"

    def test_memory_at_threshold_boundary_with_cpu_under(self) -> None:
        snapshot = _snapshot(used_cpu=50.0, used_mem=85.0, alloc_cpu=100.0, alloc_mem=100.0)
        result = project_demand(snapshot, multiplier=1.0)
        assert result.projected_memory_pct == 85.0  # noqa: PLR2004
        assert result.binding_constraint == "None"


class TestUtilizationBoundaries:
    def test_allocatable_one_returns_utilization(self) -> None:
        assert _utilization(0.5, 1.0) == 50.0  # noqa: PLR2004

    def test_zero_allocatable_returns_zero(self) -> None:
        assert _utilization(5.0, 0.0) == 0.0
