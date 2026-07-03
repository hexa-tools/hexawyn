from __future__ import annotations

from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_response import (
    WatchPodLogsResponse,
)


class TestWatchPodLogsResponse:
    def test_defaults(self) -> None:
        response = WatchPodLogsResponse()
        assert response.stop_reason == ""
        assert response.alerts == []
        assert response.patterns == []
        assert response.error is None

    def test_error_field(self) -> None:
        response = WatchPodLogsResponse(error="Pod not found")
        assert response.error == "Pod not found"
