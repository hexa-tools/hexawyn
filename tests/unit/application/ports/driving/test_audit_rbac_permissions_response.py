from __future__ import annotations


class TestAuditRBACPermissionsResponse:
    def test_defaults(self) -> None:
        from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_response import (
            AuditRBACPermissionsResponse,
        )

        response = AuditRBACPermissionsResponse()

        assert response.findings == []
        assert response.unused_service_accounts == []
        assert response.excluded_system_service_accounts == []
        assert response.total_service_accounts_checked == 0
        assert response.summary == ""
        assert response.error is None

    def test_accepts_explicit_values(self) -> None:
        from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_response import (
            AuditRBACPermissionsResponse,
            PolicyRuleDict,
            RBACFindingDict,
            SuggestedRoleDict,
            UnusedServiceAccountDict,
        )

        rule: PolicyRuleDict = {"verbs": ["*"], "resources": ["*"], "api_groups": ["*"]}
        suggested: SuggestedRoleDict = {
            "kind": "Role",
            "rules": [{"verbs": ["get", "list"], "resources": ["pods"], "api_groups": [""]}],
            "basis": "estimated",
        }
        finding: RBACFindingDict = {
            "service_account": "payment-sa",
            "namespace": "production",
            "risk_level": "critical",
            "reasons": ["bound to cluster-admin"],
            "current_permissions": [rule],
            "pods_using": ["payment-pod-abc"],
            "misconfigured": False,
            "recommendation": "Replace with a Role limited to: get/list pods in the production namespace.",
            "suggested_role": suggested,
        }
        unused: UnusedServiceAccountDict = {"name": "idle-sa", "namespace": "staging"}

        response = AuditRBACPermissionsResponse(
            findings=[finding],
            unused_service_accounts=[unused],
            excluded_system_service_accounts=["kube-system:default"],
            total_service_accounts_checked=12,
            summary="1 over-privileged service account found, 1 critical.",
            error=None,
        )

        assert response.findings == [finding]
        assert response.unused_service_accounts == [unused]
        assert response.excluded_system_service_accounts == ["kube-system:default"]
        assert response.total_service_accounts_checked == 12
        assert response.summary == "1 over-privileged service account found, 1 critical."
