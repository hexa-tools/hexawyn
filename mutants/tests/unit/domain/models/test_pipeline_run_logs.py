from __future__ import annotations

from hexawyn.domain.models.pipeline_run_logs import (
    PipelineRunLogsRequest,
    PipelineRunLogsResult,
    StepLog,
    StepStatus,
)


class TestStepLog:
    def test_failed(self) -> None:
        sl = StepLog(
            step_name="build-image",
            status=StepStatus.FAILED,
            log_lines=["ERROR: no space left on device"],
            truncated=False,
        )
        assert sl.status == StepStatus.FAILED
        assert sl.truncated is False

    def test_truncated(self) -> None:
        lines = [f"line {i}" for i in range(501)]
        sl = StepLog(
            step_name="big-step",
            status=StepStatus.SUCCEEDED,
            log_lines=lines[-500:],
            truncated=True,
        )
        assert sl.truncated is True
        assert len(sl.log_lines) == 500  # noqa: PLR2004


class TestPipelineRunLogsResult:
    def test_failed_step_highlighted(self) -> None:
        steps = [
            StepLog(
                step_name="clone-repo",
                status=StepStatus.SUCCEEDED,
                log_lines=["cloning..."],
                truncated=False,
            ),
            StepLog(
                step_name="build-image",
                status=StepStatus.FAILED,
                log_lines=["ERROR: no space left on device"],
                truncated=False,
            ),
            StepLog(step_name="deploy", status=StepStatus.SKIPPED, log_lines=[], truncated=False),
        ]
        result = PipelineRunLogsResult.compute(
            request=PipelineRunLogsRequest(pipeline_run_name="deploy-payment-v2", namespace="ci"),
            steps=steps,
        )
        assert result.failed_step_count == 1
        assert result.failed_steps[0].step_name == "build-image"

    def test_not_found(self) -> None:
        result = PipelineRunLogsResult.compute(
            request=PipelineRunLogsRequest(pipeline_run_name="ghost", namespace="ci"),
            steps=[],
        )
        assert result.pipeline_run_found is False

    def test_still_running(self) -> None:
        steps = [
            StepLog(
                step_name="clone-repo",
                status=StepStatus.RUNNING,
                log_lines=["progress..."],
                truncated=False,
            ),
        ]
        result = PipelineRunLogsResult.compute(
            request=PipelineRunLogsRequest(pipeline_run_name="deploy-v3", namespace="ci"),
            steps=steps,
        )
        assert result.is_still_running is True

    def test_truncation_in_compute(self) -> None:
        lines = [f"line {i}" for i in range(600)]
        steps = [
            StepLog(
                step_name="big-step", status=StepStatus.SUCCEEDED, log_lines=lines, truncated=False
            ),
        ]
        result = PipelineRunLogsResult.compute(
            request=PipelineRunLogsRequest(pipeline_run_name="verbose", namespace="ci"),
            steps=steps,
        )
        assert result.steps[0].truncated is True
        assert len(result.steps[0].log_lines) == 500  # noqa: PLR2004
