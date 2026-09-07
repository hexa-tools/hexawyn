"""MCP tool: policy_violations_list."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.governance.policy_violations_list.command import (
    PolicyViolationsListCommand,
)
from hexawyn.application.use_case.governance.policy_violations_list.policy_violations_list_use_case import (  # noqa: E501
    PolicyViolationsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_policy_violations_list__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_policy_violations_list__mutmut)
def policy_violations_list() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyViolationsListUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyViolationsListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_violations_list__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyViolationsListUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyViolationsListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_violations_list__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = None
        _ = use_case.execute(PolicyViolationsListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_violations_list__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyViolationsListUseCase(policy_port=None)
        _ = use_case.execute(PolicyViolationsListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_violations_list__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyViolationsListUseCase(policy_port=build_policy_adapter())
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_violations_list__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyViolationsListUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_violations_list__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyViolationsListUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyViolationsListCommand())
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_violations_list__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyViolationsListUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyViolationsListCommand())
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_violations_list__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyViolationsListUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyViolationsListCommand())
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_policy_violations_list__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyViolationsListUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyViolationsListCommand())
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_policy_violations_list__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyViolationsListUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyViolationsListCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_policy_violations_list__mutmut['_mutmut_orig'] = x_policy_violations_list__mutmut_orig # type: ignore # mutmut generated
mutants_x_policy_violations_list__mutmut['x_policy_violations_list__mutmut_1'] = x_policy_violations_list__mutmut_1 # type: ignore # mutmut generated
mutants_x_policy_violations_list__mutmut['x_policy_violations_list__mutmut_2'] = x_policy_violations_list__mutmut_2 # type: ignore # mutmut generated
mutants_x_policy_violations_list__mutmut['x_policy_violations_list__mutmut_3'] = x_policy_violations_list__mutmut_3 # type: ignore # mutmut generated
mutants_x_policy_violations_list__mutmut['x_policy_violations_list__mutmut_4'] = x_policy_violations_list__mutmut_4 # type: ignore # mutmut generated
mutants_x_policy_violations_list__mutmut['x_policy_violations_list__mutmut_5'] = x_policy_violations_list__mutmut_5 # type: ignore # mutmut generated
mutants_x_policy_violations_list__mutmut['x_policy_violations_list__mutmut_6'] = x_policy_violations_list__mutmut_6 # type: ignore # mutmut generated
mutants_x_policy_violations_list__mutmut['x_policy_violations_list__mutmut_7'] = x_policy_violations_list__mutmut_7 # type: ignore # mutmut generated
mutants_x_policy_violations_list__mutmut['x_policy_violations_list__mutmut_8'] = x_policy_violations_list__mutmut_8 # type: ignore # mutmut generated
mutants_x_policy_violations_list__mutmut['x_policy_violations_list__mutmut_9'] = x_policy_violations_list__mutmut_9 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_violations_list)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(policy_violations_list)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
