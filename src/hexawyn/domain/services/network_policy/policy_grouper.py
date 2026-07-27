from __future__ import annotations

from hexawyn.application.ports.driven.network_policy_audit_port import NetworkPolicyRaw
from hexawyn.domain.models.constants import NetworkPolicyConstants
from hexawyn.domain.models.network_policy import NetworkStatus

_cfg = NetworkPolicyConstants()


def group_policies_by_namespace(
    policies_raw: list[NetworkPolicyRaw],
) -> dict[str, list[NetworkPolicyRaw]]:
    grouped: dict[str, list[NetworkPolicyRaw]] = {}
    for policy in policies_raw:
        grouped.setdefault(policy["namespace"], []).append(policy)
    return grouped


def build_note(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_cfg.calico_note)
        if has_istio_strict:
            notes.append(_cfg.istio_note)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace "
            "(empty podSelector)"
        )

    return "; ".join(notes) if notes else None
