from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.tekton_port import NamespacedPipelineRunInfo
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.sort_stuck import (
    find_stuck_runs,
    sort_by_status_then_time,
)


def _make_run(name: str, status: str, start_time: str | None = None) -> NamespacedPipelineRunInfo:
    return NamespacedPipelineRunInfo(
        name=name,
        status=status,
        start_time=start_time,
        duration=None,
        duration_seconds=None,
        pipeline_ref="test-pipeline",
    )


class TestSortByStatusThenTime:
    def test_empty_list(self) -> None:
        result = sort_by_status_then_time([])
        assert result == []

    def test_mixed_statuses(self) -> None:
        runs: list[NamespacedPipelineRunInfo] = [
            _make_run("run-1", "Succeeded", "2024-01-01T10:00:00Z"),
            _make_run("run-2", "Failed", "2024-01-01T09:00:00Z"),
            _make_run("run-3", "Running", "2024-01-01T11:00:00Z"),
            _make_run("run-4", "Failed", "2024-01-01T08:00:00Z"),
        ]

        result = sort_by_status_then_time(runs)

        statuses = [r["status"] for r in result]
        assert statuses == ["Failed", "Failed", "Running", "Succeeded"]
        assert result[0]["name"] == "run-2"
        assert result[1]["name"] == "run-4"

    def test_unrecognized_status_gets_priority_3(self) -> None:
        runs: list[NamespacedPipelineRunInfo] = [
            _make_run("run-1", "Succeeded", "2024-01-01T10:00:00Z"),
            _make_run("run-2", "Canceled", "2024-01-01T09:00:00Z"),
            _make_run("run-3", "Failed", "2024-01-01T08:00:00Z"),
        ]

        result = sort_by_status_then_time(runs)

        statuses = [r["status"] for r in result]
        assert statuses == ["Failed", "Succeeded", "Canceled"]

    def test_start_time_none_sorted_last(self) -> None:
        runs: list[NamespacedPipelineRunInfo] = [
            _make_run("run-1", "Failed", "2024-01-01T10:00:00Z"),
            _make_run("run-2", "Failed", None),
        ]

        result = sort_by_status_then_time(runs)

        assert result[0]["name"] == "run-1"
        assert result[1]["name"] == "run-2"


class TestFindStuckRuns:
    def test_empty_list(self) -> None:
        result = find_stuck_runs([])
        assert result == []

    def test_running_older_than_one_hour_is_stuck(self) -> None:
        stale_time = (datetime.now(UTC) - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
        runs: list[NamespacedPipelineRunInfo] = [
            _make_run("stuck-run", "Running", stale_time),
        ]

        result = find_stuck_runs(runs)

        assert result == ["stuck-run"]

    def test_running_less_than_one_hour_is_not_stuck(self) -> None:
        recent_time = (datetime.now(UTC) - timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
        runs: list[NamespacedPipelineRunInfo] = [
            _make_run("fresh-run", "Running", recent_time),
        ]

        result = find_stuck_runs(runs)

        assert result == []

    def test_all_recent_runs_not_stuck(self) -> None:
        recent_time = (datetime.now(UTC) - timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
        runs: list[NamespacedPipelineRunInfo] = [
            _make_run("run-1", "Running", recent_time),
            _make_run("run-2", "Running", recent_time),
        ]

        result = find_stuck_runs(runs)

        assert result == []

    def test_non_running_status_ignored(self) -> None:
        stale_time = (datetime.now(UTC) - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
        runs: list[NamespacedPipelineRunInfo] = [
            _make_run("failed-run", "Failed", stale_time),
            _make_run("succeeded-run", "Succeeded", stale_time),
        ]

        result = find_stuck_runs(runs)

        assert result == []

    def test_none_start_time_ignored(self) -> None:
        runs: list[NamespacedPipelineRunInfo] = [
            _make_run("running-no-start", "Running", None),
        ]

        result = find_stuck_runs(runs)

        assert result == []

    def test_invalid_date_format_is_ignored(self) -> None:
        runs: list[NamespacedPipelineRunInfo] = [
            _make_run("bad-date-run", "Running", "not-a-date"),
        ]

        result = find_stuck_runs(runs)

        assert result == []
