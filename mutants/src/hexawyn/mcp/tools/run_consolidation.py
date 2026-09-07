"""MCP tool: run_consolidation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.run_consolidation.command import RunConsolidationCommand
from hexawyn.application.use_case.cluster.run_consolidation.run_consolidation_use_case import (
    RunConsolidationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_run_consolidation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_run_consolidation__mutmut)
def run_consolidation() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=build_consolidation_adapter())
        use_case = RunConsolidationUseCase(service=service)  # type: ignore
        _ = use_case.execute(RunConsolidationCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_run_consolidation__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=build_consolidation_adapter())
        use_case = RunConsolidationUseCase(service=service)  # type: ignore
        _ = use_case.execute(RunConsolidationCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_run_consolidation__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = None
        use_case = RunConsolidationUseCase(service=service)  # type: ignore
        _ = use_case.execute(RunConsolidationCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_run_consolidation__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=None)
        use_case = RunConsolidationUseCase(service=service)  # type: ignore
        _ = use_case.execute(RunConsolidationCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_run_consolidation__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=build_consolidation_adapter())
        use_case = None  # type: ignore
        _ = use_case.execute(RunConsolidationCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_run_consolidation__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=build_consolidation_adapter())
        use_case = RunConsolidationUseCase(service=None)  # type: ignore
        _ = use_case.execute(RunConsolidationCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_run_consolidation__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=build_consolidation_adapter())
        use_case = RunConsolidationUseCase(service=service)  # type: ignore
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_run_consolidation__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=build_consolidation_adapter())
        use_case = RunConsolidationUseCase(service=service)  # type: ignore
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_run_consolidation__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=build_consolidation_adapter())
        use_case = RunConsolidationUseCase(service=service)  # type: ignore
        _ = use_case.execute(RunConsolidationCommand())
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_run_consolidation__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=build_consolidation_adapter())
        use_case = RunConsolidationUseCase(service=service)  # type: ignore
        _ = use_case.execute(RunConsolidationCommand())
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_run_consolidation__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=build_consolidation_adapter())
        use_case = RunConsolidationUseCase(service=service)  # type: ignore
        _ = use_case.execute(RunConsolidationCommand())
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_run_consolidation__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=build_consolidation_adapter())
        use_case = RunConsolidationUseCase(service=service)  # type: ignore
        _ = use_case.execute(RunConsolidationCommand())
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_run_consolidation__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=build_consolidation_adapter())
        use_case = RunConsolidationUseCase(service=service)  # type: ignore
        _ = use_case.execute(RunConsolidationCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_run_consolidation__mutmut['_mutmut_orig'] = x_run_consolidation__mutmut_orig # type: ignore # mutmut generated
mutants_x_run_consolidation__mutmut['x_run_consolidation__mutmut_1'] = x_run_consolidation__mutmut_1 # type: ignore # mutmut generated
mutants_x_run_consolidation__mutmut['x_run_consolidation__mutmut_2'] = x_run_consolidation__mutmut_2 # type: ignore # mutmut generated
mutants_x_run_consolidation__mutmut['x_run_consolidation__mutmut_3'] = x_run_consolidation__mutmut_3 # type: ignore # mutmut generated
mutants_x_run_consolidation__mutmut['x_run_consolidation__mutmut_4'] = x_run_consolidation__mutmut_4 # type: ignore # mutmut generated
mutants_x_run_consolidation__mutmut['x_run_consolidation__mutmut_5'] = x_run_consolidation__mutmut_5 # type: ignore # mutmut generated
mutants_x_run_consolidation__mutmut['x_run_consolidation__mutmut_6'] = x_run_consolidation__mutmut_6 # type: ignore # mutmut generated
mutants_x_run_consolidation__mutmut['x_run_consolidation__mutmut_7'] = x_run_consolidation__mutmut_7 # type: ignore # mutmut generated
mutants_x_run_consolidation__mutmut['x_run_consolidation__mutmut_8'] = x_run_consolidation__mutmut_8 # type: ignore # mutmut generated
mutants_x_run_consolidation__mutmut['x_run_consolidation__mutmut_9'] = x_run_consolidation__mutmut_9 # type: ignore # mutmut generated
mutants_x_run_consolidation__mutmut['x_run_consolidation__mutmut_10'] = x_run_consolidation__mutmut_10 # type: ignore # mutmut generated
mutants_x_run_consolidation__mutmut['x_run_consolidation__mutmut_11'] = x_run_consolidation__mutmut_11 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(run_consolidation)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(run_consolidation)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
