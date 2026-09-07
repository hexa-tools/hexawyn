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
from hexawyn.domain.services.failure_analysis.timeline import build_pipeline_timeline

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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_analyze_pipeline_failure__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_analyze_pipeline_failure__mutmut)
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


def x_analyze_pipeline_failure__mutmut_orig(
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


def x_analyze_pipeline_failure__mutmut_1(
    request: AnalyzeFailedPipelineRequest,
    task_runs: list[TaskRunInfo],
    step_logs: list[StepLog],
) -> AnalyzeFailedPipelineResult:
    """Domain service — automated pipeline failure RCA (ECA-8 TaskRun history,
    ECA-11 step logs). Zero K8s dependency: operates on data already fetched
    through TektonPort and PipelineRunLogsPort.
    """
    if task_runs:
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


def x_analyze_pipeline_failure__mutmut_2(
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
            pipeline_name=None,
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


def x_analyze_pipeline_failure__mutmut_3(
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
            namespace=None,
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


def x_analyze_pipeline_failure__mutmut_4(
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
            pipeline_run_found=None,
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


def x_analyze_pipeline_failure__mutmut_5(
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


def x_analyze_pipeline_failure__mutmut_6(
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


def x_analyze_pipeline_failure__mutmut_7(
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


def x_analyze_pipeline_failure__mutmut_8(
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
            pipeline_run_found=True,
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


def x_analyze_pipeline_failure__mutmut_9(
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

    step_logs_by_name = None
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


def x_analyze_pipeline_failure__mutmut_10(
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
    groups = None

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


def x_analyze_pipeline_failure__mutmut_11(
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
    groups = _group_by_task(None)

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


def x_analyze_pipeline_failure__mutmut_12(
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

    failures: list[FailureAnalysis] = None
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


def x_analyze_pipeline_failure__mutmut_13(
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
        latest = None
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


def x_analyze_pipeline_failure__mutmut_14(
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
        latest = history[1]
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


def x_analyze_pipeline_failure__mutmut_15(
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
        if latest["XXstatusXX"] not in _FAILED_STATUSES:
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


def x_analyze_pipeline_failure__mutmut_16(
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
        if latest["STATUS"] not in _FAILED_STATUSES:
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


def x_analyze_pipeline_failure__mutmut_17(
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
        if latest["status"] in _FAILED_STATUSES:
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


def x_analyze_pipeline_failure__mutmut_18(
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
            break
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


def x_analyze_pipeline_failure__mutmut_19(
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
        failures.append(None)

    failures.sort(key=lambda failure: _failure_start_time(failure, groups))

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_20(
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
        failures.append(_analyze_failure(None, history, step_logs_by_name))

    failures.sort(key=lambda failure: _failure_start_time(failure, groups))

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_21(
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
        failures.append(_analyze_failure(task_ref, None, step_logs_by_name))

    failures.sort(key=lambda failure: _failure_start_time(failure, groups))

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_22(
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
        failures.append(_analyze_failure(task_ref, history, None))

    failures.sort(key=lambda failure: _failure_start_time(failure, groups))

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_23(
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
        failures.append(_analyze_failure(history, step_logs_by_name))

    failures.sort(key=lambda failure: _failure_start_time(failure, groups))

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_24(
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
        failures.append(_analyze_failure(task_ref, step_logs_by_name))

    failures.sort(key=lambda failure: _failure_start_time(failure, groups))

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_25(
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
        failures.append(_analyze_failure(task_ref, history, ))

    failures.sort(key=lambda failure: _failure_start_time(failure, groups))

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_26(
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

    failures.sort(key=None)

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_27(
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

    failures.sort(key=lambda failure: None)

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_28(
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

    failures.sort(key=lambda failure: _failure_start_time(None, groups))

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_29(
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

    failures.sort(key=lambda failure: _failure_start_time(failure, None))

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_30(
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

    failures.sort(key=lambda failure: _failure_start_time(groups))

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_31(
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

    failures.sort(key=lambda failure: _failure_start_time(failure, ))

    return AnalyzeFailedPipelineResult(
        pipeline_name=request.pipeline_name,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_32(
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
        pipeline_name=None,
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_33(
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
        namespace=None,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_34(
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
        pipeline_run_found=None,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_35(
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
        failures=None,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_36(
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
        aggregated_root_cause=None,
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_37(
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
        summary=None,
    )


def x_analyze_pipeline_failure__mutmut_38(
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
        namespace=request.namespace,
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_39(
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
        pipeline_run_found=True,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_40(
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
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_41(
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
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_42(
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
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_43(
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
        )


def x_analyze_pipeline_failure__mutmut_44(
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
        pipeline_run_found=False,
        failures=failures,
        aggregated_root_cause=_aggregate_root_cause(failures),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_45(
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
        aggregated_root_cause=_aggregate_root_cause(None),
        summary=_summary(failures),
    )


def x_analyze_pipeline_failure__mutmut_46(
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
        summary=_summary(None),
    )

mutants_x_analyze_pipeline_failure__mutmut['_mutmut_orig'] = x_analyze_pipeline_failure__mutmut_orig # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_1'] = x_analyze_pipeline_failure__mutmut_1 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_2'] = x_analyze_pipeline_failure__mutmut_2 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_3'] = x_analyze_pipeline_failure__mutmut_3 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_4'] = x_analyze_pipeline_failure__mutmut_4 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_5'] = x_analyze_pipeline_failure__mutmut_5 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_6'] = x_analyze_pipeline_failure__mutmut_6 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_7'] = x_analyze_pipeline_failure__mutmut_7 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_8'] = x_analyze_pipeline_failure__mutmut_8 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_9'] = x_analyze_pipeline_failure__mutmut_9 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_10'] = x_analyze_pipeline_failure__mutmut_10 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_11'] = x_analyze_pipeline_failure__mutmut_11 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_12'] = x_analyze_pipeline_failure__mutmut_12 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_13'] = x_analyze_pipeline_failure__mutmut_13 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_14'] = x_analyze_pipeline_failure__mutmut_14 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_15'] = x_analyze_pipeline_failure__mutmut_15 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_16'] = x_analyze_pipeline_failure__mutmut_16 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_17'] = x_analyze_pipeline_failure__mutmut_17 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_18'] = x_analyze_pipeline_failure__mutmut_18 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_19'] = x_analyze_pipeline_failure__mutmut_19 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_20'] = x_analyze_pipeline_failure__mutmut_20 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_21'] = x_analyze_pipeline_failure__mutmut_21 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_22'] = x_analyze_pipeline_failure__mutmut_22 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_23'] = x_analyze_pipeline_failure__mutmut_23 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_24'] = x_analyze_pipeline_failure__mutmut_24 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_25'] = x_analyze_pipeline_failure__mutmut_25 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_26'] = x_analyze_pipeline_failure__mutmut_26 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_27'] = x_analyze_pipeline_failure__mutmut_27 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_28'] = x_analyze_pipeline_failure__mutmut_28 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_29'] = x_analyze_pipeline_failure__mutmut_29 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_30'] = x_analyze_pipeline_failure__mutmut_30 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_31'] = x_analyze_pipeline_failure__mutmut_31 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_32'] = x_analyze_pipeline_failure__mutmut_32 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_33'] = x_analyze_pipeline_failure__mutmut_33 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_34'] = x_analyze_pipeline_failure__mutmut_34 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_35'] = x_analyze_pipeline_failure__mutmut_35 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_36'] = x_analyze_pipeline_failure__mutmut_36 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_37'] = x_analyze_pipeline_failure__mutmut_37 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_38'] = x_analyze_pipeline_failure__mutmut_38 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_39'] = x_analyze_pipeline_failure__mutmut_39 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_40'] = x_analyze_pipeline_failure__mutmut_40 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_41'] = x_analyze_pipeline_failure__mutmut_41 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_42'] = x_analyze_pipeline_failure__mutmut_42 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_43'] = x_analyze_pipeline_failure__mutmut_43 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_44'] = x_analyze_pipeline_failure__mutmut_44 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_45'] = x_analyze_pipeline_failure__mutmut_45 # type: ignore # mutmut generated
mutants_x_analyze_pipeline_failure__mutmut['x_analyze_pipeline_failure__mutmut_46'] = x_analyze_pipeline_failure__mutmut_46 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__group_by_task__mutmut)
def _group_by_task(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] or "", reverse=True)
    return groups


def x__group_by_task__mutmut_orig(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] or "", reverse=True)
    return groups


def x__group_by_task__mutmut_1(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = None
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] or "", reverse=True)
    return groups


def x__group_by_task__mutmut_2(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(None)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] or "", reverse=True)
    return groups


def x__group_by_task__mutmut_3(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(None)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] or "", reverse=True)
    return groups


def x__group_by_task__mutmut_4(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["XXtask_refXX"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] or "", reverse=True)
    return groups


def x__group_by_task__mutmut_5(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["TASK_REF"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] or "", reverse=True)
    return groups


def x__group_by_task__mutmut_6(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=None, reverse=True)
    return groups


def x__group_by_task__mutmut_7(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] or "", reverse=None)
    return groups


def x__group_by_task__mutmut_8(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(reverse=True)
    return groups


def x__group_by_task__mutmut_9(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] or "", )
    return groups


def x__group_by_task__mutmut_10(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: None, reverse=True)
    return groups


def x__group_by_task__mutmut_11(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] and "", reverse=True)
    return groups


def x__group_by_task__mutmut_12(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["XXstart_timeXX"] or "", reverse=True)
    return groups


def x__group_by_task__mutmut_13(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["START_TIME"] or "", reverse=True)
    return groups


def x__group_by_task__mutmut_14(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] or "XXXX", reverse=True)
    return groups


def x__group_by_task__mutmut_15(task_runs: list[TaskRunInfo]) -> dict[str, list[TaskRunInfo]]:
    groups: dict[str, list[TaskRunInfo]] = defaultdict(list)
    for run in task_runs:
        groups[run["task_ref"]].append(run)
    for history in groups.values():
        history.sort(key=lambda run: run["start_time"] or "", reverse=False)
    return groups

mutants_x__group_by_task__mutmut['_mutmut_orig'] = x__group_by_task__mutmut_orig # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_1'] = x__group_by_task__mutmut_1 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_2'] = x__group_by_task__mutmut_2 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_3'] = x__group_by_task__mutmut_3 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_4'] = x__group_by_task__mutmut_4 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_5'] = x__group_by_task__mutmut_5 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_6'] = x__group_by_task__mutmut_6 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_7'] = x__group_by_task__mutmut_7 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_8'] = x__group_by_task__mutmut_8 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_9'] = x__group_by_task__mutmut_9 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_10'] = x__group_by_task__mutmut_10 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_11'] = x__group_by_task__mutmut_11 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_12'] = x__group_by_task__mutmut_12 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_13'] = x__group_by_task__mutmut_13 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_14'] = x__group_by_task__mutmut_14 # type: ignore # mutmut generated
mutants_x__group_by_task__mutmut['x__group_by_task__mutmut_15'] = x__group_by_task__mutmut_15 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__analyze_failure__mutmut)
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_orig(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_1(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = None
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_2(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[1]
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_3(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = None

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_4(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(None, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_5(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, None)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_6(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_7(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, )

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_8(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = None
    failures_in_window = sum(1 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_9(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = None
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_10(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(None)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_11(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(2 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_12(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["XXstatusXX"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_13(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["STATUS"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_14(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["status"] not in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_15(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = None

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_16(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures < failures_in_window < len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_17(
    task_ref: str,
    history: list[TaskRunInfo],
    step_logs_by_name: dict[str, StepLog],
) -> FailureAnalysis:
    latest = history[0]
    root_cause = _resolve_error_message(latest, step_logs_by_name)

    window = history[: _cfg.flaky_test_window_runs]
    failures_in_window = sum(1 for run in window if run["status"] in _FAILED_STATUSES)
    is_flaky = _cfg.flaky_test_min_failures <= failures_in_window <= len(window)

    if is_flaky:
        failure_type = FailureType.FLAKY_TEST
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_18(
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
        failure_type = None
        matched_known_pattern = True
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_19(
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
        matched_known_pattern = None
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_20(
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
        matched_known_pattern = False
    else:
        failure_type, matched_known_pattern = _classify_by_message(root_cause)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_21(
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
        failure_type, matched_known_pattern = None

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_22(
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
        failure_type, matched_known_pattern = _classify_by_message(None)

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_23(
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

    timeline = None
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_24(
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

    timeline = build_pipeline_timeline(
        step_logs=None,
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_25(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=None,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_26(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=None,
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_27(
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

    timeline = build_pipeline_timeline(
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_28(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_29(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_30(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_31(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(None, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_32(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, None),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_33(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_34(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, ),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_35(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = None
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_36(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) >= 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_37(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 2
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_38(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = None
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_39(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=None,
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_40(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=None,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_41(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=None,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_42(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_43(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_44(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_45(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(None).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_46(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(None),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_47(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = None

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_48(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=None, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_49(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=None, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_50(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=None
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_51(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_52(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_53(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_54(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(None).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_55(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=2, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_56(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=1, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_57(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=None,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_58(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=None,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_59(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=None,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_60(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=None,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_61(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=None,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_62(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=None,
    )


def x__analyze_failure__mutmut_63(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_64(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_65(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        confidence=confidence.value,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_66(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        impact_score=impact.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_67(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        remediation=_REMEDIATION[failure_type],
    )


def x__analyze_failure__mutmut_68(
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

    timeline = build_pipeline_timeline(
        step_logs=_step_logs_for(latest, step_logs_by_name),
        task_runs=history,
        termination_reasons=[],
        events=None,
    )
    timeline_available = len(timeline.entries) > 1
    confidence = RcaScorer(_SCORING_CONFIG).calculate_confidence(
        logs_analyzed=bool(root_cause),
        root_cause_found=matched_known_pattern,
        timeline_available=timeline_available,
    )
    impact = RcaScorer(_SCORING_CONFIG).calculate_impact(
        affected_tasks=1, related_incidents=0, timeline_events=len(timeline.entries)
    )

    return FailureAnalysis(
        task_name=task_ref,
        root_cause=root_cause,
        failure_type=failure_type,
        confidence=confidence.value,
        impact_score=impact.value,
        )

mutants_x__analyze_failure__mutmut['_mutmut_orig'] = x__analyze_failure__mutmut_orig # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_1'] = x__analyze_failure__mutmut_1 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_2'] = x__analyze_failure__mutmut_2 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_3'] = x__analyze_failure__mutmut_3 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_4'] = x__analyze_failure__mutmut_4 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_5'] = x__analyze_failure__mutmut_5 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_6'] = x__analyze_failure__mutmut_6 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_7'] = x__analyze_failure__mutmut_7 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_8'] = x__analyze_failure__mutmut_8 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_9'] = x__analyze_failure__mutmut_9 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_10'] = x__analyze_failure__mutmut_10 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_11'] = x__analyze_failure__mutmut_11 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_12'] = x__analyze_failure__mutmut_12 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_13'] = x__analyze_failure__mutmut_13 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_14'] = x__analyze_failure__mutmut_14 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_15'] = x__analyze_failure__mutmut_15 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_16'] = x__analyze_failure__mutmut_16 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_17'] = x__analyze_failure__mutmut_17 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_18'] = x__analyze_failure__mutmut_18 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_19'] = x__analyze_failure__mutmut_19 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_20'] = x__analyze_failure__mutmut_20 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_21'] = x__analyze_failure__mutmut_21 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_22'] = x__analyze_failure__mutmut_22 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_23'] = x__analyze_failure__mutmut_23 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_24'] = x__analyze_failure__mutmut_24 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_25'] = x__analyze_failure__mutmut_25 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_26'] = x__analyze_failure__mutmut_26 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_27'] = x__analyze_failure__mutmut_27 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_28'] = x__analyze_failure__mutmut_28 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_29'] = x__analyze_failure__mutmut_29 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_30'] = x__analyze_failure__mutmut_30 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_31'] = x__analyze_failure__mutmut_31 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_32'] = x__analyze_failure__mutmut_32 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_33'] = x__analyze_failure__mutmut_33 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_34'] = x__analyze_failure__mutmut_34 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_35'] = x__analyze_failure__mutmut_35 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_36'] = x__analyze_failure__mutmut_36 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_37'] = x__analyze_failure__mutmut_37 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_38'] = x__analyze_failure__mutmut_38 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_39'] = x__analyze_failure__mutmut_39 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_40'] = x__analyze_failure__mutmut_40 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_41'] = x__analyze_failure__mutmut_41 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_42'] = x__analyze_failure__mutmut_42 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_43'] = x__analyze_failure__mutmut_43 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_44'] = x__analyze_failure__mutmut_44 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_45'] = x__analyze_failure__mutmut_45 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_46'] = x__analyze_failure__mutmut_46 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_47'] = x__analyze_failure__mutmut_47 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_48'] = x__analyze_failure__mutmut_48 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_49'] = x__analyze_failure__mutmut_49 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_50'] = x__analyze_failure__mutmut_50 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_51'] = x__analyze_failure__mutmut_51 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_52'] = x__analyze_failure__mutmut_52 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_53'] = x__analyze_failure__mutmut_53 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_54'] = x__analyze_failure__mutmut_54 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_55'] = x__analyze_failure__mutmut_55 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_56'] = x__analyze_failure__mutmut_56 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_57'] = x__analyze_failure__mutmut_57 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_58'] = x__analyze_failure__mutmut_58 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_59'] = x__analyze_failure__mutmut_59 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_60'] = x__analyze_failure__mutmut_60 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_61'] = x__analyze_failure__mutmut_61 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_62'] = x__analyze_failure__mutmut_62 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_63'] = x__analyze_failure__mutmut_63 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_64'] = x__analyze_failure__mutmut_64 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_65'] = x__analyze_failure__mutmut_65 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_66'] = x__analyze_failure__mutmut_66 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_67'] = x__analyze_failure__mutmut_67 # type: ignore # mutmut generated
mutants_x__analyze_failure__mutmut['x__analyze_failure__mutmut_68'] = x__analyze_failure__mutmut_68 # type: ignore # mutmut generated
mutants_x__step_logs_for__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__step_logs_for__mutmut)
def _step_logs_for(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> list[StepLog]:
    failing_step = task.get("failing_step")
    if failing_step and failing_step in step_logs_by_name:
        return [step_logs_by_name[failing_step]]
    return []


def x__step_logs_for__mutmut_orig(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> list[StepLog]:
    failing_step = task.get("failing_step")
    if failing_step and failing_step in step_logs_by_name:
        return [step_logs_by_name[failing_step]]
    return []


def x__step_logs_for__mutmut_1(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> list[StepLog]:
    failing_step = None
    if failing_step and failing_step in step_logs_by_name:
        return [step_logs_by_name[failing_step]]
    return []


def x__step_logs_for__mutmut_2(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> list[StepLog]:
    failing_step = task.get(None)
    if failing_step and failing_step in step_logs_by_name:
        return [step_logs_by_name[failing_step]]
    return []


def x__step_logs_for__mutmut_3(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> list[StepLog]:
    failing_step = task.get("XXfailing_stepXX")
    if failing_step and failing_step in step_logs_by_name:
        return [step_logs_by_name[failing_step]]
    return []


def x__step_logs_for__mutmut_4(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> list[StepLog]:
    failing_step = task.get("FAILING_STEP")
    if failing_step and failing_step in step_logs_by_name:
        return [step_logs_by_name[failing_step]]
    return []


def x__step_logs_for__mutmut_5(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> list[StepLog]:
    failing_step = task.get("failing_step")
    if failing_step or failing_step in step_logs_by_name:
        return [step_logs_by_name[failing_step]]
    return []


def x__step_logs_for__mutmut_6(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> list[StepLog]:
    failing_step = task.get("failing_step")
    if failing_step and failing_step not in step_logs_by_name:
        return [step_logs_by_name[failing_step]]
    return []

mutants_x__step_logs_for__mutmut['_mutmut_orig'] = x__step_logs_for__mutmut_orig # type: ignore # mutmut generated
mutants_x__step_logs_for__mutmut['x__step_logs_for__mutmut_1'] = x__step_logs_for__mutmut_1 # type: ignore # mutmut generated
mutants_x__step_logs_for__mutmut['x__step_logs_for__mutmut_2'] = x__step_logs_for__mutmut_2 # type: ignore # mutmut generated
mutants_x__step_logs_for__mutmut['x__step_logs_for__mutmut_3'] = x__step_logs_for__mutmut_3 # type: ignore # mutmut generated
mutants_x__step_logs_for__mutmut['x__step_logs_for__mutmut_4'] = x__step_logs_for__mutmut_4 # type: ignore # mutmut generated
mutants_x__step_logs_for__mutmut['x__step_logs_for__mutmut_5'] = x__step_logs_for__mutmut_5 # type: ignore # mutmut generated
mutants_x__step_logs_for__mutmut['x__step_logs_for__mutmut_6'] = x__step_logs_for__mutmut_6 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__resolve_error_message__mutmut)
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


def x__resolve_error_message__mutmut_orig(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
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


def x__resolve_error_message__mutmut_1(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = None
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_2(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get(None)
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_3(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("XXfailing_stepXX")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_4(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("FAILING_STEP")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_5(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = None
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_6(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") and ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_7(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get(None) or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_8(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("XXfailing_step_errorXX") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_9(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("FAILING_STEP_ERROR") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_10(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or "XXXX"
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_11(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_12(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(None) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_13(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines or (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_14(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log or step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_15(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error and failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_16(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_17(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith(None))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_18(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("XXexit codeXX"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_19(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("EXIT CODE"))
    ):
        return step_log.log_lines[-1]
    return failing_step_error


def x__resolve_error_message__mutmut_20(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[+1]
    return failing_step_error


def x__resolve_error_message__mutmut_21(task: TaskRunInfo, step_logs_by_name: dict[str, StepLog]) -> str:
    failing_step = task.get("failing_step")
    failing_step_error = task.get("failing_step_error") or ""
    step_log = step_logs_by_name.get(failing_step) if failing_step else None

    if (
        step_log
        and step_log.log_lines
        and (not failing_step_error or failing_step_error.startswith("exit code"))
    ):
        return step_log.log_lines[-2]
    return failing_step_error

mutants_x__resolve_error_message__mutmut['_mutmut_orig'] = x__resolve_error_message__mutmut_orig # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_1'] = x__resolve_error_message__mutmut_1 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_2'] = x__resolve_error_message__mutmut_2 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_3'] = x__resolve_error_message__mutmut_3 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_4'] = x__resolve_error_message__mutmut_4 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_5'] = x__resolve_error_message__mutmut_5 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_6'] = x__resolve_error_message__mutmut_6 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_7'] = x__resolve_error_message__mutmut_7 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_8'] = x__resolve_error_message__mutmut_8 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_9'] = x__resolve_error_message__mutmut_9 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_10'] = x__resolve_error_message__mutmut_10 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_11'] = x__resolve_error_message__mutmut_11 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_12'] = x__resolve_error_message__mutmut_12 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_13'] = x__resolve_error_message__mutmut_13 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_14'] = x__resolve_error_message__mutmut_14 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_15'] = x__resolve_error_message__mutmut_15 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_16'] = x__resolve_error_message__mutmut_16 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_17'] = x__resolve_error_message__mutmut_17 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_18'] = x__resolve_error_message__mutmut_18 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_19'] = x__resolve_error_message__mutmut_19 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_20'] = x__resolve_error_message__mutmut_20 # type: ignore # mutmut generated
mutants_x__resolve_error_message__mutmut['x__resolve_error_message__mutmut_21'] = x__resolve_error_message__mutmut_21 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__classify_by_message__mutmut)
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


def x__classify_by_message__mutmut_orig(error_message: str) -> tuple[FailureType, bool]:
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


def x__classify_by_message__mutmut_1(error_message: str) -> tuple[FailureType, bool]:
    lower = None
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_2(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.upper()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_3(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(None):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_4(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword not in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_5(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, False
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_6(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(None):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_7(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword not in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_8(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, False
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_9(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(None):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_10(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword not in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_11(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, False
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_12(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(None):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_13(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword not in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_14(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, False
    return FailureType.REGRESSION, False


def x__classify_by_message__mutmut_15(error_message: str) -> tuple[FailureType, bool]:
    lower = error_message.lower()
    if any(keyword in lower for keyword in _INFRASTRUCTURE_KEYWORDS):
        return FailureType.INFRASTRUCTURE, True
    if any(keyword in lower for keyword in _DEPENDENCY_KEYWORDS):
        return FailureType.DEPENDENCY, True
    if any(keyword in lower for keyword in _CONFIG_KEYWORDS):
        return FailureType.CONFIG_ERROR, True
    if any(keyword in lower for keyword in _REGRESSION_KEYWORDS):
        return FailureType.REGRESSION, True
    return FailureType.REGRESSION, True

mutants_x__classify_by_message__mutmut['_mutmut_orig'] = x__classify_by_message__mutmut_orig # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_1'] = x__classify_by_message__mutmut_1 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_2'] = x__classify_by_message__mutmut_2 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_3'] = x__classify_by_message__mutmut_3 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_4'] = x__classify_by_message__mutmut_4 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_5'] = x__classify_by_message__mutmut_5 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_6'] = x__classify_by_message__mutmut_6 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_7'] = x__classify_by_message__mutmut_7 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_8'] = x__classify_by_message__mutmut_8 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_9'] = x__classify_by_message__mutmut_9 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_10'] = x__classify_by_message__mutmut_10 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_11'] = x__classify_by_message__mutmut_11 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_12'] = x__classify_by_message__mutmut_12 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_13'] = x__classify_by_message__mutmut_13 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_14'] = x__classify_by_message__mutmut_14 # type: ignore # mutmut generated
mutants_x__classify_by_message__mutmut['x__classify_by_message__mutmut_15'] = x__classify_by_message__mutmut_15 # type: ignore # mutmut generated
mutants_x__failure_start_time__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__failure_start_time__mutmut)
def _failure_start_time(failure: FailureAnalysis, groups: dict[str, list[TaskRunInfo]]) -> str:
    return groups[failure.task_name][0]["start_time"] or ""


def x__failure_start_time__mutmut_orig(failure: FailureAnalysis, groups: dict[str, list[TaskRunInfo]]) -> str:
    return groups[failure.task_name][0]["start_time"] or ""


def x__failure_start_time__mutmut_1(failure: FailureAnalysis, groups: dict[str, list[TaskRunInfo]]) -> str:
    return groups[failure.task_name][0]["start_time"] and ""


def x__failure_start_time__mutmut_2(failure: FailureAnalysis, groups: dict[str, list[TaskRunInfo]]) -> str:
    return groups[failure.task_name][1]["start_time"] or ""


def x__failure_start_time__mutmut_3(failure: FailureAnalysis, groups: dict[str, list[TaskRunInfo]]) -> str:
    return groups[failure.task_name][0]["XXstart_timeXX"] or ""


def x__failure_start_time__mutmut_4(failure: FailureAnalysis, groups: dict[str, list[TaskRunInfo]]) -> str:
    return groups[failure.task_name][0]["START_TIME"] or ""


def x__failure_start_time__mutmut_5(failure: FailureAnalysis, groups: dict[str, list[TaskRunInfo]]) -> str:
    return groups[failure.task_name][0]["start_time"] or "XXXX"

mutants_x__failure_start_time__mutmut['_mutmut_orig'] = x__failure_start_time__mutmut_orig # type: ignore # mutmut generated
mutants_x__failure_start_time__mutmut['x__failure_start_time__mutmut_1'] = x__failure_start_time__mutmut_1 # type: ignore # mutmut generated
mutants_x__failure_start_time__mutmut['x__failure_start_time__mutmut_2'] = x__failure_start_time__mutmut_2 # type: ignore # mutmut generated
mutants_x__failure_start_time__mutmut['x__failure_start_time__mutmut_3'] = x__failure_start_time__mutmut_3 # type: ignore # mutmut generated
mutants_x__failure_start_time__mutmut['x__failure_start_time__mutmut_4'] = x__failure_start_time__mutmut_4 # type: ignore # mutmut generated
mutants_x__failure_start_time__mutmut['x__failure_start_time__mutmut_5'] = x__failure_start_time__mutmut_5 # type: ignore # mutmut generated
mutants_x__aggregate_root_cause__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__aggregate_root_cause__mutmut)
def _aggregate_root_cause(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return ""
    if len(failures) == 1:
        return f"{failures[0].task_name}: {failures[0].root_cause}"
    parts = [f"{failure.task_name} ({failure.failure_type.value})" for failure in failures]
    return f"{len(failures)} tasks failed: " + ", ".join(parts)


def x__aggregate_root_cause__mutmut_orig(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return ""
    if len(failures) == 1:
        return f"{failures[0].task_name}: {failures[0].root_cause}"
    parts = [f"{failure.task_name} ({failure.failure_type.value})" for failure in failures]
    return f"{len(failures)} tasks failed: " + ", ".join(parts)


def x__aggregate_root_cause__mutmut_1(failures: list[FailureAnalysis]) -> str:
    if failures:
        return ""
    if len(failures) == 1:
        return f"{failures[0].task_name}: {failures[0].root_cause}"
    parts = [f"{failure.task_name} ({failure.failure_type.value})" for failure in failures]
    return f"{len(failures)} tasks failed: " + ", ".join(parts)


def x__aggregate_root_cause__mutmut_2(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return "XXXX"
    if len(failures) == 1:
        return f"{failures[0].task_name}: {failures[0].root_cause}"
    parts = [f"{failure.task_name} ({failure.failure_type.value})" for failure in failures]
    return f"{len(failures)} tasks failed: " + ", ".join(parts)


def x__aggregate_root_cause__mutmut_3(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return ""
    if len(failures) != 1:
        return f"{failures[0].task_name}: {failures[0].root_cause}"
    parts = [f"{failure.task_name} ({failure.failure_type.value})" for failure in failures]
    return f"{len(failures)} tasks failed: " + ", ".join(parts)


def x__aggregate_root_cause__mutmut_4(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return ""
    if len(failures) == 2:
        return f"{failures[0].task_name}: {failures[0].root_cause}"
    parts = [f"{failure.task_name} ({failure.failure_type.value})" for failure in failures]
    return f"{len(failures)} tasks failed: " + ", ".join(parts)


def x__aggregate_root_cause__mutmut_5(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return ""
    if len(failures) == 1:
        return f"{failures[1].task_name}: {failures[0].root_cause}"
    parts = [f"{failure.task_name} ({failure.failure_type.value})" for failure in failures]
    return f"{len(failures)} tasks failed: " + ", ".join(parts)


def x__aggregate_root_cause__mutmut_6(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return ""
    if len(failures) == 1:
        return f"{failures[0].task_name}: {failures[1].root_cause}"
    parts = [f"{failure.task_name} ({failure.failure_type.value})" for failure in failures]
    return f"{len(failures)} tasks failed: " + ", ".join(parts)


def x__aggregate_root_cause__mutmut_7(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return ""
    if len(failures) == 1:
        return f"{failures[0].task_name}: {failures[0].root_cause}"
    parts = None
    return f"{len(failures)} tasks failed: " + ", ".join(parts)


def x__aggregate_root_cause__mutmut_8(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return ""
    if len(failures) == 1:
        return f"{failures[0].task_name}: {failures[0].root_cause}"
    parts = [f"{failure.task_name} ({failure.failure_type.value})" for failure in failures]
    return f"{len(failures)} tasks failed: " - ", ".join(parts)


def x__aggregate_root_cause__mutmut_9(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return ""
    if len(failures) == 1:
        return f"{failures[0].task_name}: {failures[0].root_cause}"
    parts = [f"{failure.task_name} ({failure.failure_type.value})" for failure in failures]
    return f"{len(failures)} tasks failed: " + ", ".join(None)


def x__aggregate_root_cause__mutmut_10(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return ""
    if len(failures) == 1:
        return f"{failures[0].task_name}: {failures[0].root_cause}"
    parts = [f"{failure.task_name} ({failure.failure_type.value})" for failure in failures]
    return f"{len(failures)} tasks failed: " + "XX, XX".join(parts)

mutants_x__aggregate_root_cause__mutmut['_mutmut_orig'] = x__aggregate_root_cause__mutmut_orig # type: ignore # mutmut generated
mutants_x__aggregate_root_cause__mutmut['x__aggregate_root_cause__mutmut_1'] = x__aggregate_root_cause__mutmut_1 # type: ignore # mutmut generated
mutants_x__aggregate_root_cause__mutmut['x__aggregate_root_cause__mutmut_2'] = x__aggregate_root_cause__mutmut_2 # type: ignore # mutmut generated
mutants_x__aggregate_root_cause__mutmut['x__aggregate_root_cause__mutmut_3'] = x__aggregate_root_cause__mutmut_3 # type: ignore # mutmut generated
mutants_x__aggregate_root_cause__mutmut['x__aggregate_root_cause__mutmut_4'] = x__aggregate_root_cause__mutmut_4 # type: ignore # mutmut generated
mutants_x__aggregate_root_cause__mutmut['x__aggregate_root_cause__mutmut_5'] = x__aggregate_root_cause__mutmut_5 # type: ignore # mutmut generated
mutants_x__aggregate_root_cause__mutmut['x__aggregate_root_cause__mutmut_6'] = x__aggregate_root_cause__mutmut_6 # type: ignore # mutmut generated
mutants_x__aggregate_root_cause__mutmut['x__aggregate_root_cause__mutmut_7'] = x__aggregate_root_cause__mutmut_7 # type: ignore # mutmut generated
mutants_x__aggregate_root_cause__mutmut['x__aggregate_root_cause__mutmut_8'] = x__aggregate_root_cause__mutmut_8 # type: ignore # mutmut generated
mutants_x__aggregate_root_cause__mutmut['x__aggregate_root_cause__mutmut_9'] = x__aggregate_root_cause__mutmut_9 # type: ignore # mutmut generated
mutants_x__aggregate_root_cause__mutmut['x__aggregate_root_cause__mutmut_10'] = x__aggregate_root_cause__mutmut_10 # type: ignore # mutmut generated
mutants_x__summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__summary__mutmut)
def _summary(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return "no failures detected"
    plural = "" if len(failures) == 1 else "s"
    return f"{len(failures)} failure{plural} detected"


def x__summary__mutmut_orig(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return "no failures detected"
    plural = "" if len(failures) == 1 else "s"
    return f"{len(failures)} failure{plural} detected"


def x__summary__mutmut_1(failures: list[FailureAnalysis]) -> str:
    if failures:
        return "no failures detected"
    plural = "" if len(failures) == 1 else "s"
    return f"{len(failures)} failure{plural} detected"


def x__summary__mutmut_2(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return "XXno failures detectedXX"
    plural = "" if len(failures) == 1 else "s"
    return f"{len(failures)} failure{plural} detected"


def x__summary__mutmut_3(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return "NO FAILURES DETECTED"
    plural = "" if len(failures) == 1 else "s"
    return f"{len(failures)} failure{plural} detected"


def x__summary__mutmut_4(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return "no failures detected"
    plural = None
    return f"{len(failures)} failure{plural} detected"


def x__summary__mutmut_5(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return "no failures detected"
    plural = "XXXX" if len(failures) == 1 else "s"
    return f"{len(failures)} failure{plural} detected"


def x__summary__mutmut_6(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return "no failures detected"
    plural = "" if len(failures) != 1 else "s"
    return f"{len(failures)} failure{plural} detected"


def x__summary__mutmut_7(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return "no failures detected"
    plural = "" if len(failures) == 2 else "s"
    return f"{len(failures)} failure{plural} detected"


def x__summary__mutmut_8(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return "no failures detected"
    plural = "" if len(failures) == 1 else "XXsXX"
    return f"{len(failures)} failure{plural} detected"


def x__summary__mutmut_9(failures: list[FailureAnalysis]) -> str:
    if not failures:
        return "no failures detected"
    plural = "" if len(failures) == 1 else "S"
    return f"{len(failures)} failure{plural} detected"

mutants_x__summary__mutmut['_mutmut_orig'] = x__summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_1'] = x__summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_2'] = x__summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_3'] = x__summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_4'] = x__summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_5'] = x__summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_6'] = x__summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_7'] = x__summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_8'] = x__summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_9'] = x__summary__mutmut_9 # type: ignore # mutmut generated
