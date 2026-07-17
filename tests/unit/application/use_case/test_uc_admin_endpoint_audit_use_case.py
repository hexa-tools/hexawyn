"""Unit tests for AdminEndpointAuditUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.admin_endpoint_audit.admin_endpoint_audit_service_port import (
    AdminEndpointAuditServicePort,
)
from hexawyn.application.use_case.admin_endpoint_audit.admin_endpoint_audit_use_case import (
    AdminEndpointAuditUseCase,
)


class TestAdminEndpointAuditUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=AdminEndpointAuditServicePort)
        use_case = AdminEndpointAuditUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.audit.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=AdminEndpointAuditServicePort)
        mock_service.audit.side_effect = RuntimeError("test error")
        use_case = AdminEndpointAuditUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
