from __future__ import annotations

from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
    KubernetesAuditLogAdapter,
    _parse_audit_line,
)
from hexawyn.application.ports.driven.gitops_drift_audit_port import (
    GitOpsDriftAuditPort,
)


class TestKubernetesAuditLogAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesAuditLogAdapter(), GitOpsDriftAuditPort)


class TestParseAuditLineForDrift:
    def test_valid_configmap_event(self) -> None:
        import json

        line = json.dumps(
            {
                "user": {"username": "admin"},
                "objectRef": {"resource": "configmaps", "namespace": "default", "name": "my-cm"},
                "verb": "patch",
                "requestReceivedTimestamp": "2024-01-01T00:00:00Z",
            }
        )
        result = _parse_audit_line(line, "default")
        assert result is not None
        assert result["kind"] == "ConfigMap"
        assert result["name"] == "my-cm"
        assert result["actor"] == "admin"
        assert result["verb"] == "patch"

    def test_different_namespace_returns_none(self) -> None:
        import json

        line = json.dumps(
            {
                "user": {"username": "admin"},
                "objectRef": {"resource": "configmaps", "namespace": "other", "name": "my-cm"},
                "verb": "patch",
                "requestReceivedTimestamp": "2024-01-01T00:00:00Z",
            }
        )
        assert _parse_audit_line(line, "default") is None

    def test_unknown_resource_returns_none(self) -> None:
        import json

        line = json.dumps(
            {
                "user": {"username": "admin"},
                "objectRef": {"resource": "unknown", "namespace": "default", "name": "x"},
                "verb": "get",
                "requestReceivedTimestamp": "2024-01-01T00:00:00Z",
            }
        )
        assert _parse_audit_line(line, "default") is None

    def test_invalid_json_returns_none(self) -> None:
        assert _parse_audit_line("bad json", "default") is None
