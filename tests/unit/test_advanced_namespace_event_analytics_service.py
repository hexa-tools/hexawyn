"""Unit tests for AdvancedNamespaceEventAnalyticsService (mocks both driven ports)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_command import (
    AdvancedNamespaceEventAnalyticsCommand,
)
from hexawyn.application.service.advanced_namespace_event_analytics_service import (
    AdvancedNamespaceEventAnalyticsService,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import NamespaceEvent


def _event(reason: str = "BackOff", obj: str = "pod/payment-api") -> NamespaceEvent:
    return NamespaceEvent(
        event_type="Warning",
        reason=reason,
        message=reason,
        object=obj,
        count=1,
        last_seen="2024-01-01T15:00:00Z",
    )


class TestAdvancedNamespaceEventAnalyticsService:
    def test_analyze_validates_namespace_then_returns_report(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "data-pipeline", "status": "Active", "age": "10d"}
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = [_event(), _event(), _event()]
        service = AdvancedNamespaceEventAnalyticsService(events_port=events_port, k8s_port=k8s_port)

        response = service.analyze(
            AdvancedNamespaceEventAnalyticsCommand(namespace="data-pipeline")
        )

        assert response.namespace == "data-pipeline"
        assert response.total_events == 3
        assert len(response.correlated_incidents) == 1
        incident = response.correlated_incidents[0]
        assert incident["reason"] == "BackOff"
        assert incident["event_count"] == 3
        assert len(incident["sample_events"]) == 3
        assert incident["sample_events"][0]["reason"] == "BackOff"
        events_port.list_events.assert_called_once()

    def test_analyze_raises_when_namespace_missing(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [{"name": "other", "status": "Active", "age": "1d"}]
        events_port = MagicMock()
        service = AdvancedNamespaceEventAnalyticsService(events_port=events_port, k8s_port=k8s_port)

        with pytest.raises(ResourceNotFoundError):
            service.analyze(AdvancedNamespaceEventAnalyticsCommand(namespace="ghost"))

        events_port.list_events.assert_not_called()

    def test_analyze_returns_empty_report_when_no_events(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "data-pipeline", "status": "Active", "age": "10d"}
        ]
        events_port = MagicMock()
        events_port.list_events.return_value = []
        service = AdvancedNamespaceEventAnalyticsService(events_port=events_port, k8s_port=k8s_port)

        response = service.analyze(
            AdvancedNamespaceEventAnalyticsCommand(namespace="data-pipeline")
        )

        assert response.total_events == 0
        assert response.storms == []
        assert response.correlated_incidents == []
