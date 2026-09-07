"""Unit tests for is_misconfigured_binding — a namespace-scoped RoleBinding
referencing a ClusterRole whose rules target a cluster-scoped resource is a
no-op for that rule inside the namespace, and is flagged as a misconfiguration."""

from __future__ import annotations

from hexawyn.domain.models.rbac_audit import PolicyRule


def _rule(resources: list[str]) -> PolicyRule:
    return PolicyRule(verbs=["get"], resources=resources, api_groups=[""])


class TestIsMisconfiguredBinding:
    def test_role_binding_targeting_cluster_scoped_resource_is_misconfigured(
        self,
    ) -> None:
        from hexawyn.domain.services.rbac_audit.misconfiguration import (
            is_misconfigured_binding,
        )

        result = is_misconfigured_binding(
            binding_kind="RoleBinding", effective_rules=[_rule(["nodes"])]
        )

        assert result is True

    def test_role_binding_targeting_namespaced_resource_is_not_misconfigured(
        self,
    ) -> None:
        from hexawyn.domain.services.rbac_audit.misconfiguration import (
            is_misconfigured_binding,
        )

        result = is_misconfigured_binding(
            binding_kind="RoleBinding", effective_rules=[_rule(["pods"])]
        )

        assert result is False

    def test_cluster_role_binding_is_never_misconfigured(self) -> None:
        """ClusterRoleBinding is cluster-scoped by nature; the check only
        applies to namespace-scoped RoleBinding."""
        from hexawyn.domain.services.rbac_audit.misconfiguration import (
            is_misconfigured_binding,
        )

        result = is_misconfigured_binding(
            binding_kind="ClusterRoleBinding", effective_rules=[_rule(["nodes"])]
        )

        assert result is False

    def test_no_rules_is_not_misconfigured(self) -> None:
        from hexawyn.domain.services.rbac_audit.misconfiguration import (
            is_misconfigured_binding,
        )

        result = is_misconfigured_binding(binding_kind="RoleBinding", effective_rules=[])

        assert result is False

    def test_mixed_namespaced_and_cluster_scoped_resources_is_misconfigured(
        self,
    ) -> None:
        from hexawyn.domain.services.rbac_audit.misconfiguration import (
            is_misconfigured_binding,
        )

        result = is_misconfigured_binding(
            binding_kind="RoleBinding",
            effective_rules=[_rule(["pods"]), _rule(["clusterroles"])],
        )

        assert result is True
