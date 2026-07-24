"""MCP tool: keda_scaledjobs_list — List KEDA ScaledJobs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.keda_scaledjobs_list.command import KedaScaledjobsListCommand
from hexawyn.application.use_case.keda_scaledjobs_list.keda_scaledjobs_list_use_case import (
    KedaScaledJobsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledjobs_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledJobsListUseCase(keda_port=adapter)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"scaled_jobs": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledjobs_list)
