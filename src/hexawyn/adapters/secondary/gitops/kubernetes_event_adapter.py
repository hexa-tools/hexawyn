from __future__ import annotations

from hexawyn.application.ports.driven.trace_event_correlation_port import (
    TraceEventCorrelationPort,
)
from hexawyn.domain.models.trace_k8s_events import (  # noqa: E501
    K8sEvent,
    K8sEventType,
    TraceEventCorrelationRequest,
)
from kubernetes import client, config


class KubernetesEventAdapter(TraceEventCorrelationPort):
    def fetch_k8s_events(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []

    def fetch_slowest_span(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=20)

            warning_events = [e for e in events.items if e.type == "Warning" and e.involved_object]
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: " f"{top.reason}"
            return None
        except Exception:
            return None
