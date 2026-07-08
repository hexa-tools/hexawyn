"""Unit tests for suggest_minimal_role / build_recommendation.

When an audit log is available, the suggestion is built from the actual
distinct (verb, resource) pairs observed, tagged basis="audit_log" — even
when that means suggesting zero rules (unused permissions, Test Scenario 5).
When no audit log is configured, the suggestion falls back to narrowing the
current rules' verbs to read-only, tagged basis="estimated" (Checker case 5:
never present an "estimated" suggestion as if it were audit-log-precise).
"""

from __future__ import annotations

from hexawyn.domain.models.rbac_audit import PolicyRule, SuggestedRole


def _rule(verbs: list[str], resources: list[str]) -> PolicyRule:
    return PolicyRule(verbs=verbs, resources=resources, api_groups=[""])


class TestSuggestMinimalRoleWithAuditLog:
    def test_suggests_role_from_observed_verb_resource_pairs(self) -> None:
        from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
            suggest_minimal_role,
        )

        suggestion = suggest_minimal_role(
            effective_rules=[_rule(["*"], ["*"])],
            api_usage_available=True,
            observed_verb_resource_pairs=[("get", "pods"), ("list", "pods")],
        )

        assert suggestion.kind == "Role"
        assert suggestion.basis == "audit_log"
        assert suggestion.rules == [
            PolicyRule(verbs=["get", "list"], resources=["pods"], api_groups=[""])
        ]

    def test_tc5_zero_observed_usage_recommends_empty_rules(self) -> None:
        from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
            suggest_minimal_role,
        )

        suggestion = suggest_minimal_role(
            effective_rules=[_rule(["get"], ["configmaps"])],
            api_usage_available=True,
            observed_verb_resource_pairs=[],
        )

        assert suggestion.basis == "audit_log"
        assert suggestion.rules == []


class TestSuggestMinimalRoleWithoutAuditLog:
    def test_narrows_wildcard_verb_to_read_only_and_tags_estimated(self) -> None:
        from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
            suggest_minimal_role,
        )

        suggestion = suggest_minimal_role(
            effective_rules=[_rule(["*"], ["secrets"])],
            api_usage_available=False,
            observed_verb_resource_pairs=[],
        )

        assert suggestion.basis == "estimated"
        assert suggestion.rules == [
            PolicyRule(verbs=["get", "list", "watch"], resources=["secrets"], api_groups=[""])
        ]

    def test_drops_rule_with_no_read_verbs_at_all(self) -> None:
        from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
            suggest_minimal_role,
        )

        suggestion = suggest_minimal_role(
            effective_rules=[_rule(["create", "delete"], ["pods"])],
            api_usage_available=False,
            observed_verb_resource_pairs=[],
        )

        assert suggestion.rules == []

    def test_keeps_only_the_read_verbs_already_granted(self) -> None:
        from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
            suggest_minimal_role,
        )

        suggestion = suggest_minimal_role(
            effective_rules=[_rule(["get", "create"], ["pods"])],
            api_usage_available=False,
            observed_verb_resource_pairs=[],
        )

        assert suggestion.rules == [PolicyRule(verbs=["get"], resources=["pods"], api_groups=[""])]


class TestBuildRecommendation:
    def test_low_risk_needs_no_action(self) -> None:
        from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
            build_recommendation,
        )

        recommendation = build_recommendation(
            risk_level="low",
            namespace="production",
            suggested_role=SuggestedRole(
                kind="Role", rules=[_rule(["get"], ["pods"])], basis="estimated"
            ),
        )

        assert recommendation == "Current permissions are minimal — no action needed."

    def test_confirmed_zero_usage_overrides_low_risk_shortcut(self) -> None:
        """TC5: even when breadth-scoring alone would call this SA 'low' risk,
        an audit log confirming zero real usage must still recommend removal
        — proof of non-use always wins over a heuristic risk bucket."""
        from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
            build_recommendation,
        )

        recommendation = build_recommendation(
            risk_level="low",
            namespace="production",
            suggested_role=SuggestedRole(kind="Role", rules=[], basis="audit_log"),
        )

        assert "remove" in recommendation.lower()

    def test_estimated_basis_with_no_read_verbs_at_all_still_recommends_removal(self) -> None:
        """A medium/high-risk SA whose rules grant only write verbs (no
        get/list/watch) narrows to zero estimated rules — the fallback
        removal wording must apply even though basis is "estimated", not
        "audit_log"."""
        from hexawyn.domain.services.rbac_audit.minimal_role_suggester import build_recommendation

        recommendation = build_recommendation(
            risk_level="medium",
            namespace="production",
            suggested_role=SuggestedRole(kind="Role", rules=[], basis="estimated"),
        )

        assert "remove" in recommendation.lower()

    def test_zero_suggested_rules_recommends_removal(self) -> None:
        from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
            build_recommendation,
        )

        recommendation = build_recommendation(
            risk_level="high",
            namespace="monitoring",
            suggested_role=SuggestedRole(kind="Role", rules=[], basis="audit_log"),
        )

        assert "remove" in recommendation.lower()

    def test_critical_risk_names_verbs_resources_and_namespace(self) -> None:
        from hexawyn.domain.services.rbac_audit.minimal_role_suggester import (
            build_recommendation,
        )

        recommendation = build_recommendation(
            risk_level="critical",
            namespace="production",
            suggested_role=SuggestedRole(
                kind="Role",
                rules=[PolicyRule(verbs=["get", "list"], resources=["pods"], api_groups=[""])],
                basis="estimated",
            ),
        )

        assert "get/list" in recommendation
        assert "pods" in recommendation
        assert "production" in recommendation
