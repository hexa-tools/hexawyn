"""Unit tests for ComputeMTTRTrendUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.compute_mttr_trend.compute_mttr_trend_service_port import (
    ComputeMTTRTrendServicePort,
)
from hexawyn.application.use_case.compute_mttr_trend.compute_mttr_trend_use_case import (
    ComputeMTTRTrendUseCase,
)


class TestComputeMTTRTrendUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ComputeMTTRTrendServicePort)
        use_case = ComputeMTTRTrendUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compute.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ComputeMTTRTrendServicePort)
        mock_service.compute.side_effect = RuntimeError("test error")
        use_case = ComputeMTTRTrendUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
