"""MCP tool: analyze_failed_pipeline — Analyze a failed pipeline run."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.analyze_failed_pipeline_use_case import (  # noqa: E501
    AnalyzeFailedPipelineUseCase,
)
from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.command import (
    AnalyzeFailedPipelineCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def analyze_failed_pipeline(pipeline_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = AnalyzeFailedPipelineUseCase(tekton_port=build_tekton_adapter())  # type: ignore
        r = use_case.execute(AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name))
        return {"analysis": r.analysis, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"analysis": "", "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(analyze_failed_pipeline)
