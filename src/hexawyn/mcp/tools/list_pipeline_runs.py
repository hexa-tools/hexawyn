"""MCP tool: list_pipeline_runs — List last N PipelineRuns for a service with delivery stats."""

from __future__ import annotations

from dataclasses import asdict
from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.list_pipeline_runs.list_pipeline_runs_command import (
    ListPipelineRunsCommand,
)
from hexawyn.application.use_case.list_pipeline_runs.list_pipeline_runs_use_case import (
    ListPipelineRunsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_pipeline_runs(
    service_name: str,
    namespace: str = "default",
    limit: int = 10,
) -> dict[str, object]:
    """List the last N PipelineRuns for a service with success rate, average duration,
    fastest/slowest run, and outlier detection (runs exceeding 2x average duration).

    Args:
        service_name: The service or pipeline name to query PipelineRuns for.
        namespace: The Kubernetes namespace (default: "default").
        limit: Maximum number of runs to return, most recent first (default: 10).
    """
    from hexawyn.application.service.list_pipeline_runs_service import ListPipelineRunsService
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        service = ListPipelineRunsService(tekton_port=adapter)
        use_case = ListPipelineRunsUseCase(service=service)
        response = use_case.execute(
            ListPipelineRunsCommand(
                service_name=service_name,
                namespace=namespace,
                limit=limit,
            )
        )
        return {
            "runs": list(response.runs),
            "stats": asdict(response.stats),
            "outliers": response.outliers,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stats": {},
            "outliers": [],
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    """Register list_pipeline_runs as an MCP tool on the given FastMCP server."""
    mcp.tool()(list_pipeline_runs)
