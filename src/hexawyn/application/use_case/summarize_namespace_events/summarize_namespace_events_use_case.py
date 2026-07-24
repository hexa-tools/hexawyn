from __future__ import annotations

from collections import Counter

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.summarize_namespace_events.command import (
    SummarizeNamespaceEventsCommand,
)
from hexawyn.application.use_case.summarize_namespace_events.response import (
    SummarizeNamespaceEventsResponse,
)
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest


class SummarizeNamespaceEventsUseCase:
    def __init__(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port

    def execute(self, command: SummarizeNamespaceEventsCommand) -> SummarizeNamespaceEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        events = self._events_port.list_events(request)

        total = len(events)

        severity_counts: dict[str, int] = {}
        for e in events:
            label = e.urgency if e.urgency else "normal"
            severity_counts[label] = severity_counts.get(label, 0) + 1

        obj_counter: Counter[str] = Counter(e.object for e in events if e.object)
        top_objects = obj_counter.most_common(5)
        top_affected: list[dict[str, object]] = [
            {"pod_name": obj, "event_count": count} for obj, count in top_objects
        ]

        return SummarizeNamespaceEventsResponse(
            namespace=command.namespace,
            total_events=total,
            severity_breakdown=severity_counts,
            top_affected_pods=top_affected,
        )
