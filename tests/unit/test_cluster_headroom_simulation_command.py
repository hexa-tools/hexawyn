from __future__ import annotations

from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_command import (
    ClusterHeadroomSimulationCommand,
)


class TestClusterHeadroomSimulationCommand:
    def test_defaults_to_no_workloads(self) -> None:
        cmd = ClusterHeadroomSimulationCommand()
        assert cmd.proposed_workloads == []

    def test_accepts_proposed_workloads(self) -> None:
        cmd = ClusterHeadroomSimulationCommand(
            proposed_workloads=[
                {
                    "name": "analytics-service",
                    "cpu_request_per_pod": "500m",
                    "memory_request_per_pod": "512Mi",
                }
            ]
        )
        assert cmd.proposed_workloads[0]["name"] == "analytics-service"
