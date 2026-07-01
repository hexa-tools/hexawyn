"""MCP tool: check_resource_constraints — CPU/memory pressure report for a namespace."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.pod_resource_metrics_port import PodResourceMetricsPort
from hexawyn.application.ports.driving.check_resource_constraints.check_resource_constraints_command import (
    CheckResourceConstraintsCommand,
)
from hexawyn.application.use_case.check_resource_constraints.check_resource_constraints_use_case import (
    CheckResourceConstraintsUseCase,
)
from hexawyn.domain.models.resource_constraint import ContainerResourceEntry

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _build_adapter() -> PodResourceMetricsPort:
    from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
        KubernetesPodResourceAdapter,
    )

    return KubernetesPodResourceAdapter()


def _serialize_entry(entry: ContainerResourceEntry) -> dict[str, str | int | float | bool | None]:
    return {
        "container_name": entry.container_name,
        "pod_name": entry.pod_name,
        "namespace": entry.namespace,
        "cpu_usage_millicores": entry.cpu_usage_millicores,
        "cpu_limit_millicores": entry.cpu_limit_millicores,
        "memory_usage_bytes": entry.memory_usage_bytes,
        "memory_limit_bytes": entry.memory_limit_bytes,
        "cpu_pct": round(entry.cpu_pct, 1) if entry.cpu_pct is not None else None,
        "memory_pct": round(entry.memory_pct, 1) if entry.memory_pct is not None else None,
        "risk_level": entry.risk_level.value,
        "is_init_container": entry.is_init_container,
        "tags": ",".join(entry.tags) if entry.tags else "",
    }


def check_resource_constraints(
    namespace: str = "production",
    cpu_threshold_pct: float = 80.0,
    memory_threshold_pct: float = 85.0,
) -> dict[str, str | int | float | list[dict[str, str | int | float | bool | None]] | None]:
    """Return a resource pressure report for all pods in a namespace.

    Identifies containers throttled on CPU (usage > cpu_threshold_pct of limit)
    and at OOMKill risk (memory usage > memory_threshold_pct of limit).
    Sorted CRITICAL first.

    Args:
        namespace: Kubernetes namespace to scan (default: "production").
        cpu_threshold_pct: CPU usage percentage above which a container is throttling risk (default: 80.0).
        memory_threshold_pct: Memory usage percentage above which a container is OOMKill risk (default: 85.0).
    """
    from hexawyn.application.service.resource_constraint_service import ResourceConstraintService

    try:
        adapter = _build_adapter()
        service = ResourceConstraintService(port=adapter)
        use_case = CheckResourceConstraintsUseCase(service=service)
        response = use_case.execute(
            CheckResourceConstraintsCommand(
                namespace=namespace,
                cpu_threshold_pct=cpu_threshold_pct,
                memory_threshold_pct=memory_threshold_pct,
            )
        )
        report = response.report
        return {
            "namespace": report.namespace,
            "total_pods_scanned": report.total_pods_scanned,
            "total_containers": report.total_containers,
            "critical_count": report.critical_count,
            "no_limits_count": report.no_limits_count,
            "ok_count": report.ok_count,
            "containers": [_serialize_entry(e) for e in report.containers],
            "generated_at": report.generated_at.isoformat(),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "total_pods_scanned": 0,
            "total_containers": 0,
            "critical_count": 0,
            "no_limits_count": 0,
            "ok_count": 0,
            "containers": [],
            "generated_at": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(check_resource_constraints)
