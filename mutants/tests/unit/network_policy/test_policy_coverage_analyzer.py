"""Unit tests for provides_ingress_restriction / provides_egress_restriction.

Test Scenario 5 / Checker case 2: a NetworkPolicy with zero rules provides
no effective restriction, regardless of podSelector or policyTypes — taken
literally from the ticket's own wording, not full k8s policyTypes-defaulting
semantics (out of scope, untested by any Test Scenario)."""

from __future__ import annotations


class TestProvidesIngressRestriction:
    def test_zero_rules_provides_no_restriction(self) -> None:
        from hexawyn.domain.services.network_policy.policy_coverage_analyzer import (
            provides_ingress_restriction,
        )

        assert provides_ingress_restriction(0) is False

    def test_at_least_one_rule_provides_restriction(self) -> None:
        from hexawyn.domain.services.network_policy.policy_coverage_analyzer import (
            provides_ingress_restriction,
        )

        assert provides_ingress_restriction(1) is True


class TestProvidesEgressRestriction:
    def test_zero_rules_provides_no_restriction(self) -> None:
        from hexawyn.domain.services.network_policy.policy_coverage_analyzer import (
            provides_egress_restriction,
        )

        assert provides_egress_restriction(0) is False

    def test_at_least_one_rule_provides_restriction(self) -> None:
        from hexawyn.domain.services.network_policy.policy_coverage_analyzer import (
            provides_egress_restriction,
        )

        assert provides_egress_restriction(3) is True
