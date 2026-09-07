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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_pipeline_performance_baseline__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_pipeline_performance_baseline__mutmut)
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


def x_pipeline_performance_baseline__mutmut_orig(
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


def x_pipeline_performance_baseline__mutmut_1(
    pipeline_name: str,
    namespace: str = "XXciXX",
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


def x_pipeline_performance_baseline__mutmut_2(
    pipeline_name: str,
    namespace: str = "CI",
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


def x_pipeline_performance_baseline__mutmut_3(
    pipeline_name: str,
    namespace: str = "ci",
    limit: int = 31,
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


def x_pipeline_performance_baseline__mutmut_4(
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
        use_case = None
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


def x_pipeline_performance_baseline__mutmut_5(
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
            port=None,
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


def x_pipeline_performance_baseline__mutmut_6(
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
        r = None
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


def x_pipeline_performance_baseline__mutmut_7(
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
            None
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


def x_pipeline_performance_baseline__mutmut_8(
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
                pipeline_name=None,
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


def x_pipeline_performance_baseline__mutmut_9(
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
                namespace=None,
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


def x_pipeline_performance_baseline__mutmut_10(
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
                limit=None,
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


def x_pipeline_performance_baseline__mutmut_11(
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


def x_pipeline_performance_baseline__mutmut_12(
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


def x_pipeline_performance_baseline__mutmut_13(
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


def x_pipeline_performance_baseline__mutmut_14(
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
            "XXpipelineXX": r.pipeline,
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


def x_pipeline_performance_baseline__mutmut_15(
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
            "PIPELINE": r.pipeline,
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


def x_pipeline_performance_baseline__mutmut_16(
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
            "XXruns_analyzedXX": r.runs_analyzed,
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


def x_pipeline_performance_baseline__mutmut_17(
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
            "RUNS_ANALYZED": r.runs_analyzed,
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


def x_pipeline_performance_baseline__mutmut_18(
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
            "XXrequested_limitXX": r.requested_limit,
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


def x_pipeline_performance_baseline__mutmut_19(
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
            "REQUESTED_LIMIT": r.requested_limit,
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


def x_pipeline_performance_baseline__mutmut_20(
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
            "XXstagesXX": {
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


def x_pipeline_performance_baseline__mutmut_21(
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
            "STAGES": {
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


def x_pipeline_performance_baseline__mutmut_22(
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
                    "XXavgXX": s.avg,
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


def x_pipeline_performance_baseline__mutmut_23(
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
                    "AVG": s.avg,
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


def x_pipeline_performance_baseline__mutmut_24(
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
                    "XXp50XX": s.p50,
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


def x_pipeline_performance_baseline__mutmut_25(
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
                    "P50": s.p50,
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


def x_pipeline_performance_baseline__mutmut_26(
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
                    "XXp95XX": s.p95,
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


def x_pipeline_performance_baseline__mutmut_27(
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
                    "P95": s.p95,
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


def x_pipeline_performance_baseline__mutmut_28(
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
                    "XXmaxXX": s.max,
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


def x_pipeline_performance_baseline__mutmut_29(
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
                    "MAX": s.max,
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


def x_pipeline_performance_baseline__mutmut_30(
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
                    "XXunitXX": s.unit,
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


def x_pipeline_performance_baseline__mutmut_31(
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
                    "UNIT": s.unit,
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


def x_pipeline_performance_baseline__mutmut_32(
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
            "XXtotal_durationXX": (
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


def x_pipeline_performance_baseline__mutmut_33(
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
            "TOTAL_DURATION": (
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


def x_pipeline_performance_baseline__mutmut_34(
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
                    "XXavgXX": r.total_duration.avg,
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


def x_pipeline_performance_baseline__mutmut_35(
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
                    "AVG": r.total_duration.avg,
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


def x_pipeline_performance_baseline__mutmut_36(
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
                    "XXp50XX": r.total_duration.p50,
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


def x_pipeline_performance_baseline__mutmut_37(
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
                    "P50": r.total_duration.p50,
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


def x_pipeline_performance_baseline__mutmut_38(
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
                    "XXp95XX": r.total_duration.p95,
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


def x_pipeline_performance_baseline__mutmut_39(
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
                    "P95": r.total_duration.p95,
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


def x_pipeline_performance_baseline__mutmut_40(
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
                    "XXmaxXX": r.total_duration.max,
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


def x_pipeline_performance_baseline__mutmut_41(
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
                    "MAX": r.total_duration.max,
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


def x_pipeline_performance_baseline__mutmut_42(
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
                    "XXunitXX": r.total_duration.unit,
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


def x_pipeline_performance_baseline__mutmut_43(
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
                    "UNIT": r.total_duration.unit,
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


def x_pipeline_performance_baseline__mutmut_44(
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
            "XXoutliersXX": r.outliers,
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


def x_pipeline_performance_baseline__mutmut_45(
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
            "OUTLIERS": r.outliers,
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


def x_pipeline_performance_baseline__mutmut_46(
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
            "XXexcluded_runningXX": r.excluded_running,
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


def x_pipeline_performance_baseline__mutmut_47(
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
            "EXCLUDED_RUNNING": r.excluded_running,
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


def x_pipeline_performance_baseline__mutmut_48(
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
            "XXexcluded_failedXX": r.excluded_failed,
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


def x_pipeline_performance_baseline__mutmut_49(
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
            "EXCLUDED_FAILED": r.excluded_failed,
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


def x_pipeline_performance_baseline__mutmut_50(
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
            "XXtrendXX": r.trend,
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


def x_pipeline_performance_baseline__mutmut_51(
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
            "TREND": r.trend,
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


def x_pipeline_performance_baseline__mutmut_52(
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
            "XXtrend_pctXX": r.trend_pct,
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


def x_pipeline_performance_baseline__mutmut_53(
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
            "TREND_PCT": r.trend_pct,
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


def x_pipeline_performance_baseline__mutmut_54(
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
            "XXbottleneck_stageXX": r.bottleneck_stage,
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


def x_pipeline_performance_baseline__mutmut_55(
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
            "BOTTLENECK_STAGE": r.bottleneck_stage,
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


def x_pipeline_performance_baseline__mutmut_56(
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
            "XXnoteXX": r.note,
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


def x_pipeline_performance_baseline__mutmut_57(
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
            "NOTE": r.note,
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


def x_pipeline_performance_baseline__mutmut_58(
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
            "XXerrorXX": r.error,
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


def x_pipeline_performance_baseline__mutmut_59(
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
            "ERROR": r.error,
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


def x_pipeline_performance_baseline__mutmut_60(
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
            "XXpipelineXX": pipeline_name,
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


def x_pipeline_performance_baseline__mutmut_61(
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
            "PIPELINE": pipeline_name,
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


def x_pipeline_performance_baseline__mutmut_62(
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
            "XXruns_analyzedXX": 0,
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


def x_pipeline_performance_baseline__mutmut_63(
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
            "RUNS_ANALYZED": 0,
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


def x_pipeline_performance_baseline__mutmut_64(
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
            "runs_analyzed": 1,
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


def x_pipeline_performance_baseline__mutmut_65(
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
            "XXrequested_limitXX": limit,
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


def x_pipeline_performance_baseline__mutmut_66(
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
            "REQUESTED_LIMIT": limit,
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


def x_pipeline_performance_baseline__mutmut_67(
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
            "XXstagesXX": {},
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


def x_pipeline_performance_baseline__mutmut_68(
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
            "STAGES": {},
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


def x_pipeline_performance_baseline__mutmut_69(
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
            "XXtotal_durationXX": None,
            "outliers": [],
            "excluded_running": 0,
            "excluded_failed": 0,
            "trend": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_70(
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
            "TOTAL_DURATION": None,
            "outliers": [],
            "excluded_running": 0,
            "excluded_failed": 0,
            "trend": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_71(
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
            "XXoutliersXX": [],
            "excluded_running": 0,
            "excluded_failed": 0,
            "trend": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_72(
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
            "OUTLIERS": [],
            "excluded_running": 0,
            "excluded_failed": 0,
            "trend": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_73(
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
            "XXexcluded_runningXX": 0,
            "excluded_failed": 0,
            "trend": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_74(
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
            "EXCLUDED_RUNNING": 0,
            "excluded_failed": 0,
            "trend": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_75(
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
            "excluded_running": 1,
            "excluded_failed": 0,
            "trend": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_76(
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
            "XXexcluded_failedXX": 0,
            "trend": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_77(
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
            "EXCLUDED_FAILED": 0,
            "trend": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_78(
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
            "excluded_failed": 1,
            "trend": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_79(
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
            "XXtrendXX": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_80(
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
            "TREND": "insufficient_data",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_81(
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
            "trend": "XXinsufficient_dataXX",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_82(
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
            "trend": "INSUFFICIENT_DATA",
            "trend_pct": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_83(
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
            "XXtrend_pctXX": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_84(
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
            "TREND_PCT": None,
            "bottleneck_stage": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_85(
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
            "XXbottleneck_stageXX": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_86(
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
            "BOTTLENECK_STAGE": None,
            "note": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_87(
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
            "XXnoteXX": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_88(
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
            "NOTE": "",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_89(
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
            "note": "XXXX",
            "error": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_90(
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
            "XXerrorXX": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_91(
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
            "ERROR": str(exc),
        }


def x_pipeline_performance_baseline__mutmut_92(
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
            "error": str(None),
        }

mutants_x_pipeline_performance_baseline__mutmut['_mutmut_orig'] = x_pipeline_performance_baseline__mutmut_orig # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_1'] = x_pipeline_performance_baseline__mutmut_1 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_2'] = x_pipeline_performance_baseline__mutmut_2 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_3'] = x_pipeline_performance_baseline__mutmut_3 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_4'] = x_pipeline_performance_baseline__mutmut_4 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_5'] = x_pipeline_performance_baseline__mutmut_5 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_6'] = x_pipeline_performance_baseline__mutmut_6 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_7'] = x_pipeline_performance_baseline__mutmut_7 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_8'] = x_pipeline_performance_baseline__mutmut_8 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_9'] = x_pipeline_performance_baseline__mutmut_9 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_10'] = x_pipeline_performance_baseline__mutmut_10 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_11'] = x_pipeline_performance_baseline__mutmut_11 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_12'] = x_pipeline_performance_baseline__mutmut_12 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_13'] = x_pipeline_performance_baseline__mutmut_13 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_14'] = x_pipeline_performance_baseline__mutmut_14 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_15'] = x_pipeline_performance_baseline__mutmut_15 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_16'] = x_pipeline_performance_baseline__mutmut_16 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_17'] = x_pipeline_performance_baseline__mutmut_17 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_18'] = x_pipeline_performance_baseline__mutmut_18 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_19'] = x_pipeline_performance_baseline__mutmut_19 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_20'] = x_pipeline_performance_baseline__mutmut_20 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_21'] = x_pipeline_performance_baseline__mutmut_21 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_22'] = x_pipeline_performance_baseline__mutmut_22 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_23'] = x_pipeline_performance_baseline__mutmut_23 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_24'] = x_pipeline_performance_baseline__mutmut_24 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_25'] = x_pipeline_performance_baseline__mutmut_25 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_26'] = x_pipeline_performance_baseline__mutmut_26 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_27'] = x_pipeline_performance_baseline__mutmut_27 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_28'] = x_pipeline_performance_baseline__mutmut_28 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_29'] = x_pipeline_performance_baseline__mutmut_29 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_30'] = x_pipeline_performance_baseline__mutmut_30 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_31'] = x_pipeline_performance_baseline__mutmut_31 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_32'] = x_pipeline_performance_baseline__mutmut_32 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_33'] = x_pipeline_performance_baseline__mutmut_33 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_34'] = x_pipeline_performance_baseline__mutmut_34 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_35'] = x_pipeline_performance_baseline__mutmut_35 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_36'] = x_pipeline_performance_baseline__mutmut_36 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_37'] = x_pipeline_performance_baseline__mutmut_37 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_38'] = x_pipeline_performance_baseline__mutmut_38 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_39'] = x_pipeline_performance_baseline__mutmut_39 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_40'] = x_pipeline_performance_baseline__mutmut_40 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_41'] = x_pipeline_performance_baseline__mutmut_41 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_42'] = x_pipeline_performance_baseline__mutmut_42 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_43'] = x_pipeline_performance_baseline__mutmut_43 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_44'] = x_pipeline_performance_baseline__mutmut_44 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_45'] = x_pipeline_performance_baseline__mutmut_45 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_46'] = x_pipeline_performance_baseline__mutmut_46 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_47'] = x_pipeline_performance_baseline__mutmut_47 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_48'] = x_pipeline_performance_baseline__mutmut_48 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_49'] = x_pipeline_performance_baseline__mutmut_49 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_50'] = x_pipeline_performance_baseline__mutmut_50 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_51'] = x_pipeline_performance_baseline__mutmut_51 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_52'] = x_pipeline_performance_baseline__mutmut_52 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_53'] = x_pipeline_performance_baseline__mutmut_53 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_54'] = x_pipeline_performance_baseline__mutmut_54 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_55'] = x_pipeline_performance_baseline__mutmut_55 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_56'] = x_pipeline_performance_baseline__mutmut_56 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_57'] = x_pipeline_performance_baseline__mutmut_57 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_58'] = x_pipeline_performance_baseline__mutmut_58 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_59'] = x_pipeline_performance_baseline__mutmut_59 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_60'] = x_pipeline_performance_baseline__mutmut_60 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_61'] = x_pipeline_performance_baseline__mutmut_61 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_62'] = x_pipeline_performance_baseline__mutmut_62 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_63'] = x_pipeline_performance_baseline__mutmut_63 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_64'] = x_pipeline_performance_baseline__mutmut_64 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_65'] = x_pipeline_performance_baseline__mutmut_65 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_66'] = x_pipeline_performance_baseline__mutmut_66 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_67'] = x_pipeline_performance_baseline__mutmut_67 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_68'] = x_pipeline_performance_baseline__mutmut_68 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_69'] = x_pipeline_performance_baseline__mutmut_69 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_70'] = x_pipeline_performance_baseline__mutmut_70 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_71'] = x_pipeline_performance_baseline__mutmut_71 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_72'] = x_pipeline_performance_baseline__mutmut_72 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_73'] = x_pipeline_performance_baseline__mutmut_73 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_74'] = x_pipeline_performance_baseline__mutmut_74 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_75'] = x_pipeline_performance_baseline__mutmut_75 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_76'] = x_pipeline_performance_baseline__mutmut_76 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_77'] = x_pipeline_performance_baseline__mutmut_77 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_78'] = x_pipeline_performance_baseline__mutmut_78 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_79'] = x_pipeline_performance_baseline__mutmut_79 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_80'] = x_pipeline_performance_baseline__mutmut_80 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_81'] = x_pipeline_performance_baseline__mutmut_81 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_82'] = x_pipeline_performance_baseline__mutmut_82 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_83'] = x_pipeline_performance_baseline__mutmut_83 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_84'] = x_pipeline_performance_baseline__mutmut_84 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_85'] = x_pipeline_performance_baseline__mutmut_85 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_86'] = x_pipeline_performance_baseline__mutmut_86 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_87'] = x_pipeline_performance_baseline__mutmut_87 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_88'] = x_pipeline_performance_baseline__mutmut_88 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_89'] = x_pipeline_performance_baseline__mutmut_89 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_90'] = x_pipeline_performance_baseline__mutmut_90 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_91'] = x_pipeline_performance_baseline__mutmut_91 # type: ignore # mutmut generated
mutants_x_pipeline_performance_baseline__mutmut['x_pipeline_performance_baseline__mutmut_92'] = x_pipeline_performance_baseline__mutmut_92 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(pipeline_performance_baseline)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(pipeline_performance_baseline)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
