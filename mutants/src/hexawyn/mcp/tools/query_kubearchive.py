"""MCP tool: query_kubearchive."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.query_kubearchive.command import (
    QueryKubearchiveCommand,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.query_kubearchive_use_case import (  # noqa: E501
    QueryKubeArchiveUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_query_kubearchive__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_query_kubearchive__mutmut)
def query_kubearchive(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = QueryKubeArchiveUseCase(kubearchive_port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(QueryKubearchiveCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_query_kubearchive__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = QueryKubeArchiveUseCase(kubearchive_port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(QueryKubearchiveCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_query_kubearchive__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = None  # type: ignore
        _ = use_case.execute(QueryKubearchiveCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_query_kubearchive__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = QueryKubeArchiveUseCase(kubearchive_port=None)  # type: ignore
        _ = use_case.execute(QueryKubearchiveCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_query_kubearchive__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = QueryKubeArchiveUseCase(kubearchive_port=build_k8s_adapter())  # type: ignore
        _ = None  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_query_kubearchive__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = QueryKubeArchiveUseCase(kubearchive_port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_query_kubearchive__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = QueryKubeArchiveUseCase(kubearchive_port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(QueryKubearchiveCommand())  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_query_kubearchive__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = QueryKubeArchiveUseCase(kubearchive_port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(QueryKubearchiveCommand())  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_query_kubearchive__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = QueryKubeArchiveUseCase(kubearchive_port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(QueryKubearchiveCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_query_kubearchive__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = QueryKubeArchiveUseCase(kubearchive_port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(QueryKubearchiveCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_query_kubearchive__mutmut_9(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = QueryKubeArchiveUseCase(kubearchive_port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(QueryKubearchiveCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_query_kubearchive__mutmut['_mutmut_orig'] = x_query_kubearchive__mutmut_orig # type: ignore # mutmut generated
mutants_x_query_kubearchive__mutmut['x_query_kubearchive__mutmut_1'] = x_query_kubearchive__mutmut_1 # type: ignore # mutmut generated
mutants_x_query_kubearchive__mutmut['x_query_kubearchive__mutmut_2'] = x_query_kubearchive__mutmut_2 # type: ignore # mutmut generated
mutants_x_query_kubearchive__mutmut['x_query_kubearchive__mutmut_3'] = x_query_kubearchive__mutmut_3 # type: ignore # mutmut generated
mutants_x_query_kubearchive__mutmut['x_query_kubearchive__mutmut_4'] = x_query_kubearchive__mutmut_4 # type: ignore # mutmut generated
mutants_x_query_kubearchive__mutmut['x_query_kubearchive__mutmut_5'] = x_query_kubearchive__mutmut_5 # type: ignore # mutmut generated
mutants_x_query_kubearchive__mutmut['x_query_kubearchive__mutmut_6'] = x_query_kubearchive__mutmut_6 # type: ignore # mutmut generated
mutants_x_query_kubearchive__mutmut['x_query_kubearchive__mutmut_7'] = x_query_kubearchive__mutmut_7 # type: ignore # mutmut generated
mutants_x_query_kubearchive__mutmut['x_query_kubearchive__mutmut_8'] = x_query_kubearchive__mutmut_8 # type: ignore # mutmut generated
mutants_x_query_kubearchive__mutmut['x_query_kubearchive__mutmut_9'] = x_query_kubearchive__mutmut_9 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(query_kubearchive)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(query_kubearchive)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
