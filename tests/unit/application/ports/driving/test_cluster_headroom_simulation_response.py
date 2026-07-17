from __future__ import annotations

from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_response import (
    ClusterHeadroomSimulationResponse,
)


class TestClusterHeadroomSimulationResponse:
    def test_defaults(self) -> None:
        response = ClusterHeadroomSimulationResponse()

        assert response.verdict == ""
        assert response.binding_constraint == ""
        assert response.unschedulable_workloads == []
        assert response.recommended_additional_nodes == 0
        assert response.error is None

    def test_error_field(self) -> None:
        response = ClusterHeadroomSimulationResponse(error="Prometheus unavailable")

        assert response.error == "Prometheus unavailable"
