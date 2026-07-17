"""Unit tests for ReportStaleCredentialsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_service_port import (
    ReportStaleCredentialsServicePort,
)
from hexawyn.application.use_case.report_stale_credentials.report_stale_credentials_use_case import (
    ReportStaleCredentialsUseCase,
)


class TestReportStaleCredentialsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ReportStaleCredentialsServicePort)
        use_case = ReportStaleCredentialsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.report.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ReportStaleCredentialsServicePort)
        mock_service.report.side_effect = RuntimeError("test error")
        use_case = ReportStaleCredentialsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
