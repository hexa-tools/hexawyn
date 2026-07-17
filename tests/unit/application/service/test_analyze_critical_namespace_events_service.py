"""Unit tests for AnalyzeCriticalNamespaceEventsService (mocks both driven ports)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_command import (
    AnalyzeCriticalNamespaceEventsCommand,
)
from hexawyn.application.service.analyze_critical_namespace_events_service import (
    AnalyzeCriticalNamespaceEventsService,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import NamespaceEvent


def _event(
    event_type: str = "Warning", reason: str = "OOMKilling", obj: str = "pod/payment-api"
) -> NamespaceEvent:
    return NamespaceEvent(
        event_type=event_type,
        reason=reason,
        message=reason,
        object=obj,
        count=1,
        last_seen="2024-01-01T15:00:00Z",
    )


class TestAnalyzeCriticalNamespaceEventsService:
    def test_analyze_validates_namespace_then_returns_critical_incidents(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "staging", "status": "Active", "age": "1d"}
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = [_event(), _event(), _event()]
        service = AnalyzeCriticalNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        response = service.analyze(AnalyzeCriticalNamespaceEventsCommand(namespace="staging"))

        assert response.namespace == "staging"
        assert len(response.critical_incidents) == 1
        incident = response.critical_incidents[0]
        assert incident["reason"] == "OOMKilling"
        assert incident["event_count"] == 3
        assert incident["runbook_id"] == "runbook-memory-001"

    def test_analyze_raises_when_namespace_missing(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [{"name": "other", "status": "Active", "age": "1d"}]
        events_port = MagicMock()
        service = AnalyzeCriticalNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        with pytest.raises(ResourceNotFoundError):
            service.analyze(AnalyzeCriticalNamespaceEventsCommand(namespace="ghost"))

        events_port.list_events.assert_not_called()

    def test_analyze_returns_empty_incidents_when_no_critical_events(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "staging", "status": "Active", "age": "1d"}
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = [_event(event_type="Normal", reason="Scheduled")]
        service = AnalyzeCriticalNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        response = service.analyze(AnalyzeCriticalNamespaceEventsCommand(namespace="staging"))

        assert response.critical_incidents == []

    def test_empty_namespace_events_no_crashes(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "staging", "status": "Active", "age": "1d"}
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = []
        service = AnalyzeCriticalNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)
        response = service.analyze(AnalyzeCriticalNamespaceEventsCommand(namespace="staging"))
        assert response.critical_incidents == []


class TestAnalyzeCriticalNamespaceEventsServiceEdgeCases:
    def test_k8s_port_failure_propagates(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.side_effect = RuntimeError("API server timeout")
        events_port = MagicMock()
        service = AnalyzeCriticalNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        with pytest.raises(RuntimeError, match="API server timeout"):
            service.analyze(AnalyzeCriticalNamespaceEventsCommand(namespace="production"))

    def test_events_port_failure_propagates(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "production", "status": "Active", "age": "1d"}
        ]
        events_port = MagicMock()
        events_port.list_events.side_effect = RuntimeError("events collector fail")
        service = AnalyzeCriticalNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        with pytest.raises(RuntimeError, match="events collector fail"):
            service.analyze(AnalyzeCriticalNamespaceEventsCommand(namespace="production"))

    def test_time_window_zero(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "production", "status": "Active", "age": "1d"}
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = [_event()]
        service = AnalyzeCriticalNamespaceEventsService(events_port=events_port, k8s_port=k8s_port)

        response = service.analyze(
            AnalyzeCriticalNamespaceEventsCommand(namespace="production", time_window_minutes=0)
        )

        assert response.namespace == "production"
