from __future__ import annotations

from hexawyn.application.ports.driven.spike_provisioning_port import ClusterCapacityRaw
from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot


def to_snapshot(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )
