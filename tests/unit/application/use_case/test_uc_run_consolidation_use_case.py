"""Unit tests for RunConsolidationUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.run_consolidation.run_consolidation_service_port import (
    RunConsolidationServicePort,
)
from hexawyn.application.use_case.run_consolidation.run_consolidation_use_case import (
    RunConsolidationUseCase,
)


class TestRunConsolidationUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=RunConsolidationServicePort)
        use_case = RunConsolidationUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.execute.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=RunConsolidationServicePort)
        mock_service.execute.side_effect = RuntimeError("test error")
        use_case = RunConsolidationUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
