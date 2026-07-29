"""Unit tests for the Cluster Headroom Simulation domain models — pure
dataclasses, no I/O."""

from __future__ import annotations

from hexawyn.domain.models.headroom_simulation import (
    ClusterHeadroomSnapshot,
    HeadroomSimulationReport,
    HeadroomSimulationRequest,
    ProposedWorkload,
)


class TestProposedWorkload:
    def test_default_replicas(self) -> None:
        workload = ProposedWorkload(
            name="notification-service",
            cpu_request_per_pod="250m",
            memory_request_per_pod="256Mi",
        )

        assert workload.replicas == 2  # noqa: PLR2004

    def test_custom_replicas(self) -> None:
        workload = ProposedWorkload(
            name="analytics-service",
            cpu_request_per_pod="500m",
            memory_request_per_pod="512Mi",
            replicas=3,
        )

        assert workload.replicas == 3  # noqa: PLR2004


class TestClusterHeadroomSnapshot:
    def test_fields(self) -> None:
        snapshot = ClusterHeadroomSnapshot(
            total_allocatable_cpu_cores=80.0,
            total_allocatable_memory_gb=320.0,
            used_cpu_cores=48.0,
            used_memory_gb=192.0,
            node_count=10,
            largest_node_cpu_cores=8.0,
            largest_node_memory_gb=32.0,
            autoscaler_enabled=False,
        )

        assert snapshot.node_count == 10  # noqa: PLR2004
        assert snapshot.largest_node_cpu_cores == 8.0  # noqa: PLR2004


class TestHeadroomSimulationRequest:
    def test_defaults_to_no_workloads(self) -> None:
        request = HeadroomSimulationRequest()

        assert request.proposed_workloads == []


class TestHeadroomSimulationReport:
    def test_fields(self) -> None:
        report = HeadroomSimulationReport(
            current_cpu_utilization_percent=60.0,
            current_memory_utilization_percent=60.0,
            total_new_cpu_cores=1.5,
            total_new_memory_gb=1.5,
            post_cpu_utilization_percent=62.0,
            post_memory_utilization_percent=61.0,
            binding_constraint="CPU",
            verdict="fits",
            recommended_additional_nodes=0,
            autoscaler_enabled=False,
            unschedulable_workloads=[],
            summary="Fits comfortably.",
        )

        assert report.verdict == "fits"
        assert report.binding_constraint == "CPU"
        assert report.unschedulable_workloads == []
