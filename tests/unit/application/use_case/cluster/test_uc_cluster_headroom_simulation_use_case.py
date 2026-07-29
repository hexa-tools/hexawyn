from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cluster.cluster_headroom_simulation.cluster_headroom_simulation_use_case import (  # noqa: E501
    ClusterHeadroomSimulationUseCase,
)
from hexawyn.application.use_case.cluster.cluster_headroom_simulation.command import (
    ClusterHeadroomSimulationCommand,
    ProposedWorkloadDict,
)
from hexawyn.application.use_case.cluster.cluster_headroom_simulation.response import (
    ClusterHeadroomSimulationResponse,
)


class TestClusterHeadroomSimulationUseCase:
    def test_simulate_returns_response_type(self) -> None:
        metrics_port = MagicMock()
        metrics_port.get_current_usage.return_value = {
            "cpu_cores": 8.0,
            "memory_gb": 16.0,
        }
        headroom_port = MagicMock()
        headroom_port.get_node_capacity_info.return_value = {
            "total_allocatable_cpu_cores": 32.0,
            "total_allocatable_memory_gb": 64.0,
            "node_count": 4,
            "largest_node_cpu_cores": 8.0,
            "largest_node_memory_gb": 16.0,
            "autoscaler_enabled": True,
        }

        use_case = ClusterHeadroomSimulationUseCase(
            metrics_port=metrics_port, headroom_port=headroom_port
        )
        result = use_case.simulate(ClusterHeadroomSimulationCommand())

        assert isinstance(result, ClusterHeadroomSimulationResponse)
        assert result.error is None

    def test_simulate_with_proposed_workloads(self) -> None:
        metrics_port = MagicMock()
        metrics_port.get_current_usage.return_value = {
            "cpu_cores": 8.0,
            "memory_gb": 16.0,
        }
        headroom_port = MagicMock()
        headroom_port.get_node_capacity_info.return_value = {
            "total_allocatable_cpu_cores": 32.0,
            "total_allocatable_memory_gb": 64.0,
            "node_count": 4,
            "largest_node_cpu_cores": 8.0,
            "largest_node_memory_gb": 16.0,
            "autoscaler_enabled": True,
        }
        workload: ProposedWorkloadDict = {
            "name": "api-service",
            "cpu_request_per_pod": "2",
            "memory_request_per_pod": "4Gi",
            "replicas": 3,
        }

        use_case = ClusterHeadroomSimulationUseCase(
            metrics_port=metrics_port, headroom_port=headroom_port
        )
        result = use_case.simulate(ClusterHeadroomSimulationCommand(proposed_workloads=[workload]))

        assert result.verdict is not None
        assert result.current_cpu_utilization_percent >= 0

    def test_simulate_includes_all_response_fields(self) -> None:
        metrics_port = MagicMock()
        metrics_port.get_current_usage.return_value = {
            "cpu_cores": 8.0,
            "memory_gb": 16.0,
        }
        headroom_port = MagicMock()
        headroom_port.get_node_capacity_info.return_value = {
            "total_allocatable_cpu_cores": 32.0,
            "total_allocatable_memory_gb": 64.0,
            "node_count": 4,
            "largest_node_cpu_cores": 8.0,
            "largest_node_memory_gb": 16.0,
            "autoscaler_enabled": True,
        }

        use_case = ClusterHeadroomSimulationUseCase(
            metrics_port=metrics_port, headroom_port=headroom_port
        )
        result = use_case.simulate(ClusterHeadroomSimulationCommand())

        assert result.current_cpu_utilization_percent >= 0
        assert result.current_memory_utilization_percent >= 0
        assert result.binding_constraint is not None
        assert result.summary is not None
        assert result.autoscaler_enabled is True
