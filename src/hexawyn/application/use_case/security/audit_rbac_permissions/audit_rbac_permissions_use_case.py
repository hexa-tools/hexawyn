# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.ports.driven.rbac_security_audit_port import (
    ApiUsageFetchResult,
    RBACSecurityAuditPort,
    RoleBindingRaw,
    RoleRaw,
    ServiceAccountRaw,
)
from hexawyn.application.use_case.security.audit_rbac_permissions.command import (
    AuditRbacPermissionsCommand,
)
from hexawyn.application.use_case.security.audit_rbac_permissions.mapper import (
    index_bindings_by_service_account,
    index_pods_by_service_account,
    resolve_role,
    to_candidate,
    to_policy_rule,
    to_response,
)
from hexawyn.application.use_case.security.audit_rbac_permissions.response import (
    AuditRbacPermissionsResponse,
)
from hexawyn.domain.models.constants import RBACAuditConstants
from hexawyn.domain.models.rbac_audit import (
    PolicyRule,
    RBACFinding,
    UnusedServiceAccount,
)
from hexawyn.domain.services.rbac_audit.aggregation_resolver import (
    resolve_effective_rules,
)
from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
    build_recommendation,
    suggest_minimal_role,
)
from hexawyn.domain.services.rbac_audit.misconfiguration import (
    is_misconfigured_binding,
)
from hexawyn.domain.services.rbac_audit.rbac_audit_report_builder import (
    build_report,
)
from hexawyn.domain.services.rbac_audit.risk_scoring import (
    build_risk_reasons,
    classify_risk_level,
)

_cfg = RBACAuditConstants()
_RoleKey = tuple[str | None, str]


class AuditRbacPermissionsUseCase:
    def __init__(self, rbac_port: RBACSecurityAuditPort) -> None:
        self._rbac_port = rbac_port

    def audit_permissions(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(command.window_days)

        cluster_roles_by_name = {r["name"]: r for r in roles if r["kind"] == "ClusterRole"}
        roles_by_ns_name: dict[_RoleKey, RoleRaw] = {
            (r["namespace"], r["name"]): r for r in roles if r["kind"] == "Role"
        }
        cluster_role_candidates = [to_candidate(role) for role in cluster_roles_by_name.values()]
        bindings_by_sa = index_bindings_by_service_account(role_bindings)
        pods_by_sa = index_pods_by_service_account(pod_owners)

        findings: list[RBACFinding] = []
        unused: list[UnusedServiceAccount] = []
        excluded: list[str] = []

        for sa in service_accounts:
            key = (sa["namespace"], sa["name"])
            if sa["namespace"] == _cfg.system_namespace:
                excluded.append(
                    f"{sa['namespace']}:{sa['name']}",
                )
                continue

            bindings = bindings_by_sa.get(key, [])
            if not bindings:
                unused.append(
                    UnusedServiceAccount(
                        name=sa["name"],
                        namespace=sa["namespace"],
                    )
                )
                continue

            findings.append(
                self._build_finding(
                    service_account=sa,
                    bindings=bindings,
                    cluster_roles_by_name=cluster_roles_by_name,
                    roles_by_ns_name=roles_by_ns_name,
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
        return to_response(report)

    def _build_finding(  # noqa: PLR0913
        self,
        service_account: ServiceAccountRaw,
        bindings: list[RoleBindingRaw],
        cluster_roles_by_name: dict[str, RoleRaw],
        roles_by_ns_name: dict[_RoleKey, RoleRaw],
        cluster_role_candidates: list[ClusterRoleCandidate],  # noqa: F821  # type: ignore
        pods_using: list[str],
        api_usage: ApiUsageFetchResult,
    ) -> RBACFinding:
        is_cluster_admin = False
        misconfigured = False
        effective_rules: list[PolicyRule] = []

        for binding in bindings:
            role_raw = resolve_role(
                binding["role_ref"],  # type: ignore
                binding,
                cluster_roles_by_name,
                roles_by_ns_name,
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
                resolved = resolve_effective_rules(
                    own_rules,
                    role_raw["aggregation_selectors"],
                    cluster_role_candidates,
                )
            else:
                resolved = own_rules
            effective_rules.extend(resolved)
            if is_misconfigured_binding(
                binding["binding_kind"],
                resolved,
            ):
                misconfigured = True

        risk_level = classify_risk_level(is_cluster_admin, effective_rules)
        reasons = build_risk_reasons(is_cluster_admin, effective_rules)
        if misconfigured:
            reasons.append(
                "RoleBinding grants cluster-scoped resource access "
                "that has no effect within a namespace"
            )

        observed_pairs = [
            (event["verb"], event["resource"])
            for event in api_usage["events"]
            if event["service_account"] == service_account["name"]
            and event["namespace"] == service_account["namespace"]
        ]
        suggested = suggest_minimal_role(
            effective_rules,
            api_usage["available"],
            observed_pairs,
        )
        recommendation = build_recommendation(
            risk_level,
            service_account["namespace"],
            suggested,
        )

        return RBACFinding(
            service_account=service_account["name"],
            namespace=service_account["namespace"],
            risk_level=risk_level,
            reasons=reasons,
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )
