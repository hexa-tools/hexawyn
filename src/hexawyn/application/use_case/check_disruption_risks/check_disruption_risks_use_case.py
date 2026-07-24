from hexawyn.application.ports.driven.disruption_risk_port import DisruptionRiskPort
from hexawyn.application.use_case.check_disruption_risks.command import CheckDisruptionRisksCommand
from hexawyn.application.use_case.check_disruption_risks.response import (
    CheckDisruptionRisksResponse,
)
from hexawyn.domain.services.disruption_risk.disruption_risk_service import compute_disruption_risks


class CheckDisruptionRisksUseCase:
    def __init__(self, disruption_risk_port: DisruptionRiskPort) -> None:
        self._port = disruption_risk_port

    def execute(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period="Semaine en cours", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)
