from __future__ import annotations

from hexawyn.application.ports.driven.headroom_simulation_port import (
    HeadroomSimulationPort,
)
from hexawyn.application.ports.driven.spike_provisioning_port import (
    ClusterCapacityRaw,
    SpikeProvisioningPort,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSpikeProvisioningAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut: MutantDict = {}  # type: ignore


class SpikeProvisioningAdapter(SpikeProvisioningPort):
    """Provides cluster capacity for spike planning.

    Reuses the headroom port for allocatable capacity, node count and
    autoscaler presence, combined with the current used CPU/memory (from the
    cluster metrics source). The historical spike multiplier is optional and
    injected from the memory layer when available.
    """

    @_mutmut_mutated(mutants_xǁSpikeProvisioningAdapterǁ__init____mutmut)
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

    def xǁSpikeProvisioningAdapterǁ__init____mutmut_orig(
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

    def xǁSpikeProvisioningAdapterǁ__init____mutmut_1(
        self,
        headroom_port: HeadroomSimulationPort,
        current_cpu_used_cores: float,
        current_memory_used_gb: float,
        historical_multiplier: float | None = None,
    ) -> None:
        self._headroom_port = None
        self._current_cpu_used_cores = current_cpu_used_cores
        self._current_memory_used_gb = current_memory_used_gb
        self._historical_multiplier = historical_multiplier

    def xǁSpikeProvisioningAdapterǁ__init____mutmut_2(
        self,
        headroom_port: HeadroomSimulationPort,
        current_cpu_used_cores: float,
        current_memory_used_gb: float,
        historical_multiplier: float | None = None,
    ) -> None:
        self._headroom_port = headroom_port
        self._current_cpu_used_cores = None
        self._current_memory_used_gb = current_memory_used_gb
        self._historical_multiplier = historical_multiplier

    def xǁSpikeProvisioningAdapterǁ__init____mutmut_3(
        self,
        headroom_port: HeadroomSimulationPort,
        current_cpu_used_cores: float,
        current_memory_used_gb: float,
        historical_multiplier: float | None = None,
    ) -> None:
        self._headroom_port = headroom_port
        self._current_cpu_used_cores = current_cpu_used_cores
        self._current_memory_used_gb = None
        self._historical_multiplier = historical_multiplier

    def xǁSpikeProvisioningAdapterǁ__init____mutmut_4(
        self,
        headroom_port: HeadroomSimulationPort,
        current_cpu_used_cores: float,
        current_memory_used_gb: float,
        historical_multiplier: float | None = None,
    ) -> None:
        self._headroom_port = headroom_port
        self._current_cpu_used_cores = current_cpu_used_cores
        self._current_memory_used_gb = current_memory_used_gb
        self._historical_multiplier = None

    @_mutmut_mutated(mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut)
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

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_orig(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_1(self) -> ClusterCapacityRaw:
        info = None
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_2(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=None,
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_3(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=None,
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_4(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=None,
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_5(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=None,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_6(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=None,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_7(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=None,
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_8(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_9(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_10(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_11(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_12(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_13(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_14(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["XXnode_countXX"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_15(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["NODE_COUNT"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_16(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["XXtotal_allocatable_cpu_coresXX"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_17(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["TOTAL_ALLOCATABLE_CPU_CORES"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_18(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["XXtotal_allocatable_memory_gbXX"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_19(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["TOTAL_ALLOCATABLE_MEMORY_GB"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["autoscaler_enabled"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_20(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["XXautoscaler_enabledXX"],
        )

    def xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_21(self) -> ClusterCapacityRaw:
        info = self._headroom_port.get_node_capacity_info()
        return ClusterCapacityRaw(
            node_count=info["node_count"],
            allocatable_cpu_cores=info["total_allocatable_cpu_cores"],
            allocatable_memory_gb=info["total_allocatable_memory_gb"],
            used_cpu_cores=self._current_cpu_used_cores,
            used_memory_gb=self._current_memory_used_gb,
            autoscaler_enabled=info["AUTOSCALER_ENABLED"],
        )

    def get_historical_spike_multiplier(self) -> float | None:
        return self._historical_multiplier

mutants_xǁSpikeProvisioningAdapterǁ__init____mutmut['_mutmut_orig'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁ__init____mutmut['xǁSpikeProvisioningAdapterǁ__init____mutmut_1'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁ__init____mutmut['xǁSpikeProvisioningAdapterǁ__init____mutmut_2'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁ__init____mutmut['xǁSpikeProvisioningAdapterǁ__init____mutmut_3'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁ__init____mutmut['xǁSpikeProvisioningAdapterǁ__init____mutmut_4'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['_mutmut_orig'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_1'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_2'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_3'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_4'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_5'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_6'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_7'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_8'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_9'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_10'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_11'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_12'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_13'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_14'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_15'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_16'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_17'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_18'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_19'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_20'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut['xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_21'] = SpikeProvisioningAdapter.xǁSpikeProvisioningAdapterǁget_cluster_capacity__mutmut_21 # type: ignore # mutmut generated
