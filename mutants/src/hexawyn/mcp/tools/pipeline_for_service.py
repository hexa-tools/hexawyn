# mypy: ignore-errors
"""MCP tool: pipeline_for_service."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.pipeline_for_service.command import (
    PipelineForServiceCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_for_service.pipeline_for_service_use_case import (  # noqa: E501  # type: ignore  # type: ignore
    PipelineForUseCaseUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_pipeline_for_service__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_pipeline_for_service__mutmut)
def pipeline_for_service(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = PipelineForUseCaseUseCase(port=build_pipeline_for_service_adapter())
        _ = use_case.execute(PipelineForServiceCommand(service_name=service_name))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_pipeline_for_service__mutmut_orig(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = PipelineForUseCaseUseCase(port=build_pipeline_for_service_adapter())
        _ = use_case.execute(PipelineForServiceCommand(service_name=service_name))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_pipeline_for_service__mutmut_1(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = None
        _ = use_case.execute(PipelineForServiceCommand(service_name=service_name))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_pipeline_for_service__mutmut_2(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = PipelineForUseCaseUseCase(port=None)
        _ = use_case.execute(PipelineForServiceCommand(service_name=service_name))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_pipeline_for_service__mutmut_3(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = PipelineForUseCaseUseCase(port=build_pipeline_for_service_adapter())
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_pipeline_for_service__mutmut_4(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = PipelineForUseCaseUseCase(port=build_pipeline_for_service_adapter())
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_pipeline_for_service__mutmut_5(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = PipelineForUseCaseUseCase(port=build_pipeline_for_service_adapter())
        _ = use_case.execute(PipelineForServiceCommand(service_name=None))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_pipeline_for_service__mutmut_6(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = PipelineForUseCaseUseCase(port=build_pipeline_for_service_adapter())
        _ = use_case.execute(PipelineForServiceCommand(service_name=service_name))
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_pipeline_for_service__mutmut_7(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = PipelineForUseCaseUseCase(port=build_pipeline_for_service_adapter())
        _ = use_case.execute(PipelineForServiceCommand(service_name=service_name))
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_pipeline_for_service__mutmut_8(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = PipelineForUseCaseUseCase(port=build_pipeline_for_service_adapter())
        _ = use_case.execute(PipelineForServiceCommand(service_name=service_name))
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_pipeline_for_service__mutmut_9(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = PipelineForUseCaseUseCase(port=build_pipeline_for_service_adapter())
        _ = use_case.execute(PipelineForServiceCommand(service_name=service_name))
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_pipeline_for_service__mutmut_10(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = PipelineForUseCaseUseCase(port=build_pipeline_for_service_adapter())
        _ = use_case.execute(PipelineForServiceCommand(service_name=service_name))
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_pipeline_for_service__mutmut['_mutmut_orig'] = x_pipeline_for_service__mutmut_orig # type: ignore # mutmut generated
mutants_x_pipeline_for_service__mutmut['x_pipeline_for_service__mutmut_1'] = x_pipeline_for_service__mutmut_1 # type: ignore # mutmut generated
mutants_x_pipeline_for_service__mutmut['x_pipeline_for_service__mutmut_2'] = x_pipeline_for_service__mutmut_2 # type: ignore # mutmut generated
mutants_x_pipeline_for_service__mutmut['x_pipeline_for_service__mutmut_3'] = x_pipeline_for_service__mutmut_3 # type: ignore # mutmut generated
mutants_x_pipeline_for_service__mutmut['x_pipeline_for_service__mutmut_4'] = x_pipeline_for_service__mutmut_4 # type: ignore # mutmut generated
mutants_x_pipeline_for_service__mutmut['x_pipeline_for_service__mutmut_5'] = x_pipeline_for_service__mutmut_5 # type: ignore # mutmut generated
mutants_x_pipeline_for_service__mutmut['x_pipeline_for_service__mutmut_6'] = x_pipeline_for_service__mutmut_6 # type: ignore # mutmut generated
mutants_x_pipeline_for_service__mutmut['x_pipeline_for_service__mutmut_7'] = x_pipeline_for_service__mutmut_7 # type: ignore # mutmut generated
mutants_x_pipeline_for_service__mutmut['x_pipeline_for_service__mutmut_8'] = x_pipeline_for_service__mutmut_8 # type: ignore # mutmut generated
mutants_x_pipeline_for_service__mutmut['x_pipeline_for_service__mutmut_9'] = x_pipeline_for_service__mutmut_9 # type: ignore # mutmut generated
mutants_x_pipeline_for_service__mutmut['x_pipeline_for_service__mutmut_10'] = x_pipeline_for_service__mutmut_10 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(pipeline_for_service)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(pipeline_for_service)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
