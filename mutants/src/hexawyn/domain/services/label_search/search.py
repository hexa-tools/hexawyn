from __future__ import annotations

from hexawyn.application.ports.driven.resource_search_port import MatchedResourceRaw
from hexawyn.domain.models.constants import LabelSearchConstants
from hexawyn.domain.models.label_search import (
    LabelSearchRequest,
    LabelSearchResult,
    MatchedResourceResult,
)
from hexawyn.domain.services.label_search.label_parser import parse_label_selector
from hexawyn.domain.services.label_search.resource_grouping import group_by_namespace
from hexawyn.domain.services.label_search.status_formatter import (
    is_pod_healthy,
    summarize_health,
)

_cfg = LabelSearchConstants()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_search_resources_by_labels__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_search_resources_by_labels__mutmut)
def search_resources_by_labels(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_orig(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_1(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(None)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_2(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = None
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_3(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total != 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_4(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 1:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_5(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=None,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_6(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=None,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_7(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=None,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_8(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=None,
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_9(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_10(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_11(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_12(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_13(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=1,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_14(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=False,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_15(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health(None, request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_16(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], None),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_17(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health(request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_18(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], ),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_19(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = None
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_20(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total >= _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_21(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = None
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_22(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(None, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_23(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, None)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_24(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_25(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, )
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_26(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(1, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_27(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total + _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_28(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = None

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_29(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = None
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_30(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(None) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_31(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = None
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_32(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(None)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_33(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = None

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_34(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(None, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_35(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, None)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_36(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_37(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, )

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_38(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=None,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_39(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=None,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_40(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=None,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_41(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=None,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_42(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=None,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_43(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=None,
    )


def x_search_resources_by_labels__mutmut_44(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_45(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_46(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        has_more=has_more,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_47(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        remaining_count=remaining_count,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_48(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        summary=summary,
    )


def x_search_resources_by_labels__mutmut_49(
    request: LabelSearchRequest, raw_matches: list[MatchedResourceRaw]
) -> LabelSearchResult:
    """Composes label-parsed validation, truncation, health flagging, and
    namespace grouping into one report. Pure domain function — raw_matches is
    already fetched through ResourceSearchPort.
    """
    parse_label_selector(request.label_selector)

    total = len(raw_matches)
    if total == 0:
        return LabelSearchResult(
            label_selector=request.label_selector,
            total_matched=0,
            no_matches=True,
            summary=summarize_health([], request.label_selector),
        )

    has_more = total > _cfg.max_results
    remaining_count = max(0, total - _cfg.max_results)
    limited = raw_matches[: _cfg.max_results]

    resources = [_to_result(item) for item in limited]
    groups = group_by_namespace(resources)
    summary = summarize_health(resources, request.label_selector)

    return LabelSearchResult(
        label_selector=request.label_selector,
        total_matched=total,
        groups=groups,
        has_more=has_more,
        remaining_count=remaining_count,
        )

mutants_x_search_resources_by_labels__mutmut['_mutmut_orig'] = x_search_resources_by_labels__mutmut_orig # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_1'] = x_search_resources_by_labels__mutmut_1 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_2'] = x_search_resources_by_labels__mutmut_2 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_3'] = x_search_resources_by_labels__mutmut_3 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_4'] = x_search_resources_by_labels__mutmut_4 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_5'] = x_search_resources_by_labels__mutmut_5 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_6'] = x_search_resources_by_labels__mutmut_6 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_7'] = x_search_resources_by_labels__mutmut_7 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_8'] = x_search_resources_by_labels__mutmut_8 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_9'] = x_search_resources_by_labels__mutmut_9 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_10'] = x_search_resources_by_labels__mutmut_10 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_11'] = x_search_resources_by_labels__mutmut_11 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_12'] = x_search_resources_by_labels__mutmut_12 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_13'] = x_search_resources_by_labels__mutmut_13 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_14'] = x_search_resources_by_labels__mutmut_14 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_15'] = x_search_resources_by_labels__mutmut_15 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_16'] = x_search_resources_by_labels__mutmut_16 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_17'] = x_search_resources_by_labels__mutmut_17 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_18'] = x_search_resources_by_labels__mutmut_18 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_19'] = x_search_resources_by_labels__mutmut_19 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_20'] = x_search_resources_by_labels__mutmut_20 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_21'] = x_search_resources_by_labels__mutmut_21 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_22'] = x_search_resources_by_labels__mutmut_22 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_23'] = x_search_resources_by_labels__mutmut_23 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_24'] = x_search_resources_by_labels__mutmut_24 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_25'] = x_search_resources_by_labels__mutmut_25 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_26'] = x_search_resources_by_labels__mutmut_26 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_27'] = x_search_resources_by_labels__mutmut_27 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_28'] = x_search_resources_by_labels__mutmut_28 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_29'] = x_search_resources_by_labels__mutmut_29 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_30'] = x_search_resources_by_labels__mutmut_30 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_31'] = x_search_resources_by_labels__mutmut_31 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_32'] = x_search_resources_by_labels__mutmut_32 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_33'] = x_search_resources_by_labels__mutmut_33 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_34'] = x_search_resources_by_labels__mutmut_34 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_35'] = x_search_resources_by_labels__mutmut_35 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_36'] = x_search_resources_by_labels__mutmut_36 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_37'] = x_search_resources_by_labels__mutmut_37 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_38'] = x_search_resources_by_labels__mutmut_38 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_39'] = x_search_resources_by_labels__mutmut_39 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_40'] = x_search_resources_by_labels__mutmut_40 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_41'] = x_search_resources_by_labels__mutmut_41 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_42'] = x_search_resources_by_labels__mutmut_42 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_43'] = x_search_resources_by_labels__mutmut_43 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_44'] = x_search_resources_by_labels__mutmut_44 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_45'] = x_search_resources_by_labels__mutmut_45 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_46'] = x_search_resources_by_labels__mutmut_46 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_47'] = x_search_resources_by_labels__mutmut_47 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_48'] = x_search_resources_by_labels__mutmut_48 # type: ignore # mutmut generated
mutants_x_search_resources_by_labels__mutmut['x_search_resources_by_labels__mutmut_49'] = x_search_resources_by_labels__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_result__mutmut)
def _to_result(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_orig(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_1(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = None
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_2(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["XXphaseXX"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_3(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["PHASE"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_4(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=None,
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_5(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=None,
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_6(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=None,  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_7(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=None,
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_8(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=None,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_9(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=None,
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_10(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=None,
        labels=item["labels"],
    )


def x__to_result__mutmut_11(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=None,
    )


def x__to_result__mutmut_12(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_13(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_14(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_15(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_16(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_17(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_18(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        labels=item["labels"],
    )


def x__to_result__mutmut_19(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        )


def x__to_result__mutmut_20(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["XXnameXX"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_21(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["NAME"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_22(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["XXnamespaceXX"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_23(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["NAMESPACE"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_24(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["XXkindXX"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_25(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["KIND"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_26(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["XXnodeXX"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_27(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["NODE"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_28(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["XXreadyXX"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_29(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["READY"],
        is_healthy=is_pod_healthy(phase),
        labels=item["labels"],
    )


def x__to_result__mutmut_30(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(None),
        labels=item["labels"],
    )


def x__to_result__mutmut_31(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["XXlabelsXX"],
    )


def x__to_result__mutmut_32(item: MatchedResourceRaw) -> MatchedResourceResult:
    phase = item["phase"]
    return MatchedResourceResult(
        name=item["name"],
        namespace=item["namespace"],
        kind=item["kind"],  # type: ignore[arg-type]
        node=item["node"],
        phase=phase,
        ready=item["ready"],
        is_healthy=is_pod_healthy(phase),
        labels=item["LABELS"],
    )

mutants_x__to_result__mutmut['_mutmut_orig'] = x__to_result__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_1'] = x__to_result__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_2'] = x__to_result__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_3'] = x__to_result__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_4'] = x__to_result__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_5'] = x__to_result__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_6'] = x__to_result__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_7'] = x__to_result__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_8'] = x__to_result__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_9'] = x__to_result__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_10'] = x__to_result__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_11'] = x__to_result__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_12'] = x__to_result__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_13'] = x__to_result__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_14'] = x__to_result__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_15'] = x__to_result__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_16'] = x__to_result__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_17'] = x__to_result__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_18'] = x__to_result__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_19'] = x__to_result__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_20'] = x__to_result__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_21'] = x__to_result__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_22'] = x__to_result__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_23'] = x__to_result__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_24'] = x__to_result__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_25'] = x__to_result__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_26'] = x__to_result__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_27'] = x__to_result__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_28'] = x__to_result__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_29'] = x__to_result__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_30'] = x__to_result__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_31'] = x__to_result__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_result__mutmut['x__to_result__mutmut_32'] = x__to_result__mutmut_32 # type: ignore # mutmut generated
