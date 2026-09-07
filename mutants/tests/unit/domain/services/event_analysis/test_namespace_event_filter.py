"""Unit tests for the namespace_event_filter domain service.

Covers TC1-TC3 (TC4/RBAC is an adapter/service-level error, not tested here)
and the domain-level edge cases (urgency flag, deleted-object note).
"""

from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest, NamespaceEvent
from hexawyn.domain.services.event_analysis.namespace_event_filter import get_namespace_events

_OBSERVED_AT = datetime(2024, 1, 1, 15, 0, 0, tzinfo=UTC)


def _event(  # noqa: PLR0913
    event_type: str,
    reason: str,
    obj: str,
    count: int,
    last_seen: str,
    message: str = "",
    object_exists: bool = True,
) -> NamespaceEvent:
    return NamespaceEvent(
        event_type=event_type,
        reason=reason,
        message=message or reason,
        object=obj,
        count=count,
        last_seen=last_seen,
        object_exists=object_exists,
    )


class TestRecurringGrouping:
    """TC1: 3 Warning events for same pod → grouped and flagged as recurring."""

    def test_events_over_threshold_flagged_recurring_and_adjacent(self) -> None:
        events = [
            _event("Warning", "BackOff", "pod/payment-api", 12, "2024-01-01T14:59:50Z"),
            _event("Warning", "Unhealthy", "pod/payment-api", 8, "2024-01-01T14:59:40Z"),
            _event("Warning", "FailedMount", "pod/payment-api", 3, "2024-01-01T14:59:30Z"),
        ]
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, events, observed_at=_OBSERVED_AT)

        recurring_flags = [e.recurring for e in result.events]
        assert recurring_flags == [True, True, False]
        objects = {e.object for e in result.events}
        assert objects == {"pod/payment-api"}


class TestNoEvents:
    """TC2: No events in last 15 minutes → returns clean "no events detected" message."""

    def test_empty_events_returns_clean_message(self) -> None:
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, [], observed_at=_OBSERVED_AT)

        assert result.events == []
        assert result.total_events == 0
        assert result.summary == "no events detected"


class TestProgressiveDisclosure:
    """TC3: 500+ events in namespace → progressive disclosure: top 20 shown, rest paginated."""

    def test_more_than_top_n_events_paginated(self) -> None:
        events = [
            _event("Warning", "BackOff", f"pod/worker-{i}", 1, "2024-01-01T14:59:00Z")
            for i in range(500)
        ]
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, events, observed_at=_OBSERVED_AT)

        assert result.total_events == 500  # noqa: PLR2004
        assert len(result.events) == 20  # noqa: PLR2004
        assert result.has_more is True
        assert result.remaining_count == 480  # noqa: PLR2004


class TestSeverityThenTimestampSort:
    def test_error_events_sorted_before_warning_regardless_of_timestamp(self) -> None:
        events = [
            _event("Warning", "BackOff", "pod/a", 1, "2024-01-01T14:59:55Z"),
            _event("Error", "OOMKilling", "pod/b", 1, "2024-01-01T14:00:00Z"),
        ]
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, events, observed_at=_OBSERVED_AT)

        assert result.events[0].event_type == "Error"
        assert result.events[1].event_type == "Warning"

    def test_same_severity_sorted_by_most_recent_first(self) -> None:
        events = [
            _event("Warning", "BackOff", "pod/a", 1, "2024-01-01T14:00:00Z"),
            _event("Warning", "Unhealthy", "pod/b", 1, "2024-01-01T14:59:00Z"),
        ]
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, events, observed_at=_OBSERVED_AT)

        assert result.events[0].reason == "Unhealthy"
        assert result.events[1].reason == "BackOff"

    def test_normal_type_events_are_filtered_out(self) -> None:
        events = [
            _event("Normal", "Scheduled", "pod/a", 1, "2024-01-01T14:59:00Z"),
            _event("Warning", "BackOff", "pod/b", 1, "2024-01-01T14:59:00Z"),
        ]
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, events, observed_at=_OBSERVED_AT)

        assert result.total_events == 1
        assert result.events[0].reason == "BackOff"


class TestEdgeCases:
    def test_single_recent_event_flagged_high_urgency(self) -> None:
        """count=1 but very recent (30s ago) → shown with HIGH urgency flag."""
        events = [_event("Warning", "FailedMount", "pod/a", 1, "2024-01-01T14:59:30Z")]
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, events, observed_at=_OBSERVED_AT)

        assert result.events[0].urgency == "high"

    def test_old_single_event_is_normal_urgency(self) -> None:
        events = [_event("Warning", "FailedMount", "pod/a", 1, "2024-01-01T14:00:00Z")]
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, events, observed_at=_OBSERVED_AT)

        assert result.events[0].urgency == "normal"

    def test_deleted_object_shown_with_note(self) -> None:
        """Events from deleted pods still present → shown with "object no longer exists" note."""
        events = [
            _event(
                "Warning",
                "FailedMount",
                "pod/ghost",
                1,
                "2024-01-01T14:00:00Z",
                message="volume not found",
                object_exists=False,
            )
        ]
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, events, observed_at=_OBSERVED_AT)

        assert result.events[0].object_exists is False
        assert "object no longer exists" in result.events[0].message


class TestBoundaryThresholds:
    def test_count_exactly_threshold_not_recurring(self) -> None:
        event = _event("Warning", "BackOff", "pod/a", 5, "2024-01-01T14:59:00Z")
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, [event], observed_at=_OBSERVED_AT)

        assert result.events[0].recurring is False

    def test_urgency_window_exact_boundary_is_normal(self) -> None:
        event = _event("Warning", "BackOff", "pod/a", 1, "2024-01-01T14:59:00Z")
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, [event], observed_at=_OBSERVED_AT)

        assert result.events[0].urgency == "normal"
        assert result.summary == "1 event detected"

    def test_recurring_event_summary_exact(self) -> None:
        events = [
            _event("Warning", "BackOff", "pod/a", 6, "2024-01-01T14:59:00Z"),
            _event("Error", "OOM", "pod/b", 1, "2024-01-01T14:59:00Z"),
        ]
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, events, observed_at=_OBSERVED_AT)

        assert result.total_events == 2  # noqa: PLR2004
        assert result.summary == "2 events detected, 1 recurring"


class TestPaginationBoundaries:
    def test_exactly_top_n_events_no_more(self) -> None:
        events = [
            _event("Warning", "BackOff", f"pod/worker-{i}", 1, "2024-01-01T14:59:00Z")
            for i in range(20)
        ]
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, events, observed_at=_OBSERVED_AT)

        assert result.total_events == 20  # noqa: PLR2004
        assert result.has_more is False
        assert result.remaining_count == 0

    def test_exactly_top_n_plus_one_has_more(self) -> None:
        events = [
            _event("Warning", "BackOff", f"pod/worker-{i}", 1, "2024-01-01T14:59:00Z")
            for i in range(21)
        ]
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, events, observed_at=_OBSERVED_AT)

        assert result.has_more is True
        assert result.remaining_count == 1

    def test_custom_top_n_respected(self) -> None:
        events = [
            _event("Warning", "BackOff", f"pod/worker-{i}", 1, "2024-01-01T14:59:00Z")
            for i in range(5)
        ]
        request = GetNamespaceEventsRequest(namespace="production", top_n=3)

        result = get_namespace_events(request, events, observed_at=_OBSERVED_AT)

        assert len(result.events) == 3  # noqa: PLR2004
        assert result.remaining_count == 2  # noqa: PLR2004


class TestFieldPropagationDiscriminators:
    def test_result_fields_propagated_exact(self) -> None:
        event = _event("Warning", "BackOff", "pod/a", 1, "2024-01-01T14:59:00Z")
        request = GetNamespaceEventsRequest(
            namespace="production", time_window_minutes=30, top_n=20
        )

        result = get_namespace_events(request, [event], observed_at=_OBSERVED_AT)

        assert result.namespace == "production"
        assert result.time_window_minutes == 30  # noqa: PLR2004
        assert result.total_events == 1

    def test_empty_result_fields_propagated(self) -> None:
        request = GetNamespaceEventsRequest(namespace="staging", time_window_minutes=45, top_n=20)

        result = get_namespace_events(request, [], observed_at=_OBSERVED_AT)

        assert result.namespace == "staging"
        assert result.time_window_minutes == 45  # noqa: PLR2004
        assert result.total_events == 0
        assert result.summary == "no events detected"

    def test_existing_object_message_not_appended(self) -> None:
        event = _event(
            "Warning",
            "BackOff",
            "pod/a",
            1,
            "2024-01-01T14:59:00Z",
            message="volume not found",
            object_exists=True,
        )
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, [event], observed_at=_OBSERVED_AT)

        assert result.events[0].message == "volume not found"

    def test_deleted_object_with_note_not_duplicated(self) -> None:
        event = _event(
            "Warning",
            "BackOff",
            "pod/a",
            1,
            "2024-01-01T14:59:00Z",
            message="volume not found (object no longer exists)",
            object_exists=False,
        )
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, [event], observed_at=_OBSERVED_AT)

        assert result.events[0].message == "volume not found (object no longer exists)"

    def test_multi_count_event_normal_urgency(self) -> None:
        event = _event("Warning", "BackOff", "pod/a", 3, "2024-01-01T14:59:30Z")
        request = GetNamespaceEventsRequest(namespace="production")

        result = get_namespace_events(request, [event], observed_at=_OBSERVED_AT)

        assert result.events[0].urgency == "normal"
