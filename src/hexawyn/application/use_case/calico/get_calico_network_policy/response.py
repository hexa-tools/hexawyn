from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class GetCalicoNetworkPolicyResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    found: bool = False
    name: str | None = None
    namespace: str | None = None
    scope: str | None = None
    kind: str | None = None
    selector: str | None = None
    action: str | None = None
    ingress_rules: list[object] = field(default_factory=list)
    egress_rules: list[object] = field(default_factory=list)
    ingress_rule_count: int = 0
    egress_rule_count: int = 0
    order: float = 0.0
    apply_on_forward: bool = False
    error: str | None = None
