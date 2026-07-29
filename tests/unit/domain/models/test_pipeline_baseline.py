"""RED → GREEN — Pipeline performance baseline domain models."""

from hexawyn.domain.models.pipeline_baseline import PipelineBaselineResult, StageStats


class TestStageStats:
    def test_defaults(self) -> None:
        s = StageStats()
        assert s.avg == 0.0
        assert s.p50 == 0.0
        assert s.p95 == 0.0
        assert s.max == 0.0
        assert s.unit == "seconds"

    def test_full_construction(self) -> None:
        s = StageStats(avg=135.0, p50=120.0, p95=220.0, max=310.0, unit="seconds")
        assert s.avg == 135.0  # noqa: PLR2004
        assert s.p50 == 120.0  # noqa: PLR2004
        assert s.p95 == 220.0  # noqa: PLR2004
        assert s.max == 310.0  # noqa: PLR2004
        assert s.unit == "seconds"

    def test_is_frozen(self) -> None:
        import pytest

        s = StageStats(avg=100.0)
        with pytest.raises(Exception):
            s.avg = 200.0  # type: ignore[misc]


class TestPipelineBaselineResult:
    def test_default_values(self) -> None:
        r = PipelineBaselineResult()
        assert r.pipeline == ""
        assert r.runs_analyzed == 0
        assert r.requested_limit == 30  # noqa: PLR2004
        assert r.stages == {}
        assert r.total_duration is None
        assert r.outliers == []
        assert r.excluded_running == 0
        assert r.excluded_failed == 0
        assert r.trend == "insufficient_data"
        assert r.note == ""

    def test_full_baseline(self) -> None:
        stages = {
            "build": StageStats(avg=135.0, p50=120.0, p95=220.0, max=310.0),
            "test": StageStats(avg=90.0, p50=85.0, p95=150.0, max=260.0),
            "deploy": StageStats(avg=45.0, p50=40.0, p95=70.0, max=120.0),
        }
        r = PipelineBaselineResult(
            pipeline="payment-service",
            runs_analyzed=30,
            requested_limit=30,
            stages=stages,
            total_duration=StageStats(avg=270.0, p50=260.0, p95=400.0, max=600.0),
            outliers=["run-17", "run-28"],
            excluded_running=3,
            excluded_failed=2,
            trend="stable",
            note="Only 28 runs had completionTime",
        )
        assert r.pipeline == "payment-service"
        assert r.runs_analyzed == 30  # noqa: PLR2004
        assert len(r.stages) == 3  # noqa: PLR2004
        assert r.stages["build"].avg == 135.0  # noqa: PLR2004
        assert r.total_duration is not None
        assert r.total_duration.max == 600.0  # noqa: PLR2004
        assert r.outliers == ["run-17", "run-28"]
        assert r.trend == "stable"
        assert r.note == "Only 28 runs had completionTime"
