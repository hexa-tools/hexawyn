"""RED → GREEN — CICD performance baseline domain service."""

from __future__ import annotations

from hexawyn.domain.services.pipeline_baseline.cicd_performance_baseline_service import (
    PipelineRunRecord,
    TaskRunRecord,
    _worst_degrading_stage,
    compute_baseline,
)


def _make_run(
    name: str,
    status: str = "succeeded",
    duration: int | None = 300,
    completion: str | None = "2024-01-01T00:10:00Z",
    start: str | None = "2024-01-01T00:05:00Z",
) -> PipelineRunRecord:
    return {
        "name": name,
        "status": status,
        "duration_seconds": duration,
        "start_time": start,
        "completion_time": completion,
    }


def _make_task(
    name: str, task_name: str = "build", pipeline_run_name: str = "run-1", duration: int = 120
) -> TaskRunRecord:
    return {
        "name": name,
        "task_name": task_name,
        "pipeline_run_name": pipeline_run_name,
        "duration_seconds": duration,
    }


class TestComputeBaselineHappyPath:
    def test_stable_30_runs_returns_correct_baseline(self) -> None:
        runs = [_make_run(f"run-{i}", duration=240 + i) for i in range(1, 31)]
        tasks = []
        for i in range(1, 31):
            tasks.append(_make_task(f"build-{i}", "build", f"run-{i}", 120))
            tasks.append(_make_task(f"test-{i}", "test", f"run-{i}", 80))
            tasks.append(_make_task(f"deploy-{i}", "deploy", f"run-{i}", 40))

        result = compute_baseline("payment-service", runs, tasks)
        assert result.pipeline == "payment-service"
        assert result.runs_analyzed == 30  # noqa: PLR2004
        assert "build" in result.stages
        assert "test" in result.stages
        assert "deploy" in result.stages
        assert result.stages["build"].avg > 0
        assert result.trend in ("stable", "improving", "degrading")

    def test_p50_p95_max_computed_correctly(self) -> None:
        runs = [_make_run(f"run-{i}", duration=100 + i * 10) for i in range(1, 11)]
        result = compute_baseline("svc", runs, [])
        assert result.total_duration is not None
        assert result.total_duration.p50 > 0
        assert result.total_duration.p95 >= result.total_duration.p50
        assert result.total_duration.max >= result.total_duration.p95

    def test_happy_path_returns_all_keys(self) -> None:
        runs = [_make_run(f"run-{i}", duration=300) for i in range(1, 6)]
        result = compute_baseline("svc", runs, [])
        assert isinstance(result.pipeline, str)
        assert isinstance(result.runs_analyzed, int)
        assert isinstance(result.trend, str)
        assert isinstance(result.outliers, list)


class TestOutlierDetection:
    def test_single_outlier_flagged(self) -> None:
        runs = [
            _make_run("run-1", duration=300),
            _make_run("run-2", duration=290),
            _make_run("run-3", duration=310),
            _make_run("run-4", duration=280),
            _make_run("run-5", duration=2700),
        ]
        result = compute_baseline("svc", runs, [])
        assert len(result.outliers) >= 1

    def test_all_similar_no_outliers(self) -> None:
        runs = [_make_run(f"run-{i}", duration=300) for i in range(1, 11)]
        result = compute_baseline("svc", runs, [])
        assert result.outliers == []


class TestEdgeCases:
    def test_only_5_runs_computes_with_note(self) -> None:
        runs = [_make_run(f"run-{i}", duration=300) for i in range(1, 6)]
        result = compute_baseline("svc", runs, [], requested_limit=30)
        assert result.runs_analyzed == 5  # noqa: PLR2004
        assert "Only 5" in result.note

    def test_no_taskrun_stages_returns_total_only(self) -> None:
        runs = [_make_run(f"run-{i}", duration=100 + i) for i in range(1, 6)]
        result = compute_baseline("svc", runs, [])
        assert result.stages == {}
        assert result.total_duration is not None
        assert result.total_duration.avg > 0

    def test_runs_without_completion_time_excluded(self) -> None:
        runs = [
            _make_run("run-1", duration=300, completion="2024-01-01T00:10:00Z"),
            _make_run("run-2", duration=400, completion=None),
            _make_run("run-3", duration=350, completion="2024-01-01T00:35:00Z"),
        ]
        result = compute_baseline("svc", runs, [])
        assert result.runs_analyzed == 2  # noqa: PLR2004
        assert result.excluded_running == 1

    def test_all_failed_runs_returns_empty(self) -> None:
        runs = [_make_run(f"run-{i}", status="failed", duration=300) for i in range(1, 6)]
        result = compute_baseline("svc", runs, [])
        assert result.runs_analyzed == 0
        assert result.trend == "insufficient_data"

    def test_stage_names_vary_best_effort_matching(self) -> None:
        runs = [_make_run("run-1", duration=300)]
        tasks = [
            _make_task("t1", "build-image", "run-1", 120),
            _make_task("t2", "run-tests", "run-1", 80),
            _make_task("t3", "deploy-to-prod", "run-1", 40),
        ]
        result = compute_baseline("svc", runs, tasks)
        assert "build" in result.stages
        assert "test" in result.stages
        assert "deploy" in result.stages


class TestTrendComputation:
    def test_trend_improving(self) -> None:
        runs = [
            _make_run(f"early-{i}", duration=400 - i, start=f"2024-01-01T00:{i:02d}:00Z")
            for i in range(5)
        ] + [
            _make_run(f"late-{i}", duration=200 - i, start=f"2024-01-02T00:{i:02d}:00Z")
            for i in range(5)
        ]
        result = compute_baseline("svc", runs, [])
        assert result.trend == "improving"

    def test_trend_degrading(self) -> None:
        runs = [
            _make_run(f"early-{i}", duration=200 + i, start=f"2024-01-01T00:{i:02d}:00Z")
            for i in range(5)
        ] + [
            _make_run(f"late-{i}", duration=400 + i, start=f"2024-01-02T00:{i:02d}:00Z")
            for i in range(5)
        ]
        result = compute_baseline("svc", runs, [])
        assert result.trend == "degrading"

    def test_trend_stable(self) -> None:
        runs = [
            _make_run(f"early-{i}", duration=300, start=f"2024-01-01T00:{i:02d}:00Z")
            for i in range(5)
        ] + [
            _make_run(f"late-{i}", duration=315, start=f"2024-01-02T00:{i:02d}:00Z")
            for i in range(5)
        ]
        result = compute_baseline("svc", runs, [])
        assert result.trend == "stable"

    def test_insufficient_data_under_5(self) -> None:
        runs = [_make_run(f"run-{i}", duration=300) for i in range(1, 4)]
        result = compute_baseline("svc", runs, [])
        assert result.trend == "insufficient_data"


class TestTrendPercentageAndBottleneck:
    """CP mock had richer trend data (precise %, bottleneck stage) than this
    real service ever computed — this brings the real service up to that
    level of detail using data it already collects, instead of the mock
    staying artificially richer than what production can actually deliver.
    """

    def test_trend_pct_positive_when_degrading(self) -> None:
        runs = [
            _make_run(f"early-{i}", duration=200 + i, start=f"2024-01-01T00:{i:02d}:00Z")
            for i in range(5)
        ] + [
            _make_run(f"late-{i}", duration=400 + i, start=f"2024-01-02T00:{i:02d}:00Z")
            for i in range(5)
        ]
        result = compute_baseline("svc", runs, [])
        assert result.trend == "degrading"
        assert result.trend_pct is not None
        assert result.trend_pct > 0

    def test_trend_pct_negative_when_improving(self) -> None:
        runs = [
            _make_run(f"early-{i}", duration=400 - i, start=f"2024-01-01T00:{i:02d}:00Z")
            for i in range(5)
        ] + [
            _make_run(f"late-{i}", duration=200 - i, start=f"2024-01-02T00:{i:02d}:00Z")
            for i in range(5)
        ]
        result = compute_baseline("svc", runs, [])
        assert result.trend == "improving"
        assert result.trend_pct is not None
        assert result.trend_pct < 0

    def test_trend_pct_none_when_insufficient_data(self) -> None:
        runs = [_make_run(f"run-{i}", duration=300) for i in range(1, 4)]
        result = compute_baseline("svc", runs, [])
        assert result.trend_pct is None

    def test_bottleneck_stage_identifies_the_worst_degrading_stage(self) -> None:
        runs = [
            _make_run(f"early-{i}", duration=300, start=f"2024-01-01T00:{i:02d}:00Z")
            for i in range(5)
        ] + [
            _make_run(f"late-{i}", duration=500, start=f"2024-01-02T00:{i:02d}:00Z")
            for i in range(5)
        ]
        tasks = []
        for i in range(5):
            tasks.append(_make_task(f"b-early-{i}", "build", f"early-{i}", 100))
            tasks.append(_make_task(f"t-early-{i}", "test", f"early-{i}", 80))
        for i in range(5):
            tasks.append(_make_task(f"b-late-{i}", "build", f"late-{i}", 300))
            tasks.append(_make_task(f"t-late-{i}", "test", f"late-{i}", 85))
        result = compute_baseline("svc", runs, tasks)
        assert result.bottleneck_stage == "build"

    def test_bottleneck_stage_none_when_stable(self) -> None:
        runs = [
            _make_run(f"early-{i}", duration=300, start=f"2024-01-01T00:{i:02d}:00Z")
            for i in range(5)
        ] + [
            _make_run(f"late-{i}", duration=315, start=f"2024-01-02T00:{i:02d}:00Z")
            for i in range(5)
        ]
        tasks = []
        for i in range(5):
            tasks.append(_make_task(f"b-early-{i}", "build", f"early-{i}", 120))
            tasks.append(_make_task(f"t-early-{i}", "test", f"early-{i}", 80))
        for i in range(5):
            tasks.append(_make_task(f"b-late-{i}", "build", f"late-{i}", 122))
            tasks.append(_make_task(f"t-late-{i}", "test", f"late-{i}", 82))
        result = compute_baseline("svc", runs, tasks)
        assert result.bottleneck_stage is None

    def test_bottleneck_stage_none_when_no_task_runs(self) -> None:
        runs = [
            _make_run(f"early-{i}", duration=200, start=f"2024-01-01T00:{i:02d}:00Z")
            for i in range(5)
        ] + [
            _make_run(f"late-{i}", duration=400, start=f"2024-01-02T00:{i:02d}:00Z")
            for i in range(5)
        ]
        result = compute_baseline("svc", runs, [])
        assert result.bottleneck_stage is None

    def test_bottleneck_stage_ignores_zero_duration_tasks(self) -> None:
        """A task run with duration_seconds=0 (e.g. skipped/cached step) must
        not be bucketed as real data for bottleneck comparison."""
        runs = [
            _make_run(f"early-{i}", duration=300, start=f"2024-01-01T00:{i:02d}:00Z")
            for i in range(5)
        ] + [
            _make_run(f"late-{i}", duration=500, start=f"2024-01-02T00:{i:02d}:00Z")
            for i in range(5)
        ]
        tasks = []
        for i in range(5):
            tasks.append(_make_task(f"cached-early-{i}", "lint", f"early-{i}", 0))
            tasks.append(_make_task(f"b-early-{i}", "build", f"early-{i}", 100))
        for i in range(5):
            tasks.append(_make_task(f"cached-late-{i}", "lint", f"late-{i}", 0))
            tasks.append(_make_task(f"b-late-{i}", "build", f"late-{i}", 300))
        result = compute_baseline("svc", runs, tasks)
        assert result.bottleneck_stage == "build"

    def test_bottleneck_stage_skips_a_stage_absent_from_one_window(self) -> None:
        """A stage present only in the early runs (e.g. a step removed from
        the pipeline since) has nothing to compare against in the later
        window — it must be skipped, not crash or win by default."""
        runs = [
            _make_run(f"early-{i}", duration=300, start=f"2024-01-01T00:{i:02d}:00Z")
            for i in range(5)
        ] + [
            _make_run(f"late-{i}", duration=500, start=f"2024-01-02T00:{i:02d}:00Z")
            for i in range(5)
        ]
        tasks = []
        for i in range(5):
            tasks.append(_make_task(f"legacy-early-{i}", "scan", f"early-{i}", 50))
            tasks.append(_make_task(f"b-early-{i}", "build", f"early-{i}", 100))
        for i in range(5):
            tasks.append(_make_task(f"b-late-{i}", "build", f"late-{i}", 300))
        result = compute_baseline("svc", runs, tasks)
        assert result.bottleneck_stage == "build"


class TestWorstDegradingStageDirectly:
    """_worst_degrading_stage is exercised end-to-end via compute_baseline
    above, but its zero-average guard can never trigger through that path —
    _bucket_stage_durations_by_window only ever appends durations > 0, so the
    mean of a non-empty list is always > 0. Tested directly here since it's
    a real safety net against division by zero if this helper is ever called
    with data that doesn't uphold that invariant.
    """

    def test_returns_none_when_first_avg_is_zero(self) -> None:
        result = _worst_degrading_stage(
            first_durations={"build": [0.0]},
            last_durations={"build": [300.0]},
        )
        assert result is None
