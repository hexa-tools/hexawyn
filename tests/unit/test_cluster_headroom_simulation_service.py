"""Unit tests for ClusterHeadroomSimulationService (mocks the existing
MetricsQueryPort [ECA-31, reused via instant_query] + the new
HeadroomSimulationPort)."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_command import (
    ClusterHeadroomSimulationCommand,
)
from hexawyn.application.service.cluster_headroom_simulation_service import (
    ClusterHeadroomSimulationService,
)


def _capacity_info(
    total_cpu: float = 80.0,
    total_memory: float = 320.0,
    node_count: int = 10,
    largest_cpu: float = 8.0,
    largest_memory: float = 32.0,
    autoscaler_enabled: bool = False,
) -> dict:
    return {
        "total_allocatable_cpu_cores": total_cpu,
        "total_allocatable_memory_gb": total_memory,
        "node_count": node_count,
        "largest_node_cpu_cores": largest_cpu,
        "largest_node_memory_gb": largest_memory,
        "autoscaler_enabled": autoscaler_enabled,
    }


def _make_service(
    metrics_port: MagicMock | None = None, headroom_port: MagicMock | None = None
) -> tuple[ClusterHeadroomSimulationService, MagicMock, MagicMock]:
    if metrics_port is None:
        metrics_port = MagicMock()
        metrics_port.instant_query.side_effect = [
            [{"metric": {}, "value": 48.0}],
            [{"metric": {}, "value": 192.0}],
        ]
    if headroom_port is None:
        headroom_port = MagicMock()
        headroom_port.get_node_capacity_info.return_value = _capacity_info()
    service = ClusterHeadroomSimulationService(
        metrics_port=metrics_port, headroom_port=headroom_port
    )
    return service, metrics_port, headroom_port


class TestPrometheusQueries:
    def test_calls_instant_query_twice(self) -> None:
        service, metrics_port, _ = _make_service()

        service.simulate(ClusterHeadroomSimulationCommand())

        assert metrics_port.instant_query.call_count == 2

    def test_missing_prometheus_data_defaults_to_zero_usage(self) -> None:
        metrics_port = MagicMock()
        metrics_port.instant_query.side_effect = [[], []]
        service, _, _ = _make_service(metrics_port=metrics_port)

        response = service.simulate(ClusterHeadroomSimulationCommand())

        assert response.current_cpu_utilization_percent == 0.0


class TestHeadroomPort:
    def test_calls_capacity_port_once(self) -> None:
        service, _, headroom_port = _make_service()

        service.simulate(ClusterHeadroomSimulationCommand())

        headroom_port.get_node_capacity_info.assert_called_once()


class TestWorkloadMapping:
    def test_default_replicas_applied_when_omitted(self) -> None:
        service, _, _ = _make_service()

        response = service.simulate(
            ClusterHeadroomSimulationCommand(
                proposed_workloads=[
                    {
                        "name": "solo-service",
                        "cpu_request_per_pod": "500m",
                        "memory_request_per_pod": "512Mi",
                    }
                ]
            )
        )

        assert response.total_new_cpu_cores == 1.0
        assert response.total_new_memory_gb == 1.0

    def test_explicit_replicas_respected(self) -> None:
        service, _, _ = _make_service()

        response = service.simulate(
            ClusterHeadroomSimulationCommand(
                proposed_workloads=[
                    {
                        "name": "solo-service",
                        "cpu_request_per_pod": "500m",
                        "memory_request_per_pod": "512Mi",
                        "replicas": 3,
                    }
                ]
            )
        )

        assert response.total_new_cpu_cores == 1.5


class TestResponseComposition:
    def test_fits_scenario(self) -> None:
        service, _, _ = _make_service()

        response = service.simulate(ClusterHeadroomSimulationCommand())

        assert response.error is None
        assert response.current_cpu_utilization_percent == 60.0
        assert response.verdict == "fits"
