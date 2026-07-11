from __future__ import annotations

from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_command import (  # noqa: E501
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_response import (  # noqa: E501
    ReportUnauthorizedAccessResponse,
)
from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_service_port import (  # noqa: E501
    ReportUnauthorizedAccessServicePort,
)


class ReportUnauthorizedAccessUseCase:
    def __init__(self, service: ReportUnauthorizedAccessServicePort) -> None:
        self._service = service

    def execute(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        return self._service.report(command)
