"""MCP tool: gitops_sources_list."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.gitops_sources_list.command import GitopsSourcesListCommand
from hexawyn.application.use_case.gitops.gitops_sources_list.gitops_sources_list_use_case import (
    GitopsSourcesListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_gitops_sources_list__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_gitops_sources_list__mutmut)
def gitops_sources_list() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourcesListUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsSourcesListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_sources_list__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourcesListUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsSourcesListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_sources_list__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = None
        _ = use_case.execute(GitopsSourcesListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_sources_list__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourcesListUseCase(gitops_port=None)
        _ = use_case.execute(GitopsSourcesListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_sources_list__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourcesListUseCase(gitops_port=build_gitops_adapter())
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_sources_list__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourcesListUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_sources_list__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourcesListUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsSourcesListCommand())
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_sources_list__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourcesListUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsSourcesListCommand())
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_sources_list__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourcesListUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsSourcesListCommand())
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_gitops_sources_list__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourcesListUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsSourcesListCommand())
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_gitops_sources_list__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsSourcesListUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsSourcesListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_gitops_sources_list__mutmut['_mutmut_orig'] = x_gitops_sources_list__mutmut_orig # type: ignore # mutmut generated
mutants_x_gitops_sources_list__mutmut['x_gitops_sources_list__mutmut_1'] = x_gitops_sources_list__mutmut_1 # type: ignore # mutmut generated
mutants_x_gitops_sources_list__mutmut['x_gitops_sources_list__mutmut_2'] = x_gitops_sources_list__mutmut_2 # type: ignore # mutmut generated
mutants_x_gitops_sources_list__mutmut['x_gitops_sources_list__mutmut_3'] = x_gitops_sources_list__mutmut_3 # type: ignore # mutmut generated
mutants_x_gitops_sources_list__mutmut['x_gitops_sources_list__mutmut_4'] = x_gitops_sources_list__mutmut_4 # type: ignore # mutmut generated
mutants_x_gitops_sources_list__mutmut['x_gitops_sources_list__mutmut_5'] = x_gitops_sources_list__mutmut_5 # type: ignore # mutmut generated
mutants_x_gitops_sources_list__mutmut['x_gitops_sources_list__mutmut_6'] = x_gitops_sources_list__mutmut_6 # type: ignore # mutmut generated
mutants_x_gitops_sources_list__mutmut['x_gitops_sources_list__mutmut_7'] = x_gitops_sources_list__mutmut_7 # type: ignore # mutmut generated
mutants_x_gitops_sources_list__mutmut['x_gitops_sources_list__mutmut_8'] = x_gitops_sources_list__mutmut_8 # type: ignore # mutmut generated
mutants_x_gitops_sources_list__mutmut['x_gitops_sources_list__mutmut_9'] = x_gitops_sources_list__mutmut_9 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_sources_list)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(gitops_sources_list)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
