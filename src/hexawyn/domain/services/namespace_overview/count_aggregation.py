from __future__ import annotations

from hexawyn.application.ports.driven.namespace_overview_port import (
    DeploymentStatusRaw,
    PodStatusRaw,
)
from hexawyn.domain.models.namespace_overview import NamespaceCounts


def aggregate_counts(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )
