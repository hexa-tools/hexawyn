from __future__ import annotations

from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_response import (
    SemanticLogSearchResponse,
)


class TestSemanticLogSearchResponse:
    def test_defaults(self) -> None:
        response = SemanticLogSearchResponse()
        assert response.groups == []
        assert response.pods_affected == 0
        assert response.services_affected == 0
        assert response.skipped_pods == []
        assert response.skipped_namespaces == []
        assert response.scanned_namespaces == []
        assert response.namespaces_total == 0
        assert response.no_matches is False
        assert response.summary == ""
        assert response.error is None

    def test_error_field(self) -> None:
        response = SemanticLogSearchResponse(error="Namespace 'ghost' not found")
        assert response.error == "Namespace 'ghost' not found"
