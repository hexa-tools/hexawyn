from __future__ import annotations

from hexawyn.domain.models.pod_security import PodSecurityAuditReport, PodSecurityFinding


def build_report(
    findings: list[PodSecurityFinding], compliant_pod_count: int, total_pods_checked: int
) -> PodSecurityAuditReport:
    return PodSecurityAuditReport(
        findings=findings,
        compliant_pod_count=compliant_pod_count,
        total_pods_checked=total_pods_checked,
        summary=_build_summary(findings, compliant_pod_count),
    )


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
