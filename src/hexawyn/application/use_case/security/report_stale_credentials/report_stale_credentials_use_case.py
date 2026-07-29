from __future__ import annotations

from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialsPort
from hexawyn.application.use_case.security.report_stale_credentials.command import (  # noqa: E501
    ReportStaleCredentialsCommand,
)
from hexawyn.application.use_case.security.report_stale_credentials.response import (  # noqa: E501
    ReportStaleCredentialsResponse,
)
from hexawyn.domain.services.stale_credentials.stale_credentials_service import (
    compute_stale_credentials_report,
)


class ReportStaleCredentialsUseCase:
    def __init__(self, credentials_port: StaleCredentialsPort) -> None:
        self._port = credentials_port

    def execute(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)
