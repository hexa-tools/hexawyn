from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot

_DEFAULT_SAFE_THRESHOLD_PCT = 85.0


@dataclass(frozen=True)
class DemandProjection:
    current_cpu_headroom_pct: float
    current_memory_headroom_pct: float
    projected_cpu_pct: float
    projected_memory_pct: float
    binding_constraint: str


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


def _utilization(used: float, allocatable: float) -> float:
    if allocatable <= 0:
        return 0.0
    return round(used / allocatable * 100, 1)
