# mypy: ignore-errors
"""MCP tool: gitops_app_sync."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.gitops_app_sync.command import GitopsAppSyncCommand
from hexawyn.application.use_case.gitops.gitops_app_sync.gitops_app_sync_use_case import (
    GitopsAppSyncUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_gitops_app_sync__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_gitops_app_sync__mutmut)
def gitops_app_sync(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_app_sync__mutmut_orig(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_app_sync__mutmut_1(name: str = "XXtest-nameXX", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_app_sync__mutmut_2(name: str = "TEST-NAME", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_app_sync__mutmut_3(name: str = "test-name", namespace: str = "XXtest-nsXX") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_app_sync__mutmut_4(name: str = "test-name", namespace: str = "TEST-NS") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_app_sync__mutmut_5(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = None
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_app_sync__mutmut_6(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=None)
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_app_sync__mutmut_7(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = None  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_app_sync__mutmut_8(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_app_sync__mutmut_9(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_app_sync__mutmut_10(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_gitops_app_sync__mutmut_11(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_gitops_app_sync__mutmut_12(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_gitops_app_sync__mutmut_13(name: str = "test-name", namespace: str = "test-ns") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppSyncUseCase(gitops_port=build_gitops_adapter())
        _ = use_case.execute(GitopsAppSyncCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_gitops_app_sync__mutmut['_mutmut_orig'] = x_gitops_app_sync__mutmut_orig # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_1'] = x_gitops_app_sync__mutmut_1 # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_2'] = x_gitops_app_sync__mutmut_2 # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_3'] = x_gitops_app_sync__mutmut_3 # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_4'] = x_gitops_app_sync__mutmut_4 # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_5'] = x_gitops_app_sync__mutmut_5 # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_6'] = x_gitops_app_sync__mutmut_6 # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_7'] = x_gitops_app_sync__mutmut_7 # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_8'] = x_gitops_app_sync__mutmut_8 # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_9'] = x_gitops_app_sync__mutmut_9 # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_10'] = x_gitops_app_sync__mutmut_10 # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_11'] = x_gitops_app_sync__mutmut_11 # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_12'] = x_gitops_app_sync__mutmut_12 # type: ignore # mutmut generated
mutants_x_gitops_app_sync__mutmut['x_gitops_app_sync__mutmut_13'] = x_gitops_app_sync__mutmut_13 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(gitops_app_sync)


def x_register__mutmut_orig(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(gitops_app_sync)


def x_register__mutmut_1(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
