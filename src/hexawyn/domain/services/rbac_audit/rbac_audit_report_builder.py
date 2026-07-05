from __future__ import annotations

from hexawyn.domain.models.rbac_audit import (
    RBACAuditReport,
    RBACFinding,
    UnusedServiceAccount,
)


def build_report(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
    total_service_accounts_checked: int,
) -> RBACAuditReport:
    return RBACAuditReport(
        findings=findings,
        unused_service_accounts=unused_service_accounts,
        excluded_system_service_accounts=excluded_system_service_accounts,
        total_service_accounts_checked=total_service_accounts_checked,
        summary=_build_summary(findings, unused_service_accounts, excluded_system_service_accounts),
    )


def _build_summary(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if not findings:
        summary = "No over-privileged service accounts found."
    else:
        critical_count = sum(1 for finding in findings if finding.risk_level == "critical")
        summary = f"{len(findings)} over-privileged service account(s) found"
        if critical_count:
            summary += f", {critical_count} critical"
        summary += "."
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary
