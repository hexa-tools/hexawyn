from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class K8sEventType(Enum):
    OOM_KILLED = "OOMKilled"
    CONTAINER_RESTART = "ContainerRestart"
    EVICTION = "Eviction"
    OTHER = "Other"


@dataclass(frozen=True)
class K8sEvent:
    event_type: K8sEventType
    pod_name: str
    timestamp: str
    namespace: str
    reason: str


@dataclass(frozen=True)
class TraceEventCorrelationRequest:
    trace_id: str


@dataclass(frozen=True)
class TraceEventResult:
    trace_id: str
    matching_events: list[K8sEvent]
    slowest_span: str | None
    conclusion: str

    @staticmethod
    def compute(
        request: TraceEventCorrelationRequest,
        events: list[K8sEvent],
        slowest_span: str | None,
    ) -> TraceEventResult:
        if not events:
            return TraceEventResult(
                trace_id=request.trace_id,
                matching_events=[],
                slowest_span=slowest_span,
                conclusion="No system events (OOM, restart, eviction) found during this trace window",
            )

        parts = [f"Found {len(events)} system event(s) during trace {request.trace_id}"]
        oom_count = sum(1 for e in events if e.event_type == K8sEventType.OOM_KILLED)
        restart_count = sum(1 for e in events if e.event_type == K8sEventType.CONTAINER_RESTART)
        eviction_count = sum(1 for e in events if e.event_type == K8sEventType.EVICTION)

        if oom_count:
            parts.append(f"{oom_count} OOMKilled event(s)")
        if restart_count:
            parts.append(f"{restart_count} container restart(s)")
        if eviction_count:
            parts.append(f"{eviction_count} eviction(s)")

        if slowest_span and oom_count:
            parts.append(f"OOMKilled event overlaps with slowest span: {slowest_span}")

        return TraceEventResult(
            trace_id=request.trace_id,
            matching_events=events,
            slowest_span=slowest_span,
            conclusion=". ".join(parts),
        )
