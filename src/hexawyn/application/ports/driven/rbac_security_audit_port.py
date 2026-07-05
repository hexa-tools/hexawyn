from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Literal, TypedDict


class ServiceAccountRaw(TypedDict):
    name: str
    namespace: str


class SubjectRaw(TypedDict):
    kind: str
    name: str
    namespace: str | None


class RoleRefRaw(TypedDict):
    kind: Literal["ClusterRole", "Role"]
    name: str


class RoleBindingRaw(TypedDict):
    binding_kind: Literal["ClusterRoleBinding", "RoleBinding"]
    binding_name: str
    namespace: str | None
    subjects: list[SubjectRaw]
    role_ref: RoleRefRaw


class PolicyRuleRaw(TypedDict):
    verbs: list[str]
    resources: list[str]
    api_groups: list[str]


class RoleRaw(TypedDict):
    kind: Literal["ClusterRole", "Role"]
    name: str
    namespace: str | None
    rules: list[PolicyRuleRaw]
    labels: dict[str, str]
    aggregation_selectors: list[dict[str, str]]


class PodOwnerRaw(TypedDict):
    pod_name: str
    namespace: str
    service_account_name: str


class ApiUsageEventRaw(TypedDict):
    service_account: str
    namespace: str
    verb: str
    resource: str
    timestamp: str


class ApiUsageFetchResult(TypedDict):
    available: bool
    events: list[ApiUsageEventRaw]


class RBACSecurityAuditPort(ABC):
    """Port for enumerating ServiceAccounts, their RoleBindings/
    ClusterRoleBindings, the referenced Role/ClusterRole rules (including raw
    aggregationRule label-selector data), owning Pods, and an optional
    audit-log source used to compute actual API usage per service account."""

    @abstractmethod
    def list_service_accounts(self) -> list[ServiceAccountRaw]:
        """List every ServiceAccount across all namespaces."""

    @abstractmethod
    def list_role_bindings(self) -> list[RoleBindingRaw]:
        """List every ClusterRoleBinding and RoleBinding across all namespaces."""

    @abstractmethod
    def list_roles(self) -> list[RoleRaw]:
        """List every Role and ClusterRole, including own labels and raw
        aggregationRule.clusterRoleSelectors match-labels (unresolved)."""

    @abstractmethod
    def list_pods_by_service_account(self) -> list[PodOwnerRaw]:
        """List every Pod's owning service account, across all namespaces."""

    @abstractmethod
    def fetch_api_usage(self, window_days: int) -> ApiUsageFetchResult:
        """Fetch k8s audit log events for service-account API calls, if configured."""
