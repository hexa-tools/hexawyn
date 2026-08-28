from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class CiliumNetworkPolicyOutput(TypedDict):
    kind: str
    name: str
    namespace: str | None
    endpoint_selector: str
    ingress_rule_count: int
    egress_rule_count: int
    l7_rule_count: int
    l7_protocols: list[str]


@dataclass
class ListCiliumNetworkPoliciesResponse:
    installed: bool = False
    status: str = "not_installed"
    total_policies: int = 0
    namespaced_count: int = 0
    clusterwide_count: int = 0
    policies: list[CiliumNetworkPolicyOutput] | None = None
    note: str | None = None
    error: str | None = None
