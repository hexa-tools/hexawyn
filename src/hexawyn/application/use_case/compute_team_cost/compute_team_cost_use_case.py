from __future__ import annotations

from hexawyn.application.ports.driving.compute_team_cost.compute_team_cost_command import (
    ComputeTeamCostCommand,
)
from hexawyn.application.ports.driving.compute_team_cost.compute_team_cost_response import (
    ComputeTeamCostResponse,
)
from hexawyn.application.ports.driving.compute_team_cost.compute_team_cost_service_port import (
    ComputeTeamCostServicePort,
)


class ComputeTeamCostUseCase:
    def __init__(self, service: ComputeTeamCostServicePort) -> None:
        self._service = service

    def execute(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        return self._service.compute(command)
