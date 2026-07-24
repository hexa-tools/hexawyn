"""MCP tool: trace_pipeline_run_dag."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.trace_pipeline_run_dag.command import TracePipelineRunDagCommand
from hexawyn.application.use_case.trace_pipeline_run_dag.trace_pipeline_run_dag_use_case import (
    TracePipelineRunDAGUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def trace_pipeline_run_dag() -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        use_case = TracePipelineRunDAGUseCase(port=build_pipeline_run_logs_adapter())
        use_case.execute(TracePipelineRunDagCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(trace_pipeline_run_dag)
