"""Pure Cilium network-policy detail builder — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumL7RuleSummary,
    CiliumNetworkPolicyDetail,
    CiliumRuleSummary,
)

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"
_ENDPOINT_KEYS = (
    "fromEndpoints",
    "toEndpoints",
    "fromEntities",
    "toEntities",
    "fromCIDR",
    "toCIDR",
)


def _as_dict(value: object) -> dict[str, object]:
    return value if isinstance(value, dict) else {}


def _list_field(value: object) -> list[object]:
    return value if isinstance(value, list) else []


def build_policy_detail(
    kind: str, namespace: str | None, raw: dict[str, object]
) -> CiliumNetworkPolicyDetail:
    """Build a policy detail from a raw cilium.io custom object."""
    metadata = _as_dict(raw.get("metadata"))
    spec = _as_dict(raw.get("spec"))
    ingress = tuple(
        _summarize_rule("ingress", rule)
        for rule in _list_field(spec.get("ingress"))
        if isinstance(rule, dict)
    )
    egress = tuple(
        _summarize_rule("egress", rule)
        for rule in _list_field(spec.get("egress"))
        if isinstance(rule, dict)
    )
    l7_protocols = _collect_l7_protocols((*ingress, *egress))
    return CiliumNetworkPolicyDetail(
        installed=True,
        status="ok",
        kind=kind,
        name=str(metadata.get("name", "")),
        namespace=namespace,
        endpoint_selector=_render_selector(spec.get("endpointSelector")),
        ingress_rules=ingress,
        egress_rules=egress,
        l7_protocols=l7_protocols,
        spec=spec,
        note=None,
    )


def not_installed_policy_detail() -> CiliumNetworkPolicyDetail:
    """Honest NOT_INSTALLED marker — no fabricated policy detail."""
    return CiliumNetworkPolicyDetail(
        installed=False,
        status="not_installed",
        kind="",
        name="",
        namespace=None,
        endpoint_selector="",
        ingress_rules=(),
        egress_rules=(),
        l7_protocols=(),
        spec={},
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


def _summarize_rule(direction: str, rule: object) -> CiliumRuleSummary:
    if not isinstance(rule, dict):
        return CiliumRuleSummary(direction=direction, endpoints=(), ports=(), l7=())
    return CiliumRuleSummary(
        direction=direction,
        endpoints=_render_endpoints(rule),
        ports=_render_ports(rule),
        l7=_render_l7(rule),
    )


def _render_endpoints(rule: dict[str, object]) -> tuple[str, ...]:
    rendered: list[str] = []
    for key in _ENDPOINT_KEYS:
        for item in _list_field(rule.get(key)):
            rendered.append(_render_entity(item))
    return tuple(rendered)


def _render_entity(item: object) -> str:
    if isinstance(item, dict):
        labels = item.get("matchLabels")
        if isinstance(labels, dict) and labels:
            pairs = ", ".join(f"{k}={v}" for k, v in sorted(labels.items()))
            return f"matchLabels: {pairs}"
        return str(item)
    return str(item)


def _render_ports(rule: dict[str, object]) -> tuple[str, ...]:
    ports: list[str] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        for entry in _list_field(to_port.get("ports")):
            if isinstance(entry, dict):
                port = entry.get("port")
                protocol = entry.get("protocol")
                if protocol:
                    ports.append(f"{port}/{protocol}")
                elif port is not None:
                    ports.append(str(port))
    return tuple(ports)


def _render_l7(rule: dict[str, object]) -> tuple[CiliumL7RuleSummary, ...]:
    summaries: list[CiliumL7RuleSummary] = []
    for to_port in _list_field(rule.get("toPorts")):
        if not isinstance(to_port, dict):
            continue
        rules = to_port.get("rules")
        if not isinstance(rules, dict) or not rules:
            continue
        for protocol, match in rules.items():
            summaries.append(
                CiliumL7RuleSummary(protocol=str(protocol), match=_render_match(match))
            )
    return tuple(summaries)


def _render_match(match: object) -> tuple[str, ...]:
    if isinstance(match, list):
        return tuple(str(item) for item in match)
    if isinstance(match, dict):
        return tuple(f"{k}={v}" for k, v in sorted(match.items()))
    return (str(match),)


def _collect_l7_protocols(rules: tuple[CiliumRuleSummary, ...]) -> tuple[str, ...]:
    protocols: set[str] = set()
    for rule in rules:
        for l7 in rule.l7:
            protocols.add(l7.protocol)
    return tuple(sorted(protocols))
