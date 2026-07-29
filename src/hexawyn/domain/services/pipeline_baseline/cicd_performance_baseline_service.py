from __future__ import annotations

import statistics
from typing import TypedDict

from hexawyn.domain.models.pipeline_baseline import PipelineBaselineResult, StageStats


class PipelineRunRecord(TypedDict):
    name: str
    status: str
    duration_seconds: int | None
    start_time: str | None
    completion_time: str | None


class TaskRunRecord(TypedDict):
    name: str
    task_name: str
    pipeline_run_name: str
    duration_seconds: int | None


_SIGNIFICANT_TREND_PCT = 0.10
_OUTLIER_MULTIPLIER = 2.0


def _parse_stage_name(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower or "test-" in lower or "-test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def _compute_stats(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
        unit="seconds",
    )


def _percentile(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def _detect_outliers(runs: list[PipelineRunRecord], stage_avgs: dict[str, float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for stage, avg in stage_avgs.items():
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def _compute_trend(runs: list[PipelineRunRecord]) -> str:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data"
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data"
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    if first_avg == 0:
        return "insufficient_data"
    delta = (last_avg - first_avg) / first_avg
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def compute_baseline(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            runs_analyzed=0,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            trend="insufficient_data",
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name", "")
        task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = {name: s.avg for name, s in stages.items()}
    if total_stats:
        stage_avgs["_total"] = total_stats.avg
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend = _compute_trend(succeeded)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        note=note,
    )
