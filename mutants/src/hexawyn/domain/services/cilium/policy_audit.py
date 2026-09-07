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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_selector_matches__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_selector_matches__mutmut)
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


def x_selector_matches__mutmut_orig(
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


def x_selector_matches__mutmut_1(
    workload_labels: dict[str, str],
    endpoint_labels: tuple[tuple[str, str], ...] | None,
) -> bool:
    """True if a workload is selected by a Cilium endpoint selector.

    ``None`` (unparseable selector) never claims coverage; an empty selector
    matches every workload.
    """
    if endpoint_labels is not None:
        return False
    if not endpoint_labels:
        return True
    return all(workload_labels.get(key) == value for key, value in endpoint_labels)


def x_selector_matches__mutmut_2(
    workload_labels: dict[str, str],
    endpoint_labels: tuple[tuple[str, str], ...] | None,
) -> bool:
    """True if a workload is selected by a Cilium endpoint selector.

    ``None`` (unparseable selector) never claims coverage; an empty selector
    matches every workload.
    """
    if endpoint_labels is None:
        return True
    if not endpoint_labels:
        return True
    return all(workload_labels.get(key) == value for key, value in endpoint_labels)


def x_selector_matches__mutmut_3(
    workload_labels: dict[str, str],
    endpoint_labels: tuple[tuple[str, str], ...] | None,
) -> bool:
    """True if a workload is selected by a Cilium endpoint selector.

    ``None`` (unparseable selector) never claims coverage; an empty selector
    matches every workload.
    """
    if endpoint_labels is None:
        return False
    if endpoint_labels:
        return True
    return all(workload_labels.get(key) == value for key, value in endpoint_labels)


def x_selector_matches__mutmut_4(
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
        return False
    return all(workload_labels.get(key) == value for key, value in endpoint_labels)


def x_selector_matches__mutmut_5(
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
    return all(None)


def x_selector_matches__mutmut_6(
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
    return all(workload_labels.get(None) == value for key, value in endpoint_labels)


def x_selector_matches__mutmut_7(
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
    return all(workload_labels.get(key) != value for key, value in endpoint_labels)

mutants_x_selector_matches__mutmut['_mutmut_orig'] = x_selector_matches__mutmut_orig # type: ignore # mutmut generated
mutants_x_selector_matches__mutmut['x_selector_matches__mutmut_1'] = x_selector_matches__mutmut_1 # type: ignore # mutmut generated
mutants_x_selector_matches__mutmut['x_selector_matches__mutmut_2'] = x_selector_matches__mutmut_2 # type: ignore # mutmut generated
mutants_x_selector_matches__mutmut['x_selector_matches__mutmut_3'] = x_selector_matches__mutmut_3 # type: ignore # mutmut generated
mutants_x_selector_matches__mutmut['x_selector_matches__mutmut_4'] = x_selector_matches__mutmut_4 # type: ignore # mutmut generated
mutants_x_selector_matches__mutmut['x_selector_matches__mutmut_5'] = x_selector_matches__mutmut_5 # type: ignore # mutmut generated
mutants_x_selector_matches__mutmut['x_selector_matches__mutmut_6'] = x_selector_matches__mutmut_6 # type: ignore # mutmut generated
mutants_x_selector_matches__mutmut['x_selector_matches__mutmut_7'] = x_selector_matches__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_policy_audit__mutmut)
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


def x_build_policy_audit__mutmut_orig(
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


def x_build_policy_audit__mutmut_1(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = None
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


def x_build_policy_audit__mutmut_2(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if workloads:
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


def x_build_policy_audit__mutmut_3(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if not workloads:
        return CiliumPolicyAuditResult(
            installed=None,
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


def x_build_policy_audit__mutmut_4(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if not workloads:
        return CiliumPolicyAuditResult(
            installed=True,
            status=None,
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


def x_build_policy_audit__mutmut_5(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if not workloads:
        return CiliumPolicyAuditResult(
            installed=True,
            status="empty",
            view=None,
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


def x_build_policy_audit__mutmut_6(
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
            total_workloads=None,
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


def x_build_policy_audit__mutmut_7(
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
            uncovered_count=None,
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


def x_build_policy_audit__mutmut_8(
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
            findings=None,
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


def x_build_policy_audit__mutmut_9(
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
            summary=None,
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


def x_build_policy_audit__mutmut_10(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if not workloads:
        return CiliumPolicyAuditResult(
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


def x_build_policy_audit__mutmut_11(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if not workloads:
        return CiliumPolicyAuditResult(
            installed=True,
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


def x_build_policy_audit__mutmut_12(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if not workloads:
        return CiliumPolicyAuditResult(
            installed=True,
            status="empty",
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


def x_build_policy_audit__mutmut_13(
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


def x_build_policy_audit__mutmut_14(
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


def x_build_policy_audit__mutmut_15(
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


def x_build_policy_audit__mutmut_16(
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


def x_build_policy_audit__mutmut_17(
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


def x_build_policy_audit__mutmut_18(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if not workloads:
        return CiliumPolicyAuditResult(
            installed=False,
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


def x_build_policy_audit__mutmut_19(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if not workloads:
        return CiliumPolicyAuditResult(
            installed=True,
            status="XXemptyXX",
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


def x_build_policy_audit__mutmut_20(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if not workloads:
        return CiliumPolicyAuditResult(
            installed=True,
            status="EMPTY",
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


def x_build_policy_audit__mutmut_21(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if not workloads:
        return CiliumPolicyAuditResult(
            installed=True,
            status="empty",
            view="XXciliumXX",
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


def x_build_policy_audit__mutmut_22(
    policies: list[CiliumNetworkPolicyInfo],
    workloads: list[CiliumWorkload],
) -> CiliumPolicyAuditResult:
    """Audit Cilium policy coverage, flagging gaps and ranking them by risk."""
    total = len(workloads)
    if not workloads:
        return CiliumPolicyAuditResult(
            installed=True,
            status="empty",
            view="CILIUM",
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


def x_build_policy_audit__mutmut_23(
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
            total_workloads=1,
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


def x_build_policy_audit__mutmut_24(
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
            uncovered_count=1,
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


def x_build_policy_audit__mutmut_25(
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
            summary="XXNo workloads found to auditXX",
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


def x_build_policy_audit__mutmut_26(
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
            summary="no workloads found to audit",
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


def x_build_policy_audit__mutmut_27(
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
            summary="NO WORKLOADS FOUND TO AUDIT",
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


def x_build_policy_audit__mutmut_28(
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
    findings: list[CiliumAuditFinding] = None
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


def x_build_policy_audit__mutmut_29(
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
        finding = None
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


def x_build_policy_audit__mutmut_30(
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
        finding = _classify(None, workload)
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


def x_build_policy_audit__mutmut_31(
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
        finding = _classify(policies, None)
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


def x_build_policy_audit__mutmut_32(
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
        finding = _classify(workload)
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


def x_build_policy_audit__mutmut_33(
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
        finding = _classify(policies, )
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


def x_build_policy_audit__mutmut_34(
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
        if finding is None:
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


def x_build_policy_audit__mutmut_35(
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
            findings.append(None)
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


def x_build_policy_audit__mutmut_36(
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
    uncovered = None
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


def x_build_policy_audit__mutmut_37(
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
        None
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


def x_build_policy_audit__mutmut_38(
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
        2 for finding in findings if finding.coverage in ("no_policy", "no_default_deny")
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


def x_build_policy_audit__mutmut_39(
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
        1 for finding in findings if finding.coverage not in ("no_policy", "no_default_deny")
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


def x_build_policy_audit__mutmut_40(
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
        1 for finding in findings if finding.coverage in ("XXno_policyXX", "no_default_deny")
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


def x_build_policy_audit__mutmut_41(
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
        1 for finding in findings if finding.coverage in ("NO_POLICY", "no_default_deny")
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


def x_build_policy_audit__mutmut_42(
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
        1 for finding in findings if finding.coverage in ("no_policy", "XXno_default_denyXX")
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


def x_build_policy_audit__mutmut_43(
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
        1 for finding in findings if finding.coverage in ("no_policy", "NO_DEFAULT_DENY")
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


def x_build_policy_audit__mutmut_44(
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
        installed=None,
        status="gaps_found" if findings else "covered",
        view="cilium",
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_45(
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
        status=None,
        view="cilium",
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_46(
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
        view=None,
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_47(
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
        total_workloads=None,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_48(
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
        uncovered_count=None,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_49(
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
        findings=None,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_50(
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
        summary=None,
        note=None,
    )


def x_build_policy_audit__mutmut_51(
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
        status="gaps_found" if findings else "covered",
        view="cilium",
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_52(
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
        view="cilium",
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_53(
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
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_54(
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
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_55(
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
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_56(
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
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_57(
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
        note=None,
    )


def x_build_policy_audit__mutmut_58(
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
        )


def x_build_policy_audit__mutmut_59(
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
        installed=False,
        status="gaps_found" if findings else "covered",
        view="cilium",
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_60(
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
        status="XXgaps_foundXX" if findings else "covered",
        view="cilium",
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_61(
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
        status="GAPS_FOUND" if findings else "covered",
        view="cilium",
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_62(
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
        status="gaps_found" if findings else "XXcoveredXX",
        view="cilium",
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_63(
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
        status="gaps_found" if findings else "COVERED",
        view="cilium",
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_64(
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
        view="XXciliumXX",
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_65(
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
        view="CILIUM",
        total_workloads=total,
        uncovered_count=uncovered,
        findings=findings,
        summary=_summary(len(findings), total),
        note=None,
    )


def x_build_policy_audit__mutmut_66(
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
        summary=_summary(None, total),
        note=None,
    )


def x_build_policy_audit__mutmut_67(
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
        summary=_summary(len(findings), None),
        note=None,
    )


def x_build_policy_audit__mutmut_68(
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
        summary=_summary(total),
        note=None,
    )


def x_build_policy_audit__mutmut_69(
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
        summary=_summary(len(findings), ),
        note=None,
    )

mutants_x_build_policy_audit__mutmut['_mutmut_orig'] = x_build_policy_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_1'] = x_build_policy_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_2'] = x_build_policy_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_3'] = x_build_policy_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_4'] = x_build_policy_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_5'] = x_build_policy_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_6'] = x_build_policy_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_7'] = x_build_policy_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_8'] = x_build_policy_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_9'] = x_build_policy_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_10'] = x_build_policy_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_11'] = x_build_policy_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_12'] = x_build_policy_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_13'] = x_build_policy_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_14'] = x_build_policy_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_15'] = x_build_policy_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_16'] = x_build_policy_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_17'] = x_build_policy_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_18'] = x_build_policy_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_19'] = x_build_policy_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_20'] = x_build_policy_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_21'] = x_build_policy_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_22'] = x_build_policy_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_23'] = x_build_policy_audit__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_24'] = x_build_policy_audit__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_25'] = x_build_policy_audit__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_26'] = x_build_policy_audit__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_27'] = x_build_policy_audit__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_28'] = x_build_policy_audit__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_29'] = x_build_policy_audit__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_30'] = x_build_policy_audit__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_31'] = x_build_policy_audit__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_32'] = x_build_policy_audit__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_33'] = x_build_policy_audit__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_34'] = x_build_policy_audit__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_35'] = x_build_policy_audit__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_36'] = x_build_policy_audit__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_37'] = x_build_policy_audit__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_38'] = x_build_policy_audit__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_39'] = x_build_policy_audit__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_40'] = x_build_policy_audit__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_41'] = x_build_policy_audit__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_42'] = x_build_policy_audit__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_43'] = x_build_policy_audit__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_44'] = x_build_policy_audit__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_45'] = x_build_policy_audit__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_46'] = x_build_policy_audit__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_47'] = x_build_policy_audit__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_48'] = x_build_policy_audit__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_49'] = x_build_policy_audit__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_50'] = x_build_policy_audit__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_51'] = x_build_policy_audit__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_52'] = x_build_policy_audit__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_53'] = x_build_policy_audit__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_54'] = x_build_policy_audit__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_55'] = x_build_policy_audit__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_56'] = x_build_policy_audit__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_57'] = x_build_policy_audit__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_58'] = x_build_policy_audit__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_59'] = x_build_policy_audit__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_60'] = x_build_policy_audit__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_61'] = x_build_policy_audit__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_62'] = x_build_policy_audit__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_63'] = x_build_policy_audit__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_64'] = x_build_policy_audit__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_65'] = x_build_policy_audit__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_66'] = x_build_policy_audit__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_67'] = x_build_policy_audit__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_68'] = x_build_policy_audit__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_policy_audit__mutmut['x_build_policy_audit__mutmut_69'] = x_build_policy_audit__mutmut_69 # type: ignore # mutmut generated
mutants_x__classify__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__classify__mutmut)
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


def x__classify__mutmut_orig(
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


def x__classify__mutmut_1(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = None
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


def x__classify__mutmut_2(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(None, p.endpoint_labels)]
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


def x__classify__mutmut_3(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, None)]
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


def x__classify__mutmut_4(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(p.endpoint_labels)]
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


def x__classify__mutmut_5(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, )]
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


def x__classify__mutmut_6(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if matching:
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


def x__classify__mutmut_7(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(None, "no_policy", restricted=(False, False, False))
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


def x__classify__mutmut_8(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, None, restricted=(False, False, False))
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


def x__classify__mutmut_9(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=None)
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


def x__classify__mutmut_10(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding("no_policy", restricted=(False, False, False))
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


def x__classify__mutmut_11(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, restricted=(False, False, False))
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


def x__classify__mutmut_12(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", )
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


def x__classify__mutmut_13(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "XXno_policyXX", restricted=(False, False, False))
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


def x__classify__mutmut_14(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "NO_POLICY", restricted=(False, False, False))
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


def x__classify__mutmut_15(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(True, False, False))
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


def x__classify__mutmut_16(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, True, False))
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


def x__classify__mutmut_17(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, True))
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


def x__classify__mutmut_18(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = None
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


def x__classify__mutmut_19(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(None)
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


def x__classify__mutmut_20(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count >= 0 for p in matching)
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


def x__classify__mutmut_21(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count > 1 for p in matching)
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


def x__classify__mutmut_22(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count > 0 for p in matching)
    egress = None
    l7 = any(p.l7_rule_count > 0 for p in matching)
    restricted = (ingress, egress, l7)
    if ingress and egress:
        if l7:
            return None
        return _finding(workload, "l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_23(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count > 0 for p in matching)
    egress = any(None)
    l7 = any(p.l7_rule_count > 0 for p in matching)
    restricted = (ingress, egress, l7)
    if ingress and egress:
        if l7:
            return None
        return _finding(workload, "l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_24(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count > 0 for p in matching)
    egress = any(p.egress_rule_count >= 0 for p in matching)
    l7 = any(p.l7_rule_count > 0 for p in matching)
    restricted = (ingress, egress, l7)
    if ingress and egress:
        if l7:
            return None
        return _finding(workload, "l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_25(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count > 0 for p in matching)
    egress = any(p.egress_rule_count > 1 for p in matching)
    l7 = any(p.l7_rule_count > 0 for p in matching)
    restricted = (ingress, egress, l7)
    if ingress and egress:
        if l7:
            return None
        return _finding(workload, "l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_26(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count > 0 for p in matching)
    egress = any(p.egress_rule_count > 0 for p in matching)
    l7 = None
    restricted = (ingress, egress, l7)
    if ingress and egress:
        if l7:
            return None
        return _finding(workload, "l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_27(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count > 0 for p in matching)
    egress = any(p.egress_rule_count > 0 for p in matching)
    l7 = any(None)
    restricted = (ingress, egress, l7)
    if ingress and egress:
        if l7:
            return None
        return _finding(workload, "l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_28(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count > 0 for p in matching)
    egress = any(p.egress_rule_count > 0 for p in matching)
    l7 = any(p.l7_rule_count >= 0 for p in matching)
    restricted = (ingress, egress, l7)
    if ingress and egress:
        if l7:
            return None
        return _finding(workload, "l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_29(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count > 0 for p in matching)
    egress = any(p.egress_rule_count > 0 for p in matching)
    l7 = any(p.l7_rule_count > 1 for p in matching)
    restricted = (ingress, egress, l7)
    if ingress and egress:
        if l7:
            return None
        return _finding(workload, "l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_30(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count > 0 for p in matching)
    egress = any(p.egress_rule_count > 0 for p in matching)
    l7 = any(p.l7_rule_count > 0 for p in matching)
    restricted = None
    if ingress and egress:
        if l7:
            return None
        return _finding(workload, "l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_31(
    policies: list[CiliumNetworkPolicyInfo], workload: CiliumWorkload
) -> CiliumAuditFinding | None:
    matching = [p for p in policies if selector_matches(workload.labels, p.endpoint_labels)]
    if not matching:
        return _finding(workload, "no_policy", restricted=(False, False, False))
    ingress = any(p.ingress_rule_count > 0 for p in matching)
    egress = any(p.egress_rule_count > 0 for p in matching)
    l7 = any(p.l7_rule_count > 0 for p in matching)
    restricted = (ingress, egress, l7)
    if ingress or egress:
        if l7:
            return None
        return _finding(workload, "l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_32(
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
        return _finding(None, "l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_33(
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
        return _finding(workload, None, restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_34(
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
        return _finding(workload, "l7_gap", None)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_35(
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
        return _finding("l7_gap", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_36(
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
        return _finding(workload, restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_37(
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
        return _finding(workload, "l7_gap", )
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_38(
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
        return _finding(workload, "XXl7_gapXX", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_39(
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
        return _finding(workload, "L7_GAP", restricted)
    if ingress or egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_40(
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
    if ingress and egress:
        return _finding(workload, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_41(
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
        return _finding(None, "partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_42(
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
        return _finding(workload, None, restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_43(
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
        return _finding(workload, "partial", None)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_44(
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
        return _finding("partial", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_45(
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
        return _finding(workload, restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_46(
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
        return _finding(workload, "partial", )
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_47(
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
        return _finding(workload, "XXpartialXX", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_48(
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
        return _finding(workload, "PARTIAL", restricted)
    return _finding(workload, "no_default_deny", restricted)


def x__classify__mutmut_49(
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
    return _finding(None, "no_default_deny", restricted)


def x__classify__mutmut_50(
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
    return _finding(workload, None, restricted)


def x__classify__mutmut_51(
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
    return _finding(workload, "no_default_deny", None)


def x__classify__mutmut_52(
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
    return _finding("no_default_deny", restricted)


def x__classify__mutmut_53(
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
    return _finding(workload, restricted)


def x__classify__mutmut_54(
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
    return _finding(workload, "no_default_deny", )


def x__classify__mutmut_55(
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
    return _finding(workload, "XXno_default_denyXX", restricted)


def x__classify__mutmut_56(
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
    return _finding(workload, "NO_DEFAULT_DENY", restricted)

mutants_x__classify__mutmut['_mutmut_orig'] = x__classify__mutmut_orig # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_1'] = x__classify__mutmut_1 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_2'] = x__classify__mutmut_2 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_3'] = x__classify__mutmut_3 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_4'] = x__classify__mutmut_4 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_5'] = x__classify__mutmut_5 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_6'] = x__classify__mutmut_6 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_7'] = x__classify__mutmut_7 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_8'] = x__classify__mutmut_8 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_9'] = x__classify__mutmut_9 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_10'] = x__classify__mutmut_10 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_11'] = x__classify__mutmut_11 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_12'] = x__classify__mutmut_12 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_13'] = x__classify__mutmut_13 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_14'] = x__classify__mutmut_14 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_15'] = x__classify__mutmut_15 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_16'] = x__classify__mutmut_16 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_17'] = x__classify__mutmut_17 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_18'] = x__classify__mutmut_18 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_19'] = x__classify__mutmut_19 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_20'] = x__classify__mutmut_20 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_21'] = x__classify__mutmut_21 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_22'] = x__classify__mutmut_22 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_23'] = x__classify__mutmut_23 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_24'] = x__classify__mutmut_24 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_25'] = x__classify__mutmut_25 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_26'] = x__classify__mutmut_26 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_27'] = x__classify__mutmut_27 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_28'] = x__classify__mutmut_28 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_29'] = x__classify__mutmut_29 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_30'] = x__classify__mutmut_30 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_31'] = x__classify__mutmut_31 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_32'] = x__classify__mutmut_32 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_33'] = x__classify__mutmut_33 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_34'] = x__classify__mutmut_34 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_35'] = x__classify__mutmut_35 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_36'] = x__classify__mutmut_36 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_37'] = x__classify__mutmut_37 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_38'] = x__classify__mutmut_38 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_39'] = x__classify__mutmut_39 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_40'] = x__classify__mutmut_40 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_41'] = x__classify__mutmut_41 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_42'] = x__classify__mutmut_42 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_43'] = x__classify__mutmut_43 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_44'] = x__classify__mutmut_44 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_45'] = x__classify__mutmut_45 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_46'] = x__classify__mutmut_46 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_47'] = x__classify__mutmut_47 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_48'] = x__classify__mutmut_48 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_49'] = x__classify__mutmut_49 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_50'] = x__classify__mutmut_50 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_51'] = x__classify__mutmut_51 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_52'] = x__classify__mutmut_52 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_53'] = x__classify__mutmut_53 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_54'] = x__classify__mutmut_54 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_55'] = x__classify__mutmut_55 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_56'] = x__classify__mutmut_56 # type: ignore # mutmut generated
mutants_x__finding__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__finding__mutmut)
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


def x__finding__mutmut_orig(
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


def x__finding__mutmut_1(
    workload: CiliumWorkload,
    coverage: str,
    restricted: tuple[bool, bool, bool],
) -> CiliumAuditFinding:
    ingress, egress, l7 = None
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


def x__finding__mutmut_2(
    workload: CiliumWorkload,
    coverage: str,
    restricted: tuple[bool, bool, bool],
) -> CiliumAuditFinding:
    ingress, egress, l7 = restricted
    return CiliumAuditFinding(
        namespace=None,
        workload=workload.name,
        coverage=coverage,
        ingress_restricted=ingress,
        egress_restricted=egress,
        l7_restricted=l7,
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def x__finding__mutmut_3(
    workload: CiliumWorkload,
    coverage: str,
    restricted: tuple[bool, bool, bool],
) -> CiliumAuditFinding:
    ingress, egress, l7 = restricted
    return CiliumAuditFinding(
        namespace=workload.namespace,
        workload=None,
        coverage=coverage,
        ingress_restricted=ingress,
        egress_restricted=egress,
        l7_restricted=l7,
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def x__finding__mutmut_4(
    workload: CiliumWorkload,
    coverage: str,
    restricted: tuple[bool, bool, bool],
) -> CiliumAuditFinding:
    ingress, egress, l7 = restricted
    return CiliumAuditFinding(
        namespace=workload.namespace,
        workload=workload.name,
        coverage=None,
        ingress_restricted=ingress,
        egress_restricted=egress,
        l7_restricted=l7,
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def x__finding__mutmut_5(
    workload: CiliumWorkload,
    coverage: str,
    restricted: tuple[bool, bool, bool],
) -> CiliumAuditFinding:
    ingress, egress, l7 = restricted
    return CiliumAuditFinding(
        namespace=workload.namespace,
        workload=workload.name,
        coverage=coverage,
        ingress_restricted=None,
        egress_restricted=egress,
        l7_restricted=l7,
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def x__finding__mutmut_6(
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
        egress_restricted=None,
        l7_restricted=l7,
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def x__finding__mutmut_7(
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
        l7_restricted=None,
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def x__finding__mutmut_8(
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
        risk=None,
        note=_note_for(coverage),
    )


def x__finding__mutmut_9(
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
        note=None,
    )


def x__finding__mutmut_10(
    workload: CiliumWorkload,
    coverage: str,
    restricted: tuple[bool, bool, bool],
) -> CiliumAuditFinding:
    ingress, egress, l7 = restricted
    return CiliumAuditFinding(
        workload=workload.name,
        coverage=coverage,
        ingress_restricted=ingress,
        egress_restricted=egress,
        l7_restricted=l7,
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def x__finding__mutmut_11(
    workload: CiliumWorkload,
    coverage: str,
    restricted: tuple[bool, bool, bool],
) -> CiliumAuditFinding:
    ingress, egress, l7 = restricted
    return CiliumAuditFinding(
        namespace=workload.namespace,
        coverage=coverage,
        ingress_restricted=ingress,
        egress_restricted=egress,
        l7_restricted=l7,
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def x__finding__mutmut_12(
    workload: CiliumWorkload,
    coverage: str,
    restricted: tuple[bool, bool, bool],
) -> CiliumAuditFinding:
    ingress, egress, l7 = restricted
    return CiliumAuditFinding(
        namespace=workload.namespace,
        workload=workload.name,
        ingress_restricted=ingress,
        egress_restricted=egress,
        l7_restricted=l7,
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def x__finding__mutmut_13(
    workload: CiliumWorkload,
    coverage: str,
    restricted: tuple[bool, bool, bool],
) -> CiliumAuditFinding:
    ingress, egress, l7 = restricted
    return CiliumAuditFinding(
        namespace=workload.namespace,
        workload=workload.name,
        coverage=coverage,
        egress_restricted=egress,
        l7_restricted=l7,
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def x__finding__mutmut_14(
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
        l7_restricted=l7,
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def x__finding__mutmut_15(
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
        risk=_COVERAGE_RISK[coverage],
        note=_note_for(coverage),
    )


def x__finding__mutmut_16(
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
        note=_note_for(coverage),
    )


def x__finding__mutmut_17(
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
        )


def x__finding__mutmut_18(
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
        note=_note_for(None),
    )

mutants_x__finding__mutmut['_mutmut_orig'] = x__finding__mutmut_orig # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_1'] = x__finding__mutmut_1 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_2'] = x__finding__mutmut_2 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_3'] = x__finding__mutmut_3 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_4'] = x__finding__mutmut_4 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_5'] = x__finding__mutmut_5 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_6'] = x__finding__mutmut_6 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_7'] = x__finding__mutmut_7 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_8'] = x__finding__mutmut_8 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_9'] = x__finding__mutmut_9 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_10'] = x__finding__mutmut_10 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_11'] = x__finding__mutmut_11 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_12'] = x__finding__mutmut_12 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_13'] = x__finding__mutmut_13 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_14'] = x__finding__mutmut_14 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_15'] = x__finding__mutmut_15 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_16'] = x__finding__mutmut_16 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_17'] = x__finding__mutmut_17 # type: ignore # mutmut generated
mutants_x__finding__mutmut['x__finding__mutmut_18'] = x__finding__mutmut_18 # type: ignore # mutmut generated
mutants_x__note_for__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__note_for__mutmut)
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


def x__note_for__mutmut_orig(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_1(coverage: str) -> str | None:
    if coverage != "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_2(coverage: str) -> str | None:
    if coverage == "XXno_policyXX":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_3(coverage: str) -> str | None:
    if coverage == "NO_POLICY":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_4(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "XXNo Cilium network policy selects this workloadXX"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_5(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "no cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_6(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "NO CILIUM NETWORK POLICY SELECTS THIS WORKLOAD"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_7(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage != "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_8(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "XXno_default_denyXX":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_9(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "NO_DEFAULT_DENY":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_10(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "XXPolicy selects the workload but defines no ingress/egress ruleXX"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_11(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_12(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "POLICY SELECTS THE WORKLOAD BUT DEFINES NO INGRESS/EGRESS RULE"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_13(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage != "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_14(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "XXpartialXX":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_15(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "PARTIAL":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_16(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "XXWorkload partially restricted (ingress or egress only)XX"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_17(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_18(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "WORKLOAD PARTIALLY RESTRICTED (INGRESS OR EGRESS ONLY)"
    if coverage == "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_19(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage != "l7_gap":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_20(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "XXl7_gapXX":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_21(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "L7_GAP":
        return "Workload restricted at L3/L4 but not by an L7 rule"
    return None


def x__note_for__mutmut_22(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "XXWorkload restricted at L3/L4 but not by an L7 ruleXX"
    return None


def x__note_for__mutmut_23(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "workload restricted at l3/l4 but not by an l7 rule"
    return None


def x__note_for__mutmut_24(coverage: str) -> str | None:
    if coverage == "no_policy":
        return "No Cilium network policy selects this workload"
    if coverage == "no_default_deny":
        return "Policy selects the workload but defines no ingress/egress rule"
    if coverage == "partial":
        return "Workload partially restricted (ingress or egress only)"
    if coverage == "l7_gap":
        return "WORKLOAD RESTRICTED AT L3/L4 BUT NOT BY AN L7 RULE"
    return None

mutants_x__note_for__mutmut['_mutmut_orig'] = x__note_for__mutmut_orig # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_1'] = x__note_for__mutmut_1 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_2'] = x__note_for__mutmut_2 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_3'] = x__note_for__mutmut_3 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_4'] = x__note_for__mutmut_4 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_5'] = x__note_for__mutmut_5 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_6'] = x__note_for__mutmut_6 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_7'] = x__note_for__mutmut_7 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_8'] = x__note_for__mutmut_8 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_9'] = x__note_for__mutmut_9 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_10'] = x__note_for__mutmut_10 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_11'] = x__note_for__mutmut_11 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_12'] = x__note_for__mutmut_12 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_13'] = x__note_for__mutmut_13 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_14'] = x__note_for__mutmut_14 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_15'] = x__note_for__mutmut_15 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_16'] = x__note_for__mutmut_16 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_17'] = x__note_for__mutmut_17 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_18'] = x__note_for__mutmut_18 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_19'] = x__note_for__mutmut_19 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_20'] = x__note_for__mutmut_20 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_21'] = x__note_for__mutmut_21 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_22'] = x__note_for__mutmut_22 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_23'] = x__note_for__mutmut_23 # type: ignore # mutmut generated
mutants_x__note_for__mutmut['x__note_for__mutmut_24'] = x__note_for__mutmut_24 # type: ignore # mutmut generated


def _summary(gap_count: int, total: int) -> str:
    return f"{gap_count} workload(s) with a coverage gap out of {total}"
