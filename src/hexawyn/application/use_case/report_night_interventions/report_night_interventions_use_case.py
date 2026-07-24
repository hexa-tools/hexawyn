from hexawyn.application.ports.driven.engineer_workload_port import EngineerWorkloadPort
from hexawyn.application.use_case.report_night_interventions.command import (
    ReportNightInterventionsCommand,
)
from hexawyn.application.use_case.report_night_interventions.response import (
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
        result = compute_night_intervention_report(months[split:], months[:split], period="Ce mois")
        return ReportNightInterventionsResponse(result=result)
