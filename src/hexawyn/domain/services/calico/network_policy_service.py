"""Pure Calico network-policy rule extraction — no infrastructure imports.

Parses the ``projectcalico.org/v3`` CRD payloads (namespaced
``CalicoNetworkPolicy`` and cluster-scope ``GlobalNetworkPolicy``) into the
frozen ``CalicoNetworkPolicy`` model, deriving the per-rule summary and the
policy-level action. Field values that cannot be interpreted are preserved as
observed — never fabricated.
"""

from __future__ import annotations

from collections.abc import Mapping

from hexawyn.domain.models.calico import CalicoNetworkPolicy

_KIND_NAMESPACED = "CalicoNetworkPolicy"
_KIND_GLOBAL = "GlobalNetworkPolicy"


def parse_calico_network_policy(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a namespaced CalicoNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace=str(meta.get("namespace", "")),
        kind=_KIND_NAMESPACED,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
    )


def parse_global_network_policy(item: Mapping[str, object]) -> CalicoNetworkPolicy:
    """Parse a cluster-scope GlobalNetworkPolicy CRD payload."""
    meta = _as_mapping(item.get("metadata"))
    spec = _as_mapping(item.get("spec"))
    ingress = _rules(spec.get("ingress"))
    egress = _rules(spec.get("egress"))
    return CalicoNetworkPolicy(
        name=str(meta.get("name", "")),
        namespace="",
        kind=_KIND_GLOBAL,
        order=_order(spec),
        selector=str(spec.get("selector", "")),
        ingress_rules=tuple(_summarize_rule(rule) for rule in ingress),
        egress_rules=tuple(_summarize_rule(rule) for rule in egress),
        ingress_rule_count=len(ingress),
        egress_rule_count=len(egress),
        action=resolve_action(ingress, egress),
        apply_on_forward=bool(spec.get("applyOnForward", False)),
    )


def resolve_action(ingress: list[dict[str, object]], egress: list[dict[str, object]]) -> str | None:
    """Derive a policy-level action from the observed rule actions.

    - all ``Allow``  -> ``"allow"``
    - all ``Deny``   -> ``"deny"``
    - a single other action (e.g. ``Log``) is preserved as-is (raw)
    - any mix        -> ``"mixed"``
    - no rules       -> ``None``
    """
    actions = {
        str(rule.get("action", "")).lower()
        for rule in ingress + egress
        if isinstance(rule, dict) and rule.get("action")
    }
    if not actions:
        return None
    lowered = sorted(actions)
    if len(lowered) == 1:
        return lowered[0]
    return "mixed"


def _as_mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _order(spec: Mapping[str, object]) -> float:
    try:
        return float(spec.get("order", 0.0))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def _rules(raw: object) -> list[dict[str, object]]:
    if not isinstance(raw, list):
        return []
    return [rule for rule in raw if isinstance(rule, dict)]


def _summarize_rule(rule: dict[str, object]) -> str:
    """Compact, human-readable rule summary (action [protocol [ports]])."""
    action = str(rule.get("action", "allow")).lower()
    protocol = str(rule.get("protocol", "")).lower()
    destination = _as_mapping(rule.get("destination"))
    ports = destination.get("ports") or destination.get("port") or ""
    if isinstance(ports, list):
        ports = ",".join(str(port) for port in ports)
    summary = action
    if protocol:
        summary = f"{summary} {protocol}"
    if ports:
        summary = f"{summary} {ports}"
    return summary
