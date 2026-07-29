# mypy: ignore-errors
"""MCP tool: pipeline_for_service."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.pipeline_for_service.command import (
    PipelineForServiceCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_for_service.pipeline_for_service_use_case import (  # noqa: E501  # type: ignore  # type: ignore
    PipelineForServiceUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def pipeline_for_service(service_name: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_for_service_adapter

    try:
        use_case = PipelineForServiceUseCase(port=build_pipeline_for_service_adapter())
        _ = use_case.execute(PipelineForServiceCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(pipeline_for_service)
