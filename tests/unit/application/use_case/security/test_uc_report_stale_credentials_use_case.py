from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.report_stale_credentials.command import (  # noqa: E501
    ReportStaleCredentialsCommand,
)
from hexawyn.application.use_case.security.report_stale_credentials.report_stale_credentials_use_case import (  # noqa: E501
    ReportStaleCredentialsUseCase,
)
from hexawyn.application.use_case.security.report_stale_credentials.response import (  # noqa: E501
    ReportStaleCredentialsResponse,
)


class TestReportStaleCredentialsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_stale_credentials.return_value = []

        use_case = ReportStaleCredentialsUseCase(credentials_port=port)
        result = use_case.execute(ReportStaleCredentialsCommand())

        assert isinstance(result, ReportStaleCredentialsResponse)

    def test_execute_passes_min_days_to_port(self) -> None:
        port = MagicMock()
        port.get_stale_credentials.return_value = []

        use_case = ReportStaleCredentialsUseCase(credentials_port=port)
        use_case.execute(ReportStaleCredentialsCommand(min_days=30))

        port.get_stale_credentials.assert_called_once_with(30)

    def test_execute_with_data_returns_report(self) -> None:
        port = MagicMock()
        port.get_stale_credentials.return_value = [
            {"name": "old-secret", "days_unrotated": 120, "risk_level": "high"}
        ]

        use_case = ReportStaleCredentialsUseCase(credentials_port=port)
        result = use_case.execute(ReportStaleCredentialsCommand())

        assert result.result is not None

    def test_execute_with_no_credentials(self) -> None:
        port = MagicMock()
        port.get_stale_credentials.return_value = []

        use_case = ReportStaleCredentialsUseCase(credentials_port=port)
        result = use_case.execute(ReportStaleCredentialsCommand(min_days=0))

        assert isinstance(result, ReportStaleCredentialsResponse)
