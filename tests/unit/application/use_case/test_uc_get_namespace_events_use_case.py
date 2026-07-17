"""Unit tests for GetNamespaceEventsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_service_port import (
    GetNamespaceEventsServicePort,
)
from hexawyn.application.use_case.get_namespace_events.get_namespace_events_use_case import (
    GetNamespaceEventsUseCase,
)


class TestGetNamespaceEventsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GetNamespaceEventsServicePort)
        use_case = GetNamespaceEventsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_events.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GetNamespaceEventsServicePort)
        mock_service.get_events.side_effect = RuntimeError("test error")
        use_case = GetNamespaceEventsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
