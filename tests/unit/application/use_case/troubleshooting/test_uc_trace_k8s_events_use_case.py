from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.trace_k8s_events.command import (
    TraceK8sEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.trace_k8s_events.response import (  # noqa: E501
    TraceK8sEventsResponse,
)
from hexawyn.application.use_case.troubleshooting.trace_k8s_events.trace_k8s_events_use_case import (  # noqa: E501
    TraceK8sEventsUseCase,
)


class TestTraceK8sEventsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_trace_spans.return_value = []

        use_case = TraceK8sEventsUseCase(port=port)
        result = use_case.execute(TraceK8sEventsCommand(trace_id="abc123"))

        assert isinstance(result, TraceK8sEventsResponse)
