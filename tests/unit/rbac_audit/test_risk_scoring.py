"""Unit tests for the deterministic RBAC risk matrix.

Priority order, no LLM/heuristic ambiguity:
1. cluster-admin binding -> always critical, no exceptions.
2. Any rule granting all resources ("*") -> critical.
3. Any rule granting a wildcard verb ("*") -> high; if that rule also
   targets secrets, a dedicated reason is always appended.
4. Otherwise, breadth-scored: narrow -> low ("healthy"), else -> medium.
"""

from __future__ import annotations

from hexawyn.domain.models.rbac_audit import PolicyRule


def _rule(
    verbs: list[str], resources: list[str], api_groups: list[str] | None = None
) -> PolicyRule:
    return PolicyRule(verbs=verbs, resources=resources, api_groups=api_groups or [""])


class TestClassifyRiskLevel:
    def test_tc1_cluster_admin_binding_is_always_critical(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import classify_risk_level

        level = classify_risk_level(
            is_cluster_admin=True, effective_rules=[_rule(["get"], ["pods"])]
        )

        assert level == "critical"

    def test_cluster_admin_overrides_even_narrow_looking_rules(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import classify_risk_level

        level = classify_risk_level(is_cluster_admin=True, effective_rules=[])

        assert level == "critical"

    def test_wildcard_resource_is_critical(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import classify_risk_level

        level = classify_risk_level(is_cluster_admin=False, effective_rules=[_rule(["get"], ["*"])])

        assert level == "critical"

    def test_tc2_wildcard_verb_on_secrets_is_high_not_critical(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import classify_risk_level

        level = classify_risk_level(
            is_cluster_admin=False, effective_rules=[_rule(["*"], ["secrets"])]
        )

        assert level == "high"

    def test_wildcard_verb_on_non_secrets_is_high(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import classify_risk_level

        level = classify_risk_level(
            is_cluster_admin=False, effective_rules=[_rule(["*"], ["configmaps"])]
        )

        assert level == "high"

    def test_tc3_narrow_single_verb_single_resource_is_low(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import classify_risk_level

        level = classify_risk_level(
            is_cluster_admin=False, effective_rules=[_rule(["get"], ["pods"])]
        )

        assert level == "low"

    def test_broad_non_wildcard_permissions_are_medium(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import classify_risk_level

        level = classify_risk_level(
            is_cluster_admin=False,
            effective_rules=[
                _rule(
                    ["get", "list", "create", "update", "delete"],
                    ["pods", "deployments"],
                )
            ],
        )

        assert level == "medium"

    def test_no_rules_at_all_is_low(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import classify_risk_level

        level = classify_risk_level(is_cluster_admin=False, effective_rules=[])

        assert level == "low"


class TestBuildRiskReasons:
    def test_cluster_admin_reason_is_present(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import build_risk_reasons

        reasons = build_risk_reasons(is_cluster_admin=True, effective_rules=[])

        assert any("cluster-admin" in reason for reason in reasons)

    def test_wildcard_resource_reason_is_present(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import build_risk_reasons

        reasons = build_risk_reasons(
            is_cluster_admin=False, effective_rules=[_rule(["get"], ["*"])]
        )

        assert any("all resources" in reason for reason in reasons)

    def test_wildcard_verb_on_secrets_reason_is_never_missing(self) -> None:
        """Checker Node edge case: a wildcard verb on secrets must always be
        surfaced as its own reason, regardless of the overall risk bucket."""
        from hexawyn.domain.services.rbac_audit.risk_scoring import build_risk_reasons

        reasons = build_risk_reasons(
            is_cluster_admin=False, effective_rules=[_rule(["*"], ["secrets"])]
        )

        assert any("secrets" in reason for reason in reasons)

    def test_wildcard_verb_on_non_secrets_has_no_secrets_reason(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import build_risk_reasons

        reasons = build_risk_reasons(
            is_cluster_admin=False, effective_rules=[_rule(["*"], ["configmaps"])]
        )

        assert not any("secrets" in reason for reason in reasons)

    def test_narrow_permissions_have_no_reasons(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import build_risk_reasons

        reasons = build_risk_reasons(
            is_cluster_admin=False, effective_rules=[_rule(["get"], ["pods"])]
        )

        assert reasons == []


class TestComputePermissionBreadth:
    def test_single_verb_single_resource_is_narrow(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import (
            compute_permission_breadth,
        )

        breadth = compute_permission_breadth([_rule(["get"], ["pods"])])

        assert breadth == 1

    def test_multiple_verbs_and_resources_multiply(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import (
            compute_permission_breadth,
        )

        breadth = compute_permission_breadth(
            [_rule(["get", "list", "create"], ["pods", "deployments"])]
        )

        assert breadth == 6  # noqa: PLR2004

    def test_no_rules_has_zero_breadth(self) -> None:
        from hexawyn.domain.services.rbac_audit.risk_scoring import (
            compute_permission_breadth,
        )

        assert compute_permission_breadth([]) == 0
