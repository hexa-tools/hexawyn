"""MCP tool: pipeline_run_logs — Get logs of a PipelineRun with failed step highlighting."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.pipeline_run_logs.pipeline_run_logs_command import (
    PipelineRunLogsCommand,
)
from hexawyn.application.use_case.pipeline_run_logs.pipeline_run_logs_use_case import (
    PipelineRunLogsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def pipeline_run_logs(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.application.service.pipeline_run_logs_service import PipelineRunLogsService
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(service=PipelineRunLogsService(port=a)).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(pipeline_run_logs)
