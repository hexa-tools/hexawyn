from unittest.mock import MagicMock

from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_command import (  # noqa: E501
    ReportStaleCredentialsCommand,
)
from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_response import (  # noqa: E501
    ReportStaleCredentialsResponse,
)
from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_service_port import (  # noqa: E501
    ReportStaleCredentialsServicePort,
)
from hexawyn.domain.models.stale_credentials import StaleCredentialsReport


class TestReportStaleCredentialsUseCase:
    def test_delegates(self) -> None:
        from hexawyn.application.use_case.report_stale_credentials.report_stale_credentials_use_case import (  # noqa: E501
            ReportStaleCredentialsUseCase,
        )

        service = MagicMock(spec=ReportStaleCredentialsServicePort)
        expected = ReportStaleCredentialsResponse(
            result=StaleCredentialsReport(period_label="Rotation")
        )
        service.report.return_value = expected
        use_case = ReportStaleCredentialsUseCase(service=service)

        response = use_case.execute(ReportStaleCredentialsCommand())
        assert response is expected
