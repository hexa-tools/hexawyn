"""MCP tool: compare_cluster_health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.compare_cluster_health.command import (
    CompareClusterHealthCommand,
)
from hexawyn.application.use_case.cluster.compare_cluster_health.compare_cluster_health_use_case import (  # noqa: E501
    CompareClusterHealthUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from hexawyn.domain.models.cluster_health_comparison import ClusterHealthSnapshot


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__snapshot_to_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__snapshot_to_dict__mutmut)
def _snapshot_to_dict(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_orig(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_1(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "XXcluster_nameXX": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_2(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "CLUSTER_NAME": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_3(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "XXfailing_podsXX": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_4(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "FAILING_PODS": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_5(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "XXtotal_podsXX": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_6(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "TOTAL_PODS": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_7(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "XXcpu_utilization_pctXX": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_8(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "CPU_UTILIZATION_PCT": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_9(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "XXmemory_utilization_pctXX": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_10(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "MEMORY_UTILIZATION_PCT": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_11(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "XXnode_countXX": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_12(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "NODE_COUNT": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_13(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "XXnodes_not_readyXX": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_14(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "NODES_NOT_READY": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_15(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "XXactive_incidentsXX": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_16(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "ACTIVE_INCIDENTS": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_17(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "XXhealth_statusXX": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_18(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "HEALTH_STATUS": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_19(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "XXin_maintenanceXX": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_20(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "IN_MAINTENANCE": snapshot.in_maintenance,
        "reachable": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_21(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "XXreachableXX": snapshot.reachable,
    }


def x__snapshot_to_dict__mutmut_22(snapshot: ClusterHealthSnapshot) -> dict[str, object]:
    return {
        "cluster_name": snapshot.cluster_name,
        "failing_pods": snapshot.failing_pods,
        "total_pods": snapshot.total_pods,
        "cpu_utilization_pct": snapshot.cpu_utilization_pct,
        "memory_utilization_pct": snapshot.memory_utilization_pct,
        "node_count": snapshot.node_count,
        "nodes_not_ready": snapshot.nodes_not_ready,
        "active_incidents": snapshot.active_incidents,
        "health_status": snapshot.health_status,
        "in_maintenance": snapshot.in_maintenance,
        "REACHABLE": snapshot.reachable,
    }

mutants_x__snapshot_to_dict__mutmut['_mutmut_orig'] = x__snapshot_to_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_1'] = x__snapshot_to_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_2'] = x__snapshot_to_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_3'] = x__snapshot_to_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_4'] = x__snapshot_to_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_5'] = x__snapshot_to_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_6'] = x__snapshot_to_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_7'] = x__snapshot_to_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_8'] = x__snapshot_to_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_9'] = x__snapshot_to_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_10'] = x__snapshot_to_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_11'] = x__snapshot_to_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_12'] = x__snapshot_to_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_13'] = x__snapshot_to_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_14'] = x__snapshot_to_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_15'] = x__snapshot_to_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_16'] = x__snapshot_to_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_17'] = x__snapshot_to_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_18'] = x__snapshot_to_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_19'] = x__snapshot_to_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_20'] = x__snapshot_to_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_21'] = x__snapshot_to_dict__mutmut_21 # type: ignore # mutmut generated
mutants_x__snapshot_to_dict__mutmut['x__snapshot_to_dict__mutmut_22'] = x__snapshot_to_dict__mutmut_22 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compare_cluster_health__mutmut)
def compare_cluster_health(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_orig(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_1(cluster_a: str = "XXtestXX", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_2(cluster_a: str = "TEST", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_3(cluster_a: str = "test", cluster_b: str = "XXtestXX") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_4(cluster_a: str = "test", cluster_b: str = "TEST") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_5(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = None
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_6(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=None)
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_7(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = None
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_8(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            None
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_9(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=None, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_10(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=None)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_11(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_12(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, )
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_13(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = None
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_14(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "XXcomparisonXX": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_15(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "COMPARISON": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_16(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "XXworse_clusterXX": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_17(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "WORSE_CLUSTER": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_18(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "XXreasonXX": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_19(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "REASON": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_20(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "XXdelta_failing_podsXX": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_21(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "DELTA_FAILING_PODS": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_22(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "XXdelta_cpu_pctXX": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_23(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "DELTA_CPU_PCT": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_24(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "XXdelta_active_incidentsXX": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_25(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "DELTA_ACTIVE_INCIDENTS": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_26(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "XXnormalized_a_failing_per_100XX": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_27(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "NORMALIZED_A_FAILING_PER_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_28(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "XXnormalized_b_failing_per_100XX": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_29(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "NORMALIZED_B_FAILING_PER_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_30(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "XXcluster_aXX": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_31(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "CLUSTER_A": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_32(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(None),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_33(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "XXcluster_bXX": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_34(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "CLUSTER_B": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_35(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(None),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_36(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_37(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "ERROR": None,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_cluster_health__mutmut_38(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_compare_cluster_health__mutmut_39(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_compare_cluster_health__mutmut_40(cluster_a: str = "test", cluster_b: str = "test") -> dict[str, object]:
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        use_case = CompareClusterHealthUseCase(fleet_health_port=build_fleet_health_adapter())
        response = use_case.execute(
            CompareClusterHealthCommand(cluster_a=cluster_a, cluster_b=cluster_b)
        )
        comp = response.result.comparison
        return {
            "comparison": {
                "worse_cluster": comp.worse_cluster,
                "reason": comp.reason,
                "delta_failing_pods": comp.delta_failing_pods,
                "delta_cpu_pct": comp.delta_cpu_pct,
                "delta_active_incidents": comp.delta_active_incidents,
                "normalized_a_failing_per_100": comp.normalized_a_failing_per_100,
                "normalized_b_failing_per_100": comp.normalized_b_failing_per_100,
            },
            "cluster_a": _snapshot_to_dict(response.result.cluster_a),
            "cluster_b": _snapshot_to_dict(response.result.cluster_b),
            "error": None,
        }
    except Exception as exc:
        return {"error": str(None)}

mutants_x_compare_cluster_health__mutmut['_mutmut_orig'] = x_compare_cluster_health__mutmut_orig # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_1'] = x_compare_cluster_health__mutmut_1 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_2'] = x_compare_cluster_health__mutmut_2 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_3'] = x_compare_cluster_health__mutmut_3 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_4'] = x_compare_cluster_health__mutmut_4 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_5'] = x_compare_cluster_health__mutmut_5 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_6'] = x_compare_cluster_health__mutmut_6 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_7'] = x_compare_cluster_health__mutmut_7 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_8'] = x_compare_cluster_health__mutmut_8 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_9'] = x_compare_cluster_health__mutmut_9 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_10'] = x_compare_cluster_health__mutmut_10 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_11'] = x_compare_cluster_health__mutmut_11 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_12'] = x_compare_cluster_health__mutmut_12 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_13'] = x_compare_cluster_health__mutmut_13 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_14'] = x_compare_cluster_health__mutmut_14 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_15'] = x_compare_cluster_health__mutmut_15 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_16'] = x_compare_cluster_health__mutmut_16 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_17'] = x_compare_cluster_health__mutmut_17 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_18'] = x_compare_cluster_health__mutmut_18 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_19'] = x_compare_cluster_health__mutmut_19 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_20'] = x_compare_cluster_health__mutmut_20 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_21'] = x_compare_cluster_health__mutmut_21 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_22'] = x_compare_cluster_health__mutmut_22 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_23'] = x_compare_cluster_health__mutmut_23 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_24'] = x_compare_cluster_health__mutmut_24 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_25'] = x_compare_cluster_health__mutmut_25 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_26'] = x_compare_cluster_health__mutmut_26 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_27'] = x_compare_cluster_health__mutmut_27 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_28'] = x_compare_cluster_health__mutmut_28 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_29'] = x_compare_cluster_health__mutmut_29 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_30'] = x_compare_cluster_health__mutmut_30 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_31'] = x_compare_cluster_health__mutmut_31 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_32'] = x_compare_cluster_health__mutmut_32 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_33'] = x_compare_cluster_health__mutmut_33 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_34'] = x_compare_cluster_health__mutmut_34 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_35'] = x_compare_cluster_health__mutmut_35 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_36'] = x_compare_cluster_health__mutmut_36 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_37'] = x_compare_cluster_health__mutmut_37 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_38'] = x_compare_cluster_health__mutmut_38 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_39'] = x_compare_cluster_health__mutmut_39 # type: ignore # mutmut generated
mutants_x_compare_cluster_health__mutmut['x_compare_cluster_health__mutmut_40'] = x_compare_cluster_health__mutmut_40 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(compare_cluster_health)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(compare_cluster_health)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
