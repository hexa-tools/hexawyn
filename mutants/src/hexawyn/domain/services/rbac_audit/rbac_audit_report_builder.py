from __future__ import annotations

from hexawyn.domain.models.rbac_audit import (
    RBACAuditReport,
    RBACFinding,
    UnusedServiceAccount,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_report__mutmut)
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


def x_build_report__mutmut_orig(
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


def x_build_report__mutmut_1(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
    total_service_accounts_checked: int,
) -> RBACAuditReport:
    return RBACAuditReport(
        findings=None,
        unused_service_accounts=unused_service_accounts,
        excluded_system_service_accounts=excluded_system_service_accounts,
        total_service_accounts_checked=total_service_accounts_checked,
        summary=_build_summary(findings, unused_service_accounts, excluded_system_service_accounts),
    )


def x_build_report__mutmut_2(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
    total_service_accounts_checked: int,
) -> RBACAuditReport:
    return RBACAuditReport(
        findings=findings,
        unused_service_accounts=None,
        excluded_system_service_accounts=excluded_system_service_accounts,
        total_service_accounts_checked=total_service_accounts_checked,
        summary=_build_summary(findings, unused_service_accounts, excluded_system_service_accounts),
    )


def x_build_report__mutmut_3(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
    total_service_accounts_checked: int,
) -> RBACAuditReport:
    return RBACAuditReport(
        findings=findings,
        unused_service_accounts=unused_service_accounts,
        excluded_system_service_accounts=None,
        total_service_accounts_checked=total_service_accounts_checked,
        summary=_build_summary(findings, unused_service_accounts, excluded_system_service_accounts),
    )


def x_build_report__mutmut_4(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
    total_service_accounts_checked: int,
) -> RBACAuditReport:
    return RBACAuditReport(
        findings=findings,
        unused_service_accounts=unused_service_accounts,
        excluded_system_service_accounts=excluded_system_service_accounts,
        total_service_accounts_checked=None,
        summary=_build_summary(findings, unused_service_accounts, excluded_system_service_accounts),
    )


def x_build_report__mutmut_5(
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
        summary=None,
    )


def x_build_report__mutmut_6(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
    total_service_accounts_checked: int,
) -> RBACAuditReport:
    return RBACAuditReport(
        unused_service_accounts=unused_service_accounts,
        excluded_system_service_accounts=excluded_system_service_accounts,
        total_service_accounts_checked=total_service_accounts_checked,
        summary=_build_summary(findings, unused_service_accounts, excluded_system_service_accounts),
    )


def x_build_report__mutmut_7(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
    total_service_accounts_checked: int,
) -> RBACAuditReport:
    return RBACAuditReport(
        findings=findings,
        excluded_system_service_accounts=excluded_system_service_accounts,
        total_service_accounts_checked=total_service_accounts_checked,
        summary=_build_summary(findings, unused_service_accounts, excluded_system_service_accounts),
    )


def x_build_report__mutmut_8(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
    total_service_accounts_checked: int,
) -> RBACAuditReport:
    return RBACAuditReport(
        findings=findings,
        unused_service_accounts=unused_service_accounts,
        total_service_accounts_checked=total_service_accounts_checked,
        summary=_build_summary(findings, unused_service_accounts, excluded_system_service_accounts),
    )


def x_build_report__mutmut_9(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
    total_service_accounts_checked: int,
) -> RBACAuditReport:
    return RBACAuditReport(
        findings=findings,
        unused_service_accounts=unused_service_accounts,
        excluded_system_service_accounts=excluded_system_service_accounts,
        summary=_build_summary(findings, unused_service_accounts, excluded_system_service_accounts),
    )


def x_build_report__mutmut_10(
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
        )


def x_build_report__mutmut_11(
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
        summary=_build_summary(None, unused_service_accounts, excluded_system_service_accounts),
    )


def x_build_report__mutmut_12(
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
        summary=_build_summary(findings, None, excluded_system_service_accounts),
    )


def x_build_report__mutmut_13(
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
        summary=_build_summary(findings, unused_service_accounts, None),
    )


def x_build_report__mutmut_14(
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
        summary=_build_summary(unused_service_accounts, excluded_system_service_accounts),
    )


def x_build_report__mutmut_15(
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
        summary=_build_summary(findings, excluded_system_service_accounts),
    )


def x_build_report__mutmut_16(
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
        summary=_build_summary(findings, unused_service_accounts, ),
    )

mutants_x_build_report__mutmut['_mutmut_orig'] = x_build_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_1'] = x_build_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_2'] = x_build_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_3'] = x_build_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_4'] = x_build_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_5'] = x_build_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_6'] = x_build_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_7'] = x_build_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_8'] = x_build_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_9'] = x_build_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_10'] = x_build_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_11'] = x_build_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_12'] = x_build_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_13'] = x_build_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_14'] = x_build_report__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_15'] = x_build_report__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_16'] = x_build_report__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_summary__mutmut)
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


def x__build_summary__mutmut_orig(
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


def x__build_summary__mutmut_1(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if findings:
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


def x__build_summary__mutmut_2(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if not findings:
        summary = None
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


def x__build_summary__mutmut_3(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if not findings:
        summary = "XXNo over-privileged service accounts found.XX"
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


def x__build_summary__mutmut_4(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if not findings:
        summary = "no over-privileged service accounts found."
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


def x__build_summary__mutmut_5(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if not findings:
        summary = "NO OVER-PRIVILEGED SERVICE ACCOUNTS FOUND."
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


def x__build_summary__mutmut_6(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if not findings:
        summary = "No over-privileged service accounts found."
    else:
        critical_count = None
        summary = f"{len(findings)} over-privileged service account(s) found"
        if critical_count:
            summary += f", {critical_count} critical"
        summary += "."
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_7(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if not findings:
        summary = "No over-privileged service accounts found."
    else:
        critical_count = sum(None)
        summary = f"{len(findings)} over-privileged service account(s) found"
        if critical_count:
            summary += f", {critical_count} critical"
        summary += "."
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_8(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if not findings:
        summary = "No over-privileged service accounts found."
    else:
        critical_count = sum(2 for finding in findings if finding.risk_level == "critical")
        summary = f"{len(findings)} over-privileged service account(s) found"
        if critical_count:
            summary += f", {critical_count} critical"
        summary += "."
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_9(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if not findings:
        summary = "No over-privileged service accounts found."
    else:
        critical_count = sum(1 for finding in findings if finding.risk_level != "critical")
        summary = f"{len(findings)} over-privileged service account(s) found"
        if critical_count:
            summary += f", {critical_count} critical"
        summary += "."
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_10(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if not findings:
        summary = "No over-privileged service accounts found."
    else:
        critical_count = sum(1 for finding in findings if finding.risk_level == "XXcriticalXX")
        summary = f"{len(findings)} over-privileged service account(s) found"
        if critical_count:
            summary += f", {critical_count} critical"
        summary += "."
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_11(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if not findings:
        summary = "No over-privileged service accounts found."
    else:
        critical_count = sum(1 for finding in findings if finding.risk_level == "CRITICAL")
        summary = f"{len(findings)} over-privileged service account(s) found"
        if critical_count:
            summary += f", {critical_count} critical"
        summary += "."
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_12(
    findings: list[RBACFinding],
    unused_service_accounts: list[UnusedServiceAccount],
    excluded_system_service_accounts: list[str],
) -> str:
    if not findings:
        summary = "No over-privileged service accounts found."
    else:
        critical_count = sum(1 for finding in findings if finding.risk_level == "critical")
        summary = None
        if critical_count:
            summary += f", {critical_count} critical"
        summary += "."
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_13(
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
            summary = f", {critical_count} critical"
        summary += "."
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_14(
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
            summary -= f", {critical_count} critical"
        summary += "."
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_15(
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
        summary = "."
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_16(
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
        summary -= "."
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_17(
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
        summary += "XX.XX"
    if unused_service_accounts:
        summary += f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_18(
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
        summary = f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_19(
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
        summary -= f" {len(unused_service_accounts)} unused service account(s) with no bindings."
    if excluded_system_service_accounts:
        summary += f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_20(
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
        summary = f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary


def x__build_summary__mutmut_21(
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
        summary -= f" {len(excluded_system_service_accounts)} system service account(s) excluded."
    return summary

mutants_x__build_summary__mutmut['_mutmut_orig'] = x__build_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_1'] = x__build_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_2'] = x__build_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_3'] = x__build_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_4'] = x__build_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_5'] = x__build_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_6'] = x__build_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_7'] = x__build_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_8'] = x__build_summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_9'] = x__build_summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_10'] = x__build_summary__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_11'] = x__build_summary__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_12'] = x__build_summary__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_13'] = x__build_summary__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_14'] = x__build_summary__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_15'] = x__build_summary__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_16'] = x__build_summary__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_17'] = x__build_summary__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_18'] = x__build_summary__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_19'] = x__build_summary__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_20'] = x__build_summary__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_21'] = x__build_summary__mutmut_21 # type: ignore # mutmut generated
