from __future__ import annotations

from hexawyn.application.ports.driven.rbac_security_audit_port import (
    ApiUsageFetchResult,
    PolicyRuleRaw,
    RoleBindingRaw,
    RoleRaw,
    RoleRefRaw,
    ServiceAccountRaw,
)
from hexawyn.domain.models.constants import RBACAuditConstants
from hexawyn.domain.models.rbac_audit import (
    ClusterRoleCandidate,
    PolicyRule,
    RBACFinding,
    RoleKey,
    ServiceAccountKey,
)
from hexawyn.domain.services.rbac_audit.aggregation_resolver import (
    resolve_effective_rules,
)
from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
    build_recommendation,
    suggest_minimal_role,
)
from hexawyn.domain.services.rbac_audit.misconfiguration import is_misconfigured_binding
from hexawyn.domain.services.rbac_audit.risk_scoring import (
    build_risk_reasons,
    classify_risk_level,
)

_cfg = RBACAuditConstants()


def build_finding(  # noqa: PLR0913
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [to_policy_rule(rule) for rule in role_raw["rules"]]
        if role_raw["kind"] == "ClusterRole":
            binding_rules = resolve_effective_rules(
                own_rules, role_raw["aggregation_selectors"], cluster_role_candidates
            )
        else:
            binding_rules = own_rules
        effective_rules.extend(binding_rules)
        if is_misconfigured_binding(binding["binding_kind"], binding_rules):
            misconfigured = True

    risk_level = classify_risk_level(is_cluster_admin, effective_rules)
    reasons = build_risk_reasons(is_cluster_admin, effective_rules)
    if misconfigured:
        reasons.append(
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"  # noqa: E501
        )

    observed_pairs = [
        (event["verb"], event["resource"])
        for event in api_usage["events"]
        if event["service_account"] == service_account["name"]
        and event["namespace"] == service_account["namespace"]
    ]
    suggested_role = suggest_minimal_role(effective_rules, api_usage["available"], observed_pairs)
    recommendation = build_recommendation(risk_level, service_account["namespace"], suggested_role)

    return RBACFinding(
        service_account=service_account["name"],
        namespace=service_account["namespace"],
        risk_level=risk_level,
        reasons=reasons,
        current_permissions=effective_rules,
        pods_using=pods_using,
        misconfigured=misconfigured,
        recommendation=recommendation,
        suggested_role=suggested_role,
    )


def resolve_role(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def index_bindings_by_service_account(
    role_bindings: list[RoleBindingRaw],
) -> dict[ServiceAccountKey, list[RoleBindingRaw]]:
    index: dict[ServiceAccountKey, list[RoleBindingRaw]] = {}
    for binding in role_bindings:
        for subject in binding["subjects"]:
            if subject["kind"] != "ServiceAccount":
                continue
            namespace = subject["namespace"] or binding["namespace"]
            if namespace is None:
                continue
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def index_pods_by_service_account(
    pod_owners: list[dict[str, str]],
) -> dict[ServiceAccountKey, list[str]]:
    index: dict[ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key: tuple[str, str] = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def to_policy_rule(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["verbs"], resources=raw["resources"], api_groups=raw["api_groups"])


def to_candidate(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=role["labels"],
        rules=[to_policy_rule(rule) for rule in role["rules"]],
    )
