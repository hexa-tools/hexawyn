from __future__ import annotations

from hexawyn.application.ports.driven.engineer_workload_port import EngineerWorkloadPort
from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_command import (  # noqa: E501
    ReportNightInterventionsCommand,
)
from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_response import (  # noqa: E501
    ReportNightInterventionsResponse,
)
from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_service_port import (  # noqa: E501
    ReportNightInterventionsServicePort,
)
from hexawyn.domain.services.engineer_workload.night_intervention_service import (
    compute_night_intervention_report,
)


class ReportNightInterventionsService(ReportNightInterventionsServicePort):
    def __init__(self, workload_port: EngineerWorkloadPort) -> None:
        self._port = workload_port

    def report(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)
