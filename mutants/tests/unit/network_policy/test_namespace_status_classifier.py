"""Unit tests for classify_network_status.

Checker case 5: ingress and egress are independent counts — a namespace
with only egress policies must be "ingress open, egress restricted," never
the reverse."""

from __future__ import annotations


class TestClassifyNetworkStatus:
    def test_tc1_zero_ingress_zero_egress_is_open(self) -> None:
        from hexawyn.domain.services.network_policy.namespace_status_classifier import (
            classify_network_status,
        )

        assert classify_network_status(ingress_policies=0, egress_policies=0) == "open"

    def test_tc2_ingress_only_is_partially_restricted(self) -> None:
        from hexawyn.domain.services.network_policy.namespace_status_classifier import (
            classify_network_status,
        )

        assert (
            classify_network_status(ingress_policies=2, egress_policies=0) == "partially_restricted"
        )

    def test_egress_only_is_partially_restricted_not_inverted(self) -> None:
        """Checker case 5's exact scenario: only egress policies exist."""
        from hexawyn.domain.services.network_policy.namespace_status_classifier import (
            classify_network_status,
        )

        assert (
            classify_network_status(ingress_policies=0, egress_policies=3) == "partially_restricted"
        )

    def test_tc3_both_present_is_restricted(self) -> None:
        from hexawyn.domain.services.network_policy.namespace_status_classifier import (
            classify_network_status,
        )

        assert classify_network_status(ingress_policies=5, egress_policies=3) == "restricted"
