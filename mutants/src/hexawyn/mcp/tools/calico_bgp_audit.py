"""MCP tool: calico_bgp_audit — Calico BGP configuration and peer state."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_bgp_audit.calico_bgp_audit_use_case import (
    CalicoBgpAuditUseCase,
)
from hexawyn.application.use_case.calico.calico_bgp_audit.command import CalicoBgpAuditCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__peer_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__peer_dict__mutmut)
def _peer_dict(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_orig(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_1(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "XXnameXX": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_2(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "NAME": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_3(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(None, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_4(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, None, None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_5(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr("name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_6(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_7(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", ),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_8(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "XXnameXX", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_9(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "NAME", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_10(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "XXpeer_ipXX": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_11(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "PEER_IP": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_12(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(None, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_13(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, None, None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_14(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr("peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_15(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_16(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", ),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_17(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "XXpeer_ipXX", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_18(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "PEER_IP", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_19(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "XXas_numberXX": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_20(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "AS_NUMBER": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_21(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(None, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_22(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, None, None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_23(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr("as_number", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_24(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_25(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", ),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_26(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "XXas_numberXX", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_27(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "AS_NUMBER", None),
        "node_selector": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_28(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "XXnode_selectorXX": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_29(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "NODE_SELECTOR": getattr(peer, "node_selector", ""),
    }


def x__peer_dict__mutmut_30(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(None, "node_selector", ""),
    }


def x__peer_dict__mutmut_31(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, None, ""),
    }


def x__peer_dict__mutmut_32(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", None),
    }


def x__peer_dict__mutmut_33(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr("node_selector", ""),
    }


def x__peer_dict__mutmut_34(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, ""),
    }


def x__peer_dict__mutmut_35(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", ),
    }


def x__peer_dict__mutmut_36(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "XXnode_selectorXX", ""),
    }


def x__peer_dict__mutmut_37(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "NODE_SELECTOR", ""),
    }


def x__peer_dict__mutmut_38(peer: object) -> dict[str, object]:
    """Project a CalicoBgpPeer into a plain, serialisable dict."""
    return {
        "name": getattr(peer, "name", None),
        "peer_ip": getattr(peer, "peer_ip", None),
        "as_number": getattr(peer, "as_number", None),
        "node_selector": getattr(peer, "node_selector", "XXXX"),
    }

mutants_x__peer_dict__mutmut['_mutmut_orig'] = x__peer_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_1'] = x__peer_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_2'] = x__peer_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_3'] = x__peer_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_4'] = x__peer_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_5'] = x__peer_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_6'] = x__peer_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_7'] = x__peer_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_8'] = x__peer_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_9'] = x__peer_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_10'] = x__peer_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_11'] = x__peer_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_12'] = x__peer_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_13'] = x__peer_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_14'] = x__peer_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_15'] = x__peer_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_16'] = x__peer_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_17'] = x__peer_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_18'] = x__peer_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_19'] = x__peer_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_20'] = x__peer_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_21'] = x__peer_dict__mutmut_21 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_22'] = x__peer_dict__mutmut_22 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_23'] = x__peer_dict__mutmut_23 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_24'] = x__peer_dict__mutmut_24 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_25'] = x__peer_dict__mutmut_25 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_26'] = x__peer_dict__mutmut_26 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_27'] = x__peer_dict__mutmut_27 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_28'] = x__peer_dict__mutmut_28 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_29'] = x__peer_dict__mutmut_29 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_30'] = x__peer_dict__mutmut_30 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_31'] = x__peer_dict__mutmut_31 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_32'] = x__peer_dict__mutmut_32 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_33'] = x__peer_dict__mutmut_33 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_34'] = x__peer_dict__mutmut_34 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_35'] = x__peer_dict__mutmut_35 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_36'] = x__peer_dict__mutmut_36 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_37'] = x__peer_dict__mutmut_37 # type: ignore # mutmut generated
mutants_x__peer_dict__mutmut['x__peer_dict__mutmut_38'] = x__peer_dict__mutmut_38 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calico_bgp_audit__mutmut)
def calico_bgp_audit() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = None
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=None)
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = None
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "XXinstalledXX": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "INSTALLED": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "XXnot_installed_markerXX": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "NOT_INSTALLED_MARKER": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "XXas_numberXX": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "AS_NUMBER": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "XXnode_to_node_mesh_enabledXX": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "NODE_TO_NODE_MESH_ENABLED": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "XXservice_cluster_ipsXX": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "SERVICE_CLUSTER_IPS": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(None),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "XXpeer_countXX": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "PEER_COUNT": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "XXpeersXX": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "PEERS": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(None) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "XXsession_stateXX": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "SESSION_STATE": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "XXsession_noteXX": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "SESSION_NOTE": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "XXsummaryXX": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "SUMMARY": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_31() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_32() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXnot_installed_markerXX": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_33() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "NOT_INSTALLED_MARKER": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_34() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "XXNOT_INSTALLEDXX",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_35() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "not_installed",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_36() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "XXas_numberXX": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_37() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "AS_NUMBER": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_38() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "XXnode_to_node_mesh_enabledXX": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_39() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "NODE_TO_NODE_MESH_ENABLED": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_40() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "XXservice_cluster_ipsXX": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_41() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "SERVICE_CLUSTER_IPS": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_42() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "XXpeer_countXX": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_43() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "PEER_COUNT": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_44() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 1,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_45() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "XXpeersXX": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_46() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "PEERS": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_47() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "XXsession_stateXX": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_48() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "SESSION_STATE": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_49() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "XXunknownXX",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_50() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "UNKNOWN",
            "session_note": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_51() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "XXsession_noteXX": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_52() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "SESSION_NOTE": None,
            "summary": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_53() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "XXsummaryXX": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_54() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "SUMMARY": None,
            "error": str(exc),
        }


def x_calico_bgp_audit__mutmut_55() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "XXerrorXX": str(exc),
        }


def x_calico_bgp_audit__mutmut_56() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "ERROR": str(exc),
        }


def x_calico_bgp_audit__mutmut_57() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoBgpAuditUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoBgpAuditCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "as_number": result.as_number,
            "node_to_node_mesh_enabled": result.node_to_node_mesh_enabled,
            "service_cluster_ips": list(result.service_cluster_ips),
            "peer_count": result.peer_count,
            "peers": [_peer_dict(peer) for peer in result.peers],
            "session_state": result.session_state,
            "session_note": result.session_note,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "as_number": None,
            "node_to_node_mesh_enabled": None,
            "service_cluster_ips": [],
            "peer_count": 0,
            "peers": [],
            "session_state": "unknown",
            "session_note": None,
            "summary": None,
            "error": str(None),
        }

mutants_x_calico_bgp_audit__mutmut['_mutmut_orig'] = x_calico_bgp_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_1'] = x_calico_bgp_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_2'] = x_calico_bgp_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_3'] = x_calico_bgp_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_4'] = x_calico_bgp_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_5'] = x_calico_bgp_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_6'] = x_calico_bgp_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_7'] = x_calico_bgp_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_8'] = x_calico_bgp_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_9'] = x_calico_bgp_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_10'] = x_calico_bgp_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_11'] = x_calico_bgp_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_12'] = x_calico_bgp_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_13'] = x_calico_bgp_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_14'] = x_calico_bgp_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_15'] = x_calico_bgp_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_16'] = x_calico_bgp_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_17'] = x_calico_bgp_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_18'] = x_calico_bgp_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_19'] = x_calico_bgp_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_20'] = x_calico_bgp_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_21'] = x_calico_bgp_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_22'] = x_calico_bgp_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_23'] = x_calico_bgp_audit__mutmut_23 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_24'] = x_calico_bgp_audit__mutmut_24 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_25'] = x_calico_bgp_audit__mutmut_25 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_26'] = x_calico_bgp_audit__mutmut_26 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_27'] = x_calico_bgp_audit__mutmut_27 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_28'] = x_calico_bgp_audit__mutmut_28 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_29'] = x_calico_bgp_audit__mutmut_29 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_30'] = x_calico_bgp_audit__mutmut_30 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_31'] = x_calico_bgp_audit__mutmut_31 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_32'] = x_calico_bgp_audit__mutmut_32 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_33'] = x_calico_bgp_audit__mutmut_33 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_34'] = x_calico_bgp_audit__mutmut_34 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_35'] = x_calico_bgp_audit__mutmut_35 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_36'] = x_calico_bgp_audit__mutmut_36 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_37'] = x_calico_bgp_audit__mutmut_37 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_38'] = x_calico_bgp_audit__mutmut_38 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_39'] = x_calico_bgp_audit__mutmut_39 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_40'] = x_calico_bgp_audit__mutmut_40 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_41'] = x_calico_bgp_audit__mutmut_41 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_42'] = x_calico_bgp_audit__mutmut_42 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_43'] = x_calico_bgp_audit__mutmut_43 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_44'] = x_calico_bgp_audit__mutmut_44 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_45'] = x_calico_bgp_audit__mutmut_45 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_46'] = x_calico_bgp_audit__mutmut_46 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_47'] = x_calico_bgp_audit__mutmut_47 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_48'] = x_calico_bgp_audit__mutmut_48 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_49'] = x_calico_bgp_audit__mutmut_49 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_50'] = x_calico_bgp_audit__mutmut_50 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_51'] = x_calico_bgp_audit__mutmut_51 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_52'] = x_calico_bgp_audit__mutmut_52 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_53'] = x_calico_bgp_audit__mutmut_53 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_54'] = x_calico_bgp_audit__mutmut_54 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_55'] = x_calico_bgp_audit__mutmut_55 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_56'] = x_calico_bgp_audit__mutmut_56 # type: ignore # mutmut generated
mutants_x_calico_bgp_audit__mutmut['x_calico_bgp_audit__mutmut_57'] = x_calico_bgp_audit__mutmut_57 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_bgp_audit)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(calico_bgp_audit)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
