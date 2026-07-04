from __future__ import annotations

from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_response import (
    HotNodeAnalysisResponse,
)


class TestHotNodeAnalysisResponse:
    def test_defaults(self) -> None:
        response = HotNodeAnalysisResponse()

        assert response.hot_nodes == []
        assert response.healthy_node_count == 0
        assert response.excluded_cordoned_nodes == []
        assert response.warnings == []
        assert response.summary == ""
        assert response.error is None

    def test_error_field(self) -> None:
        response = HotNodeAnalysisResponse(error="Prometheus unavailable")

        assert response.error == "Prometheus unavailable"
