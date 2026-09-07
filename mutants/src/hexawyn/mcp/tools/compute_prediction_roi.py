# mypy: ignore-errors
"""MCP tool: compute_prediction_roi."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.compute_prediction_roi.command import (
    ComputePredictionRoiCommand,
)
from hexawyn.application.use_case.finops.compute_prediction_roi.compute_prediction_roi_use_case import (  # noqa: E501
    ComputePredictionRoiUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_prediction_roi__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_prediction_roi__mutmut)
def compute_prediction_roi(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_prediction_roi__mutmut_orig(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_prediction_roi__mutmut_1(period: str = "XXtestXX") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_prediction_roi__mutmut_2(period: str = "TEST") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_prediction_roi__mutmut_3(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = None  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_prediction_roi__mutmut_4(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=None)  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_prediction_roi__mutmut_5(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = None  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_prediction_roi__mutmut_6(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=None)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_prediction_roi__mutmut_7(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = None  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_prediction_roi__mutmut_8(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_prediction_roi__mutmut_9(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_prediction_roi__mutmut_10(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_prediction_roi__mutmut_11(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_compute_prediction_roi__mutmut_12(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_compute_prediction_roi__mutmut_13(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_compute_prediction_roi__mutmut['_mutmut_orig'] = x_compute_prediction_roi__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_1'] = x_compute_prediction_roi__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_2'] = x_compute_prediction_roi__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_3'] = x_compute_prediction_roi__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_4'] = x_compute_prediction_roi__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_5'] = x_compute_prediction_roi__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_6'] = x_compute_prediction_roi__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_7'] = x_compute_prediction_roi__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_8'] = x_compute_prediction_roi__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_9'] = x_compute_prediction_roi__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_10'] = x_compute_prediction_roi__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_11'] = x_compute_prediction_roi__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_12'] = x_compute_prediction_roi__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_13'] = x_compute_prediction_roi__mutmut_13 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(compute_prediction_roi)


def x_register__mutmut_orig(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(compute_prediction_roi)


def x_register__mutmut_1(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
