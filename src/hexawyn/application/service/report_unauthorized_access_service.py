from __future__ import annotations

from hexawyn.application.ports.driven.unauthorized_access_port import UnauthorizedAccessPort
from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_command import (  # noqa: E501
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_response import (  # noqa: E501
    ReportUnauthorizedAccessResponse,
)
from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_service_port import (  # noqa: E501
    ReportUnauthorizedAccessServicePort,
)
from hexawyn.domain.services.unauthorized_access.unauthorized_access_service import (
    compute_unauthorized_access_report,
)


class ReportUnauthorizedAccessService(ReportUnauthorizedAccessServicePort):
    def __init__(self, access_port: UnauthorizedAccessPort) -> None:
        self._port = access_port

    def report(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, has_data=True, period="Dernieres 30 minutes"
        )
        return ReportUnauthorizedAccessResponse(result=result)
