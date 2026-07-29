from __future__ import annotations

from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
    _compute_duration_seconds,
    _extract_pipeline_ref,
    _extract_status,
    _to_record,
)


class TestExtractStatus:
    def test_succeeded(self) -> None:
        status, reason = _extract_status(
            {"conditions": [{"type": "Succeeded", "status": "True", "reason": "Succeeded"}]}
        )
        assert status == "Succeeded"
        assert reason is None

    def test_failed(self) -> None:
        status, reason = _extract_status(
            {"conditions": [{"type": "Succeeded", "status": "False", "reason": "Failed"}]}
        )
        assert status == "Failed"
        assert reason == "Failed"

    def test_cancelled(self) -> None:
        status, reason = _extract_status(
            {"conditions": [{"type": "Succeeded", "status": "False", "reason": "Cancelled"}]}
        )
        assert status == "Cancelled"
        assert reason is None

    def test_running(self) -> None:
        status, _ = _extract_status(
            {"conditions": [{"type": "Succeeded", "status": "Unknown", "reason": "Running"}]}
        )
        assert status == "Running"

    def test_not_started(self) -> None:
        status, _ = _extract_status(
            {"conditions": [{"type": "Succeeded", "status": "Unknown", "reason": "Pending"}]}
        )
        assert status == "NotStarted"

    def test_none_status(self) -> None:
        status, _ = _extract_status(None)
        assert status == "NotStarted"

    def test_empty_conditions(self) -> None:
        status, _ = _extract_status({"conditions": []})
        assert status == "NotStarted"

    def test_conditions_not_list(self) -> None:
        status, _ = _extract_status({"conditions": "bad"})
        assert status == "NotStarted"


class TestComputeDurationSeconds:
    def test_completed_run(self) -> None:
        duration = _compute_duration_seconds("2024-01-01T00:00:00Z", "2024-01-01T00:05:00Z")
        assert duration == 300  # noqa: PLR2004

    def test_none_start_time(self) -> None:
        assert _compute_duration_seconds(None, "2024-01-01T00:05:00Z") is None

    def test_running_run(self) -> None:
        duration = _compute_duration_seconds("2024-01-01T00:00:00Z", None)
        assert duration is not None
        assert duration > 0

    def test_invalid_date(self) -> None:
        assert _compute_duration_seconds("invalid", None) is None


class TestExtractPipelineRef:
    def test_pipeline_ref_with_name(self) -> None:
        spec = {"pipelineRef": {"name": "my-pipeline"}}
        assert _extract_pipeline_ref(spec) == "my-pipeline"

    def test_inline_spec(self) -> None:
        spec = {"pipelineSpec": {"tasks": []}}
        assert _extract_pipeline_ref(spec) == "inline"

    def test_no_ref(self) -> None:
        spec = {"other": "value"}
        assert _extract_pipeline_ref(spec) == "unknown"

    def test_none_spec(self) -> None:
        assert _extract_pipeline_ref(None) == "unknown"

    def test_pipeline_ref_without_name(self) -> None:
        spec = {"pipelineRef": {"other": "value"}}
        assert _extract_pipeline_ref(spec) == "unknown"


class TestToRecord:
    def test_basic_record(self) -> None:
        item = {
            "metadata": {"name": "run-1", "namespace": "default"},
            "spec": {"pipelineRef": {"name": "my-pipeline"}},
            "status": {
                "conditions": [{"type": "Succeeded", "status": "True", "reason": "Succeeded"}],
                "startTime": "2024-01-01T00:00:00Z",
                "completionTime": "2024-01-01T00:05:00Z",
            },
        }
        result = _to_record(item)
        assert result["name"] == "run-1"
        assert result["status"] == "Succeeded"
        assert result["pipeline_ref"] == "my-pipeline"
        assert result["duration_seconds"] == 300  # noqa: PLR2004

    def test_record_no_metadata(self) -> None:
        item = {
            "spec": {"pipelineRef": {"name": "p"}},
            "status": {
                "conditions": [{"type": "Succeeded", "status": "True"}],
            },
        }
        result = _to_record(item)
        assert result["name"] == "unknown"

    def test_record_no_status(self) -> None:
        item = {"metadata": {"name": "run-1"}, "spec": {}}
        result = _to_record(item)
        assert result["status"] == "NotStarted"
