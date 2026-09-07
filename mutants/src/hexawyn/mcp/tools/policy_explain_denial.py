# mypy: ignore-errors
"""MCP tool: policy_explain_denial."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.governance.policy_explain_denial.command import (
    PolicyExplainDenialCommand,
)
from hexawyn.application.use_case.governance.policy_explain_denial.policy_explain_denial_use_case import (  # noqa: E501
    PolicyExplainDenialUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_policy_explain_denial__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_policy_explain_denial__mutmut)
def policy_explain_denial(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_orig(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_1(  # type: ignore
    resource_kind="XXtestXX", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_2(  # type: ignore
    resource_kind="TEST", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_3(  # type: ignore
    resource_kind="test", resource_name="XXtest-resource_nameXX", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_4(  # type: ignore
    resource_kind="test", resource_name="TEST-RESOURCE_NAME", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_5(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="XXtest-nsXX"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_6(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="TEST-NS"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_7(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = None
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_8(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=None)
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_9(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = None  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_10(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_11(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_12(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_policy_explain_denial__mutmut_13(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_policy_explain_denial__mutmut_14(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_policy_explain_denial__mutmut_15(  # type: ignore
    resource_kind="test", resource_name="test-resource_name", namespace="test-ns"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyExplainDenialUseCase(policy_port=build_policy_adapter())
        _ = use_case.execute(PolicyExplainDenialCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_policy_explain_denial__mutmut['_mutmut_orig'] = x_policy_explain_denial__mutmut_orig # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_1'] = x_policy_explain_denial__mutmut_1 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_2'] = x_policy_explain_denial__mutmut_2 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_3'] = x_policy_explain_denial__mutmut_3 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_4'] = x_policy_explain_denial__mutmut_4 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_5'] = x_policy_explain_denial__mutmut_5 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_6'] = x_policy_explain_denial__mutmut_6 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_7'] = x_policy_explain_denial__mutmut_7 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_8'] = x_policy_explain_denial__mutmut_8 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_9'] = x_policy_explain_denial__mutmut_9 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_10'] = x_policy_explain_denial__mutmut_10 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_11'] = x_policy_explain_denial__mutmut_11 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_12'] = x_policy_explain_denial__mutmut_12 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_13'] = x_policy_explain_denial__mutmut_13 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_14'] = x_policy_explain_denial__mutmut_14 # type: ignore # mutmut generated
mutants_x_policy_explain_denial__mutmut['x_policy_explain_denial__mutmut_15'] = x_policy_explain_denial__mutmut_15 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(policy_explain_denial)


def x_register__mutmut_orig(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(policy_explain_denial)


def x_register__mutmut_1(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
