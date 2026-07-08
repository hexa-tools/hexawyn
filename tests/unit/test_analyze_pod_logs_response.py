from __future__ import annotations

from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_response import (
    AnalyzePodLogsResponse,
)


class TestAnalyzePodLogsResponse:
    def test_defaults(self) -> None:
        response = AnalyzePodLogsResponse()
        assert response.total_lines == 0
        assert response.error is None
        assert response.patterns == []
        assert response.ranked_events == []

    def test_error_field(self) -> None:
        response = AnalyzePodLogsResponse(error="Pod not found")
        assert response.error == "Pod not found"
