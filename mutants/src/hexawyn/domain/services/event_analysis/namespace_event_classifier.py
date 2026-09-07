from __future__ import annotations

from datetime import datetime

from hexawyn.domain.models.event import ClassifiedEvent, EventCategory, EventSeverity
from hexawyn.domain.models.namespace_event import NamespaceEvent

_REASON_CLASSIFICATION: dict[str, tuple[EventSeverity, EventCategory]] = {
    "OOMKilling": (EventSeverity.CRITICAL, EventCategory.RESOURCE),
    "OOMKilled": (EventSeverity.CRITICAL, EventCategory.RESOURCE),
    "BackOff": (EventSeverity.HIGH, EventCategory.LIFECYCLE),
    "CrashLoopBackOff": (EventSeverity.HIGH, EventCategory.LIFECYCLE),
    "FailedScheduling": (EventSeverity.HIGH, EventCategory.SCHEDULING),
    "FailedMount": (EventSeverity.MEDIUM, EventCategory.STORAGE),
}
_DEFAULT_WARNING_CLASSIFICATION = (EventSeverity.MEDIUM, EventCategory.OTHER)
_NORMAL_CLASSIFICATION = (EventSeverity.LOW, EventCategory.LIFECYCLE)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_namespace_event__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_namespace_event__mutmut)
def classify_namespace_event(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_orig(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_1(event: NamespaceEvent, namespace: str = "XXXX") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_2(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = None
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_3(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(None)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_4(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = None
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_5(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(None)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_6(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=None,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_7(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=None,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_8(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=None,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_9(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=None,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_10(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=None,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_11(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=None,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_12(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=None,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_13(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=None,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_14(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=None,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_15(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=None,
    )


def x_classify_namespace_event__mutmut_16(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_17(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_18(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_19(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_20(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_21(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_22(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        count=event.count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_23(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_24(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        last_timestamp=timestamp,
    )


def x_classify_namespace_event__mutmut_25(event: NamespaceEvent, namespace: str = "") -> ClassifiedEvent:
    """Maps a raw NamespaceEvent (K8s TYPE/REASON) to a ClassifiedEvent
    (severity + category), the input format ProgressiveEventAnalyzer,
    EventCorrelator, and RunbookSuggestionEngine all operate on."""
    severity, category = _classify(event)
    timestamp = _parse_timestamp(event.last_seen)
    return ClassifiedEvent(
        event_type=event.event_type,
        reason=event.reason,
        message=event.message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=event.object,
        count=event.count,
        first_timestamp=timestamp,
        )

mutants_x_classify_namespace_event__mutmut['_mutmut_orig'] = x_classify_namespace_event__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_1'] = x_classify_namespace_event__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_2'] = x_classify_namespace_event__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_3'] = x_classify_namespace_event__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_4'] = x_classify_namespace_event__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_5'] = x_classify_namespace_event__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_6'] = x_classify_namespace_event__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_7'] = x_classify_namespace_event__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_8'] = x_classify_namespace_event__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_9'] = x_classify_namespace_event__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_10'] = x_classify_namespace_event__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_11'] = x_classify_namespace_event__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_12'] = x_classify_namespace_event__mutmut_12 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_13'] = x_classify_namespace_event__mutmut_13 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_14'] = x_classify_namespace_event__mutmut_14 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_15'] = x_classify_namespace_event__mutmut_15 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_16'] = x_classify_namespace_event__mutmut_16 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_17'] = x_classify_namespace_event__mutmut_17 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_18'] = x_classify_namespace_event__mutmut_18 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_19'] = x_classify_namespace_event__mutmut_19 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_20'] = x_classify_namespace_event__mutmut_20 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_21'] = x_classify_namespace_event__mutmut_21 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_22'] = x_classify_namespace_event__mutmut_22 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_23'] = x_classify_namespace_event__mutmut_23 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_24'] = x_classify_namespace_event__mutmut_24 # type: ignore # mutmut generated
mutants_x_classify_namespace_event__mutmut['x_classify_namespace_event__mutmut_25'] = x_classify_namespace_event__mutmut_25 # type: ignore # mutmut generated
mutants_x__classify__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__classify__mutmut)
def _classify(event: NamespaceEvent) -> tuple[EventSeverity, EventCategory]:
    if event.event_type == "Normal":
        return _NORMAL_CLASSIFICATION
    return _REASON_CLASSIFICATION.get(event.reason, _DEFAULT_WARNING_CLASSIFICATION)


def x__classify__mutmut_orig(event: NamespaceEvent) -> tuple[EventSeverity, EventCategory]:
    if event.event_type == "Normal":
        return _NORMAL_CLASSIFICATION
    return _REASON_CLASSIFICATION.get(event.reason, _DEFAULT_WARNING_CLASSIFICATION)


def x__classify__mutmut_1(event: NamespaceEvent) -> tuple[EventSeverity, EventCategory]:
    if event.event_type != "Normal":
        return _NORMAL_CLASSIFICATION
    return _REASON_CLASSIFICATION.get(event.reason, _DEFAULT_WARNING_CLASSIFICATION)


def x__classify__mutmut_2(event: NamespaceEvent) -> tuple[EventSeverity, EventCategory]:
    if event.event_type == "XXNormalXX":
        return _NORMAL_CLASSIFICATION
    return _REASON_CLASSIFICATION.get(event.reason, _DEFAULT_WARNING_CLASSIFICATION)


def x__classify__mutmut_3(event: NamespaceEvent) -> tuple[EventSeverity, EventCategory]:
    if event.event_type == "normal":
        return _NORMAL_CLASSIFICATION
    return _REASON_CLASSIFICATION.get(event.reason, _DEFAULT_WARNING_CLASSIFICATION)


def x__classify__mutmut_4(event: NamespaceEvent) -> tuple[EventSeverity, EventCategory]:
    if event.event_type == "NORMAL":
        return _NORMAL_CLASSIFICATION
    return _REASON_CLASSIFICATION.get(event.reason, _DEFAULT_WARNING_CLASSIFICATION)


def x__classify__mutmut_5(event: NamespaceEvent) -> tuple[EventSeverity, EventCategory]:
    if event.event_type == "Normal":
        return _NORMAL_CLASSIFICATION
    return _REASON_CLASSIFICATION.get(None, _DEFAULT_WARNING_CLASSIFICATION)


def x__classify__mutmut_6(event: NamespaceEvent) -> tuple[EventSeverity, EventCategory]:
    if event.event_type == "Normal":
        return _NORMAL_CLASSIFICATION
    return _REASON_CLASSIFICATION.get(event.reason, None)


def x__classify__mutmut_7(event: NamespaceEvent) -> tuple[EventSeverity, EventCategory]:
    if event.event_type == "Normal":
        return _NORMAL_CLASSIFICATION
    return _REASON_CLASSIFICATION.get(_DEFAULT_WARNING_CLASSIFICATION)


def x__classify__mutmut_8(event: NamespaceEvent) -> tuple[EventSeverity, EventCategory]:
    if event.event_type == "Normal":
        return _NORMAL_CLASSIFICATION
    return _REASON_CLASSIFICATION.get(event.reason, )

mutants_x__classify__mutmut['_mutmut_orig'] = x__classify__mutmut_orig # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_1'] = x__classify__mutmut_1 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_2'] = x__classify__mutmut_2 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_3'] = x__classify__mutmut_3 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_4'] = x__classify__mutmut_4 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_5'] = x__classify__mutmut_5 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_6'] = x__classify__mutmut_6 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_7'] = x__classify__mutmut_7 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_8'] = x__classify__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_timestamp__mutmut)
def _parse_timestamp(raw: str) -> datetime | None:
    if not raw:
        return None
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def x__parse_timestamp__mutmut_orig(raw: str) -> datetime | None:
    if not raw:
        return None
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def x__parse_timestamp__mutmut_1(raw: str) -> datetime | None:
    if raw:
        return None
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def x__parse_timestamp__mutmut_2(raw: str) -> datetime | None:
    if not raw:
        return None
    return datetime.fromisoformat(None)


def x__parse_timestamp__mutmut_3(raw: str) -> datetime | None:
    if not raw:
        return None
    return datetime.fromisoformat(raw.replace(None, "+00:00"))


def x__parse_timestamp__mutmut_4(raw: str) -> datetime | None:
    if not raw:
        return None
    return datetime.fromisoformat(raw.replace("Z", None))


def x__parse_timestamp__mutmut_5(raw: str) -> datetime | None:
    if not raw:
        return None
    return datetime.fromisoformat(raw.replace("+00:00"))


def x__parse_timestamp__mutmut_6(raw: str) -> datetime | None:
    if not raw:
        return None
    return datetime.fromisoformat(raw.replace("Z", ))


def x__parse_timestamp__mutmut_7(raw: str) -> datetime | None:
    if not raw:
        return None
    return datetime.fromisoformat(raw.replace("XXZXX", "+00:00"))


def x__parse_timestamp__mutmut_8(raw: str) -> datetime | None:
    if not raw:
        return None
    return datetime.fromisoformat(raw.replace("z", "+00:00"))


def x__parse_timestamp__mutmut_9(raw: str) -> datetime | None:
    if not raw:
        return None
    return datetime.fromisoformat(raw.replace("Z", "XX+00:00XX"))

mutants_x__parse_timestamp__mutmut['_mutmut_orig'] = x__parse_timestamp__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_1'] = x__parse_timestamp__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_2'] = x__parse_timestamp__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_3'] = x__parse_timestamp__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_4'] = x__parse_timestamp__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_5'] = x__parse_timestamp__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_6'] = x__parse_timestamp__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_7'] = x__parse_timestamp__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_8'] = x__parse_timestamp__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_9'] = x__parse_timestamp__mutmut_9 # type: ignore # mutmut generated
