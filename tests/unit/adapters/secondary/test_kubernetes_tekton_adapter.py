from __future__ import annotations

from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
    _compute_duration_seconds,
    _extract_pipeline_ref,
    _extract_status,
    _to_record,
)


class TestExtractStatus:
    def test_none(self) -> None:
        assert _extract_status(None) == ("NotStarted", None)

    def test_succeeded(self) -> None:
        assert _extract_status({"conditions": [{"status": "True", "reason": ""}]}) == (
            "Succeeded",
            None,
        )

    def test_failed(self) -> None:
        assert _extract_status({"conditions": [{"status": "False", "reason": "OOM"}]}) == (
            "Failed",
            "OOM",
        )

    def test_cancelled(self) -> None:
        assert _extract_status(
            {"conditions": [{"status": "False", "reason": "PipelineRunCancelled"}]}
        ) == ("Cancelled", None)

    def test_running(self) -> None:
        assert _extract_status({"conditions": [{"status": "Unknown", "reason": "Running"}]}) == (
            "Running",
            None,
        )

    def test_empty_conditions(self) -> None:
        assert _extract_status({"conditions": []}) == ("NotStarted", None)

    def test_no_conditions(self) -> None:
        assert _extract_status({}) == ("NotStarted", None)

    def test_not_list(self) -> None:
        assert _extract_status({"conditions": "bad"}) == ("NotStarted", None)


class TestComputeDuration:
    def test_none_start(self) -> None:
        assert _compute_duration_seconds(None, "2026-01-01T00:00:00Z") is None

    def test_no_completion(self) -> None:
        result = _compute_duration_seconds("2026-01-01T00:00:00Z", None)
        assert result is not None
        assert result > 0

    def test_valid(self) -> None:
        result = _compute_duration_seconds("2026-01-01T00:00:00Z", "2026-01-01T00:05:00Z")
        assert result == 300  # noqa: PLR2004

    def test_invalid_format(self) -> None:
        assert _compute_duration_seconds("bad-date", "bad-date") is None


class TestExtractPipelineRef:
    def test_none(self) -> None:
        assert _extract_pipeline_ref(None) == "unknown"

    def test_with_name(self) -> None:
        assert _extract_pipeline_ref({"pipelineRef": {"name": "my-pipeline"}}) == "my-pipeline"

    def test_inline(self) -> None:
        assert _extract_pipeline_ref({"pipelineSpec": {}}) == "inline"

    def test_empty_name(self) -> None:
        assert _extract_pipeline_ref({"pipelineRef": {"name": ""}}) == "unknown"

    def test_no_pipeline(self) -> None:
        assert _extract_pipeline_ref({}) == "unknown"


class TestToRecord:
    def test_minimal(self) -> None:
        record = _to_record({})
        assert record["name"] == "unknown"
        assert record["status"] == "NotStarted"

    def test_full(self) -> None:
        item = {
            "metadata": {
                "name": "my-run",
                "namespace": "ns",
                "creationTimestamp": "2026-01-01T00:00:00Z",
            },
            "spec": {"pipelineRef": {"name": "pipeline-1"}},
            "status": {"conditions": [{"status": "True", "reason": "Succeeded"}]},
        }
        record = _to_record(item)
        assert record["name"] == "my-run"
        assert record["status"] == "Succeeded"
        assert record["pipeline_ref"] == "pipeline-1"
