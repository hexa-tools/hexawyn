"""Unit tests for build_recommendation — reproduces the ticket's own
recommendation strings exactly for each status."""

from __future__ import annotations


class TestBuildRecommendation:
    def test_tc1_open_namespace_ticket_exact_text(self) -> None:
        """Test Data: dev -> "Apply default-deny NetworkPolicy for both ingress and egress"."""
        from hexawyn.domain.services.network_policy.recommendation_builder import (
            build_recommendation,
        )

        result = build_recommendation(network_status="open", ingress_policies=0, egress_policies=0)

        assert result == "Apply default-deny NetworkPolicy for both ingress and egress"

    def test_tc2_missing_egress_ticket_exact_text(self) -> None:
        """Test Data: staging (ingress=2, egress=0) -> "Add default-deny egress NetworkPolicy"."""
        from hexawyn.domain.services.network_policy.recommendation_builder import (
            build_recommendation,
        )

        result = build_recommendation(
            network_status="partially_restricted", ingress_policies=2, egress_policies=0
        )

        assert result == "Add default-deny egress NetworkPolicy"

    def test_missing_ingress_recommends_ingress_policy(self) -> None:
        from hexawyn.domain.services.network_policy.recommendation_builder import (
            build_recommendation,
        )

        result = build_recommendation(
            network_status="partially_restricted", ingress_policies=0, egress_policies=3
        )

        assert result == "Add default-deny ingress NetworkPolicy"

    def test_tc3_restricted_namespace_has_no_recommendation(self) -> None:
        """Test Data: production (ingress=5, egress=3) -> no recommendation key."""
        from hexawyn.domain.services.network_policy.recommendation_builder import (
            build_recommendation,
        )

        result = build_recommendation(
            network_status="restricted", ingress_policies=5, egress_policies=3
        )

        assert result is None
