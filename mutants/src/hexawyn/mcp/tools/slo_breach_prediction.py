# mypy: ignore-errors
"""MCP tool: slo_breach_prediction."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.slo_breach_prediction.command import (  # type: ignore
    SLOBreachPredictionCommand,
)
from hexawyn.application.use_case.workloads.slo_breach_prediction.slo_breach_prediction_use_case import (  # noqa: E501  # type: ignore  # type: ignore
    SLOBreachPredictionUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_slo_breach_prediction__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_slo_breach_prediction__mutmut)
def slo_breach_prediction(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = use_case.execute(
            SLOBreachPredictionCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_slo_breach_prediction__mutmut_orig(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = use_case.execute(
            SLOBreachPredictionCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_slo_breach_prediction__mutmut_1(prediction_window_minutes: str = "XXXX") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = use_case.execute(
            SLOBreachPredictionCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_slo_breach_prediction__mutmut_2(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = None
        _ = use_case.execute(
            SLOBreachPredictionCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_slo_breach_prediction__mutmut_3(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=None)
        _ = use_case.execute(
            SLOBreachPredictionCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_slo_breach_prediction__mutmut_4(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_slo_breach_prediction__mutmut_5(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = use_case.execute(
            None
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_slo_breach_prediction__mutmut_6(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = use_case.execute(
            SLOBreachPredictionCommand(prediction_window_minutes=None)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_slo_breach_prediction__mutmut_7(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = use_case.execute(
            SLOBreachPredictionCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_slo_breach_prediction__mutmut_8(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = use_case.execute(
            SLOBreachPredictionCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_slo_breach_prediction__mutmut_9(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = use_case.execute(
            SLOBreachPredictionCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_slo_breach_prediction__mutmut_10(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = use_case.execute(
            SLOBreachPredictionCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_slo_breach_prediction__mutmut_11(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = use_case.execute(
            SLOBreachPredictionCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_slo_breach_prediction__mutmut['_mutmut_orig'] = x_slo_breach_prediction__mutmut_orig # type: ignore # mutmut generated
mutants_x_slo_breach_prediction__mutmut['x_slo_breach_prediction__mutmut_1'] = x_slo_breach_prediction__mutmut_1 # type: ignore # mutmut generated
mutants_x_slo_breach_prediction__mutmut['x_slo_breach_prediction__mutmut_2'] = x_slo_breach_prediction__mutmut_2 # type: ignore # mutmut generated
mutants_x_slo_breach_prediction__mutmut['x_slo_breach_prediction__mutmut_3'] = x_slo_breach_prediction__mutmut_3 # type: ignore # mutmut generated
mutants_x_slo_breach_prediction__mutmut['x_slo_breach_prediction__mutmut_4'] = x_slo_breach_prediction__mutmut_4 # type: ignore # mutmut generated
mutants_x_slo_breach_prediction__mutmut['x_slo_breach_prediction__mutmut_5'] = x_slo_breach_prediction__mutmut_5 # type: ignore # mutmut generated
mutants_x_slo_breach_prediction__mutmut['x_slo_breach_prediction__mutmut_6'] = x_slo_breach_prediction__mutmut_6 # type: ignore # mutmut generated
mutants_x_slo_breach_prediction__mutmut['x_slo_breach_prediction__mutmut_7'] = x_slo_breach_prediction__mutmut_7 # type: ignore # mutmut generated
mutants_x_slo_breach_prediction__mutmut['x_slo_breach_prediction__mutmut_8'] = x_slo_breach_prediction__mutmut_8 # type: ignore # mutmut generated
mutants_x_slo_breach_prediction__mutmut['x_slo_breach_prediction__mutmut_9'] = x_slo_breach_prediction__mutmut_9 # type: ignore # mutmut generated
mutants_x_slo_breach_prediction__mutmut['x_slo_breach_prediction__mutmut_10'] = x_slo_breach_prediction__mutmut_10 # type: ignore # mutmut generated
mutants_x_slo_breach_prediction__mutmut['x_slo_breach_prediction__mutmut_11'] = x_slo_breach_prediction__mutmut_11 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(slo_breach_prediction)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(slo_breach_prediction)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
