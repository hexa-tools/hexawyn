"""MCP tool: cost_profiling — Identify the most CPU-intensive HTTP endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.cost_profiling.command import (
    CostProfilingCommand,
)
from hexawyn.application.use_case.finops.cost_profiling.cost_profiling_use_case import (
    CostProfilingUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_cost_profiling__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_cost_profiling__mutmut)
def cost_profiling(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_orig(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_1(time_window_minutes: int = 61, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_2(time_window_minutes: int = 60, top_n: int = 6) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_3(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = None
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_4(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = None
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_5(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            None
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_6(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=None).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_7(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=None, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_8(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=None)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_9(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_10(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, )
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_11(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "XXtime_window_minutesXX": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_12(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "TIME_WINDOW_MINUTES": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_13(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "XXranked_endpointsXX": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_14(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "RANKED_ENDPOINTS": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_15(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "XXoptimisation_candidatesXX": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_16(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "OPTIMISATION_CANDIDATES": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_17(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_18(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_19(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXranked_endpointsXX": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_20(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"RANKED_ENDPOINTS": [], "optimisation_candidates": [], "error": str(exc)}


def x_cost_profiling__mutmut_21(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "XXoptimisation_candidatesXX": [], "error": str(exc)}


def x_cost_profiling__mutmut_22(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "OPTIMISATION_CANDIDATES": [], "error": str(exc)}


def x_cost_profiling__mutmut_23(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "XXerrorXX": str(exc)}


def x_cost_profiling__mutmut_24(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "ERROR": str(exc)}


def x_cost_profiling__mutmut_25(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(port=a).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(None)}

mutants_x_cost_profiling__mutmut['_mutmut_orig'] = x_cost_profiling__mutmut_orig # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_1'] = x_cost_profiling__mutmut_1 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_2'] = x_cost_profiling__mutmut_2 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_3'] = x_cost_profiling__mutmut_3 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_4'] = x_cost_profiling__mutmut_4 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_5'] = x_cost_profiling__mutmut_5 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_6'] = x_cost_profiling__mutmut_6 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_7'] = x_cost_profiling__mutmut_7 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_8'] = x_cost_profiling__mutmut_8 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_9'] = x_cost_profiling__mutmut_9 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_10'] = x_cost_profiling__mutmut_10 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_11'] = x_cost_profiling__mutmut_11 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_12'] = x_cost_profiling__mutmut_12 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_13'] = x_cost_profiling__mutmut_13 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_14'] = x_cost_profiling__mutmut_14 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_15'] = x_cost_profiling__mutmut_15 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_16'] = x_cost_profiling__mutmut_16 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_17'] = x_cost_profiling__mutmut_17 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_18'] = x_cost_profiling__mutmut_18 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_19'] = x_cost_profiling__mutmut_19 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_20'] = x_cost_profiling__mutmut_20 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_21'] = x_cost_profiling__mutmut_21 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_22'] = x_cost_profiling__mutmut_22 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_23'] = x_cost_profiling__mutmut_23 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_24'] = x_cost_profiling__mutmut_24 # type: ignore # mutmut generated
mutants_x_cost_profiling__mutmut['x_cost_profiling__mutmut_25'] = x_cost_profiling__mutmut_25 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(cost_profiling)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(cost_profiling)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
