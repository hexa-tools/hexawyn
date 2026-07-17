"""Unit tests for ReportUnauthorizedAccessUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_service_port import (
    ReportUnauthorizedAccessServicePort,
)
from hexawyn.application.use_case.report_unauthorized_access.report_unauthorized_access_use_case import (
    ReportUnauthorizedAccessUseCase,
)


class TestReportUnauthorizedAccessUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ReportUnauthorizedAccessServicePort)
        use_case = ReportUnauthorizedAccessUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.report.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ReportUnauthorizedAccessServicePort)
        mock_service.report.side_effect = RuntimeError("test error")
        use_case = ReportUnauthorizedAccessUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
