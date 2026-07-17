"""Unit tests for CompareServiceCostUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.compare_service_cost.compare_service_cost_service_port import (
    CompareServiceCostServicePort,
)
from hexawyn.application.use_case.compare_service_cost.compare_service_cost_use_case import (
    CompareServiceCostUseCase,
)


class TestCompareServiceCostUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CompareServiceCostServicePort)
        use_case = CompareServiceCostUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compare.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CompareServiceCostServicePort)
        mock_service.compare.side_effect = RuntimeError("test error")
        use_case = CompareServiceCostUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
