from __future__ import annotations

from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import PipelineRunStats
from hexawyn.domain.models.constants import PIPELINE_OUTLIER_THRESHOLD


def start_time_sort_key(run: dict[str, object]) -> tuple[int, str]:
    start = run.get("start_time", "")
    return (1, str(start)) if start else (0, "")


def compute_pipeline_stats(runs: list[dict[str, object]]) -> PipelineRunStats:
    from hexawyn.domain.models.constants import PIPELINE_CANCELLED_STATUS

    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == PIPELINE_CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated * 100.0) if rated > 0 else 0.0

    timed = [r for r in runs if r["duration_seconds"] is not None]
    if not timed:
        return PipelineRunStats(
            total_runs=total,
            succeeded_runs=succeeded,
            failed_runs=failed,
            cancelled_runs=cancelled,
            success_rate=success_rate,
            average_duration_seconds=None,
            fastest_run_name=None,
            slowest_run_name=None,
        )

    durations = [r["duration_seconds"] for r in timed]
    average = sum(durations) / len(durations)  # type: ignore[arg-type]
    fastest = min(timed, key=lambda r: r["duration_seconds"] or 0)  # type: ignore
    slowest = max(timed, key=lambda r: r["duration_seconds"] or 0)  # type: ignore

    return PipelineRunStats(
        total_runs=total,
        succeeded_runs=succeeded,
        failed_runs=failed,
        cancelled_runs=cancelled,
        success_rate=success_rate,
        average_duration_seconds=average,
        fastest_run_name=fastest["name"],  # type: ignore
        slowest_run_name=slowest["name"],  # type: ignore
    )


def sort_by_status_then_time(
    runs: list[dict[str, object]],
) -> list[dict[str, object]]:
    from hexawyn.domain.models.constants import PIPELINE_RUN_STATUS_PRIORITY

    by_time = sorted(runs, key=lambda r: r.get("start_time") or "", reverse=True)  # type: ignore
    return sorted(
        by_time,
        key=lambda r: PIPELINE_RUN_STATUS_PRIORITY.get(str(r.get("status", "")), 3),
    )


def find_outlier_names(runs: list[dict[str, object]], average: float | None) -> list[str]:
    if average is None:
        return []
    threshold = PIPELINE_OUTLIER_THRESHOLD * average
    return [r["name"] for r in runs if (r["duration_seconds"] or 0) > threshold]  # type: ignore
