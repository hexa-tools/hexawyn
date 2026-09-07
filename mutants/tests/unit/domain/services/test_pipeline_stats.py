from __future__ import annotations

from hexawyn.domain.services.pipeline.pipeline_stats import (
    compute_pipeline_stats,
    find_outlier_names,
    sort_by_status_then_time,
    start_time_sort_key,
)


def _run(
    name: str = "run-1",
    status: str = "Succeeded",
    start_time: str | None = "2026-01-01T00:00:00Z",
    duration_seconds: float | None = 60.0,
) -> dict[str, object]:
    return {
        "name": name,
        "status": status,
        "start_time": start_time,
        "duration_seconds": duration_seconds,
    }


class TestStartTimeSortKey:
    def test_with_start_time_returns_one_and_time(self) -> None:
        key = start_time_sort_key({"start_time": "2026-01-01"})
        assert key[0] == 1
        assert key[1] == "2026-01-01"

    def test_without_start_time_returns_zero_and_empty(self) -> None:
        key = start_time_sort_key({})
        assert key[0] == 0
        assert key[1] == ""


class TestComputePipelineStats:
    def test_basic_stats(self) -> None:
        runs = [
            _run("run-1", "Succeeded", duration_seconds=60.0),
            _run("run-2", "Failed", duration_seconds=30.0),
            _run("run-3", "Succeeded", duration_seconds=90.0),
        ]
        stats = compute_pipeline_stats(runs)
        assert stats.total_runs == 3  # noqa: PLR2004
        assert stats.succeeded_runs == 2  # noqa: PLR2004
        assert stats.failed_runs == 1
        assert stats.average_duration_seconds == 60.0  # noqa: PLR2004
        assert stats.fastest_run_name == "run-2"
        assert stats.slowest_run_name == "run-3"

    def test_empty_runs(self) -> None:
        runs: list[dict[str, object]] = []
        stats = compute_pipeline_stats(runs)
        assert stats.total_runs == 0
        assert stats.average_duration_seconds is None

    def test_all_without_duration(self) -> None:
        runs = [
            _run("run-1", duration_seconds=None),
            _run("run-2", duration_seconds=None),
        ]
        stats = compute_pipeline_stats(runs)
        assert stats.average_duration_seconds is None
        assert stats.fastest_run_name is None
        assert stats.slowest_run_name is None

    def test_success_rate_computed(self) -> None:
        runs = [
            _run("a", "Succeeded"),
            _run("b", "Succeeded"),
            _run("c", "Succeeded"),
            _run("d", "Failed"),
        ]
        stats = compute_pipeline_stats(runs)
        assert stats.success_rate == 75.0  # noqa: PLR2004

    def test_cancelled_runs_counted(self) -> None:
        runs = [
            _run("a", "Succeeded"),
            _run("b", "Cancelled"),
        ]
        stats = compute_pipeline_stats(runs)
        assert stats.cancelled_runs == 1

    def test_zero_rated_returns_zero_success_rate(self) -> None:
        runs = [_run("a", "Cancelled")]
        stats = compute_pipeline_stats(runs)
        assert stats.success_rate == 0.0


class TestSortByStatusThenTime:
    def test_sorts_by_status_priority_then_time(self) -> None:
        runs = [
            _run("a", "Succeeded", start_time="2026-01-01T03:00:00Z"),
            _run("b", "Failed", start_time="2026-01-01T01:00:00Z"),
            _run("c", "Failed", start_time="2026-01-01T02:00:00Z"),
            _run("d", "Succeeded", start_time="2026-01-01T04:00:00Z"),
        ]
        sorted_runs = sort_by_status_then_time(runs)
        assert sorted_runs[0]["name"] in ("c", "b")

    def test_missing_status_ranks_low(self) -> None:
        runs = [
            {"name": "x", "status": "Failed", "start_time": "2026-01-01"},
            {"name": "y", "start_time": "2026-01-01"},
        ]
        sorted_runs = sort_by_status_then_time(runs)
        assert sorted_runs[0]["name"] == "x"


class TestFindOutlierNames:
    def test_finds_outliers_above_threshold(self) -> None:
        runs = [
            _run("fast", duration_seconds=10.0),
            _run("slow", duration_seconds=400.0),
        ]
        outliers = find_outlier_names(runs, average=100.0)
        assert "slow" in outliers
        assert "fast" not in outliers

    def test_none_average_returns_empty(self) -> None:
        runs = [_run("a", duration_seconds=999.0)]
        outliers = find_outlier_names(runs, average=None)
        assert outliers == []

    def test_no_outliers(self) -> None:
        runs = [
            _run("a", duration_seconds=50.0),
            _run("b", duration_seconds=60.0),
        ]
        outliers = find_outlier_names(runs, average=100.0)
        assert outliers == []
