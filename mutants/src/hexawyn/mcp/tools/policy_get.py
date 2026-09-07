# mypy: ignore-errors
"""MCP tool: policy_get."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.governance.policy_get.command import PolicyGetCommand
from hexawyn.application.use_case.governance.policy_get.policy_get_use_case import PolicyGetUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_policy_get__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_policy_get__mutmut)
def policy_get(name: str = "test-name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyGetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_get__mutmut_orig(name: str = "test-name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyGetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_get__mutmut_1(name: str = "XXtest-nameXX") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyGetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_get__mutmut_2(name: str = "TEST-NAME") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyGetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_get__mutmut_3(name: str = "test-name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = None
        _ = use_case.execute(PolicyGetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_get__mutmut_4(name: str = "test-name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=None)
        _ = use_case.execute(PolicyGetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_get__mutmut_5(name: str = "test-name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=build_policy_adapter())
        _ = None  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_get__mutmut_6(name: str = "test-name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_get__mutmut_7(name: str = "test-name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyGetCommand())  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_get__mutmut_8(name: str = "test-name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyGetCommand())  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_get__mutmut_9(name: str = "test-name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyGetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_policy_get__mutmut_10(name: str = "test-name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyGetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_policy_get__mutmut_11(name: str = "test-name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyGetUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyGetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_policy_get__mutmut['_mutmut_orig'] = x_policy_get__mutmut_orig # type: ignore # mutmut generated
mutants_x_policy_get__mutmut['x_policy_get__mutmut_1'] = x_policy_get__mutmut_1 # type: ignore # mutmut generated
mutants_x_policy_get__mutmut['x_policy_get__mutmut_2'] = x_policy_get__mutmut_2 # type: ignore # mutmut generated
mutants_x_policy_get__mutmut['x_policy_get__mutmut_3'] = x_policy_get__mutmut_3 # type: ignore # mutmut generated
mutants_x_policy_get__mutmut['x_policy_get__mutmut_4'] = x_policy_get__mutmut_4 # type: ignore # mutmut generated
mutants_x_policy_get__mutmut['x_policy_get__mutmut_5'] = x_policy_get__mutmut_5 # type: ignore # mutmut generated
mutants_x_policy_get__mutmut['x_policy_get__mutmut_6'] = x_policy_get__mutmut_6 # type: ignore # mutmut generated
mutants_x_policy_get__mutmut['x_policy_get__mutmut_7'] = x_policy_get__mutmut_7 # type: ignore # mutmut generated
mutants_x_policy_get__mutmut['x_policy_get__mutmut_8'] = x_policy_get__mutmut_8 # type: ignore # mutmut generated
mutants_x_policy_get__mutmut['x_policy_get__mutmut_9'] = x_policy_get__mutmut_9 # type: ignore # mutmut generated
mutants_x_policy_get__mutmut['x_policy_get__mutmut_10'] = x_policy_get__mutmut_10 # type: ignore # mutmut generated
mutants_x_policy_get__mutmut['x_policy_get__mutmut_11'] = x_policy_get__mutmut_11 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(policy_get)


def x_register__mutmut_orig(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(policy_get)


def x_register__mutmut_1(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
