from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_command import (
    GetNamespaceEventsCommand,
)
from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_response import (
    GetNamespaceEventsResponse,
)
from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_service_port import (
    GetNamespaceEventsServicePort,
)
from hexawyn.application.use_case.get_namespace_events.get_namespace_events_use_case import (
    GetNamespaceEventsUseCase,
)


class TestGetNamespaceEventsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=GetNamespaceEventsServicePort)
        expected = GetNamespaceEventsResponse(namespace="production")
        service.get_events.return_value = expected
        use_case = GetNamespaceEventsUseCase(service=service)
        command = GetNamespaceEventsCommand(namespace="production")

        result = use_case.execute(command)

        service.get_events.assert_called_once_with(command)
        assert result is expected
