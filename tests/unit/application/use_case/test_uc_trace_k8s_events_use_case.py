"""Unit tests for TraceK8sEventsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.trace_k8s_events.trace_k8s_events_service_port import (
    TraceK8sEventsServicePort,
)
from hexawyn.application.use_case.trace_k8s_events.trace_k8s_events_use_case import (
    TraceK8sEventsUseCase,
)


class TestTraceK8sEventsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=TraceK8sEventsServicePort)
        use_case = TraceK8sEventsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.correlate.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=TraceK8sEventsServicePort)
        mock_service.correlate.side_effect = RuntimeError("test error")
        use_case = TraceK8sEventsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
