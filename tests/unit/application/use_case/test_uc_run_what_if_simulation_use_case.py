"""Unit tests for RunWhatIfSimulationUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_service_port import (
    RunWhatIfSimulationServicePort,
)
from hexawyn.application.use_case.run_what_if_simulation.run_what_if_simulation_use_case import (
    RunWhatIfSimulationUseCase,
)


class TestRunWhatIfSimulationUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=RunWhatIfSimulationServicePort)
        use_case = RunWhatIfSimulationUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.simulate.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=RunWhatIfSimulationServicePort)
        mock_service.simulate.side_effect = RuntimeError("test error")
        use_case = RunWhatIfSimulationUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
