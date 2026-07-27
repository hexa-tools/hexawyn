from __future__ import annotations

from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
    KubernetesRBACAdapter,
    _parse_audit_line,
)
from hexawyn.application.ports.driven.rbac_security_audit_port import (
    RBACSecurityAuditPort,
)


class TestKubernetesRBACAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesRBACAdapter(), RBACSecurityAuditPort)


class TestParseAuditLine:
    def test_valid_service_account_event(self) -> None:
        import json

        line = json.dumps(
            {
                "user": {"username": "system:serviceaccount:default:my-sa"},
                "objectRef": {"resource": "pods"},
                "verb": "list",
                "requestReceivedTimestamp": "2024-01-01T00:00:00Z",
            }
        )
        result = _parse_audit_line(line)
        assert result is not None
        assert result["service_account"] == "my-sa"
        assert result["namespace"] == "default"
        assert result["verb"] == "list"
        assert result["resource"] == "pods"

    def test_invalid_json_returns_none(self) -> None:
        assert _parse_audit_line("not json") is None

    def test_non_dict_returns_none(self) -> None:
        import json

        assert _parse_audit_line(json.dumps(["array"])) is None

    def test_non_service_account_user_returns_none(self) -> None:
        import json

        line = json.dumps(
            {
                "user": {"username": "admin"},
                "objectRef": {"resource": "pods"},
                "verb": "list",
                "requestReceivedTimestamp": "2024-01-01T00:00:00Z",
            }
        )
        assert _parse_audit_line(line) is None

    def test_invalid_sa_format_returns_none(self) -> None:
        import json

        line = json.dumps(
            {
                "user": {"username": "system:serviceaccount:onlythree"},
                "objectRef": {"resource": "pods"},
                "verb": "list",
                "requestReceivedTimestamp": "2024-01-01T00:00:00Z",
            }
        )
        assert _parse_audit_line(line) is None

    def test_missing_fields_returns_none(self) -> None:
        import json

        line = json.dumps(
            {
                "user": {"username": "system:serviceaccount:default:my-sa"},
                "objectRef": {"resource": "pods"},
            }
        )
        assert _parse_audit_line(line) is None
