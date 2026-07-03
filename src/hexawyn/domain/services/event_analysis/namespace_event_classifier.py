from __future__ import annotations

from datetime import datetime

from hexawyn.domain.models.event import ClassifiedEvent, EventCategory, EventSeverity
from hexawyn.domain.models.namespace_event import NamespaceEvent

_REASON_CLASSIFICATION: dict[str, tuple[EventSeverity, EventCategory]] = {
    "OOMKilling": (EventSeverity.CRITICAL, EventCategory.RESOURCE),
    "OOMKilled": (EventSeverity.CRITICAL, EventCategory.RESOURCE),
    "BackOff": (EventSeverity.HIGH, EventCategory.LIFECYCLE),
    "CrashLoopBackOff": (EventSeverity.HIGH, EventCategory.LIFECYCLE),
    "FailedScheduling": (EventSeverity.HIGH, EventCategory.SCHEDULING),
    "FailedMount": (EventSeverity.MEDIUM, EventCategory.STORAGE),
}
_DEFAULT_WARNING_CLASSIFICATION = (EventSeverity.MEDIUM, EventCategory.OTHER)
_NORMAL_CLASSIFICATION = (EventSeverity.LOW, EventCategory.LIFECYCLE)


def classify_namespace_event(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def _classify(event: NamespaceEvent) -> tuple[EventSeverity, EventCategory]:
    if event.event_type == "Normal":
        return _NORMAL_CLASSIFICATION
    return _REASON_CLASSIFICATION.get(event.reason, _DEFAULT_WARNING_CLASSIFICATION)


def _parse_timestamp(raw: str) -> datetime | None:
    if not raw:
        return None
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))
