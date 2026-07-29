from hexawyn.application.ports.driven.tekton_port import PipelineRunInfo
from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import (
    PipelineRunStats,
)

_OUTLIER_THRESHOLD = 2.0
_CANCELLED_STATUS = "Cancelled"


def start_time_sort_key(run: PipelineRunInfo) -> tuple[int, str]:
    start = run["start_time"]
    return (1, start) if start else (0, "")


def compute_stats(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

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
    fastest = min(timed, key=lambda r: r["duration_seconds"] or 0)
    slowest = max(timed, key=lambda r: r["duration_seconds"] or 0)

    return PipelineRunStats(
        total_runs=total,
        succeeded_runs=succeeded,
        failed_runs=failed,
        cancelled_runs=cancelled,
        success_rate=success_rate,
        average_duration_seconds=average,
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def find_outliers(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is None:
        return []
    threshold = _OUTLIER_THRESHOLD * average
    return [r["name"] for r in runs if (r["duration_seconds"] or 0) > threshold]
