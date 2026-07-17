"""Unit tests for EstimateCostSavingUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.estimate_cost_saving.estimate_cost_saving_service_port import (
    EstimateCostSavingServicePort,
)
from hexawyn.application.use_case.estimate_cost_saving.estimate_cost_saving_use_case import (
    EstimateCostSavingUseCase,
)


class TestEstimateCostSavingUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=EstimateCostSavingServicePort)
        use_case = EstimateCostSavingUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.estimate_cost_saving.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=EstimateCostSavingServicePort)
        mock_service.estimate_cost_saving.side_effect = RuntimeError("test error")
        use_case = EstimateCostSavingUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
