from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.report_unauthorized_access.command import (
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.use_case.security.report_unauthorized_access.report_unauthorized_access_use_case import (  # noqa: E501
    ReportUnauthorizedAccessUseCase,
)
from hexawyn.application.use_case.security.report_unauthorized_access.response import (
    ReportUnauthorizedAccessResponse,
)


class TestReportUnauthorizedAccessUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_unauthorized_access_data.return_value = {
            "attempt_count": 0,
            "window_minutes": 30,
            "source_type": "external",
        }

        use_case = ReportUnauthorizedAccessUseCase(access_port=port)
        result = use_case.execute(ReportUnauthorizedAccessCommand())

        assert isinstance(result, ReportUnauthorizedAccessResponse)

    def test_execute_with_access_data(self) -> None:
        port = MagicMock()
        port.get_unauthorized_access_data.return_value = {
            "attempt_count": 150,
            "window_minutes": 30,
            "source_type": "external",
        }

        use_case = ReportUnauthorizedAccessUseCase(access_port=port)
        result = use_case.execute(ReportUnauthorizedAccessCommand())

        assert isinstance(result, ReportUnauthorizedAccessResponse)
        assert result.result is not None
