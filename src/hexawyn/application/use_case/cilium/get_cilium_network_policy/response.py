from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class CiliumL7RuleOutput(TypedDict):
    protocol: str
    match: list[str]


class CiliumRuleOutput(TypedDict):
    direction: str
    endpoints: list[str]
    ports: list[str]
    l7: list[CiliumL7RuleOutput]


@dataclass
class GetCiliumNetworkPolicyResponse:
    installed: bool = False
    status: str = "not_installed"
    kind: str = ""
    name: str = ""
    namespace: str | None = None
    endpoint_selector: str = ""
    ingress_rules: list[CiliumRuleOutput] | None = None
    egress_rules: list[CiliumRuleOutput] | None = None
    l7_protocols: list[str] | None = None
    spec: dict[str, object] | None = None
    note: str | None = None
    error: str | None = None
