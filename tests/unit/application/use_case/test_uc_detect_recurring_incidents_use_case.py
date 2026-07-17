"""Unit tests for DetectRecurringIncidentsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_recurring_incidents.detect_recurring_incidents_service_port import (
    DetectRecurringIncidentsServicePort,
)
from hexawyn.application.use_case.detect_recurring_incidents.detect_recurring_incidents_use_case import (
    DetectRecurringIncidentsUseCase,
)


class TestDetectRecurringIncidentsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DetectRecurringIncidentsServicePort)
        use_case = DetectRecurringIncidentsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DetectRecurringIncidentsServicePort)
        mock_service.detect.side_effect = RuntimeError("test error")
        use_case = DetectRecurringIncidentsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
