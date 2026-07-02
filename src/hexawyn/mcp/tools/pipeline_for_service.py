"""MCP tool: pipeline_for_service — Find the pipeline deploying a given service."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.pipeline_for_service.pipeline_for_service_command import (
    PipelineForServiceCommand,
)
from hexawyn.application.use_case.pipeline_for_service.pipeline_for_service_use_case import (
    PipelineForServiceUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def pipeline_for_service(service_name: str) -> dict[str, object]:
    from hexawyn.application.service.pipeline_for_service_service import PipelineForServiceService
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        a = build_pipeline_for_service_adapter()
        r = PipelineForServiceUseCase(service=PipelineForServiceService(port=a)).execute(
            PipelineForServiceCommand(service_name=service_name)
        )
        return {
            "service_name": r.service_name,
            "pipelines_found": r.pipelines_found,
            "pipelines": r.pipelines,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(pipeline_for_service)
