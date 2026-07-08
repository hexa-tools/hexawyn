from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

RiskLevel = Literal["critical", "high", "medium", "low"]
PermissionBasis = Literal["audit_log", "estimated"]


@dataclass(frozen=True)
class PolicyRule:
    verbs: list[str]
    resources: list[str]
    api_groups: list[str]


@dataclass(frozen=True)
class ClusterRoleCandidate:
    name: str
    labels: dict[str, str]
    rules: list[PolicyRule]


@dataclass(frozen=True)
class RoleBindingRef:
    binding_kind: Literal["ClusterRoleBinding", "RoleBinding"]
    binding_name: str
    role_kind: Literal["ClusterRole", "Role"]
    role_name: str
    namespace: str | None


@dataclass(frozen=True)
class SuggestedRole:
    kind: Literal["Role", "ClusterRole"]
    rules: list[PolicyRule]
    basis: PermissionBasis


@dataclass(frozen=True)
class RBACFinding:
    service_account: str
    namespace: str
    risk_level: RiskLevel
    reasons: list[str]
    current_permissions: list[PolicyRule]
    pods_using: list[str]
    misconfigured: bool
    recommendation: str
    suggested_role: SuggestedRole


@dataclass(frozen=True)
class UnusedServiceAccount:
    name: str
    namespace: str


@dataclass(frozen=True)
class RBACAuditReport:
    findings: list[RBACFinding]
    unused_service_accounts: list[UnusedServiceAccount]
    excluded_system_service_accounts: list[str]
    total_service_accounts_checked: int
    summary: str
