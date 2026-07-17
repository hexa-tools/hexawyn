"""Unit tests for ServiceAccountRBACAuditService (mocks RBACSecurityAuditPort).

Covers the ticket's five Test Scenarios (TC1-TC5) and its five Edge Cases by
name in the test names.
"""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_command import (
    AuditRBACPermissionsCommand,
)
from hexawyn.application.service.audit_rbac_permissions_service import (
    ServiceAccountRBACAuditService,
)


def _sa(name: str, namespace: str = "production") -> dict:
    return {"name": name, "namespace": namespace}


def _cluster_role_binding(name: str, sa_name: str, sa_namespace: str, role_name: str) -> dict:
    return {
        "binding_kind": "ClusterRoleBinding",
        "binding_name": f"{name}-binding",
        "namespace": None,
        "subjects": [{"kind": "ServiceAccount", "name": sa_name, "namespace": sa_namespace}],
        "role_ref": {"kind": "ClusterRole", "name": role_name},
    }


def _role_binding(
    name: str, sa_name: str, sa_namespace: str, role_kind: str, role_name: str
) -> dict:
    return {
        "binding_kind": "RoleBinding",
        "binding_name": f"{name}-binding",
        "namespace": sa_namespace,
        "subjects": [{"kind": "ServiceAccount", "name": sa_name, "namespace": sa_namespace}],
        "role_ref": {"kind": role_kind, "name": role_name},
    }


def _cluster_role(
    name: str,
    rules: list[dict] | None = None,
    labels: dict[str, str] | None = None,
    aggregation_selectors: list[dict[str, str]] | None = None,
) -> dict:
    return {
        "kind": "ClusterRole",
        "name": name,
        "namespace": None,
        "rules": rules or [],
        "labels": labels or {},
        "aggregation_selectors": aggregation_selectors or [],
    }


def _role(name: str, namespace: str, rules: list[dict] | None = None) -> dict:
    return {
        "kind": "Role",
        "name": name,
        "namespace": namespace,
        "rules": rules or [],
        "labels": {},
        "aggregation_selectors": [],
    }


def _rule(verbs: list[str], resources: list[str]) -> dict:
    return {"verbs": verbs, "resources": resources, "api_groups": [""]}


def _pod(pod_name: str, namespace: str, service_account_name: str) -> dict:
    return {
        "pod_name": pod_name,
        "namespace": namespace,
        "service_account_name": service_account_name,
    }


def _make_service(
    service_accounts: list[dict] | None = None,
    role_bindings: list[dict] | None = None,
    roles: list[dict] | None = None,
    pods: list[dict] | None = None,
    api_usage_available: bool = False,
    api_usage_events: list[dict] | None = None,
) -> tuple[ServiceAccountRBACAuditService, MagicMock]:
    port = MagicMock()
    port.list_service_accounts.return_value = service_accounts or []
    port.list_role_bindings.return_value = role_bindings or []
    port.list_roles.return_value = roles or []
    port.list_pods_by_service_account.return_value = pods or []
    port.fetch_api_usage.return_value = {
        "available": api_usage_available,
        "events": api_usage_events or [],
    }
    service = ServiceAccountRBACAuditService(rbac_port=port)
    return service, port


class TestClusterAdminBinding:
    def test_tc1_sa_bound_to_cluster_admin_is_critical_with_namespace_scoped_suggestion(
        self,
    ) -> None:
        service, _ = _make_service(
            service_accounts=[_sa("payment-sa", "production")],
            role_bindings=[
                _cluster_role_binding(
                    "payment-sa-admin", "payment-sa", "production", "cluster-admin"
                )
            ],
            roles=[_cluster_role("cluster-admin", rules=[_rule(["*"], ["*"])])],
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        assert len(response.findings) == 1
        finding = response.findings[0]
        assert finding["service_account"] == "payment-sa"
        assert finding["risk_level"] == "critical"
        assert finding["suggested_role"]["kind"] == "Role"


class TestWildcardVerbOnSecrets:
    def test_tc2_wildcard_verbs_on_secrets_is_high_and_flags_secret_access(
        self,
    ) -> None:
        service, _ = _make_service(
            service_accounts=[_sa("monitoring-sa", "monitoring")],
            role_bindings=[
                _role_binding(
                    "monitoring-secrets",
                    "monitoring-sa",
                    "monitoring",
                    "ClusterRole",
                    "secrets-reader",
                )
            ],
            roles=[_cluster_role("secrets-reader", rules=[_rule(["*"], ["secrets"])])],
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        finding = response.findings[0]
        assert finding["risk_level"] == "high"
        assert any("secrets" in reason for reason in finding["reasons"])


class TestMinimalHealthyPermissions:
    def test_tc3_sa_with_only_get_on_pods_is_low_and_healthy(self) -> None:
        service, _ = _make_service(
            service_accounts=[_sa("reader-sa", "production")],
            role_bindings=[
                _role_binding("reader", "reader-sa", "production", "Role", "pod-reader")
            ],
            roles=[_role("pod-reader", "production", rules=[_rule(["get"], ["pods"])])],
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        finding = response.findings[0]
        assert finding["risk_level"] == "low"
        assert "no action needed" in finding["recommendation"].lower()


class TestFiveOverPrivilegedServiceAccounts:
    def test_tc4_five_over_privileged_service_accounts_all_listed_with_risk_scores(
        self,
    ) -> None:
        service_accounts = [_sa(f"sa-{i}", "production") for i in range(5)]
        role_bindings = [
            _cluster_role_binding(f"binding-{i}", f"sa-{i}", "production", "cluster-admin")
            for i in range(5)
        ]
        service, _ = _make_service(
            service_accounts=service_accounts,
            role_bindings=role_bindings,
            roles=[_cluster_role("cluster-admin", rules=[_rule(["*"], ["*"])])],
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        assert len(response.findings) == 5
        assert all(finding["risk_level"] == "critical" for finding in response.findings)


class TestUnusedPermissionsFromAuditLog:
    def test_tc5_audit_log_shows_no_usage_recommends_removing_permissions(self) -> None:
        service, _ = _make_service(
            service_accounts=[_sa("idle-perms-sa", "production")],
            role_bindings=[
                _role_binding(
                    "idle-perms",
                    "idle-perms-sa",
                    "production",
                    "Role",
                    "configmap-editor",
                )
            ],
            roles=[
                _role(
                    "configmap-editor",
                    "production",
                    rules=[_rule(["get"], ["configmaps"])],
                )
            ],
            api_usage_available=True,
            api_usage_events=[],
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        finding = response.findings[0]
        assert finding["suggested_role"]["basis"] == "audit_log"
        assert finding["suggested_role"]["rules"] == []
        assert "remove" in finding["recommendation"].lower()


class TestServiceAccountUsedByMultiplePods:
    def test_edge_case_multiple_pods_are_all_listed_in_impact(self) -> None:
        service, _ = _make_service(
            service_accounts=[_sa("payment-sa", "production")],
            role_bindings=[
                _cluster_role_binding("payment-admin", "payment-sa", "production", "cluster-admin")
            ],
            roles=[_cluster_role("cluster-admin", rules=[_rule(["*"], ["*"])])],
            pods=[
                _pod("payment-pod-abc", "production", "payment-sa"),
                _pod("payment-pod-def", "production", "payment-sa"),
            ],
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        finding = response.findings[0]
        assert set(finding["pods_using"]) == {"payment-pod-abc", "payment-pod-def"}


class TestAggregatedClusterRole:
    def test_edge_case_aggregated_cluster_role_computes_effective_union(self) -> None:
        selector = {"rbac.example.com/aggregate-to-monitoring": "true"}
        service, _ = _make_service(
            service_accounts=[_sa("aggregate-sa", "monitoring")],
            role_bindings=[
                _cluster_role_binding(
                    "aggregate-binding",
                    "aggregate-sa",
                    "monitoring",
                    "monitoring-aggregate",
                )
            ],
            roles=[
                _cluster_role("monitoring-aggregate", rules=[], aggregation_selectors=[selector]),
                _cluster_role("view-pods", rules=[_rule(["get"], ["pods"])], labels=selector),
                _cluster_role("view-secrets", rules=[_rule(["get"], ["secrets"])], labels=selector),
                _cluster_role(
                    "view-configmaps",
                    rules=[_rule(["get"], ["configmaps"])],
                    labels=selector,
                ),
            ],
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        finding = response.findings[0]
        resources = {
            resource for rule in finding["current_permissions"] for resource in rule["resources"]
        }
        assert resources == {"pods", "secrets", "configmaps"}


class TestServiceAccountWithNoBindings:
    def test_edge_case_no_bindings_is_unused_not_a_risk(self) -> None:
        service, _ = _make_service(service_accounts=[_sa("idle-sa", "staging")])

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        assert response.findings == []
        assert response.unused_service_accounts == [{"name": "idle-sa", "namespace": "staging"}]


class TestNamespaceScopedBindingForClusterScopedResource:
    def test_edge_case_role_binding_to_cluster_scoped_resource_is_misconfigured(
        self,
    ) -> None:
        service, _ = _make_service(
            service_accounts=[_sa("node-viewer-sa", "production")],
            role_bindings=[
                _role_binding(
                    "node-viewer",
                    "node-viewer-sa",
                    "production",
                    "ClusterRole",
                    "node-reader",
                )
            ],
            roles=[_cluster_role("node-reader", rules=[_rule(["get"], ["nodes"])])],
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        finding = response.findings[0]
        assert finding["misconfigured"] is True


class TestSystemServiceAccountsExcluded:
    def test_edge_case_kube_system_service_accounts_are_excluded_not_scored(
        self,
    ) -> None:
        service, _ = _make_service(
            service_accounts=[_sa("default", "kube-system")],
            role_bindings=[
                _cluster_role_binding("sys-binding", "default", "kube-system", "cluster-admin")
            ],
            roles=[_cluster_role("cluster-admin", rules=[_rule(["*"], ["*"])])],
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        assert response.findings == []
        assert response.unused_service_accounts == []
        assert response.excluded_system_service_accounts == ["kube-system:default"]


class TestDanglingRoleReference:
    def test_binding_referencing_a_deleted_role_is_skipped_not_an_error(self) -> None:
        service, _ = _make_service(
            service_accounts=[_sa("orphan-sa", "production")],
            role_bindings=[
                _role_binding("orphan", "orphan-sa", "production", "ClusterRole", "deleted-role")
            ],
            roles=[],
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        finding = response.findings[0]
        assert finding["current_permissions"] == []
        assert finding["risk_level"] == "low"


class TestNonServiceAccountSubjectsAreIgnored:
    def test_user_subject_on_a_binding_is_not_indexed_as_a_service_account(self) -> None:
        service, port = _make_service(
            service_accounts=[_sa("payment-sa", "production")],
            role_bindings=[
                {
                    "binding_kind": "ClusterRoleBinding",
                    "binding_name": "human-admin",
                    "namespace": None,
                    "subjects": [{"kind": "User", "name": "jane.ops", "namespace": None}],
                    "role_ref": {"kind": "ClusterRole", "name": "cluster-admin"},
                }
            ],
            roles=[_cluster_role("cluster-admin", rules=[_rule(["*"], ["*"])])],
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        assert response.findings == []
        assert response.unused_service_accounts == [
            {"name": "payment-sa", "namespace": "production"}
        ]


class TestSubjectWithUnresolvableNamespaceIsIgnored:
    def test_cluster_role_binding_subject_missing_namespace_is_skipped(self) -> None:
        service, _ = _make_service(
            service_accounts=[_sa("payment-sa", "production")],
            role_bindings=[
                {
                    "binding_kind": "ClusterRoleBinding",
                    "binding_name": "malformed-binding",
                    "namespace": None,
                    "subjects": [
                        {"kind": "ServiceAccount", "name": "payment-sa", "namespace": None}
                    ],
                    "role_ref": {"kind": "ClusterRole", "name": "cluster-admin"},
                }
            ],
            roles=[_cluster_role("cluster-admin", rules=[_rule(["*"], ["*"])])],
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        assert response.findings == []
        assert response.unused_service_accounts == [
            {"name": "payment-sa", "namespace": "production"}
        ]


class TestAuditPermissionsReturnsTotalChecked:
    def test_total_service_accounts_checked_reflects_all_service_accounts(self) -> None:
        service, _ = _make_service(
            service_accounts=[_sa("a", "production"), _sa("b", "production")]
        )

        response = service.audit_permissions(AuditRBACPermissionsCommand())

        assert response.total_service_accounts_checked == 2
