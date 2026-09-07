from __future__ import annotations

from hexawyn.application.ports.driven.spike_provisioning_port import ClusterCapacityRaw
from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_to_snapshot__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_snapshot__mutmut)
def to_snapshot(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_orig(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_1(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=None,
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_2(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=None,
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_3(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=None,
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_4(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=None,
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_5(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=None,
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_6(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=None,
    )


def x_to_snapshot__mutmut_7(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_8(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_9(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_10(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_11(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_12(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        )


def x_to_snapshot__mutmut_13(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["XXnode_countXX"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_14(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["NODE_COUNT"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_15(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["XXallocatable_cpu_coresXX"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_16(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["ALLOCATABLE_CPU_CORES"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_17(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["XXallocatable_memory_gbXX"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_18(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["ALLOCATABLE_MEMORY_GB"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_19(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["XXused_cpu_coresXX"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_20(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["USED_CPU_CORES"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_21(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["XXused_memory_gbXX"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_22(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["USED_MEMORY_GB"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x_to_snapshot__mutmut_23(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["XXautoscaler_enabledXX"],
    )


def x_to_snapshot__mutmut_24(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["AUTOSCALER_ENABLED"],
    )

mutants_x_to_snapshot__mutmut['_mutmut_orig'] = x_to_snapshot__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_1'] = x_to_snapshot__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_2'] = x_to_snapshot__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_3'] = x_to_snapshot__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_4'] = x_to_snapshot__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_5'] = x_to_snapshot__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_6'] = x_to_snapshot__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_7'] = x_to_snapshot__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_8'] = x_to_snapshot__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_9'] = x_to_snapshot__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_10'] = x_to_snapshot__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_11'] = x_to_snapshot__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_12'] = x_to_snapshot__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_13'] = x_to_snapshot__mutmut_13 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_14'] = x_to_snapshot__mutmut_14 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_15'] = x_to_snapshot__mutmut_15 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_16'] = x_to_snapshot__mutmut_16 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_17'] = x_to_snapshot__mutmut_17 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_18'] = x_to_snapshot__mutmut_18 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_19'] = x_to_snapshot__mutmut_19 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_20'] = x_to_snapshot__mutmut_20 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_21'] = x_to_snapshot__mutmut_21 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_22'] = x_to_snapshot__mutmut_22 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_23'] = x_to_snapshot__mutmut_23 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_24'] = x_to_snapshot__mutmut_24 # type: ignore # mutmut generated
