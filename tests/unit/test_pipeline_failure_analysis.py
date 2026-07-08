"""Unit tests for analyze_failed_pipeline domain models (pure dataclasses)."""

from __future__ import annotations

from hexawyn.domain.models.pipeline_failure_analysis import (
    AnalyzeFailedPipelineRequest,
    AnalyzeFailedPipelineResult,
    FailureAnalysis,
    FailureType,
)


class TestFailureType:
    def test_expected_members(self) -> None:
        assert FailureType.FLAKY_TEST.value == "flaky_test"
        assert FailureType.REGRESSION.value == "regression"
        assert FailureType.INFRASTRUCTURE.value == "infrastructure"
        assert FailureType.DEPENDENCY.value == "dependency"
        assert FailureType.CONFIG_ERROR.value == "config_error"


class TestFailureAnalysis:
    def test_fields(self) -> None:
        analysis = FailureAnalysis(
            task_name="integration-tests",
            root_cause="AssertionError: expected 200 got 500",
            failure_type=FailureType.REGRESSION,
            confidence=0.85,
            impact_score=5.5,
            remediation="Review the recent code changes to this task.",
        )
        assert analysis.task_name == "integration-tests"
        assert analysis.failure_type == FailureType.REGRESSION
        assert analysis.confidence == 0.85
        assert analysis.impact_score == 5.5


class TestAnalyzeFailedPipelineRequest:
    def test_defaults(self) -> None:
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3")
        assert request.namespace == "default"

    def test_custom_namespace(self) -> None:
        request = AnalyzeFailedPipelineRequest(pipeline_name="deploy-payment-v3", namespace="prod")
        assert request.namespace == "prod"


class TestAnalyzeFailedPipelineResult:
    def test_defaults(self) -> None:
        result = AnalyzeFailedPipelineResult(
            pipeline_name="deploy-payment-v3", namespace="default", pipeline_run_found=True
        )
        assert result.failures == []
        assert result.aggregated_root_cause == ""
        assert result.summary == ""

    def test_with_failures(self) -> None:
        failure = FailureAnalysis(
            task_name="integration-tests",
            root_cause="AssertionError: expected 200 got 500",
            failure_type=FailureType.REGRESSION,
            confidence=0.85,
            impact_score=5.5,
            remediation="Review the recent code changes to this task.",
        )
        result = AnalyzeFailedPipelineResult(
            pipeline_name="deploy-payment-v3",
            namespace="default",
            pipeline_run_found=True,
            failures=[failure],
            summary="1 failure detected",
        )
        assert len(result.failures) == 1
        assert result.summary == "1 failure detected"
