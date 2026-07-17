from __future__ import annotations

from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_response import (
    AdaptiveNamespaceInvestigationResponse,
)


class TestAdaptiveNamespaceInvestigationResponse:
    def test_defaults(self) -> None:
        response = AdaptiveNamespaceInvestigationResponse()

        assert response.namespace == ""
        assert response.investigated_resources == []
        assert response.root_cause_candidates == []
        assert response.recommended_actions == []
        assert response.skipped_resources == []
        assert response.node_pressure_context is None
        assert response.has_more_failing is False
        assert response.remaining_failing_count == 0
        assert response.error is None

    def test_error_field(self) -> None:
        response = AdaptiveNamespaceInvestigationResponse(error="Namespace 'ghost' not found")

        assert response.error == "Namespace 'ghost' not found"
