"""MCP tool: get_resource_usage — Real CPU/memory usage per pod/namespace from metrics-server."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.get_resource_usage.command import (
    GetResourceUsageCommand,
)
from hexawyn.application.use_case.cluster.get_resource_usage.get_resource_usage_use_case import (
    GetResourceUsageUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def get_resource_usage(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_resource_usage)
