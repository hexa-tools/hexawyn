from __future__ import annotations

from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_response import (
    SummarizeNamespaceEventsResponse,
)


class TestSummarizeNamespaceEventsResponse:
    def test_defaults(self) -> None:
        response = SummarizeNamespaceEventsResponse()
        assert response.total_events == 0
        assert response.severity_breakdown == {}
        assert response.top_affected_pods == []
        assert response.error is None

    def test_error_field(self) -> None:
        response = SummarizeNamespaceEventsResponse(error="Namespace 'ghost' not found")
        assert response.error == "Namespace 'ghost' not found"
