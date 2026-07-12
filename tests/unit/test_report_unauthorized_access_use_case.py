from unittest.mock import MagicMock

from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_command import (  # noqa: E501
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_response import (  # noqa: E501
    ReportUnauthorizedAccessResponse,
)
from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_service_port import (  # noqa: E501
    ReportUnauthorizedAccessServicePort,
)
from hexawyn.domain.models.unauthorized_access import UnauthorizedAccessReport


class TestReportUnauthorizedAccessUseCase:
    def test_delegates(self) -> None:
        from hexawyn.application.use_case.report_unauthorized_access.report_unauthorized_access_use_case import (  # noqa: E501
            ReportUnauthorizedAccessUseCase,
        )

        service = MagicMock(spec=ReportUnauthorizedAccessServicePort)
        expected = ReportUnauthorizedAccessResponse(
            result=UnauthorizedAccessReport(period_label="30 min")
        )
        service.report.return_value = expected
        use_case = ReportUnauthorizedAccessUseCase(service=service)

        response = use_case.execute(ReportUnauthorizedAccessCommand())
        assert response is expected
