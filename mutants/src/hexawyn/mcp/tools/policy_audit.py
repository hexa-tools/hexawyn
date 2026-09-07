"""MCP tool: policy_audit — Global compliance audit report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.governance.policy_audit.command import PolicyAuditCommand
from hexawyn.application.use_case.governance.policy_audit.policy_audit_use_case import (
    PolicyAuditUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_policy_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_policy_audit__mutmut)
def policy_audit(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def x_policy_audit__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def x_policy_audit__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = None
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def x_policy_audit__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = None
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def x_policy_audit__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=None)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def x_policy_audit__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = None
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def x_policy_audit__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(None)
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def x_policy_audit__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=None))
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def x_policy_audit__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"XXresultsXX": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def x_policy_audit__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"RESULTS": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def x_policy_audit__mutmut_9(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "XXerrorXX": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def x_policy_audit__mutmut_10(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "ERROR": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(exc)}


def x_policy_audit__mutmut_11(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"XXresultsXX": {}, "error": str(exc)}


def x_policy_audit__mutmut_12(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"RESULTS": {}, "error": str(exc)}


def x_policy_audit__mutmut_13(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "XXerrorXX": str(exc)}


def x_policy_audit__mutmut_14(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "ERROR": str(exc)}


def x_policy_audit__mutmut_15(namespace: str | None = None) -> dict[str, object]:
    """Run a global compliance audit with per-namespace breakdown."""
    from hexawyn.mcp.server import build_policy_adapter

    try:
        adapter = build_policy_adapter()
        use_case = PolicyAuditUseCase(policy_port=adapter)
        response = use_case.execute(PolicyAuditCommand(namespace=namespace))
        return {"results": response.results, "error": response.error}
    except Exception as exc:
        return {"results": {}, "error": str(None)}

mutants_x_policy_audit__mutmut['_mutmut_orig'] = x_policy_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_1'] = x_policy_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_2'] = x_policy_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_3'] = x_policy_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_4'] = x_policy_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_5'] = x_policy_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_6'] = x_policy_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_7'] = x_policy_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_8'] = x_policy_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_9'] = x_policy_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_10'] = x_policy_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_11'] = x_policy_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_12'] = x_policy_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_13'] = x_policy_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_14'] = x_policy_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_policy_audit__mutmut['x_policy_audit__mutmut_15'] = x_policy_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_audit)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(policy_audit)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
