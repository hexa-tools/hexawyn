from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.troubleshooting.summarize_namespace_events.command import (
    SummarizeNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.summarize_namespace_events.response import (
    SummarizeNamespaceEventsResponse,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest
from hexawyn.domain.services.event_analysis.progressive_namespace_analysis import (
    NamespaceEventsSummary,
    summarize_namespace_events,
)


class SummarizeNamespaceEventsUseCase:
    def __init__(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port

    def summarize(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(command.namespace, raw_events)
        return _to_response(summary)

    def _validate_namespace_exists(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )


def _to_response(summary: NamespaceEventsSummary) -> SummarizeNamespaceEventsResponse:
    return SummarizeNamespaceEventsResponse(
        namespace=summary.namespace,
        total_events=summary.total_events,
        severity_breakdown=summary.severity_breakdown,
        top_affected_pods=summary.top_affected_pods,  # type: ignore
    )
