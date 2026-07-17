"""Unit tests for AnalyzeCriticalNamespaceEventsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_service_port import (
    AnalyzeCriticalNamespaceEventsServicePort,
)
from hexawyn.application.use_case.analyze_critical_namespace_events.analyze_critical_namespace_events_use_case import (
    AnalyzeCriticalNamespaceEventsUseCase,
)


class TestAnalyzeCriticalNamespaceEventsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=AnalyzeCriticalNamespaceEventsServicePort)
        use_case = AnalyzeCriticalNamespaceEventsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.analyze.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=AnalyzeCriticalNamespaceEventsServicePort)
        mock_service.analyze.side_effect = RuntimeError("test error")
        use_case = AnalyzeCriticalNamespaceEventsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
