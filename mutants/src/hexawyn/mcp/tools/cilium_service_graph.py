"""MCP tool: cilium_service_graph — build a service graph from Cilium flows."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.cilium_service_graph.cilium_service_graph_use_case import (
    CiliumServiceGraphUseCase,
)
from hexawyn.application.use_case.cilium.cilium_service_graph.command import (
    CiliumServiceGraphCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_cilium_service_graph__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_cilium_service_graph__mutmut)
def cilium_service_graph(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_orig(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_1(time_window_minutes: int = 61) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_2(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = None
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_3(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = None
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_4(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=None)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_5(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = None
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_6(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            None
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_7(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=None)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_8(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "XXtime_window_minutesXX": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_9(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "TIME_WINDOW_MINUTES": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_10(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "XXnodesXX": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_11(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "NODES": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_12(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "XXedgesXX": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_13(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "EDGES": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_14(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "XXnoteXX": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_15(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "NOTE": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_16(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_17(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_18(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXtime_window_minutesXX": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_19(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "TIME_WINDOW_MINUTES": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_20(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "XXnodesXX": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_21(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "NODES": [],
            "edges": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_22(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "XXedgesXX": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_23(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "EDGES": [],
            "note": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_24(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "XXnoteXX": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_25(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "NOTE": None,
            "error": str(exc),
        }


def x_cilium_service_graph__mutmut_26(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "XXerrorXX": str(exc),
        }


def x_cilium_service_graph__mutmut_27(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "ERROR": str(exc),
        }


def x_cilium_service_graph__mutmut_28(time_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_service_graph_adapter

    try:
        adapter = build_cilium_service_graph_adapter()
        use_case = CiliumServiceGraphUseCase(port=adapter)
        result = use_case.execute(
            CiliumServiceGraphCommand(time_window_minutes=time_window_minutes)
        )
        return {
            "time_window_minutes": result.time_window_minutes,
            "nodes": result.nodes,
            "edges": result.edges,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "time_window_minutes": time_window_minutes,
            "nodes": [],
            "edges": [],
            "note": None,
            "error": str(None),
        }

mutants_x_cilium_service_graph__mutmut['_mutmut_orig'] = x_cilium_service_graph__mutmut_orig # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_1'] = x_cilium_service_graph__mutmut_1 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_2'] = x_cilium_service_graph__mutmut_2 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_3'] = x_cilium_service_graph__mutmut_3 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_4'] = x_cilium_service_graph__mutmut_4 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_5'] = x_cilium_service_graph__mutmut_5 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_6'] = x_cilium_service_graph__mutmut_6 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_7'] = x_cilium_service_graph__mutmut_7 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_8'] = x_cilium_service_graph__mutmut_8 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_9'] = x_cilium_service_graph__mutmut_9 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_10'] = x_cilium_service_graph__mutmut_10 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_11'] = x_cilium_service_graph__mutmut_11 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_12'] = x_cilium_service_graph__mutmut_12 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_13'] = x_cilium_service_graph__mutmut_13 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_14'] = x_cilium_service_graph__mutmut_14 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_15'] = x_cilium_service_graph__mutmut_15 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_16'] = x_cilium_service_graph__mutmut_16 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_17'] = x_cilium_service_graph__mutmut_17 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_18'] = x_cilium_service_graph__mutmut_18 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_19'] = x_cilium_service_graph__mutmut_19 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_20'] = x_cilium_service_graph__mutmut_20 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_21'] = x_cilium_service_graph__mutmut_21 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_22'] = x_cilium_service_graph__mutmut_22 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_23'] = x_cilium_service_graph__mutmut_23 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_24'] = x_cilium_service_graph__mutmut_24 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_25'] = x_cilium_service_graph__mutmut_25 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_26'] = x_cilium_service_graph__mutmut_26 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_27'] = x_cilium_service_graph__mutmut_27 # type: ignore # mutmut generated
mutants_x_cilium_service_graph__mutmut['x_cilium_service_graph__mutmut_28'] = x_cilium_service_graph__mutmut_28 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(cilium_service_graph)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(cilium_service_graph)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
