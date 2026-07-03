from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_command import (
    AdvancedNamespaceEventAnalyticsCommand,
)
from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_response import (
    AdvancedNamespaceEventAnalyticsResponse,
)
from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_service_port import (
    AdvancedNamespaceEventAnalyticsServicePort,
)
from hexawyn.application.use_case.advanced_namespace_event_analytics.advanced_namespace_event_analytics_use_case import (
    AdvancedNamespaceEventAnalyticsUseCase,
)


class TestAdvancedNamespaceEventAnalyticsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=AdvancedNamespaceEventAnalyticsServicePort)
        expected = AdvancedNamespaceEventAnalyticsResponse(namespace="data-pipeline")
        service.analyze.return_value = expected
        use_case = AdvancedNamespaceEventAnalyticsUseCase(service=service)
        command = AdvancedNamespaceEventAnalyticsCommand(namespace="data-pipeline")

        result = use_case.execute(command)

        service.analyze.assert_called_once_with(command)
        assert result is expected
