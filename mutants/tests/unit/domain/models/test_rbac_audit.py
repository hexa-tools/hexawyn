"""Unit tests for the Service Account RBAC Audit domain models."""

from __future__ import annotations

import dataclasses

import pytest


class TestPolicyRule:
    def test_creates_rule_with_expected_fields(self) -> None:
        from hexawyn.domain.models.rbac_audit import PolicyRule

        rule = PolicyRule(verbs=["get", "list"], resources=["pods"], api_groups=[""])

        assert rule.verbs == ["get", "list"]
        assert rule.resources == ["pods"]
        assert rule.api_groups == [""]

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.rbac_audit import PolicyRule

        rule = PolicyRule(verbs=["get"], resources=["pods"], api_groups=[""])

        with pytest.raises(dataclasses.FrozenInstanceError):
            rule.verbs = ["*"]  # type: ignore[misc]


class TestClusterRoleCandidate:
    def test_creates_candidate_with_expected_fields(self) -> None:
        from hexawyn.domain.models.rbac_audit import ClusterRoleCandidate, PolicyRule

        candidate = ClusterRoleCandidate(
            name="secrets-reader",
            labels={"rbac.example.com/aggregate-to-monitoring": "true"},
            rules=[PolicyRule(verbs=["get"], resources=["secrets"], api_groups=[""])],
        )

        assert candidate.name == "secrets-reader"
        assert candidate.labels == {"rbac.example.com/aggregate-to-monitoring": "true"}
        assert candidate.rules[0].resources == ["secrets"]

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.rbac_audit import ClusterRoleCandidate

        candidate = ClusterRoleCandidate(name="r", labels={}, rules=[])

        with pytest.raises(dataclasses.FrozenInstanceError):
            candidate.name = "other"  # type: ignore[misc]


class TestRoleBindingRef:
    def test_creates_cluster_scoped_binding(self) -> None:
        from hexawyn.domain.models.rbac_audit import RoleBindingRef

        ref = RoleBindingRef(
            binding_kind="ClusterRoleBinding",
            binding_name="payment-sa-admin",
            role_kind="ClusterRole",
            role_name="cluster-admin",
            namespace=None,
        )

        assert ref.binding_kind == "ClusterRoleBinding"
        assert ref.binding_name == "payment-sa-admin"
        assert ref.role_kind == "ClusterRole"
        assert ref.role_name == "cluster-admin"
        assert ref.namespace is None

    def test_creates_namespace_scoped_binding(self) -> None:
        from hexawyn.domain.models.rbac_audit import RoleBindingRef

        ref = RoleBindingRef(
            binding_kind="RoleBinding",
            binding_name="monitoring-secrets-reader",
            role_kind="ClusterRole",
            role_name="secrets-reader",
            namespace="monitoring",
        )

        assert ref.namespace == "monitoring"

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.rbac_audit import RoleBindingRef

        ref = RoleBindingRef(
            binding_kind="RoleBinding",
            binding_name="b",
            role_kind="Role",
            role_name="r",
            namespace="ns",
        )

        with pytest.raises(dataclasses.FrozenInstanceError):
            ref.role_name = "other"  # type: ignore[misc]


class TestSuggestedRole:
    def test_creates_suggested_role(self) -> None:
        from hexawyn.domain.models.rbac_audit import PolicyRule, SuggestedRole

        suggestion = SuggestedRole(
            kind="Role",
            rules=[PolicyRule(verbs=["get", "list"], resources=["pods"], api_groups=[""])],
            basis="audit_log",
        )

        assert suggestion.kind == "Role"
        assert suggestion.rules[0].resources == ["pods"]
        assert suggestion.basis == "audit_log"

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.rbac_audit import SuggestedRole

        suggestion = SuggestedRole(kind="Role", rules=[], basis="estimated")

        with pytest.raises(dataclasses.FrozenInstanceError):
            suggestion.basis = "audit_log"  # type: ignore[misc]


class TestRBACFinding:
    def test_creates_finding_with_expected_fields(self) -> None:
        from hexawyn.domain.models.rbac_audit import (
            PolicyRule,
            RBACFinding,
            SuggestedRole,
        )

        finding = RBACFinding(
            service_account="payment-sa",
            namespace="production",
            risk_level="critical",
            reasons=["bound to cluster-admin"],
            current_permissions=[PolicyRule(verbs=["*"], resources=["*"], api_groups=["*"])],
            pods_using=["payment-pod-abc", "payment-pod-def"],
            misconfigured=False,
            recommendation="Replace with Role limited to: get/list pods in production namespace",
            suggested_role=SuggestedRole(
                kind="Role",
                rules=[PolicyRule(verbs=["get", "list"], resources=["pods"], api_groups=[""])],
                basis="estimated",
            ),
        )

        assert finding.service_account == "payment-sa"
        assert finding.namespace == "production"
        assert finding.risk_level == "critical"
        assert finding.reasons == ["bound to cluster-admin"]
        assert finding.pods_using == ["payment-pod-abc", "payment-pod-def"]
        assert finding.misconfigured is False
        assert finding.suggested_role.basis == "estimated"

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.rbac_audit import RBACFinding, SuggestedRole

        finding = RBACFinding(
            service_account="sa",
            namespace="ns",
            risk_level="low",
            reasons=[],
            current_permissions=[],
            pods_using=[],
            misconfigured=False,
            recommendation="No action needed.",
            suggested_role=SuggestedRole(kind="Role", rules=[], basis="estimated"),
        )

        with pytest.raises(dataclasses.FrozenInstanceError):
            finding.risk_level = "high"  # type: ignore[misc]


class TestUnusedServiceAccount:
    def test_creates_unused_service_account(self) -> None:
        from hexawyn.domain.models.rbac_audit import UnusedServiceAccount

        unused = UnusedServiceAccount(name="idle-sa", namespace="staging")

        assert unused.name == "idle-sa"
        assert unused.namespace == "staging"


class TestRBACAuditReport:
    def test_creates_report_with_expected_fields(self) -> None:
        from hexawyn.domain.models.rbac_audit import (
            PolicyRule,
            RBACAuditReport,
            RBACFinding,
            SuggestedRole,
            UnusedServiceAccount,
        )

        finding = RBACFinding(
            service_account="payment-sa",
            namespace="production",
            risk_level="critical",
            reasons=["bound to cluster-admin"],
            current_permissions=[PolicyRule(verbs=["*"], resources=["*"], api_groups=["*"])],
            pods_using=["payment-pod-abc"],
            misconfigured=False,
            recommendation="Replace with Role limited to: get/list pods in production namespace",
            suggested_role=SuggestedRole(kind="Role", rules=[], basis="estimated"),
        )
        report = RBACAuditReport(
            findings=[finding],
            unused_service_accounts=[UnusedServiceAccount(name="idle-sa", namespace="staging")],
            excluded_system_service_accounts=["kube-system:default"],
            total_service_accounts_checked=12,
            summary="1 over-privileged service account found.",
        )

        assert report.findings == [finding]
        assert report.unused_service_accounts == [
            UnusedServiceAccount(name="idle-sa", namespace="staging")
        ]
        assert report.excluded_system_service_accounts == ["kube-system:default"]
        assert report.total_service_accounts_checked == 12  # noqa: PLR2004
        assert report.summary == "1 over-privileged service account found."
