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
