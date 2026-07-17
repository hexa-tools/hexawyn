from __future__ import annotations

from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_response import (
    GetNamespaceEventsResponse,
)


class TestGetNamespaceEventsResponse:
    def test_defaults(self) -> None:
        response = GetNamespaceEventsResponse()
        assert response.total_events == 0
        assert response.events == []
        assert response.has_more is False
        assert response.error is None

    def test_error_field(self) -> None:
        response = GetNamespaceEventsResponse(error="Namespace 'ghost' not found")
        assert response.error == "Namespace 'ghost' not found"
