from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.team_cost import TeamCostReport


@dataclass
class ComputeTeamCostResponse:
    result: TeamCostReport
