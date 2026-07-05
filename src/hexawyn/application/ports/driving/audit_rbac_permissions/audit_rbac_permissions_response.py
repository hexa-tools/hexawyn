from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, TypedDict


class PolicyRuleDict(TypedDict):
    verbs: list[str]
    resources: list[str]
    api_groups: list[str]


class SuggestedRoleDict(TypedDict):
    kind: Literal["Role", "ClusterRole"]
    rules: list[PolicyRuleDict]
    basis: Literal["audit_log", "estimated"]


class RBACFindingDict(TypedDict):
    service_account: str
    namespace: str
    risk_level: Literal["critical", "high", "medium", "low"]
    reasons: list[str]
    current_permissions: list[PolicyRuleDict]
    pods_using: list[str]
    misconfigured: bool
    recommendation: str
    suggested_role: SuggestedRoleDict


class UnusedServiceAccountDict(TypedDict):
    name: str
    namespace: str


@dataclass
class AuditRBACPermissionsResponse:
    findings: list[RBACFindingDict] = field(default_factory=list)
    unused_service_accounts: list[UnusedServiceAccountDict] = field(default_factory=list)
    excluded_system_service_accounts: list[str] = field(default_factory=list)
    total_service_accounts_checked: int = 0
    summary: str = ""
    error: str | None = None
