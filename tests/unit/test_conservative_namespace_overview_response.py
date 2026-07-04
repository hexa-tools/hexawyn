from __future__ import annotations

from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_response import (
    ConservativeNamespaceOverviewResponse,
)


class TestConservativeNamespaceOverviewResponse:
    def test_defaults(self) -> None:
        response = ConservativeNamespaceOverviewResponse()
        assert response.counts is None
        assert response.health_status == ""
        assert response.root_cause == ""
        assert response.unhealthy_resources == []
        assert response.warnings == []
        assert response.has_more_unhealthy is False
        assert response.remaining_unhealthy_count == 0
        assert response.estimated_tokens == 0
        assert response.is_empty is False
        assert response.summary == ""
        assert response.error is None

    def test_error_field(self) -> None:
        response = ConservativeNamespaceOverviewResponse(error="Namespace 'ghost' not found")
        assert response.error == "Namespace 'ghost' not found"
