from __future__ import annotations

from hexawyn.domain.models.pod_security import PodSecurityAuditReport, PodSecurityFinding


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_report__mutmut)
def build_report(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        compliant_pod_count=compliant_pod_count,
        total_pods_checked=total_pods_checked,
        summary=_build_summary(findings, compliant_pod_count),
    )


def x_build_report__mutmut_orig(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        compliant_pod_count=compliant_pod_count,
        total_pods_checked=total_pods_checked,
        summary=_build_summary(findings, compliant_pod_count),
    )


def x_build_report__mutmut_1(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=None,
        compliant_pod_count=compliant_pod_count,
        total_pods_checked=total_pods_checked,
        summary=_build_summary(findings, compliant_pod_count),
    )


def x_build_report__mutmut_2(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        compliant_pod_count=None,
        total_pods_checked=total_pods_checked,
        summary=_build_summary(findings, compliant_pod_count),
    )


def x_build_report__mutmut_3(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        compliant_pod_count=compliant_pod_count,
        total_pods_checked=None,
        summary=_build_summary(findings, compliant_pod_count),
    )


def x_build_report__mutmut_4(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        compliant_pod_count=compliant_pod_count,
        total_pods_checked=total_pods_checked,
        summary=None,
    )


def x_build_report__mutmut_5(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        compliant_pod_count=compliant_pod_count,
        total_pods_checked=total_pods_checked,
        summary=_build_summary(findings, compliant_pod_count),
    )


def x_build_report__mutmut_6(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        total_pods_checked=total_pods_checked,
        summary=_build_summary(findings, compliant_pod_count),
    )


def x_build_report__mutmut_7(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        compliant_pod_count=compliant_pod_count,
        summary=_build_summary(findings, compliant_pod_count),
    )


def x_build_report__mutmut_8(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        compliant_pod_count=compliant_pod_count,
        total_pods_checked=total_pods_checked,
        )


def x_build_report__mutmut_9(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        compliant_pod_count=compliant_pod_count,
        total_pods_checked=total_pods_checked,
        summary=_build_summary(None, compliant_pod_count),
    )


def x_build_report__mutmut_10(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        compliant_pod_count=compliant_pod_count,
        total_pods_checked=total_pods_checked,
        summary=_build_summary(findings, None),
    )


def x_build_report__mutmut_11(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        compliant_pod_count=compliant_pod_count,
        total_pods_checked=total_pods_checked,
        summary=_build_summary(compliant_pod_count),
    )


def x_build_report__mutmut_12(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        compliant_pod_count=compliant_pod_count,
        total_pods_checked=total_pods_checked,
        summary=_build_summary(findings, ),
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
mutants_x__build_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_summary__mutmut)
def _build_summary(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_orig(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_1(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_2(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "XXNo pods violating Pod Security Standards found.XX"

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_3(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "no pods violating pod security standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_4(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "NO PODS VIOLATING POD SECURITY STANDARDS FOUND."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_5(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = None
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_6(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = None
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_7(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        None
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_8(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        2
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_9(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(None)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_10(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity != "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_11(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "XXcriticalXX" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_12(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "CRITICAL" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_13(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = None
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_14(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary = f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_15(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary -= f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_16(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary = "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_17(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary -= "."
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_18(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "XX.XX"
    if compliant_pod_count:
        summary += f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_19(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary = f" {compliant_pod_count} pod(s) compliant."
    return summary


def x__build_summary__mutmut_20(findings: list[PodSecurityFinding], compliant_pod_count: int) -> str:
    if not findings:
        return "No pods violating Pod Security Standards found."

    namespaces = {finding.namespace for finding in findings}
    critical_count = sum(
        1
        for finding in findings
        if any(violation.severity == "critical" for violation in finding.violations)
    )
    summary = (
        f"{len(findings)} pod(s) violating Pod Security Standards "
        f"across {len(namespaces)} namespace(s)"
    )
    if critical_count:
        summary += f", {critical_count} critical"
    summary += "."
    if compliant_pod_count:
        summary -= f" {compliant_pod_count} pod(s) compliant."
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
