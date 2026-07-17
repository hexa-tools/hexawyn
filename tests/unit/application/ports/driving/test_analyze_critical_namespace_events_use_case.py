from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_command import (
    AnalyzeCriticalNamespaceEventsCommand,
)
from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_response import (
    AnalyzeCriticalNamespaceEventsResponse,
)
from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_service_port import (
    AnalyzeCriticalNamespaceEventsServicePort,
)
from hexawyn.application.use_case.analyze_critical_namespace_events.analyze_critical_namespace_events_use_case import (
    AnalyzeCriticalNamespaceEventsUseCase,
)


class TestAnalyzeCriticalNamespaceEventsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=AnalyzeCriticalNamespaceEventsServicePort)
        expected = AnalyzeCriticalNamespaceEventsResponse(namespace="staging")
        service.analyze.return_value = expected
        use_case = AnalyzeCriticalNamespaceEventsUseCase(service=service)
        command = AnalyzeCriticalNamespaceEventsCommand(namespace="staging")

        result = use_case.execute(command)

        service.analyze.assert_called_once_with(command)
        assert result is expected
