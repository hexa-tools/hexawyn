"""Unit tests for Kubernetes event domain models."""

import dataclasses
from datetime import UTC, datetime

from hexawyn.domain.models.event import (
    ClassifiedEvent,
    EventCategory,
    EventSeverity,
)


class TestEventSeverity:
    def test_all_members_present(self) -> None:
        assert len(EventSeverity) == 4
        assert EventSeverity.CRITICAL.value == "critical"
        assert EventSeverity.HIGH.value == "high"
        assert EventSeverity.MEDIUM.value == "medium"
        assert EventSeverity.LOW.value == "low"

    def test_is_enum(self) -> None:
        assert isinstance(EventSeverity.CRITICAL, EventSeverity)

    def test_ordering_highest_is_critical(self) -> None:
        severities = list(EventSeverity)
        critical_index = severities.index(EventSeverity.CRITICAL)
        assert critical_index == 0


class TestEventCategory:
    def test_all_members_present(self) -> None:
        assert len(EventCategory) == 12

    def test_values_are_lowercase(self) -> None:
        for category in EventCategory:
            assert category.value == category.value.lower()

    def test_fallback_is_other(self) -> None:
        assert EventCategory.OTHER.value == "other"

    def test_is_enum(self) -> None:
        assert isinstance(EventCategory.FAILURE, EventCategory)


class TestClassifiedEvent:
    def test_minimal_construction(self) -> None:
        event = ClassifiedEvent(
            event_type="Warning",
            reason="OOMKilled",
            message="Memory cgroup out of memory",
            severity=EventSeverity.CRITICAL,
            category=EventCategory.RESOURCE,
            namespace="production",
            involved_object="Pod/payments-api-7d8f9",
        )
        assert event.event_type == "Warning"
        assert event.reason == "OOMKilled"
        assert event.severity == EventSeverity.CRITICAL
        assert event.category == EventCategory.RESOURCE
        assert event.count == 1
        assert event.first_timestamp is None
        assert event.last_timestamp is None

    def test_full_construction(self) -> None:
        now = datetime.now(UTC)
        event = ClassifiedEvent(
            event_type="Normal",
            reason="Started",
            message="Container started",
            severity=EventSeverity.LOW,
            category=EventCategory.LIFECYCLE,
            namespace="staging",
            involved_object="Pod/nginx-deploy-abc123",
            count=15,
            first_timestamp=now,
            last_timestamp=now,
        )
        assert event.count == 15
        assert event.first_timestamp == now
        assert event.last_timestamp == now

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(ClassifiedEvent)

    def test_equality(self) -> None:
        a = ClassifiedEvent(
            event_type="Warning",
            reason="Unhealthy",
            message="Liveness probe failed",
            severity=EventSeverity.HIGH,
            category=EventCategory.HEALTH,
            namespace="prod",
            involved_object="Pod/api-1",
        )
        b = ClassifiedEvent(
            event_type="Warning",
            reason="Unhealthy",
            message="Liveness probe failed",
            severity=EventSeverity.HIGH,
            category=EventCategory.HEALTH,
            namespace="prod",
            involved_object="Pod/api-1",
        )
        assert a == b

    def test_count_default_is_one(self) -> None:
        event = ClassifiedEvent(
            event_type="Normal",
            reason="Pulled",
            message="Container image pulled",
            severity=EventSeverity.LOW,
            category=EventCategory.IMAGE,
            namespace="default",
            involved_object="Pod/app",
        )
        assert event.count == 1
