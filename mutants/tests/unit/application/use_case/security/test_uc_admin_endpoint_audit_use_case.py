from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.admin_endpoint_audit.admin_endpoint_audit_use_case import (  # noqa: E501
    AdminEndpointAuditUseCase,
)
from hexawyn.application.use_case.security.admin_endpoint_audit.command import (  # noqa: E501
    AdminEndpointAuditCommand,
)
from hexawyn.application.use_case.security.admin_endpoint_audit.response import (  # noqa: E501
    AdminEndpointAuditResponse,
)


class TestAdminEndpointAuditUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_failed_admin_calls.return_value = []
        port.fetch_total_requests.return_value = 100

        use_case = AdminEndpointAuditUseCase(port=port)
        result = use_case.execute(AdminEndpointAuditCommand())

        assert isinstance(result, AdminEndpointAuditResponse)
        assert result.total_requests == 100  # noqa: PLR2004

    def test_execute_passes_command_params(self) -> None:
        port = MagicMock()
        port.fetch_failed_admin_calls.return_value = []
        port.fetch_total_requests.return_value = 0

        use_case = AdminEndpointAuditUseCase(port=port)
        result = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern="/api/admin",
                time_window_minutes=60,
                flag_threshold=10,
            )
        )

        assert result.endpoint_pattern == "/api/admin"

    def test_execute_with_zero_total_requests(self) -> None:
        port = MagicMock()
        port.fetch_failed_admin_calls.return_value = []
        port.fetch_total_requests.return_value = 0

        use_case = AdminEndpointAuditUseCase(port=port)
        result = use_case.execute(AdminEndpointAuditCommand())

        assert result.total_requests == 0
        assert result.rate_403_pct == 0.0
