from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.troubleshooting.get_namespace_events.command import (
    GetNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.get_namespace_events.mapper import to_response
from hexawyn.application.use_case.troubleshooting.get_namespace_events.response import (
    GetNamespaceEventsResponse,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import (
    GetNamespaceEventsRequest,
)
from hexawyn.domain.services.event_analysis.namespace_event_filter import get_namespace_events


class GetNamespaceEventsUseCase:
    def __init__(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port

    def execute(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def _validate_namespace_exists(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )
