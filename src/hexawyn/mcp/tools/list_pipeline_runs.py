"""MCP tool: list_pipeline_runs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.list_pipeline_runs.command import ListPipelineRunsCommand
from hexawyn.application.use_case.list_pipeline_runs.list_pipeline_runs_use_case import (
    ListPipelineRunsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _compute_outliers(runs: list[dict[str, object]]) -> list[str]:
    if len(runs) < 3:
        return []
    outlier_names: list[str] = []
    for i, run in enumerate(runs):
        dur = run.get("duration_seconds")
        if dur is None:
            continue
        if isinstance(dur, int | float) and dur > 0:
            other_durations: list[float] = [
                float(runs[j].get("duration_seconds") or 0)  # type: ignore[arg-type]
                for j in range(len(runs))
                if j != i
            ]
            other_mean = sum(other_durations) / len(other_durations)
            if other_mean > 0 and dur > other_mean * 2:
                outlier_names.append(str(run.get("name", "")))
    return outlier_names


def _compute_duration_stats(runs: list[dict[str, object]]) -> dict[str, object]:
    durations: list[float] = []
    for run in runs:
        dur = run.get("duration_seconds")
        if dur is not None and isinstance(dur, int | float):
            durations.append(float(dur))
    if not durations:
        return {"mean_s": 0, "median_s": 0}
    sorted_durations = sorted(durations)
    n = len(sorted_durations)
    median = (
        sorted_durations[n // 2]
        if n % 2 == 1
        else (sorted_durations[n // 2 - 1] + sorted_durations[n // 2]) / 2
    )
    return {
        "mean_s": round(sum(durations) / len(durations), 1),
        "median_s": round(median, 1),
    }


def list_pipeline_runs(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListPipelineRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.pipeline_runs)
        outliers = _compute_outliers(runs)
        stats = _compute_duration_stats(runs)
        return {
            "runs": runs,
            "stats": stats,
            "outliers": outliers,
            "note": f"{len(runs)} runs, {len(outliers)} outliers" if outliers else None,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_pipeline_runs)
