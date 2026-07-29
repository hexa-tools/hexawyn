from __future__ import annotations

from unittest.mock import MagicMock


class TestAnalyzeAdvancedNamespaceEventsUseCase:
    def test_execute_returns_response(self) -> None:
        from hexawyn.application.use_case.troubleshooting.analyze_advanced_namespace_events.analyze_advanced_namespace_events_use_case import (  # noqa: E501
            AnalyzeAdvancedNamespaceEventsUseCase,
        )
        from hexawyn.application.use_case.troubleshooting.analyze_advanced_namespace_events.command import (  # noqa: E501
            AnalyzeAdvancedNamespaceEventsCommand,
        )
        from hexawyn.application.use_case.troubleshooting.analyze_advanced_namespace_events.response import (  # noqa: E501
            AdvancedNamespaceEventAnalyticsResponse,
        )

        port = MagicMock()
        port.list_events.return_value = []
        use_case = AnalyzeAdvancedNamespaceEventsUseCase(port=port)
        result = use_case.execute(AnalyzeAdvancedNamespaceEventsCommand(namespace="default"))
        assert isinstance(result, AdvancedNamespaceEventAnalyticsResponse)
