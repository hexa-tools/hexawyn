from __future__ import annotations

from dataclasses import dataclass

from hexawyn.application.ports.driven.tekton_port import TaskRunInfo
from hexawyn.domain.models.namespace_event import NamespaceEvent
from hexawyn.domain.models.pipeline_run_logs import StepLog, StepStatus

_ERROR_STATUSES = frozenset({"Failed", "Timeout"})


@dataclass(frozen=True)
class PipelineTimelineEntry:
    """One ordered piece of evidence in a failed pipeline run.

    ``timestamp`` is an ISO string or ``None`` (unknown bucket, sorted last).
    ``source`` is one of ``step_log`` / ``task_run`` / ``termination`` / ``event``.
    """

    timestamp: str | None
    source: str
    step_name: str
    severity: str
    message: str
    task_run_id: str | None = None


@dataclass(frozen=True)
class PipelineTimeline:
    """An ordered timeline of failure evidence for a pipeline.

    Entries are sorted by timestamp (stable), with unknown-timestamp entries
    sorted last. ``first_failure`` is the earliest error/warning entry.
    """

    entries: tuple[PipelineTimelineEntry, ...]
    first_failure: PipelineTimelineEntry | None
    failure_count: int


def build_pipeline_timeline(
    step_logs: list[StepLog],
    task_runs: list[TaskRunInfo],
    termination_reasons: list[str],
    events: list[NamespaceEvent] | None,
) -> PipelineTimeline:
    """Assemble an ordered failure timeline from pipeline evidence.

    Pure domain function: no I/O, no imports beyond the domain models. Mixed
    sources are merged, deduplicated, and stably sorted by timestamp with
    ``None`` (unknown) timestamps placed last. Never raises on missing data.
    """
    entries = (
        _from_task_runs(task_runs)
        + _from_step_logs(step_logs)
        + [
            PipelineTimelineEntry(
                timestamp=None,
                source="termination",
                step_name="",
                severity="error",
                message=reason,
            )
            for reason in termination_reasons
        ]
        + _from_events(events or [])
    )

    ordered = _sort(_dedup(entries))
    failure_count = sum(1 for entry in ordered if entry.severity == "error")
    first_failure = next(
        (entry for entry in ordered if entry.severity in {"error", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def _from_task_runs(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def _from_step_logs(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="step_log",
            step_name=log.step_name,
            severity=_step_severity(log.status),
            message=log.log_lines[-1] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]


def _from_events(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=event.last_seen,
            source="event",
            step_name=event.object,
            severity=_event_severity(event.event_type),
            message=event.message,
        )
        for event in events
    ]


def _status_severity(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "error"
    if status == "Running":
        return "warning"
    return "info"


def _step_severity(status: StepStatus) -> str:
    if status == StepStatus.FAILED:
        return "error"
    if status in (StepStatus.RUNNING, StepStatus.SKIPPED):
        return "warning"
    return "info"


def _event_severity(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def _dedup(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    seen: set[tuple[str, str, str | None]] = set()
    result: list[PipelineTimelineEntry] = []
    for entry in entries:
        key = (entry.source, entry.message, entry.timestamp)
        if key in seen:
            continue
        seen.add(key)
        result.append(entry)
    return result


def _sort(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    return sorted(entries, key=lambda entry: (entry.timestamp is None, entry.timestamp or ""))
