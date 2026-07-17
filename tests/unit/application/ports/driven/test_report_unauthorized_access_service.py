from unittest.mock import MagicMock

from hexawyn.application.ports.driven.unauthorized_access_port import UnauthorizedAccessPort
from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_command import (  # noqa: E501
    ReportUnauthorizedAccessCommand,
)


class TestReportUnauthorizedAccessService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_service_port import (  # noqa: E501
            ReportUnauthorizedAccessServicePort,
        )
        from hexawyn.application.service.report_unauthorized_access_service import (
            ReportUnauthorizedAccessService,
        )

        service = ReportUnauthorizedAccessService(
            access_port=MagicMock(spec=UnauthorizedAccessPort)
        )
        assert isinstance(service, ReportUnauthorizedAccessServicePort)

    def test_report_returns_result(self) -> None:
        from hexawyn.application.service.report_unauthorized_access_service import (
            ReportUnauthorizedAccessService,
        )

        port = MagicMock(spec=UnauthorizedAccessPort)
        port.get_unauthorized_access_data.return_value = {
            "attempt_count": 0,
            "window_minutes": 30,
            "source_type": "unknown",
        }
        service = ReportUnauthorizedAccessService(access_port=port)

        response = service.report(ReportUnauthorizedAccessCommand())
        assert response.result.attempt_count == 0
