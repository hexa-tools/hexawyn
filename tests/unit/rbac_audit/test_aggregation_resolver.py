"""Unit tests for resolve_effective_rules — union of an aggregated
ClusterRole's own rules with every other ClusterRole whose labels match
one of its aggregationRule.clusterRoleSelectors (matchLabels)."""

from __future__ import annotations

from hexawyn.domain.models.rbac_audit import ClusterRoleCandidate, PolicyRule


def _rule(verbs: list[str], resources: list[str]) -> PolicyRule:
    return PolicyRule(verbs=verbs, resources=resources, api_groups=[""])


class TestResolveEffectiveRules:
    def test_no_selectors_returns_own_rules_only(self) -> None:
        from hexawyn.domain.services.rbac_audit.aggregation_resolver import (
            resolve_effective_rules,
        )

        result = resolve_effective_rules(
            own_rules=[_rule(["get"], ["pods"])],
            aggregation_selectors=[],
            all_cluster_roles=[],
        )

        assert result == [_rule(["get"], ["pods"])]

    def test_aggregates_three_sub_roles_matching_selector(self) -> None:
        """Ticket edge case: ClusterRole aggregates 3 sub-roles -> the union
        of all their permissions must be computed, not just the first match."""
        from hexawyn.domain.services.rbac_audit.aggregation_resolver import (
            resolve_effective_rules,
        )

        selector = {"rbac.example.com/aggregate-to-monitoring": "true"}
        sub_roles = [
            ClusterRoleCandidate(
                name="view-pods",
                labels=selector,
                rules=[_rule(["get", "list"], ["pods"])],
            ),
            ClusterRoleCandidate(
                name="view-secrets",
                labels=selector,
                rules=[_rule(["get"], ["secrets"])],
            ),
            ClusterRoleCandidate(
                name="view-configmaps",
                labels=selector,
                rules=[_rule(["get"], ["configmaps"])],
            ),
            ClusterRoleCandidate(
                name="unrelated-role",
                labels={"other": "label"},
                rules=[_rule(["*"], ["*"])],
            ),
        ]

        result = resolve_effective_rules(
            own_rules=[],
            aggregation_selectors=[selector],
            all_cluster_roles=sub_roles,
        )

        assert _rule(["get", "list"], ["pods"]) in result
        assert _rule(["get"], ["secrets"]) in result
        assert _rule(["get"], ["configmaps"]) in result
        assert _rule(["*"], ["*"]) not in result
        assert len(result) == 3

    def test_own_rules_are_kept_alongside_aggregated_rules(self) -> None:
        from hexawyn.domain.services.rbac_audit.aggregation_resolver import (
            resolve_effective_rules,
        )

        selector = {"aggregate": "true"}
        sub_role = ClusterRoleCandidate(
            name="sub", labels=selector, rules=[_rule(["get"], ["secrets"])]
        )

        result = resolve_effective_rules(
            own_rules=[_rule(["get"], ["pods"])],
            aggregation_selectors=[selector],
            all_cluster_roles=[sub_role],
        )

        assert _rule(["get"], ["pods"]) in result
        assert _rule(["get"], ["secrets"]) in result

    def test_partial_label_match_does_not_qualify(self) -> None:
        from hexawyn.domain.services.rbac_audit.aggregation_resolver import (
            resolve_effective_rules,
        )

        selector = {"a": "1", "b": "2"}
        candidate = ClusterRoleCandidate(name="c", labels={"a": "1"}, rules=[_rule(["*"], ["*"])])

        result = resolve_effective_rules(
            own_rules=[],
            aggregation_selectors=[selector],
            all_cluster_roles=[candidate],
        )

        assert result == []

    def test_duplicate_rules_are_not_repeated(self) -> None:
        from hexawyn.domain.services.rbac_audit.aggregation_resolver import (
            resolve_effective_rules,
        )

        selector = {"aggregate": "true"}
        candidate = ClusterRoleCandidate(
            name="dup", labels=selector, rules=[_rule(["get"], ["pods"])]
        )

        result = resolve_effective_rules(
            own_rules=[_rule(["get"], ["pods"])],
            aggregation_selectors=[selector],
            all_cluster_roles=[candidate],
        )

        assert result == [_rule(["get"], ["pods"])]
