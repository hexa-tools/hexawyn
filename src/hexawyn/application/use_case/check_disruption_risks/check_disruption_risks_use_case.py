from __future__ import annotations

from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_command import (  # noqa: E501
    CheckDisruptionRisksCommand,
)
from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_response import (  # noqa: E501
    CheckDisruptionRisksResponse,
)
from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_service_port import (  # noqa: E501
    CheckDisruptionRisksServicePort,
)


class CheckDisruptionRisksUseCase:
    def __init__(self, service: CheckDisruptionRisksServicePort) -> None:
        self._service = service

    def execute(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse:
        return self._service.check(command)
