from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

MAX_LOG_LINES: int = 500


class StepStatus(Enum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    RUNNING = "running"
    SKIPPED = "skipped"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class StepLog:
    step_name: str
    status: StepStatus
    log_lines: list[str]
    truncated: bool


@dataclass(frozen=True)
class PipelineRunLogsRequest:
    pipeline_run_name: str
    namespace: str


@dataclass(frozen=True)
class PipelineRunLogsResult:
    pipeline_run_name: str
    namespace: str
    pipeline_run_found: bool
    is_still_running: bool
    steps: list[StepLog]
    failed_steps: list[StepLog]
    failed_step_count: int
    total_step_count: int

    @staticmethod
    def compute(
        request: PipelineRunLogsRequest,
        steps: list[StepLog],
    ) -> PipelineRunLogsResult:
        failed = [s for s in steps if s.status == StepStatus.FAILED]
        running = any(s.status == StepStatus.RUNNING for s in steps)

        truncated_steps: list[StepLog] = []
        for s in steps:
            if len(s.log_lines) > MAX_LOG_LINES:
                truncated_steps.append(
                    StepLog(
                        step_name=s.step_name,
                        status=s.status,
                        log_lines=s.log_lines[-MAX_LOG_LINES:],
                        truncated=True,
                    )
                )
            else:
                truncated_steps.append(s)

        return PipelineRunLogsResult(
            pipeline_run_name=request.pipeline_run_name,
            namespace=request.namespace,
            pipeline_run_found=len(steps) > 0,
            is_still_running=running,
            steps=truncated_steps,
            failed_steps=failed,
            failed_step_count=len(failed),
            total_step_count=len(steps),
        )
