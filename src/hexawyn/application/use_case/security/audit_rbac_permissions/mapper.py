from __future__ import annotations

from hexawyn.application.ports.driven.rbac_security_audit_port import (
    PodOwnerRaw,
    PolicyRuleRaw,
    RoleBindingRaw,
    RoleRaw,
)
from hexawyn.application.use_case.security.audit_rbac_permissions.response import (
    AuditRbacPermissionsResponse,
    PolicyRuleDict,
    RBACFindingDict,
    SuggestedRoleDict,
    UnusedServiceAccountDict,
)
from hexawyn.domain.models.rbac_audit import (
    ClusterRoleCandidate,
    PolicyRule,
    RBACAuditReport,
    RBACFinding,
    SuggestedRole,
)

_ServiceAccountKey = tuple[str, str]
_RoleKey = tuple[str | None, str]


def to_policy_rule(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(
        verbs=raw["verbs"],
        resources=raw["resources"],
        api_groups=raw["api_groups"],
    )


def to_candidate(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=role["labels"],
        rules=[to_policy_rule(rule) for rule in role["rules"]],
    )


def index_bindings_by_service_account(
    role_bindings: list[RoleBindingRaw],
) -> dict[_ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[_ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            key: _ServiceAccountKey = (namespace, subject["name"])
            index.setdefault(key, []).append(binding)
    return index


def index_pods_by_service_account(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: _ServiceAccountKey = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def resolve_role(
    role_ref: RoleBindingRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":  # type: ignore
        return cluster_roles_by_name.get(role_ref["name"])  # type: ignore
    return roles_by_namespace_name.get(
        (binding["namespace"], role_ref["name"]),  # type: ignore
    )


def to_response(report: RBACAuditReport) -> AuditRbacPermissionsResponse:
    return AuditRbacPermissionsResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=u.name, namespace=u.namespace)
            for u in report.unused_service_accounts
        ],
        excluded_system_service_accounts=report.excluded_system_service_accounts,
        total_service_accounts_checked=report.total_service_accounts_checked,
        summary=report.summary,
        error=None,
    )


def _to_finding_dict(finding: RBACFinding) -> RBACFindingDict:
    return RBACFindingDict(
        service_account=finding.service_account,
        namespace=finding.namespace,
        risk_level=finding.risk_level,
        reasons=finding.reasons,
        current_permissions=[_to_rule_dict(rule) for rule in finding.current_permissions],
        pods_using=finding.pods_using,
        misconfigured=finding.misconfigured,
        recommendation=finding.recommendation,
        suggested_role=_to_suggested_role_dict(finding.suggested_role),
    )


def _to_rule_dict(rule: PolicyRule) -> PolicyRuleDict:
    return PolicyRuleDict(
        verbs=rule.verbs,
        resources=rule.resources,
        api_groups=rule.api_groups,
    )


def _to_suggested_role_dict(
    suggested_role: SuggestedRole,
) -> SuggestedRoleDict:
    return SuggestedRoleDict(
        kind=suggested_role.kind,
        rules=[_to_rule_dict(rule) for rule in suggested_role.rules],
        basis=suggested_role.basis,
    )
