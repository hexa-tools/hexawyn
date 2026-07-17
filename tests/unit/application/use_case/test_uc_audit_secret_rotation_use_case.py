"""Unit tests for AuditSecretRotationUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_service_port import (
    AuditSecretRotationServicePort,
)
from hexawyn.application.use_case.audit_secret_rotation.audit_secret_rotation_use_case import (
    AuditSecretRotationUseCase,
)


class TestAuditSecretRotationUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=AuditSecretRotationServicePort)
        use_case = AuditSecretRotationUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.audit_secret_rotation.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=AuditSecretRotationServicePort)
        mock_service.audit_secret_rotation.side_effect = RuntimeError("test error")
        use_case = AuditSecretRotationUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
