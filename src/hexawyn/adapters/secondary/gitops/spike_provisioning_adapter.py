from __future__ import annotations

from hexawyn.application.ports.driven.headroom_simulation_port import (
    HeadroomSimulationPort,
)
from hexawyn.application.ports.driven.spike_provisioning_port import (
    ClusterCapacityRaw,
    SpikeProvisioningPort,
)


class SpikeProvisioningAdapter(SpikeProvisioningPort):
    """Provides cluster capacity for spike planning.

    Reuses the headroom port for allocatable capacity, node count and
    autoscaler presence, combined with the current used CPU/memory (from the
    cluster metrics source). The historical spike multiplier is optional and
    injected from the memory layer when available.
    """

    def __init__(
        self,
        headroom_port: HeadroomSimulationPort,
        current_cpu_used_cores: float,
        current_memory_used_gb: float,
        historical_multiplier: float | None = None,
    ) -> None:
        self._headroom_port = headroom_port
        self._current_cpu_used_cores = current_cpu_used_cores
        self._current_memory_used_gb = current_memory_used_gb
        self._historical_multiplier = historical_multiplier

    def get_cluster_capacity(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def get_historical_spike_multiplier(self) -> float | None:
        return self._historical_multiplier
