from __future__ import annotations

from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_response import (
    ClusterCapacityCeilingForecastResponse,
)


class TestClusterCapacityCeilingForecastResponse:
    def test_defaults(self) -> None:
        response = ClusterCapacityCeilingForecastResponse()

        assert response.cpu is None
        assert response.memory is None
        assert response.critical_resource == ""
        assert response.autoscaler_enabled is False
        assert response.recommendation == ""
        assert response.confidence == ""
        assert response.window_days_used == 0
        assert response.error is None

    def test_error_field(self) -> None:
        response = ClusterCapacityCeilingForecastResponse(error="Prometheus unavailable")

        assert response.error == "Prometheus unavailable"
