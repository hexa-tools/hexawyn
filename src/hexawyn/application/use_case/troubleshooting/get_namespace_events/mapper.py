from hexawyn.application.use_case.troubleshooting.get_namespace_events.response import (
    GetNamespaceEventsResponse,
    NamespaceEventDict,
)
from hexawyn.domain.models.namespace_event import GetNamespaceEventsResult


def to_response(result: GetNamespaceEventsResult) -> GetNamespaceEventsResponse:
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
