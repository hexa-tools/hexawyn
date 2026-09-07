"""MCP tool: analyze_failed_pipeline — Analyze a failed pipeline run."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.analyze_failed_pipeline_use_case import (  # noqa: E501
    AnalyzeFailedPipelineUseCase,
)
from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.command import (
    AnalyzeFailedPipelineCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_analyze_failed_pipeline__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_analyze_failed_pipeline__mutmut)
def analyze_failed_pipeline(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_orig(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_1(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = None  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_2(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=None)  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_3(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = None
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_4(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(None)
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_5(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=None))
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_6(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"XXanalysisXX": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_7(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"ANALYSIS": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_8(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "XXerrorXX": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_9(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "ERROR": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_10(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"XXanalysisXX": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_11(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"ANALYSIS": "", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_12(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "XXXX", "error": str(exc)}


def x_analyze_failed_pipeline__mutmut_13(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "XXerrorXX": str(exc)}


def x_analyze_failed_pipeline__mutmut_14(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "ERROR": str(exc)}


def x_analyze_failed_pipeline__mutmut_15(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(None)}

mutants_x_analyze_failed_pipeline__mutmut['_mutmut_orig'] = x_analyze_failed_pipeline__mutmut_orig # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_1'] = x_analyze_failed_pipeline__mutmut_1 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_2'] = x_analyze_failed_pipeline__mutmut_2 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_3'] = x_analyze_failed_pipeline__mutmut_3 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_4'] = x_analyze_failed_pipeline__mutmut_4 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_5'] = x_analyze_failed_pipeline__mutmut_5 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_6'] = x_analyze_failed_pipeline__mutmut_6 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_7'] = x_analyze_failed_pipeline__mutmut_7 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_8'] = x_analyze_failed_pipeline__mutmut_8 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_9'] = x_analyze_failed_pipeline__mutmut_9 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_10'] = x_analyze_failed_pipeline__mutmut_10 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_11'] = x_analyze_failed_pipeline__mutmut_11 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_12'] = x_analyze_failed_pipeline__mutmut_12 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_13'] = x_analyze_failed_pipeline__mutmut_13 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_14'] = x_analyze_failed_pipeline__mutmut_14 # type: ignore # mutmut generated
mutants_x_analyze_failed_pipeline__mutmut['x_analyze_failed_pipeline__mutmut_15'] = x_analyze_failed_pipeline__mutmut_15 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(analyze_failed_pipeline)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(analyze_failed_pipeline)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
