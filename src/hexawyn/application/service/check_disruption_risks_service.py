from __future__ import annotations

from hexawyn.application.ports.driven.disruption_risk_port import DisruptionRiskPort
from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_command import (  # noqa: E501
    CheckDisruptionRisksCommand,
)
from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_response import (  # noqa: E501
    CheckDisruptionRisksResponse,
)
from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_service_port import (  # noqa: E501
    CheckDisruptionRisksServicePort,
)
from hexawyn.domain.services.disruption_risk.disruption_risk_service import (
    compute_disruption_risks,
)


class CheckDisruptionRisksService(CheckDisruptionRisksServicePort):
    def __init__(self, disruption_risk_port: DisruptionRiskPort) -> None:
        self._port = disruption_risk_port

    def check(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        raw = self._port.get_disruption_risks(command.warning_days)
        has_data = bool(raw)
        result = compute_disruption_risks(raw, period="Semaine en cours", has_data=has_data)
        return CheckDisruptionRisksResponse(result=result)
