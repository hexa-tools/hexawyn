from collections import defaultdict
from dataclasses import dataclass, field

from hexawyn.domain.models.event import ClassifiedEvent


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class CorrelatedIncident:
    """A group of events sharing the same REASON — the domain's unit of
    "likely one root cause", regardless of how many distinct objects
    (pods) are involved."""

    reason: str
    events: list[ClassifiedEvent] = field(default_factory=list)
    involved_objects: list[str] = field(default_factory=list)
    likely_root_cause: str = ""
mutants_xǁEventCorrelatorǁcorrelate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁEventCorrelatorǁ_to_incident__mutmut: MutantDict = {}  # type: ignore


class EventCorrelator:
    """Groups related events that likely share the same root cause.

    Grouping key is the event REASON, not the involved object — a single
    reason recurring across many pods (e.g. a cluster-wide OOM) is one
    incident, not one per pod.
    """

    @_mutmut_mutated(mutants_xǁEventCorrelatorǁcorrelate__mutmut)
    def correlate(self, events: list[ClassifiedEvent]) -> list[CorrelatedIncident]:
        by_reason: dict[str, list[ClassifiedEvent]] = defaultdict(list)
        for event in events:
            by_reason[event.reason].append(event)

        return [self._to_incident(reason, group) for reason, group in by_reason.items()]

    def xǁEventCorrelatorǁcorrelate__mutmut_orig(self, events: list[ClassifiedEvent]) -> list[CorrelatedIncident]:
        by_reason: dict[str, list[ClassifiedEvent]] = defaultdict(list)
        for event in events:
            by_reason[event.reason].append(event)

        return [self._to_incident(reason, group) for reason, group in by_reason.items()]

    def xǁEventCorrelatorǁcorrelate__mutmut_1(self, events: list[ClassifiedEvent]) -> list[CorrelatedIncident]:
        by_reason: dict[str, list[ClassifiedEvent]] = None
        for event in events:
            by_reason[event.reason].append(event)

        return [self._to_incident(reason, group) for reason, group in by_reason.items()]

    def xǁEventCorrelatorǁcorrelate__mutmut_2(self, events: list[ClassifiedEvent]) -> list[CorrelatedIncident]:
        by_reason: dict[str, list[ClassifiedEvent]] = defaultdict(None)
        for event in events:
            by_reason[event.reason].append(event)

        return [self._to_incident(reason, group) for reason, group in by_reason.items()]

    def xǁEventCorrelatorǁcorrelate__mutmut_3(self, events: list[ClassifiedEvent]) -> list[CorrelatedIncident]:
        by_reason: dict[str, list[ClassifiedEvent]] = defaultdict(list)
        for event in events:
            by_reason[event.reason].append(None)

        return [self._to_incident(reason, group) for reason, group in by_reason.items()]

    def xǁEventCorrelatorǁcorrelate__mutmut_4(self, events: list[ClassifiedEvent]) -> list[CorrelatedIncident]:
        by_reason: dict[str, list[ClassifiedEvent]] = defaultdict(list)
        for event in events:
            by_reason[event.reason].append(event)

        return [self._to_incident(None, group) for reason, group in by_reason.items()]

    def xǁEventCorrelatorǁcorrelate__mutmut_5(self, events: list[ClassifiedEvent]) -> list[CorrelatedIncident]:
        by_reason: dict[str, list[ClassifiedEvent]] = defaultdict(list)
        for event in events:
            by_reason[event.reason].append(event)

        return [self._to_incident(reason, None) for reason, group in by_reason.items()]

    def xǁEventCorrelatorǁcorrelate__mutmut_6(self, events: list[ClassifiedEvent]) -> list[CorrelatedIncident]:
        by_reason: dict[str, list[ClassifiedEvent]] = defaultdict(list)
        for event in events:
            by_reason[event.reason].append(event)

        return [self._to_incident(group) for reason, group in by_reason.items()]

    def xǁEventCorrelatorǁcorrelate__mutmut_7(self, events: list[ClassifiedEvent]) -> list[CorrelatedIncident]:
        by_reason: dict[str, list[ClassifiedEvent]] = defaultdict(list)
        for event in events:
            by_reason[event.reason].append(event)

        return [self._to_incident(reason, ) for reason, group in by_reason.items()]

    @staticmethod
    @_mutmut_mutated(mutants_xǁEventCorrelatorǁ_to_incident__mutmut)
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

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_orig(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
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

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_1(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = None
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

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_2(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = list(None)
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

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_3(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = list(dict.fromkeys(None))
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

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_4(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = list(dict.fromkeys(event.involved_object for event in group))
        if len(involved_objects) >= 1:
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

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_5(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = list(dict.fromkeys(event.involved_object for event in group))
        if len(involved_objects) > 2:
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

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_6(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = list(dict.fromkeys(event.involved_object for event in group))
        if len(involved_objects) > 1:
            root_cause = None
        else:
            root_cause = f"Repeated '{reason}' events on {involved_objects[0]}"
        return CorrelatedIncident(
            reason=reason,
            events=group,
            involved_objects=involved_objects,
            likely_root_cause=root_cause,
        )

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_7(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = list(dict.fromkeys(event.involved_object for event in group))
        if len(involved_objects) > 1:
            root_cause = (
                f"{len(involved_objects)} objects affected by '{reason}' — "
                "XXlikely a shared root cause (node/cluster-wide issue)XX"
            )
        else:
            root_cause = f"Repeated '{reason}' events on {involved_objects[0]}"
        return CorrelatedIncident(
            reason=reason,
            events=group,
            involved_objects=involved_objects,
            likely_root_cause=root_cause,
        )

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_8(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = list(dict.fromkeys(event.involved_object for event in group))
        if len(involved_objects) > 1:
            root_cause = (
                f"{len(involved_objects)} objects affected by '{reason}' — "
                "LIKELY A SHARED ROOT CAUSE (NODE/CLUSTER-WIDE ISSUE)"
            )
        else:
            root_cause = f"Repeated '{reason}' events on {involved_objects[0]}"
        return CorrelatedIncident(
            reason=reason,
            events=group,
            involved_objects=involved_objects,
            likely_root_cause=root_cause,
        )

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_9(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = list(dict.fromkeys(event.involved_object for event in group))
        if len(involved_objects) > 1:
            root_cause = (
                f"{len(involved_objects)} objects affected by '{reason}' — "
                "likely a shared root cause (node/cluster-wide issue)"
            )
        else:
            root_cause = None
        return CorrelatedIncident(
            reason=reason,
            events=group,
            involved_objects=involved_objects,
            likely_root_cause=root_cause,
        )

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_10(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = list(dict.fromkeys(event.involved_object for event in group))
        if len(involved_objects) > 1:
            root_cause = (
                f"{len(involved_objects)} objects affected by '{reason}' — "
                "likely a shared root cause (node/cluster-wide issue)"
            )
        else:
            root_cause = f"Repeated '{reason}' events on {involved_objects[1]}"
        return CorrelatedIncident(
            reason=reason,
            events=group,
            involved_objects=involved_objects,
            likely_root_cause=root_cause,
        )

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_11(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = list(dict.fromkeys(event.involved_object for event in group))
        if len(involved_objects) > 1:
            root_cause = (
                f"{len(involved_objects)} objects affected by '{reason}' — "
                "likely a shared root cause (node/cluster-wide issue)"
            )
        else:
            root_cause = f"Repeated '{reason}' events on {involved_objects[0]}"
        return CorrelatedIncident(
            reason=None,
            events=group,
            involved_objects=involved_objects,
            likely_root_cause=root_cause,
        )

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_12(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
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
            events=None,
            involved_objects=involved_objects,
            likely_root_cause=root_cause,
        )

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_13(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
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
            involved_objects=None,
            likely_root_cause=root_cause,
        )

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_14(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
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
            likely_root_cause=None,
        )

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_15(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
        involved_objects = list(dict.fromkeys(event.involved_object for event in group))
        if len(involved_objects) > 1:
            root_cause = (
                f"{len(involved_objects)} objects affected by '{reason}' — "
                "likely a shared root cause (node/cluster-wide issue)"
            )
        else:
            root_cause = f"Repeated '{reason}' events on {involved_objects[0]}"
        return CorrelatedIncident(
            events=group,
            involved_objects=involved_objects,
            likely_root_cause=root_cause,
        )

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_16(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
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
            involved_objects=involved_objects,
            likely_root_cause=root_cause,
        )

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_17(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
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
            likely_root_cause=root_cause,
        )

    @staticmethod
    def xǁEventCorrelatorǁ_to_incident__mutmut_18(reason: str, group: list[ClassifiedEvent]) -> CorrelatedIncident:
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
            )

mutants_xǁEventCorrelatorǁcorrelate__mutmut['_mutmut_orig'] = EventCorrelator.xǁEventCorrelatorǁcorrelate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁcorrelate__mutmut['xǁEventCorrelatorǁcorrelate__mutmut_1'] = EventCorrelator.xǁEventCorrelatorǁcorrelate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁcorrelate__mutmut['xǁEventCorrelatorǁcorrelate__mutmut_2'] = EventCorrelator.xǁEventCorrelatorǁcorrelate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁcorrelate__mutmut['xǁEventCorrelatorǁcorrelate__mutmut_3'] = EventCorrelator.xǁEventCorrelatorǁcorrelate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁcorrelate__mutmut['xǁEventCorrelatorǁcorrelate__mutmut_4'] = EventCorrelator.xǁEventCorrelatorǁcorrelate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁcorrelate__mutmut['xǁEventCorrelatorǁcorrelate__mutmut_5'] = EventCorrelator.xǁEventCorrelatorǁcorrelate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁcorrelate__mutmut['xǁEventCorrelatorǁcorrelate__mutmut_6'] = EventCorrelator.xǁEventCorrelatorǁcorrelate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁcorrelate__mutmut['xǁEventCorrelatorǁcorrelate__mutmut_7'] = EventCorrelator.xǁEventCorrelatorǁcorrelate__mutmut_7 # type: ignore # mutmut generated

mutants_xǁEventCorrelatorǁ_to_incident__mutmut['_mutmut_orig'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_1'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_2'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_3'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_4'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_5'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_6'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_7'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_7 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_8'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_8 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_9'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_9 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_10'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_10 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_11'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_11 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_12'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_12 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_13'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_13 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_14'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_14 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_15'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_15 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_16'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_16 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_17'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_17 # type: ignore # mutmut generated
mutants_xǁEventCorrelatorǁ_to_incident__mutmut['xǁEventCorrelatorǁ_to_incident__mutmut_18'] = EventCorrelator.xǁEventCorrelatorǁ_to_incident__mutmut_18 # type: ignore # mutmut generated
