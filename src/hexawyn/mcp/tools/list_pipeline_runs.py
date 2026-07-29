"""MCP tool: list_pipeline_runs."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict

from hexawyn.application.use_case.pipelines.list_pipeline_runs.command import (
    ListPipelineRunsCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs.list_pipeline_runs_use_case import (
    ListPipelineRunsUseCase,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import (
    PipelineRunStats,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


class PipelineRunStatsPayload(TypedDict):
    total_runs: int
    succeeded_runs: int
    failed_runs: int
    cancelled_runs: int
    success_rate: float
    average_duration_seconds: float | None
    fastest_run_name: str | None
    slowest_run_name: str | None


def _stats_payload(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def list_pipeline_runs(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_pipeline_runs)
