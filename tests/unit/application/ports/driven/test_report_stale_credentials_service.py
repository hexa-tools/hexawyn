from unittest.mock import MagicMock

from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialsPort
from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_command import (  # noqa: E501
    ReportStaleCredentialsCommand,
)


class TestReportStaleCredentialsService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_service_port import (  # noqa: E501
            ReportStaleCredentialsServicePort,
        )
        from hexawyn.application.service.report_stale_credentials_service import (
            ReportStaleCredentialsService,
        )

        service = ReportStaleCredentialsService(
            credentials_port=MagicMock(spec=StaleCredentialsPort)
        )
        assert isinstance(service, ReportStaleCredentialsServicePort)

    def test_report_returns_result(self) -> None:
        from hexawyn.application.service.report_stale_credentials_service import (
            ReportStaleCredentialsService,
        )

        port = MagicMock(spec=StaleCredentialsPort)
        port.get_stale_credentials.return_value = []
        service = ReportStaleCredentialsService(credentials_port=port)

        response = service.report(ReportStaleCredentialsCommand())
        assert response.result.total_stale == 0
