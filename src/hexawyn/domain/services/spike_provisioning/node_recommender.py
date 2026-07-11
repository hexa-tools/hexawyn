from __future__ import annotations

import math
from dataclasses import dataclass

from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot

_NODE_TYPE_BY_CONSTRAINT = {
    "CPU": "compute_optimized",
    "Memory": "memory_optimized",
    "None": "balanced",
}


@dataclass(frozen=True)
class NodeRecommendation:
    node_count: int
    node_type: str


def recommend_nodes(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    binding_constraint: str,
    safe_threshold_pct: float,
) -> NodeRecommendation:
    """Recommend how many nodes to add, and of which type.

    Sizes the addition so the binding resource's projected utilisation returns
    below the safe threshold. Node type follows the binding constraint:
    CPU-bound → compute-optimized, memory-bound → memory-optimized.
    """
    node_type = _NODE_TYPE_BY_CONSTRAINT.get(binding_constraint, "balanced")
    if binding_constraint == "None":
        return NodeRecommendation(node_count=0, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def _nodes_for_constraint(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    binding_constraint: str,
    safe_threshold_pct: float,
) -> int:
    if binding_constraint == "CPU":
        used, allocatable = snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores
    else:
        used, allocatable = snapshot.used_memory_gb, snapshot.allocatable_memory_gb

    if allocatable <= 0 or snapshot.node_count <= 0:
        return 0

    projected_used = used * multiplier
    safe_fraction = safe_threshold_pct / 100
    required_allocatable = projected_used / safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)
