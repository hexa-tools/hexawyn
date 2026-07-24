"""MCP tool: list_pipeline_runs_in_namespace — Operational view of all PipelineRuns in a namespace."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.list_pipeline_runs_in_namespace.command import (
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.use_case.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_use_case import (
    ListPipelineRunsInNamespaceUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_pipeline_runs_in_namespace(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    """Register list_pipeline_runs_in_namespace as an MCP tool on the given FastMCP server."""
    mcp.tool()(list_pipeline_runs_in_namespace)
