from __future__ import annotations

from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_response import (
    AdvancedNamespaceEventAnalyticsResponse,
)


class TestAdvancedNamespaceEventAnalyticsResponse:
    def test_defaults(self) -> None:
        response = AdvancedNamespaceEventAnalyticsResponse()
        assert response.total_events == 0
        assert response.timeline == []
        assert response.storms == []
        assert response.top_reasons == []
        assert response.correlated_incidents == []
        assert response.sampling_applied is False
        assert response.error is None

    def test_error_field(self) -> None:
        response = AdvancedNamespaceEventAnalyticsResponse(error="Namespace 'ghost' not found")
        assert response.error == "Namespace 'ghost' not found"
