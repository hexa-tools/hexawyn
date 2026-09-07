# mypy: ignore-errors
"""MCP tool: search_resources_by_labels."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.search_resources_by_labels.command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.use_case.cluster.search_resources_by_labels.search_resources_by_labels_use_case import (  # noqa: E501
    SearchResourcesByLabelsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_search_resources_by_labels__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_search_resources_by_labels__mutmut)
def search_resources_by_labels(label_selector: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(SearchResourcesByLabelsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_search_resources_by_labels__mutmut_orig(label_selector: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(SearchResourcesByLabelsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_search_resources_by_labels__mutmut_1(label_selector: str = "XXtestXX") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(SearchResourcesByLabelsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_search_resources_by_labels__mutmut_2(label_selector: str = "TEST") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(SearchResourcesByLabelsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_search_resources_by_labels__mutmut_3(label_selector: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = None  # type: ignore
        _ = use_case.execute(SearchResourcesByLabelsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_search_resources_by_labels__mutmut_4(label_selector: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=None)  # type: ignore
        _ = use_case.execute(SearchResourcesByLabelsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_search_resources_by_labels__mutmut_5(label_selector: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_search_resources_by_labels__mutmut_6(label_selector: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_search_resources_by_labels__mutmut_7(label_selector: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(SearchResourcesByLabelsCommand())
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_search_resources_by_labels__mutmut_8(label_selector: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(SearchResourcesByLabelsCommand())
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_search_resources_by_labels__mutmut_9(label_selector: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(SearchResourcesByLabelsCommand())
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_search_resources_by_labels__mutmut_10(label_selector: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(SearchResourcesByLabelsCommand())
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_search_resources_by_labels__mutmut_11(label_selector: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = SearchResourcesByLabelsUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(SearchResourcesByLabelsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_search_resources_by_labels__mutmut['_mutmut_orig'] = x_search_resources_by_labels__mutmut_orig # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_1'] = x_search_resources_by_labels__mutmut_1 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_2'] = x_search_resources_by_labels__mutmut_2 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_3'] = x_search_resources_by_labels__mutmut_3 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_4'] = x_search_resources_by_labels__mutmut_4 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_5'] = x_search_resources_by_labels__mutmut_5 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_6'] = x_search_resources_by_labels__mutmut_6 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_7'] = x_search_resources_by_labels__mutmut_7 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_8'] = x_search_resources_by_labels__mutmut_8 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_9'] = x_search_resources_by_labels__mutmut_9 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_10'] = x_search_resources_by_labels__mutmut_10 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_11'] = x_search_resources_by_labels__mutmut_11 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(search_resources_by_labels)


def x_register__mutmut_orig(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(search_resources_by_labels)


def x_register__mutmut_1(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
