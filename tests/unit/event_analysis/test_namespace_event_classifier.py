"""Unit tests for classify_namespace_event (raw NamespaceEvent -> ClassifiedEvent)."""

from __future__ import annotations

from hexawyn.domain.models.event import EventCategory, EventSeverity
from hexawyn.domain.models.namespace_event import NamespaceEvent
from hexawyn.domain.services.event_analysis.namespace_event_classifier import (
    classify_namespace_event,
)


def _event(event_type: str, reason: str, obj: str = "pod/api-1", count: int = 1) -> NamespaceEvent:
    return NamespaceEvent(
        event_type=event_type,
        reason=reason,
        message=reason,
        object=obj,
        count=count,
        last_seen="2024-01-01T15:00:00Z",
    )


class TestClassifyNamespaceEvent:
    def test_oomkilling_is_critical_resource(self) -> None:
        classified = classify_namespace_event(_event("Warning", "OOMKilling"))
        assert classified.severity == EventSeverity.CRITICAL
        assert classified.category == EventCategory.RESOURCE

    def test_oomkilled_alias_is_critical(self) -> None:
        classified = classify_namespace_event(_event("Warning", "OOMKilled"))
        assert classified.severity == EventSeverity.CRITICAL

    def test_backoff_is_high(self) -> None:
        classified = classify_namespace_event(_event("Warning", "BackOff"))
        assert classified.severity == EventSeverity.HIGH

    def test_crashloopbackoff_is_high(self) -> None:
        classified = classify_namespace_event(_event("Warning", "CrashLoopBackOff"))
        assert classified.severity == EventSeverity.HIGH

    def test_failed_scheduling_is_high_scheduling_category(self) -> None:
        classified = classify_namespace_event(_event("Warning", "FailedScheduling"))
        assert classified.severity == EventSeverity.HIGH
        assert classified.category == EventCategory.SCHEDULING

    def test_failed_mount_is_medium_storage_category(self) -> None:
        classified = classify_namespace_event(_event("Warning", "FailedMount"))
        assert classified.severity == EventSeverity.MEDIUM
        assert classified.category == EventCategory.STORAGE

    def test_unknown_warning_falls_back_to_medium(self) -> None:
        classified = classify_namespace_event(_event("Warning", "SomeExoticCRDReason"))
        assert classified.severity == EventSeverity.MEDIUM

    def test_normal_type_is_low_severity(self) -> None:
        classified = classify_namespace_event(_event("Normal", "Scheduled"))
        assert classified.severity == EventSeverity.LOW

    def test_empty_last_seen_yields_no_timestamp(self) -> None:
        event = _event("Warning", "OOMKilling")
        event = NamespaceEvent(
            event_type=event.event_type,
            reason=event.reason,
            message=event.message,
            object=event.object,
            count=event.count,
            last_seen="",
        )

        classified = classify_namespace_event(event)

        assert classified.first_timestamp is None
        assert classified.last_timestamp is None

    def test_fields_pass_through(self) -> None:
        classified = classify_namespace_event(
            _event("Warning", "OOMKilling", obj="pod/payment-api", count=3)
        )
        assert classified.reason == "OOMKilling"
        assert classified.involved_object == "pod/payment-api"
        assert classified.count == 3
        assert classified.last_timestamp is not None
        assert classified.first_timestamp == classified.last_timestamp
