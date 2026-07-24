from __future__ import annotations

from hexawyn.application.ports.driven.rbac_security_audit_port import (
    ApiUsageFetchResult,
    PodOwnerRaw,
    PolicyRuleRaw,
    RBACSecurityAuditPort,
    RoleBindingRaw,
    RoleRaw,
    RoleRefRaw,
    ServiceAccountRaw,
)
from hexawyn.application.use_case.audit_rbac_permissions.command import (
    AuditRBACPermissionsCommand,
)
from hexawyn.application.use_case.audit_rbac_permissions.response import (
    AuditRBACPermissionsResponse,
    PolicyRuleDict,
    RBACFindingDict,
    SuggestedRoleDict,
    UnusedServiceAccountDict,
)
from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_service_port import (
    AuditRBACPermissionsServicePort,
)
from hexawyn.domain.models.constants import RBACAuditConstants
from hexawyn.domain.models.rbac_audit import (
    ClusterRoleCandidate,
    PolicyRule,
    RBACAuditReport,
    RBACFinding,
    SuggestedRole,
    UnusedServiceAccount,
)
from hexawyn.domain.services.rbac_audit.aggregation_resolver import (
    resolve_effective_rules,
)
from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
    build_recommendation,
    suggest_minimal_role,
)
from hexawyn.domain.services.rbac_audit.misconfiguration import is_misconfigured_binding
from hexawyn.domain.services.rbac_audit.rbac_audit_report_builder import build_report
from hexawyn.domain.services.rbac_audit.risk_scoring import (
    build_risk_reasons,
    classify_risk_level,
)

_cfg = RBACAuditConstants()
_ServiceAccountKey = tuple[str, str]
_RoleKey = tuple[str | None, str]


class ServiceAccountRBACAuditService(AuditRBACPermissionsServicePort):
    def __init__(self, rbac_port: RBACSecurityAuditPort) -> None:
        self._rbac_port = rbac_port

    def audit_permissions(
        self, command: AuditRBACPermissionsCommand
    ) -> AuditRBACPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(command.window_days)

        cluster_roles_by_name = {
            role["name"]: role for role in roles if role["kind"] == "ClusterRole"
        }
        roles_by_namespace_name: dict[_RoleKey, RoleRaw] = {
            (role["namespace"], role["name"]): role for role in roles if role["kind"] == "Role"
        }
        cluster_role_candidates = [_to_candidate(role) for role in cluster_roles_by_name.values()]
        bindings_by_sa = _index_bindings_by_service_account(role_bindings)
        pods_by_sa = _index_pods_by_service_account(pod_owners)

        findings: list[RBACFinding] = []
        unused: list[UnusedServiceAccount] = []
        excluded: list[str] = []

        for service_account in service_accounts:
            key = (service_account["namespace"], service_account["name"])
            if service_account["namespace"] == _cfg.system_namespace:
                excluded.append(f"{service_account['namespace']}:{service_account['name']}")
                continue

            bindings = bindings_by_sa.get(key, [])
            if not bindings:
                unused.append(
                    UnusedServiceAccount(
                        name=service_account["name"],
                        namespace=service_account["namespace"],
                    )
                )
                continue

            findings.append(
                _build_finding(
                    service_account=service_account,
                    bindings=bindings,
                    cluster_roles_by_name=cluster_roles_by_name,
                    roles_by_namespace_name=roles_by_namespace_name,
                    cluster_role_candidates=cluster_role_candidates,
                    pods_using=pods_by_sa.get(key, []),
                    api_usage=api_usage,
                )
            )

        report = build_report(
            findings=findings,
            unused_service_accounts=unused,
            excluded_system_service_accounts=excluded,
            total_service_accounts_checked=len(service_accounts),
        )
        return _to_response(report)


def _build_finding(
    service_account: ServiceAccountRaw,
    bindings: list[RoleBindingRaw],
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
    cluster_role_candidates: list[ClusterRoleCandidate],
    pods_using: list[str],
    api_usage: ApiUsageFetchResult,
) -> RBACFinding:
    is_cluster_admin = False
    misconfigured = False
    effective_rules: list[PolicyRule] = []

    for binding in bindings:
        role_raw = _resolve_role(
            binding["role_ref"], binding, cluster_roles_by_name, roles_by_namespace_name
        )
        if role_raw is None:
            continue
        if (
            binding["role_ref"]["kind"] == "ClusterRole"
            and binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
        ):
            is_cluster_admin = True

        own_rules = [_to_policy_rule(rule) for rule in role_raw["rules"]]
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
            "RoleBinding grants cluster-scoped resource access that has no effect within a namespace"
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


def _resolve_role(
    role_ref: RoleRefRaw,
    binding: RoleBindingRaw,
    cluster_roles_by_name: dict[str, RoleRaw],
    roles_by_namespace_name: dict[_RoleKey, RoleRaw],
) -> RoleRaw | None:
    if role_ref["kind"] == "ClusterRole":
        return cluster_roles_by_name.get(role_ref["name"])
    return roles_by_namespace_name.get((binding["namespace"], role_ref["name"]))


def _index_bindings_by_service_account(
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
            index.setdefault((namespace, subject["name"]), []).append(binding)
    return index


def _index_pods_by_service_account(
    pod_owners: list[PodOwnerRaw],
) -> dict[_ServiceAccountKey, list[str]]:
    index: dict[_ServiceAccountKey, list[str]] = {}
    for pod in pod_owners:
        key = (pod["namespace"], pod["service_account_name"])
        index.setdefault(key, []).append(pod["pod_name"])
    return index


def _to_policy_rule(raw: PolicyRuleRaw) -> PolicyRule:
    return PolicyRule(verbs=raw["verbs"], resources=raw["resources"], api_groups=raw["api_groups"])


def _to_candidate(role: RoleRaw) -> ClusterRoleCandidate:
    return ClusterRoleCandidate(
        name=role["name"],
        labels=role["labels"],
        rules=[_to_policy_rule(rule) for rule in role["rules"]],
    )


def _to_response(report: RBACAuditReport) -> AuditRBACPermissionsResponse:
    return AuditRBACPermissionsResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        unused_service_accounts=[
            UnusedServiceAccountDict(name=unused.name, namespace=unused.namespace)
            for unused in report.unused_service_accounts
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
    return PolicyRuleDict(verbs=rule.verbs, resources=rule.resources, api_groups=rule.api_groups)


def _to_suggested_role_dict(suggested_role: SuggestedRole) -> SuggestedRoleDict:
    return SuggestedRoleDict(
        kind=suggested_role.kind,
        rules=[_to_rule_dict(rule) for rule in suggested_role.rules],
        basis=suggested_role.basis,
    )
