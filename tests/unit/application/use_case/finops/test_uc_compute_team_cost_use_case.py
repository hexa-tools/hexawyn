from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.compute_team_cost.command import (
    ComputeTeamCostCommand,
)
from hexawyn.application.use_case.finops.compute_team_cost.compute_team_cost_use_case import (  # noqa: E501
    ComputeTeamCostUseCase,
)
from hexawyn.application.use_case.finops.compute_team_cost.response import (
    ComputeTeamCostResponse,
)


class TestComputeTeamCostUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_namespace_resources.return_value = []

        use_case = ComputeTeamCostUseCase(cost_port=port)
        result = use_case.execute(ComputeTeamCostCommand())

        assert isinstance(result, ComputeTeamCostResponse)

    def test_execute_with_custom_pricing(self) -> None:
        port = MagicMock()
        port.fetch_namespace_resources.return_value = []

        use_case = ComputeTeamCostUseCase(cost_port=port)
        result = use_case.execute(ComputeTeamCostCommand(cpu_price_per_core_hour=0.05))

        assert isinstance(result, ComputeTeamCostResponse)
