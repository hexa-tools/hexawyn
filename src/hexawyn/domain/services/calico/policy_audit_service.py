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


def _is_default_deny(policy: CalicoNetworkPolicy) -> bool:
    return policy.action in ("deny", "mixed")


def _is_broad(selector: str) -> bool:
    return selector in _BROAD_SELECTORS


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


def _rank_key(gap: CalicoCoverageGap) -> tuple[int, int]:
    return (_RISK_ORDER.get(gap.risk_level, 2), -gap.workload_count)


def _summary(gap_count: int, checked: int) -> str:
    if gap_count == 0:
        return f"No Calico L3/L4 coverage gaps out of {checked} namespace(s) checked."
    return f"{gap_count} namespace(s) have Calico L3/L4 coverage gaps out of {checked} checked."
