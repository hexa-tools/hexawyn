from __future__ import annotations

from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_response import (
    AnalyzeCriticalNamespaceEventsResponse,
)


class TestAnalyzeCriticalNamespaceEventsResponse:
    def test_defaults(self) -> None:
        response = AnalyzeCriticalNamespaceEventsResponse()
        assert response.critical_incidents == []
        assert response.error is None

    def test_error_field(self) -> None:
        response = AnalyzeCriticalNamespaceEventsResponse(error="Namespace 'ghost' not found")
        assert response.error == "Namespace 'ghost' not found"
