from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.troubleshooting.advanced_namespace_event_analytics.advanced_namespace_event_analytics_use_case import (  # noqa: E501
    AdvancedNamespaceEventAnalyticsUseCase,
)
from hexawyn.application.use_case.troubleshooting.advanced_namespace_event_analytics.command import (  # noqa: E501
    AdvancedNamespaceEventAnalyticsCommand,
)
from hexawyn.application.use_case.troubleshooting.advanced_namespace_event_analytics.response import (  # noqa: E501
    AdvancedNamespaceEventAnalyticsResponse,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import (
    NamespaceEvent,
)


def _make_event(  # noqa: PLR0913
    event_type: str = "Warning",
    reason: str = "Unhealthy",
    message: str = "Liveness probe failed",
    object_ref: str = "Pod/payment-svc-abc",
    count: int = 1,
    last_seen: str = "2026-07-28T10:00:00Z",
    recurring: bool = False,
) -> NamespaceEvent:
    return NamespaceEvent(
        event_type=event_type,
        reason=reason,
        message=message,
        object=object_ref,
        count=count,
        last_seen=last_seen,
        recurring=recurring,
        urgency="normal",
        object_exists=True,
    )


class TestAdvancedNamespaceEventAnalyticsUseCase:
    def test_execute_returns_response(self) -> None:
        events_port = MagicMock()
        events_port.list_events.return_value = []
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "2d"},
        ]

        use_case = AdvancedNamespaceEventAnalyticsUseCase(
            events_port=events_port, k8s_port=k8s_port
        )
        result = use_case.execute(AdvancedNamespaceEventAnalyticsCommand(namespace="default"))

        assert isinstance(result, AdvancedNamespaceEventAnalyticsResponse)
        assert result.namespace == "default"

    def test_execute_with_events(self) -> None:
        events_port = MagicMock()
        events_port.list_events.return_value = [
            _make_event(reason="CrashLoopBackOff", message="Back-off restarting"),
            _make_event(reason="FailedScheduling", message="0/3 nodes available"),
            _make_event(reason="Unhealthy", message="Liveness probe failed"),
        ]
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "2d"},
        ]

        use_case = AdvancedNamespaceEventAnalyticsUseCase(
            events_port=events_port, k8s_port=k8s_port
        )
        result = use_case.execute(AdvancedNamespaceEventAnalyticsCommand(namespace="default"))

        assert isinstance(result, AdvancedNamespaceEventAnalyticsResponse)
        assert result.namespace == "default"

    def test_execute_namespace_not_found(self) -> None:
        events_port = MagicMock()
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "2d"},
        ]

        use_case = AdvancedNamespaceEventAnalyticsUseCase(
            events_port=events_port, k8s_port=k8s_port
        )

        with pytest.raises(ResourceNotFoundError):
            use_case.execute(AdvancedNamespaceEventAnalyticsCommand(namespace="missing-ns"))

    def test_execute_empty_namespace_list(self) -> None:
        events_port = MagicMock()
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = []

        use_case = AdvancedNamespaceEventAnalyticsUseCase(
            events_port=events_port, k8s_port=k8s_port
        )

        with pytest.raises(ResourceNotFoundError):
            use_case.execute(AdvancedNamespaceEventAnalyticsCommand(namespace="default"))

    def test_execute_with_large_event_volume(self) -> None:
        events_port = MagicMock()
        events_port.list_events.return_value = [
            _make_event(
                reason="FailedScheduling",
                message=f"event-{i}",
                last_seen=f"2026-07-28T10:{i % 60:02d}:00Z",
            )
            for i in range(100)
        ]
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "2d"},
        ]

        use_case = AdvancedNamespaceEventAnalyticsUseCase(
            events_port=events_port, k8s_port=k8s_port
        )
        result = use_case.execute(AdvancedNamespaceEventAnalyticsCommand(namespace="default"))

        assert isinstance(result, AdvancedNamespaceEventAnalyticsResponse)

    def test_execute_with_normal_events_only(self) -> None:
        events_port = MagicMock()
        events_port.list_events.return_value = [
            _make_event(event_type="Normal", reason="Pulled", message="Container image pulled"),
            _make_event(event_type="Normal", reason="Started", message="Container started"),
        ]
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "2d"},
        ]

        use_case = AdvancedNamespaceEventAnalyticsUseCase(
            events_port=events_port, k8s_port=k8s_port
        )
        result = use_case.execute(AdvancedNamespaceEventAnalyticsCommand(namespace="default"))

        assert isinstance(result, AdvancedNamespaceEventAnalyticsResponse)

    def test_execute_with_mixed_event_types(self) -> None:
        events_port = MagicMock()
        events_port.list_events.return_value = [
            _make_event(event_type="Normal", reason="Pulled", message="Pulled"),
            _make_event(event_type="Warning", reason="Unhealthy", message="Probe failed"),
            _make_event(event_type="Warning", reason="BackOff", message="Back-off restarting"),
        ]
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "2d"},
        ]

        use_case = AdvancedNamespaceEventAnalyticsUseCase(
            events_port=events_port, k8s_port=k8s_port
        )
        result = use_case.execute(AdvancedNamespaceEventAnalyticsCommand(namespace="default"))

        assert isinstance(result, AdvancedNamespaceEventAnalyticsResponse)

    def test_execute_with_recurring_events(self) -> None:
        events_port = MagicMock()
        events_port.list_events.return_value = [
            _make_event(
                reason="CrashLoopBackOff",
                message="Back-off restarting",
                count=50,
                recurring=True,
            ),
        ]
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "2d"},
        ]

        use_case = AdvancedNamespaceEventAnalyticsUseCase(
            events_port=events_port, k8s_port=k8s_port
        )
        result = use_case.execute(AdvancedNamespaceEventAnalyticsCommand(namespace="default"))

        assert isinstance(result, AdvancedNamespaceEventAnalyticsResponse)
