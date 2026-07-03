from __future__ import annotations

from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_response import (
    ExecutePrometheusQueryResponse,
)


class TestExecutePrometheusQueryResponse:
    def test_defaults(self) -> None:
        response = ExecutePrometheusQueryResponse()
        assert response.results == []
        assert response.result_count == 0
        assert response.truncated is False
        assert response.no_data is False
        assert response.summary == ""
        assert response.error is None

    def test_error_field(self) -> None:
        response = ExecutePrometheusQueryResponse(
            error="Prometheus is unavailable at 'http://prometheus.monitoring.svc:9090'."
        )
        assert "prometheus.monitoring.svc:9090" in response.error
