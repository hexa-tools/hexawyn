from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_command import (
    SummarizeNamespaceEventsCommand,
)
from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_response import (
    SummarizeNamespaceEventsResponse,
)
from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_service_port import (
    SummarizeNamespaceEventsServicePort,
)
from hexawyn.application.use_case.summarize_namespace_events.summarize_namespace_events_use_case import (
    SummarizeNamespaceEventsUseCase,
)


class TestSummarizeNamespaceEventsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=SummarizeNamespaceEventsServicePort)
        expected = SummarizeNamespaceEventsResponse(namespace="staging")
        service.summarize.return_value = expected
        use_case = SummarizeNamespaceEventsUseCase(service=service)
        command = SummarizeNamespaceEventsCommand(namespace="staging")

        result = use_case.execute(command)

        service.summarize.assert_called_once_with(command)
        assert result is expected
