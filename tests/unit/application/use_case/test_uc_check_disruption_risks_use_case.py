"""Unit tests for CheckDisruptionRisksUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_service_port import (
    CheckDisruptionRisksServicePort,
)
from hexawyn.application.use_case.check_disruption_risks.check_disruption_risks_use_case import (
    CheckDisruptionRisksUseCase,
)


class TestCheckDisruptionRisksUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CheckDisruptionRisksServicePort)
        use_case = CheckDisruptionRisksUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.check.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CheckDisruptionRisksServicePort)
        mock_service.check.side_effect = RuntimeError("test error")
        use_case = CheckDisruptionRisksUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
