"""MCP tool: analysis_runs_list — List AnalysisRuns."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.analysis_runs_list.analysis_runs_list_use_case import (
    AnalysisRunsListUseCase,
)
from hexawyn.application.use_case.pipelines.analysis_runs_list.command import (
    AnalysisRunsListCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def analysis_runs_list(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(analysis_runs_list)
