"""RED → GREEN — CICD performance baseline domain service."""

from __future__ import annotations

from hexawyn.domain.services.pipeline_baseline.cicd_performance_baseline_service import (
    PipelineRunRecord,
    TaskRunRecord,
    _bucket_stage_durations_by_window,
    _compute_stats,
    _compute_trend,
    _detect_outliers,
    _find_bottleneck_stage,
    _parse_stage_name,
    _percentile,
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
        assert result.requested_limit == 30  # noqa: PLR2004
        assert result.pipeline == "svc"
        assert result.trend == "stable"

    def test_exact_requested_limit_no_note(self) -> None:
        # len(succeeded) == requested_limit -> note vide (mutant <= donnerait une note)
        runs = [_make_run(f"run-{i}", duration=100) for i in range(5)]
        result = compute_baseline("svc", runs, [], requested_limit=5)
        assert result.note == ""
        assert result.runs_analyzed == 5  # noqa: PLR2004
        assert result.requested_limit == 5  # noqa: PLR2004

    def test_stages_built_from_task_runs(self) -> None:
        runs = [_make_run(f"run-{i}", duration=100 + i) for i in range(10)]
        tasks = [
            {
                "name": f"b{i}",
                "task_name": "build",
                "pipeline_run_name": f"run-{i}",
                "duration_seconds": 50,
            }
            for i in range(10)
        ]
        result = compute_baseline("svc", runs, tasks, requested_limit=30)
        assert "build" in result.stages
        assert result.stages["build"].avg == 50.0  # noqa: PLR2004
        assert result.total_duration is not None
        assert result.note == "Only 10 runs available (requested 30)"

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
        runs = [
            _make_run("run-1", status="failed", duration=300),
            _make_run("run-2", status="failed", duration=300, completion=None),
        ]
        result = compute_baseline("svc", runs, [])
        assert result.runs_analyzed == 0
        assert result.trend == "insufficient_data"
        assert result.pipeline == "svc"
        assert result.requested_limit == 30  # noqa: PLR2004
        assert result.excluded_running == 1
        assert result.excluded_failed == 1
        assert result.note == "No succeeded runs with completionTime available"
        assert result.stages == {}
        assert result.outliers == []

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


class TestParseStageName:
    def test_build(self) -> None:
        assert _parse_stage_name("build-image") == "build"

    def test_test(self) -> None:
        assert _parse_stage_name("run-tests") == "test"

    def test_test_hyphen_suffix(self) -> None:
        assert _parse_stage_name("pytest") == "test"

    def test_test_only_hyphen_prefix(self) -> None:
        # "test-" seul (sans "test" ni "-test") couvre la branche test-
        assert _parse_stage_name("test-a") == "test"

    def test_test_only_hyphen_suffix_branch(self) -> None:
        # "-test" seul couvre la branche -test
        assert _parse_stage_name("a-test") == "test"

    def test_test_plain_kw(self) -> None:
        assert _parse_stage_name("the-test-ng") == "test"

    def test_deploy(self) -> None:
        assert _parse_stage_name("deploy-to-prod") == "deploy"

    def test_lint(self) -> None:
        assert _parse_stage_name("lint-check") == "lint"

    def test_scan(self) -> None:
        assert _parse_stage_name("security-scan") == "scan"

    def test_unknown_falls_back_to_original(self) -> None:
        assert _parse_stage_name("CustomStep") == "CustomStep"


class TestComputeStats:
    def test_empty_returns_default(self) -> None:
        stats = _compute_stats([])
        assert stats.avg == 0.0
        assert stats.p50 == 0.0
        assert stats.p95 == 0.0
        assert stats.max == 0.0

    def test_single_duration_p95_falls_back_to_value(self) -> None:
        stats = _compute_stats([42.35])
        assert stats.avg == 42.4  # round(42.35, 1)  # noqa: PLR2004
        assert stats.p50 == 42.4  # noqa: PLR2004
        assert stats.p95 == 42.4  # round(...,1) ; mutant round(...,2) -> 42.35  # noqa: PLR2004
        assert stats.max == 42.4  # noqa: PLR2004
        assert stats.unit == "seconds"

    def test_multiple_durations(self) -> None:
        stats = _compute_stats([10.0, 20.0, 30.0])
        assert stats.avg == 20.0  # noqa: PLR2004
        assert stats.p50 == 20.0  # noqa: PLR2004
        assert stats.max == 30.0  # noqa: PLR2004
        assert stats.p95 >= stats.p50

    def test_rounding_preserved(self) -> None:
        # durations avec decimales -> l'arrondi a 1 decimale doit trancher
        stats = _compute_stats([10.05, 10.15, 10.25])
        assert stats.avg == 10.2  # noqa: PLR2004
        assert stats.p50 == 10.2  # noqa: PLR2004
        assert stats.max == 10.2  # noqa: PLR2004


class TestPercentile:
    def test_empty_returns_zero(self) -> None:
        assert _percentile([], 95) == 0.0

    def test_single_element(self) -> None:
        assert _percentile([15.0], 50) == 15.0  # noqa: PLR2004

    def test_exact_index_no_interpolation(self) -> None:
        data = [10.0, 20.0, 30.0, 40.0]
        assert _percentile(data, 0) == 10.0  # noqa: PLR2004

    def test_interpolated(self) -> None:
        data = [10.0, 20.0, 30.0, 40.0]
        # pct=95 -> k=(0.95)*(3)=2.85 -> between index 2 and 3
        result = _percentile(data, 95)
        assert result >= 30.0  # noqa: PLR2004
        assert result <= 40.0  # noqa: PLR2004


class TestDetectOutliers:
    def _runs(self, durations: list[int]) -> list[PipelineRunRecord]:
        return [_make_run(f"run-{i}", duration=d) for i, d in enumerate(durations, 1)]

    def test_no_outlier_when_within_threshold(self) -> None:
        runs = self._runs([100, 120, 110, 105, 115])
        outliers = _detect_outliers(runs, [110.0])
        assert outliers == []

    def test_outlier_above_2x_average(self) -> None:
        runs = self._runs([100, 120, 300, 110, 115])
        outliers = _detect_outliers(runs, [110.0])
        assert "run-3" in outliers

    def test_zero_duration_skipped(self) -> None:
        runs = self._runs([0, 100, 110])
        outliers = _detect_outliers(runs, [110.0])
        assert outliers == []

    def test_stage_avg_zero_never_outlier(self) -> None:
        runs = self._runs([300, 200, 400])
        outliers = _detect_outliers(runs, [0.0])
        assert outliers == []

    def test_no_duplicate_outlier_names(self) -> None:
        runs = self._runs([300, 200, 210])
        outliers = _detect_outliers(runs, [100.0, 100.0])
        assert "run-1" in outliers
        assert outliers.count("run-1") == 1

    def test_negative_duration_skipped(self) -> None:
        # dur = -5: <= 0 est TRUE -> skippe; mutant dur < 0 laisserait passer
        runs = [self._make_run(-5)]
        assert _detect_outliers(runs, [110.0]) == []

    def _make_run(self, duration: int) -> PipelineRunRecord:
        return _make_run("run-1", duration=duration)


class TestComputeTrend:
    def test_under_5_insufficient(self) -> None:
        runs = [_make_run(f"run-{i}", duration=100) for i in range(4)]
        assert _compute_trend(runs) == ("insufficient_data", None)

    def test_insufficient_completed_when_gaps(self) -> None:
        # Fenetre early avec < 3 runs ayant un duration valide (ici 1 seul)
        runs = [
            _make_run(f"run-{i}", duration=100 if i == 0 else None, completion=None)
            for i in range(5)
        ]
        assert _compute_trend(runs) == ("insufficient_data", None)

    def test_stable_between_thresholds(self) -> None:
        runs = [
            _make_run(f"early-{i}", duration=110, start=f"2024-01-01T00:{i:02d}:00Z")
            for i in range(5)
        ] + [
            _make_run(f"late-{i}", duration=115, start=f"2024-01-02T00:{i:02d}:00Z")
            for i in range(5)
        ]
        trend, pct = _compute_trend(runs)
        assert trend == "stable"
        assert pct is not None

    def test_sorts_by_start_time_out_of_order(self) -> None:
        # start_time non tries: le tri par start_time doit etre respecte
        runs = [
            _make_run("late-4", duration=400, start="2024-01-02T00:04:00Z"),
            _make_run("early-0", duration=200, start="2024-01-01T00:00:00Z"),
            _make_run("early-2", duration=220, start="2024-01-01T00:02:00Z"),
            _make_run("late-1", duration=380, start="2024-01-02T00:01:00Z"),
            _make_run("early-1", duration=210, start="2024-01-01T00:01:00Z"),
            _make_run("late-2", duration=420, start="2024-01-02T00:02:00Z"),
            _make_run("early-3", duration=230, start="2024-01-01T00:03:00Z"),
            _make_run("late-3", duration=360, start="2024-01-02T00:03:00Z"),
            _make_run("early-4", duration=240, start="2024-01-01T00:04:00Z"),
            _make_run("late-0", duration=400, start="2024-01-02T00:00:00Z"),
        ]
        trend, pct = _compute_trend(runs)
        # early avg=220, late avg=392 -> degrade
        assert trend == "degrading"
        assert pct is not None
        assert pct > 0

    def test_improving_negative_delta(self) -> None:
        runs = [
            _make_run(f"early-{i}", duration=200, start=f"2024-01-01T00:{i:02d}:00Z")
            for i in range(5)
        ] + [
            _make_run(f"late-{i}", duration=160, start=f"2024-01-02T00:{i:02d}:00Z")
            for i in range(5)
        ]
        trend, pct = _compute_trend(runs)
        assert trend == "improving"
        assert pct is not None
        assert pct < 0

    def test_exactly_five_runs_not_insufficient(self) -> None:
        # len == 5: < 5 est FALSE -> on entre dans le calcul (mutant <= 5 donnerait insufficient)
        runs = [_make_run(f"r{i}", duration=100, start=f"2024-01-01T00:0{i}:00Z") for i in range(5)]
        trend, pct = _compute_trend(runs)
        assert trend == "stable"
        assert pct == 0.0

    def test_exact_negative_10pct_stable(self) -> None:
        # delta = -10% exact: < -0.10 est FALSE -> stable (mutant <= donnerait degrading)
        runs = [
            _make_run(f"e{i}", duration=100, start=f"2024-01-01T00:0{i}:00Z") for i in range(5)
        ] + [_make_run(f"l{i}", duration=90, start=f"2024-01-02T00:0{i}:00Z") for i in range(5)]
        trend, pct = _compute_trend(runs)
        assert trend == "stable"
        assert pct == -10.0  # noqa: PLR2004

    def test_exact_positive_10pct_stable(self) -> None:
        # delta = +10% exact: > 0.10 est FALSE -> stable (mutant >= donnerait degrading)
        runs = [
            _make_run(f"e{i}", duration=100, start=f"2024-01-01T00:0{i}:00Z") for i in range(5)
        ] + [_make_run(f"l{i}", duration=110, start=f"2024-01-02T00:0{i}:00Z") for i in range(5)]
        trend, pct = _compute_trend(runs)
        assert trend == "stable"
        assert pct == 10.0  # noqa: PLR2004

    def test_first_avg_zero_insufficient(self) -> None:
        # first_5 contient des runs avec duration=0 -> mean==0 -> insufficient
        runs = [
            _make_run(f"e{i}", duration=0, start=f"2024-01-01T00:0{i}:00Z") for i in range(5)
        ] + [_make_run(f"l{i}", duration=100, start=f"2024-01-02T00:0{i}:00Z") for i in range(5)]
        assert _compute_trend(runs) == ("insufficient_data", None)


class TestBucketStageDurationsByWindow:
    def test_splits_by_window(self) -> None:
        tasks = [
            _make_task("b1", "build", "early-1", 100),
            _make_task("b2", "build", "late-1", 300),
        ]
        by_pipeline = {"early-1": [tasks[0]], "late-1": [tasks[1]]}
        first, last = _bucket_stage_durations_by_window(by_pipeline, {"early-1"}, {"late-1"})
        assert first["build"] == [100.0]
        assert last["build"] == [300.0]

    def test_skips_runs_outside_both_windows(self) -> None:
        task = _make_task("b1", "build", "mid-1", 200)
        by_pipeline = {"mid-1": [task]}
        first, last = _bucket_stage_durations_by_window(by_pipeline, {"early-1"}, {"late-1"})
        assert first == {}
        assert last == {}

    def test_zero_duration_task_skipped(self) -> None:
        task = _make_task("cached", "lint", "early-1", 0)
        by_pipeline = {"early-1": [task]}
        first, last = _bucket_stage_durations_by_window(by_pipeline, {"early-1"}, set())
        assert first == {}
        assert last == {}


class TestEdgeBoundaries:
    def test_percentile_interpolated_50(self) -> None:
        # pct=50, 4 elems: k=(0.5)*(3)=1.5 -> interpole entre index 1,2 -> 25.0
        assert _percentile([10.0, 20.0, 30.0, 40.0], 50) == 25.0  # noqa: PLR2004

    def test_percentile_95_3_elements(self) -> None:
        # k=(0.95)*(2)=1.9 -> f=1, c=0.9 -> 20 + 0.9*10 = 29.0
        assert _percentile([10.0, 20.0, 30.0], 95) == 29.0  # noqa: PLR2004

    def test_detect_outliers_break_on_zero_dur(self) -> None:
        # run-1 dur=0 (skip, si break -> r2 jamais teste); r2 est outlier
        runs = [
            {"name": "r1", "duration_seconds": 0},
            {"name": "r2", "duration_seconds": 300},
            {"name": "r3", "duration_seconds": 100},
        ]
        outliers = _detect_outliers(runs, [110.0])
        assert "r2" in outliers

    def test_detect_outliers_boundary_2x(self) -> None:
        # dur == 2*avg n'est PAS > 2*avg -> pas outlier (mutant >= le serait)
        runs = [{"name": "r1", "duration_seconds": 220}]
        assert _detect_outliers(runs, [110.0]) == []

    def test_worst_degrading_delta_above_threshold(self) -> None:
        # delta doit etre > 0.10 strictement: 15/10 = 1.5 -> (20-10)/10=1.0 > .10
        result = _worst_degrading_stage({"a": [10.0]}, {"a": [20.0]})
        assert result == "a"

    def test_worst_degrading_skips_zero_first_avg(self) -> None:
        # first_avg = 0 -> skip (mutant break sortirait avant les suivants)
        result = _worst_degrading_stage(
            {"bad": [0.0], "good": [10.0]}, {"bad": [20.0], "good": [20.0]}
        )
        assert result == "good"

    def test_bucket_break_when_run_not_in_windows_then_real(self) -> None:
        # run "mid" hors fenetres suivi d'un run "early" -> si break, early perdu
        tasks_early = _make_task("b1", "build", "early-1", 100)
        tasks_mid = _make_task("m1", "build", "mid-1", 200)
        by_pipeline = {"mid-1": [tasks_mid], "early-1": [tasks_early]}
        first, last = _bucket_stage_durations_by_window(by_pipeline, {"early-1"}, {"late-1"})
        assert first["build"] == [100.0]
        assert last == {}


class TestBottleneckBoundaries:
    def test_first_5_window_excludes_6th(self) -> None:
        # 6 runs: le 6e (r5) est a 300 -> uniquement dans last5. first5 = r0..r4 (tous 100)
        def make(name: str, dur: int, start: str) -> dict[str, object]:
            return {
                "name": name,
                "status": "succeeded",
                "duration_seconds": dur,
                "start_time": start,
                "completion_time": start,
            }

        runs: list[dict[str, object]] = [
            make(f"r{i}", 300 if i == 5 else 100, f"2024-01-01T00:0{i}:00Z")  # noqa: PLR2004
            for i in range(6)
        ]
        tasks: dict[str, list[dict[str, object]]] = {
            f"r{i}": [
                {
                    "name": f"b{i}",
                    "task_name": "build",
                    "pipeline_run_name": f"r{i}",
                    "duration_seconds": 300 if i == 5 else 100,  # noqa: PLR2004
                }
            ]
            for i in range(6)
        }
        result = _find_bottleneck_stage(runs, tasks)
        assert result == "build"

    def test_under_5_succeeded_returns_none(self) -> None:
        # len(succeeded_runs) < 5 -> None (mutant <= 5 donnerait autre chose a 5)
        result = _find_bottleneck_stage([], {})
        assert result is None


class TestExactBoundaries:
    def test_detect_outliers_duration_one_kept(self) -> None:
        # dur=1 avec avg=0.4: 1 > 2*0.4=0.8 -> outlier (mutant dur<=1 le sauterait)
        runs = [{"name": "r1", "duration_seconds": 1}]
        assert _detect_outliers(runs, [0.4]) == ["r1"]

    def test_bucket_duration_one_kept(self) -> None:
        # dur=1 est > 0 -> conservé (mutant dur<=1 le sauterait)
        by_pipeline = {
            "early-1": [
                {
                    "name": "t",
                    "task_name": "build",
                    "pipeline_run_name": "early-1",
                    "duration_seconds": 1,
                }
            ]
        }
        first, last = _bucket_stage_durations_by_window(by_pipeline, {"early-1"}, set())
        assert first["build"] == [1.0]

    def test_worst_degrading_delta_strictly_above(self) -> None:
        # delta = 0.11 > 0.10 -> degradant (mutant >= donnerait aussi a -> pas discriminant ici)
        assert _worst_degrading_stage({"a": [100.0]}, {"a": [111.0]}) == "a"

    def test_worst_degrading_delta_exact_threshold_discriminates(self) -> None:
        # delta = 0.10 exact: > 0.10 FALSE -> None (mutant >= donnerait 'a')
        assert _worst_degrading_stage({"a": [100.0]}, {"a": [110.0]}) is None


class TestTrendSortingBoundary:
    def test_reversed_input_still_sorted_by_start_time(self) -> None:
        # l'ordre d'entree est l'inverse de l'ordre chronologique: le tri doit re-trier
        def make(name: str, dur: int, start: str) -> dict[str, object]:
            return {
                "name": name,
                "status": "succeeded",
                "duration_seconds": dur,
                "start_time": start,
                "completion_time": start,
            }

        runs: list[dict[str, object]] = []
        for i in range(10):
            tag = "e" if i < 5 else "l"  # noqa: PLR2004
            start = f"2024-01-01T00:{i:02d}:00Z" if i < 5 else f"2024-01-02T00:{i - 5:02d}:00Z"  # noqa: PLR2004
            runs.append(make(f"{tag}{i}", 100 if i < 5 else 120, start))  # noqa: PLR2004
        runs = list(reversed(runs))
        trend, pct = _compute_trend(runs)
        assert trend == "degrading"
        assert pct == 20.0  # noqa: PLR2004


class TestTrendRoundingPrecision:
    def test_pct_rounding_two_decimals_distinguishes(self) -> None:
        # delta ~0.0009 -> pct brut 0.09 ; round 1 dec = 0.1, round 2 dec = 0.09
        def make(name: str, dur: float, start: str) -> dict[str, object]:
            return {
                "name": name,
                "status": "succeeded",
                "duration_seconds": dur,
                "start_time": start,
                "completion_time": start,
            }

        runs: list[dict[str, object]] = [
            make(f"e{i}", 100.0, f"2024-01-01T00:0{i}:00Z") for i in range(5)
        ] + [make(f"l{i}", 100.09, f"2024-01-02T00:0{i}:00Z") for i in range(5)]
        trend, pct = _compute_trend(runs)
        assert trend == "stable"
        assert pct == 0.1  # noqa: PLR2004


class TestStatsAndBucketPrecision:
    def test_p95_two_element_list(self) -> None:
        # len == 2: la branche len>=2 s'applique (mutant len>=3 donnerait durations[0])
        stats = _compute_stats([1.0, 2.0])
        assert stats.p95 == 1.9  # noqa: PLR2004

    def test_p95_rounding_precision(self) -> None:
        # p95 = 3.85 brut -> round(3.85, 1) = 3.8 (mutant round(...,None) donnerait 3.85)
        stats = _compute_stats([1.0, 2.0, 3.0, 4.0])
        assert stats.p95 == 3.8  # noqa: PLR2004

    def test_bucket_absent_task_name_unknown(self) -> None:
        # task sans cle 'task_name' -> stage 'unknown' (mutants get()/variantes ties)
        task = {"name": "t", "pipeline_run_name": "early-1", "duration_seconds": 50}
        first, last = _bucket_stage_durations_by_window({"early-1": [task]}, {"early-1"}, set())
        assert first["unknown"] == [50.0]


class TestComputeBaselineNoneDurations:
    def _run(self, name: str, dur: int | None) -> dict[str, object]:
        return {
            "name": name,
            "status": "succeeded",
            "duration_seconds": dur,
            "start_time": "2024-01-01T00:00:00Z",
            "completion_time": "2024-01-01T01:00:00Z",
        }

    def test_none_duration_run_excluded_from_total(self) -> None:
        # run avec duration=None -> or 0 -> exclu (mutant or 1 l'inclurait)
        runs = [
            self._run("r1", None),
            self._run("r2", 100),
            self._run("r3", 100),
            self._run("r4", 100),
            self._run("r5", 100),
        ]
        result = compute_baseline("svc", runs, [], requested_limit=30)
        assert result.total_duration is not None
        assert result.total_duration.avg == 100.0  # noqa: PLR2004
        assert result.runs_analyzed == 5  # noqa: PLR2004

    def test_none_duration_task_creates_unknown_stage(self) -> None:
        # task sans task_name ni duration -> stage 'unknown', tue get("pipeline_run_name","")->None
        runs = [self._run("r1", 100)]
        tasks = [
            {"name": "t1", "pipeline_run_name": "r1", "duration_seconds": 50},
            {"name": "t2", "pipeline_run_name": "r2", "duration_seconds": None},
        ]
        result = compute_baseline("svc", runs, tasks, requested_limit=30)
        assert "unknown" in result.stages
        assert result.stages["unknown"].avg == 50.0  # noqa: PLR2004


class TestComputeBaselineDurOne:
    def _run(self, name: str, dur: int | None) -> dict[str, object]:
        return {
            "name": name,
            "status": "succeeded",
            "duration_seconds": dur,
            "start_time": "2024-01-01T00:00:00Z",
            "completion_time": "2024-01-01T01:00:00Z",
        }

    def test_duration_one_run_included(self) -> None:
        # dur=1 > 0 : inclus dans le total (mutant > 1 l'exclurait -> avg different)
        runs = [self._run("r0", 1)] + [self._run(f"r{i}", 100) for i in range(1, 5)]
        result = compute_baseline("svc", runs, [], requested_limit=30)
        assert result.total_duration is not None
        assert result.total_duration.avg == 80.2  # noqa: PLR2004

    def test_duration_one_task_kept_in_stage(self) -> None:
        # task dur=1 > 0 : garde dans le stage (mutant > 1 l'exclurait -> stage vide)
        runs = [self._run("r1", 100)]
        tasks = [
            {"name": "t", "task_name": "build", "pipeline_run_name": "r1", "duration_seconds": 1}
        ]
        result = compute_baseline("svc", runs, tasks, requested_limit=30)
        assert "build" in result.stages
        assert result.stages["build"].avg == 1.0  # noqa: PLR2004


class TestComputeBaselineExclusions:
    def test_mixed_failed_normal_return_excluded_failed(self) -> None:
        # 1 succeeded + 1 failed (completion present) -> retour normal excluded_failed=1
        # (mutant excluded_failed=None du retour final detecte)
        runs = [
            _make_run("a", duration=100),
            _make_run("b", duration=50, status="failed"),
        ]
        result = compute_baseline("svc", runs, [])
        assert result.runs_analyzed == 1
        assert result.excluded_failed == 1
        assert result.excluded_running == 0

    def test_zero_duration_task_excluded_from_stage(self) -> None:
        # task dur=0 -> > 0 FALSE -> pas de stage build
        # (mutant tr_dur >= 0 creerait un stage a avg 0)
        runs = [_make_run("a", duration=100)]
        tasks = [
            {"name": "t", "task_name": "build", "pipeline_run_name": "a", "duration_seconds": 0}
        ]
        result = compute_baseline("svc", runs, tasks)
        assert "build" not in result.stages

    def test_no_succeeded_with_custom_limit(self) -> None:
        # no-succeeded avec requested_limit non-defaut -> conserve (mutant supprime -> 30)
        runs = [_make_run("x", duration=100, status="failed")]
        result = compute_baseline("svc", runs, [], requested_limit=5)
        assert result.requested_limit == 5  # noqa: PLR2004


class TestSortMissingStartTime:
    def _run(self, name: str, dur: int, start: str | None) -> dict[str, object]:
        return {
            "name": name,
            "status": "succeeded",
            "duration_seconds": dur,
            "start_time": start,
            "completion_time": start or "2024-01-01T00:00:00Z",
        }

    def test_trend_sorts_missing_start_first(self) -> None:
        # runs sans start_time (dur 100) + runs dates (dur 50).
        # le tri par start_time met les no-start (cle '') en premier
        # -> first_5 = no-start (100), last_5 = dates (50) -> improving -50
        runs = [self._run(f"ns{i}", 100, None) for i in range(5)] + [
            self._run(f"d{i}", 50, f"2024-01-01T00:0{i}:00Z") for i in range(5)
        ]
        trend, pct = _compute_trend(runs)
        assert trend == "improving"
        assert pct == -50.0  # noqa: PLR2004

    def test_bottleneck_ordering_missing_start(self) -> None:
        # no-start build=200 (first_5), dates build=50 (last_5) -> pas de degradation
        # (le mutant de cle de tri inverserait les fenetres -> build detecte a tort)
        runs = [self._run(f"ns{i}", 200, None) for i in range(5)] + [
            self._run(f"d{i}", 50, f"2024-01-01T00:0{i}:00Z") for i in range(5)
        ]
        tasks: dict[str, list[dict[str, object]]] = {}
        for i in range(5):
            tasks[f"ns{i}"] = [
                {
                    "name": f"b{i}",
                    "task_name": "build",
                    "pipeline_run_name": f"ns{i}",
                    "duration_seconds": 200,
                }
            ]
            tasks[f"d{i}"] = [
                {
                    "name": f"c{i}",
                    "task_name": "build",
                    "pipeline_run_name": f"d{i}",
                    "duration_seconds": 50,
                }
            ]
        result = _find_bottleneck_stage(runs, tasks)
        assert result is None


class TestTrendWindowBoundary:
    def _run(self, name: str, dur: int | None, start: str | None) -> dict[str, object]:
        return {
            "name": name,
            "status": "succeeded",
            "duration_seconds": dur,
            "start_time": start,
            "completion_time": start or "2024-01-01T00:00:00Z",
        }

    def test_first_window_exactly_three_valid(self) -> None:
        # first_5 ne contient que 3 runs avec duration valide (r0-r2), r3-r4 dur None
        # len(first_5) == 3 : 3 < 3 est FALSE -> on continue (mutant <= 3 -> insufficient)
        runs = [
            self._run(f"e{i}", 100 if i < 3 else None, f"2024-01-01T00:0{i}:00Z")  # noqa: PLR2004
            for i in range(5)
        ] + [self._run(f"l{i}", 50, f"2024-01-02T00:0{i}:00Z") for i in range(5)]
        trend, pct = _compute_trend(runs)
        assert trend == "improving"
        assert pct == -50.0  # noqa: PLR2004


class TestDetectOutliersNoneDuration:
    def test_none_duration_skipped_with_low_avg(self) -> None:
        # dur None -> or 0 = 0 -> skip (0 <= 0). Mutant or 1 -> 1 > 2*0.4=0.8 -> outlier
        runs = [{"name": "x", "duration_seconds": None}]
        assert _detect_outliers(runs, [0.4]) == []


class TestLastWindowBoundary:
    def test_last_window_exactly_three_valid(self) -> None:
        # last_5 ne contient que 3 runs valides (l0-l2), l3-l4 dur None
        # len(last_5) == 3 : 3 < 3 FALSE -> on continue (mutant < 4 -> insufficient)
        def make(name: str, dur: int | None, start: str | None) -> dict[str, object]:
            return {
                "name": name,
                "status": "succeeded",
                "duration_seconds": dur,
                "start_time": start,
                "completion_time": start or "2024-01-01T00:00:00Z",
            }

        runs = [make(f"e{i}", 100, f"2024-01-01T00:0{i}:00Z") for i in range(5)] + [
            make(f"l{i}", 200 if i < 3 else None, f"2024-01-02T00:0{i}:00Z")  # noqa: PLR2004
            for i in range(5)
        ]
        trend, pct = _compute_trend(runs)
        assert trend == "degrading"
        assert pct == 100.0  # noqa: PLR2004


class TestBottleneckSortDiscrimination:
    def test_sorted_by_start_time_not_input_order(self) -> None:
        # Entree: dates (build 50) EN PREMIER puis no-start (build 200).
        # Le tri par start_time met les no-start (cle '') en premier -> first=200, last=50 -> None.
        # Si la cle de tri est cassee (ordre stable d'entree) -> dates first (50),
        # no-start last (200) -> 'build' detecte a tort.
        def make(name: str, dur: int, start: str | None) -> dict[str, object]:
            return {
                "name": name,
                "status": "succeeded",
                "duration_seconds": 100,
                "start_time": start,
                "completion_time": start or "2024-01-01T00:00:00Z",
            }

        runs: list[dict[str, object]] = [
            make(f"d{i}", 50, f"2024-01-01T00:0{i}:00Z") for i in range(5)
        ] + [make(f"ns{i}", 200, None) for i in range(5)]
        tasks: dict[str, list[dict[str, object]]] = {}
        for i in range(5):
            tasks[f"d{i}"] = [
                {
                    "name": f"t{i}",
                    "task_name": "build",
                    "pipeline_run_name": f"d{i}",
                    "duration_seconds": 50,
                }
            ]
            tasks[f"ns{i}"] = [
                {
                    "name": f"u{i}",
                    "task_name": "build",
                    "pipeline_run_name": f"ns{i}",
                    "duration_seconds": 200,
                }
            ]
        result = _find_bottleneck_stage(runs, tasks)
        assert result is None
