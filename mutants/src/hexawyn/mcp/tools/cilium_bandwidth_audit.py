"""MCP tool: cilium_bandwidth_audit — Cilium bandwidth manager audit."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.cilium_bandwidth_audit_use_case import (  # noqa: E501
    CiliumBandwidthAuditUseCase,
)
from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.command import (
    CiliumBandwidthAuditCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_cilium_bandwidth_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_cilium_bandwidth_audit__mutmut)
def cilium_bandwidth_audit() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = None
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = None
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=None)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = None
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "XXinstalledXX": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "INSTALLED": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "XXstatusXX": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "STATUS": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "XXtotal_podsXX": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "TOTAL_PODS": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "XXentriesXX": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "ENTRIES": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "XXnoteXX": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "NOTE": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXstatusXX": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "STATUS": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "XXunknownXX",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "UNKNOWN",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "XXtotal_podsXX": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "TOTAL_PODS": 0,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 1,
            "entries": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "XXentriesXX": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "ENTRIES": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "XXnoteXX": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_31() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "NOTE": None,
            "error": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_32() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "XXerrorXX": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_33() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "ERROR": str(exc),
        }


def x_cilium_bandwidth_audit__mutmut_34() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumBandwidthAuditUseCase(port=adapter)
        result = use_case.execute(CiliumBandwidthAuditCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "total_pods": result.total_pods,
            "entries": result.entries,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_pods": 0,
            "entries": [],
            "note": None,
            "error": str(None),
        }

mutants_x_cilium_bandwidth_audit__mutmut['_mutmut_orig'] = x_cilium_bandwidth_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_1'] = x_cilium_bandwidth_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_2'] = x_cilium_bandwidth_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_3'] = x_cilium_bandwidth_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_4'] = x_cilium_bandwidth_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_5'] = x_cilium_bandwidth_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_6'] = x_cilium_bandwidth_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_7'] = x_cilium_bandwidth_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_8'] = x_cilium_bandwidth_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_9'] = x_cilium_bandwidth_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_10'] = x_cilium_bandwidth_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_11'] = x_cilium_bandwidth_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_12'] = x_cilium_bandwidth_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_13'] = x_cilium_bandwidth_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_14'] = x_cilium_bandwidth_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_15'] = x_cilium_bandwidth_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_16'] = x_cilium_bandwidth_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_17'] = x_cilium_bandwidth_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_18'] = x_cilium_bandwidth_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_19'] = x_cilium_bandwidth_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_20'] = x_cilium_bandwidth_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_21'] = x_cilium_bandwidth_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_22'] = x_cilium_bandwidth_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_23'] = x_cilium_bandwidth_audit__mutmut_23 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_24'] = x_cilium_bandwidth_audit__mutmut_24 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_25'] = x_cilium_bandwidth_audit__mutmut_25 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_26'] = x_cilium_bandwidth_audit__mutmut_26 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_27'] = x_cilium_bandwidth_audit__mutmut_27 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_28'] = x_cilium_bandwidth_audit__mutmut_28 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_29'] = x_cilium_bandwidth_audit__mutmut_29 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_30'] = x_cilium_bandwidth_audit__mutmut_30 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_31'] = x_cilium_bandwidth_audit__mutmut_31 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_32'] = x_cilium_bandwidth_audit__mutmut_32 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_33'] = x_cilium_bandwidth_audit__mutmut_33 # type: ignore # mutmut generated
mutants_x_cilium_bandwidth_audit__mutmut['x_cilium_bandwidth_audit__mutmut_34'] = x_cilium_bandwidth_audit__mutmut_34 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(cilium_bandwidth_audit)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(cilium_bandwidth_audit)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
