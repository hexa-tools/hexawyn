from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.sensitive_data_audit.command import (  # noqa: E501
    SensitiveDataAuditCommand,
)
from hexawyn.application.use_case.security.sensitive_data_audit.response import (  # noqa: E501
    SensitiveDataAuditResponse,
)
from hexawyn.application.use_case.security.sensitive_data_audit.sensitive_data_audit_use_case import (  # noqa: E501
    SensitiveDataAuditUseCase,
)


class TestSensitiveDataAuditUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_access_matches.return_value = []

        use_case = SensitiveDataAuditUseCase(port=port)
        result = use_case.execute(SensitiveDataAuditCommand())

        assert isinstance(result, SensitiveDataAuditResponse)

    def test_execute_passes_command_params(self) -> None:
        port = MagicMock()
        port.fetch_access_matches.return_value = []

        use_case = SensitiveDataAuditUseCase(port=port)
        result = use_case.execute(
            SensitiveDataAuditCommand(
                pattern="/api/secrets",
                time_window_minutes=15,
                allowlist=["trusted-service"],
            )
        )

        assert result.pattern == "/api/secrets"
        assert result.total_matches == 0
