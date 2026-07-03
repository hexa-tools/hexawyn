from collections import defaultdict
from dataclasses import dataclass, field

from hexawyn.domain.models.event import ClassifiedEvent


@dataclass(frozen=True)
class CorrelatedIncident:
    """A group of events sharing the same REASON — the domain's unit of
    "likely one root cause", regardless of how many distinct objects
    (pods) are involved."""

    reason: str
    events: list[ClassifiedEvent] = field(default_factory=list)
    involved_objects: list[str] = field(default_factory=list)
    likely_root_cause: str = ""


class EventCorrelator:
    """Groups related events that likely share the same root cause.

    Grouping key is the event REASON, not the involved object — a single
    reason recurring across many pods (e.g. a cluster-wide OOM) is one
    incident, not one per pod.
    """

    def correlate(self, events: list[ClassifiedEvent]) -> list[CorrelatedIncident]:
        by_reason: dict[str, list[ClassifiedEvent]] = defaultdict(list)
        for event in events:
            by_reason[event.reason].append(event)

        return [self._to_incident(reason, group) for reason, group in by_reason.items()]

    @staticmethod
    def _to_incident(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = list(dict.fromkeys(event.involved_object for event in group))
        if len(involved_objects) > 1:
            root_cause = (
                f"{len(involved_objects)} objects affected by '{reason}' — "
                "likely a shared root cause (node/cluster-wide issue)"
            )
        else:
            root_cause = f"Repeated '{reason}' events on {involved_objects[0]}"
        return CorrelatedIncident(
            reason=reason,
            events=group,
            involved_objects=involved_objects,
            likely_root_cause=root_cause,
        )
