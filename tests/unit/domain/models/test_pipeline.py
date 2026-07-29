from __future__ import annotations

from hexawyn.domain.models.pipeline import PipelineRunStatusReport, PipelineRunSummary


class TestPipelineRunSummary:
    def test_create(self) -> None:
        s = PipelineRunSummary(
            name="run-1",
            status="Succeeded",
            start_time="2026-01-01T00:00:00Z",
            duration_seconds=120,
            failure_reason=None,
            pipeline_ref="pipeline-abc",
        )
        assert s.name == "run-1"
        assert s.status == "Succeeded"

    def test_defaults(self) -> None:
        s = PipelineRunSummary(
            name="",
            status="",
            start_time=None,
            duration_seconds=None,
            failure_reason=None,
            pipeline_ref="",
        )
        assert s.name == ""


class TestPipelineRunStatusReport:
    def test_create(self) -> None:
        r = PipelineRunStatusReport(namespace="default", window_hours=24, total=10)
        assert r.namespace == "default"
        assert r.window_hours == 24  # noqa: PLR2004
        assert r.total == 10  # noqa: PLR2004
        assert r.running == 0
        assert r.most_recent_failed is None
        assert r.generated_at is not None

    def test_with_failed(self) -> None:
        summary = PipelineRunSummary(
            name="bad",
            status="Failed",
            start_time="2026-01-01T00:00:00Z",
            duration_seconds=60,
            failure_reason="OOM",
            pipeline_ref="p",
        )
        r = PipelineRunStatusReport(
            namespace="ns",
            window_hours=1,
            total=5,
            failed=2,
            most_recent_failed=summary,
        )
        assert r.failed == 2  # noqa: PLR2004
        assert r.most_recent_failed is not None
        assert r.most_recent_failed.name == "bad"

    def test_slowest_run(self) -> None:
        slow = PipelineRunSummary(
            name="slow",
            status="Succeeded",
            start_time="2026-01-01T00:00:00Z",
            duration_seconds=3600,
            failure_reason=None,
            pipeline_ref="p",
        )
        r = PipelineRunStatusReport(
            namespace="ns",
            window_hours=1,
            total=5,
            slowest_run=slow,
        )
        assert r.slowest_run is not None
        assert r.slowest_run.duration_seconds == 3600  # noqa: PLR2004
