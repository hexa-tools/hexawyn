from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.gitops.policy_detector import PolicyDetector
from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.policy import PolicyAction, PolicyEngine


def _kyverno_policy_item(name: str, action: str, message: str) -> dict:
    return {
        "metadata": {"name": name, "status": "Ready"},
        "spec": {
            "rules": [
                {
                    "validate": {
                        "message": message,
                        "failureAction": action,
                    }
                }
            ]
        },
    }


def _policyreport_item(resource: str, policy: str, message: str) -> dict:
    return {
        "metadata": {"name": f"{resource}-vl", "namespace": "production"},
        "spec": {
            "policy": policy,
            "resource": resource,
            "message": message,
            "result": "fail",
        },
    }


class TestPolicyDetector:
    def test_implements_policy_port(self) -> None:
        detector = PolicyDetector()
        assert isinstance(detector, PolicyPort)

    @patch("kubernetes.client.CustomObjectsApi")
    def test_detect_engine_kyverno(self, mock_api: MagicMock) -> None:
        mock_api.return_value.list_cluster_custom_object.return_value = {
            "items": [
                _kyverno_policy_item("require-pod-limits", "enforce", "Pods must have limits")
            ]
        }
        detector = PolicyDetector()
        result = detector.detect_engine()
        assert result.engine == PolicyEngine.KYVERNO
        assert result.total_policies == 1
        assert result.enforce_policies == 1

    @patch("kubernetes.client.CustomObjectsApi")
    def test_detect_engine_absent_degrades_to_none(self, mock_api: MagicMock) -> None:
        mock_api.return_value.list_cluster_custom_object.side_effect = Exception("not found")
        detector = PolicyDetector()
        result = detector.detect_engine()
        assert result.engine == PolicyEngine.NONE
        assert result.total_policies == 0

    @patch("kubernetes.client.CustomObjectsApi")
    def test_list_policies_returns_actions(self, mock_api: MagicMock) -> None:
        mock_api.return_value.list_cluster_custom_object.return_value = {
            "items": [
                _kyverno_policy_item("require-pod-limits", "enforce", "Pods must have limits"),
                _kyverno_policy_item(
                    "block-privileged-containers", "audit", "Privileged not allowed"
                ),
            ]
        }
        detector = PolicyDetector()
        policies = detector.list_policies()
        assert len(policies) == 2  # noqa: PLR2004
        assert policies[0].action == PolicyAction.ENFORCE
        assert policies[1].action == PolicyAction.AUDIT
        assert policies[0].ready is True

    @patch("kubernetes.client.CustomObjectsApi")
    def test_list_policies_absent_returns_empty(self, mock_api: MagicMock) -> None:
        mock_api.return_value.list_cluster_custom_object.side_effect = Exception("not found")
        detector = PolicyDetector()
        assert detector.list_policies() == []

    @patch("kubernetes.client.CustomObjectsApi")
    def test_list_violations(self, mock_api: MagicMock) -> None:
        mock_api.return_value.list_cluster_custom_object.return_value = {
            "items": [
                _policyreport_item(
                    "checkout-service-abc123",
                    "require-pod-limits",
                    "Pod missing resource limits",
                )
            ]
        }
        detector = PolicyDetector()
        violations = detector.list_violations()
        assert len(violations) == 1
        assert violations[0].policy_name == "require-pod-limits"
        assert violations[0].resource_name == "checkout-service-abc123"

    @patch("kubernetes.client.CustomObjectsApi")
    def test_list_violations_absent_returns_empty(self, mock_api: MagicMock) -> None:
        mock_api.return_value.list_cluster_custom_object.side_effect = Exception("not found")
        detector = PolicyDetector()
        assert detector.list_violations() == []

    @patch("kubernetes.client.CustomObjectsApi")
    def test_get_policy_returns_matching(self, mock_api: MagicMock) -> None:
        mock_api.return_value.list_cluster_custom_object.return_value = {
            "items": [_kyverno_policy_item("require-pod-limits", "enforce", "limits")]
        }
        detector = PolicyDetector()
        p = detector.get_policy(name="require-pod-limits")
        assert p.name == "require-pod-limits"
        assert p.action == PolicyAction.ENFORCE

    @patch("kubernetes.client.CustomObjectsApi")
    def test_explain_denial_finds_violation(self, mock_api: MagicMock) -> None:
        mock_api.return_value.list_cluster_custom_object.return_value = {
            "items": [
                _policyreport_item(
                    "checkout-service-abc123", "require-pod-limits", "missing limits"
                )
            ]
        }
        detector = PolicyDetector()
        exp = detector.explain_denial(
            resource_kind="Pod", resource_name="checkout-service-abc123", namespace="production"
        )
        assert exp.policy_name == "require-pod-limits"
        assert "limits" in exp.fix_suggestion

    @patch("kubernetes.client.CustomObjectsApi")
    def test_audit_returns_aggregate(self, mock_api: MagicMock) -> None:
        mock_api.return_value.list_cluster_custom_object.side_effect = [
            {"items": [_kyverno_policy_item("p1", "enforce", "m")]},  # policies
            {"items": []},  # policyreports
        ]
        detector = PolicyDetector()
        audit = detector.audit()
        assert audit["total_policies"] == 1
        assert audit["total_violations"] == 0

    @patch("kubernetes.client.CustomObjectsApi")
    def test_forbidden_raises_permission_error(self, mock_api: MagicMock) -> None:
        exc = Exception("forbidden")
        exc.status = 403  # type: ignore[attr-defined]
        mock_api.return_value.list_cluster_custom_object.side_effect = exc
        detector = PolicyDetector()
        with pytest.raises(InsufficientPermissionsError):
            detector.list_policies()
