"""MCP tool: get_pipeline_run_status."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.get_pipeline_run_status.command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.get_pipeline_run_status_use_case import (  # noqa: E501
    GetPipelineRunStatusUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def get_pipeline_run_status() -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = GetPipelineRunStatusUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(GetPipelineRunStatusCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_pipeline_run_status)
