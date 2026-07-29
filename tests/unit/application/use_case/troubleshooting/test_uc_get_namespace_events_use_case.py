from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.troubleshooting.get_namespace_events.command import (
    GetNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.get_namespace_events.get_namespace_events_use_case import (  # noqa: E501
    GetNamespaceEventsUseCase,
)
from hexawyn.application.use_case.troubleshooting.get_namespace_events.response import (
    GetNamespaceEventsResponse,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import NamespaceEvent


def _k8s_port_with(namespace: str) -> MagicMock:
    port = MagicMock()
    port.list_namespaces.return_value = [
        {"name": namespace, "status": "Active", "age": "30d"},
    ]
    return port


class TestGetNamespaceEventsUseCase:
    def test_execute_returns_get_namespace_events_response(self) -> None:
        events_port = MagicMock()
        events_port.list_events.return_value = []

        use_case = GetNamespaceEventsUseCase(
            events_port=events_port,
            k8s_port=_k8s_port_with("default"),
        )
        result = use_case.execute(GetNamespaceEventsCommand(namespace="default"))

        assert isinstance(result, GetNamespaceEventsResponse)
        assert result.namespace == "default"

    def test_execute_raises_resource_not_found_for_unknown_namespace(self) -> None:
        events_port = MagicMock()
        use_case = GetNamespaceEventsUseCase(
            events_port=events_port,
            k8s_port=_k8s_port_with("default"),
        )

        with pytest.raises(ResourceNotFoundError, match="Namespace 'production' not found"):
            use_case.execute(GetNamespaceEventsCommand(namespace="production"))

    def test_execute_passes_time_window_and_top_n(self) -> None:
        events_port = MagicMock()
        events_port.list_events.return_value = []

        use_case = GetNamespaceEventsUseCase(
            events_port=events_port,
            k8s_port=_k8s_port_with("ns"),
        )
        use_case.execute(
            GetNamespaceEventsCommand(
                namespace="ns",
                time_window_minutes=30,
                top_n=10,
            )
        )

        call_args = events_port.list_events.call_args[0][0]
        assert call_args.time_window_minutes == 30  # noqa: PLR2004
        assert call_args.top_n == 10  # noqa: PLR2004

    def test_execute_with_warning_events_returns_summary(self) -> None:
        event = NamespaceEvent(
            event_type="Warning",
            reason="Unhealthy",
            message="Pod is crashing",
            object="Pod/nginx",
            count=3,
            last_seen="2025-01-15T10:00:00Z",
        )
        events_port = MagicMock()
        events_port.list_events.return_value = [event]

        use_case = GetNamespaceEventsUseCase(
            events_port=events_port,
            k8s_port=_k8s_port_with("default"),
        )
        result = use_case.execute(GetNamespaceEventsCommand(namespace="default"))

        assert result.total_events > 0
        assert len(result.events) > 0
        assert result.events[0]["event_type"] == "Warning"
        assert result.events[0]["reason"] == "Unhealthy"

    def test_execute_with_no_relevant_events_returns_empty(self) -> None:
        normal_event = NamespaceEvent(
            event_type="Normal",
            reason="Started",
            message="Started container",
            object="Pod/nginx",
            count=1,
            last_seen="2025-01-15T10:00:00Z",
        )
        events_port = MagicMock()
        events_port.list_events.return_value = [normal_event]

        use_case = GetNamespaceEventsUseCase(
            events_port=events_port,
            k8s_port=_k8s_port_with("default"),
        )
        result = use_case.execute(GetNamespaceEventsCommand(namespace="default"))

        assert result.total_events == 0
        assert len(result.events) == 0

    def test_execute_with_high_event_count(self) -> None:
        events = [
            NamespaceEvent(
                event_type="Warning",
                reason="Test",
                message=f"msg {i}",
                object="Pod/test",
                count=i,
                last_seen="2025-01-15T10:00:00Z",
            )
            for i in range(100)
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = events

        use_case = GetNamespaceEventsUseCase(
            events_port=events_port,
            k8s_port=_k8s_port_with("default"),
        )
        result = use_case.execute(GetNamespaceEventsCommand(namespace="default", top_n=5))

        assert len(result.events) == 5  # noqa: PLR2004
        assert result.has_more is True
