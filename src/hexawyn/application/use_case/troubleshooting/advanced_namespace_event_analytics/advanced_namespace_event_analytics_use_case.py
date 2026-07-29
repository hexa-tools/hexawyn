# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.troubleshooting.advanced_namespace_event_analytics.command import (  # noqa: E501
    AdvancedNamespaceEventAnalyticsCommand,
)
from hexawyn.application.use_case.troubleshooting.advanced_namespace_event_analytics.response import (  # noqa: E501  # type: ignore
    AdvancedNamespaceEventAnalyticsResponse,
    EventStormDict,
    IncidentSummaryDict,
    ReasonCountDict,
    SampleEventDict,
    TimelineBucketDict,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.event import ClassifiedEvent
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest
from hexawyn.domain.services.event_analysis.advanced_event_analytics import (
    AdvancedEventAnalyticsReport,
    IncidentSummary,
    generate_advanced_event_analytics,
)


class AdvancedNamespaceEventAnalyticsUseCase:
    def __init__(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port

    def execute(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(command.namespace, raw_events)
        return _to_response(report)

    def _validate_namespace_exists(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )


def _to_response(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def _to_incident_dict(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=incident.event_count,
        likely_root_cause=incident.likely_root_cause,
        sample_events=[_to_sample_event_dict(event) for event in incident.sample_events],
    )


def _to_sample_event_dict(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=event.reason,
        message=event.message,
        involved_object=event.involved_object,
        severity=event.severity.value,
        timestamp=event.last_timestamp.isoformat() if event.last_timestamp else "",
    )
