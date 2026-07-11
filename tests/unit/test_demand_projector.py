from __future__ import annotations

from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot


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

        assert result.projected_cpu_pct == 140.0
        assert result.projected_memory_pct == 130.0

    def test_current_headroom_computed(self) -> None:
        from hexawyn.domain.services.spike_provisioning.demand_projector import project_demand

        result = project_demand(_snapshot(used_cpu=70.0, used_mem=130.0), multiplier=1.0)

        assert result.current_cpu_headroom_pct == 30.0
        assert result.current_memory_headroom_pct == 35.0


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
