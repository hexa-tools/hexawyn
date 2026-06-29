"""MCP tool: list_task_runs — List all TaskRuns for a given pipeline."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.list_task_runs.list_task_runs_command import (
    ListTaskRunsCommand,
)
from hexawyn.application.use_case.list_task_runs.list_task_runs_use_case import (
    ListTaskRunsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_task_runs(pipeline_name: str, namespace: str = "default") -> dict[str, object]:
    """List all TaskRuns for a given Tekton pipeline with status and step-level detail.

    Args:
        pipeline_name: The Tekton pipeline name to list TaskRuns for.
        namespace: The Kubernetes namespace (default: "default").
    """
    from hexawyn.application.service.list_task_runs_service import ListTaskRunsService
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        service = ListTaskRunsService(tekton_port=adapter)
        use_case = ListTaskRunsUseCase(service=service)
        response = use_case.execute(
            ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace)
        )
        return {"task_runs": list(response.task_runs), "error": None}
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    """Register list_task_runs as an MCP tool on the given FastMCP server."""
    mcp.tool()(list_task_runs)
