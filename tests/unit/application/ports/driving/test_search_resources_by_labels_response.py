from __future__ import annotations

from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_response import (
    SearchResourcesByLabelsResponse,
)


class TestSearchResourcesByLabelsResponse:
    def test_defaults(self) -> None:
        response = SearchResourcesByLabelsResponse()
        assert response.total_matched == 0
        assert response.groups == []
        assert response.has_more is False
        assert response.remaining_count == 0
        assert response.no_matches is False
        assert response.summary == ""
        assert response.error is None

    def test_error_field(self) -> None:
        response = SearchResourcesByLabelsResponse(error="Namespace 'ghost' not found")
        assert response.error == "Namespace 'ghost' not found"
