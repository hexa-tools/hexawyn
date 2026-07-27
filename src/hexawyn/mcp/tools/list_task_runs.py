"""MCP tool: list_task_runs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.list_task_runs.command import ListTaskRunsCommand
from hexawyn.application.use_case.pipelines.list_task_runs.list_task_runs_use_case import (
    ListTaskRunsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def list_task_runs(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_task_runs)
