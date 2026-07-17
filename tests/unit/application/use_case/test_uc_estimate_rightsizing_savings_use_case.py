"""Unit tests for EstimateRightsizingSavingsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_service_port import (
    EstimateRightsizingSavingsServicePort,
)
from hexawyn.application.use_case.estimate_rightsizing_savings.estimate_rightsizing_savings_use_case import (
    EstimateRightsizingSavingsUseCase,
)


class TestEstimateRightsizingSavingsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=EstimateRightsizingSavingsServicePort)
        use_case = EstimateRightsizingSavingsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.estimate_rightsizing_savings.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=EstimateRightsizingSavingsServicePort)
        mock_service.estimate_rightsizing_savings.side_effect = RuntimeError("test error")
        use_case = EstimateRightsizingSavingsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
