from __future__ import annotations

from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialsPort
from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_command import (  # noqa: E501
    ReportStaleCredentialsCommand,
)
from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_response import (  # noqa: E501
    ReportStaleCredentialsResponse,
)
from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_service_port import (  # noqa: E501
    ReportStaleCredentialsServicePort,
)
from hexawyn.domain.services.stale_credentials.stale_credentials_service import (
    compute_stale_credentials_report,
)


class ReportStaleCredentialsService(ReportStaleCredentialsServicePort):
    def __init__(self, credentials_port: StaleCredentialsPort) -> None:
        self._port = credentials_port

    def report(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)
