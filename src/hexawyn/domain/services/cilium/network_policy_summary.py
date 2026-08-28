"""Pure Cilium network-policy rule summarisation — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumNetworkPoliciesResult,
    CiliumNetworkPolicyInfo,
)

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"
_NAMESPACED_KIND = "CiliumNetworkPolicy"
_CLUSTERWIDE_KIND = "CiliumClusterwideNetworkPolicy"


def _as_dict(value: object) -> dict[str, object]:
    return value if isinstance(value, dict) else {}


def build_network_policy(kind: str, raw: dict[str, object]) -> CiliumNetworkPolicyInfo:
    """Extract a policy summary from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    raw_ingress = spec.get("ingress", [])
    raw_egress = spec.get("egress", [])
    ingress = raw_ingress if isinstance(raw_ingress, list) else []
    egress = raw_egress if isinstance(raw_egress, list) else []
    l7_count, l7_protocols = _l7_summary(ingress, egress)
    namespace = metadata.get("namespace")
    return CiliumNetworkPolicyInfo(
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=str(namespace) if namespace else None,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        l7_rule_count=l7_count,
        l7_protocols=l7_protocols,
    )


def build_policies_result(
    policies: list[CiliumNetworkPolicyInfo],
) -> CiliumNetworkPoliciesResult:
    """Wrap a policy inventory with kind breakdown and an honest status."""
    namespaced = sum(1 for policy in policies if policy.kind == _NAMESPACED_KIND)
    clusterwide = sum(1 for policy in policies if policy.kind == _CLUSTERWIDE_KIND)
    return CiliumNetworkPoliciesResult(
        installed=True,
        status="present" if policies else "empty",
        total_policies=len(policies),
        namespaced_count=namespaced,
        clusterwide_count=clusterwide,
        policies=policies,
        note=None if policies else "No Cilium network policies found",
    )


def not_installed_policies_result() -> CiliumNetworkPoliciesResult:
    """Honest NOT_INSTALLED marker — no fabricated policies."""
    return CiliumNetworkPoliciesResult(
        installed=False,
        status="not_installed",
        total_policies=0,
        namespaced_count=0,
        clusterwide_count=0,
        policies=[],
        note=_NOT_INSTALLED_NOTE,
    )


def _render_selector(selector: object) -> str:
    """Render an endpoint selector, preserving malformed values as-is."""
    if selector is None:
        return "matchLabels: {}"
    if isinstance(selector, dict):
        match_labels = selector.get("matchLabels")
        labels = match_labels if isinstance(match_labels, dict) else {}
        if labels:
            pairs = ", ".join(f"{key}={value}" for key, value in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return "matchLabels: {}"
    return str(selector)


def _l7_summary(ingress: list[object], egress: list[object]) -> tuple[int, tuple[str, ...]]:
    """Count L7-aware ports and collect the raw protocol names (http, dns…)."""
    protocols: set[str] = set()
    count = 0
    for rule in [*ingress, *egress]:
        if not isinstance(rule, dict):
            continue
        to_ports = rule.get("toPorts", [])
        if not isinstance(to_ports, list):
            continue
        for port in to_ports:
            if not isinstance(port, dict):
                continue
            rules = port.get("rules", {})
            if not isinstance(rules, dict) or not rules:
                continue
            count += 1
            for protocol in rules:
                if isinstance(protocol, str):
                    protocols.add(protocol)
    return count, tuple(sorted(protocols))
