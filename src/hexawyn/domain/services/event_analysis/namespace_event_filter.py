from __future__ import annotations

from dataclasses import replace
from datetime import datetime

from hexawyn.domain.models.constants import NamespaceEventsConstants
from hexawyn.domain.models.namespace_event import (
    GetNamespaceEventsRequest,
    GetNamespaceEventsResult,
    NamespaceEvent,
    Urgency,
)

_cfg = NamespaceEventsConstants()
_NO_EVENTS_SUMMARY = "no events detected"
_RELEVANT_TYPES = frozenset({"Warning", "Error"})
_SEVERITY_ORDER = {"Error": 0, "Warning": 1}
_OBJECT_DELETED_NOTE = "object no longer exists"


def get_namespace_events(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def _sort_key(event: NamespaceEvent) -> tuple[int, float]:
    """Ascending sort: severity rank first (Error before Warning), then most
    recent last_seen first (negated timestamp) as the secondary key."""
    return (
        _SEVERITY_ORDER.get(event.event_type, 2),
        -_parse_timestamp(event.last_seen).timestamp(),
    )


def _finalize(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def _compute_urgency(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "normal"
    age_seconds = (observed_at - _parse_timestamp(event.last_seen)).total_seconds()
    return "high" if age_seconds < _cfg.urgency_recent_window_seconds else "normal"


def _parse_timestamp(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))
