"""Unit tests for CanaryComparisonUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.canary_comparison.canary_comparison_service_port import (
    CanaryComparisonServicePort,
)
from hexawyn.application.use_case.canary_comparison.canary_comparison_use_case import (
    CanaryComparisonUseCase,
)


class TestCanaryComparisonUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CanaryComparisonServicePort)
        use_case = CanaryComparisonUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compare.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CanaryComparisonServicePort)
        mock_service.compare.side_effect = RuntimeError("test error")
        use_case = CanaryComparisonUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
