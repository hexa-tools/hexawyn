from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.get_namespace_events.command import (
    GetNamespaceEventsCommand,
)
from hexawyn.application.use_case.get_namespace_events.response import (
    GetNamespaceEventsResponse,
    NamespaceEventDict,
)
from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_service_port import (
    GetNamespaceEventsServicePort,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import (
    GetNamespaceEventsRequest,
    GetNamespaceEventsResult,
)
from hexawyn.domain.services.event_analysis.namespace_event_filter import get_namespace_events


class GetNamespaceEventsService(GetNamespaceEventsServicePort):
    def __init__(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port

    def get_events(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return _to_response(result)

    def _validate_namespace_exists(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )


def _to_response(result: GetNamespaceEventsResult) -> GetNamespaceEventsResponse:
    return GetNamespaceEventsResponse(
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_events=result.total_events,
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        summary=result.summary,
        events=[
            NamespaceEventDict(
                event_type=e.event_type,
                reason=e.reason,
                message=e.message,
                object=e.object,
                count=e.count,
                last_seen=e.last_seen,
                recurring=e.recurring,
                urgency=e.urgency,
                object_exists=e.object_exists,
            )
            for e in result.events
        ],
    )
