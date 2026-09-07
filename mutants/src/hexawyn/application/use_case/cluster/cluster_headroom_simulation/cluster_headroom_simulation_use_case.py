from __future__ import annotations

from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)
from hexawyn.application.ports.driven.headroom_simulation_port import HeadroomSimulationPort
from hexawyn.application.use_case.cluster.cluster_headroom_simulation.command import (
    ClusterHeadroomSimulationCommand,
    ProposedWorkloadDict,
)
from hexawyn.application.use_case.cluster.cluster_headroom_simulation.response import (
    ClusterHeadroomSimulationResponse,
)
from hexawyn.domain.models.headroom_simulation import (
    ClusterHeadroomSnapshot,
    HeadroomSimulationReport,
    HeadroomSimulationRequest,
    ProposedWorkload,
)
from hexawyn.domain.services.headroom_simulation.headroom_builder import simulate_headroom

_QUERY_TIMEOUT_SECONDS = 15.0
_DEFAULT_REPLICAS = 2


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut: MutantDict = {}  # type: ignore


class ClusterHeadroomSimulationUseCase:
    @_mutmut_mutated(mutants_xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut)
    def __init__(
        self, metrics_port: ClusterResourceMetricsPort, headroom_port: HeadroomSimulationPort
    ) -> None:
        self._metrics_port = metrics_port
        self._headroom_port = headroom_port
    def xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut_orig(
        self, metrics_port: ClusterResourceMetricsPort, headroom_port: HeadroomSimulationPort
    ) -> None:
        self._metrics_port = metrics_port
        self._headroom_port = headroom_port
    def xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut_1(
        self, metrics_port: ClusterResourceMetricsPort, headroom_port: HeadroomSimulationPort
    ) -> None:
        self._metrics_port = None
        self._headroom_port = headroom_port
    def xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut_2(
        self, metrics_port: ClusterResourceMetricsPort, headroom_port: HeadroomSimulationPort
    ) -> None:
        self._metrics_port = metrics_port
        self._headroom_port = None

    @_mutmut_mutated(mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut)
    def simulate(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_orig(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_1(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = None
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_2(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=None)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_3(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = None
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_4(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["XXcpu_coresXX"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_5(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["CPU_CORES"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_6(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = None

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_7(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["XXmemory_gbXX"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_8(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["MEMORY_GB"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_9(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = None
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_10(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = None

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_11(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=None,
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_12(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=None,
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_13(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=None,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_14(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=None,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_15(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=None,
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_16(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=None,
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_17(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=None,
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_18(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=None,
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_19(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_20(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_21(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_22(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_23(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_24(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_25(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_26(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_27(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["XXtotal_allocatable_cpu_coresXX"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_28(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["TOTAL_ALLOCATABLE_CPU_CORES"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_29(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["XXtotal_allocatable_memory_gbXX"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_30(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["TOTAL_ALLOCATABLE_MEMORY_GB"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_31(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["XXnode_countXX"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_32(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["NODE_COUNT"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_33(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["XXlargest_node_cpu_coresXX"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_34(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["LARGEST_NODE_CPU_CORES"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_35(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["XXlargest_node_memory_gbXX"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_36(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["LARGEST_NODE_MEMORY_GB"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_37(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["XXautoscaler_enabledXX"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_38(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["AUTOSCALER_ENABLED"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_39(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = None
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_40(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(None) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_41(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = None
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_42(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            None, snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_43(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), None
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_44(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_45(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_46(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=None), snapshot
        )
        return _to_response(report)

    def xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_47(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        current_usage = self._metrics_port.get_current_usage(timeout_seconds=_QUERY_TIMEOUT_SECONDS)
        used_cpu = current_usage["cpu_cores"]
        used_memory = current_usage["memory_gb"]

        capacity_info = self._headroom_port.get_node_capacity_info()
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            used_cpu_cores=used_cpu,
            used_memory_gb=used_memory,
            node_count=capacity_info["node_count"],
            largest_node_cpu_cores=capacity_info["largest_node_cpu_cores"],
            largest_node_memory_gb=capacity_info["largest_node_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        workloads = [_to_proposed_workload(raw) for raw in command.proposed_workloads]
        report = simulate_headroom(
            HeadroomSimulationRequest(proposed_workloads=workloads), snapshot
        )
        return _to_response(None)

mutants_xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut['_mutmut_orig'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut['xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut_1'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut['xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut_2'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['_mutmut_orig'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_1'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_2'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_3'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_4'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_5'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_6'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_7'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_8'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_9'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_10'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_11'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_12'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_13'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_14'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_15'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_16'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_17'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_18'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_19'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_20'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_21'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_22'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_23'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_24'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_25'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_26'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_27'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_28'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_29'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_30'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_31'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_32'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_33'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_34'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_34 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_35'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_35 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_36'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_36 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_37'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_37 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_38'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_38 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_39'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_39 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_40'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_40 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_41'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_41 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_42'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_42 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_43'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_43 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_44'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_44 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_45'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_45 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_46'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_46 # type: ignore # mutmut generated
mutants_xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut['xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_47'] = ClusterHeadroomSimulationUseCase.xǁClusterHeadroomSimulationUseCaseǁsimulate__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_proposed_workload__mutmut)
def _to_proposed_workload(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_orig(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_1(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=None,
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_2(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=None,
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_3(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=None,
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_4(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=None,
    )


def x__to_proposed_workload__mutmut_5(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_6(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_7(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_8(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        )


def x__to_proposed_workload__mutmut_9(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["XXnameXX"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_10(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["NAME"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_11(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["XXcpu_request_per_podXX"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_12(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["CPU_REQUEST_PER_POD"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_13(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["XXmemory_request_per_podXX"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_14(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["MEMORY_REQUEST_PER_POD"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_15(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get(None, _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_16(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", None),
    )


def x__to_proposed_workload__mutmut_17(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get(_DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_18(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", ),
    )


def x__to_proposed_workload__mutmut_19(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("XXreplicasXX", _DEFAULT_REPLICAS),
    )


def x__to_proposed_workload__mutmut_20(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("REPLICAS", _DEFAULT_REPLICAS),
    )

mutants_x__to_proposed_workload__mutmut['_mutmut_orig'] = x__to_proposed_workload__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_1'] = x__to_proposed_workload__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_2'] = x__to_proposed_workload__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_3'] = x__to_proposed_workload__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_4'] = x__to_proposed_workload__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_5'] = x__to_proposed_workload__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_6'] = x__to_proposed_workload__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_7'] = x__to_proposed_workload__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_8'] = x__to_proposed_workload__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_9'] = x__to_proposed_workload__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_10'] = x__to_proposed_workload__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_11'] = x__to_proposed_workload__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_12'] = x__to_proposed_workload__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_13'] = x__to_proposed_workload__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_14'] = x__to_proposed_workload__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_15'] = x__to_proposed_workload__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_16'] = x__to_proposed_workload__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_17'] = x__to_proposed_workload__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_18'] = x__to_proposed_workload__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_19'] = x__to_proposed_workload__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_proposed_workload__mutmut['x__to_proposed_workload__mutmut_20'] = x__to_proposed_workload__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_orig(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_1(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=None,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_2(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=None,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_3(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=None,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_4(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=None,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_5(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=None,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_6(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=None,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_7(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=None,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_8(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=None,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_9(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=None,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_10(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=None,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_11(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=None,
        summary=report.summary,
    )


def x__to_response__mutmut_12(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=None,
    )


def x__to_response__mutmut_13(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_14(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_15(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_16(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_17(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_18(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_19(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_20(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_21(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_22(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        unschedulable_workloads=report.unschedulable_workloads,
        summary=report.summary,
    )


def x__to_response__mutmut_23(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        summary=report.summary,
    )


def x__to_response__mutmut_24(report: HeadroomSimulationReport) -> ClusterHeadroomSimulationResponse:
    return ClusterHeadroomSimulationResponse(
        current_cpu_utilization_percent=report.current_cpu_utilization_percent,
        current_memory_utilization_percent=report.current_memory_utilization_percent,
        total_new_cpu_cores=report.total_new_cpu_cores,
        total_new_memory_gb=report.total_new_memory_gb,
        post_cpu_utilization_percent=report.post_cpu_utilization_percent,
        post_memory_utilization_percent=report.post_memory_utilization_percent,
        binding_constraint=report.binding_constraint,
        verdict=report.verdict,
        recommended_additional_nodes=report.recommended_additional_nodes,
        autoscaler_enabled=report.autoscaler_enabled,
        unschedulable_workloads=report.unschedulable_workloads,
        )

mutants_x__to_response__mutmut['_mutmut_orig'] = x__to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_1'] = x__to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_2'] = x__to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_3'] = x__to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_4'] = x__to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_5'] = x__to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_6'] = x__to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_7'] = x__to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_8'] = x__to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_9'] = x__to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_10'] = x__to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_11'] = x__to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_12'] = x__to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_13'] = x__to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_14'] = x__to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_15'] = x__to_response__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_16'] = x__to_response__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_17'] = x__to_response__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_18'] = x__to_response__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_19'] = x__to_response__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_20'] = x__to_response__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_21'] = x__to_response__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_22'] = x__to_response__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_23'] = x__to_response__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_24'] = x__to_response__mutmut_24 # type: ignore # mutmut generated
