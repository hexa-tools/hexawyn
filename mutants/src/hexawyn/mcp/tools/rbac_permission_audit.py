"""MCP tool: audit_rbac_permissions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.audit_rbac_permissions.audit_rbac_permissions_use_case import (  # noqa: E501
    AuditRbacPermissionsUseCase,
)
from hexawyn.application.use_case.security.audit_rbac_permissions.command import (
    AuditRbacPermissionsCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_audit_rbac_permissions__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_audit_rbac_permissions__mutmut)
def audit_rbac_permissions(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_orig(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_1(namespace: str = "XXXX") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_2(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = None  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_3(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=None)  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_4(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = None  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_5(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(None)  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_6(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=None))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_7(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "XXfindingsXX": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_8(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "FINDINGS": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_9(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "XXunused_service_accountsXX": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_10(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "UNUSED_SERVICE_ACCOUNTS": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_11(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "XXtotal_auditedXX": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_12(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "TOTAL_AUDITED": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_13(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "XXsummaryXX": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_14(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "SUMMARY": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_15(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "XXerrorXX": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_16(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "ERROR": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_17(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "XXfindingsXX": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_18(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "FINDINGS": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_19(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "XXunused_service_accountsXX": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_20(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "UNUSED_SERVICE_ACCOUNTS": [],
            "total_audited": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_21(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "XXtotal_auditedXX": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_22(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "TOTAL_AUDITED": 0,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_23(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 1,
            "summary": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_24(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "XXsummaryXX": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_25(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "SUMMARY": "",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_26(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "XXXX",
            "error": str(exc),
        }


def x_audit_rbac_permissions__mutmut_27(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "XXerrorXX": str(exc),
        }


def x_audit_rbac_permissions__mutmut_28(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "ERROR": str(exc),
        }


def x_audit_rbac_permissions__mutmut_29(namespace: str = "") -> dict[str, object]:
    """Audit RBAC permissions for cluster-admin, wildcard verbs, and unused service accounts.

    Args:
        namespace: Optional namespace to scope (empty = all namespaces).
    """
    from hexawyn.mcp.server import build_rbac_audit_adapter

    try:
        use_case = AuditRbacPermissionsUseCase(port=build_rbac_audit_adapter())  # type: ignore
        response = use_case.execute(AuditRbacPermissionsCommand(namespace=namespace))  # type: ignore
        return {
            "findings": response.findings,
            "unused_service_accounts": response.unused_service_accounts,
            "total_audited": response.total_audited,
            "summary": response.summary,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "findings": [],
            "unused_service_accounts": [],
            "total_audited": 0,
            "summary": "",
            "error": str(None),
        }

mutants_x_audit_rbac_permissions__mutmut['_mutmut_orig'] = x_audit_rbac_permissions__mutmut_orig # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_1'] = x_audit_rbac_permissions__mutmut_1 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_2'] = x_audit_rbac_permissions__mutmut_2 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_3'] = x_audit_rbac_permissions__mutmut_3 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_4'] = x_audit_rbac_permissions__mutmut_4 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_5'] = x_audit_rbac_permissions__mutmut_5 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_6'] = x_audit_rbac_permissions__mutmut_6 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_7'] = x_audit_rbac_permissions__mutmut_7 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_8'] = x_audit_rbac_permissions__mutmut_8 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_9'] = x_audit_rbac_permissions__mutmut_9 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_10'] = x_audit_rbac_permissions__mutmut_10 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_11'] = x_audit_rbac_permissions__mutmut_11 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_12'] = x_audit_rbac_permissions__mutmut_12 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_13'] = x_audit_rbac_permissions__mutmut_13 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_14'] = x_audit_rbac_permissions__mutmut_14 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_15'] = x_audit_rbac_permissions__mutmut_15 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_16'] = x_audit_rbac_permissions__mutmut_16 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_17'] = x_audit_rbac_permissions__mutmut_17 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_18'] = x_audit_rbac_permissions__mutmut_18 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_19'] = x_audit_rbac_permissions__mutmut_19 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_20'] = x_audit_rbac_permissions__mutmut_20 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_21'] = x_audit_rbac_permissions__mutmut_21 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_22'] = x_audit_rbac_permissions__mutmut_22 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_23'] = x_audit_rbac_permissions__mutmut_23 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_24'] = x_audit_rbac_permissions__mutmut_24 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_25'] = x_audit_rbac_permissions__mutmut_25 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_26'] = x_audit_rbac_permissions__mutmut_26 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_27'] = x_audit_rbac_permissions__mutmut_27 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_28'] = x_audit_rbac_permissions__mutmut_28 # type: ignore # mutmut generated
mutants_x_audit_rbac_permissions__mutmut['x_audit_rbac_permissions__mutmut_29'] = x_audit_rbac_permissions__mutmut_29 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(audit_rbac_permissions)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(audit_rbac_permissions)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
