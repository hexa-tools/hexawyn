from __future__ import annotations

from unittest.mock import MagicMock

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
from hexawyn.domain.models.rbac_audit import (
    ClusterRoleCandidate,
    PolicyRule,
    RBACAuditReport,
    RBACFinding,
    SuggestedRole,
    UnusedServiceAccount,
)


class TestMapperFunctions:
    def test_to_policy_rule_converts_raw(self) -> None:
        raw = {"verbs": ["get", "list"], "resources": ["pods"], "api_groups": [""]}

        result = to_policy_rule(raw)

        assert isinstance(result, PolicyRule)
        assert result.verbs == ["get", "list"]
        assert result.resources == ["pods"]
        assert result.api_groups == [""]

    def test_to_candidate_converts_role_with_rules(self) -> None:
        role = {
            "kind": "ClusterRole",
            "name": "pod-reader",
            "namespace": None,
            "rules": [
                {"verbs": ["get"], "resources": ["pods"], "api_groups": [""]},
            ],
            "labels": {"app": "demo"},
            "aggregation_selectors": [],
        }

        result = to_candidate(role)

        assert isinstance(result, ClusterRoleCandidate)
        assert result.name == "pod-reader"
        assert result.labels == {"app": "demo"}
        assert len(result.rules) == 1  # noqa: PLR2004
        assert result.rules[0].verbs == ["get"]

    def test_index_bindings_by_service_account_groups_bindings(self) -> None:
        bindings = [
            {
                "binding_kind": "RoleBinding",
                "binding_name": "rb-1",
                "namespace": "default",
                "subjects": [
                    {"kind": "ServiceAccount", "name": "my-sa", "namespace": "default"},
                ],
                "role_ref": {"kind": "Role", "name": "reader"},
            },
            {
                "binding_kind": "RoleBinding",
                "binding_name": "rb-2",
                "namespace": "default",
                "subjects": [
                    {"kind": "ServiceAccount", "name": "my-sa", "namespace": "default"},
                ],
                "role_ref": {"kind": "Role", "name": "writer"},
            },
        ]

        index = index_bindings_by_service_account(bindings)

        assert ("default", "my-sa") in index
        assert len(index[("default", "my-sa")]) == 2  # noqa: PLR2004

    def test_index_bindings_skips_non_service_account_subjects(self) -> None:
        bindings = [
            {
                "binding_kind": "RoleBinding",
                "binding_name": "rb-1",
                "namespace": "default",
                "subjects": [
                    {"kind": "User", "name": "admin", "namespace": None},
                ],
                "role_ref": {"kind": "Role", "name": "reader"},
            },
        ]

        index = index_bindings_by_service_account(bindings)

        assert len(index) == 0  # noqa: PLR2004

    def test_index_bindings_skips_null_namespace(self) -> None:
        bindings = [
            {
                "binding_kind": "ClusterRoleBinding",
                "binding_name": "crb-1",
                "namespace": None,
                "subjects": [
                    {"kind": "ServiceAccount", "name": "orphan", "namespace": None},
                ],
                "role_ref": {"kind": "ClusterRole", "name": "admin"},
            },
        ]

        index = index_bindings_by_service_account(bindings)

        assert len(index) == 0  # noqa: PLR2004

    def test_index_pods_by_service_account_groups_pods(self) -> None:
        pod_owners = [
            {"pod_name": "web-1", "namespace": "default", "service_account_name": "web-sa"},
            {"pod_name": "web-2", "namespace": "default", "service_account_name": "web-sa"},
            {"pod_name": "worker-1", "namespace": "default", "service_account_name": "worker-sa"},
        ]

        index = index_pods_by_service_account(pod_owners)

        assert len(index) == 2  # noqa: PLR2004
        assert index[("default", "web-sa")] == ["web-1", "web-2"]
        assert index[("default", "worker-sa")] == ["worker-1"]

    def test_resolve_role_returns_cluster_role_by_name(self) -> None:
        cluster_roles = {
            "view": {
                "kind": "ClusterRole",
                "name": "view",
                "namespace": None,
                "rules": [],
                "labels": {},
                "aggregation_selectors": [],
            },
        }
        role_ref = {"kind": "ClusterRole", "name": "view"}
        binding = {
            "namespace": "default",
            "binding_kind": "ClusterRoleBinding",
            "binding_name": "crb-1",
            "subjects": [],
            "role_ref": role_ref,
        }

        result = resolve_role(role_ref, binding, cluster_roles, {})

        assert result is not None
        assert result["name"] == "view"

    def test_resolve_role_returns_namespaced_role(self) -> None:
        roles_by_ns_name = {
            ("default", "reader"): {
                "kind": "Role",
                "name": "reader",
                "namespace": "default",
                "rules": [],
                "labels": {},
                "aggregation_selectors": [],
            },
        }
        role_ref = {"kind": "Role", "name": "reader"}
        binding = {
            "namespace": "default",
            "binding_kind": "RoleBinding",
            "binding_name": "rb-1",
            "subjects": [],
            "role_ref": role_ref,
        }

        result = resolve_role(role_ref, binding, {}, roles_by_ns_name)

        assert result is not None
        assert result["name"] == "reader"

    def test_resolve_role_returns_none_when_not_found(self) -> None:
        role_ref = {"kind": "ClusterRole", "name": "nonexistent"}
        binding = {
            "namespace": "default",
            "binding_kind": "ClusterRoleBinding",
            "binding_name": "crb-1",
            "subjects": [],
            "role_ref": role_ref,
        }

        result = resolve_role(role_ref, binding, {}, {})

        assert result is None

    def test_to_response_converts_full_report(self) -> None:
        finding = RBACFinding(
            service_account="web-sa",
            namespace="default",
            risk_level="low",
            reasons=["Read-only access to pods"],
            current_permissions=[
                PolicyRule(verbs=["get", "list"], resources=["pods"], api_groups=[""]),
            ],
            pods_using=["web-1"],
            misconfigured=False,
            recommendation="No changes needed",
            suggested_role=SuggestedRole(
                kind="Role",
                rules=[PolicyRule(verbs=["get", "list"], resources=["pods"], api_groups=[""])],
                basis="audit_log",
            ),
        )
        unused = UnusedServiceAccount(name="orphan-sa", namespace="default")
        report = RBACAuditReport(
            findings=[finding],
            unused_service_accounts=[unused],
            excluded_system_service_accounts=["kube-system:default"],
            total_service_accounts_checked=3,
            summary="1 SA has bindings, 1 unused, 1 system excluded",
        )

        result = to_response(report)

        assert isinstance(result, AuditRbacPermissionsResponse)
        assert len(result.findings) == 1  # noqa: PLR2004
        assert result.findings[0]["service_account"] == "web-sa"
        assert result.findings[0]["risk_level"] == "low"
        assert len(result.findings[0]["current_permissions"]) == 1  # noqa: PLR2004
        assert result.findings[0]["suggested_role"]["kind"] == "Role"
        assert len(result.unused_service_accounts) == 1  # noqa: PLR2004
        assert result.unused_service_accounts[0]["name"] == "orphan-sa"
        assert result.excluded_system_service_accounts == ["kube-system:default"]
        assert result.total_service_accounts_checked == 3  # noqa: PLR2004

    """RED phase — will fail until use case is properly wired."""

    def test_execute_returns_response_with_empty_cluster(self) -> None:
        from hexawyn.application.use_case.security.audit_rbac_permissions.audit_rbac_permissions_use_case import (  # noqa: E501
            AuditRbacPermissionsUseCase,
        )

        port = MagicMock()
        port.list_service_accounts.return_value = []
        port.list_role_bindings.return_value = []
        port.list_roles.return_value = []
        port.list_pods_by_service_account.return_value = []
        port.fetch_api_usage.return_value = {"events": [], "available": []}

        use_case = AuditRbacPermissionsUseCase(rbac_port=port)
        result = use_case.audit_permissions(AuditRbacPermissionsCommand(window_days=30))

        assert isinstance(result, AuditRbacPermissionsResponse)
        assert result.total_service_accounts_checked == 0  # noqa: PLR2004

    def test_execute_excludes_system_namespace_service_accounts(self) -> None:
        from hexawyn.application.use_case.security.audit_rbac_permissions.audit_rbac_permissions_use_case import (  # noqa: E501
            AuditRbacPermissionsUseCase,
        )

        port = MagicMock()
        port.list_service_accounts.return_value = [
            {"name": "default", "namespace": "kube-system", "annotations": {}},
        ]
        port.list_role_bindings.return_value = []
        port.list_roles.return_value = []
        port.list_pods_by_service_account.return_value = []
        port.fetch_api_usage.return_value = {"events": [], "available": []}

        use_case = AuditRbacPermissionsUseCase(rbac_port=port)
        result = use_case.audit_permissions(AuditRbacPermissionsCommand())

        assert result.total_service_accounts_checked == 1  # noqa: PLR2004
        assert len(result.excluded_system_service_accounts) == 1  # noqa: PLR2004

    def test_execute_detects_unused_service_account(self) -> None:
        from hexawyn.application.use_case.security.audit_rbac_permissions.audit_rbac_permissions_use_case import (  # noqa: E501
            AuditRbacPermissionsUseCase,
        )

        port = MagicMock()
        port.list_service_accounts.return_value = [
            {"name": "unused-sa", "namespace": "default", "annotations": {}},
        ]
        port.list_role_bindings.return_value = []
        port.list_roles.return_value = []
        port.list_pods_by_service_account.return_value = []
        port.fetch_api_usage.return_value = {"events": [], "available": []}

        use_case = AuditRbacPermissionsUseCase(rbac_port=port)
        result = use_case.audit_permissions(AuditRbacPermissionsCommand())

        assert len(result.unused_service_accounts) == 1  # noqa: PLR2004
        assert result.unused_service_accounts[0]["name"] == "unused-sa"

    def test_execute_with_service_account_with_bindings_produces_findings(self) -> None:
        from hexawyn.application.use_case.security.audit_rbac_permissions.audit_rbac_permissions_use_case import (  # noqa: E501
            AuditRbacPermissionsUseCase,
        )

        port = MagicMock()
        port.list_service_accounts.return_value = [
            {"name": "web-sa", "namespace": "default", "annotations": {}},
        ]
        port.list_role_bindings.return_value = [
            {
                "binding_kind": "RoleBinding",
                "binding_name": "read-pods",
                "namespace": "default",
                "subjects": [
                    {"kind": "ServiceAccount", "name": "web-sa", "namespace": "default"},
                ],
                "role_ref": {"kind": "Role", "name": "pod-reader"},
            },
        ]
        port.list_roles.return_value = [
            {
                "kind": "Role",
                "name": "pod-reader",
                "namespace": "default",
                "rules": [
                    {"verbs": ["get", "list"], "resources": ["pods"], "api_groups": [""]},
                ],
                "labels": {},
                "aggregation_selectors": [],
            },
        ]
        port.list_pods_by_service_account.return_value = [
            {"pod_name": "web-1", "namespace": "default", "service_account_name": "web-sa"},
        ]
        port.fetch_api_usage.return_value = {
            "events": [
                {
                    "service_account": "web-sa",
                    "namespace": "default",
                    "verb": "get",
                    "resource": "pods",
                    "timestamp": "2026-07-01T00:00:00Z",
                },
            ],
            "available": True,
        }

        use_case = AuditRbacPermissionsUseCase(rbac_port=port)
        result = use_case.audit_permissions(AuditRbacPermissionsCommand(window_days=30))

        assert isinstance(result, AuditRbacPermissionsResponse)
        assert len(result.findings) == 1  # noqa: PLR2004
        finding = result.findings[0]
        assert finding["service_account"] == "web-sa"
        assert finding["pods_using"] == ["web-1"]
        assert finding["risk_level"] in ("low", "medium", "high", "critical")

    def test_execute_with_cluster_admin_and_misconfigured_binding(self) -> None:
        from hexawyn.application.use_case.security.audit_rbac_permissions.audit_rbac_permissions_use_case import (  # noqa: E501
            AuditRbacPermissionsUseCase,
        )

        port = MagicMock()
        port.list_service_accounts.return_value = [
            {"name": "admin-sa", "namespace": "default", "annotations": {}},
        ]
        port.list_role_bindings.return_value = [
            {
                "binding_kind": "RoleBinding",
                "binding_name": "admin-access",
                "namespace": "default",
                "subjects": [
                    {"kind": "ServiceAccount", "name": "admin-sa", "namespace": "default"},
                ],
                "role_ref": {"kind": "ClusterRole", "name": "cluster-admin"},
            },
            {
                "binding_kind": "RoleBinding",
                "binding_name": "ghost-role",
                "namespace": "default",
                "subjects": [
                    {"kind": "ServiceAccount", "name": "admin-sa", "namespace": "default"},
                ],
                "role_ref": {"kind": "Role", "name": "nonexistent"},
            },
        ]
        port.list_roles.return_value = [
            {
                "kind": "ClusterRole",
                "name": "cluster-admin",
                "namespace": None,
                "rules": [
                    {"verbs": ["*"], "resources": ["*", "nodes"], "api_groups": ["*"]},
                ],
                "labels": {},
                "aggregation_selectors": [],
            },
        ]
        port.list_pods_by_service_account.return_value = [
            {"pod_name": "admin-app", "namespace": "default", "service_account_name": "admin-sa"},
        ]
        port.fetch_api_usage.return_value = {
            "events": [],
            "available": False,
        }

        use_case = AuditRbacPermissionsUseCase(rbac_port=port)
        result = use_case.audit_permissions(AuditRbacPermissionsCommand(window_days=30))

        assert len(result.findings) == 1  # noqa: PLR2004
        finding = result.findings[0]
        assert finding["risk_level"] == "critical"
        assert finding["misconfigured"] is True
        assert "cluster-admin" in finding["reasons"][0]
