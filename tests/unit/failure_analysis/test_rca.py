"""Unit tests for analyze_pipeline_failure — automated pipeline failure RCA."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driven.tekton_port import TaskRunInfo
from hexawyn.domain.models.pipeline_failure_analysis import (
    AnalyzeFailedPipelineRequest,
    FailureType,
)
from hexawyn.domain.models.pipeline_run_logs import StepLog, StepStatus
from hexawyn.domain.services.failure_analysis.rca import analyze_pipeline_failure


def _task_run(
    name: str,
    task_ref: str,
    status: str,
    start_time: str,
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


def _step_log(step_name: str, log_lines: list[str]) -> StepLog:
    return StepLog(
        step_name=step_name, status=StepStatus.FAILED, log_lines=log_lines, truncated=False
    )


class TestRegressionClassification:
    """TC1: Unit test failed with "AssertionError" → classified as regression with confidence 0.85."""

    def test_assertion_error_classified_as_regression(self) -> None:
        history = [
            _task_run(
                "deploy-payment-v3-integration-tests",
                "integration-tests",
                "Failed",
                "2024-01-10T15:00:00Z",
                failing_step="integration-tests",
                failing_step_error="AssertionError: expected 200 got 500",
            )
        ] + [
            _task_run(
                f"deploy-payment-v3-run-{i}-integration-tests",
                "integration-tests",
                "Succeeded",
                f"2024-01-{i:02d}T15:00:00Z",
            )
            for i in range(1, 11)
        ]
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")

        result = analyze_pipeline_failure(request, history, [])

        assert len(result.failures) == 1
        failure = result.failures[0]
        assert failure.failure_type == FailureType.REGRESSION
        assert failure.confidence == pytest.approx(0.85)
        assert "AssertionError" in failure.root_cause


class TestInfrastructureClassification:
    """TC2: Test failed due to "connection timeout" → classified as infrastructure, not regression."""

    def test_connection_timeout_classified_as_infrastructure(self) -> None:
        history = [
            _task_run(
                "deploy-run-db-check",
                "db-check",
                "Failed",
                "2024-01-10T15:00:00Z",
                failing_step="db-check",
                failing_step_error="connection timeout to postgres:5432",
            )
        ]
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")

        result = analyze_pipeline_failure(request, history, [])

        assert result.failures[0].failure_type == FailureType.INFRASTRUCTURE


class TestDependencyClassification:
    def test_module_not_found_classified_as_dependency(self) -> None:
        history = [
            _task_run(
                "run-build",
                "build",
                "Failed",
                "2024-01-10T15:00:00Z",
                failing_step="build",
                failing_step_error="ModuleNotFoundError: No module named 'requests'",
            )
        ]
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")

        result = analyze_pipeline_failure(request, history, [])

        assert result.failures[0].failure_type == FailureType.DEPENDENCY


class TestConfigErrorClassification:
    def test_missing_env_var_classified_as_config_error(self) -> None:
        history = [
            _task_run(
                "run-deploy",
                "deploy",
                "Failed",
                "2024-01-10T15:00:00Z",
                failing_step="deploy",
                failing_step_error="missing required field: environment variable DATABASE_URL not set",
            )
        ]
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")

        result = analyze_pipeline_failure(request, history, [])

        assert result.failures[0].failure_type == FailureType.CONFIG_ERROR


class TestUnmatchedErrorFallsBackToRegression:
    def test_unrecognized_error_message_falls_back_to_regression_without_root_cause_found(
        self,
    ) -> None:
        history = [
            _task_run(
                "run-mystery",
                "mystery-task",
                "Failed",
                "2024-01-10T15:00:00Z",
                failing_step="mystery-task",
                failing_step_error="something odd happened",
            )
        ]
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")

        result = analyze_pipeline_failure(request, history, [])

        assert result.failures[0].failure_type == FailureType.REGRESSION
        assert result.failures[0].confidence == pytest.approx(0.7)


class TestFlakyTestClassification:
    """TC3: Same test failed 3 times in last 5 runs → classified as flaky test."""

    def test_intermittent_failures_classified_as_flaky(self) -> None:
        history = [
            _task_run(
                "run5-e2e",
                "e2e-tests",
                "Failed",
                "2024-01-05T15:00:00Z",
                "e2e-tests",
                "AssertionError: flaky",
            ),
            _task_run("run4-e2e", "e2e-tests", "Succeeded", "2024-01-04T15:00:00Z"),
            _task_run("run3-e2e", "e2e-tests", "Failed", "2024-01-03T15:00:00Z"),
            _task_run("run2-e2e", "e2e-tests", "Succeeded", "2024-01-02T15:00:00Z"),
            _task_run("run1-e2e", "e2e-tests", "Failed", "2024-01-01T15:00:00Z"),
        ]
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")

        result = analyze_pipeline_failure(request, history, [])

        assert result.failures[0].failure_type == FailureType.FLAKY_TEST

    def test_all_runs_failing_is_not_flaky(self) -> None:
        """A persistent (not intermittent) failure across all recent runs is a real regression."""
        history = [
            _task_run(
                f"run{i}-e2e",
                "e2e-tests",
                "Failed",
                f"2024-01-0{i}T15:00:00Z",
                "e2e-tests",
                "AssertionError: x",
            )
            for i in range(1, 6)
        ]
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")

        result = analyze_pipeline_failure(request, history, [])

        assert result.failures[0].failure_type != FailureType.FLAKY_TEST


class TestNoFailures:
    def test_all_succeeded_returns_no_failures(self) -> None:
        history = [_task_run("run1", "build", "Succeeded", "2024-01-01T15:00:00Z")]
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")

        result = analyze_pipeline_failure(request, history, [])

        assert result.failures == []
        assert result.pipeline_run_found is True

    def test_empty_task_runs_reports_not_found(self) -> None:
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")

        result = analyze_pipeline_failure(request, [], [])

        assert result.pipeline_run_found is False
        assert result.failures == []


class TestMultipleFailuresAggregated:
    """Edge case: multiple failures in same PipelineRun → each analyzed separately, aggregated."""

    def test_two_failing_tasks_both_analyzed(self) -> None:
        history = [
            _task_run(
                "run-build",
                "build",
                "Failed",
                "2024-01-01T15:00:00Z",
                "build",
                "connection timeout",
            ),
            _task_run(
                "run-tests",
                "integration-tests",
                "Failed",
                "2024-01-01T15:05:00Z",
                "integration-tests",
                "AssertionError: x",
            ),
        ]
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")

        result = analyze_pipeline_failure(request, history, [])

        assert len(result.failures) == 2
        assert result.aggregated_root_cause != ""


class TestInitContainerOrdering:
    """Edge case: failure in init container → detected and shown before main container failure."""

    def test_earlier_task_failure_appears_first(self) -> None:
        history = [
            _task_run(
                "run-tests",
                "integration-tests",
                "Failed",
                "2024-01-01T15:05:00Z",
                "integration-tests",
                "AssertionError: x",
            ),
            _task_run(
                "run-init",
                "clone-repo",
                "Failed",
                "2024-01-01T15:00:00Z",
                "clone-repo",
                "connection timeout",
            ),
        ]
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")

        result = analyze_pipeline_failure(request, history, [])

        assert result.failures[0].task_name == "clone-repo"
        assert result.failures[1].task_name == "integration-tests"


class TestStepLogsEnrichment:
    def test_generic_exit_code_error_enriched_by_step_logs(self) -> None:
        history = [
            _task_run(
                "run-tests",
                "integration-tests",
                "Failed",
                "2024-01-01T15:00:00Z",
                "integration-tests",
                "exit code 1",
            )
        ]
        step_logs = [
            _step_log(
                "integration-tests", ["running tests...", "AssertionError: expected 200 got 500"]
            )
        ]
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")

        result = analyze_pipeline_failure(request, history, step_logs)

        assert "AssertionError" in result.failures[0].root_cause
