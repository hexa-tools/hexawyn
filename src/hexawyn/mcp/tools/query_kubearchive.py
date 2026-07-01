"""MCP tool: query_kubearchive — Query KubeArchive for historical Kubernetes resource state."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_command import (
    QueryKubeArchiveCommand,
)
from hexawyn.application.use_case.query_kubearchive.query_kubearchive_use_case import (
    QueryKubeArchiveUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

DEFAULT_KUBEARCHIVE_URL = "http://localhost:8081"


def query_kubearchive(
    namespace: str,
    resource_type: str = "pods",
    timestamp: str = "",
    compare_with_current: bool = False,
) -> dict[str, object]:
    """Query KubeArchive for the historical state of Kubernetes resources at a given timestamp.

    Args:
        namespace: The Kubernetes namespace to query.
        resource_type: The resource type (e.g. 'pods', 'deployments'). Defaults to 'pods'.
        timestamp: ISO 8601 timestamp to query (e.g. '2026-06-09T10:00:00Z').
        compare_with_current: If True, compare historical state against current cluster state.
    """
    from hexawyn.adapters.secondary.kubearchive_http_adapter import (
        KubeArchiveHTTPAdapter,
    )
    from hexawyn.application.service.historical_state_query_service import (
        HistoricalStateQueryService,
    )
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        endpoint = os.environ.get("KUBEARCHIVE_URL", DEFAULT_KUBEARCHIVE_URL)
        kubearchive = KubeArchiveHTTPAdapter(endpoint=endpoint)
        try:
            k8s = build_k8s_adapter()
            service = HistoricalStateQueryService(kubearchive_port=kubearchive, k8s_port=k8s)
            use_case = QueryKubeArchiveUseCase(service=service)
            response = use_case.execute(
                QueryKubeArchiveCommand(
                    namespace=namespace,
                    resource_type=resource_type,
                    timestamp=timestamp,
                    compare_with_current=compare_with_current,
                )
            )
            result: dict[str, object] = {
                "total_resources": response.total_resources,
                "pods": list(response.pods),
                "queried_timestamp": response.queried_timestamp,
                "comparison": response.comparison,
                "error": response.error,
            }
            return result
        finally:
            kubearchive.close()
    except Exception as exc:
        return {
            "total_resources": 0,
            "pods": [],
            "queried_timestamp": None,
            "comparison": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    """Register query_kubearchive as an MCP tool."""
    mcp.tool()(query_kubearchive)
