"""MCP tool: policy_detect."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.governance.policy_detect.command import PolicyDetectCommand
from hexawyn.application.use_case.governance.policy_detect.policy_detect_use_case import (
    PolicyDetectUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_policy_detect__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_policy_detect__mutmut)
def policy_detect() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = None
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=None)
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = None
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(None)
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "XXengineXX": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "ENGINE": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "XXversionXX": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "VERSION": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "XXnamespaceXX": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "NAMESPACE": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "XXtotal_policiesXX": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "TOTAL_POLICIES": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "XXenforce_policiesXX": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "ENFORCE_POLICIES": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "XXaudit_policiesXX": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "AUDIT_POLICIES": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "XXtotal_violationsXX": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "TOTAL_VIOLATIONS": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "XXhigh_severityXX": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "HIGH_SEVERITY": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXengineXX": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "ENGINE": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "XXXX",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "XXversionXX": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "VERSION": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "XXnamespaceXX": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "NAMESPACE": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "XXtotal_policiesXX": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_31() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "TOTAL_POLICIES": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_32() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 1,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_33() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "XXenforce_policiesXX": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_34() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "ENFORCE_POLICIES": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_35() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 1,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_36() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "XXaudit_policiesXX": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_37() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "AUDIT_POLICIES": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_38() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 1,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_39() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "XXtotal_violationsXX": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_40() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "TOTAL_VIOLATIONS": 0,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_41() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 1,
            "high_severity": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_42() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "XXhigh_severityXX": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_43() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "HIGH_SEVERITY": 0,
            "error": str(exc),
        }


def x_policy_detect__mutmut_44() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 1,
            "error": str(exc),
        }


def x_policy_detect__mutmut_45() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "XXerrorXX": str(exc),
        }


def x_policy_detect__mutmut_46() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "ERROR": str(exc),
        }


def x_policy_detect__mutmut_47() -> dict[str, object]:
    from hexawyn.mcp.server import build_policy_adapter

    try:
        use_case = PolicyDetectUseCase(policy_port=build_policy_adapter())
        response = use_case.execute(PolicyDetectCommand())
        return {
            "engine": response.engine,
            "version": response.version,
            "namespace": response.namespace,
            "total_policies": response.total_policies,
            "enforce_policies": response.enforce_policies,
            "audit_policies": response.audit_policies,
            "total_violations": response.total_violations,
            "high_severity": response.high_severity,
            "error": None,
        }
    except Exception as exc:
        return {
            "engine": "",
            "version": None,
            "namespace": None,
            "total_policies": 0,
            "enforce_policies": 0,
            "audit_policies": 0,
            "total_violations": 0,
            "high_severity": 0,
            "error": str(None),
        }

mutants_x_policy_detect__mutmut['_mutmut_orig'] = x_policy_detect__mutmut_orig # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_1'] = x_policy_detect__mutmut_1 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_2'] = x_policy_detect__mutmut_2 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_3'] = x_policy_detect__mutmut_3 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_4'] = x_policy_detect__mutmut_4 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_5'] = x_policy_detect__mutmut_5 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_6'] = x_policy_detect__mutmut_6 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_7'] = x_policy_detect__mutmut_7 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_8'] = x_policy_detect__mutmut_8 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_9'] = x_policy_detect__mutmut_9 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_10'] = x_policy_detect__mutmut_10 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_11'] = x_policy_detect__mutmut_11 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_12'] = x_policy_detect__mutmut_12 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_13'] = x_policy_detect__mutmut_13 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_14'] = x_policy_detect__mutmut_14 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_15'] = x_policy_detect__mutmut_15 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_16'] = x_policy_detect__mutmut_16 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_17'] = x_policy_detect__mutmut_17 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_18'] = x_policy_detect__mutmut_18 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_19'] = x_policy_detect__mutmut_19 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_20'] = x_policy_detect__mutmut_20 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_21'] = x_policy_detect__mutmut_21 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_22'] = x_policy_detect__mutmut_22 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_23'] = x_policy_detect__mutmut_23 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_24'] = x_policy_detect__mutmut_24 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_25'] = x_policy_detect__mutmut_25 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_26'] = x_policy_detect__mutmut_26 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_27'] = x_policy_detect__mutmut_27 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_28'] = x_policy_detect__mutmut_28 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_29'] = x_policy_detect__mutmut_29 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_30'] = x_policy_detect__mutmut_30 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_31'] = x_policy_detect__mutmut_31 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_32'] = x_policy_detect__mutmut_32 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_33'] = x_policy_detect__mutmut_33 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_34'] = x_policy_detect__mutmut_34 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_35'] = x_policy_detect__mutmut_35 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_36'] = x_policy_detect__mutmut_36 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_37'] = x_policy_detect__mutmut_37 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_38'] = x_policy_detect__mutmut_38 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_39'] = x_policy_detect__mutmut_39 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_40'] = x_policy_detect__mutmut_40 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_41'] = x_policy_detect__mutmut_41 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_42'] = x_policy_detect__mutmut_42 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_43'] = x_policy_detect__mutmut_43 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_44'] = x_policy_detect__mutmut_44 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_45'] = x_policy_detect__mutmut_45 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_46'] = x_policy_detect__mutmut_46 # type: ignore # mutmut generated
mutants_x_policy_detect__mutmut['x_policy_detect__mutmut_47'] = x_policy_detect__mutmut_47 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(policy_detect)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(policy_detect)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
