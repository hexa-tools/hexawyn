"""Unit tests for has_empty_pod_selector. Edge Case 5: an empty podSelector
means the policy applies to all pods in the namespace — informational
context, not itself a restriction judgment."""

from __future__ import annotations


class TestHasEmptyPodSelector:
    def test_both_empty_is_empty_selector(self) -> None:
        from hexawyn.domain.services.network_policy.pod_selector_analyzer import (
            has_empty_pod_selector,
        )

        assert has_empty_pod_selector(match_labels={}, match_expressions=[]) is True

    def test_match_labels_present_is_not_empty(self) -> None:
        from hexawyn.domain.services.network_policy.pod_selector_analyzer import (
            has_empty_pod_selector,
        )

        assert (
            has_empty_pod_selector(match_labels={"app": "frontend"}, match_expressions=[]) is False
        )

    def test_match_expressions_present_is_not_empty(self) -> None:
        from hexawyn.domain.services.network_policy.pod_selector_analyzer import (
            has_empty_pod_selector,
        )

        assert has_empty_pod_selector(match_labels={}, match_expressions=[{"key": "tier"}]) is False
