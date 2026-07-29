from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.troubleshooting.get_pod_events.command import (
    GetPodEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.get_pod_events.response import (
    GetPodEventsResponse,
)
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest


class GetPodEventsUseCase:
    def __init__(
        self,
        events_port: NamespaceEventsPort,
        k8s_port: K8sPort,
    ) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port

    def execute(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )
