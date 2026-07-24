from __future__ import annotations

from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)
from hexawyn.application.ports.driven.headroom_simulation_port import HeadroomSimulationPort
from hexawyn.application.use_case.cluster_headroom_simulation.command import (
    ClusterHeadroomSimulationCommand,
    ProposedWorkloadDict,
)
from hexawyn.application.use_case.cluster_headroom_simulation.response import (
    ClusterHeadroomSimulationResponse,
)
from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_service_port import (
    ClusterHeadroomSimulationServicePort,
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


class ClusterHeadroomSimulationService(ClusterHeadroomSimulationServicePort):
    def __init__(
        self, metrics_port: ClusterResourceMetricsPort, headroom_port: HeadroomSimulationPort
    ) -> None:
        self._metrics_port = metrics_port
        self._headroom_port = headroom_port

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


def _to_proposed_workload(raw: ProposedWorkloadDict) -> ProposedWorkload:
    return ProposedWorkload(
        name=raw["name"],
        cpu_request_per_pod=raw["cpu_request_per_pod"],
        memory_request_per_pod=raw["memory_request_per_pod"],
        replicas=raw.get("replicas", _DEFAULT_REPLICAS),
    )


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
