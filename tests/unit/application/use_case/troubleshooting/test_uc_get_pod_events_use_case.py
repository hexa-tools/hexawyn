from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.get_pod_events.command import (
    GetPodEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.get_pod_events.get_pod_events_use_case import (  # noqa: E501
    GetPodEventsUseCase,
)
from hexawyn.application.use_case.troubleshooting.get_pod_events.response import (
    GetPodEventsResponse,
)


class TestGetPodEventsUseCase:
    def test_execute_returns_response(self) -> None:
        events_port = MagicMock()
        events_port.list_events.return_value = []
        k8s = MagicMock()

        use_case = GetPodEventsUseCase(
            events_port=events_port,
            k8s_port=k8s,
        )
        result = use_case.execute(GetPodEventsCommand(namespace="default", pod_name="nginx"))

        assert isinstance(result, GetPodEventsResponse)
        assert result.pod_name == "nginx"

    def test_execute_filters_events_by_pod_name(self) -> None:
        from hexawyn.domain.models.namespace_event import NamespaceEvent

        event_a = NamespaceEvent(
            event_type="Warning",
            reason="OOM",
            message="OOM",
            object="Pod/nginx",
            count=1,
            last_seen="2025-01-15T10:00:00Z",
        )
        event_b = NamespaceEvent(
            event_type="Warning",
            reason="Crash",
            message="crash",
            object="Pod/other",
            count=1,
            last_seen="2025-01-15T10:00:00Z",
        )
        events_port = MagicMock()
        events_port.list_events.return_value = [event_a, event_b]
        k8s = MagicMock()

        use_case = GetPodEventsUseCase(
            events_port=events_port,
            k8s_port=k8s,
        )
        result = use_case.execute(GetPodEventsCommand(namespace="default", pod_name="nginx"))

        assert result.total_events == 1

    def test_execute_pod_not_found_returns_zero_events(self) -> None:
        events_port = MagicMock()
        events_port.list_events.return_value = []
        k8s = MagicMock()

        use_case = GetPodEventsUseCase(
            events_port=events_port,
            k8s_port=k8s,
        )
        result = use_case.execute(GetPodEventsCommand(namespace="default", pod_name="nonexistent"))

        assert result.total_events == 0
        assert result.events == []
