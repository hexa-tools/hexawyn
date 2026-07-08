"""MCP tool: analysis_runs_list — List AnalysisRuns associated with Rollouts."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.analysis_runs_list.analysis_runs_list_command import (
    AnalysisRunsListCommand,
)
from hexawyn.application.use_case.analysis_runs_list.analysis_runs_list_use_case import (
    AnalysisRunsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def analysis_runs_list(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    """List AnalysisRuns, optionally filtered by rollout name.

    Args:
        rollout_name: Optional rollout name filter.
        namespace: Optional namespace filter.
    """
    from hexawyn.application.service.analysis_runs_list_service import (
        AnalysisRunsListService,
    )
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        service = AnalysisRunsListService(rollouts_port=adapter)
        use_case = AnalysisRunsListUseCase(service=service)
        response = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {
            "analysis_runs": response.analysis_runs,
            "error": response.error,
        }
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(analysis_runs_list)
