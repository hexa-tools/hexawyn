"""MCP tool: get_cilium_flows — query Cilium flow logs via Hubble."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.get_cilium_flows.command import (
    GetCiliumFlowsCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_flows.get_cilium_flows_use_case import (
    GetCiliumFlowsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_cilium_flows__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_cilium_flows__mutmut)
def get_cilium_flows(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_orig(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_1(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 16,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_2(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 101,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_3(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = None
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_4(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = None
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_5(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=None)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_6(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = None
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_7(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            None
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_8(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=None,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_9(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=None,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_10(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=None,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_11(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=None,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_12(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=None,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_13(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=None,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_14(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_15(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_16(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_17(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_18(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_19(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_20(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "XXinstalledXX": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_21(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "INSTALLED": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_22(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "XXstatusXX": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_23(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "STATUS": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_24(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "XXtotal_flowsXX": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_25(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "TOTAL_FLOWS": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_26(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "XXflowsXX": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_27(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "FLOWS": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_28(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "XXnoteXX": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_29(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "NOTE": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_30(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_31(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_32(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_33(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_34(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_35(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXstatusXX": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_36(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "STATUS": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_37(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "XXunknownXX",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_38(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "UNKNOWN",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_39(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "XXtotal_flowsXX": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_40(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "TOTAL_FLOWS": 0,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_41(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 1,
            "flows": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_42(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "XXflowsXX": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_43(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "FLOWS": [],
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_44(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "XXnoteXX": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_45(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "NOTE": None,
            "error": str(exc),
        }


def x_get_cilium_flows__mutmut_46(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "XXerrorXX": str(exc),
        }


def x_get_cilium_flows__mutmut_47(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "ERROR": str(exc),
        }


def x_get_cilium_flows__mutmut_48(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = GetCiliumFlowsUseCase(port=adapter)
        result = use_case.execute(
            GetCiliumFlowsCommand(
                namespace=namespace,
                pod=pod,
                direction=direction,
                verdict=verdict,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_flows": result.total_flows,
            "flows": result.flows,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_flows": 0,
            "flows": [],
            "note": None,
            "error": str(None),
        }

mutants_x_get_cilium_flows__mutmut['_mutmut_orig'] = x_get_cilium_flows__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_1'] = x_get_cilium_flows__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_2'] = x_get_cilium_flows__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_3'] = x_get_cilium_flows__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_4'] = x_get_cilium_flows__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_5'] = x_get_cilium_flows__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_6'] = x_get_cilium_flows__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_7'] = x_get_cilium_flows__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_8'] = x_get_cilium_flows__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_9'] = x_get_cilium_flows__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_10'] = x_get_cilium_flows__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_11'] = x_get_cilium_flows__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_12'] = x_get_cilium_flows__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_13'] = x_get_cilium_flows__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_14'] = x_get_cilium_flows__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_15'] = x_get_cilium_flows__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_16'] = x_get_cilium_flows__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_17'] = x_get_cilium_flows__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_18'] = x_get_cilium_flows__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_19'] = x_get_cilium_flows__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_20'] = x_get_cilium_flows__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_21'] = x_get_cilium_flows__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_22'] = x_get_cilium_flows__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_23'] = x_get_cilium_flows__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_24'] = x_get_cilium_flows__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_25'] = x_get_cilium_flows__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_26'] = x_get_cilium_flows__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_27'] = x_get_cilium_flows__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_28'] = x_get_cilium_flows__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_29'] = x_get_cilium_flows__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_30'] = x_get_cilium_flows__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_31'] = x_get_cilium_flows__mutmut_31 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_32'] = x_get_cilium_flows__mutmut_32 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_33'] = x_get_cilium_flows__mutmut_33 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_34'] = x_get_cilium_flows__mutmut_34 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_35'] = x_get_cilium_flows__mutmut_35 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_36'] = x_get_cilium_flows__mutmut_36 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_37'] = x_get_cilium_flows__mutmut_37 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_38'] = x_get_cilium_flows__mutmut_38 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_39'] = x_get_cilium_flows__mutmut_39 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_40'] = x_get_cilium_flows__mutmut_40 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_41'] = x_get_cilium_flows__mutmut_41 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_42'] = x_get_cilium_flows__mutmut_42 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_43'] = x_get_cilium_flows__mutmut_43 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_44'] = x_get_cilium_flows__mutmut_44 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_45'] = x_get_cilium_flows__mutmut_45 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_46'] = x_get_cilium_flows__mutmut_46 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_47'] = x_get_cilium_flows__mutmut_47 # type: ignore # mutmut generated
mutants_x_get_cilium_flows__mutmut['x_get_cilium_flows__mutmut_48'] = x_get_cilium_flows__mutmut_48 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(get_cilium_flows)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(get_cilium_flows)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
