"""MCP tool: policy_list."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.governance.policy_list.command import PolicyListCommand
from hexawyn.application.use_case.governance.policy_list.policy_list_use_case import (
    PolicyListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_policy_list__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_policy_list__mutmut)
def policy_list() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyListCommand())
        return {
            "policies": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "error": str(exc),
        }


def x_policy_list__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyListCommand())
        return {
            "policies": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "error": str(exc),
        }


def x_policy_list__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = None
        response = use_case.execute(PolicyListCommand())
        return {
            "policies": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "error": str(exc),
        }


def x_policy_list__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=None)
        response = use_case.execute(PolicyListCommand())
        return {
            "policies": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "error": str(exc),
        }


def x_policy_list__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = None
        return {
            "policies": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "error": str(exc),
        }


def x_policy_list__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(None)
        return {
            "policies": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "error": str(exc),
        }


def x_policy_list__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyListCommand())
        return {
            "XXpoliciesXX": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "error": str(exc),
        }


def x_policy_list__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyListCommand())
        return {
            "POLICIES": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "error": str(exc),
        }


def x_policy_list__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyListCommand())
        return {
            "policies": response.policies,
            "XXerrorXX": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "error": str(exc),
        }


def x_policy_list__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyListCommand())
        return {
            "policies": response.policies,
            "ERROR": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "error": str(exc),
        }


def x_policy_list__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyListCommand())
        return {
            "policies": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "XXpoliciesXX": [],
            "error": str(exc),
        }


def x_policy_list__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyListCommand())
        return {
            "policies": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "POLICIES": [],
            "error": str(exc),
        }


def x_policy_list__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyListCommand())
        return {
            "policies": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "XXerrorXX": str(exc),
        }


def x_policy_list__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyListCommand())
        return {
            "policies": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "ERROR": str(exc),
        }


def x_policy_list__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyListUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyListCommand())
        return {
            "policies": response.policies,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "policies": [],
            "error": str(None),
        }

mutants_x_policy_list__mutmut['_mutmut_orig'] = x_policy_list__mutmut_orig # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_1'] = x_policy_list__mutmut_1 # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_2'] = x_policy_list__mutmut_2 # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_3'] = x_policy_list__mutmut_3 # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_4'] = x_policy_list__mutmut_4 # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_5'] = x_policy_list__mutmut_5 # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_6'] = x_policy_list__mutmut_6 # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_7'] = x_policy_list__mutmut_7 # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_8'] = x_policy_list__mutmut_8 # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_9'] = x_policy_list__mutmut_9 # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_10'] = x_policy_list__mutmut_10 # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_11'] = x_policy_list__mutmut_11 # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_12'] = x_policy_list__mutmut_12 # type: ignore # mutmut generated
mutants_x_policy_list__mutmut['x_policy_list__mutmut_13'] = x_policy_list__mutmut_13 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_list)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(policy_list)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
