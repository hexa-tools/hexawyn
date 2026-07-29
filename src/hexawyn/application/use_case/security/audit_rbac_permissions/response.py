from dataclasses import dataclass, field
from typing import TypedDict


class PolicyRuleDict(TypedDict):
    verbs: list[str]
    resources: list[str]
    api_groups: list[str]


class SuggestedRoleDict(TypedDict):
    kind: str
    rules: list[PolicyRuleDict]
    basis: str


class RBACFindingDict(TypedDict):
    service_account: str
    namespace: str
    risk_level: str
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
class AuditRbacPermissionsResponse:
    findings: list[RBACFindingDict] = field(default_factory=list)
    unused_service_accounts: list[UnusedServiceAccountDict] = field(
        default_factory=list,
    )
    excluded_system_service_accounts: list[str] = field(default_factory=list)
    total_service_accounts_checked: int = 0
    summary: str = ""
    error: str | None = None
