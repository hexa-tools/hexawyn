"""MCP tool: detect_missing_probes."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.detect_missing_probes.command import (
    DetectMissingProbesCommand,
)
from hexawyn.application.use_case.security.detect_missing_probes.detect_missing_probes_use_case import (  # noqa: E501
    DetectMissingProbesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_missing_probes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_missing_probes__mutmut)
def detect_missing_probes() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = DetectMissingProbesUseCase(port=build_optimization_roi_adapter())  # type: ignore
        _ = use_case.execute(DetectMissingProbesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_missing_probes__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = DetectMissingProbesUseCase(port=build_optimization_roi_adapter())  # type: ignore
        _ = use_case.execute(DetectMissingProbesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_missing_probes__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = None  # type: ignore
        _ = use_case.execute(DetectMissingProbesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_missing_probes__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = DetectMissingProbesUseCase(port=None)  # type: ignore
        _ = use_case.execute(DetectMissingProbesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_missing_probes__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = DetectMissingProbesUseCase(port=build_optimization_roi_adapter())  # type: ignore
        _ = None  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_missing_probes__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = DetectMissingProbesUseCase(port=build_optimization_roi_adapter())  # type: ignore
        _ = use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_missing_probes__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = DetectMissingProbesUseCase(port=build_optimization_roi_adapter())  # type: ignore
        _ = use_case.execute(DetectMissingProbesCommand())  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_missing_probes__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = DetectMissingProbesUseCase(port=build_optimization_roi_adapter())  # type: ignore
        _ = use_case.execute(DetectMissingProbesCommand())  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_missing_probes__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = DetectMissingProbesUseCase(port=build_optimization_roi_adapter())  # type: ignore
        _ = use_case.execute(DetectMissingProbesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_detect_missing_probes__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = DetectMissingProbesUseCase(port=build_optimization_roi_adapter())  # type: ignore
        _ = use_case.execute(DetectMissingProbesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_detect_missing_probes__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = DetectMissingProbesUseCase(port=build_optimization_roi_adapter())  # type: ignore
        _ = use_case.execute(DetectMissingProbesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_detect_missing_probes__mutmut['_mutmut_orig'] = x_detect_missing_probes__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_missing_probes__mutmut['x_detect_missing_probes__mutmut_1'] = x_detect_missing_probes__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_missing_probes__mutmut['x_detect_missing_probes__mutmut_2'] = x_detect_missing_probes__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_missing_probes__mutmut['x_detect_missing_probes__mutmut_3'] = x_detect_missing_probes__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_missing_probes__mutmut['x_detect_missing_probes__mutmut_4'] = x_detect_missing_probes__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_missing_probes__mutmut['x_detect_missing_probes__mutmut_5'] = x_detect_missing_probes__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_missing_probes__mutmut['x_detect_missing_probes__mutmut_6'] = x_detect_missing_probes__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_missing_probes__mutmut['x_detect_missing_probes__mutmut_7'] = x_detect_missing_probes__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_missing_probes__mutmut['x_detect_missing_probes__mutmut_8'] = x_detect_missing_probes__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_missing_probes__mutmut['x_detect_missing_probes__mutmut_9'] = x_detect_missing_probes__mutmut_9 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_missing_probes)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(detect_missing_probes)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
