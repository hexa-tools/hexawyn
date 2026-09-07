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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAuditRbacPermissionsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut: MutantDict = {}  # type: ignore


class AuditRbacPermissionsUseCase:
    @_mutmut_mutated(mutants_xǁAuditRbacPermissionsUseCaseǁ__init____mutmut)
    def __init__(self, rbac_port: RBACSecurityAuditPort) -> None:
        self._rbac_port = rbac_port
    def xǁAuditRbacPermissionsUseCaseǁ__init____mutmut_orig(self, rbac_port: RBACSecurityAuditPort) -> None:
        self._rbac_port = rbac_port
    def xǁAuditRbacPermissionsUseCaseǁ__init____mutmut_1(self, rbac_port: RBACSecurityAuditPort) -> None:
        self._rbac_port = None

    @_mutmut_mutated(mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut)
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_orig(
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_1(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_2(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_3(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_4(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_5(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = None

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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_6(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(None)

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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_7(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(command.window_days)

        cluster_roles_by_name = None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_8(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(command.window_days)

        cluster_roles_by_name = {r["XXnameXX"]: r for r in roles if r["kind"] == "ClusterRole"}
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_9(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(command.window_days)

        cluster_roles_by_name = {r["NAME"]: r for r in roles if r["kind"] == "ClusterRole"}
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_10(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(command.window_days)

        cluster_roles_by_name = {r["name"]: r for r in roles if r["XXkindXX"] == "ClusterRole"}
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_11(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(command.window_days)

        cluster_roles_by_name = {r["name"]: r for r in roles if r["KIND"] == "ClusterRole"}
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_12(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(command.window_days)

        cluster_roles_by_name = {r["name"]: r for r in roles if r["kind"] != "ClusterRole"}
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_13(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(command.window_days)

        cluster_roles_by_name = {r["name"]: r for r in roles if r["kind"] == "XXClusterRoleXX"}
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_14(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(command.window_days)

        cluster_roles_by_name = {r["name"]: r for r in roles if r["kind"] == "clusterrole"}
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_15(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(command.window_days)

        cluster_roles_by_name = {r["name"]: r for r in roles if r["kind"] == "CLUSTERROLE"}
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_16(
        self,
        command: AuditRbacPermissionsCommand,
    ) -> AuditRbacPermissionsResponse:
        service_accounts = self._rbac_port.list_service_accounts()
        role_bindings = self._rbac_port.list_role_bindings()
        roles = self._rbac_port.list_roles()
        pod_owners = self._rbac_port.list_pods_by_service_account()
        api_usage = self._rbac_port.fetch_api_usage(command.window_days)

        cluster_roles_by_name = {r["name"]: r for r in roles if r["kind"] == "ClusterRole"}
        roles_by_ns_name: dict[_RoleKey, RoleRaw] = None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_17(
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
            (r["XXnamespaceXX"], r["name"]): r for r in roles if r["kind"] == "Role"
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_18(
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
            (r["NAMESPACE"], r["name"]): r for r in roles if r["kind"] == "Role"
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_19(
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
            (r["namespace"], r["XXnameXX"]): r for r in roles if r["kind"] == "Role"
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_20(
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
            (r["namespace"], r["NAME"]): r for r in roles if r["kind"] == "Role"
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_21(
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
            (r["namespace"], r["name"]): r for r in roles if r["XXkindXX"] == "Role"
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_22(
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
            (r["namespace"], r["name"]): r for r in roles if r["KIND"] == "Role"
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_23(
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
            (r["namespace"], r["name"]): r for r in roles if r["kind"] != "Role"
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_24(
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
            (r["namespace"], r["name"]): r for r in roles if r["kind"] == "XXRoleXX"
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_25(
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
            (r["namespace"], r["name"]): r for r in roles if r["kind"] == "role"
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_26(
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
            (r["namespace"], r["name"]): r for r in roles if r["kind"] == "ROLE"
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_27(
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
        cluster_role_candidates = None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_28(
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
        cluster_role_candidates = [to_candidate(None) for role in cluster_roles_by_name.values()]
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_29(
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
        bindings_by_sa = None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_30(
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
        bindings_by_sa = index_bindings_by_service_account(None)
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_31(
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
        pods_by_sa = None

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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_32(
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
        pods_by_sa = index_pods_by_service_account(None)

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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_33(
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

        findings: list[RBACFinding] = None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_34(
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
        unused: list[UnusedServiceAccount] = None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_35(
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
        excluded: list[str] = None

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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_36(
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
            key = None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_37(
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
            key = (sa["XXnamespaceXX"], sa["name"])
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_38(
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
            key = (sa["NAMESPACE"], sa["name"])
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_39(
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
            key = (sa["namespace"], sa["XXnameXX"])
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_40(
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
            key = (sa["namespace"], sa["NAME"])
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_41(
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
            if sa["XXnamespaceXX"] == _cfg.system_namespace:
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_42(
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
            if sa["NAMESPACE"] == _cfg.system_namespace:
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_43(
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
            if sa["namespace"] != _cfg.system_namespace:
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_44(
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
                    None,
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_45(
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
                    f"{sa['XXnamespaceXX']}:{sa['name']}",
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_46(
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
                    f"{sa['NAMESPACE']}:{sa['name']}",
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_47(
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
                    f"{sa['namespace']}:{sa['XXnameXX']}",
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_48(
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
                    f"{sa['namespace']}:{sa['NAME']}",
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_49(
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
                break

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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_50(
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

            bindings = None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_51(
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

            bindings = bindings_by_sa.get(None, [])
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_52(
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

            bindings = bindings_by_sa.get(key, None)
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_53(
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

            bindings = bindings_by_sa.get([])
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_54(
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

            bindings = bindings_by_sa.get(key, )
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_55(
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
            if bindings:
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_56(
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
                    None
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_57(
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
                        name=None,
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_58(
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
                        namespace=None,
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_59(
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_60(
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_61(
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
                        name=sa["XXnameXX"],
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_62(
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
                        name=sa["NAME"],
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_63(
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
                        namespace=sa["XXnamespaceXX"],
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_64(
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
                        namespace=sa["NAMESPACE"],
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_65(
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
                break

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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_66(
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
                None
            )

        report = build_report(
            findings=findings,
            unused_service_accounts=unused,
            excluded_system_service_accounts=excluded,
            total_service_accounts_checked=len(service_accounts),
        )
        return to_response(report)

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_67(
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
                    service_account=None,
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_68(
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
                    bindings=None,
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_69(
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
                    cluster_roles_by_name=None,
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_70(
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
                    roles_by_ns_name=None,
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_71(
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
                    cluster_role_candidates=None,
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_72(
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
                    pods_using=None,
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_73(
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
                    api_usage=None,
                )
            )

        report = build_report(
            findings=findings,
            unused_service_accounts=unused,
            excluded_system_service_accounts=excluded,
            total_service_accounts_checked=len(service_accounts),
        )
        return to_response(report)

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_74(
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_75(
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_76(
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_77(
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_78(
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_79(
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_80(
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
                    )
            )

        report = build_report(
            findings=findings,
            unused_service_accounts=unused,
            excluded_system_service_accounts=excluded,
            total_service_accounts_checked=len(service_accounts),
        )
        return to_response(report)

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_81(
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
                    pods_using=pods_by_sa.get(None, []),
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_82(
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
                    pods_using=pods_by_sa.get(key, None),
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_83(
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
                    pods_using=pods_by_sa.get([]),
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_84(
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
                    pods_using=pods_by_sa.get(key, ),
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

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_85(
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

        report = None
        return to_response(report)

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_86(
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
            findings=None,
            unused_service_accounts=unused,
            excluded_system_service_accounts=excluded,
            total_service_accounts_checked=len(service_accounts),
        )
        return to_response(report)

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_87(
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
            unused_service_accounts=None,
            excluded_system_service_accounts=excluded,
            total_service_accounts_checked=len(service_accounts),
        )
        return to_response(report)

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_88(
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
            excluded_system_service_accounts=None,
            total_service_accounts_checked=len(service_accounts),
        )
        return to_response(report)

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_89(
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
            total_service_accounts_checked=None,
        )
        return to_response(report)

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_90(
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
            unused_service_accounts=unused,
            excluded_system_service_accounts=excluded,
            total_service_accounts_checked=len(service_accounts),
        )
        return to_response(report)

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_91(
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
            excluded_system_service_accounts=excluded,
            total_service_accounts_checked=len(service_accounts),
        )
        return to_response(report)

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_92(
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
            total_service_accounts_checked=len(service_accounts),
        )
        return to_response(report)

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_93(
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
            )
        return to_response(report)

    def xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_94(
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
        return to_response(None)

    @_mutmut_mutated(mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut)
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_orig(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_1(  # noqa: PLR0913
        self,
        service_account: ServiceAccountRaw,
        bindings: list[RoleBindingRaw],
        cluster_roles_by_name: dict[str, RoleRaw],
        roles_by_ns_name: dict[_RoleKey, RoleRaw],
        cluster_role_candidates: list[ClusterRoleCandidate],  # noqa: F821  # type: ignore
        pods_using: list[str],
        api_usage: ApiUsageFetchResult,
    ) -> RBACFinding:
        is_cluster_admin = None
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_2(  # noqa: PLR0913
        self,
        service_account: ServiceAccountRaw,
        bindings: list[RoleBindingRaw],
        cluster_roles_by_name: dict[str, RoleRaw],
        roles_by_ns_name: dict[_RoleKey, RoleRaw],
        cluster_role_candidates: list[ClusterRoleCandidate],  # noqa: F821  # type: ignore
        pods_using: list[str],
        api_usage: ApiUsageFetchResult,
    ) -> RBACFinding:
        is_cluster_admin = True
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_3(  # noqa: PLR0913
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
        misconfigured = None
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_4(  # noqa: PLR0913
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
        misconfigured = True
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_5(  # noqa: PLR0913
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
        effective_rules: list[PolicyRule] = None

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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_6(  # noqa: PLR0913
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
            role_raw = None
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_7(  # noqa: PLR0913
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
                None,  # type: ignore
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_8(  # noqa: PLR0913
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
                None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_9(  # noqa: PLR0913
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
                None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_10(  # noqa: PLR0913
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
                None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_11(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_12(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_13(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_14(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_15(  # noqa: PLR0913
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
                binding["XXrole_refXX"],  # type: ignore
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_16(  # noqa: PLR0913
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
                binding["ROLE_REF"],  # type: ignore
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_17(  # noqa: PLR0913
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
            if role_raw is not None:
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_18(  # noqa: PLR0913
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
                break
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_19(  # noqa: PLR0913
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
                binding["role_ref"]["kind"] == "ClusterRole" or binding["role_ref"]["name"] == _cfg.cluster_admin_role_name
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_20(  # noqa: PLR0913
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
                binding["XXrole_refXX"]["kind"] == "ClusterRole"
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_21(  # noqa: PLR0913
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
                binding["ROLE_REF"]["kind"] == "ClusterRole"
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_22(  # noqa: PLR0913
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
                binding["role_ref"]["XXkindXX"] == "ClusterRole"
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_23(  # noqa: PLR0913
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
                binding["role_ref"]["KIND"] == "ClusterRole"
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_24(  # noqa: PLR0913
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
                binding["role_ref"]["kind"] != "ClusterRole"
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_25(  # noqa: PLR0913
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
                binding["role_ref"]["kind"] == "XXClusterRoleXX"
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_26(  # noqa: PLR0913
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
                binding["role_ref"]["kind"] == "clusterrole"
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_27(  # noqa: PLR0913
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
                binding["role_ref"]["kind"] == "CLUSTERROLE"
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_28(  # noqa: PLR0913
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
                and binding["XXrole_refXX"]["name"] == _cfg.cluster_admin_role_name
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_29(  # noqa: PLR0913
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
                and binding["ROLE_REF"]["name"] == _cfg.cluster_admin_role_name
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_30(  # noqa: PLR0913
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
                and binding["role_ref"]["XXnameXX"] == _cfg.cluster_admin_role_name
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_31(  # noqa: PLR0913
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
                and binding["role_ref"]["NAME"] == _cfg.cluster_admin_role_name
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_32(  # noqa: PLR0913
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
                and binding["role_ref"]["name"] != _cfg.cluster_admin_role_name
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_33(  # noqa: PLR0913
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
                is_cluster_admin = None

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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_34(  # noqa: PLR0913
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
                is_cluster_admin = False

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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_35(  # noqa: PLR0913
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

            own_rules = None
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_36(  # noqa: PLR0913
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

            own_rules = [to_policy_rule(None) for rule in role_raw["rules"]]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_37(  # noqa: PLR0913
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

            own_rules = [to_policy_rule(rule) for rule in role_raw["XXrulesXX"]]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_38(  # noqa: PLR0913
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

            own_rules = [to_policy_rule(rule) for rule in role_raw["RULES"]]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_39(  # noqa: PLR0913
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
            if role_raw["XXkindXX"] == "ClusterRole":
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_40(  # noqa: PLR0913
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
            if role_raw["KIND"] == "ClusterRole":
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_41(  # noqa: PLR0913
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
            if role_raw["kind"] != "ClusterRole":
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_42(  # noqa: PLR0913
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
            if role_raw["kind"] == "XXClusterRoleXX":
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_43(  # noqa: PLR0913
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
            if role_raw["kind"] == "clusterrole":
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_44(  # noqa: PLR0913
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
            if role_raw["kind"] == "CLUSTERROLE":
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_45(  # noqa: PLR0913
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
                resolved = None
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_46(  # noqa: PLR0913
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
                    None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_47(  # noqa: PLR0913
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
                    None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_48(  # noqa: PLR0913
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
                    None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_49(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_50(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_51(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_52(  # noqa: PLR0913
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
                    role_raw["XXaggregation_selectorsXX"],
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_53(  # noqa: PLR0913
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
                    role_raw["AGGREGATION_SELECTORS"],
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_54(  # noqa: PLR0913
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
                resolved = None
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_55(  # noqa: PLR0913
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
            effective_rules.extend(None)
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_56(  # noqa: PLR0913
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
                None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_57(  # noqa: PLR0913
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
                None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_58(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_59(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_60(  # noqa: PLR0913
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
                binding["XXbinding_kindXX"],
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_61(  # noqa: PLR0913
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
                binding["BINDING_KIND"],
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_62(  # noqa: PLR0913
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
                misconfigured = None

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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_63(  # noqa: PLR0913
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
                misconfigured = False

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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_64(  # noqa: PLR0913
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

        risk_level = None
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_65(  # noqa: PLR0913
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

        risk_level = classify_risk_level(None, effective_rules)
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_66(  # noqa: PLR0913
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

        risk_level = classify_risk_level(is_cluster_admin, None)
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_67(  # noqa: PLR0913
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

        risk_level = classify_risk_level(effective_rules)
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_68(  # noqa: PLR0913
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

        risk_level = classify_risk_level(is_cluster_admin, )
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_69(  # noqa: PLR0913
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
        reasons = None
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_70(  # noqa: PLR0913
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
        reasons = build_risk_reasons(None, effective_rules)
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_71(  # noqa: PLR0913
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
        reasons = build_risk_reasons(is_cluster_admin, None)
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_72(  # noqa: PLR0913
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
        reasons = build_risk_reasons(effective_rules)
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_73(  # noqa: PLR0913
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
        reasons = build_risk_reasons(is_cluster_admin, )
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_74(  # noqa: PLR0913
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
                None
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_75(  # noqa: PLR0913
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
                "XXRoleBinding grants cluster-scoped resource access XX"
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_76(  # noqa: PLR0913
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
                "rolebinding grants cluster-scoped resource access "
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_77(  # noqa: PLR0913
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
                "ROLEBINDING GRANTS CLUSTER-SCOPED RESOURCE ACCESS "
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_78(  # noqa: PLR0913
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
                "XXthat has no effect within a namespaceXX"
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_79(  # noqa: PLR0913
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
                "THAT HAS NO EFFECT WITHIN A NAMESPACE"
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_80(  # noqa: PLR0913
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

        observed_pairs = None
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_81(  # noqa: PLR0913
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
            (event["XXverbXX"], event["resource"])
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_82(  # noqa: PLR0913
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
            (event["VERB"], event["resource"])
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_83(  # noqa: PLR0913
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
            (event["verb"], event["XXresourceXX"])
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_84(  # noqa: PLR0913
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
            (event["verb"], event["RESOURCE"])
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_85(  # noqa: PLR0913
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
            for event in api_usage["XXeventsXX"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_86(  # noqa: PLR0913
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
            for event in api_usage["EVENTS"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_87(  # noqa: PLR0913
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
            if event["service_account"] == service_account["name"] or event["namespace"] == service_account["namespace"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_88(  # noqa: PLR0913
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
            if event["XXservice_accountXX"] == service_account["name"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_89(  # noqa: PLR0913
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
            if event["SERVICE_ACCOUNT"] == service_account["name"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_90(  # noqa: PLR0913
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
            if event["service_account"] != service_account["name"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_91(  # noqa: PLR0913
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
            if event["service_account"] == service_account["XXnameXX"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_92(  # noqa: PLR0913
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
            if event["service_account"] == service_account["NAME"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_93(  # noqa: PLR0913
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
            and event["XXnamespaceXX"] == service_account["namespace"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_94(  # noqa: PLR0913
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
            and event["NAMESPACE"] == service_account["namespace"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_95(  # noqa: PLR0913
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
            and event["namespace"] != service_account["namespace"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_96(  # noqa: PLR0913
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
            and event["namespace"] == service_account["XXnamespaceXX"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_97(  # noqa: PLR0913
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
            and event["namespace"] == service_account["NAMESPACE"]
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_98(  # noqa: PLR0913
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
        suggested = None
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_99(  # noqa: PLR0913
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
            None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_100(  # noqa: PLR0913
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
            None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_101(  # noqa: PLR0913
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
            None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_102(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_103(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_104(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_105(  # noqa: PLR0913
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
            api_usage["XXavailableXX"],
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_106(  # noqa: PLR0913
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
            api_usage["AVAILABLE"],
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_107(  # noqa: PLR0913
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
        recommendation = None

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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_108(  # noqa: PLR0913
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
            None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_109(  # noqa: PLR0913
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
            None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_110(  # noqa: PLR0913
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
            None,
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_111(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_112(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_113(  # noqa: PLR0913
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_114(  # noqa: PLR0913
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
            service_account["XXnamespaceXX"],
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_115(  # noqa: PLR0913
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
            service_account["NAMESPACE"],
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

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_116(  # noqa: PLR0913
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
            service_account=None,
            namespace=service_account["namespace"],
            risk_level=risk_level,
            reasons=reasons,
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_117(  # noqa: PLR0913
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
            namespace=None,
            risk_level=risk_level,
            reasons=reasons,
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_118(  # noqa: PLR0913
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
            risk_level=None,
            reasons=reasons,
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_119(  # noqa: PLR0913
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
            reasons=None,
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_120(  # noqa: PLR0913
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
            current_permissions=None,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_121(  # noqa: PLR0913
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
            pods_using=None,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_122(  # noqa: PLR0913
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
            misconfigured=None,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_123(  # noqa: PLR0913
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
            recommendation=None,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_124(  # noqa: PLR0913
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
            suggested_role=None,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_125(  # noqa: PLR0913
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
            namespace=service_account["namespace"],
            risk_level=risk_level,
            reasons=reasons,
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_126(  # noqa: PLR0913
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
            risk_level=risk_level,
            reasons=reasons,
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_127(  # noqa: PLR0913
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
            reasons=reasons,
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_128(  # noqa: PLR0913
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
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_129(  # noqa: PLR0913
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
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_130(  # noqa: PLR0913
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
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_131(  # noqa: PLR0913
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
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_132(  # noqa: PLR0913
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
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_133(  # noqa: PLR0913
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
            )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_134(  # noqa: PLR0913
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
            service_account=service_account["XXnameXX"],
            namespace=service_account["namespace"],
            risk_level=risk_level,
            reasons=reasons,
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_135(  # noqa: PLR0913
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
            service_account=service_account["NAME"],
            namespace=service_account["namespace"],
            risk_level=risk_level,
            reasons=reasons,
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_136(  # noqa: PLR0913
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
            namespace=service_account["XXnamespaceXX"],
            risk_level=risk_level,
            reasons=reasons,
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

    def xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_137(  # noqa: PLR0913
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
            namespace=service_account["NAMESPACE"],
            risk_level=risk_level,
            reasons=reasons,
            current_permissions=effective_rules,
            pods_using=pods_using,
            misconfigured=misconfigured,
            recommendation=recommendation,
            suggested_role=suggested,
        )

mutants_xǁAuditRbacPermissionsUseCaseǁ__init____mutmut['_mutmut_orig'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ__init____mutmut['xǁAuditRbacPermissionsUseCaseǁ__init____mutmut_1'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['_mutmut_orig'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_1'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_2'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_3'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_4'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_5'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_6'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_7'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_8'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_9'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_10'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_11'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_12'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_13'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_14'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_15'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_16'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_17'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_18'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_19'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_20'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_21'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_22'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_23'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_24'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_25'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_26'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_27'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_28'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_29'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_30'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_31'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_32'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_33'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_34'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_35'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_36'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_37'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_38'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_39'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_40'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_41'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_42'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_43'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_44'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_45'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_46'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_47'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_48'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_49'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_49 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_50'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_50 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_51'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_51 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_52'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_52 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_53'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_53 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_54'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_54 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_55'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_55 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_56'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_56 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_57'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_57 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_58'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_58 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_59'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_59 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_60'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_60 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_61'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_61 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_62'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_62 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_63'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_63 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_64'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_64 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_65'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_65 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_66'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_66 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_67'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_67 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_68'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_68 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_69'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_69 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_70'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_70 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_71'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_71 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_72'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_72 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_73'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_73 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_74'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_74 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_75'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_75 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_76'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_76 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_77'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_77 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_78'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_78 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_79'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_79 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_80'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_80 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_81'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_81 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_82'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_82 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_83'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_83 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_84'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_84 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_85'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_85 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_86'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_86 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_87'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_87 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_88'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_88 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_89'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_89 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_90'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_90 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_91'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_91 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_92'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_92 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_93'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_93 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut['xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_94'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁaudit_permissions__mutmut_94 # type: ignore # mutmut generated

mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['_mutmut_orig'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_1'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_2'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_3'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_4'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_5'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_6'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_7'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_8'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_9'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_10'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_11'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_12'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_13'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_14'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_15'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_16'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_17'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_18'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_19'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_20'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_21'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_22'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_23'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_24'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_25'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_26'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_27'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_28'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_29'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_30'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_31'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_32'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_33'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_34'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_35'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_36'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_37'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_38'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_39'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_40'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_41'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_42'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_43'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_44'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_45'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_46'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_47'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_48'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_49'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_49 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_50'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_50 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_51'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_51 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_52'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_52 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_53'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_53 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_54'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_54 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_55'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_55 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_56'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_56 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_57'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_57 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_58'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_58 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_59'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_59 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_60'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_60 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_61'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_61 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_62'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_62 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_63'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_63 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_64'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_64 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_65'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_65 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_66'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_66 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_67'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_67 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_68'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_68 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_69'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_69 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_70'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_70 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_71'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_71 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_72'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_72 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_73'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_73 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_74'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_74 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_75'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_75 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_76'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_76 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_77'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_77 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_78'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_78 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_79'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_79 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_80'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_80 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_81'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_81 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_82'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_82 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_83'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_83 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_84'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_84 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_85'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_85 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_86'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_86 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_87'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_87 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_88'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_88 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_89'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_89 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_90'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_90 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_91'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_91 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_92'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_92 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_93'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_93 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_94'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_94 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_95'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_95 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_96'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_96 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_97'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_97 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_98'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_98 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_99'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_99 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_100'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_100 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_101'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_101 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_102'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_102 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_103'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_103 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_104'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_104 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_105'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_105 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_106'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_106 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_107'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_107 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_108'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_108 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_109'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_109 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_110'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_110 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_111'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_111 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_112'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_112 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_113'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_113 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_114'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_114 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_115'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_115 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_116'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_116 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_117'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_117 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_118'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_118 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_119'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_119 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_120'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_120 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_121'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_121 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_122'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_122 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_123'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_123 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_124'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_124 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_125'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_125 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_126'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_126 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_127'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_127 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_128'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_128 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_129'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_129 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_130'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_130 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_131'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_131 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_132'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_132 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_133'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_133 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_134'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_134 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_135'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_135 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_136'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_136 # type: ignore # mutmut generated
mutants_xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut['xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_137'] = AuditRbacPermissionsUseCase.xǁAuditRbacPermissionsUseCaseǁ_build_finding__mutmut_137 # type: ignore # mutmut generated
