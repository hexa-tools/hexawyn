from __future__ import annotations

from hexawyn.domain.models.headroom_simulation import ProposedWorkload
from hexawyn.domain.services.headroom_simulation.quantity_parsing import (
    parse_cpu_quantity,
    parse_memory_quantity,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_total_workload_needs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_total_workload_needs__mutmut)
def compute_total_workload_needs(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = 0.0
    for workload in workloads:
        total_cpu += parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory += parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_orig(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = 0.0
    for workload in workloads:
        total_cpu += parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory += parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_1(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = None
    total_memory = 0.0
    for workload in workloads:
        total_cpu += parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory += parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_2(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 1.0
    total_memory = 0.0
    for workload in workloads:
        total_cpu += parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory += parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_3(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = None
    for workload in workloads:
        total_cpu += parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory += parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_4(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = 1.0
    for workload in workloads:
        total_cpu += parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory += parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_5(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = 0.0
    for workload in workloads:
        total_cpu = parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory += parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_6(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = 0.0
    for workload in workloads:
        total_cpu -= parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory += parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_7(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = 0.0
    for workload in workloads:
        total_cpu += parse_cpu_quantity(workload.cpu_request_per_pod) / workload.replicas
        total_memory += parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_8(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = 0.0
    for workload in workloads:
        total_cpu += parse_cpu_quantity(None) * workload.replicas
        total_memory += parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_9(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = 0.0
    for workload in workloads:
        total_cpu += parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory = parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_10(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = 0.0
    for workload in workloads:
        total_cpu += parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory -= parse_memory_quantity(workload.memory_request_per_pod) * workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_11(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = 0.0
    for workload in workloads:
        total_cpu += parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory += parse_memory_quantity(workload.memory_request_per_pod) / workload.replicas
    return total_cpu, total_memory


def x_compute_total_workload_needs__mutmut_12(workloads: list[ProposedWorkload]) -> tuple[float, float]:
    """Sums CPU cores and memory GB across all proposed workloads, each
    multiplied by its own replica count."""
    total_cpu = 0.0
    total_memory = 0.0
    for workload in workloads:
        total_cpu += parse_cpu_quantity(workload.cpu_request_per_pod) * workload.replicas
        total_memory += parse_memory_quantity(None) * workload.replicas
    return total_cpu, total_memory

mutants_x_compute_total_workload_needs__mutmut['_mutmut_orig'] = x_compute_total_workload_needs__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_total_workload_needs__mutmut['x_compute_total_workload_needs__mutmut_1'] = x_compute_total_workload_needs__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_total_workload_needs__mutmut['x_compute_total_workload_needs__mutmut_2'] = x_compute_total_workload_needs__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_total_workload_needs__mutmut['x_compute_total_workload_needs__mutmut_3'] = x_compute_total_workload_needs__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_total_workload_needs__mutmut['x_compute_total_workload_needs__mutmut_4'] = x_compute_total_workload_needs__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_total_workload_needs__mutmut['x_compute_total_workload_needs__mutmut_5'] = x_compute_total_workload_needs__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_total_workload_needs__mutmut['x_compute_total_workload_needs__mutmut_6'] = x_compute_total_workload_needs__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_total_workload_needs__mutmut['x_compute_total_workload_needs__mutmut_7'] = x_compute_total_workload_needs__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_total_workload_needs__mutmut['x_compute_total_workload_needs__mutmut_8'] = x_compute_total_workload_needs__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_total_workload_needs__mutmut['x_compute_total_workload_needs__mutmut_9'] = x_compute_total_workload_needs__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_total_workload_needs__mutmut['x_compute_total_workload_needs__mutmut_10'] = x_compute_total_workload_needs__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_total_workload_needs__mutmut['x_compute_total_workload_needs__mutmut_11'] = x_compute_total_workload_needs__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_total_workload_needs__mutmut['x_compute_total_workload_needs__mutmut_12'] = x_compute_total_workload_needs__mutmut_12 # type: ignore # mutmut generated
mutants_x_find_unschedulable_workloads__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_find_unschedulable_workloads__mutmut)
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


def x_find_unschedulable_workloads__mutmut_orig(
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


def x_find_unschedulable_workloads__mutmut_1(
    workloads: list[ProposedWorkload],
    largest_node_cpu_cores: float,
    largest_node_memory_gb: float,
) -> list[str]:
    """A single pod's request (not the workload's total across replicas)
    exceeding the largest node means it can never schedule, regardless of
    aggregate cluster headroom."""
    unschedulable: list[str] = None
    for workload in workloads:
        cpu_per_pod = parse_cpu_quantity(workload.cpu_request_per_pod)
        memory_per_pod = parse_memory_quantity(workload.memory_request_per_pod)
        if cpu_per_pod > largest_node_cpu_cores or memory_per_pod > largest_node_memory_gb:
            unschedulable.append(workload.name)
    return unschedulable


def x_find_unschedulable_workloads__mutmut_2(
    workloads: list[ProposedWorkload],
    largest_node_cpu_cores: float,
    largest_node_memory_gb: float,
) -> list[str]:
    """A single pod's request (not the workload's total across replicas)
    exceeding the largest node means it can never schedule, regardless of
    aggregate cluster headroom."""
    unschedulable: list[str] = []
    for workload in workloads:
        cpu_per_pod = None
        memory_per_pod = parse_memory_quantity(workload.memory_request_per_pod)
        if cpu_per_pod > largest_node_cpu_cores or memory_per_pod > largest_node_memory_gb:
            unschedulable.append(workload.name)
    return unschedulable


def x_find_unschedulable_workloads__mutmut_3(
    workloads: list[ProposedWorkload],
    largest_node_cpu_cores: float,
    largest_node_memory_gb: float,
) -> list[str]:
    """A single pod's request (not the workload's total across replicas)
    exceeding the largest node means it can never schedule, regardless of
    aggregate cluster headroom."""
    unschedulable: list[str] = []
    for workload in workloads:
        cpu_per_pod = parse_cpu_quantity(None)
        memory_per_pod = parse_memory_quantity(workload.memory_request_per_pod)
        if cpu_per_pod > largest_node_cpu_cores or memory_per_pod > largest_node_memory_gb:
            unschedulable.append(workload.name)
    return unschedulable


def x_find_unschedulable_workloads__mutmut_4(
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
        memory_per_pod = None
        if cpu_per_pod > largest_node_cpu_cores or memory_per_pod > largest_node_memory_gb:
            unschedulable.append(workload.name)
    return unschedulable


def x_find_unschedulable_workloads__mutmut_5(
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
        memory_per_pod = parse_memory_quantity(None)
        if cpu_per_pod > largest_node_cpu_cores or memory_per_pod > largest_node_memory_gb:
            unschedulable.append(workload.name)
    return unschedulable


def x_find_unschedulable_workloads__mutmut_6(
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
        if cpu_per_pod > largest_node_cpu_cores and memory_per_pod > largest_node_memory_gb:
            unschedulable.append(workload.name)
    return unschedulable


def x_find_unschedulable_workloads__mutmut_7(
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
        if cpu_per_pod >= largest_node_cpu_cores or memory_per_pod > largest_node_memory_gb:
            unschedulable.append(workload.name)
    return unschedulable


def x_find_unschedulable_workloads__mutmut_8(
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
        if cpu_per_pod > largest_node_cpu_cores or memory_per_pod >= largest_node_memory_gb:
            unschedulable.append(workload.name)
    return unschedulable


def x_find_unschedulable_workloads__mutmut_9(
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
            unschedulable.append(None)
    return unschedulable

mutants_x_find_unschedulable_workloads__mutmut['_mutmut_orig'] = x_find_unschedulable_workloads__mutmut_orig # type: ignore # mutmut generated
mutants_x_find_unschedulable_workloads__mutmut['x_find_unschedulable_workloads__mutmut_1'] = x_find_unschedulable_workloads__mutmut_1 # type: ignore # mutmut generated
mutants_x_find_unschedulable_workloads__mutmut['x_find_unschedulable_workloads__mutmut_2'] = x_find_unschedulable_workloads__mutmut_2 # type: ignore # mutmut generated
mutants_x_find_unschedulable_workloads__mutmut['x_find_unschedulable_workloads__mutmut_3'] = x_find_unschedulable_workloads__mutmut_3 # type: ignore # mutmut generated
mutants_x_find_unschedulable_workloads__mutmut['x_find_unschedulable_workloads__mutmut_4'] = x_find_unschedulable_workloads__mutmut_4 # type: ignore # mutmut generated
mutants_x_find_unschedulable_workloads__mutmut['x_find_unschedulable_workloads__mutmut_5'] = x_find_unschedulable_workloads__mutmut_5 # type: ignore # mutmut generated
mutants_x_find_unschedulable_workloads__mutmut['x_find_unschedulable_workloads__mutmut_6'] = x_find_unschedulable_workloads__mutmut_6 # type: ignore # mutmut generated
mutants_x_find_unschedulable_workloads__mutmut['x_find_unschedulable_workloads__mutmut_7'] = x_find_unschedulable_workloads__mutmut_7 # type: ignore # mutmut generated
mutants_x_find_unschedulable_workloads__mutmut['x_find_unschedulable_workloads__mutmut_8'] = x_find_unschedulable_workloads__mutmut_8 # type: ignore # mutmut generated
mutants_x_find_unschedulable_workloads__mutmut['x_find_unschedulable_workloads__mutmut_9'] = x_find_unschedulable_workloads__mutmut_9 # type: ignore # mutmut generated
