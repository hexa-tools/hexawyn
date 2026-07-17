"""Unit tests for CostProfilingUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.cost_profiling.cost_profiling_service_port import (
    CostProfilingServicePort,
)
from hexawyn.application.use_case.cost_profiling.cost_profiling_use_case import CostProfilingUseCase


class TestCostProfilingUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CostProfilingServicePort)
        use_case = CostProfilingUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.profile.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CostProfilingServicePort)
        mock_service.profile.side_effect = RuntimeError("test error")
        use_case = CostProfilingUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
