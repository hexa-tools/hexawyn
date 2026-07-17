"""Unit tests for SummarizeNamespaceEventsService (mocks both driven ports)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_command import (
    SummarizeNamespaceEventsCommand,
)
from hexawyn.application.service.summarize_namespace_events_service import (
    SummarizeNamespaceEventsService,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import NamespaceEvent


def _event(
    event_type: str = "Warning", reason: str = "OOMKilling", obj: str = "pod/a"
) -> NamespaceEvent:
    return NamespaceEvent(
        event_type=event_type,
        reason=reason,
        message=reason,
        object=obj,
        count=1,
        last_seen="2024-01-01T15:00:00Z",
    )


class TestSummarizeNamespaceEventsService:
    def test_summarize_validates_namespace_then_fetches_events(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "staging", "status": "Active", "age": "1d"}
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = [_event()]
        service = SummarizeNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)
        command = SummarizeNamespaceEventsCommand(namespace="staging")

        response = service.summarize(command)

        assert response.namespace == "staging"
        assert response.total_events == 1
        assert response.severity_breakdown["critical"] == 1
        events_port.list_events.assert_called_once()

    def test_summarize_raises_when_namespace_missing(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [{"name": "other", "status": "Active", "age": "1d"}]
        events_port = MagicMock()
        service = SummarizeNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        with pytest.raises(ResourceNotFoundError):
            service.summarize(SummarizeNamespaceEventsCommand(namespace="ghost"))

        events_port.list_events.assert_not_called()

    def test_empty_events_returns_zero_counts(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "staging", "status": "Active", "age": "1d"}
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = []
        service = SummarizeNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        response = service.summarize(SummarizeNamespaceEventsCommand(namespace="staging"))
        assert response.total_events == 0
        assert response.namespace == "staging"

    def test_k8s_port_failure_propagates(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.side_effect = RuntimeError("cluster unreachable")
        events_port = MagicMock()
        service = SummarizeNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        with pytest.raises(RuntimeError, match="cluster unreachable"):
            service.summarize(SummarizeNamespaceEventsCommand(namespace="staging"))


class TestSummarizeNamespaceEventsServiceEdgeCases:
    def test_events_port_failure_propagates(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "staging", "status": "Active", "age": "1d"}
        ]
        events_port = MagicMock()
        events_port.list_events.side_effect = RuntimeError("event collector down")
        service = SummarizeNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        with pytest.raises(RuntimeError, match="event collector down"):
            service.summarize(SummarizeNamespaceEventsCommand(namespace="staging"))

    def test_time_window_zero_boundary(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "staging", "status": "Active", "age": "1d"}
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = [_event()]
        service = SummarizeNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        response = service.summarize(
            SummarizeNamespaceEventsCommand(namespace="staging", time_window_minutes=0)
        )

        assert response.namespace == "staging"
        assert response.total_events == 1

    def test_mixed_severity_events_breakdown(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "staging", "status": "Active", "age": "1d"}
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = [
            _event(reason="OOMKilling"),
            _event(event_type="Normal", reason="Started"),
            _event(reason="Unhealthy"),
        ]
        service = SummarizeNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        response = service.summarize(SummarizeNamespaceEventsCommand(namespace="staging"))

        assert response.total_events == 3
        assert response.namespace == "staging"
