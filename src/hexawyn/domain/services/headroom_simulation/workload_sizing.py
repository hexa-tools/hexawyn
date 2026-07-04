from __future__ import annotations

from hexawyn.domain.models.headroom_simulation import ProposedWorkload
from hexawyn.domain.services.headroom_simulation.quantity_parsing import (
    parse_cpu_quantity,
    parse_memory_quantity,
)


def compute_total_workload_needs(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = 0.0
    for workload in workloads:
        total_cpu += parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory += parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def find_unschedulable_workloads(
    workloads: list[ProposedWorkload],
    largest_node_cpu_cores: float,
    largest_node_memory_gb: float,
) -> list[str]:
    """A single pod's request (not the workload's total across replicas)
    exceeding the largest node means it can never schedule, regardless of
    aggregate cluster headroom."""
    unschedulable: list[str] = []
    for workload in workloads:
        cpu_per_pod = parse_cpu_quantity(workload.cpu_request_per_pod)
        memory_per_pod = parse_memory_quantity(workload.memory_request_per_pod)
        if cpu_per_pod > largest_node_cpu_cores or memory_per_pod > largest_node_memory_gb:
            unschedulable.append(workload.name)
    return unschedulable
