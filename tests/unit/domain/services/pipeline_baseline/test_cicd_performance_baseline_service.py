"""RED → GREEN — CICD performance baseline domain service."""

from __future__ import annotations

from hexawyn.domain.services.pipeline_baseline.cicd_performance_baseline_service import (
    PipelineRunRecord,
    TaskRunRecord,
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
