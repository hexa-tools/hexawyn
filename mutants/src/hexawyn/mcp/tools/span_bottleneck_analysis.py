"""MCP tool: span_bottleneck_analysis."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.span_bottleneck_analysis.command import (
    SpanBottleneckAnalysisCommand,
)
from hexawyn.application.use_case.observability.span_bottleneck_analysis.span_bottleneck_analysis_use_case import (  # noqa: E501
    SpanBottleneckAnalysisUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_span_bottleneck_analysis__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_span_bottleneck_analysis__mutmut)
def span_bottleneck_analysis() -> dict[str, object]:
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        use_case = SpanBottleneckAnalysisUseCase(port=build_span_bottleneck_adapter())
        _ = use_case.execute(SpanBottleneckAnalysisCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_span_bottleneck_analysis__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        use_case = SpanBottleneckAnalysisUseCase(port=build_span_bottleneck_adapter())
        _ = use_case.execute(SpanBottleneckAnalysisCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_span_bottleneck_analysis__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        use_case = None
        _ = use_case.execute(SpanBottleneckAnalysisCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_span_bottleneck_analysis__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        use_case = SpanBottleneckAnalysisUseCase(port=None)
        _ = use_case.execute(SpanBottleneckAnalysisCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_span_bottleneck_analysis__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        use_case = SpanBottleneckAnalysisUseCase(port=build_span_bottleneck_adapter())
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_span_bottleneck_analysis__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        use_case = SpanBottleneckAnalysisUseCase(port=build_span_bottleneck_adapter())
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_span_bottleneck_analysis__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        use_case = SpanBottleneckAnalysisUseCase(port=build_span_bottleneck_adapter())
        _ = use_case.execute(SpanBottleneckAnalysisCommand())
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_span_bottleneck_analysis__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        use_case = SpanBottleneckAnalysisUseCase(port=build_span_bottleneck_adapter())
        _ = use_case.execute(SpanBottleneckAnalysisCommand())
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_span_bottleneck_analysis__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        use_case = SpanBottleneckAnalysisUseCase(port=build_span_bottleneck_adapter())
        _ = use_case.execute(SpanBottleneckAnalysisCommand())
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_span_bottleneck_analysis__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        use_case = SpanBottleneckAnalysisUseCase(port=build_span_bottleneck_adapter())
        _ = use_case.execute(SpanBottleneckAnalysisCommand())
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_span_bottleneck_analysis__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_span_bottleneck_adapter

    try:
        use_case = SpanBottleneckAnalysisUseCase(port=build_span_bottleneck_adapter())
        _ = use_case.execute(SpanBottleneckAnalysisCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_span_bottleneck_analysis__mutmut['_mutmut_orig'] = x_span_bottleneck_analysis__mutmut_orig # type: ignore # mutmut generated
mutants_x_span_bottleneck_analysis__mutmut['x_span_bottleneck_analysis__mutmut_1'] = x_span_bottleneck_analysis__mutmut_1 # type: ignore # mutmut generated
mutants_x_span_bottleneck_analysis__mutmut['x_span_bottleneck_analysis__mutmut_2'] = x_span_bottleneck_analysis__mutmut_2 # type: ignore # mutmut generated
mutants_x_span_bottleneck_analysis__mutmut['x_span_bottleneck_analysis__mutmut_3'] = x_span_bottleneck_analysis__mutmut_3 # type: ignore # mutmut generated
mutants_x_span_bottleneck_analysis__mutmut['x_span_bottleneck_analysis__mutmut_4'] = x_span_bottleneck_analysis__mutmut_4 # type: ignore # mutmut generated
mutants_x_span_bottleneck_analysis__mutmut['x_span_bottleneck_analysis__mutmut_5'] = x_span_bottleneck_analysis__mutmut_5 # type: ignore # mutmut generated
mutants_x_span_bottleneck_analysis__mutmut['x_span_bottleneck_analysis__mutmut_6'] = x_span_bottleneck_analysis__mutmut_6 # type: ignore # mutmut generated
mutants_x_span_bottleneck_analysis__mutmut['x_span_bottleneck_analysis__mutmut_7'] = x_span_bottleneck_analysis__mutmut_7 # type: ignore # mutmut generated
mutants_x_span_bottleneck_analysis__mutmut['x_span_bottleneck_analysis__mutmut_8'] = x_span_bottleneck_analysis__mutmut_8 # type: ignore # mutmut generated
mutants_x_span_bottleneck_analysis__mutmut['x_span_bottleneck_analysis__mutmut_9'] = x_span_bottleneck_analysis__mutmut_9 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(span_bottleneck_analysis)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(span_bottleneck_analysis)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
