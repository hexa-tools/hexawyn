# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.troubleshooting.analyze_critical_namespace_events.command import (
    AnalyzeCriticalNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.analyze_critical_namespace_events.response import (  # noqa: E501
    AnalyzeCriticalNamespaceEventsResponse,
    CriticalIncidentDict,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest
from hexawyn.domain.services.event_analysis.progressive_namespace_analysis import (
    CriticalEventsAnalysis,
    analyze_critical_events,
)


class AnalyzeCriticalNamespaceEventsUseCase:
    def __init__(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port

    def execute(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(command.namespace, raw_events)  # type: ignore
        return _to_response(analysis)

    def _validate_namespace_exists(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )


def _to_response(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )
