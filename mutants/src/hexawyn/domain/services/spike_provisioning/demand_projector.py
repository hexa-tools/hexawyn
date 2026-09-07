from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot

_DEFAULT_SAFE_THRESHOLD_PCT = 85.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class DemandProjection:
    current_cpu_headroom_pct: float
    current_memory_headroom_pct: float
    projected_cpu_pct: float
    projected_memory_pct: float
    binding_constraint: str
mutants_x_project_demand__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_project_demand__mutmut)
def project_demand(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_orig(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_1(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = None
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_2(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(None, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_3(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, None)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_4(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_5(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, )
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_6(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = None
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_7(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(None, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_8(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, None)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_9(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_10(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, )
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_11(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = None
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_12(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(None, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_13(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, None)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_14(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_15(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, )
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_16(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct / multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_17(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 2)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_18(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = None

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_19(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(None, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_20(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, None)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_21(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_22(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, )

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_23(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct / multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_24(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 2)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_25(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=None,
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_26(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=None,
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_27(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=None,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_28(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=None,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_29(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=None,
    )


def x_project_demand__mutmut_30(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_31(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_32(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_33(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_34(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        )


def x_project_demand__mutmut_35(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(None, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_36(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, None),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_37(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_38(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, ),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_39(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 + current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_40(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(101.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_41(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 2),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_42(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(None, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_43(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, None),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_44(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_45(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, ),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_46(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 + current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_47(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(101.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_48(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 2),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_49(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            None, projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_50(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, None, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_51(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, None
        ),
    )


def x_project_demand__mutmut_52(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_memory_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_53(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, safe_threshold_pct
        ),
    )


def x_project_demand__mutmut_54(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
) -> DemandProjection:
    """Project peak CPU/memory utilisation under a traffic multiplier.

    The binding constraint is whichever resource is projected furthest over the
    safe threshold; when neither exceeds it, nothing binds.
    """
    current_cpu_pct = _utilization(snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores)
    current_memory_pct = _utilization(snapshot.used_memory_gb, snapshot.allocatable_memory_gb)
    projected_cpu_pct = round(current_cpu_pct * multiplier, 1)
    projected_memory_pct = round(current_memory_pct * multiplier, 1)

    return DemandProjection(
        current_cpu_headroom_pct=round(100.0 - current_cpu_pct, 1),
        current_memory_headroom_pct=round(100.0 - current_memory_pct, 1),
        projected_cpu_pct=projected_cpu_pct,
        projected_memory_pct=projected_memory_pct,
        binding_constraint=_binding_constraint(
            projected_cpu_pct, projected_memory_pct, ),
    )

mutants_x_project_demand__mutmut['_mutmut_orig'] = x_project_demand__mutmut_orig # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_1'] = x_project_demand__mutmut_1 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_2'] = x_project_demand__mutmut_2 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_3'] = x_project_demand__mutmut_3 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_4'] = x_project_demand__mutmut_4 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_5'] = x_project_demand__mutmut_5 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_6'] = x_project_demand__mutmut_6 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_7'] = x_project_demand__mutmut_7 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_8'] = x_project_demand__mutmut_8 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_9'] = x_project_demand__mutmut_9 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_10'] = x_project_demand__mutmut_10 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_11'] = x_project_demand__mutmut_11 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_12'] = x_project_demand__mutmut_12 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_13'] = x_project_demand__mutmut_13 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_14'] = x_project_demand__mutmut_14 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_15'] = x_project_demand__mutmut_15 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_16'] = x_project_demand__mutmut_16 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_17'] = x_project_demand__mutmut_17 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_18'] = x_project_demand__mutmut_18 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_19'] = x_project_demand__mutmut_19 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_20'] = x_project_demand__mutmut_20 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_21'] = x_project_demand__mutmut_21 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_22'] = x_project_demand__mutmut_22 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_23'] = x_project_demand__mutmut_23 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_24'] = x_project_demand__mutmut_24 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_25'] = x_project_demand__mutmut_25 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_26'] = x_project_demand__mutmut_26 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_27'] = x_project_demand__mutmut_27 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_28'] = x_project_demand__mutmut_28 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_29'] = x_project_demand__mutmut_29 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_30'] = x_project_demand__mutmut_30 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_31'] = x_project_demand__mutmut_31 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_32'] = x_project_demand__mutmut_32 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_33'] = x_project_demand__mutmut_33 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_34'] = x_project_demand__mutmut_34 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_35'] = x_project_demand__mutmut_35 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_36'] = x_project_demand__mutmut_36 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_37'] = x_project_demand__mutmut_37 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_38'] = x_project_demand__mutmut_38 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_39'] = x_project_demand__mutmut_39 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_40'] = x_project_demand__mutmut_40 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_41'] = x_project_demand__mutmut_41 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_42'] = x_project_demand__mutmut_42 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_43'] = x_project_demand__mutmut_43 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_44'] = x_project_demand__mutmut_44 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_45'] = x_project_demand__mutmut_45 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_46'] = x_project_demand__mutmut_46 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_47'] = x_project_demand__mutmut_47 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_48'] = x_project_demand__mutmut_48 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_49'] = x_project_demand__mutmut_49 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_50'] = x_project_demand__mutmut_50 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_51'] = x_project_demand__mutmut_51 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_52'] = x_project_demand__mutmut_52 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_53'] = x_project_demand__mutmut_53 # type: ignore # mutmut generated
mutants_x_project_demand__mutmut['x_project_demand__mutmut_54'] = x_project_demand__mutmut_54 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__binding_constraint__mutmut)
def _binding_constraint(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_orig(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_1(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = None
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_2(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct >= safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_3(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = None
    if not cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_4(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct >= safe_threshold_pct
    if not cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_5(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over or not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_6(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_7(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_8(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "XXNoneXX"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_9(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "none"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_10(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "NONE"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_11(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct > projected_memory_pct:
        return "CPU"
    return "Memory"


def x__binding_constraint__mutmut_12(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "XXCPUXX"
    return "Memory"


def x__binding_constraint__mutmut_13(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "cpu"
    return "Memory"


def x__binding_constraint__mutmut_14(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "XXMemoryXX"


def x__binding_constraint__mutmut_15(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "memory"


def x__binding_constraint__mutmut_16(
    projected_cpu_pct: float, projected_memory_pct: float, safe_threshold_pct: float
) -> str:
    cpu_over = projected_cpu_pct > safe_threshold_pct
    memory_over = projected_memory_pct > safe_threshold_pct
    if not cpu_over and not memory_over:
        return "None"
    if projected_cpu_pct >= projected_memory_pct:
        return "CPU"
    return "MEMORY"

mutants_x__binding_constraint__mutmut['_mutmut_orig'] = x__binding_constraint__mutmut_orig # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_1'] = x__binding_constraint__mutmut_1 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_2'] = x__binding_constraint__mutmut_2 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_3'] = x__binding_constraint__mutmut_3 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_4'] = x__binding_constraint__mutmut_4 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_5'] = x__binding_constraint__mutmut_5 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_6'] = x__binding_constraint__mutmut_6 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_7'] = x__binding_constraint__mutmut_7 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_8'] = x__binding_constraint__mutmut_8 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_9'] = x__binding_constraint__mutmut_9 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_10'] = x__binding_constraint__mutmut_10 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_11'] = x__binding_constraint__mutmut_11 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_12'] = x__binding_constraint__mutmut_12 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_13'] = x__binding_constraint__mutmut_13 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_14'] = x__binding_constraint__mutmut_14 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_15'] = x__binding_constraint__mutmut_15 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_16'] = x__binding_constraint__mutmut_16 # type: ignore # mutmut generated
mutants_x__utilization__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__utilization__mutmut)
def _utilization(used: float, allocatable: float) -> float:
    if allocatable <= 0:
        return 0.0
    return round(used / allocatable * 100, 1)


def x__utilization__mutmut_orig(used: float, allocatable: float) -> float:
    if allocatable <= 0:
        return 0.0
    return round(used / allocatable * 100, 1)


def x__utilization__mutmut_1(used: float, allocatable: float) -> float:
    if allocatable < 0:
        return 0.0
    return round(used / allocatable * 100, 1)


def x__utilization__mutmut_2(used: float, allocatable: float) -> float:
    if allocatable <= 1:
        return 0.0
    return round(used / allocatable * 100, 1)


def x__utilization__mutmut_3(used: float, allocatable: float) -> float:
    if allocatable <= 0:
        return 1.0
    return round(used / allocatable * 100, 1)


def x__utilization__mutmut_4(used: float, allocatable: float) -> float:
    if allocatable <= 0:
        return 0.0
    return round(None, 1)


def x__utilization__mutmut_5(used: float, allocatable: float) -> float:
    if allocatable <= 0:
        return 0.0
    return round(used / allocatable * 100, None)


def x__utilization__mutmut_6(used: float, allocatable: float) -> float:
    if allocatable <= 0:
        return 0.0
    return round(1)


def x__utilization__mutmut_7(used: float, allocatable: float) -> float:
    if allocatable <= 0:
        return 0.0
    return round(used / allocatable * 100, )


def x__utilization__mutmut_8(used: float, allocatable: float) -> float:
    if allocatable <= 0:
        return 0.0
    return round(used / allocatable / 100, 1)


def x__utilization__mutmut_9(used: float, allocatable: float) -> float:
    if allocatable <= 0:
        return 0.0
    return round(used * allocatable * 100, 1)


def x__utilization__mutmut_10(used: float, allocatable: float) -> float:
    if allocatable <= 0:
        return 0.0
    return round(used / allocatable * 101, 1)


def x__utilization__mutmut_11(used: float, allocatable: float) -> float:
    if allocatable <= 0:
        return 0.0
    return round(used / allocatable * 100, 2)

mutants_x__utilization__mutmut['_mutmut_orig'] = x__utilization__mutmut_orig # type: ignore # mutmut generated
mutants_x__utilization__mutmut['x__utilization__mutmut_1'] = x__utilization__mutmut_1 # type: ignore # mutmut generated
mutants_x__utilization__mutmut['x__utilization__mutmut_2'] = x__utilization__mutmut_2 # type: ignore # mutmut generated
mutants_x__utilization__mutmut['x__utilization__mutmut_3'] = x__utilization__mutmut_3 # type: ignore # mutmut generated
mutants_x__utilization__mutmut['x__utilization__mutmut_4'] = x__utilization__mutmut_4 # type: ignore # mutmut generated
mutants_x__utilization__mutmut['x__utilization__mutmut_5'] = x__utilization__mutmut_5 # type: ignore # mutmut generated
mutants_x__utilization__mutmut['x__utilization__mutmut_6'] = x__utilization__mutmut_6 # type: ignore # mutmut generated
mutants_x__utilization__mutmut['x__utilization__mutmut_7'] = x__utilization__mutmut_7 # type: ignore # mutmut generated
mutants_x__utilization__mutmut['x__utilization__mutmut_8'] = x__utilization__mutmut_8 # type: ignore # mutmut generated
mutants_x__utilization__mutmut['x__utilization__mutmut_9'] = x__utilization__mutmut_9 # type: ignore # mutmut generated
mutants_x__utilization__mutmut['x__utilization__mutmut_10'] = x__utilization__mutmut_10 # type: ignore # mutmut generated
mutants_x__utilization__mutmut['x__utilization__mutmut_11'] = x__utilization__mutmut_11 # type: ignore # mutmut generated
