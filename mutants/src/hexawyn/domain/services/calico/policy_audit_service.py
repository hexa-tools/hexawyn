"""Pure Calico policy coverage audit — no infrastructure imports.

Compares Calico endpoint selectors against cluster workloads and flags
namespaces whose workloads are not restricted by a default-deny L3/L4 policy
(and, when L3/L4 is covered, those lacking an L7 rule). Findings are ranked by
risk using the existing ``risk_classifier`` logic.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence

from hexawyn.domain.models.calico import (
    CalicoCoverageGap,
    CalicoNetworkPolicy,
    CalicoPolicyAuditResult,
    CalicoWorkload,
)
from hexawyn.domain.models.constants import NetworkPolicyConstants
from hexawyn.domain.models.network_policy import NetworkStatus
from hexawyn.domain.services.network_policy.risk_classifier import classify_risk_level

_KIND_GLOBAL = "GlobalNetworkPolicy"
_RISK_ORDER = {"critical": 0, "medium": 1, "low": 2}
_BROAD_SELECTORS = {"", "all()"}
_DEFAULT_EXCLUDED = NetworkPolicyConstants().system_namespaces


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_calico_policy_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_calico_policy_audit__mutmut)
def build_calico_policy_audit(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_orig(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_1(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = None

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_2(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(None) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_3(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_4(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(None)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_5(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = None
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_6(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = None
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_7(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind != _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_8(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(None)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_9(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(None)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_10(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(None, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_11(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, None).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_12(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault([]).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_13(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, ).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_14(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = None

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_15(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(None)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_16(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = None

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_17(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 or workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_18(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count >= 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_19(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 1 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_20(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_21(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = None
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_22(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = None
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_23(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) - broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_24(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(None, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_25(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, None) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_26(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get([]) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_27(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, ) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_28(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = None
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_29(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = None
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_30(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(None)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_31(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count >= 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_32(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 1 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_33(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = None
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_34(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(None)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_35(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count >= 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_36(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 1 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_37(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = None
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_38(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(None)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_39(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(None) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_40(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = None

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_41(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(None)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_42(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = None
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_43(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(None, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_44(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, None, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_45(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, None, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_46(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, None)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_47(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_48(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_49(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_50(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, )
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_51(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status == "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_52(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "XXrestrictedXX":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_53(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "RESTRICTED":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_54(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = None
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_55(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "XXno_policyXX" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_56(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "NO_POLICY" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_57(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count != 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_58(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 1 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_59(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "XXno_default_denyXX"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_60(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "NO_DEFAULT_DENY"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_61(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = None
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_62(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(None, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_63(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, None)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_64(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_65(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, )
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_66(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(None)
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_67(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(None, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_68(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, None, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_69(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, None, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_70(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, None, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_71(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, None, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_72(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, None))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_73(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_74(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_75(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_76(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_77(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_78(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, ))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_79(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_80(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = None
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_81(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(None, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_82(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, None)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_83(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_84(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, )
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_85(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(None)

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_86(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(None, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_87(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, None, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_88(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, None, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_89(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, None, risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_90(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", None, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_91(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, None))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_92(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_93(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_94(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_95(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_96(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_97(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, ))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_98(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "XXl7_gapXX", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_99(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "L7_GAP", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_100(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=None)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_101(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=None,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_102(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=None,
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_103(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=None,
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_104(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=None,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_105(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=None,
        error=None,
    )


def x_build_calico_policy_audit__mutmut_106(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_107(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_108(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_109(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_110(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_111(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        error=None,
    )


def x_build_calico_policy_audit__mutmut_112(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        )


def x_build_calico_policy_audit__mutmut_113(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=False,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_114(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(None, len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_115(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), None),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_116(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(checked)),
        error=None,
    )


def x_build_calico_policy_audit__mutmut_117(
    *,
    workloads: Sequence[CalicoWorkload],
    policies: Sequence[CalicoNetworkPolicy],
    excluded_namespaces: Iterable[str] | None = None,
) -> CalicoPolicyAuditResult:
    """Audit Calico L3/L4 (and L7) coverage and rank the gaps by risk."""
    excluded = (
        set(excluded_namespaces) if excluded_namespaces is not None else set(_DEFAULT_EXCLUDED)
    )

    ns_policies: dict[str, list[CalicoNetworkPolicy]] = {}
    global_policies: list[CalicoNetworkPolicy] = []
    for policy in policies:
        if policy.kind == _KIND_GLOBAL:
            global_policies.append(policy)
        else:
            ns_policies.setdefault(policy.namespace, []).append(policy)

    broad_globals = [policy for policy in global_policies if _is_broad(policy.selector)]

    checked = [
        workload
        for workload in workloads
        if workload.pod_count > 0 and workload.namespace not in excluded
    ]

    findings: list[CalicoCoverageGap] = []
    for workload in checked:
        applicable = ns_policies.get(workload.namespace, []) + broad_globals
        policy_count = len(applicable)
        has_ingress = any(policy.ingress_rule_count > 0 for policy in applicable)
        has_egress = any(policy.egress_rule_count > 0 for policy in applicable)
        has_default_deny = any(_is_default_deny(policy) for policy in applicable)
        has_l7 = any(policy.has_l7_rule for policy in applicable)

        status = _status(applicable, has_default_deny, has_ingress, has_egress)
        if status != "restricted":
            issue = "no_policy" if policy_count == 0 else "no_default_deny"
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, issue, risk, applicable))
        elif not has_l7:
            risk = classify_risk_level(status, workload.pod_count)
            findings.append(_gap(workload, policy_count, status, "l7_gap", risk, applicable))

    findings.sort(key=_rank_key)
    return CalicoPolicyAuditResult(
        installed=True,
        not_installed_marker=None,
        total_namespaces_checked=len(checked),
        gap_count=len(findings),
        findings=findings,
        summary=_summary(len(findings), ),
        error=None,
    )

mutants_x_build_calico_policy_audit__mutmut['_mutmut_orig'] = x_build_calico_policy_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_1'] = x_build_calico_policy_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_2'] = x_build_calico_policy_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_3'] = x_build_calico_policy_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_4'] = x_build_calico_policy_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_5'] = x_build_calico_policy_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_6'] = x_build_calico_policy_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_7'] = x_build_calico_policy_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_8'] = x_build_calico_policy_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_9'] = x_build_calico_policy_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_10'] = x_build_calico_policy_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_11'] = x_build_calico_policy_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_12'] = x_build_calico_policy_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_13'] = x_build_calico_policy_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_14'] = x_build_calico_policy_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_15'] = x_build_calico_policy_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_16'] = x_build_calico_policy_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_17'] = x_build_calico_policy_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_18'] = x_build_calico_policy_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_19'] = x_build_calico_policy_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_20'] = x_build_calico_policy_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_21'] = x_build_calico_policy_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_22'] = x_build_calico_policy_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_23'] = x_build_calico_policy_audit__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_24'] = x_build_calico_policy_audit__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_25'] = x_build_calico_policy_audit__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_26'] = x_build_calico_policy_audit__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_27'] = x_build_calico_policy_audit__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_28'] = x_build_calico_policy_audit__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_29'] = x_build_calico_policy_audit__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_30'] = x_build_calico_policy_audit__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_31'] = x_build_calico_policy_audit__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_32'] = x_build_calico_policy_audit__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_33'] = x_build_calico_policy_audit__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_34'] = x_build_calico_policy_audit__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_35'] = x_build_calico_policy_audit__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_36'] = x_build_calico_policy_audit__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_37'] = x_build_calico_policy_audit__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_38'] = x_build_calico_policy_audit__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_39'] = x_build_calico_policy_audit__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_40'] = x_build_calico_policy_audit__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_41'] = x_build_calico_policy_audit__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_42'] = x_build_calico_policy_audit__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_43'] = x_build_calico_policy_audit__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_44'] = x_build_calico_policy_audit__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_45'] = x_build_calico_policy_audit__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_46'] = x_build_calico_policy_audit__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_47'] = x_build_calico_policy_audit__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_48'] = x_build_calico_policy_audit__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_49'] = x_build_calico_policy_audit__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_50'] = x_build_calico_policy_audit__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_51'] = x_build_calico_policy_audit__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_52'] = x_build_calico_policy_audit__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_53'] = x_build_calico_policy_audit__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_54'] = x_build_calico_policy_audit__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_55'] = x_build_calico_policy_audit__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_56'] = x_build_calico_policy_audit__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_57'] = x_build_calico_policy_audit__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_58'] = x_build_calico_policy_audit__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_59'] = x_build_calico_policy_audit__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_60'] = x_build_calico_policy_audit__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_61'] = x_build_calico_policy_audit__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_62'] = x_build_calico_policy_audit__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_63'] = x_build_calico_policy_audit__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_64'] = x_build_calico_policy_audit__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_65'] = x_build_calico_policy_audit__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_66'] = x_build_calico_policy_audit__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_67'] = x_build_calico_policy_audit__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_68'] = x_build_calico_policy_audit__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_69'] = x_build_calico_policy_audit__mutmut_69 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_70'] = x_build_calico_policy_audit__mutmut_70 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_71'] = x_build_calico_policy_audit__mutmut_71 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_72'] = x_build_calico_policy_audit__mutmut_72 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_73'] = x_build_calico_policy_audit__mutmut_73 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_74'] = x_build_calico_policy_audit__mutmut_74 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_75'] = x_build_calico_policy_audit__mutmut_75 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_76'] = x_build_calico_policy_audit__mutmut_76 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_77'] = x_build_calico_policy_audit__mutmut_77 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_78'] = x_build_calico_policy_audit__mutmut_78 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_79'] = x_build_calico_policy_audit__mutmut_79 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_80'] = x_build_calico_policy_audit__mutmut_80 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_81'] = x_build_calico_policy_audit__mutmut_81 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_82'] = x_build_calico_policy_audit__mutmut_82 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_83'] = x_build_calico_policy_audit__mutmut_83 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_84'] = x_build_calico_policy_audit__mutmut_84 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_85'] = x_build_calico_policy_audit__mutmut_85 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_86'] = x_build_calico_policy_audit__mutmut_86 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_87'] = x_build_calico_policy_audit__mutmut_87 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_88'] = x_build_calico_policy_audit__mutmut_88 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_89'] = x_build_calico_policy_audit__mutmut_89 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_90'] = x_build_calico_policy_audit__mutmut_90 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_91'] = x_build_calico_policy_audit__mutmut_91 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_92'] = x_build_calico_policy_audit__mutmut_92 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_93'] = x_build_calico_policy_audit__mutmut_93 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_94'] = x_build_calico_policy_audit__mutmut_94 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_95'] = x_build_calico_policy_audit__mutmut_95 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_96'] = x_build_calico_policy_audit__mutmut_96 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_97'] = x_build_calico_policy_audit__mutmut_97 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_98'] = x_build_calico_policy_audit__mutmut_98 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_99'] = x_build_calico_policy_audit__mutmut_99 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_100'] = x_build_calico_policy_audit__mutmut_100 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_101'] = x_build_calico_policy_audit__mutmut_101 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_102'] = x_build_calico_policy_audit__mutmut_102 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_103'] = x_build_calico_policy_audit__mutmut_103 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_104'] = x_build_calico_policy_audit__mutmut_104 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_105'] = x_build_calico_policy_audit__mutmut_105 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_106'] = x_build_calico_policy_audit__mutmut_106 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_107'] = x_build_calico_policy_audit__mutmut_107 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_108'] = x_build_calico_policy_audit__mutmut_108 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_109'] = x_build_calico_policy_audit__mutmut_109 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_110'] = x_build_calico_policy_audit__mutmut_110 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_111'] = x_build_calico_policy_audit__mutmut_111 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_112'] = x_build_calico_policy_audit__mutmut_112 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_113'] = x_build_calico_policy_audit__mutmut_113 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_114'] = x_build_calico_policy_audit__mutmut_114 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_115'] = x_build_calico_policy_audit__mutmut_115 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_116'] = x_build_calico_policy_audit__mutmut_116 # type: ignore # mutmut generated
mutants_x_build_calico_policy_audit__mutmut['x_build_calico_policy_audit__mutmut_117'] = x_build_calico_policy_audit__mutmut_117 # type: ignore # mutmut generated
mutants_x__status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__status__mutmut)
def _status(
    applicable: list[CalicoNetworkPolicy],
    has_default_deny: bool,
    has_ingress: bool,
    has_egress: bool,
) -> NetworkStatus:
    if not applicable:
        return "open"
    if has_default_deny:
        return "restricted"
    if has_ingress or has_egress:
        return "partially_restricted"
    return "open"


def x__status__mutmut_orig(
    applicable: list[CalicoNetworkPolicy],
    has_default_deny: bool,
    has_ingress: bool,
    has_egress: bool,
) -> NetworkStatus:
    if not applicable:
        return "open"
    if has_default_deny:
        return "restricted"
    if has_ingress or has_egress:
        return "partially_restricted"
    return "open"


def x__status__mutmut_1(
    applicable: list[CalicoNetworkPolicy],
    has_default_deny: bool,
    has_ingress: bool,
    has_egress: bool,
) -> NetworkStatus:
    if applicable:
        return "open"
    if has_default_deny:
        return "restricted"
    if has_ingress or has_egress:
        return "partially_restricted"
    return "open"


def x__status__mutmut_2(
    applicable: list[CalicoNetworkPolicy],
    has_default_deny: bool,
    has_ingress: bool,
    has_egress: bool,
) -> NetworkStatus:
    if not applicable:
        return "XXopenXX"
    if has_default_deny:
        return "restricted"
    if has_ingress or has_egress:
        return "partially_restricted"
    return "open"


def x__status__mutmut_3(
    applicable: list[CalicoNetworkPolicy],
    has_default_deny: bool,
    has_ingress: bool,
    has_egress: bool,
) -> NetworkStatus:
    if not applicable:
        return "OPEN"
    if has_default_deny:
        return "restricted"
    if has_ingress or has_egress:
        return "partially_restricted"
    return "open"


def x__status__mutmut_4(
    applicable: list[CalicoNetworkPolicy],
    has_default_deny: bool,
    has_ingress: bool,
    has_egress: bool,
) -> NetworkStatus:
    if not applicable:
        return "open"
    if has_default_deny:
        return "XXrestrictedXX"
    if has_ingress or has_egress:
        return "partially_restricted"
    return "open"


def x__status__mutmut_5(
    applicable: list[CalicoNetworkPolicy],
    has_default_deny: bool,
    has_ingress: bool,
    has_egress: bool,
) -> NetworkStatus:
    if not applicable:
        return "open"
    if has_default_deny:
        return "RESTRICTED"
    if has_ingress or has_egress:
        return "partially_restricted"
    return "open"


def x__status__mutmut_6(
    applicable: list[CalicoNetworkPolicy],
    has_default_deny: bool,
    has_ingress: bool,
    has_egress: bool,
) -> NetworkStatus:
    if not applicable:
        return "open"
    if has_default_deny:
        return "restricted"
    if has_ingress and has_egress:
        return "partially_restricted"
    return "open"


def x__status__mutmut_7(
    applicable: list[CalicoNetworkPolicy],
    has_default_deny: bool,
    has_ingress: bool,
    has_egress: bool,
) -> NetworkStatus:
    if not applicable:
        return "open"
    if has_default_deny:
        return "restricted"
    if has_ingress or has_egress:
        return "XXpartially_restrictedXX"
    return "open"


def x__status__mutmut_8(
    applicable: list[CalicoNetworkPolicy],
    has_default_deny: bool,
    has_ingress: bool,
    has_egress: bool,
) -> NetworkStatus:
    if not applicable:
        return "open"
    if has_default_deny:
        return "restricted"
    if has_ingress or has_egress:
        return "PARTIALLY_RESTRICTED"
    return "open"


def x__status__mutmut_9(
    applicable: list[CalicoNetworkPolicy],
    has_default_deny: bool,
    has_ingress: bool,
    has_egress: bool,
) -> NetworkStatus:
    if not applicable:
        return "open"
    if has_default_deny:
        return "restricted"
    if has_ingress or has_egress:
        return "partially_restricted"
    return "XXopenXX"


def x__status__mutmut_10(
    applicable: list[CalicoNetworkPolicy],
    has_default_deny: bool,
    has_ingress: bool,
    has_egress: bool,
) -> NetworkStatus:
    if not applicable:
        return "open"
    if has_default_deny:
        return "restricted"
    if has_ingress or has_egress:
        return "partially_restricted"
    return "OPEN"

mutants_x__status__mutmut['_mutmut_orig'] = x__status__mutmut_orig # type: ignore # mutmut generated
mutants_x__status__mutmut['x__status__mutmut_1'] = x__status__mutmut_1 # type: ignore # mutmut generated
mutants_x__status__mutmut['x__status__mutmut_2'] = x__status__mutmut_2 # type: ignore # mutmut generated
mutants_x__status__mutmut['x__status__mutmut_3'] = x__status__mutmut_3 # type: ignore # mutmut generated
mutants_x__status__mutmut['x__status__mutmut_4'] = x__status__mutmut_4 # type: ignore # mutmut generated
mutants_x__status__mutmut['x__status__mutmut_5'] = x__status__mutmut_5 # type: ignore # mutmut generated
mutants_x__status__mutmut['x__status__mutmut_6'] = x__status__mutmut_6 # type: ignore # mutmut generated
mutants_x__status__mutmut['x__status__mutmut_7'] = x__status__mutmut_7 # type: ignore # mutmut generated
mutants_x__status__mutmut['x__status__mutmut_8'] = x__status__mutmut_8 # type: ignore # mutmut generated
mutants_x__status__mutmut['x__status__mutmut_9'] = x__status__mutmut_9 # type: ignore # mutmut generated
mutants_x__status__mutmut['x__status__mutmut_10'] = x__status__mutmut_10 # type: ignore # mutmut generated
mutants_x__is_default_deny__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_default_deny__mutmut)
def _is_default_deny(policy: CalicoNetworkPolicy) -> bool:
    return policy.action in ("deny", "mixed")


def x__is_default_deny__mutmut_orig(policy: CalicoNetworkPolicy) -> bool:
    return policy.action in ("deny", "mixed")


def x__is_default_deny__mutmut_1(policy: CalicoNetworkPolicy) -> bool:
    return policy.action not in ("deny", "mixed")


def x__is_default_deny__mutmut_2(policy: CalicoNetworkPolicy) -> bool:
    return policy.action in ("XXdenyXX", "mixed")


def x__is_default_deny__mutmut_3(policy: CalicoNetworkPolicy) -> bool:
    return policy.action in ("DENY", "mixed")


def x__is_default_deny__mutmut_4(policy: CalicoNetworkPolicy) -> bool:
    return policy.action in ("deny", "XXmixedXX")


def x__is_default_deny__mutmut_5(policy: CalicoNetworkPolicy) -> bool:
    return policy.action in ("deny", "MIXED")

mutants_x__is_default_deny__mutmut['_mutmut_orig'] = x__is_default_deny__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_default_deny__mutmut['x__is_default_deny__mutmut_1'] = x__is_default_deny__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_default_deny__mutmut['x__is_default_deny__mutmut_2'] = x__is_default_deny__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_default_deny__mutmut['x__is_default_deny__mutmut_3'] = x__is_default_deny__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_default_deny__mutmut['x__is_default_deny__mutmut_4'] = x__is_default_deny__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_default_deny__mutmut['x__is_default_deny__mutmut_5'] = x__is_default_deny__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_broad__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_broad__mutmut)
def _is_broad(selector: str) -> bool:
    return selector in _BROAD_SELECTORS


def x__is_broad__mutmut_orig(selector: str) -> bool:
    return selector in _BROAD_SELECTORS


def x__is_broad__mutmut_1(selector: str) -> bool:
    return selector not in _BROAD_SELECTORS

mutants_x__is_broad__mutmut['_mutmut_orig'] = x__is_broad__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_broad__mutmut['x__is_broad__mutmut_1'] = x__is_broad__mutmut_1 # type: ignore # mutmut generated
mutants_x__gap__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__gap__mutmut)
def _gap(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_orig(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_1(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = None
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_2(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] and []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_3(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=None,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_4(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=None,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_5(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=None,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_6(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=None,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_7(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=None,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_8(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=None,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_9(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=None,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_10(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=None,
    )


def x__gap__mutmut_11(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_12(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_13(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_14(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_15(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_16(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_17(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        note=_build_note(issue, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_18(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        )


def x__gap__mutmut_19(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(None, workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_20(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, None, workload.pod_count),
    )


def x__gap__mutmut_21(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, None),
    )


def x__gap__mutmut_22(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(workload.namespace, workload.pod_count),
    )


def x__gap__mutmut_23(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.pod_count),
    )


def x__gap__mutmut_24(  # noqa: PLR0913
    workload: CalicoWorkload,
    policy_count: int,
    status: NetworkStatus,
    issue: str,
    risk: str,
    applicable: list[CalicoNetworkPolicy],
) -> CalicoCoverageGap:
    selectors = [policy.selector for policy in applicable if policy.selector] or []
    return CalicoCoverageGap(
        namespace=workload.namespace,
        workload_count=workload.pod_count,
        policy_count=policy_count,
        issue=issue,
        network_status=status,
        risk_level=risk,
        selectors=selectors,
        note=_build_note(issue, workload.namespace, ),
    )

mutants_x__gap__mutmut['_mutmut_orig'] = x__gap__mutmut_orig # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_1'] = x__gap__mutmut_1 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_2'] = x__gap__mutmut_2 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_3'] = x__gap__mutmut_3 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_4'] = x__gap__mutmut_4 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_5'] = x__gap__mutmut_5 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_6'] = x__gap__mutmut_6 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_7'] = x__gap__mutmut_7 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_8'] = x__gap__mutmut_8 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_9'] = x__gap__mutmut_9 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_10'] = x__gap__mutmut_10 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_11'] = x__gap__mutmut_11 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_12'] = x__gap__mutmut_12 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_13'] = x__gap__mutmut_13 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_14'] = x__gap__mutmut_14 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_15'] = x__gap__mutmut_15 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_16'] = x__gap__mutmut_16 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_17'] = x__gap__mutmut_17 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_18'] = x__gap__mutmut_18 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_19'] = x__gap__mutmut_19 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_20'] = x__gap__mutmut_20 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_21'] = x__gap__mutmut_21 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_22'] = x__gap__mutmut_22 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_23'] = x__gap__mutmut_23 # type: ignore # mutmut generated
mutants_x__gap__mutmut['x__gap__mutmut_24'] = x__gap__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_note__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_note__mutmut)
def _build_note(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "no_policy":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "no_default_deny":
        return (
            "Partial L3/L4 coverage; no default-deny (deny rule) present for "
            f"{workload_count} workload(s)"
        )
    return (
        "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for " f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_orig(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "no_policy":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "no_default_deny":
        return (
            "Partial L3/L4 coverage; no default-deny (deny rule) present for "
            f"{workload_count} workload(s)"
        )
    return (
        "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for " f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_1(issue: str, namespace: str, workload_count: int) -> str:
    if issue != "no_policy":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "no_default_deny":
        return (
            "Partial L3/L4 coverage; no default-deny (deny rule) present for "
            f"{workload_count} workload(s)"
        )
    return (
        "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for " f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_2(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "XXno_policyXX":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "no_default_deny":
        return (
            "Partial L3/L4 coverage; no default-deny (deny rule) present for "
            f"{workload_count} workload(s)"
        )
    return (
        "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for " f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_3(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "NO_POLICY":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "no_default_deny":
        return (
            "Partial L3/L4 coverage; no default-deny (deny rule) present for "
            f"{workload_count} workload(s)"
        )
    return (
        "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for " f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_4(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "no_policy":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue != "no_default_deny":
        return (
            "Partial L3/L4 coverage; no default-deny (deny rule) present for "
            f"{workload_count} workload(s)"
        )
    return (
        "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for " f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_5(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "no_policy":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "XXno_default_denyXX":
        return (
            "Partial L3/L4 coverage; no default-deny (deny rule) present for "
            f"{workload_count} workload(s)"
        )
    return (
        "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for " f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_6(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "no_policy":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "NO_DEFAULT_DENY":
        return (
            "Partial L3/L4 coverage; no default-deny (deny rule) present for "
            f"{workload_count} workload(s)"
        )
    return (
        "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for " f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_7(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "no_policy":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "no_default_deny":
        return (
            "XXPartial L3/L4 coverage; no default-deny (deny rule) present for XX"
            f"{workload_count} workload(s)"
        )
    return (
        "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for " f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_8(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "no_policy":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "no_default_deny":
        return (
            "partial l3/l4 coverage; no default-deny (deny rule) present for "
            f"{workload_count} workload(s)"
        )
    return (
        "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for " f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_9(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "no_policy":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "no_default_deny":
        return (
            "PARTIAL L3/L4 COVERAGE; NO DEFAULT-DENY (DENY RULE) PRESENT FOR "
            f"{workload_count} workload(s)"
        )
    return (
        "L3/L4 default-deny present but no L7 (HTTP/TLS) rule for " f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_10(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "no_policy":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "no_default_deny":
        return (
            "Partial L3/L4 coverage; no default-deny (deny rule) present for "
            f"{workload_count} workload(s)"
        )
    return (
        "XXL3/L4 default-deny present but no L7 (HTTP/TLS) rule for XX" f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_11(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "no_policy":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "no_default_deny":
        return (
            "Partial L3/L4 coverage; no default-deny (deny rule) present for "
            f"{workload_count} workload(s)"
        )
    return (
        "l3/l4 default-deny present but no l7 (http/tls) rule for " f"{workload_count} workload(s)"
    )


def x__build_note__mutmut_12(issue: str, namespace: str, workload_count: int) -> str:
    if issue == "no_policy":
        return f"No Calico policy restricts {workload_count} workload(s) in namespace '{namespace}'"
    if issue == "no_default_deny":
        return (
            "Partial L3/L4 coverage; no default-deny (deny rule) present for "
            f"{workload_count} workload(s)"
        )
    return (
        "L3/L4 DEFAULT-DENY PRESENT BUT NO L7 (HTTP/TLS) RULE FOR " f"{workload_count} workload(s)"
    )

mutants_x__build_note__mutmut['_mutmut_orig'] = x__build_note__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_note__mutmut['x__build_note__mutmut_1'] = x__build_note__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_note__mutmut['x__build_note__mutmut_2'] = x__build_note__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_note__mutmut['x__build_note__mutmut_3'] = x__build_note__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_note__mutmut['x__build_note__mutmut_4'] = x__build_note__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_note__mutmut['x__build_note__mutmut_5'] = x__build_note__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_note__mutmut['x__build_note__mutmut_6'] = x__build_note__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_note__mutmut['x__build_note__mutmut_7'] = x__build_note__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_note__mutmut['x__build_note__mutmut_8'] = x__build_note__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_note__mutmut['x__build_note__mutmut_9'] = x__build_note__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_note__mutmut['x__build_note__mutmut_10'] = x__build_note__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_note__mutmut['x__build_note__mutmut_11'] = x__build_note__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_note__mutmut['x__build_note__mutmut_12'] = x__build_note__mutmut_12 # type: ignore # mutmut generated
mutants_x__rank_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__rank_key__mutmut)
def _rank_key(gap: CalicoCoverageGap) -> tuple[int, int]:
    return (_RISK_ORDER.get(gap.risk_level, 2), -gap.workload_count)


def x__rank_key__mutmut_orig(gap: CalicoCoverageGap) -> tuple[int, int]:
    return (_RISK_ORDER.get(gap.risk_level, 2), -gap.workload_count)


def x__rank_key__mutmut_1(gap: CalicoCoverageGap) -> tuple[int, int]:
    return (_RISK_ORDER.get(None, 2), -gap.workload_count)


def x__rank_key__mutmut_2(gap: CalicoCoverageGap) -> tuple[int, int]:
    return (_RISK_ORDER.get(gap.risk_level, None), -gap.workload_count)


def x__rank_key__mutmut_3(gap: CalicoCoverageGap) -> tuple[int, int]:
    return (_RISK_ORDER.get(2), -gap.workload_count)


def x__rank_key__mutmut_4(gap: CalicoCoverageGap) -> tuple[int, int]:
    return (_RISK_ORDER.get(gap.risk_level, ), -gap.workload_count)


def x__rank_key__mutmut_5(gap: CalicoCoverageGap) -> tuple[int, int]:
    return (_RISK_ORDER.get(gap.risk_level, 3), -gap.workload_count)


def x__rank_key__mutmut_6(gap: CalicoCoverageGap) -> tuple[int, int]:
    return (_RISK_ORDER.get(gap.risk_level, 2), +gap.workload_count)

mutants_x__rank_key__mutmut['_mutmut_orig'] = x__rank_key__mutmut_orig # type: ignore # mutmut generated
mutants_x__rank_key__mutmut['x__rank_key__mutmut_1'] = x__rank_key__mutmut_1 # type: ignore # mutmut generated
mutants_x__rank_key__mutmut['x__rank_key__mutmut_2'] = x__rank_key__mutmut_2 # type: ignore # mutmut generated
mutants_x__rank_key__mutmut['x__rank_key__mutmut_3'] = x__rank_key__mutmut_3 # type: ignore # mutmut generated
mutants_x__rank_key__mutmut['x__rank_key__mutmut_4'] = x__rank_key__mutmut_4 # type: ignore # mutmut generated
mutants_x__rank_key__mutmut['x__rank_key__mutmut_5'] = x__rank_key__mutmut_5 # type: ignore # mutmut generated
mutants_x__rank_key__mutmut['x__rank_key__mutmut_6'] = x__rank_key__mutmut_6 # type: ignore # mutmut generated
mutants_x__summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__summary__mutmut)
def _summary(gap_count: int, checked: int) -> str:
    if gap_count == 0:
        return f"No Calico L3/L4 coverage gaps out of {checked} namespace(s) checked."
    return f"{gap_count} namespace(s) have Calico L3/L4 coverage gaps out of {checked} checked."


def x__summary__mutmut_orig(gap_count: int, checked: int) -> str:
    if gap_count == 0:
        return f"No Calico L3/L4 coverage gaps out of {checked} namespace(s) checked."
    return f"{gap_count} namespace(s) have Calico L3/L4 coverage gaps out of {checked} checked."


def x__summary__mutmut_1(gap_count: int, checked: int) -> str:
    if gap_count != 0:
        return f"No Calico L3/L4 coverage gaps out of {checked} namespace(s) checked."
    return f"{gap_count} namespace(s) have Calico L3/L4 coverage gaps out of {checked} checked."


def x__summary__mutmut_2(gap_count: int, checked: int) -> str:
    if gap_count == 1:
        return f"No Calico L3/L4 coverage gaps out of {checked} namespace(s) checked."
    return f"{gap_count} namespace(s) have Calico L3/L4 coverage gaps out of {checked} checked."

mutants_x__summary__mutmut['_mutmut_orig'] = x__summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_1'] = x__summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_2'] = x__summary__mutmut_2 # type: ignore # mutmut generated
