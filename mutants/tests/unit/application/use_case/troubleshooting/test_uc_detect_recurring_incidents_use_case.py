from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.detect_recurring_incidents.command import (  # noqa: E501
    DetectRecurringIncidentsCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_recurring_incidents.detect_recurring_incidents_use_case import (  # noqa: E501
    DetectRecurringIncidentsUseCase,
)
from hexawyn.application.use_case.troubleshooting.detect_recurring_incidents.response import (  # noqa: E501
    DetectRecurringIncidentsResponse,
)


class TestDetectRecurringIncidentsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_incidents.return_value = []

        use_case = DetectRecurringIncidentsUseCase(
            incident_port=port,
        )
        result = use_case.execute(DetectRecurringIncidentsCommand())

        assert isinstance(result, DetectRecurringIncidentsResponse)

    def test_execute_passes_window_days_to_port(self) -> None:
        port = MagicMock()
        port.fetch_incidents.return_value = []

        use_case = DetectRecurringIncidentsUseCase(
            incident_port=port,
        )
        use_case.execute(DetectRecurringIncidentsCommand(window_days=7))

        port.fetch_incidents.assert_called_once_with(7)
