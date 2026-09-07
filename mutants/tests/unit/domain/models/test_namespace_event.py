"""Unit tests for get_namespace_events domain models (pure dataclasses)."""

from __future__ import annotations

from hexawyn.domain.models.namespace_event import (
    GetNamespaceEventsRequest,
    GetNamespaceEventsResult,
    NamespaceEvent,
)


class TestNamespaceEvent:
    def test_fields_and_defaults(self) -> None:
        event = NamespaceEvent(
            event_type="Warning",
            reason="BackOff",
            message="Back-off restarting failed container",
            object="pod/payment-api",
            count=12,
            last_seen="2024-01-01T15:00:00Z",
        )
        assert event.event_type == "Warning"
        assert event.reason == "BackOff"
        assert event.object == "pod/payment-api"
        assert event.count == 12  # noqa: PLR2004
        assert event.recurring is False
        assert event.urgency == "normal"
        assert event.object_exists is True

    def test_explicit_flags(self) -> None:
        event = NamespaceEvent(
            event_type="Warning",
            reason="FailedMount",
            message="volume not found",
            object="pod/ghost",
            count=1,
            last_seen="2024-01-01T15:00:00Z",
            recurring=False,
            urgency="high",
            object_exists=False,
        )
        assert event.urgency == "high"
        assert event.object_exists is False


class TestGetNamespaceEventsRequest:
    def test_defaults(self) -> None:
        request = GetNamespaceEventsRequest(namespace="production")
        assert request.time_window_minutes == 15  # noqa: PLR2004
        assert request.top_n == 20  # noqa: PLR2004

    def test_custom_values(self) -> None:
        request = GetNamespaceEventsRequest(
            namespace="production", time_window_minutes=30, top_n=10
        )
        assert request.time_window_minutes == 30  # noqa: PLR2004
        assert request.top_n == 10  # noqa: PLR2004


class TestGetNamespaceEventsResult:
    def test_defaults(self) -> None:
        result = GetNamespaceEventsResult(
            namespace="production", time_window_minutes=15, total_events=0
        )
        assert result.events == []
        assert result.has_more is False
        assert result.remaining_count == 0
        assert result.summary == ""

    def test_with_events(self) -> None:
        event = NamespaceEvent(
            event_type="Error",
            reason="OOMKilling",
            message="Memory cgroup out of memory",
            object="pod/worker-1",
            count=1,
            last_seen="2024-01-01T15:00:00Z",
        )
        result = GetNamespaceEventsResult(
            namespace="production",
            time_window_minutes=15,
            total_events=1,
            events=[event],
            summary="1 event detected",
        )
        assert len(result.events) == 1
        assert result.summary == "1 event detected"
