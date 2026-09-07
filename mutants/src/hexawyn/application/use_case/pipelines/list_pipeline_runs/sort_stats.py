from hexawyn.application.ports.driven.tekton_port import PipelineRunInfo
from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import (
    PipelineRunStats,
)

_OUTLIER_THRESHOLD = 2.0
_CANCELLED_STATUS = "Cancelled"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_start_time_sort_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_start_time_sort_key__mutmut)
def start_time_sort_key(run: PipelineRunInfo) -> tuple[int, str]:
    start = run["start_time"]
    return (1, start) if start else (0, "")


def x_start_time_sort_key__mutmut_orig(run: PipelineRunInfo) -> tuple[int, str]:
    start = run["start_time"]
    return (1, start) if start else (0, "")


def x_start_time_sort_key__mutmut_1(run: PipelineRunInfo) -> tuple[int, str]:
    start = None
    return (1, start) if start else (0, "")


def x_start_time_sort_key__mutmut_2(run: PipelineRunInfo) -> tuple[int, str]:
    start = run["XXstart_timeXX"]
    return (1, start) if start else (0, "")


def x_start_time_sort_key__mutmut_3(run: PipelineRunInfo) -> tuple[int, str]:
    start = run["START_TIME"]
    return (1, start) if start else (0, "")


def x_start_time_sort_key__mutmut_4(run: PipelineRunInfo) -> tuple[int, str]:
    start = run["start_time"]
    return (2, start) if start else (0, "")


def x_start_time_sort_key__mutmut_5(run: PipelineRunInfo) -> tuple[int, str]:
    start = run["start_time"]
    return (1, start) if start else (1, "")


def x_start_time_sort_key__mutmut_6(run: PipelineRunInfo) -> tuple[int, str]:
    start = run["start_time"]
    return (1, start) if start else (0, "XXXX")

mutants_x_start_time_sort_key__mutmut['_mutmut_orig'] = x_start_time_sort_key__mutmut_orig # type: ignore # mutmut generated
mutants_x_start_time_sort_key__mutmut['x_start_time_sort_key__mutmut_1'] = x_start_time_sort_key__mutmut_1 # type: ignore # mutmut generated
mutants_x_start_time_sort_key__mutmut['x_start_time_sort_key__mutmut_2'] = x_start_time_sort_key__mutmut_2 # type: ignore # mutmut generated
mutants_x_start_time_sort_key__mutmut['x_start_time_sort_key__mutmut_3'] = x_start_time_sort_key__mutmut_3 # type: ignore # mutmut generated
mutants_x_start_time_sort_key__mutmut['x_start_time_sort_key__mutmut_4'] = x_start_time_sort_key__mutmut_4 # type: ignore # mutmut generated
mutants_x_start_time_sort_key__mutmut['x_start_time_sort_key__mutmut_5'] = x_start_time_sort_key__mutmut_5 # type: ignore # mutmut generated
mutants_x_start_time_sort_key__mutmut['x_start_time_sort_key__mutmut_6'] = x_start_time_sort_key__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_stats__mutmut)
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


def x_compute_stats__mutmut_orig(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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


def x_compute_stats__mutmut_1(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = None
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


def x_compute_stats__mutmut_2(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = None
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


def x_compute_stats__mutmut_3(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(None)
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


def x_compute_stats__mutmut_4(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(2 for r in runs if r["status"] == "Succeeded")
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


def x_compute_stats__mutmut_5(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["XXstatusXX"] == "Succeeded")
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


def x_compute_stats__mutmut_6(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["STATUS"] == "Succeeded")
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


def x_compute_stats__mutmut_7(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] != "Succeeded")
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


def x_compute_stats__mutmut_8(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "XXSucceededXX")
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


def x_compute_stats__mutmut_9(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "succeeded")
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


def x_compute_stats__mutmut_10(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "SUCCEEDED")
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


def x_compute_stats__mutmut_11(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = None
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


def x_compute_stats__mutmut_12(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(None)
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


def x_compute_stats__mutmut_13(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(2 for r in runs if r["status"] == "Failed")
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


def x_compute_stats__mutmut_14(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["XXstatusXX"] == "Failed")
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


def x_compute_stats__mutmut_15(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["STATUS"] == "Failed")
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


def x_compute_stats__mutmut_16(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] != "Failed")
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


def x_compute_stats__mutmut_17(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "XXFailedXX")
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


def x_compute_stats__mutmut_18(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "failed")
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


def x_compute_stats__mutmut_19(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "FAILED")
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


def x_compute_stats__mutmut_20(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = None

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


def x_compute_stats__mutmut_21(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(None)

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


def x_compute_stats__mutmut_22(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(2 for r in runs if r["status"] == _CANCELLED_STATUS)

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


def x_compute_stats__mutmut_23(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["XXstatusXX"] == _CANCELLED_STATUS)

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


def x_compute_stats__mutmut_24(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["STATUS"] == _CANCELLED_STATUS)

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


def x_compute_stats__mutmut_25(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] != _CANCELLED_STATUS)

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


def x_compute_stats__mutmut_26(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = None
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


def x_compute_stats__mutmut_27(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded - failed
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


def x_compute_stats__mutmut_28(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = None

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


def x_compute_stats__mutmut_29(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated / 100.0) if rated > 0 else 0.0

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


def x_compute_stats__mutmut_30(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded * rated * 100.0) if rated > 0 else 0.0

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


def x_compute_stats__mutmut_31(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated * 101.0) if rated > 0 else 0.0

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


def x_compute_stats__mutmut_32(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated * 100.0) if rated >= 0 else 0.0

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


def x_compute_stats__mutmut_33(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated * 100.0) if rated > 1 else 0.0

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


def x_compute_stats__mutmut_34(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated * 100.0) if rated > 0 else 1.0

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


def x_compute_stats__mutmut_35(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated * 100.0) if rated > 0 else 0.0

    timed = None
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


def x_compute_stats__mutmut_36(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated * 100.0) if rated > 0 else 0.0

    timed = [r for r in runs if r["XXduration_secondsXX"] is not None]
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


def x_compute_stats__mutmut_37(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated * 100.0) if rated > 0 else 0.0

    timed = [r for r in runs if r["DURATION_SECONDS"] is not None]
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


def x_compute_stats__mutmut_38(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated * 100.0) if rated > 0 else 0.0

    timed = [r for r in runs if r["duration_seconds"] is None]
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


def x_compute_stats__mutmut_39(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated * 100.0) if rated > 0 else 0.0

    timed = [r for r in runs if r["duration_seconds"] is not None]
    if timed:
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


def x_compute_stats__mutmut_40(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated * 100.0) if rated > 0 else 0.0

    timed = [r for r in runs if r["duration_seconds"] is not None]
    if not timed:
        return PipelineRunStats(
            total_runs=None,
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


def x_compute_stats__mutmut_41(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
            succeeded_runs=None,
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


def x_compute_stats__mutmut_42(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
            failed_runs=None,
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


def x_compute_stats__mutmut_43(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
            cancelled_runs=None,
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


def x_compute_stats__mutmut_44(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
            success_rate=None,
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


def x_compute_stats__mutmut_45(runs: list[PipelineRunInfo]) -> PipelineRunStats:
    total = len(runs)
    succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
    failed = sum(1 for r in runs if r["status"] == "Failed")
    cancelled = sum(1 for r in runs if r["status"] == _CANCELLED_STATUS)

    rated = succeeded + failed
    success_rate = (succeeded / rated * 100.0) if rated > 0 else 0.0

    timed = [r for r in runs if r["duration_seconds"] is not None]
    if not timed:
        return PipelineRunStats(
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


def x_compute_stats__mutmut_46(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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


def x_compute_stats__mutmut_47(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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


def x_compute_stats__mutmut_48(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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


def x_compute_stats__mutmut_49(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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


def x_compute_stats__mutmut_50(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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


def x_compute_stats__mutmut_51(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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


def x_compute_stats__mutmut_52(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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


def x_compute_stats__mutmut_53(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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

    durations = None
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


def x_compute_stats__mutmut_54(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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

    durations = [r["XXduration_secondsXX"] for r in timed]
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


def x_compute_stats__mutmut_55(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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

    durations = [r["DURATION_SECONDS"] for r in timed]
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


def x_compute_stats__mutmut_56(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    average = None  # type: ignore[arg-type]
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


def x_compute_stats__mutmut_57(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    average = sum(durations) * len(durations)  # type: ignore[arg-type]
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


def x_compute_stats__mutmut_58(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    average = sum(None) / len(durations)  # type: ignore[arg-type]
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


def x_compute_stats__mutmut_59(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    fastest = None
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


def x_compute_stats__mutmut_60(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    fastest = min(None, key=lambda r: r["duration_seconds"] or 0)
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


def x_compute_stats__mutmut_61(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    fastest = min(timed, key=None)
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


def x_compute_stats__mutmut_62(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    fastest = min(key=lambda r: r["duration_seconds"] or 0)
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


def x_compute_stats__mutmut_63(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    fastest = min(timed, )
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


def x_compute_stats__mutmut_64(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    fastest = min(timed, key=lambda r: None)
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


def x_compute_stats__mutmut_65(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    fastest = min(timed, key=lambda r: r["duration_seconds"] and 0)
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


def x_compute_stats__mutmut_66(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    fastest = min(timed, key=lambda r: r["XXduration_secondsXX"] or 0)
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


def x_compute_stats__mutmut_67(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    fastest = min(timed, key=lambda r: r["DURATION_SECONDS"] or 0)
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


def x_compute_stats__mutmut_68(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    fastest = min(timed, key=lambda r: r["duration_seconds"] or 1)
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


def x_compute_stats__mutmut_69(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    slowest = None

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


def x_compute_stats__mutmut_70(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    slowest = max(None, key=lambda r: r["duration_seconds"] or 0)

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


def x_compute_stats__mutmut_71(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    slowest = max(timed, key=None)

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


def x_compute_stats__mutmut_72(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    slowest = max(key=lambda r: r["duration_seconds"] or 0)

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


def x_compute_stats__mutmut_73(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    slowest = max(timed, )

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


def x_compute_stats__mutmut_74(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    slowest = max(timed, key=lambda r: None)

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


def x_compute_stats__mutmut_75(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    slowest = max(timed, key=lambda r: r["duration_seconds"] and 0)

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


def x_compute_stats__mutmut_76(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    slowest = max(timed, key=lambda r: r["XXduration_secondsXX"] or 0)

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


def x_compute_stats__mutmut_77(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    slowest = max(timed, key=lambda r: r["DURATION_SECONDS"] or 0)

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


def x_compute_stats__mutmut_78(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
    slowest = max(timed, key=lambda r: r["duration_seconds"] or 1)

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


def x_compute_stats__mutmut_79(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        total_runs=None,
        succeeded_runs=succeeded,
        failed_runs=failed,
        cancelled_runs=cancelled,
        success_rate=success_rate,
        average_duration_seconds=average,
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_80(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        succeeded_runs=None,
        failed_runs=failed,
        cancelled_runs=cancelled,
        success_rate=success_rate,
        average_duration_seconds=average,
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_81(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        failed_runs=None,
        cancelled_runs=cancelled,
        success_rate=success_rate,
        average_duration_seconds=average,
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_82(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        cancelled_runs=None,
        success_rate=success_rate,
        average_duration_seconds=average,
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_83(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        success_rate=None,
        average_duration_seconds=average,
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_84(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        average_duration_seconds=None,
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_85(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        fastest_run_name=None,
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_86(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        slowest_run_name=None,
    )


def x_compute_stats__mutmut_87(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        succeeded_runs=succeeded,
        failed_runs=failed,
        cancelled_runs=cancelled,
        success_rate=success_rate,
        average_duration_seconds=average,
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_88(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        failed_runs=failed,
        cancelled_runs=cancelled,
        success_rate=success_rate,
        average_duration_seconds=average,
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_89(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        cancelled_runs=cancelled,
        success_rate=success_rate,
        average_duration_seconds=average,
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_90(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        success_rate=success_rate,
        average_duration_seconds=average,
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_91(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        average_duration_seconds=average,
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_92(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        fastest_run_name=fastest["name"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_93(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_94(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        )


def x_compute_stats__mutmut_95(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        fastest_run_name=fastest["XXnameXX"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_96(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        fastest_run_name=fastest["NAME"],
        slowest_run_name=slowest["name"],
    )


def x_compute_stats__mutmut_97(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        slowest_run_name=slowest["XXnameXX"],
    )


def x_compute_stats__mutmut_98(runs: list[PipelineRunInfo]) -> PipelineRunStats:
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
        slowest_run_name=slowest["NAME"],
    )

mutants_x_compute_stats__mutmut['_mutmut_orig'] = x_compute_stats__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_1'] = x_compute_stats__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_2'] = x_compute_stats__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_3'] = x_compute_stats__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_4'] = x_compute_stats__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_5'] = x_compute_stats__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_6'] = x_compute_stats__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_7'] = x_compute_stats__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_8'] = x_compute_stats__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_9'] = x_compute_stats__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_10'] = x_compute_stats__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_11'] = x_compute_stats__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_12'] = x_compute_stats__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_13'] = x_compute_stats__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_14'] = x_compute_stats__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_15'] = x_compute_stats__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_16'] = x_compute_stats__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_17'] = x_compute_stats__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_18'] = x_compute_stats__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_19'] = x_compute_stats__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_20'] = x_compute_stats__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_21'] = x_compute_stats__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_22'] = x_compute_stats__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_23'] = x_compute_stats__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_24'] = x_compute_stats__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_25'] = x_compute_stats__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_26'] = x_compute_stats__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_27'] = x_compute_stats__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_28'] = x_compute_stats__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_29'] = x_compute_stats__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_30'] = x_compute_stats__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_31'] = x_compute_stats__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_32'] = x_compute_stats__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_33'] = x_compute_stats__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_34'] = x_compute_stats__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_35'] = x_compute_stats__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_36'] = x_compute_stats__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_37'] = x_compute_stats__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_38'] = x_compute_stats__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_39'] = x_compute_stats__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_40'] = x_compute_stats__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_41'] = x_compute_stats__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_42'] = x_compute_stats__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_43'] = x_compute_stats__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_44'] = x_compute_stats__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_45'] = x_compute_stats__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_46'] = x_compute_stats__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_47'] = x_compute_stats__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_48'] = x_compute_stats__mutmut_48 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_49'] = x_compute_stats__mutmut_49 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_50'] = x_compute_stats__mutmut_50 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_51'] = x_compute_stats__mutmut_51 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_52'] = x_compute_stats__mutmut_52 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_53'] = x_compute_stats__mutmut_53 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_54'] = x_compute_stats__mutmut_54 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_55'] = x_compute_stats__mutmut_55 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_56'] = x_compute_stats__mutmut_56 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_57'] = x_compute_stats__mutmut_57 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_58'] = x_compute_stats__mutmut_58 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_59'] = x_compute_stats__mutmut_59 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_60'] = x_compute_stats__mutmut_60 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_61'] = x_compute_stats__mutmut_61 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_62'] = x_compute_stats__mutmut_62 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_63'] = x_compute_stats__mutmut_63 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_64'] = x_compute_stats__mutmut_64 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_65'] = x_compute_stats__mutmut_65 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_66'] = x_compute_stats__mutmut_66 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_67'] = x_compute_stats__mutmut_67 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_68'] = x_compute_stats__mutmut_68 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_69'] = x_compute_stats__mutmut_69 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_70'] = x_compute_stats__mutmut_70 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_71'] = x_compute_stats__mutmut_71 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_72'] = x_compute_stats__mutmut_72 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_73'] = x_compute_stats__mutmut_73 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_74'] = x_compute_stats__mutmut_74 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_75'] = x_compute_stats__mutmut_75 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_76'] = x_compute_stats__mutmut_76 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_77'] = x_compute_stats__mutmut_77 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_78'] = x_compute_stats__mutmut_78 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_79'] = x_compute_stats__mutmut_79 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_80'] = x_compute_stats__mutmut_80 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_81'] = x_compute_stats__mutmut_81 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_82'] = x_compute_stats__mutmut_82 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_83'] = x_compute_stats__mutmut_83 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_84'] = x_compute_stats__mutmut_84 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_85'] = x_compute_stats__mutmut_85 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_86'] = x_compute_stats__mutmut_86 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_87'] = x_compute_stats__mutmut_87 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_88'] = x_compute_stats__mutmut_88 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_89'] = x_compute_stats__mutmut_89 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_90'] = x_compute_stats__mutmut_90 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_91'] = x_compute_stats__mutmut_91 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_92'] = x_compute_stats__mutmut_92 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_93'] = x_compute_stats__mutmut_93 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_94'] = x_compute_stats__mutmut_94 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_95'] = x_compute_stats__mutmut_95 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_96'] = x_compute_stats__mutmut_96 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_97'] = x_compute_stats__mutmut_97 # type: ignore # mutmut generated
mutants_x_compute_stats__mutmut['x_compute_stats__mutmut_98'] = x_compute_stats__mutmut_98 # type: ignore # mutmut generated
mutants_x_find_outliers__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_find_outliers__mutmut)
def find_outliers(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is None:
        return []
    threshold = _OUTLIER_THRESHOLD * average
    return [r["name"] for r in runs if (r["duration_seconds"] or 0) > threshold]


def x_find_outliers__mutmut_orig(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is None:
        return []
    threshold = _OUTLIER_THRESHOLD * average
    return [r["name"] for r in runs if (r["duration_seconds"] or 0) > threshold]


def x_find_outliers__mutmut_1(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is not None:
        return []
    threshold = _OUTLIER_THRESHOLD * average
    return [r["name"] for r in runs if (r["duration_seconds"] or 0) > threshold]


def x_find_outliers__mutmut_2(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is None:
        return []
    threshold = None
    return [r["name"] for r in runs if (r["duration_seconds"] or 0) > threshold]


def x_find_outliers__mutmut_3(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is None:
        return []
    threshold = _OUTLIER_THRESHOLD / average
    return [r["name"] for r in runs if (r["duration_seconds"] or 0) > threshold]


def x_find_outliers__mutmut_4(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is None:
        return []
    threshold = _OUTLIER_THRESHOLD * average
    return [r["XXnameXX"] for r in runs if (r["duration_seconds"] or 0) > threshold]


def x_find_outliers__mutmut_5(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is None:
        return []
    threshold = _OUTLIER_THRESHOLD * average
    return [r["NAME"] for r in runs if (r["duration_seconds"] or 0) > threshold]


def x_find_outliers__mutmut_6(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is None:
        return []
    threshold = _OUTLIER_THRESHOLD * average
    return [r["name"] for r in runs if (r["duration_seconds"] and 0) > threshold]


def x_find_outliers__mutmut_7(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is None:
        return []
    threshold = _OUTLIER_THRESHOLD * average
    return [r["name"] for r in runs if (r["XXduration_secondsXX"] or 0) > threshold]


def x_find_outliers__mutmut_8(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is None:
        return []
    threshold = _OUTLIER_THRESHOLD * average
    return [r["name"] for r in runs if (r["DURATION_SECONDS"] or 0) > threshold]


def x_find_outliers__mutmut_9(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is None:
        return []
    threshold = _OUTLIER_THRESHOLD * average
    return [r["name"] for r in runs if (r["duration_seconds"] or 1) > threshold]


def x_find_outliers__mutmut_10(
    runs: list[PipelineRunInfo],
    average: float | None,
) -> list[str]:
    if average is None:
        return []
    threshold = _OUTLIER_THRESHOLD * average
    return [r["name"] for r in runs if (r["duration_seconds"] or 0) >= threshold]

mutants_x_find_outliers__mutmut['_mutmut_orig'] = x_find_outliers__mutmut_orig # type: ignore # mutmut generated
mutants_x_find_outliers__mutmut['x_find_outliers__mutmut_1'] = x_find_outliers__mutmut_1 # type: ignore # mutmut generated
mutants_x_find_outliers__mutmut['x_find_outliers__mutmut_2'] = x_find_outliers__mutmut_2 # type: ignore # mutmut generated
mutants_x_find_outliers__mutmut['x_find_outliers__mutmut_3'] = x_find_outliers__mutmut_3 # type: ignore # mutmut generated
mutants_x_find_outliers__mutmut['x_find_outliers__mutmut_4'] = x_find_outliers__mutmut_4 # type: ignore # mutmut generated
mutants_x_find_outliers__mutmut['x_find_outliers__mutmut_5'] = x_find_outliers__mutmut_5 # type: ignore # mutmut generated
mutants_x_find_outliers__mutmut['x_find_outliers__mutmut_6'] = x_find_outliers__mutmut_6 # type: ignore # mutmut generated
mutants_x_find_outliers__mutmut['x_find_outliers__mutmut_7'] = x_find_outliers__mutmut_7 # type: ignore # mutmut generated
mutants_x_find_outliers__mutmut['x_find_outliers__mutmut_8'] = x_find_outliers__mutmut_8 # type: ignore # mutmut generated
mutants_x_find_outliers__mutmut['x_find_outliers__mutmut_9'] = x_find_outliers__mutmut_9 # type: ignore # mutmut generated
mutants_x_find_outliers__mutmut['x_find_outliers__mutmut_10'] = x_find_outliers__mutmut_10 # type: ignore # mutmut generated
