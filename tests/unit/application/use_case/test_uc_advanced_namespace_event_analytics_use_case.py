"""Unit tests for AdvancedNamespaceEventAnalyticsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_service_port import (
    AdvancedNamespaceEventAnalyticsServicePort,
)
from hexawyn.application.use_case.advanced_namespace_event_analytics.advanced_namespace_event_analytics_use_case import (
    AdvancedNamespaceEventAnalyticsUseCase,
)


class TestAdvancedNamespaceEventAnalyticsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=AdvancedNamespaceEventAnalyticsServicePort)
        use_case = AdvancedNamespaceEventAnalyticsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.analyze.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=AdvancedNamespaceEventAnalyticsServicePort)
        mock_service.analyze.side_effect = RuntimeError("test error")
        use_case = AdvancedNamespaceEventAnalyticsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
