from __future__ import annotations

from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
    _extract_failure_reason,
    _extract_pipeline_ref,
    _extract_run_after,
    _extract_status,
    _to_iso,
    _to_pipeline_run_record,
    _to_task_run_record,
)


class TestTracerExtractStatus:
    def test_succeeded(self) -> None:
        assert (
            _extract_status([{"type": "Succeeded", "status": "True", "reason": "Succeeded"}])
            == "Succeeded"
        )

    def test_failed(self) -> None:
        assert (
            _extract_status([{"type": "Succeeded", "status": "False", "reason": "Failed"}])
            == "Failed"
        )

    def test_cancelled_pipeline(self) -> None:
        assert (
            _extract_status(
                [{"type": "Succeeded", "status": "False", "reason": "PipelineRunCancelled"}]
            )
            == "Cancelled"
        )

    def test_running(self) -> None:
        assert (
            _extract_status([{"type": "Succeeded", "status": "Unknown", "reason": "Running"}])
            == "Running"
        )

    def test_pending_is_running(self) -> None:
        assert (
            _extract_status([{"type": "Succeeded", "status": "Unknown", "reason": "Pending"}])
            == "Running"
        )

    def test_not_list_returns_unknown(self) -> None:
        assert _extract_status("bad") == "Unknown"

    def test_empty_list_returns_not_started(self) -> None:
        assert _extract_status([]) == "NotStarted"


class TestExtractFailureReason:
    def test_failed_message(self) -> None:
        status_block = {
            "conditions": [{"type": "Succeeded", "status": "False", "message": "pod crashed"}]
        }
        assert _extract_failure_reason(status_block) == "pod crashed"

    def test_no_failure(self) -> None:
        status_block = {"conditions": [{"type": "Succeeded", "status": "True"}]}
        assert _extract_failure_reason(status_block) == ""

    def test_no_conditions(self) -> None:
        assert _extract_failure_reason({}) == ""


class TestExtractRunAfter:
    def test_run_after_list(self) -> None:
        assert _extract_run_after({"runAfter": ["task-a", "task-b"]}) == ["task-a", "task-b"]

    def test_no_run_after(self) -> None:
        assert _extract_run_after({}) == []

    def test_run_after_not_list(self) -> None:
        assert _extract_run_after({"runAfter": "bad"}) == []


class TestExtractPipelineRef:
    def test_named_ref(self) -> None:
        assert _extract_pipeline_ref({"pipelineRef": {"name": "my-pipe"}}) == "my-pipe"


class TestToPipelineRunRecord:
    def test_minimal(self) -> None:
        record = _to_pipeline_run_record({})
        assert record["name"] == ""
        assert record["status"] == "NotStarted"

    def test_full(self) -> None:
        raw = {
            "metadata": {"name": "pr-1", "namespace": "ci"},
            "status": {
                "startTime": "2026-01-01T00:00:00Z",
                "conditions": [{"type": "Succeeded", "status": "True"}],
            },
            "spec": {"pipelineRef": {"name": "pipeline-1"}},
        }
        record = _to_pipeline_run_record(raw)
        assert record["name"] == "pr-1"
        assert record["status"] == "Succeeded"
        assert record["pipeline_ref"] == "pipeline-1"


class TestToTaskRunRecord:
    def test_minimal(self) -> None:
        record = _to_task_run_record({}, "pr-1")
        assert record["pipeline_run_name"] == "pr-1"
        assert record["status"] == "NotStarted"

    def test_full(self) -> None:
        raw = {
            "metadata": {"name": "task-1", "namespace": "ci"},
            "status": {
                "startTime": "2026-01-01T00:00:00Z",
                "conditions": [{"type": "Succeeded", "status": "True"}],
            },
            "spec": {"runAfter": ["build"]},
        }
        record = _to_task_run_record(raw, "pr-1")
        assert record["name"] == "task-1"
        assert record["run_after"] == ["build"]

    def test_inline_spec(self) -> None:
        assert _extract_pipeline_ref({"pipelineSpec": {"tasks": []}}) == "inline"

    def test_unknown(self) -> None:
        assert _extract_pipeline_ref({}) == "unknown"

    def test_ref_without_name(self) -> None:
        assert _extract_pipeline_ref({"pipelineRef": {"other": "x"}}) == "unknown"


class TestToIso:
    def test_string(self) -> None:
        assert _to_iso("2024-01-01T00:00:00Z") == "2024-01-01T00:00:00Z"

    def test_non_string(self) -> None:
        assert _to_iso(123) is None

    def test_none(self) -> None:
        assert _to_iso(None) is None


class TestToPipelineRunRecord:  # noqa: F811
    def test_basic(self) -> None:
        raw = {
            "metadata": {"name": "run-1", "namespace": "default"},
            "status": {
                "conditions": [{"type": "Succeeded", "status": "True", "reason": "Succeeded"}],
                "startTime": "2024-01-01T00:00:00Z",
                "completionTime": "2024-01-01T00:05:00Z",
            },
            "spec": {"pipelineRef": {"name": "pipeline-a"}},
        }
        result = _to_pipeline_run_record(raw)
        assert result["name"] == "run-1"
        assert result["namespace"] == "default"
        assert result["status"] == "Succeeded"
        assert result["start_time"] == "2024-01-01T00:00:00Z"
        assert result["pipeline_ref"] == "pipeline-a"


class TestToTaskRunRecord:  # noqa: F811
    def test_basic(self) -> None:
        raw = {
            "metadata": {"name": "task-1", "namespace": "default"},
            "status": {
                "conditions": [{"type": "Succeeded", "status": "True", "reason": "Succeeded"}],
                "startTime": "2024-01-01T00:00:00Z",
                "completionTime": "2024-01-01T00:02:00Z",
            },
            "spec": {"runAfter": ["dep-task"]},
        }
        result = _to_task_run_record(raw, "run-1")
        assert result["name"] == "task-1"
        assert result["pipeline_run_name"] == "run-1"
        assert result["status"] == "Succeeded"
        assert result["run_after"] == ["dep-task"]

    def test_failed_task(self) -> None:
        raw = {
            "metadata": {"name": "failed-task", "namespace": "ns"},
            "status": {
                "conditions": [
                    {
                        "type": "Succeeded",
                        "status": "False",
                        "reason": "Failed",
                        "message": "container OOMKilled",
                    }
                ],
            },
            "spec": {},
        }
        result = _to_task_run_record(raw, "run-1")
        assert result["status"] == "Failed"
        assert "OOMKilled" in result["failure_reason"]
