"""Unit tests for GetNamespaceEventsService (mocks both driven ports)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_command import (
    GetNamespaceEventsCommand,
)
from hexawyn.application.service.get_namespace_events_service import GetNamespaceEventsService
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import NamespaceEvent


def _event(reason: str = "BackOff", count: int = 1) -> NamespaceEvent:
    return NamespaceEvent(
        event_type="Warning",
        reason=reason,
        message=reason,
        object="pod/payment-api",
        count=count,
        last_seen="2024-01-01T15:00:00Z",
    )


class TestGetNamespaceEventsService:
    def test_get_events_validates_namespace_then_fetches_events(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "production", "status": "Active", "age": "10d"}
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = [_event(count=12)]
        service = GetNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)
        command = GetNamespaceEventsCommand(namespace="production")

        response = service.get_events(command)

        assert response.namespace == "production"
        assert response.total_events == 1
        assert response.events[0]["recurring"] is True
        events_port.list_events.assert_called_once()

    def test_get_events_raises_when_namespace_missing(self) -> None:
        """ECA-5: namespace existence is validated via list_namespaces before fetching events."""
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "staging", "status": "Active", "age": "1d"}
        ]
        events_port = MagicMock()
        service = GetNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)
        command = GetNamespaceEventsCommand(namespace="ghost")

        with pytest.raises(ResourceNotFoundError):
            service.get_events(command)

        events_port.list_events.assert_not_called()

    def test_get_events_returns_no_events_message(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "production", "status": "Active", "age": "10d"}
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = []
        service = GetNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        response = service.get_events(GetNamespaceEventsCommand(namespace="production"))

        assert response.summary == "no events detected"
        assert response.events == []
