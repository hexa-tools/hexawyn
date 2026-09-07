from __future__ import annotations

from dataclasses import dataclass

from hexawyn.application.ports.driven.tekton_port import TaskRunInfo
from hexawyn.domain.models.namespace_event import NamespaceEvent
from hexawyn.domain.models.pipeline_run_logs import StepLog, StepStatus

_ERROR_STATUSES = frozenset({"Failed", "Timeout"})


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_x_build_pipeline_timeline__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_pipeline_timeline__mutmut)
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


def x_build_pipeline_timeline__mutmut_orig(
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


def x_build_pipeline_timeline__mutmut_1(
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
    entries = None

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


def x_build_pipeline_timeline__mutmut_2(
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
        ] - _from_events(events or [])
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


def x_build_pipeline_timeline__mutmut_3(
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
        + _from_step_logs(step_logs) - [
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


def x_build_pipeline_timeline__mutmut_4(
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
        _from_task_runs(task_runs) - _from_step_logs(step_logs)
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


def x_build_pipeline_timeline__mutmut_5(
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
        _from_task_runs(None)
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


def x_build_pipeline_timeline__mutmut_6(
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
        + _from_step_logs(None)
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


def x_build_pipeline_timeline__mutmut_7(
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
                source=None,
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


def x_build_pipeline_timeline__mutmut_8(
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
                step_name=None,
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


def x_build_pipeline_timeline__mutmut_9(
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
                severity=None,
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


def x_build_pipeline_timeline__mutmut_10(
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
                message=None,
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


def x_build_pipeline_timeline__mutmut_11(
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


def x_build_pipeline_timeline__mutmut_12(
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


def x_build_pipeline_timeline__mutmut_13(
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


def x_build_pipeline_timeline__mutmut_14(
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


def x_build_pipeline_timeline__mutmut_15(
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


def x_build_pipeline_timeline__mutmut_16(
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
                source="XXterminationXX",
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


def x_build_pipeline_timeline__mutmut_17(
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
                source="TERMINATION",
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


def x_build_pipeline_timeline__mutmut_18(
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
                step_name="XXXX",
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


def x_build_pipeline_timeline__mutmut_19(
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
                severity="XXerrorXX",
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


def x_build_pipeline_timeline__mutmut_20(
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
                severity="ERROR",
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


def x_build_pipeline_timeline__mutmut_21(
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
        + _from_events(None)
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


def x_build_pipeline_timeline__mutmut_22(
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
        + _from_events(events and [])
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


def x_build_pipeline_timeline__mutmut_23(
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

    ordered = None
    failure_count = sum(1 for entry in ordered if entry.severity == "error")
    first_failure = next(
        (entry for entry in ordered if entry.severity in {"error", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_24(
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

    ordered = _sort(None)
    failure_count = sum(1 for entry in ordered if entry.severity == "error")
    first_failure = next(
        (entry for entry in ordered if entry.severity in {"error", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_25(
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

    ordered = _sort(_dedup(None))
    failure_count = sum(1 for entry in ordered if entry.severity == "error")
    first_failure = next(
        (entry for entry in ordered if entry.severity in {"error", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_26(
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
    failure_count = None
    first_failure = next(
        (entry for entry in ordered if entry.severity in {"error", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_27(
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
    failure_count = sum(None)
    first_failure = next(
        (entry for entry in ordered if entry.severity in {"error", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_28(
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
    failure_count = sum(2 for entry in ordered if entry.severity == "error")
    first_failure = next(
        (entry for entry in ordered if entry.severity in {"error", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_29(
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
    failure_count = sum(1 for entry in ordered if entry.severity != "error")
    first_failure = next(
        (entry for entry in ordered if entry.severity in {"error", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_30(
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
    failure_count = sum(1 for entry in ordered if entry.severity == "XXerrorXX")
    first_failure = next(
        (entry for entry in ordered if entry.severity in {"error", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_31(
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
    failure_count = sum(1 for entry in ordered if entry.severity == "ERROR")
    first_failure = next(
        (entry for entry in ordered if entry.severity in {"error", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_32(
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
    first_failure = None
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_33(
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
        None, None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_34(
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
        None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_35(
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
        (entry for entry in ordered if entry.severity in {"error", "warning"}), )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_36(
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
        (entry for entry in ordered if entry.severity not in {"error", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_37(
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
        (entry for entry in ordered if entry.severity in {"XXerrorXX", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_38(
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
        (entry for entry in ordered if entry.severity in {"ERROR", "warning"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_39(
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
        (entry for entry in ordered if entry.severity in {"error", "XXwarningXX"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_40(
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
        (entry for entry in ordered if entry.severity in {"error", "WARNING"}), None
    )
    return PipelineTimeline(
        entries=tuple(ordered),
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_41(
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
        entries=None,
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_42(
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
        first_failure=None,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_43(
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
        failure_count=None,
    )


def x_build_pipeline_timeline__mutmut_44(
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
        first_failure=first_failure,
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_45(
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
        failure_count=failure_count,
    )


def x_build_pipeline_timeline__mutmut_46(
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
        )


def x_build_pipeline_timeline__mutmut_47(
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
        entries=tuple(None),
        first_failure=first_failure,
        failure_count=failure_count,
    )

mutants_x_build_pipeline_timeline__mutmut['_mutmut_orig'] = x_build_pipeline_timeline__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_1'] = x_build_pipeline_timeline__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_2'] = x_build_pipeline_timeline__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_3'] = x_build_pipeline_timeline__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_4'] = x_build_pipeline_timeline__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_5'] = x_build_pipeline_timeline__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_6'] = x_build_pipeline_timeline__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_7'] = x_build_pipeline_timeline__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_8'] = x_build_pipeline_timeline__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_9'] = x_build_pipeline_timeline__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_10'] = x_build_pipeline_timeline__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_11'] = x_build_pipeline_timeline__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_12'] = x_build_pipeline_timeline__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_13'] = x_build_pipeline_timeline__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_14'] = x_build_pipeline_timeline__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_15'] = x_build_pipeline_timeline__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_16'] = x_build_pipeline_timeline__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_17'] = x_build_pipeline_timeline__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_18'] = x_build_pipeline_timeline__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_19'] = x_build_pipeline_timeline__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_20'] = x_build_pipeline_timeline__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_21'] = x_build_pipeline_timeline__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_22'] = x_build_pipeline_timeline__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_23'] = x_build_pipeline_timeline__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_24'] = x_build_pipeline_timeline__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_25'] = x_build_pipeline_timeline__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_26'] = x_build_pipeline_timeline__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_27'] = x_build_pipeline_timeline__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_28'] = x_build_pipeline_timeline__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_29'] = x_build_pipeline_timeline__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_30'] = x_build_pipeline_timeline__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_31'] = x_build_pipeline_timeline__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_32'] = x_build_pipeline_timeline__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_33'] = x_build_pipeline_timeline__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_34'] = x_build_pipeline_timeline__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_35'] = x_build_pipeline_timeline__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_36'] = x_build_pipeline_timeline__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_37'] = x_build_pipeline_timeline__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_38'] = x_build_pipeline_timeline__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_39'] = x_build_pipeline_timeline__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_40'] = x_build_pipeline_timeline__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_41'] = x_build_pipeline_timeline__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_42'] = x_build_pipeline_timeline__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_43'] = x_build_pipeline_timeline__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_44'] = x_build_pipeline_timeline__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_45'] = x_build_pipeline_timeline__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_46'] = x_build_pipeline_timeline__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_pipeline_timeline__mutmut['x_build_pipeline_timeline__mutmut_47'] = x_build_pipeline_timeline__mutmut_47 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__from_task_runs__mutmut)
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


def x__from_task_runs__mutmut_orig(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
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


def x__from_task_runs__mutmut_1(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
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


def x__from_task_runs__mutmut_2(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source=None,
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_3(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=None,
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_4(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=None,
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_5(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=None,
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_6(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=None,
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_7(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
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


def x__from_task_runs__mutmut_8(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_9(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_10(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_11(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_12(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_13(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get(None),
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


def x__from_task_runs__mutmut_14(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("XXstart_timeXX"),
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


def x__from_task_runs__mutmut_15(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("START_TIME"),
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


def x__from_task_runs__mutmut_16(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="XXtask_runXX",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_17(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="TASK_RUN",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_18(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get(None, ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_19(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", None),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_20(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get(""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_21(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_22(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("XXtask_refXX", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_23(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("TASK_REF", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_24(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", "XXXX"),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_25(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(None),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_26(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get(None, "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_27(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", None)),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_28(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_29(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", )),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_30(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("XXstatusXX", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_31(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("STATUS", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_32(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "XXXX")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_33(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step") and run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_34(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error") and run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_35(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get(None)
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_36(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("XXfailing_step_errorXX")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_37(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("FAILING_STEP_ERROR")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_38(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get(None)
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_39(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("XXfailing_stepXX")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_40(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("FAILING_STEP")
            or run.get("status", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_41(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get(None, ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_42(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", None),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_43(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get(""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_44(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_45(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("XXstatusXX", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_46(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("STATUS", ""),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_47(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", "XXXX"),
            task_run_id=run.get("name"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_48(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get(None),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_49(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("XXnameXX"),
        )
        for run in task_runs
    ]


def x__from_task_runs__mutmut_50(task_runs: list[TaskRunInfo]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=run.get("start_time"),
            source="task_run",
            step_name=run.get("task_ref", ""),
            severity=_status_severity(run.get("status", "")),
            message=run.get("failing_step_error")
            or run.get("failing_step")
            or run.get("status", ""),
            task_run_id=run.get("NAME"),
        )
        for run in task_runs
    ]

mutants_x__from_task_runs__mutmut['_mutmut_orig'] = x__from_task_runs__mutmut_orig # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_1'] = x__from_task_runs__mutmut_1 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_2'] = x__from_task_runs__mutmut_2 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_3'] = x__from_task_runs__mutmut_3 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_4'] = x__from_task_runs__mutmut_4 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_5'] = x__from_task_runs__mutmut_5 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_6'] = x__from_task_runs__mutmut_6 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_7'] = x__from_task_runs__mutmut_7 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_8'] = x__from_task_runs__mutmut_8 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_9'] = x__from_task_runs__mutmut_9 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_10'] = x__from_task_runs__mutmut_10 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_11'] = x__from_task_runs__mutmut_11 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_12'] = x__from_task_runs__mutmut_12 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_13'] = x__from_task_runs__mutmut_13 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_14'] = x__from_task_runs__mutmut_14 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_15'] = x__from_task_runs__mutmut_15 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_16'] = x__from_task_runs__mutmut_16 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_17'] = x__from_task_runs__mutmut_17 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_18'] = x__from_task_runs__mutmut_18 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_19'] = x__from_task_runs__mutmut_19 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_20'] = x__from_task_runs__mutmut_20 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_21'] = x__from_task_runs__mutmut_21 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_22'] = x__from_task_runs__mutmut_22 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_23'] = x__from_task_runs__mutmut_23 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_24'] = x__from_task_runs__mutmut_24 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_25'] = x__from_task_runs__mutmut_25 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_26'] = x__from_task_runs__mutmut_26 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_27'] = x__from_task_runs__mutmut_27 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_28'] = x__from_task_runs__mutmut_28 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_29'] = x__from_task_runs__mutmut_29 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_30'] = x__from_task_runs__mutmut_30 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_31'] = x__from_task_runs__mutmut_31 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_32'] = x__from_task_runs__mutmut_32 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_33'] = x__from_task_runs__mutmut_33 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_34'] = x__from_task_runs__mutmut_34 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_35'] = x__from_task_runs__mutmut_35 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_36'] = x__from_task_runs__mutmut_36 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_37'] = x__from_task_runs__mutmut_37 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_38'] = x__from_task_runs__mutmut_38 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_39'] = x__from_task_runs__mutmut_39 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_40'] = x__from_task_runs__mutmut_40 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_41'] = x__from_task_runs__mutmut_41 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_42'] = x__from_task_runs__mutmut_42 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_43'] = x__from_task_runs__mutmut_43 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_44'] = x__from_task_runs__mutmut_44 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_45'] = x__from_task_runs__mutmut_45 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_46'] = x__from_task_runs__mutmut_46 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_47'] = x__from_task_runs__mutmut_47 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_48'] = x__from_task_runs__mutmut_48 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_49'] = x__from_task_runs__mutmut_49 # type: ignore # mutmut generated
mutants_x__from_task_runs__mutmut['x__from_task_runs__mutmut_50'] = x__from_task_runs__mutmut_50 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__from_step_logs__mutmut)
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


def x__from_step_logs__mutmut_orig(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
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


def x__from_step_logs__mutmut_1(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source=None,
            step_name=log.step_name,
            severity=_step_severity(log.status),
            message=log.log_lines[-1] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_2(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="step_log",
            step_name=None,
            severity=_step_severity(log.status),
            message=log.log_lines[-1] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_3(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="step_log",
            step_name=log.step_name,
            severity=None,
            message=log.log_lines[-1] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_4(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="step_log",
            step_name=log.step_name,
            severity=_step_severity(log.status),
            message=None,
        )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_5(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            source="step_log",
            step_name=log.step_name,
            severity=_step_severity(log.status),
            message=log.log_lines[-1] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_6(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            step_name=log.step_name,
            severity=_step_severity(log.status),
            message=log.log_lines[-1] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_7(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="step_log",
            severity=_step_severity(log.status),
            message=log.log_lines[-1] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_8(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="step_log",
            step_name=log.step_name,
            message=log.log_lines[-1] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_9(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="step_log",
            step_name=log.step_name,
            severity=_step_severity(log.status),
            )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_10(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="XXstep_logXX",
            step_name=log.step_name,
            severity=_step_severity(log.status),
            message=log.log_lines[-1] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_11(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="STEP_LOG",
            step_name=log.step_name,
            severity=_step_severity(log.status),
            message=log.log_lines[-1] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_12(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="step_log",
            step_name=log.step_name,
            severity=_step_severity(None),
            message=log.log_lines[-1] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_13(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="step_log",
            step_name=log.step_name,
            severity=_step_severity(log.status),
            message=log.log_lines[+1] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]


def x__from_step_logs__mutmut_14(step_logs: list[StepLog]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="step_log",
            step_name=log.step_name,
            severity=_step_severity(log.status),
            message=log.log_lines[-2] if log.log_lines else log.status.value,
        )
        for log in step_logs
    ]

mutants_x__from_step_logs__mutmut['_mutmut_orig'] = x__from_step_logs__mutmut_orig # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_1'] = x__from_step_logs__mutmut_1 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_2'] = x__from_step_logs__mutmut_2 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_3'] = x__from_step_logs__mutmut_3 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_4'] = x__from_step_logs__mutmut_4 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_5'] = x__from_step_logs__mutmut_5 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_6'] = x__from_step_logs__mutmut_6 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_7'] = x__from_step_logs__mutmut_7 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_8'] = x__from_step_logs__mutmut_8 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_9'] = x__from_step_logs__mutmut_9 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_10'] = x__from_step_logs__mutmut_10 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_11'] = x__from_step_logs__mutmut_11 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_12'] = x__from_step_logs__mutmut_12 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_13'] = x__from_step_logs__mutmut_13 # type: ignore # mutmut generated
mutants_x__from_step_logs__mutmut['x__from_step_logs__mutmut_14'] = x__from_step_logs__mutmut_14 # type: ignore # mutmut generated
mutants_x__from_events__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__from_events__mutmut)
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


def x__from_events__mutmut_orig(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
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


def x__from_events__mutmut_1(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=None,
            source="event",
            step_name=event.object,
            severity=_event_severity(event.event_type),
            message=event.message,
        )
        for event in events
    ]


def x__from_events__mutmut_2(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=event.last_seen,
            source=None,
            step_name=event.object,
            severity=_event_severity(event.event_type),
            message=event.message,
        )
        for event in events
    ]


def x__from_events__mutmut_3(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=event.last_seen,
            source="event",
            step_name=None,
            severity=_event_severity(event.event_type),
            message=event.message,
        )
        for event in events
    ]


def x__from_events__mutmut_4(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=event.last_seen,
            source="event",
            step_name=event.object,
            severity=None,
            message=event.message,
        )
        for event in events
    ]


def x__from_events__mutmut_5(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=event.last_seen,
            source="event",
            step_name=event.object,
            severity=_event_severity(event.event_type),
            message=None,
        )
        for event in events
    ]


def x__from_events__mutmut_6(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            source="event",
            step_name=event.object,
            severity=_event_severity(event.event_type),
            message=event.message,
        )
        for event in events
    ]


def x__from_events__mutmut_7(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=event.last_seen,
            step_name=event.object,
            severity=_event_severity(event.event_type),
            message=event.message,
        )
        for event in events
    ]


def x__from_events__mutmut_8(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=event.last_seen,
            source="event",
            severity=_event_severity(event.event_type),
            message=event.message,
        )
        for event in events
    ]


def x__from_events__mutmut_9(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=event.last_seen,
            source="event",
            step_name=event.object,
            message=event.message,
        )
        for event in events
    ]


def x__from_events__mutmut_10(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=event.last_seen,
            source="event",
            step_name=event.object,
            severity=_event_severity(event.event_type),
            )
        for event in events
    ]


def x__from_events__mutmut_11(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=event.last_seen,
            source="XXeventXX",
            step_name=event.object,
            severity=_event_severity(event.event_type),
            message=event.message,
        )
        for event in events
    ]


def x__from_events__mutmut_12(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=event.last_seen,
            source="EVENT",
            step_name=event.object,
            severity=_event_severity(event.event_type),
            message=event.message,
        )
        for event in events
    ]


def x__from_events__mutmut_13(events: list[NamespaceEvent]) -> list[PipelineTimelineEntry]:
    return [
        PipelineTimelineEntry(
            timestamp=event.last_seen,
            source="event",
            step_name=event.object,
            severity=_event_severity(None),
            message=event.message,
        )
        for event in events
    ]

mutants_x__from_events__mutmut['_mutmut_orig'] = x__from_events__mutmut_orig # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_1'] = x__from_events__mutmut_1 # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_2'] = x__from_events__mutmut_2 # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_3'] = x__from_events__mutmut_3 # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_4'] = x__from_events__mutmut_4 # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_5'] = x__from_events__mutmut_5 # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_6'] = x__from_events__mutmut_6 # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_7'] = x__from_events__mutmut_7 # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_8'] = x__from_events__mutmut_8 # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_9'] = x__from_events__mutmut_9 # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_10'] = x__from_events__mutmut_10 # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_11'] = x__from_events__mutmut_11 # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_12'] = x__from_events__mutmut_12 # type: ignore # mutmut generated
mutants_x__from_events__mutmut['x__from_events__mutmut_13'] = x__from_events__mutmut_13 # type: ignore # mutmut generated
mutants_x__status_severity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__status_severity__mutmut)
def _status_severity(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "error"
    if status == "Running":
        return "warning"
    return "info"


def x__status_severity__mutmut_orig(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "error"
    if status == "Running":
        return "warning"
    return "info"


def x__status_severity__mutmut_1(status: str) -> str:
    if status not in _ERROR_STATUSES:
        return "error"
    if status == "Running":
        return "warning"
    return "info"


def x__status_severity__mutmut_2(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "XXerrorXX"
    if status == "Running":
        return "warning"
    return "info"


def x__status_severity__mutmut_3(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "ERROR"
    if status == "Running":
        return "warning"
    return "info"


def x__status_severity__mutmut_4(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "error"
    if status != "Running":
        return "warning"
    return "info"


def x__status_severity__mutmut_5(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "error"
    if status == "XXRunningXX":
        return "warning"
    return "info"


def x__status_severity__mutmut_6(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "error"
    if status == "running":
        return "warning"
    return "info"


def x__status_severity__mutmut_7(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "error"
    if status == "RUNNING":
        return "warning"
    return "info"


def x__status_severity__mutmut_8(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "error"
    if status == "Running":
        return "XXwarningXX"
    return "info"


def x__status_severity__mutmut_9(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "error"
    if status == "Running":
        return "WARNING"
    return "info"


def x__status_severity__mutmut_10(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "error"
    if status == "Running":
        return "warning"
    return "XXinfoXX"


def x__status_severity__mutmut_11(status: str) -> str:
    if status in _ERROR_STATUSES:
        return "error"
    if status == "Running":
        return "warning"
    return "INFO"

mutants_x__status_severity__mutmut['_mutmut_orig'] = x__status_severity__mutmut_orig # type: ignore # mutmut generated
mutants_x__status_severity__mutmut['x__status_severity__mutmut_1'] = x__status_severity__mutmut_1 # type: ignore # mutmut generated
mutants_x__status_severity__mutmut['x__status_severity__mutmut_2'] = x__status_severity__mutmut_2 # type: ignore # mutmut generated
mutants_x__status_severity__mutmut['x__status_severity__mutmut_3'] = x__status_severity__mutmut_3 # type: ignore # mutmut generated
mutants_x__status_severity__mutmut['x__status_severity__mutmut_4'] = x__status_severity__mutmut_4 # type: ignore # mutmut generated
mutants_x__status_severity__mutmut['x__status_severity__mutmut_5'] = x__status_severity__mutmut_5 # type: ignore # mutmut generated
mutants_x__status_severity__mutmut['x__status_severity__mutmut_6'] = x__status_severity__mutmut_6 # type: ignore # mutmut generated
mutants_x__status_severity__mutmut['x__status_severity__mutmut_7'] = x__status_severity__mutmut_7 # type: ignore # mutmut generated
mutants_x__status_severity__mutmut['x__status_severity__mutmut_8'] = x__status_severity__mutmut_8 # type: ignore # mutmut generated
mutants_x__status_severity__mutmut['x__status_severity__mutmut_9'] = x__status_severity__mutmut_9 # type: ignore # mutmut generated
mutants_x__status_severity__mutmut['x__status_severity__mutmut_10'] = x__status_severity__mutmut_10 # type: ignore # mutmut generated
mutants_x__status_severity__mutmut['x__status_severity__mutmut_11'] = x__status_severity__mutmut_11 # type: ignore # mutmut generated
mutants_x__step_severity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__step_severity__mutmut)
def _step_severity(status: StepStatus) -> str:
    if status == StepStatus.FAILED:
        return "error"
    if status in (StepStatus.RUNNING, StepStatus.SKIPPED):
        return "warning"
    return "info"


def x__step_severity__mutmut_orig(status: StepStatus) -> str:
    if status == StepStatus.FAILED:
        return "error"
    if status in (StepStatus.RUNNING, StepStatus.SKIPPED):
        return "warning"
    return "info"


def x__step_severity__mutmut_1(status: StepStatus) -> str:
    if status != StepStatus.FAILED:
        return "error"
    if status in (StepStatus.RUNNING, StepStatus.SKIPPED):
        return "warning"
    return "info"


def x__step_severity__mutmut_2(status: StepStatus) -> str:
    if status == StepStatus.FAILED:
        return "XXerrorXX"
    if status in (StepStatus.RUNNING, StepStatus.SKIPPED):
        return "warning"
    return "info"


def x__step_severity__mutmut_3(status: StepStatus) -> str:
    if status == StepStatus.FAILED:
        return "ERROR"
    if status in (StepStatus.RUNNING, StepStatus.SKIPPED):
        return "warning"
    return "info"


def x__step_severity__mutmut_4(status: StepStatus) -> str:
    if status == StepStatus.FAILED:
        return "error"
    if status not in (StepStatus.RUNNING, StepStatus.SKIPPED):
        return "warning"
    return "info"


def x__step_severity__mutmut_5(status: StepStatus) -> str:
    if status == StepStatus.FAILED:
        return "error"
    if status in (StepStatus.RUNNING, StepStatus.SKIPPED):
        return "XXwarningXX"
    return "info"


def x__step_severity__mutmut_6(status: StepStatus) -> str:
    if status == StepStatus.FAILED:
        return "error"
    if status in (StepStatus.RUNNING, StepStatus.SKIPPED):
        return "WARNING"
    return "info"


def x__step_severity__mutmut_7(status: StepStatus) -> str:
    if status == StepStatus.FAILED:
        return "error"
    if status in (StepStatus.RUNNING, StepStatus.SKIPPED):
        return "warning"
    return "XXinfoXX"


def x__step_severity__mutmut_8(status: StepStatus) -> str:
    if status == StepStatus.FAILED:
        return "error"
    if status in (StepStatus.RUNNING, StepStatus.SKIPPED):
        return "warning"
    return "INFO"

mutants_x__step_severity__mutmut['_mutmut_orig'] = x__step_severity__mutmut_orig # type: ignore # mutmut generated
mutants_x__step_severity__mutmut['x__step_severity__mutmut_1'] = x__step_severity__mutmut_1 # type: ignore # mutmut generated
mutants_x__step_severity__mutmut['x__step_severity__mutmut_2'] = x__step_severity__mutmut_2 # type: ignore # mutmut generated
mutants_x__step_severity__mutmut['x__step_severity__mutmut_3'] = x__step_severity__mutmut_3 # type: ignore # mutmut generated
mutants_x__step_severity__mutmut['x__step_severity__mutmut_4'] = x__step_severity__mutmut_4 # type: ignore # mutmut generated
mutants_x__step_severity__mutmut['x__step_severity__mutmut_5'] = x__step_severity__mutmut_5 # type: ignore # mutmut generated
mutants_x__step_severity__mutmut['x__step_severity__mutmut_6'] = x__step_severity__mutmut_6 # type: ignore # mutmut generated
mutants_x__step_severity__mutmut['x__step_severity__mutmut_7'] = x__step_severity__mutmut_7 # type: ignore # mutmut generated
mutants_x__step_severity__mutmut['x__step_severity__mutmut_8'] = x__step_severity__mutmut_8 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__event_severity__mutmut)
def _event_severity(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_orig(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_1(event_type: str) -> str:
    lowered = None
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_2(event_type: str) -> str:
    lowered = (event_type or "").upper()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_3(event_type: str) -> str:
    lowered = (event_type and "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_4(event_type: str) -> str:
    lowered = (event_type or "XXXX").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_5(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered not in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_6(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"XXerrorXX", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_7(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"ERROR", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_8(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "XXfailedXX"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_9(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "FAILED"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_10(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "XXerrorXX"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_11(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "ERROR"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_12(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered not in {"warning", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_13(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"XXwarningXX", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_14(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"WARNING", "warn"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_15(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "XXwarnXX"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_16(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "WARN"}:
        return "warning"
    return "info"


def x__event_severity__mutmut_17(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "XXwarningXX"
    return "info"


def x__event_severity__mutmut_18(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "WARNING"
    return "info"


def x__event_severity__mutmut_19(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "XXinfoXX"


def x__event_severity__mutmut_20(event_type: str) -> str:
    lowered = (event_type or "").lower()
    if lowered in {"error", "failed"}:
        return "error"
    if lowered in {"warning", "warn"}:
        return "warning"
    return "INFO"

mutants_x__event_severity__mutmut['_mutmut_orig'] = x__event_severity__mutmut_orig # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_1'] = x__event_severity__mutmut_1 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_2'] = x__event_severity__mutmut_2 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_3'] = x__event_severity__mutmut_3 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_4'] = x__event_severity__mutmut_4 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_5'] = x__event_severity__mutmut_5 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_6'] = x__event_severity__mutmut_6 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_7'] = x__event_severity__mutmut_7 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_8'] = x__event_severity__mutmut_8 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_9'] = x__event_severity__mutmut_9 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_10'] = x__event_severity__mutmut_10 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_11'] = x__event_severity__mutmut_11 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_12'] = x__event_severity__mutmut_12 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_13'] = x__event_severity__mutmut_13 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_14'] = x__event_severity__mutmut_14 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_15'] = x__event_severity__mutmut_15 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_16'] = x__event_severity__mutmut_16 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_17'] = x__event_severity__mutmut_17 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_18'] = x__event_severity__mutmut_18 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_19'] = x__event_severity__mutmut_19 # type: ignore # mutmut generated
mutants_x__event_severity__mutmut['x__event_severity__mutmut_20'] = x__event_severity__mutmut_20 # type: ignore # mutmut generated
mutants_x__dedup__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__dedup__mutmut)
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


def x__dedup__mutmut_orig(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    seen: set[tuple[str, str, str | None]] = set()
    result: list[PipelineTimelineEntry] = []
    for entry in entries:
        key = (entry.source, entry.message, entry.timestamp)
        if key in seen:
            continue
        seen.add(key)
        result.append(entry)
    return result


def x__dedup__mutmut_1(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    seen: set[tuple[str, str, str | None]] = None
    result: list[PipelineTimelineEntry] = []
    for entry in entries:
        key = (entry.source, entry.message, entry.timestamp)
        if key in seen:
            continue
        seen.add(key)
        result.append(entry)
    return result


def x__dedup__mutmut_2(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    seen: set[tuple[str, str, str | None]] = set()
    result: list[PipelineTimelineEntry] = None
    for entry in entries:
        key = (entry.source, entry.message, entry.timestamp)
        if key in seen:
            continue
        seen.add(key)
        result.append(entry)
    return result


def x__dedup__mutmut_3(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    seen: set[tuple[str, str, str | None]] = set()
    result: list[PipelineTimelineEntry] = []
    for entry in entries:
        key = None
        if key in seen:
            continue
        seen.add(key)
        result.append(entry)
    return result


def x__dedup__mutmut_4(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    seen: set[tuple[str, str, str | None]] = set()
    result: list[PipelineTimelineEntry] = []
    for entry in entries:
        key = (entry.source, entry.message, entry.timestamp)
        if key not in seen:
            continue
        seen.add(key)
        result.append(entry)
    return result


def x__dedup__mutmut_5(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    seen: set[tuple[str, str, str | None]] = set()
    result: list[PipelineTimelineEntry] = []
    for entry in entries:
        key = (entry.source, entry.message, entry.timestamp)
        if key in seen:
            break
        seen.add(key)
        result.append(entry)
    return result


def x__dedup__mutmut_6(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    seen: set[tuple[str, str, str | None]] = set()
    result: list[PipelineTimelineEntry] = []
    for entry in entries:
        key = (entry.source, entry.message, entry.timestamp)
        if key in seen:
            continue
        seen.add(None)
        result.append(entry)
    return result


def x__dedup__mutmut_7(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    seen: set[tuple[str, str, str | None]] = set()
    result: list[PipelineTimelineEntry] = []
    for entry in entries:
        key = (entry.source, entry.message, entry.timestamp)
        if key in seen:
            continue
        seen.add(key)
        result.append(None)
    return result

mutants_x__dedup__mutmut['_mutmut_orig'] = x__dedup__mutmut_orig # type: ignore # mutmut generated
mutants_x__dedup__mutmut['x__dedup__mutmut_1'] = x__dedup__mutmut_1 # type: ignore # mutmut generated
mutants_x__dedup__mutmut['x__dedup__mutmut_2'] = x__dedup__mutmut_2 # type: ignore # mutmut generated
mutants_x__dedup__mutmut['x__dedup__mutmut_3'] = x__dedup__mutmut_3 # type: ignore # mutmut generated
mutants_x__dedup__mutmut['x__dedup__mutmut_4'] = x__dedup__mutmut_4 # type: ignore # mutmut generated
mutants_x__dedup__mutmut['x__dedup__mutmut_5'] = x__dedup__mutmut_5 # type: ignore # mutmut generated
mutants_x__dedup__mutmut['x__dedup__mutmut_6'] = x__dedup__mutmut_6 # type: ignore # mutmut generated
mutants_x__dedup__mutmut['x__dedup__mutmut_7'] = x__dedup__mutmut_7 # type: ignore # mutmut generated
mutants_x__sort__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__sort__mutmut)
def _sort(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    return sorted(entries, key=lambda entry: (entry.timestamp is None, entry.timestamp or ""))


def x__sort__mutmut_orig(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    return sorted(entries, key=lambda entry: (entry.timestamp is None, entry.timestamp or ""))


def x__sort__mutmut_1(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    return sorted(None, key=lambda entry: (entry.timestamp is None, entry.timestamp or ""))


def x__sort__mutmut_2(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    return sorted(entries, key=None)


def x__sort__mutmut_3(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    return sorted(key=lambda entry: (entry.timestamp is None, entry.timestamp or ""))


def x__sort__mutmut_4(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    return sorted(entries, )


def x__sort__mutmut_5(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    return sorted(entries, key=lambda entry: None)


def x__sort__mutmut_6(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    return sorted(entries, key=lambda entry: (entry.timestamp is not None, entry.timestamp or ""))


def x__sort__mutmut_7(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    return sorted(entries, key=lambda entry: (entry.timestamp is None, entry.timestamp and ""))


def x__sort__mutmut_8(entries: list[PipelineTimelineEntry]) -> list[PipelineTimelineEntry]:
    return sorted(entries, key=lambda entry: (entry.timestamp is None, entry.timestamp or "XXXX"))

mutants_x__sort__mutmut['_mutmut_orig'] = x__sort__mutmut_orig # type: ignore # mutmut generated
mutants_x__sort__mutmut['x__sort__mutmut_1'] = x__sort__mutmut_1 # type: ignore # mutmut generated
mutants_x__sort__mutmut['x__sort__mutmut_2'] = x__sort__mutmut_2 # type: ignore # mutmut generated
mutants_x__sort__mutmut['x__sort__mutmut_3'] = x__sort__mutmut_3 # type: ignore # mutmut generated
mutants_x__sort__mutmut['x__sort__mutmut_4'] = x__sort__mutmut_4 # type: ignore # mutmut generated
mutants_x__sort__mutmut['x__sort__mutmut_5'] = x__sort__mutmut_5 # type: ignore # mutmut generated
mutants_x__sort__mutmut['x__sort__mutmut_6'] = x__sort__mutmut_6 # type: ignore # mutmut generated
mutants_x__sort__mutmut['x__sort__mutmut_7'] = x__sort__mutmut_7 # type: ignore # mutmut generated
mutants_x__sort__mutmut['x__sort__mutmut_8'] = x__sort__mutmut_8 # type: ignore # mutmut generated
