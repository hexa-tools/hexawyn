"""MCP tool: pipeline_performance_baseline — CI/CD pipeline performance baseline analysis."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.pipeline_performance_baseline.command import (
    PipelinePerformanceBaselineCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_performance_baseline.pipeline_performance_baseline_use_case import (  # noqa: E501
    PipelinePerformanceBaselineUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def pipeline_performance_baseline(
    pipeline_name: str,
    namespace: str = "ci",
    limit: int = 30,
) -> dict[str, object]:
    """Analyze CI/CD pipeline performance: per-stage stats, trend, outliers.

    Args:
        pipeline_name: Name of the Tekton pipeline to analyze.
        namespace: Kubernetes namespace (default: ci).
        limit: Number of PipelineRuns to analyze (default: 30).

    Returns:
        dict with pipeline, runs_analyzed, stages (avg/p50/p95/max per stage),
        trend (improving/stable/degrading/insufficient_data), trend_pct (signed
        percent change, None if insufficient_data), bottleneck_stage (the stage
        driving the trend, None if no single stage stands out), outliers, error.
    """
    from hexawyn.mcp.server import build_pipeline_baseline_adapter

    try:
        use_case = PipelinePerformanceBaselineUseCase(
            port=build_pipeline_baseline_adapter(),
        )
        r = use_case.execute(
            PipelinePerformanceBaselineCommand(
                pipeline_name=pipeline_name,
                namespace=namespace,
                limit=limit,
            )
        )
        return {
            "pipeline": r.pipeline,
            "runs_analyzed": r.runs_analyzed,
            "requested_limit": r.requested_limit,
            "stages": {
                name: {
                    "avg": s.avg,
                    "p50": s.p50,
                    "p95": s.p95,
                    "max": s.max,
                    "unit": s.unit,
                }
                for name, s in r.stages.items()
            },
            "total_duration": (
                {
                    "avg": r.total_duration.avg,
                    "p50": r.total_duration.p50,
                    "p95": r.total_duration.p95,
                    "max": r.total_duration.max,
                    "unit": r.total_duration.unit,
                }
                if r.total_duration
                else None
            ),
            "outliers": r.outliers,
            "excluded_running": r.excluded_running,
            "excluded_failed": r.excluded_failed,
            "trend": r.trend,
            "trend_pct": r.trend_pct,
            "bottleneck_stage": r.bottleneck_stage,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "pipeline": pipeline_name,
            "runs_analyzed": 0,
            "requested_limit": limit,
            "stages": {},
            "total_duration": None,
            "outliers": [],
            "excluded_running": 0,
            "excluded_failed": 0,
            "trend": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(pipeline_performance_baseline)
