"""MCP tool: audit_tls_compliance — scan services for TLS issues."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.audit_tls_compliance.audit_tls_compliance_use_case import (  # noqa: E501  # type: ignore  # type: ignore
    AuditTLSComplianceUseCase,
)
from hexawyn.application.use_case.security.audit_tls_compliance.command import (
    AuditTlsComplianceCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_audit_tls_compliance__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_audit_tls_compliance__mutmut)
def audit_tls_compliance() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = None
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=None)
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = None
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(None)
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "XXall_compliantXX": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "ALL_COMPLIANT": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "XXtotal_issuesXX": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "TOTAL_ISSUES": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "XXservicesXX": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "SERVICES": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "ERROR": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"XXall_compliantXX": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"ALL_COMPLIANT": False, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": True, "total_issues": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "XXtotal_issuesXX": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "TOTAL_ISSUES": 0, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 1, "services": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "XXservicesXX": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "SERVICES": [], "error": str(exc)}


def x_audit_tls_compliance__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "XXerrorXX": str(exc)}


def x_audit_tls_compliance__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "ERROR": str(exc)}


def x_audit_tls_compliance__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import build_tls_compliance_adapter

    try:
        use_case = AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        r = use_case.execute(AuditTlsComplianceCommand())
        return {
            "all_compliant": r.result.all_compliant,
            "total_issues": r.result.total_issues,
            "services": [],
            "error": None,
        }
    except Exception as exc:
        return {"all_compliant": False, "total_issues": 0, "services": [], "error": str(None)}

mutants_x_audit_tls_compliance__mutmut['_mutmut_orig'] = x_audit_tls_compliance__mutmut_orig # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_1'] = x_audit_tls_compliance__mutmut_1 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_2'] = x_audit_tls_compliance__mutmut_2 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_3'] = x_audit_tls_compliance__mutmut_3 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_4'] = x_audit_tls_compliance__mutmut_4 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_5'] = x_audit_tls_compliance__mutmut_5 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_6'] = x_audit_tls_compliance__mutmut_6 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_7'] = x_audit_tls_compliance__mutmut_7 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_8'] = x_audit_tls_compliance__mutmut_8 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_9'] = x_audit_tls_compliance__mutmut_9 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_10'] = x_audit_tls_compliance__mutmut_10 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_11'] = x_audit_tls_compliance__mutmut_11 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_12'] = x_audit_tls_compliance__mutmut_12 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_13'] = x_audit_tls_compliance__mutmut_13 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_14'] = x_audit_tls_compliance__mutmut_14 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_15'] = x_audit_tls_compliance__mutmut_15 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_16'] = x_audit_tls_compliance__mutmut_16 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_17'] = x_audit_tls_compliance__mutmut_17 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_18'] = x_audit_tls_compliance__mutmut_18 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_19'] = x_audit_tls_compliance__mutmut_19 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_20'] = x_audit_tls_compliance__mutmut_20 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_21'] = x_audit_tls_compliance__mutmut_21 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_22'] = x_audit_tls_compliance__mutmut_22 # type: ignore # mutmut generated
mutants_x_audit_tls_compliance__mutmut['x_audit_tls_compliance__mutmut_23'] = x_audit_tls_compliance__mutmut_23 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(audit_tls_compliance)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(audit_tls_compliance)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
