from __future__ import annotations

from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_command import (  # noqa: E501
    ReportNightInterventionsCommand,
)
from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_response import (  # noqa: E501
    ReportNightInterventionsResponse,
)
from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_service_port import (  # noqa: E501
    ReportNightInterventionsServicePort,
)


class ReportNightInterventionsUseCase:
    def __init__(self, service: ReportNightInterventionsServicePort) -> None:
        self._service = service

    def execute(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        return self._service.report(command)
