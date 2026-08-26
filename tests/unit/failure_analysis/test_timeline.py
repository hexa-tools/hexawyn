"""Unit tests for build_pipeline_timeline — pure domain timeline assembly."""

from __future__ import annotations

from hexawyn.application.ports.driven.tekton_port import TaskRunInfo
from hexawyn.domain.models.namespace_event import NamespaceEvent
from hexawyn.domain.models.pipeline_run_logs import StepLog, StepStatus
from hexawyn.domain.services.failure_analysis.timeline import (
    PipelineTimeline,
    build_pipeline_timeline,
)


def _run(  # noqa: PLR0913
    name: str,
    task_ref: str,
    status: str,
    start_time: str | None,
    failing_step: str | None = None,
    failing_step_error: str | None = None,
) -> TaskRunInfo:
    return {
        "name": name,
        "task_ref": task_ref,
        "status": status,
        "start_time": start_time,
        "duration": "10s",
        "failing_step": failing_step,
        "failing_step_error": failing_step_error,
    }


def _event(object_name: str, message: str, event_type: str, last_seen: str) -> NamespaceEvent:
    return NamespaceEvent(
        event_type=event_type,
        reason="Reason",
        message=message,
        object=object_name,
        count=1,
        last_seen=last_seen,
    )


class TestBuildPipelineTimeline:
    def test_empty_inputs_returns_empty_timeline(self) -> None:
        result = build_pipeline_timeline([], [], [], None)

        assert isinstance(result, PipelineTimeline)
        assert result.entries == ()
        assert result.first_failure is None
        assert result.failure_count == 0

    def test_sorts_task_runs_by_timestamp_ascending(self) -> None:
        runs = [
            _run("run-2", "task-b", "Failed", "2024-01-10T16:00:00Z"),
            _run("run-1", "task-a", "Failed", "2024-01-10T15:00:00Z"),
        ]

        result = build_pipeline_timeline([], runs, [], None)

        assert [e.timestamp for e in result.entries] == [
            "2024-01-10T15:00:00Z",
            "2024-01-10T16:00:00Z",
        ]

    def test_missing_timestamps_sort_last(self) -> None:
        step_log = StepLog("build", StepStatus.FAILED, ["boom"], False)
        runs = [_run("run-1", "task-a", "Failed", "2024-01-10T15:00:00Z")]

        result = build_pipeline_timeline([step_log], runs, ["OOMKilled"], None)

        assert [e.timestamp for e in result.entries if e.timestamp] == ["2024-01-10T15:00:00Z"]
        assert [e.timestamp for e in result.entries if e.timestamp is None] == [None, None]

    def test_ties_preserve_provision_order(self) -> None:
        runs = [
            _run("run-1", "task-a", "Failed", "2024-01-10T15:00:00Z", "step-a", "err-a"),
            _run("run-2", "task-b", "Failed", "2024-01-10T15:00:00Z", "step-b", "err-b"),
        ]

        result = build_pipeline_timeline([], runs, [], None)

        assert [e.step_name for e in result.entries] == ["task-a", "task-b"]

    def test_dedup_same_source_message_timestamp(self) -> None:
        runs = [
            _run("run-1", "task-a", "Failed", "2024-01-10T15:00:00Z", failing_step_error="same"),
            _run("run-2", "task-a", "Failed", "2024-01-10T15:00:00Z", failing_step_error="same"),
        ]

        result = build_pipeline_timeline([], runs, [], None)

        assert len(result.entries) == 1

    def test_first_failure_is_earliest_error(self) -> None:
        runs = [
            _run("run-1", "task-a", "Failed", "2024-01-10T15:00:00Z"),
            _run("run-2", "task-b", "Succeeded", "2024-01-10T14:00:00Z"),
        ]

        result = build_pipeline_timeline([], runs, [], None)

        assert result.first_failure is not None
        assert result.first_failure.step_name == "task-a"
        assert result.failure_count == 1

    def test_events_are_included_with_nested_severity(self) -> None:
        events = [_event("pod-a", "Back-off", "Warning", "2024-01-10T14:00:00Z")]

        result = build_pipeline_timeline([], [], [], events)

        assert len(result.entries) == 1
        assert result.entries[0].severity == "warning"

    def test_severity_mapping_for_statuses(self) -> None:
        runs = [
            _run("run-1", "task-a", "Failed", "2024-01-10T15:00:00Z"),
            _run("run-2", "task-b", "Running", "2024-01-10T14:00:00Z"),
            _run("run-3", "task-c", "Succeeded", "2024-01-10T13:00:00Z"),
        ]

        result = build_pipeline_timeline([], runs, [], None)

        by_step = {entry.step_name: entry.severity for entry in result.entries}
        assert by_step["task-a"] == "error"
        assert by_step["task-b"] == "warning"
        assert by_step["task-c"] == "info"

    def test_step_log_message_uses_last_line(self) -> None:
        step_log = StepLog("test", StepStatus.FAILED, ["line-1", "the real error"], False)

        result = build_pipeline_timeline([step_log], [], [], None)

        assert result.entries[0].message == "the real error"
        assert result.entries[0].step_name == "test"
