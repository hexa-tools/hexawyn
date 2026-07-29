from __future__ import annotations

from hexawyn.application.ports.driven.engineer_workload_port import EngineerWorkloadPort
from hexawyn.application.use_case.workloads.report_night_interventions.command import (  # noqa: E501
    ReportNightInterventionsCommand,
)
from hexawyn.application.use_case.workloads.report_night_interventions.response import (  # noqa: E501
    ReportNightInterventionsResponse,
)
from hexawyn.domain.services.engineer_workload.night_intervention_service import (
    compute_night_intervention_report,
)


class ReportNightInterventionsUseCase:
    def __init__(self, workload_port: EngineerWorkloadPort) -> None:
        self._port = workload_port

    def execute(self, command: ReportNightInterventionsCommand) -> ReportNightInterventionsResponse:
        months = self._port.get_night_intervention_data(command.history_months)
        split = max(len(months) // 2, 1)
        previous = months[:split]
        current = months[split:]
        result = compute_night_intervention_report(current, previous, period="Ce mois")
        return ReportNightInterventionsResponse(result=result)
