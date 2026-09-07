from __future__ import annotations

from dataclasses import replace
from datetime import datetime

from hexawyn.domain.models.constants import NamespaceEventsConstants
from hexawyn.domain.models.namespace_event import (
    GetNamespaceEventsRequest,
    GetNamespaceEventsResult,
    NamespaceEvent,
    Urgency,
)

_cfg = NamespaceEventsConstants()
_NO_EVENTS_SUMMARY = "no events detected"
_RELEVANT_TYPES = frozenset({"Warning", "Error"})
_SEVERITY_ORDER = {"Error": 0, "Warning": 1}
_OBJECT_DELETED_NOTE = "object no longer exists"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_namespace_events__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_namespace_events__mutmut)
def get_namespace_events(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_orig(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_1(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = None
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_2(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type not in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_3(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_4(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=None,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_5(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=None,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_6(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=None,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_7(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=None,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_8(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_9(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_10(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_11(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_12(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=1,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_13(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = None
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_14(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(None, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_15(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, None) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_16(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_17(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, ) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_18(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=None)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_19(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = None
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_20(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = None
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_21(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = None

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_22(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(None, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_23(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, None)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_24(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_25(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, )

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_26(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(1, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_27(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total + request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_28(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = None
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_29(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(None)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_30(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(2 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_31(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = None
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_32(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "XXXX" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_33(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total != 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_34(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 2 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_35(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "XXsXX"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_36(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "S"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_37(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = None
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_38(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary = f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_39(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary -= f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_40(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=None,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_41(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=None,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_42(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=None,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_43(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=None,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_44(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=None,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_45(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=None,
        summary=summary,
    )


def x_get_namespace_events__mutmut_46(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=None,
    )


def x_get_namespace_events__mutmut_47(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_48(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_49(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_50(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        has_more=remaining > 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_51(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_52(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        summary=summary,
    )


def x_get_namespace_events__mutmut_53(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 0,
        remaining_count=remaining,
        )


def x_get_namespace_events__mutmut_54(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining >= 0,
        remaining_count=remaining,
        summary=summary,
    )


def x_get_namespace_events__mutmut_55(
    request: GetNamespaceEventsRequest,
    raw_events: list[NamespaceEvent],
    observed_at: datetime,
) -> GetNamespaceEventsResult:
    """Domain service — filters, flags, sorts, and paginates namespace events
    (ECA-5 dependency: namespace existence is validated one layer up, by the
    application service, before this pure function ever runs).
    """
    relevant = [e for e in raw_events if e.event_type in _RELEVANT_TYPES]
    if not relevant:
        return GetNamespaceEventsResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_events=0,
            summary=_NO_EVENTS_SUMMARY,
        )

    finalized = [_finalize(event, observed_at) for event in relevant]
    finalized.sort(key=_sort_key)

    total = len(finalized)
    top = finalized[: request.top_n]
    remaining = max(0, total - request.top_n)

    recurring_count = sum(1 for e in finalized if e.recurring)
    plural = "" if total == 1 else "s"
    summary = f"{total} event{plural} detected"
    if recurring_count:
        summary += f", {recurring_count} recurring"

    return GetNamespaceEventsResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_events=total,
        events=top,
        has_more=remaining > 1,
        remaining_count=remaining,
        summary=summary,
    )

mutants_x_get_namespace_events__mutmut['_mutmut_orig'] = x_get_namespace_events__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_1'] = x_get_namespace_events__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_2'] = x_get_namespace_events__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_3'] = x_get_namespace_events__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_4'] = x_get_namespace_events__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_5'] = x_get_namespace_events__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_6'] = x_get_namespace_events__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_7'] = x_get_namespace_events__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_8'] = x_get_namespace_events__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_9'] = x_get_namespace_events__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_10'] = x_get_namespace_events__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_11'] = x_get_namespace_events__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_12'] = x_get_namespace_events__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_13'] = x_get_namespace_events__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_14'] = x_get_namespace_events__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_15'] = x_get_namespace_events__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_16'] = x_get_namespace_events__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_17'] = x_get_namespace_events__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_18'] = x_get_namespace_events__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_19'] = x_get_namespace_events__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_20'] = x_get_namespace_events__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_21'] = x_get_namespace_events__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_22'] = x_get_namespace_events__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_23'] = x_get_namespace_events__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_24'] = x_get_namespace_events__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_25'] = x_get_namespace_events__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_26'] = x_get_namespace_events__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_27'] = x_get_namespace_events__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_28'] = x_get_namespace_events__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_29'] = x_get_namespace_events__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_30'] = x_get_namespace_events__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_31'] = x_get_namespace_events__mutmut_31 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_32'] = x_get_namespace_events__mutmut_32 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_33'] = x_get_namespace_events__mutmut_33 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_34'] = x_get_namespace_events__mutmut_34 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_35'] = x_get_namespace_events__mutmut_35 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_36'] = x_get_namespace_events__mutmut_36 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_37'] = x_get_namespace_events__mutmut_37 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_38'] = x_get_namespace_events__mutmut_38 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_39'] = x_get_namespace_events__mutmut_39 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_40'] = x_get_namespace_events__mutmut_40 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_41'] = x_get_namespace_events__mutmut_41 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_42'] = x_get_namespace_events__mutmut_42 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_43'] = x_get_namespace_events__mutmut_43 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_44'] = x_get_namespace_events__mutmut_44 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_45'] = x_get_namespace_events__mutmut_45 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_46'] = x_get_namespace_events__mutmut_46 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_47'] = x_get_namespace_events__mutmut_47 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_48'] = x_get_namespace_events__mutmut_48 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_49'] = x_get_namespace_events__mutmut_49 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_50'] = x_get_namespace_events__mutmut_50 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_51'] = x_get_namespace_events__mutmut_51 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_52'] = x_get_namespace_events__mutmut_52 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_53'] = x_get_namespace_events__mutmut_53 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_54'] = x_get_namespace_events__mutmut_54 # type: ignore # mutmut generated
mutants_x_get_namespace_events__mutmut['x_get_namespace_events__mutmut_55'] = x_get_namespace_events__mutmut_55 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__sort_key__mutmut)
def _sort_key(event: NamespaceEvent) -> tuple[int, float]:
    """Ascending sort: severity rank first (Error before Warning), then most
    recent last_seen first (negated timestamp) as the secondary key."""
    return (
        _SEVERITY_ORDER.get(event.event_type, 2),
        -_parse_timestamp(event.last_seen).timestamp(),
    )


def x__sort_key__mutmut_orig(event: NamespaceEvent) -> tuple[int, float]:
    """Ascending sort: severity rank first (Error before Warning), then most
    recent last_seen first (negated timestamp) as the secondary key."""
    return (
        _SEVERITY_ORDER.get(event.event_type, 2),
        -_parse_timestamp(event.last_seen).timestamp(),
    )


def x__sort_key__mutmut_1(event: NamespaceEvent) -> tuple[int, float]:
    """Ascending sort: severity rank first (Error before Warning), then most
    recent last_seen first (negated timestamp) as the secondary key."""
    return (
        _SEVERITY_ORDER.get(None, 2),
        -_parse_timestamp(event.last_seen).timestamp(),
    )


def x__sort_key__mutmut_2(event: NamespaceEvent) -> tuple[int, float]:
    """Ascending sort: severity rank first (Error before Warning), then most
    recent last_seen first (negated timestamp) as the secondary key."""
    return (
        _SEVERITY_ORDER.get(event.event_type, None),
        -_parse_timestamp(event.last_seen).timestamp(),
    )


def x__sort_key__mutmut_3(event: NamespaceEvent) -> tuple[int, float]:
    """Ascending sort: severity rank first (Error before Warning), then most
    recent last_seen first (negated timestamp) as the secondary key."""
    return (
        _SEVERITY_ORDER.get(2),
        -_parse_timestamp(event.last_seen).timestamp(),
    )


def x__sort_key__mutmut_4(event: NamespaceEvent) -> tuple[int, float]:
    """Ascending sort: severity rank first (Error before Warning), then most
    recent last_seen first (negated timestamp) as the secondary key."""
    return (
        _SEVERITY_ORDER.get(event.event_type, ),
        -_parse_timestamp(event.last_seen).timestamp(),
    )


def x__sort_key__mutmut_5(event: NamespaceEvent) -> tuple[int, float]:
    """Ascending sort: severity rank first (Error before Warning), then most
    recent last_seen first (negated timestamp) as the secondary key."""
    return (
        _SEVERITY_ORDER.get(event.event_type, 3),
        -_parse_timestamp(event.last_seen).timestamp(),
    )


def x__sort_key__mutmut_6(event: NamespaceEvent) -> tuple[int, float]:
    """Ascending sort: severity rank first (Error before Warning), then most
    recent last_seen first (negated timestamp) as the secondary key."""
    return (
        _SEVERITY_ORDER.get(event.event_type, 2),
        +_parse_timestamp(event.last_seen).timestamp(),
    )


def x__sort_key__mutmut_7(event: NamespaceEvent) -> tuple[int, float]:
    """Ascending sort: severity rank first (Error before Warning), then most
    recent last_seen first (negated timestamp) as the secondary key."""
    return (
        _SEVERITY_ORDER.get(event.event_type, 2),
        -_parse_timestamp(None).timestamp(),
    )

mutants_x__sort_key__mutmut['_mutmut_orig'] = x__sort_key__mutmut_orig # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_1'] = x__sort_key__mutmut_1 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_2'] = x__sort_key__mutmut_2 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_3'] = x__sort_key__mutmut_3 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_4'] = x__sort_key__mutmut_4 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_5'] = x__sort_key__mutmut_5 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_6'] = x__sort_key__mutmut_6 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_7'] = x__sort_key__mutmut_7 # type: ignore # mutmut generated
mutants_x__finalize__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__finalize__mutmut)
def _finalize(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_orig(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_1(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = None
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_2(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count >= _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_3(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = None
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_4(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(None, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_5(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, None)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_6(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_7(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, )
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_8(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = None
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_9(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists or _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_10(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_11(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_12(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = None
    return replace(event, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_13(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(None, recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_14(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=None, urgency=urgency, message=message)


def x__finalize__mutmut_15(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=None, message=message)


def x__finalize__mutmut_16(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, message=None)


def x__finalize__mutmut_17(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(recurring=recurring, urgency=urgency, message=message)


def x__finalize__mutmut_18(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, urgency=urgency, message=message)


def x__finalize__mutmut_19(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, message=message)


def x__finalize__mutmut_20(event: NamespaceEvent, observed_at: datetime) -> NamespaceEvent:
    recurring = event.count > _cfg.recurring_count_threshold
    urgency = _compute_urgency(event, observed_at)
    message = event.message
    if not event.object_exists and _OBJECT_DELETED_NOTE not in message:
        message = f"{message} ({_OBJECT_DELETED_NOTE})"
    return replace(event, recurring=recurring, urgency=urgency, )

mutants_x__finalize__mutmut['_mutmut_orig'] = x__finalize__mutmut_orig # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_1'] = x__finalize__mutmut_1 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_2'] = x__finalize__mutmut_2 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_3'] = x__finalize__mutmut_3 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_4'] = x__finalize__mutmut_4 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_5'] = x__finalize__mutmut_5 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_6'] = x__finalize__mutmut_6 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_7'] = x__finalize__mutmut_7 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_8'] = x__finalize__mutmut_8 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_9'] = x__finalize__mutmut_9 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_10'] = x__finalize__mutmut_10 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_11'] = x__finalize__mutmut_11 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_12'] = x__finalize__mutmut_12 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_13'] = x__finalize__mutmut_13 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_14'] = x__finalize__mutmut_14 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_15'] = x__finalize__mutmut_15 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_16'] = x__finalize__mutmut_16 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_17'] = x__finalize__mutmut_17 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_18'] = x__finalize__mutmut_18 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_19'] = x__finalize__mutmut_19 # type: ignore # mutmut generated
mutants_x__finalize__mutmut['x__finalize__mutmut_20'] = x__finalize__mutmut_20 # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_urgency__mutmut)
def _compute_urgency(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "normal"
    age_seconds = (observed_at - _parse_timestamp(event.last_seen)).total_seconds()
    return "high" if age_seconds < _cfg.urgency_recent_window_seconds else "normal"


def x__compute_urgency__mutmut_orig(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "normal"
    age_seconds = (observed_at - _parse_timestamp(event.last_seen)).total_seconds()
    return "high" if age_seconds < _cfg.urgency_recent_window_seconds else "normal"


def x__compute_urgency__mutmut_1(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count == 1:
        return "normal"
    age_seconds = (observed_at - _parse_timestamp(event.last_seen)).total_seconds()
    return "high" if age_seconds < _cfg.urgency_recent_window_seconds else "normal"


def x__compute_urgency__mutmut_2(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 2:
        return "normal"
    age_seconds = (observed_at - _parse_timestamp(event.last_seen)).total_seconds()
    return "high" if age_seconds < _cfg.urgency_recent_window_seconds else "normal"


def x__compute_urgency__mutmut_3(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "XXnormalXX"
    age_seconds = (observed_at - _parse_timestamp(event.last_seen)).total_seconds()
    return "high" if age_seconds < _cfg.urgency_recent_window_seconds else "normal"


def x__compute_urgency__mutmut_4(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "NORMAL"
    age_seconds = (observed_at - _parse_timestamp(event.last_seen)).total_seconds()
    return "high" if age_seconds < _cfg.urgency_recent_window_seconds else "normal"


def x__compute_urgency__mutmut_5(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "normal"
    age_seconds = None
    return "high" if age_seconds < _cfg.urgency_recent_window_seconds else "normal"


def x__compute_urgency__mutmut_6(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "normal"
    age_seconds = (observed_at + _parse_timestamp(event.last_seen)).total_seconds()
    return "high" if age_seconds < _cfg.urgency_recent_window_seconds else "normal"


def x__compute_urgency__mutmut_7(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "normal"
    age_seconds = (observed_at - _parse_timestamp(None)).total_seconds()
    return "high" if age_seconds < _cfg.urgency_recent_window_seconds else "normal"


def x__compute_urgency__mutmut_8(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "normal"
    age_seconds = (observed_at - _parse_timestamp(event.last_seen)).total_seconds()
    return "XXhighXX" if age_seconds < _cfg.urgency_recent_window_seconds else "normal"


def x__compute_urgency__mutmut_9(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "normal"
    age_seconds = (observed_at - _parse_timestamp(event.last_seen)).total_seconds()
    return "HIGH" if age_seconds < _cfg.urgency_recent_window_seconds else "normal"


def x__compute_urgency__mutmut_10(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "normal"
    age_seconds = (observed_at - _parse_timestamp(event.last_seen)).total_seconds()
    return "high" if age_seconds <= _cfg.urgency_recent_window_seconds else "normal"


def x__compute_urgency__mutmut_11(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "normal"
    age_seconds = (observed_at - _parse_timestamp(event.last_seen)).total_seconds()
    return "high" if age_seconds < _cfg.urgency_recent_window_seconds else "XXnormalXX"


def x__compute_urgency__mutmut_12(event: NamespaceEvent, observed_at: datetime) -> Urgency:
    if event.count != 1:
        return "normal"
    age_seconds = (observed_at - _parse_timestamp(event.last_seen)).total_seconds()
    return "high" if age_seconds < _cfg.urgency_recent_window_seconds else "NORMAL"

mutants_x__compute_urgency__mutmut['_mutmut_orig'] = x__compute_urgency__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut['x__compute_urgency__mutmut_1'] = x__compute_urgency__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut['x__compute_urgency__mutmut_2'] = x__compute_urgency__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut['x__compute_urgency__mutmut_3'] = x__compute_urgency__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut['x__compute_urgency__mutmut_4'] = x__compute_urgency__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut['x__compute_urgency__mutmut_5'] = x__compute_urgency__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut['x__compute_urgency__mutmut_6'] = x__compute_urgency__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut['x__compute_urgency__mutmut_7'] = x__compute_urgency__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut['x__compute_urgency__mutmut_8'] = x__compute_urgency__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut['x__compute_urgency__mutmut_9'] = x__compute_urgency__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut['x__compute_urgency__mutmut_10'] = x__compute_urgency__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut['x__compute_urgency__mutmut_11'] = x__compute_urgency__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_urgency__mutmut['x__compute_urgency__mutmut_12'] = x__compute_urgency__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_timestamp__mutmut)
def _parse_timestamp(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def x__parse_timestamp__mutmut_orig(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def x__parse_timestamp__mutmut_1(raw: str) -> datetime:
    return datetime.fromisoformat(None)


def x__parse_timestamp__mutmut_2(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace(None, "+00:00"))


def x__parse_timestamp__mutmut_3(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", None))


def x__parse_timestamp__mutmut_4(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("+00:00"))


def x__parse_timestamp__mutmut_5(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", ))


def x__parse_timestamp__mutmut_6(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("XXZXX", "+00:00"))


def x__parse_timestamp__mutmut_7(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("z", "+00:00"))


def x__parse_timestamp__mutmut_8(raw: str) -> datetime:
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
