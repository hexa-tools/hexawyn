from hexawyn.application.ports.driven.unauthorized_access_port import UnauthorizedAccessPort
from hexawyn.application.use_case.report_unauthorized_access.command import (
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.use_case.report_unauthorized_access.response import (
    ReportUnauthorizedAccessResponse,
)
from hexawyn.domain.services.unauthorized_access.unauthorized_access_service import (
    compute_unauthorized_access_report,
)


class ReportUnauthorizedAccessUseCase:
    def __init__(self, access_port: UnauthorizedAccessPort) -> None:
        self._port = access_port

    def execute(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, has_data=True, period="Dernieres 30 minutes"
        )
        return ReportUnauthorizedAccessResponse(result=result)
