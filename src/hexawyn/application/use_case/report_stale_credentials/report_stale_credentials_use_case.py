from __future__ import annotations

from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_command import (  # noqa: E501
    ReportStaleCredentialsCommand,
)
from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_response import (  # noqa: E501
    ReportStaleCredentialsResponse,
)
from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_service_port import (  # noqa: E501
    ReportStaleCredentialsServicePort,
)


class ReportStaleCredentialsUseCase:
    def __init__(self, service: ReportStaleCredentialsServicePort) -> None:
        self._service = service

    def execute(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        return self._service.report(command)
