from __future__ import annotations

import math
from dataclasses import dataclass

from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot

_NODE_TYPE_BY_CONSTRAINT = {
    "CPU": "compute_optimized",
    "Memory": "memory_optimized",
    "None": "balanced",
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class NodeRecommendation:
    node_count: int
    node_type: str
mutants_x_recommend_nodes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_recommend_nodes__mutmut)
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


def x_recommend_nodes__mutmut_orig(
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


def x_recommend_nodes__mutmut_1(
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
    node_type = None
    if binding_constraint == "None":
        return NodeRecommendation(node_count=0, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_2(
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
    node_type = _NODE_TYPE_BY_CONSTRAINT.get(None, "balanced")
    if binding_constraint == "None":
        return NodeRecommendation(node_count=0, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_3(
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
    node_type = _NODE_TYPE_BY_CONSTRAINT.get(binding_constraint, None)
    if binding_constraint == "None":
        return NodeRecommendation(node_count=0, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_4(
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
    node_type = _NODE_TYPE_BY_CONSTRAINT.get("balanced")
    if binding_constraint == "None":
        return NodeRecommendation(node_count=0, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_5(
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
    node_type = _NODE_TYPE_BY_CONSTRAINT.get(binding_constraint, )
    if binding_constraint == "None":
        return NodeRecommendation(node_count=0, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_6(
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
    node_type = _NODE_TYPE_BY_CONSTRAINT.get(binding_constraint, "XXbalancedXX")
    if binding_constraint == "None":
        return NodeRecommendation(node_count=0, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_7(
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
    node_type = _NODE_TYPE_BY_CONSTRAINT.get(binding_constraint, "BALANCED")
    if binding_constraint == "None":
        return NodeRecommendation(node_count=0, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_8(
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
    if binding_constraint != "None":
        return NodeRecommendation(node_count=0, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_9(
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
    if binding_constraint == "XXNoneXX":
        return NodeRecommendation(node_count=0, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_10(
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
    if binding_constraint == "none":
        return NodeRecommendation(node_count=0, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_11(
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
    if binding_constraint == "NONE":
        return NodeRecommendation(node_count=0, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_12(
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
        return NodeRecommendation(node_count=None, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_13(
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
        return NodeRecommendation(node_count=0, node_type=None)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_14(
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
        return NodeRecommendation(node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_15(
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
        return NodeRecommendation(node_count=0, )

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_16(
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
        return NodeRecommendation(node_count=1, node_type=node_type)

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_17(
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

    node_count = None
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_18(
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

    node_count = _nodes_for_constraint(None, multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_19(
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

    node_count = _nodes_for_constraint(snapshot, None, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_20(
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

    node_count = _nodes_for_constraint(snapshot, multiplier, None, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_21(
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

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, None)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_22(
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

    node_count = _nodes_for_constraint(multiplier, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_23(
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

    node_count = _nodes_for_constraint(snapshot, binding_constraint, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_24(
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

    node_count = _nodes_for_constraint(snapshot, multiplier, safe_threshold_pct)
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_25(
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

    node_count = _nodes_for_constraint(snapshot, multiplier, binding_constraint, )
    return NodeRecommendation(node_count=node_count, node_type=node_type)


def x_recommend_nodes__mutmut_26(
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
    return NodeRecommendation(node_count=None, node_type=node_type)


def x_recommend_nodes__mutmut_27(
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
    return NodeRecommendation(node_count=node_count, node_type=None)


def x_recommend_nodes__mutmut_28(
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
    return NodeRecommendation(node_type=node_type)


def x_recommend_nodes__mutmut_29(
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
    return NodeRecommendation(node_count=node_count, )

mutants_x_recommend_nodes__mutmut['_mutmut_orig'] = x_recommend_nodes__mutmut_orig # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_1'] = x_recommend_nodes__mutmut_1 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_2'] = x_recommend_nodes__mutmut_2 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_3'] = x_recommend_nodes__mutmut_3 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_4'] = x_recommend_nodes__mutmut_4 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_5'] = x_recommend_nodes__mutmut_5 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_6'] = x_recommend_nodes__mutmut_6 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_7'] = x_recommend_nodes__mutmut_7 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_8'] = x_recommend_nodes__mutmut_8 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_9'] = x_recommend_nodes__mutmut_9 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_10'] = x_recommend_nodes__mutmut_10 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_11'] = x_recommend_nodes__mutmut_11 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_12'] = x_recommend_nodes__mutmut_12 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_13'] = x_recommend_nodes__mutmut_13 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_14'] = x_recommend_nodes__mutmut_14 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_15'] = x_recommend_nodes__mutmut_15 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_16'] = x_recommend_nodes__mutmut_16 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_17'] = x_recommend_nodes__mutmut_17 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_18'] = x_recommend_nodes__mutmut_18 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_19'] = x_recommend_nodes__mutmut_19 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_20'] = x_recommend_nodes__mutmut_20 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_21'] = x_recommend_nodes__mutmut_21 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_22'] = x_recommend_nodes__mutmut_22 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_23'] = x_recommend_nodes__mutmut_23 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_24'] = x_recommend_nodes__mutmut_24 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_25'] = x_recommend_nodes__mutmut_25 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_26'] = x_recommend_nodes__mutmut_26 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_27'] = x_recommend_nodes__mutmut_27 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_28'] = x_recommend_nodes__mutmut_28 # type: ignore # mutmut generated
mutants_x_recommend_nodes__mutmut['x_recommend_nodes__mutmut_29'] = x_recommend_nodes__mutmut_29 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__nodes_for_constraint__mutmut)
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


def x__nodes_for_constraint__mutmut_orig(
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


def x__nodes_for_constraint__mutmut_1(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    binding_constraint: str,
    safe_threshold_pct: float,
) -> int:
    if binding_constraint != "CPU":
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


def x__nodes_for_constraint__mutmut_2(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    binding_constraint: str,
    safe_threshold_pct: float,
) -> int:
    if binding_constraint == "XXCPUXX":
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


def x__nodes_for_constraint__mutmut_3(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    binding_constraint: str,
    safe_threshold_pct: float,
) -> int:
    if binding_constraint == "cpu":
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


def x__nodes_for_constraint__mutmut_4(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    binding_constraint: str,
    safe_threshold_pct: float,
) -> int:
    if binding_constraint == "CPU":
        used, allocatable = None
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


def x__nodes_for_constraint__mutmut_5(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    binding_constraint: str,
    safe_threshold_pct: float,
) -> int:
    if binding_constraint == "CPU":
        used, allocatable = snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores
    else:
        used, allocatable = None

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


def x__nodes_for_constraint__mutmut_6(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    binding_constraint: str,
    safe_threshold_pct: float,
) -> int:
    if binding_constraint == "CPU":
        used, allocatable = snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores
    else:
        used, allocatable = snapshot.used_memory_gb, snapshot.allocatable_memory_gb

    if allocatable <= 0 and snapshot.node_count <= 0:
        return 0

    projected_used = used * multiplier
    safe_fraction = safe_threshold_pct / 100
    required_allocatable = projected_used / safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_7(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    binding_constraint: str,
    safe_threshold_pct: float,
) -> int:
    if binding_constraint == "CPU":
        used, allocatable = snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores
    else:
        used, allocatable = snapshot.used_memory_gb, snapshot.allocatable_memory_gb

    if allocatable < 0 or snapshot.node_count <= 0:
        return 0

    projected_used = used * multiplier
    safe_fraction = safe_threshold_pct / 100
    required_allocatable = projected_used / safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_8(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    binding_constraint: str,
    safe_threshold_pct: float,
) -> int:
    if binding_constraint == "CPU":
        used, allocatable = snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores
    else:
        used, allocatable = snapshot.used_memory_gb, snapshot.allocatable_memory_gb

    if allocatable <= 1 or snapshot.node_count <= 0:
        return 0

    projected_used = used * multiplier
    safe_fraction = safe_threshold_pct / 100
    required_allocatable = projected_used / safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_9(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    binding_constraint: str,
    safe_threshold_pct: float,
) -> int:
    if binding_constraint == "CPU":
        used, allocatable = snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores
    else:
        used, allocatable = snapshot.used_memory_gb, snapshot.allocatable_memory_gb

    if allocatable <= 0 or snapshot.node_count < 0:
        return 0

    projected_used = used * multiplier
    safe_fraction = safe_threshold_pct / 100
    required_allocatable = projected_used / safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_10(
    snapshot: ClusterCapacitySnapshot,
    multiplier: float,
    binding_constraint: str,
    safe_threshold_pct: float,
) -> int:
    if binding_constraint == "CPU":
        used, allocatable = snapshot.used_cpu_cores, snapshot.allocatable_cpu_cores
    else:
        used, allocatable = snapshot.used_memory_gb, snapshot.allocatable_memory_gb

    if allocatable <= 0 or snapshot.node_count <= 1:
        return 0

    projected_used = used * multiplier
    safe_fraction = safe_threshold_pct / 100
    required_allocatable = projected_used / safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_11(
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
        return 1

    projected_used = used * multiplier
    safe_fraction = safe_threshold_pct / 100
    required_allocatable = projected_used / safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_12(
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

    projected_used = None
    safe_fraction = safe_threshold_pct / 100
    required_allocatable = projected_used / safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_13(
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

    projected_used = used / multiplier
    safe_fraction = safe_threshold_pct / 100
    required_allocatable = projected_used / safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_14(
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
    safe_fraction = None
    required_allocatable = projected_used / safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_15(
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
    safe_fraction = safe_threshold_pct * 100
    required_allocatable = projected_used / safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_16(
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
    safe_fraction = safe_threshold_pct / 101
    required_allocatable = projected_used / safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_17(
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
    required_allocatable = None
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_18(
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
    required_allocatable = projected_used * safe_fraction
    additional_capacity = required_allocatable - allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_19(
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
    additional_capacity = None
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_20(
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
    additional_capacity = required_allocatable + allocatable
    if additional_capacity <= 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_21(
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
    if additional_capacity < 0:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_22(
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
    if additional_capacity <= 1:
        return 0

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_23(
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
        return 1

    per_node_capacity = allocatable / snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_24(
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

    per_node_capacity = None
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_25(
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

    per_node_capacity = allocatable * snapshot.node_count
    return math.ceil(additional_capacity / per_node_capacity)


def x__nodes_for_constraint__mutmut_26(
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
    return math.ceil(None)


def x__nodes_for_constraint__mutmut_27(
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
    return math.ceil(additional_capacity * per_node_capacity)

mutants_x__nodes_for_constraint__mutmut['_mutmut_orig'] = x__nodes_for_constraint__mutmut_orig # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_1'] = x__nodes_for_constraint__mutmut_1 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_2'] = x__nodes_for_constraint__mutmut_2 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_3'] = x__nodes_for_constraint__mutmut_3 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_4'] = x__nodes_for_constraint__mutmut_4 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_5'] = x__nodes_for_constraint__mutmut_5 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_6'] = x__nodes_for_constraint__mutmut_6 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_7'] = x__nodes_for_constraint__mutmut_7 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_8'] = x__nodes_for_constraint__mutmut_8 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_9'] = x__nodes_for_constraint__mutmut_9 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_10'] = x__nodes_for_constraint__mutmut_10 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_11'] = x__nodes_for_constraint__mutmut_11 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_12'] = x__nodes_for_constraint__mutmut_12 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_13'] = x__nodes_for_constraint__mutmut_13 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_14'] = x__nodes_for_constraint__mutmut_14 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_15'] = x__nodes_for_constraint__mutmut_15 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_16'] = x__nodes_for_constraint__mutmut_16 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_17'] = x__nodes_for_constraint__mutmut_17 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_18'] = x__nodes_for_constraint__mutmut_18 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_19'] = x__nodes_for_constraint__mutmut_19 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_20'] = x__nodes_for_constraint__mutmut_20 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_21'] = x__nodes_for_constraint__mutmut_21 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_22'] = x__nodes_for_constraint__mutmut_22 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_23'] = x__nodes_for_constraint__mutmut_23 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_24'] = x__nodes_for_constraint__mutmut_24 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_25'] = x__nodes_for_constraint__mutmut_25 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_26'] = x__nodes_for_constraint__mutmut_26 # type: ignore # mutmut generated
mutants_x__nodes_for_constraint__mutmut['x__nodes_for_constraint__mutmut_27'] = x__nodes_for_constraint__mutmut_27 # type: ignore # mutmut generated
