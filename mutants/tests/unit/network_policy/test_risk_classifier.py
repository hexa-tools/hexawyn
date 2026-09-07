"""Unit tests for classify_risk_level.

Checker case 1: a namespace with zero pods is always low risk, regardless of
network_status — no pods means no real east-west attack surface."""

from __future__ import annotations


class TestClassifyRiskLevel:
    def test_tc1_open_with_pods_is_critical(self) -> None:
        from hexawyn.domain.services.network_policy.risk_classifier import classify_risk_level

        result = classify_risk_level(network_status="open", pod_count=8)

        assert result == "critical"

    def test_tc2_partially_restricted_with_pods_is_medium(self) -> None:
        from hexawyn.domain.services.network_policy.risk_classifier import classify_risk_level

        result = classify_risk_level(network_status="partially_restricted", pod_count=12)

        assert result == "medium"

    def test_tc3_restricted_with_pods_is_low(self) -> None:
        from hexawyn.domain.services.network_policy.risk_classifier import classify_risk_level

        result = classify_risk_level(network_status="restricted", pod_count=45)

        assert result == "low"

    def test_checker_case_1_open_namespace_with_zero_pods_is_low_not_critical(self) -> None:
        from hexawyn.domain.services.network_policy.risk_classifier import classify_risk_level

        result = classify_risk_level(network_status="open", pod_count=0)

        assert result == "low"

    def test_zero_pods_is_low_regardless_of_status(self) -> None:
        from hexawyn.domain.services.network_policy.risk_classifier import classify_risk_level

        assert classify_risk_level(network_status="partially_restricted", pod_count=0) == "low"
        assert classify_risk_level(network_status="restricted", pod_count=0) == "low"
