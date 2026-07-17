from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.gitops.policy_detector import PolicyDetector
from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.domain.errors import PolicyEngineNotFoundError
from hexawyn.domain.models.policy import PolicyEngine


class TestPolicyDetector:
    def test_implements_policy_port(self) -> None:
        detector = PolicyDetector()
        assert isinstance(detector, PolicyPort)

    def test_detect_engine_returns_none(self) -> None:
        detector = PolicyDetector()
        result = detector.detect_engine()
        assert result.engine == PolicyEngine.NONE
        assert result.total_policies == 0

    def test_list_policies_raises(self) -> None:
        detector = PolicyDetector()
        with pytest.raises(PolicyEngineNotFoundError):
            detector.list_policies()

    def test_get_policy_raises(self) -> None:
        detector = PolicyDetector()
        with pytest.raises(PolicyEngineNotFoundError):
            detector.get_policy(name="x")

    def test_list_violations_raises(self) -> None:
        detector = PolicyDetector()
        with pytest.raises(PolicyEngineNotFoundError):
            detector.list_violations()

    def test_explain_denial_raises(self) -> None:
        detector = PolicyDetector()
        with pytest.raises(PolicyEngineNotFoundError):
            detector.explain_denial(resource_kind="Pod", resource_name="x", namespace="ns")

    def test_audit_raises(self) -> None:
        detector = PolicyDetector()
        with pytest.raises(PolicyEngineNotFoundError):
            detector.audit()
