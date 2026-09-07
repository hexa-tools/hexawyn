"""MCP tool: list_cilium_network_policies — Cilium network policy inventory."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.list_cilium_network_policies.command import (
    ListCiliumNetworkPoliciesCommand,
)
from hexawyn.application.use_case.cilium.list_cilium_network_policies.list_cilium_network_policies_use_case import (  # noqa: E501
    ListCiliumNetworkPoliciesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_list_cilium_network_policies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_cilium_network_policies__mutmut)
def list_cilium_network_policies() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = None
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = None
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=None)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = None
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "XXinstalledXX": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "INSTALLED": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "XXstatusXX": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "STATUS": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "XXtotal_policiesXX": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "TOTAL_POLICIES": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "XXnamespaced_countXX": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "NAMESPACED_COUNT": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "XXclusterwide_countXX": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "CLUSTERWIDE_COUNT": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "XXpoliciesXX": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "POLICIES": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "XXnoteXX": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "NOTE": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXstatusXX": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "STATUS": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "XXunknownXX",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "UNKNOWN",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "XXtotal_policiesXX": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "TOTAL_POLICIES": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_31() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 1,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_32() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "XXnamespaced_countXX": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_33() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "NAMESPACED_COUNT": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_34() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 1,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_35() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "XXclusterwide_countXX": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_36() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "CLUSTERWIDE_COUNT": 0,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_37() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 1,
            "policies": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_38() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "XXpoliciesXX": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_39() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "POLICIES": [],
            "note": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_40() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "XXnoteXX": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_41() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "NOTE": None,
            "error": str(exc),
        }


def x_list_cilium_network_policies__mutmut_42() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "XXerrorXX": str(exc),
        }


def x_list_cilium_network_policies__mutmut_43() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "ERROR": str(exc),
        }


def x_list_cilium_network_policies__mutmut_44() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = ListCiliumNetworkPoliciesUseCase(port=adapter)
        result = use_case.execute(ListCiliumNetworkPoliciesCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_policies": result.total_policies,
            "namespaced_count": result.namespaced_count,
            "clusterwide_count": result.clusterwide_count,
            "policies": result.policies,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_policies": 0,
            "namespaced_count": 0,
            "clusterwide_count": 0,
            "policies": [],
            "note": None,
            "error": str(None),
        }

mutants_x_list_cilium_network_policies__mutmut['_mutmut_orig'] = x_list_cilium_network_policies__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_1'] = x_list_cilium_network_policies__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_2'] = x_list_cilium_network_policies__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_3'] = x_list_cilium_network_policies__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_4'] = x_list_cilium_network_policies__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_5'] = x_list_cilium_network_policies__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_6'] = x_list_cilium_network_policies__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_7'] = x_list_cilium_network_policies__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_8'] = x_list_cilium_network_policies__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_9'] = x_list_cilium_network_policies__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_10'] = x_list_cilium_network_policies__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_11'] = x_list_cilium_network_policies__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_12'] = x_list_cilium_network_policies__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_13'] = x_list_cilium_network_policies__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_14'] = x_list_cilium_network_policies__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_15'] = x_list_cilium_network_policies__mutmut_15 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_16'] = x_list_cilium_network_policies__mutmut_16 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_17'] = x_list_cilium_network_policies__mutmut_17 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_18'] = x_list_cilium_network_policies__mutmut_18 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_19'] = x_list_cilium_network_policies__mutmut_19 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_20'] = x_list_cilium_network_policies__mutmut_20 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_21'] = x_list_cilium_network_policies__mutmut_21 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_22'] = x_list_cilium_network_policies__mutmut_22 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_23'] = x_list_cilium_network_policies__mutmut_23 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_24'] = x_list_cilium_network_policies__mutmut_24 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_25'] = x_list_cilium_network_policies__mutmut_25 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_26'] = x_list_cilium_network_policies__mutmut_26 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_27'] = x_list_cilium_network_policies__mutmut_27 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_28'] = x_list_cilium_network_policies__mutmut_28 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_29'] = x_list_cilium_network_policies__mutmut_29 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_30'] = x_list_cilium_network_policies__mutmut_30 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_31'] = x_list_cilium_network_policies__mutmut_31 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_32'] = x_list_cilium_network_policies__mutmut_32 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_33'] = x_list_cilium_network_policies__mutmut_33 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_34'] = x_list_cilium_network_policies__mutmut_34 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_35'] = x_list_cilium_network_policies__mutmut_35 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_36'] = x_list_cilium_network_policies__mutmut_36 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_37'] = x_list_cilium_network_policies__mutmut_37 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_38'] = x_list_cilium_network_policies__mutmut_38 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_39'] = x_list_cilium_network_policies__mutmut_39 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_40'] = x_list_cilium_network_policies__mutmut_40 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_41'] = x_list_cilium_network_policies__mutmut_41 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_42'] = x_list_cilium_network_policies__mutmut_42 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_43'] = x_list_cilium_network_policies__mutmut_43 # type: ignore # mutmut generated
mutants_x_list_cilium_network_policies__mutmut['x_list_cilium_network_policies__mutmut_44'] = x_list_cilium_network_policies__mutmut_44 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(list_cilium_network_policies)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(list_cilium_network_policies)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
