"""MCP tool: rollouts_detect."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.rollouts_detect.command import RolloutsDetectCommand
from hexawyn.application.use_case.workloads.rollouts_detect.rollouts_detect_use_case import (
    RolloutsDetectUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_rollouts_detect__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_rollouts_detect__mutmut)
def rollouts_detect() -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutsDetectUseCase(rollouts_port=build_rollouts_adapter())
        _ = use_case.execute(RolloutsDetectCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_rollouts_detect__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutsDetectUseCase(rollouts_port=build_rollouts_adapter())
        _ = use_case.execute(RolloutsDetectCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_rollouts_detect__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = None
        _ = use_case.execute(RolloutsDetectCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_rollouts_detect__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutsDetectUseCase(rollouts_port=None)
        _ = use_case.execute(RolloutsDetectCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_rollouts_detect__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutsDetectUseCase(rollouts_port=build_rollouts_adapter())
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_rollouts_detect__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutsDetectUseCase(rollouts_port=build_rollouts_adapter())
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_rollouts_detect__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutsDetectUseCase(rollouts_port=build_rollouts_adapter())
        _ = use_case.execute(RolloutsDetectCommand())
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_rollouts_detect__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutsDetectUseCase(rollouts_port=build_rollouts_adapter())
        _ = use_case.execute(RolloutsDetectCommand())
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_rollouts_detect__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutsDetectUseCase(rollouts_port=build_rollouts_adapter())
        _ = use_case.execute(RolloutsDetectCommand())
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_rollouts_detect__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutsDetectUseCase(rollouts_port=build_rollouts_adapter())
        _ = use_case.execute(RolloutsDetectCommand())
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_rollouts_detect__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = RolloutsDetectUseCase(rollouts_port=build_rollouts_adapter())
        _ = use_case.execute(RolloutsDetectCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_rollouts_detect__mutmut['_mutmut_orig'] = x_rollouts_detect__mutmut_orig # type: ignore # mutmut generated
mutants_x_rollouts_detect__mutmut['x_rollouts_detect__mutmut_1'] = x_rollouts_detect__mutmut_1 # type: ignore # mutmut generated
mutants_x_rollouts_detect__mutmut['x_rollouts_detect__mutmut_2'] = x_rollouts_detect__mutmut_2 # type: ignore # mutmut generated
mutants_x_rollouts_detect__mutmut['x_rollouts_detect__mutmut_3'] = x_rollouts_detect__mutmut_3 # type: ignore # mutmut generated
mutants_x_rollouts_detect__mutmut['x_rollouts_detect__mutmut_4'] = x_rollouts_detect__mutmut_4 # type: ignore # mutmut generated
mutants_x_rollouts_detect__mutmut['x_rollouts_detect__mutmut_5'] = x_rollouts_detect__mutmut_5 # type: ignore # mutmut generated
mutants_x_rollouts_detect__mutmut['x_rollouts_detect__mutmut_6'] = x_rollouts_detect__mutmut_6 # type: ignore # mutmut generated
mutants_x_rollouts_detect__mutmut['x_rollouts_detect__mutmut_7'] = x_rollouts_detect__mutmut_7 # type: ignore # mutmut generated
mutants_x_rollouts_detect__mutmut['x_rollouts_detect__mutmut_8'] = x_rollouts_detect__mutmut_8 # type: ignore # mutmut generated
mutants_x_rollouts_detect__mutmut['x_rollouts_detect__mutmut_9'] = x_rollouts_detect__mutmut_9 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(rollouts_detect)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(rollouts_detect)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
