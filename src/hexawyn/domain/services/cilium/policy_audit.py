"""Pure Cilium network-policy coverage audit — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumAuditFinding,
    CiliumNetworkPolicyInfo,
    CiliumPolicyAuditResult,
    CiliumWorkload,
)

_COVERAGE_RISK: dict[str, str] = {
    "no_policy": "critical",
    "no_default_deny": "critical",
    "partial": "medium",
    "l7_gap": "medium",
}


def selector_matches(
    workload_labels: dict[str, str],
    endpoint_labels: tuple[tuple[str, str], ...] | None,
) -> bool:
    """True if a workload is selected by a Cilium endpoint selector.

    ``None`` (unparseable selector) never claims coverage; an empty selector
    matches every workload.
    """
    if endpoint_labels is None:
        return False
    if not endpoint_labels:
        return True
    return all(workload_labels.get(key) == value for key, value in endpoint_labels)


def build_policy_audit(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if not workloads:
        return CiliumPolicyAuditResult(
            installed=True,
            status="empty",
            view="cilium",
            total_workloads=0,
            uncovered_count=0,
            findings=[],
            summary="No workloads found to audit",
            note=None,
        )
    findings: list[CiliumAuditFinding] = []
    for workload in workloads:
        finding = _classify(policies, workload)
        if finding is not None:
            findings.append(finding)
    uncovered = sum(
        1 for finding in findings if finding.coverage in ("no_policy", "no_default_deny")
    )
    return CiliumPolicyAuditResult(
        installed=True,
        status="gaps_found" if findings else "covered",
        view="cilium",
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def _classify(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count > 0 for p in matching)
    egress = any(p.egress_rule_count > 0 for p in matching)
    l7 = any(p.l7_rule_count > 0 for p in matching)
    restricted = (ingress, egress, l7)
    if ingress and egress:
        if l7:
            return None
        return _finding(workload, "l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def _finding(
    workload: CiliumWorkload,
    coverage: str,
    restricted: tuple[bool, bool, bool],
) -> CiliumAuditFinding:
    ingress, egress, l7 = restricted
    return CiliumAuditFinding(
        namespace=workload.namespace,
        workload=workload.name,
        coverage=coverage,
        ingress_restricted=ingress,
        egress_restricted=egress,
        l7_restricted=l7,
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def _note_for(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def _summary(gap_count: int, total: int) -> str:
    return f"{gap_count} workload(s) with a coverage gap out of {total}"
