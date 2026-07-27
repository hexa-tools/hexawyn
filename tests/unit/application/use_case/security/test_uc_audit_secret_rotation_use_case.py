from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.audit_secret_rotation.audit_secret_rotation_use_case import (  # noqa: E501
    AuditSecretRotationUseCase,
)
from hexawyn.application.use_case.security.audit_secret_rotation.command import (
    AuditSecretRotationCommand,
)
from hexawyn.application.use_case.security.audit_secret_rotation.response import (  # noqa: E501
    AuditSecretRotationResponse,
)


def _secret_raw(name: str, namespace: str = "default") -> dict[str, object]:
    return {
        "name": name,
        "namespace": namespace,
        "secret_type": "Opaque",
        "data_keys": ["password"],
        "managed_fields": [
            {
                "manager": "kubectl",
                "operation": "Update",
                "time": "2025-01-01T00:00:00Z",
                "fields_v1_raw": {},
            }
        ],
        "creation_timestamp": "2024-01-01T00:00:00Z",
        "annotations": {},
    }


class TestAuditSecretRotationUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_secrets.return_value = []
        port.list_secret_references.return_value = []
        port.get_namespace_rotation_exemptions.return_value = set()

        use_case = AuditSecretRotationUseCase(port=port)
        result = use_case.execute(AuditSecretRotationCommand())

        assert isinstance(result, AuditSecretRotationResponse)
        assert result.total_secrets_checked == 0

    def test_execute_detects_stale_secret(self) -> None:
        secret = _secret_raw("old-secret")
        port = MagicMock()
        port.list_secrets.return_value = [secret]
        port.list_secret_references.return_value = []
        port.get_namespace_rotation_exemptions.return_value = set()

        use_case = AuditSecretRotationUseCase(port=port)
        result = use_case.execute(AuditSecretRotationCommand(rotation_threshold_days=30))

        assert result.total_secrets_checked == 1

    def test_execute_excludes_exempt_namespaces(self) -> None:
        secret = _secret_raw("exempt-secret", namespace="kube-system")
        port = MagicMock()
        port.list_secrets.return_value = [secret]
        port.list_secret_references.return_value = []
        port.get_namespace_rotation_exemptions.return_value = {"kube-system"}

        use_case = AuditSecretRotationUseCase(port=port)
        result = use_case.execute(AuditSecretRotationCommand())

        assert result.total_secrets_checked == 1
        assert len(result.findings) == 0
