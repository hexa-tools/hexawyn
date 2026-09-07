"""MCP tool: prometheus_query."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.prometheus_query.command import (
    PrometheusQueryCommand,
)
from hexawyn.application.use_case.observability.prometheus_query.prometheus_query_use_case import (
    PrometheusQueryUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_prometheus_query__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_prometheus_query__mutmut)
def prometheus_query(promql: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = PrometheusQueryUseCase(port=build_metrics_query_adapter())
        _ = use_case.execute(PrometheusQueryCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_prometheus_query__mutmut_orig(promql: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = PrometheusQueryUseCase(port=build_metrics_query_adapter())
        _ = use_case.execute(PrometheusQueryCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_prometheus_query__mutmut_1(promql: str = "XXXX") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = PrometheusQueryUseCase(port=build_metrics_query_adapter())
        _ = use_case.execute(PrometheusQueryCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_prometheus_query__mutmut_2(promql: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = None
        _ = use_case.execute(PrometheusQueryCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_prometheus_query__mutmut_3(promql: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = PrometheusQueryUseCase(port=None)
        _ = use_case.execute(PrometheusQueryCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_prometheus_query__mutmut_4(promql: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = PrometheusQueryUseCase(port=build_metrics_query_adapter())
        _ = None  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_prometheus_query__mutmut_5(promql: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = PrometheusQueryUseCase(port=build_metrics_query_adapter())
        _ = use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_prometheus_query__mutmut_6(promql: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = PrometheusQueryUseCase(port=build_metrics_query_adapter())
        _ = use_case.execute(PrometheusQueryCommand())  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_prometheus_query__mutmut_7(promql: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = PrometheusQueryUseCase(port=build_metrics_query_adapter())
        _ = use_case.execute(PrometheusQueryCommand())  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_prometheus_query__mutmut_8(promql: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = PrometheusQueryUseCase(port=build_metrics_query_adapter())
        _ = use_case.execute(PrometheusQueryCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_prometheus_query__mutmut_9(promql: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = PrometheusQueryUseCase(port=build_metrics_query_adapter())
        _ = use_case.execute(PrometheusQueryCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_prometheus_query__mutmut_10(promql: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = PrometheusQueryUseCase(port=build_metrics_query_adapter())
        _ = use_case.execute(PrometheusQueryCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_prometheus_query__mutmut['_mutmut_orig'] = x_prometheus_query__mutmut_orig # type: ignore # mutmut generated
mutants_x_prometheus_query__mutmut['x_prometheus_query__mutmut_1'] = x_prometheus_query__mutmut_1 # type: ignore # mutmut generated
mutants_x_prometheus_query__mutmut['x_prometheus_query__mutmut_2'] = x_prometheus_query__mutmut_2 # type: ignore # mutmut generated
mutants_x_prometheus_query__mutmut['x_prometheus_query__mutmut_3'] = x_prometheus_query__mutmut_3 # type: ignore # mutmut generated
mutants_x_prometheus_query__mutmut['x_prometheus_query__mutmut_4'] = x_prometheus_query__mutmut_4 # type: ignore # mutmut generated
mutants_x_prometheus_query__mutmut['x_prometheus_query__mutmut_5'] = x_prometheus_query__mutmut_5 # type: ignore # mutmut generated
mutants_x_prometheus_query__mutmut['x_prometheus_query__mutmut_6'] = x_prometheus_query__mutmut_6 # type: ignore # mutmut generated
mutants_x_prometheus_query__mutmut['x_prometheus_query__mutmut_7'] = x_prometheus_query__mutmut_7 # type: ignore # mutmut generated
mutants_x_prometheus_query__mutmut['x_prometheus_query__mutmut_8'] = x_prometheus_query__mutmut_8 # type: ignore # mutmut generated
mutants_x_prometheus_query__mutmut['x_prometheus_query__mutmut_9'] = x_prometheus_query__mutmut_9 # type: ignore # mutmut generated
mutants_x_prometheus_query__mutmut['x_prometheus_query__mutmut_10'] = x_prometheus_query__mutmut_10 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(prometheus_query)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(prometheus_query)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
