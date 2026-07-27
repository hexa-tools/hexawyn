from __future__ import annotations

from hexawyn.application.ports.driven.log_search_port import RawPodLogData
from hexawyn.domain.models.constants import LogSearchConstants
from hexawyn.domain.models.log_search import (
    LogSearchRequest,
    LogSearchResult,
    PodLogMatch,
    SkippedNamespace,
    SkippedPod,
)
from hexawyn.domain.services.log_search.log_line_extraction import extract_matching_lines
from hexawyn.domain.services.log_search.pattern_matcher import compile_pattern
from hexawyn.domain.services.log_search.service_grouping import group_by_service

_cfg = LogSearchConstants()


def search_pod_logs(  # noqa: PLR0913
    request: LogSearchRequest,
    raw_pod_logs: list[RawPodLogData],
    skipped_pods: list[SkippedPod],
    skipped_namespaces: list[SkippedNamespace],
    scanned_namespaces: list[str],
    namespaces_total: int,
) -> LogSearchResult:
    """Composes pattern matching, per-container line extraction, and
    service grouping into one report. Pure domain function — raw_pod_logs is
    already fetched through LogSearchPort.
    """
    compiled_pattern = compile_pattern(request.pattern, request.is_regex)

    matches: list[PodLogMatch] = []
    for pod_data in raw_pod_logs:
        for container_log in pod_data["containers"]:
            matching_lines = extract_matching_lines(
                compiled_pattern,
                request.pattern,
                container_log["lines"],
                _cfg.max_lines_per_pod,
                _cfg.semantic_similarity_threshold,
            )
            if not matching_lines:
                continue
            matches.append(
                PodLogMatch(
                    pod_name=pod_data["pod_name"],
                    namespace=pod_data["namespace"],
                    container=container_log["container"],
                    matching_lines=matching_lines,
                )
            )

    groups = group_by_service(matches)
    pods_affected = len({(match.namespace, match.pod_name) for match in matches})
    services_affected = len({(group.namespace, group.service_name) for group in groups})
    no_matches = not matches

    return LogSearchResult(
        pattern=request.pattern,
        time_window_minutes=request.time_window_minutes,
        namespaces_total=namespaces_total,
        groups=groups,
        pods_affected=pods_affected,
        services_affected=services_affected,
        skipped_pods=skipped_pods,
        skipped_namespaces=skipped_namespaces,
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def _build_summary(
    request: LogSearchRequest, no_matches: bool, pods_affected: int, services_affected: int
) -> str:
    if no_matches:
        return (
            f"No pods found matching pattern '{request.pattern}' in the last "
            f"{request.time_window_minutes} minutes."
        )
    return (
        f"{pods_affected} pod(s) affected across {services_affected} service(s) "
        f"matching '{request.pattern}'."
    )
