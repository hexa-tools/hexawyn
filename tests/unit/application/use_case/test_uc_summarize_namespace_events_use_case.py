"""Unit tests for SummarizeNamespaceEventsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_service_port import (
    SummarizeNamespaceEventsServicePort,
)
from hexawyn.application.use_case.summarize_namespace_events.summarize_namespace_events_use_case import (
    SummarizeNamespaceEventsUseCase,
)


class TestSummarizeNamespaceEventsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=SummarizeNamespaceEventsServicePort)
        use_case = SummarizeNamespaceEventsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.summarize.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=SummarizeNamespaceEventsServicePort)
        mock_service.summarize.side_effect = RuntimeError("test error")
        use_case = SummarizeNamespaceEventsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
