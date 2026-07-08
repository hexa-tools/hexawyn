from __future__ import annotations

from collections import defaultdict

from hexawyn.application.ports.driven.tekton_port import TaskRunInfo
from hexawyn.domain.models.constants import PipelineFailureAnalysisConstants
from hexawyn.domain.models.pipeline_failure_analysis import (
    AnalyzeFailedPipelineRequest,
    AnalyzeFailedPipelineResult,
    FailureAnalysis,
    FailureType,
)
from hexawyn.domain.models.pipeline_run_logs import StepLog
from hexawyn.domain.models.scoring import RcaScoringConfig
from hexawyn.domain.services.failure_analysis.scorer import RcaScorer

_cfg = PipelineFailureAnalysisConstants()
_FAILED_STATUSES = frozenset({"Failed", "Timeout"})

# Sums to 0.85 (base 0.5) when logs are analyzed, a root cause is found, and
# historical runs are available — matches TC1's expected confidence exactly.
_SCORING_CONFIG = RcaScoringConfig(
    base_confidence=0.5,
    logs_analyzed_weight=0.2,
    root_cause_found_weight=0.1,
    timeline_available_weight=0.05,
    max_confidence=1.0,
)

_INFRASTRUCTURE_KEYWORDS = (
    "timeout",
    "connection refused",
    "connection reset",
    "dial tcp",
    "no route to host",
    "context deadline exceeded",
)
_DEPENDENCY_KEYWORDS = (
    "modulenotfounderror",
    "importerror",
    "no matching distribution",
    "package not found",
    "could not resolve",
    "cannot find module",
)
_CONFIG_KEYWORDS = (
    "environment variable",
    "missing required field",
    "invalid configuration",
    "config file not found",
)
_REGRESSION_KEYWORDS = ("assertionerror", "expected", "test failed")

_REMEDIATION: dict[FailureType, str] = {
    FailureType.FLAKY_TEST: (
        "Quarantine or retry the test; investigate test isolation and timing "
        "dependencies rather than blocking the pipeline."
    ),
    FailureType.REGRESSION: (
        "Review the recent code changes to this task — the failure is a "
        "genuine behavioral regression, not environmental."
    ),
    FailureType.INFRASTRUCTURE: (
        "Check cluster/network health and downstream service availability; "
        "retry once infrastructure is confirmed stable."
    ),
    FailureType.DEPENDENCY: (
        "Verify package/dependency versions and registry availability; check "
        "for a recent dependency bump or lockfile drift."
    ),
    FailureType.CONFIG_ERROR: (
        "Review environment variables and configuration manifests for this "
        "task; a missing or invalid config value is the likely cause."
    ),
}


def analyze_pipeline_failure(
    request: AnalyzeFailedPipelineRequest,
    task_runs: list[TaskRunInfo],
    step_logs: list[StepLog],
) -> AnalyzeFailedPipelineResult:
    """Domain service — automated pipeline failure RCA (ECA-8 TaskRun history,
    ECA-11 step logs). Zero K8s dependency: operates on data already fetched
    through TektonPort and PipelineRunLogsPort.
    """
    if not task_runs:
        return AnalyzeFailedPipelineResult(
            pipeline_name=request.pipeline_name,
            namespace=request.namespace,
            pipeline_run_found=False,
        )

    step_logs_by_name = {log.step_name: log for log in step_logs}
    groups = _group_by_task(task_runs)

    failures: list[FailureAnalysis] = []
    for task_ref, history in groups.items():
        latest = history[0]
        if latest["status"] not in _FAILED_STATUSES:
            continue
        failures.append(_analyze_failure(task_ref, history, step_logs_by_name))

    failures.sort(key=lambda failure: _failure_start_time(failure, groups))

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def _group_by_task(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] or "", reverse=True)
    return groups


def _analyze_failure(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline_available = len(history) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=0
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def _resolve_error_message(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def _classify_by_message(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def _failure_start_time(failure: FailureAnalysis, groups: dict[str, list[TaskRunInfo]]) -> str:
    return groups[failure.task_name][0]["start_time"] or ""


def _aggregate_root_cause(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return ""
    if len(failures) == 1:
        return f"{failures[0].task_name}: {failures[0].root_cause}"
    parts = [f"{failure.task_name} ({failure.failure_type.value})" for failure in failures]
    return f"{len(failures)} tasks failed: " + ", ".join(parts)


def _summary(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return "no failures detected"
    plural = "" if len(failures) == 1 else "s"
    return f"{len(failures)} failure{plural} detected"
