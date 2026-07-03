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
