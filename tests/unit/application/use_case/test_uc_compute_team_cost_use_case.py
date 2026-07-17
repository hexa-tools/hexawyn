"""Unit tests for ComputeTeamCostUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.compute_team_cost.compute_team_cost_service_port import (
    ComputeTeamCostServicePort,
)
from hexawyn.application.use_case.compute_team_cost.compute_team_cost_use_case import (
    ComputeTeamCostUseCase,
)


class TestComputeTeamCostUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ComputeTeamCostServicePort)
        use_case = ComputeTeamCostUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compute.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ComputeTeamCostServicePort)
        mock_service.compute.side_effect = RuntimeError("test error")
        use_case = ComputeTeamCostUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
