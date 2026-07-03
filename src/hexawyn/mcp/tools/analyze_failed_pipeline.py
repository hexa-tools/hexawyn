"""MCP tool: analyze_failed_pipeline — automated root cause analysis for a failed pipeline."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_command import (
    AnalyzeFailedPipelineCommand,
)
from hexawyn.application.use_case.analyze_failed_pipeline.analyze_failed_pipeline_use_case import (
    AnalyzeFailedPipelineUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def analyze_failed_pipeline(pipeline_name: str, namespace: str = "default") -> dict[str, object]:
    from hexawyn.application.service.analyze_failed_pipeline_service import (
        AnalyzeFailedPipelineService,
    )
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter, build_tekton_adapter

    try:
        tekton_adapter = build_tekton_adapter()
        logs_adapter = build_pipeline_run_logs_adapter()
        service = AnalyzeFailedPipelineService(
            tekton_port=tekton_adapter, pipeline_run_logs_port=logs_adapter
        )
        r = AnalyzeFailedPipelineUseCase(service=service).execute(
            AnalyzeFailedPipelineCommand(pipeline_name=pipeline_name, namespace=namespace)
        )
        return {
            "pipeline_name": r.pipeline_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "failures": r.failures,
            "aggregated_root_cause": r.aggregated_root_cause,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_name": pipeline_name, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(analyze_failed_pipeline)
