from __future__ import annotations

from hexawyn.application.use_case.troubleshooting.get_namespace_events.mapper import to_response
from hexawyn.application.use_case.troubleshooting.get_namespace_events.response import (
    GetNamespaceEventsResponse,
)
from hexawyn.domain.models.namespace_event import (
    GetNamespaceEventsResult,
    NamespaceEvent,
)


class TestMapper:
    def test_maps_empty_result(self) -> None:
        result = GetNamespaceEventsResult(
            namespace="default",
            time_window_minutes=15,
            total_events=0,
        )

        response = to_response(result)

        assert isinstance(response, GetNamespaceEventsResponse)
        assert response.namespace == "default"
        assert response.total_events == 0
        assert response.events == []

    def test_maps_result_with_events(self) -> None:
        event = NamespaceEvent(
            event_type="Warning",
            reason="OOMKilled",
            message="Container was OOM killed",
            object="Pod/payments-abc",
            count=5,
            last_seen="2025-01-15T10:00:00Z",
            recurring=True,
            urgency="high",
        )
        result = GetNamespaceEventsResult(
            namespace="production",
            time_window_minutes=30,
            total_events=1,
            events=[event],
            has_more=False,
            remaining_count=0,
            summary="1 event detected, 1 recurring",
        )

        response = to_response(result)

        assert response.namespace == "production"
        assert response.summary == "1 event detected, 1 recurring"
        assert len(response.events) == 1
        assert response.events[0]["event_type"] == "Warning"
        assert response.events[0]["reason"] == "OOMKilled"

    def test_maps_result_with_has_more(self) -> None:
        result = GetNamespaceEventsResult(
            namespace="default",
            time_window_minutes=15,
            total_events=50,
            has_more=True,
            remaining_count=30,
            summary="50 events detected",
        )

        response = to_response(result)

        assert response.has_more is True
        assert response.remaining_count == 30  # noqa: PLR2004
