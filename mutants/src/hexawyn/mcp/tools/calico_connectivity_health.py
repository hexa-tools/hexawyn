"""MCP tool: calico_connectivity_health — Calico dataplane end-to-end health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_connectivity_health.calico_connectivity_health_use_case import (  # noqa: E501
    CalicoConnectivityHealthUseCase,
)
from hexawyn.application.use_case.calico.calico_connectivity_health.command import (
    CalicoConnectivityHealthCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__node_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__node_dict__mutmut)
def _node_dict(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "ready": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_orig(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "ready": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_1(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "XXnodeXX": getattr(node, "node", None),
        "ready": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_2(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "NODE": getattr(node, "node", None),
        "ready": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_3(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(None, "node", None),
        "ready": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_4(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, None, None),
        "ready": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_5(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr("node", None),
        "ready": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_6(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, None),
        "ready": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_7(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", ),
        "ready": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_8(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "XXnodeXX", None),
        "ready": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_9(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "NODE", None),
        "ready": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_10(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "XXreadyXX": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_11(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "READY": getattr(node, "ready", False),
    }


def x__node_dict__mutmut_12(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "ready": getattr(None, "ready", False),
    }


def x__node_dict__mutmut_13(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "ready": getattr(node, None, False),
    }


def x__node_dict__mutmut_14(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "ready": getattr(node, "ready", None),
    }


def x__node_dict__mutmut_15(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "ready": getattr("ready", False),
    }


def x__node_dict__mutmut_16(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "ready": getattr(node, False),
    }


def x__node_dict__mutmut_17(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "ready": getattr(node, "ready", ),
    }


def x__node_dict__mutmut_18(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "ready": getattr(node, "XXreadyXX", False),
    }


def x__node_dict__mutmut_19(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "ready": getattr(node, "READY", False),
    }


def x__node_dict__mutmut_20(node: object) -> dict[str, object]:
    """Project a CalicoNodeConnectivity into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "ready": getattr(node, "ready", True),
    }

mutants_x__node_dict__mutmut['_mutmut_orig'] = x__node_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_1'] = x__node_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_2'] = x__node_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_3'] = x__node_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_4'] = x__node_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_5'] = x__node_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_6'] = x__node_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_7'] = x__node_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_8'] = x__node_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_9'] = x__node_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_10'] = x__node_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_11'] = x__node_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_12'] = x__node_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_13'] = x__node_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_14'] = x__node_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_15'] = x__node_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_16'] = x__node_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_17'] = x__node_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_18'] = x__node_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_19'] = x__node_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_20'] = x__node_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calico_connectivity_health__mutmut)
def calico_connectivity_health() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = None
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=None)
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = None
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "XXinstalledXX": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "INSTALLED": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "XXnot_installed_markerXX": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "NOT_INSTALLED_MARKER": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "XXverdictXX": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "VERDICT": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "XXready_agentsXX": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "READY_AGENTS": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "XXtotal_agentsXX": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "TOTAL_AGENTS": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "XXdataplane_modeXX": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "DATAPLANE_MODE": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "XXtunnel_summaryXX": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "TUNNEL_SUMMARY": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "XXbgp_summaryXX": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "BGP_SUMMARY": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "XXconnectivity_probeXX": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "CONNECTIVITY_PROBE": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "XXnodesXX": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "NODES": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(None) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "XXdegraded_nodesXX": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "DEGRADED_NODES": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(None),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "XXsummaryXX": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "SUMMARY": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_31() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_32() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_33() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_34() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_35() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_36() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXnot_installed_markerXX": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_37() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "NOT_INSTALLED_MARKER": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_38() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "XXNOT_INSTALLEDXX",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_39() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "not_installed",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_40() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "XXverdictXX": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_41() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "VERDICT": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_42() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "XXunknownXX",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_43() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "UNKNOWN",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_44() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "XXready_agentsXX": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_45() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "READY_AGENTS": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_46() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 1,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_47() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "XXtotal_agentsXX": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_48() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "TOTAL_AGENTS": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_49() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 1,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_50() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "XXdataplane_modeXX": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_51() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "DATAPLANE_MODE": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_52() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "XXtunnel_summaryXX": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_53() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "TUNNEL_SUMMARY": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_54() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "XXUNKNOWNXX",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_55() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "unknown",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_56() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "XXbgp_summaryXX": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_57() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "BGP_SUMMARY": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_58() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "XXUNKNOWNXX",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_59() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "unknown",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_60() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "XXconnectivity_probeXX": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_61() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "CONNECTIVITY_PROBE": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_62() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "XXnodesXX": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_63() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "NODES": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_64() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "XXdegraded_nodesXX": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_65() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "DEGRADED_NODES": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_66() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "XXsummaryXX": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_67() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "SUMMARY": None,
            "error": str(exc),
        }


def x_calico_connectivity_health__mutmut_68() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "XXerrorXX": str(exc),
        }


def x_calico_connectivity_health__mutmut_69() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "ERROR": str(exc),
        }


def x_calico_connectivity_health__mutmut_70() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoConnectivityHealthUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoConnectivityHealthCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "verdict": result.verdict,
            "ready_agents": result.ready_agents,
            "total_agents": result.total_agents,
            "dataplane_mode": result.dataplane_mode,
            "tunnel_summary": result.tunnel_summary,
            "bgp_summary": result.bgp_summary,
            "connectivity_probe": result.connectivity_probe,
            "nodes": [_node_dict(node) for node in result.nodes],
            "degraded_nodes": list(result.degraded_nodes),
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "verdict": "unknown",
            "ready_agents": 0,
            "total_agents": 0,
            "dataplane_mode": None,
            "tunnel_summary": "UNKNOWN",
            "bgp_summary": "UNKNOWN",
            "connectivity_probe": None,
            "nodes": [],
            "degraded_nodes": [],
            "summary": None,
            "error": str(None),
        }

mutants_x_calico_connectivity_health__mutmut['_mutmut_orig'] = x_calico_connectivity_health__mutmut_orig # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_1'] = x_calico_connectivity_health__mutmut_1 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_2'] = x_calico_connectivity_health__mutmut_2 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_3'] = x_calico_connectivity_health__mutmut_3 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_4'] = x_calico_connectivity_health__mutmut_4 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_5'] = x_calico_connectivity_health__mutmut_5 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_6'] = x_calico_connectivity_health__mutmut_6 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_7'] = x_calico_connectivity_health__mutmut_7 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_8'] = x_calico_connectivity_health__mutmut_8 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_9'] = x_calico_connectivity_health__mutmut_9 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_10'] = x_calico_connectivity_health__mutmut_10 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_11'] = x_calico_connectivity_health__mutmut_11 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_12'] = x_calico_connectivity_health__mutmut_12 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_13'] = x_calico_connectivity_health__mutmut_13 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_14'] = x_calico_connectivity_health__mutmut_14 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_15'] = x_calico_connectivity_health__mutmut_15 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_16'] = x_calico_connectivity_health__mutmut_16 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_17'] = x_calico_connectivity_health__mutmut_17 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_18'] = x_calico_connectivity_health__mutmut_18 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_19'] = x_calico_connectivity_health__mutmut_19 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_20'] = x_calico_connectivity_health__mutmut_20 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_21'] = x_calico_connectivity_health__mutmut_21 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_22'] = x_calico_connectivity_health__mutmut_22 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_23'] = x_calico_connectivity_health__mutmut_23 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_24'] = x_calico_connectivity_health__mutmut_24 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_25'] = x_calico_connectivity_health__mutmut_25 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_26'] = x_calico_connectivity_health__mutmut_26 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_27'] = x_calico_connectivity_health__mutmut_27 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_28'] = x_calico_connectivity_health__mutmut_28 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_29'] = x_calico_connectivity_health__mutmut_29 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_30'] = x_calico_connectivity_health__mutmut_30 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_31'] = x_calico_connectivity_health__mutmut_31 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_32'] = x_calico_connectivity_health__mutmut_32 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_33'] = x_calico_connectivity_health__mutmut_33 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_34'] = x_calico_connectivity_health__mutmut_34 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_35'] = x_calico_connectivity_health__mutmut_35 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_36'] = x_calico_connectivity_health__mutmut_36 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_37'] = x_calico_connectivity_health__mutmut_37 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_38'] = x_calico_connectivity_health__mutmut_38 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_39'] = x_calico_connectivity_health__mutmut_39 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_40'] = x_calico_connectivity_health__mutmut_40 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_41'] = x_calico_connectivity_health__mutmut_41 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_42'] = x_calico_connectivity_health__mutmut_42 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_43'] = x_calico_connectivity_health__mutmut_43 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_44'] = x_calico_connectivity_health__mutmut_44 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_45'] = x_calico_connectivity_health__mutmut_45 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_46'] = x_calico_connectivity_health__mutmut_46 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_47'] = x_calico_connectivity_health__mutmut_47 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_48'] = x_calico_connectivity_health__mutmut_48 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_49'] = x_calico_connectivity_health__mutmut_49 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_50'] = x_calico_connectivity_health__mutmut_50 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_51'] = x_calico_connectivity_health__mutmut_51 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_52'] = x_calico_connectivity_health__mutmut_52 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_53'] = x_calico_connectivity_health__mutmut_53 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_54'] = x_calico_connectivity_health__mutmut_54 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_55'] = x_calico_connectivity_health__mutmut_55 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_56'] = x_calico_connectivity_health__mutmut_56 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_57'] = x_calico_connectivity_health__mutmut_57 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_58'] = x_calico_connectivity_health__mutmut_58 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_59'] = x_calico_connectivity_health__mutmut_59 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_60'] = x_calico_connectivity_health__mutmut_60 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_61'] = x_calico_connectivity_health__mutmut_61 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_62'] = x_calico_connectivity_health__mutmut_62 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_63'] = x_calico_connectivity_health__mutmut_63 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_64'] = x_calico_connectivity_health__mutmut_64 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_65'] = x_calico_connectivity_health__mutmut_65 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_66'] = x_calico_connectivity_health__mutmut_66 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_67'] = x_calico_connectivity_health__mutmut_67 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_68'] = x_calico_connectivity_health__mutmut_68 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_69'] = x_calico_connectivity_health__mutmut_69 # type: ignore # mutmut generated
mutants_x_calico_connectivity_health__mutmut['x_calico_connectivity_health__mutmut_70'] = x_calico_connectivity_health__mutmut_70 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_connectivity_health)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(calico_connectivity_health)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
