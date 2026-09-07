# mypy: ignore-errors
"""MCP tool: slowest_traces — Find the slowest OTel traces for a pod."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.slowest_traces.command import (
    SlowestTracesCommand,
)
from hexawyn.application.use_case.observability.slowest_traces.slowest_traces_use_case import (
    SlowestTracesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_slowest_traces__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_slowest_traces__mutmut)
def slowest_traces(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_orig(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_1(
    pod_name: str, time_window_minutes: int = 61, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_2(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 6
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_3(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = None
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_4(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = None
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_5(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            None
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_6(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=None).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_7(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=None,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_8(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=None,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_9(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=None,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_10(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_11(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_12(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_13(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "XXpod_nameXX": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_14(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "POD_NAME": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_15(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "XXslowest_tracesXX": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_16(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "SLOWEST_TRACES": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_17(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "XXtotal_traces_foundXX": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_18(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "TOTAL_TRACES_FOUND": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_19(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "XXnoteXX": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_20(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "NOTE": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_21(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_22(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_23(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXpod_nameXX": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_24(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"POD_NAME": pod_name, "error": str(exc)}


def x_slowest_traces__mutmut_25(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "XXerrorXX": str(exc)}


def x_slowest_traces__mutmut_26(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "ERROR": str(exc)}


def x_slowest_traces__mutmut_27(
    pod_name: str, time_window_minutes: int = 60, top_n: int = 5
) -> dict[str, object]:
    from hexawyn.mcp.server import build_slow_trace_search_adapter

    try:
        a = build_slow_trace_search_adapter()
        r = SlowestTracesUseCase(port=a).execute(
            SlowestTracesCommand(
                pod_name=pod_name,
                time_window_minutes=time_window_minutes,
                top_n=top_n,  # type: ignore
            )
        )
        return {
            "pod_name": r.pod_name,
            "slowest_traces": r.slowest_traces,
            "total_traces_found": r.total_traces_found,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"pod_name": pod_name, "error": str(None)}

mutants_x_slowest_traces__mutmut['_mutmut_orig'] = x_slowest_traces__mutmut_orig # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_1'] = x_slowest_traces__mutmut_1 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_2'] = x_slowest_traces__mutmut_2 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_3'] = x_slowest_traces__mutmut_3 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_4'] = x_slowest_traces__mutmut_4 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_5'] = x_slowest_traces__mutmut_5 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_6'] = x_slowest_traces__mutmut_6 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_7'] = x_slowest_traces__mutmut_7 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_8'] = x_slowest_traces__mutmut_8 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_9'] = x_slowest_traces__mutmut_9 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_10'] = x_slowest_traces__mutmut_10 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_11'] = x_slowest_traces__mutmut_11 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_12'] = x_slowest_traces__mutmut_12 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_13'] = x_slowest_traces__mutmut_13 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_14'] = x_slowest_traces__mutmut_14 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_15'] = x_slowest_traces__mutmut_15 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_16'] = x_slowest_traces__mutmut_16 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_17'] = x_slowest_traces__mutmut_17 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_18'] = x_slowest_traces__mutmut_18 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_19'] = x_slowest_traces__mutmut_19 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_20'] = x_slowest_traces__mutmut_20 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_21'] = x_slowest_traces__mutmut_21 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_22'] = x_slowest_traces__mutmut_22 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_23'] = x_slowest_traces__mutmut_23 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_24'] = x_slowest_traces__mutmut_24 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_25'] = x_slowest_traces__mutmut_25 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_26'] = x_slowest_traces__mutmut_26 # type: ignore # mutmut generated
mutants_x_slowest_traces__mutmut['x_slowest_traces__mutmut_27'] = x_slowest_traces__mutmut_27 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(slowest_traces)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(slowest_traces)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
