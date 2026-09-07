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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_search_pod_logs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_search_pod_logs__mutmut)
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


def x_search_pod_logs__mutmut_orig(  # noqa: PLR0913
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


def x_search_pod_logs__mutmut_1(  # noqa: PLR0913
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
    compiled_pattern = None

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


def x_search_pod_logs__mutmut_2(  # noqa: PLR0913
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
    compiled_pattern = compile_pattern(None, request.is_regex)

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


def x_search_pod_logs__mutmut_3(  # noqa: PLR0913
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
    compiled_pattern = compile_pattern(request.pattern, None)

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


def x_search_pod_logs__mutmut_4(  # noqa: PLR0913
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
    compiled_pattern = compile_pattern(request.is_regex)

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


def x_search_pod_logs__mutmut_5(  # noqa: PLR0913
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
    compiled_pattern = compile_pattern(request.pattern, )

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


def x_search_pod_logs__mutmut_6(  # noqa: PLR0913
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

    matches: list[PodLogMatch] = None
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


def x_search_pod_logs__mutmut_7(  # noqa: PLR0913
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
        for container_log in pod_data["XXcontainersXX"]:
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


def x_search_pod_logs__mutmut_8(  # noqa: PLR0913
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
        for container_log in pod_data["CONTAINERS"]:
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


def x_search_pod_logs__mutmut_9(  # noqa: PLR0913
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
            matching_lines = None
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


def x_search_pod_logs__mutmut_10(  # noqa: PLR0913
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
                None,
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


def x_search_pod_logs__mutmut_11(  # noqa: PLR0913
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
                None,
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


def x_search_pod_logs__mutmut_12(  # noqa: PLR0913
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
                None,
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


def x_search_pod_logs__mutmut_13(  # noqa: PLR0913
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
                None,
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


def x_search_pod_logs__mutmut_14(  # noqa: PLR0913
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
                None,
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


def x_search_pod_logs__mutmut_15(  # noqa: PLR0913
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


def x_search_pod_logs__mutmut_16(  # noqa: PLR0913
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


def x_search_pod_logs__mutmut_17(  # noqa: PLR0913
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


def x_search_pod_logs__mutmut_18(  # noqa: PLR0913
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


def x_search_pod_logs__mutmut_19(  # noqa: PLR0913
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


def x_search_pod_logs__mutmut_20(  # noqa: PLR0913
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
                container_log["XXlinesXX"],
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


def x_search_pod_logs__mutmut_21(  # noqa: PLR0913
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
                container_log["LINES"],
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


def x_search_pod_logs__mutmut_22(  # noqa: PLR0913
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
            if matching_lines:
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


def x_search_pod_logs__mutmut_23(  # noqa: PLR0913
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
                break
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


def x_search_pod_logs__mutmut_24(  # noqa: PLR0913
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
                None
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


def x_search_pod_logs__mutmut_25(  # noqa: PLR0913
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
                    pod_name=None,
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


def x_search_pod_logs__mutmut_26(  # noqa: PLR0913
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
                    namespace=None,
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


def x_search_pod_logs__mutmut_27(  # noqa: PLR0913
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
                    container=None,
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


def x_search_pod_logs__mutmut_28(  # noqa: PLR0913
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
                    matching_lines=None,
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


def x_search_pod_logs__mutmut_29(  # noqa: PLR0913
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


def x_search_pod_logs__mutmut_30(  # noqa: PLR0913
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


def x_search_pod_logs__mutmut_31(  # noqa: PLR0913
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


def x_search_pod_logs__mutmut_32(  # noqa: PLR0913
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


def x_search_pod_logs__mutmut_33(  # noqa: PLR0913
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
                    pod_name=pod_data["XXpod_nameXX"],
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


def x_search_pod_logs__mutmut_34(  # noqa: PLR0913
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
                    pod_name=pod_data["POD_NAME"],
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


def x_search_pod_logs__mutmut_35(  # noqa: PLR0913
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
                    namespace=pod_data["XXnamespaceXX"],
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


def x_search_pod_logs__mutmut_36(  # noqa: PLR0913
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
                    namespace=pod_data["NAMESPACE"],
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


def x_search_pod_logs__mutmut_37(  # noqa: PLR0913
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
                    container=container_log["XXcontainerXX"],
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


def x_search_pod_logs__mutmut_38(  # noqa: PLR0913
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
                    container=container_log["CONTAINER"],
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


def x_search_pod_logs__mutmut_39(  # noqa: PLR0913
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

    groups = None
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


def x_search_pod_logs__mutmut_40(  # noqa: PLR0913
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

    groups = group_by_service(None)
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


def x_search_pod_logs__mutmut_41(  # noqa: PLR0913
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
    pods_affected = None
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


def x_search_pod_logs__mutmut_42(  # noqa: PLR0913
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
    services_affected = None
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


def x_search_pod_logs__mutmut_43(  # noqa: PLR0913
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
    no_matches = None

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


def x_search_pod_logs__mutmut_44(  # noqa: PLR0913
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
    no_matches = matches

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


def x_search_pod_logs__mutmut_45(  # noqa: PLR0913
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
        pattern=None,
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


def x_search_pod_logs__mutmut_46(  # noqa: PLR0913
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
        time_window_minutes=None,
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


def x_search_pod_logs__mutmut_47(  # noqa: PLR0913
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
        namespaces_total=None,
        groups=groups,
        pods_affected=pods_affected,
        services_affected=services_affected,
        skipped_pods=skipped_pods,
        skipped_namespaces=skipped_namespaces,
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_48(  # noqa: PLR0913
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
        groups=None,
        pods_affected=pods_affected,
        services_affected=services_affected,
        skipped_pods=skipped_pods,
        skipped_namespaces=skipped_namespaces,
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_49(  # noqa: PLR0913
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
        pods_affected=None,
        services_affected=services_affected,
        skipped_pods=skipped_pods,
        skipped_namespaces=skipped_namespaces,
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_50(  # noqa: PLR0913
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
        services_affected=None,
        skipped_pods=skipped_pods,
        skipped_namespaces=skipped_namespaces,
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_51(  # noqa: PLR0913
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
        skipped_pods=None,
        skipped_namespaces=skipped_namespaces,
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_52(  # noqa: PLR0913
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
        skipped_namespaces=None,
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_53(  # noqa: PLR0913
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
        scanned_namespaces=None,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_54(  # noqa: PLR0913
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
        no_matches=None,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_55(  # noqa: PLR0913
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
        summary=None,
    )


def x_search_pod_logs__mutmut_56(  # noqa: PLR0913
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


def x_search_pod_logs__mutmut_57(  # noqa: PLR0913
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


def x_search_pod_logs__mutmut_58(  # noqa: PLR0913
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
        groups=groups,
        pods_affected=pods_affected,
        services_affected=services_affected,
        skipped_pods=skipped_pods,
        skipped_namespaces=skipped_namespaces,
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_59(  # noqa: PLR0913
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
        pods_affected=pods_affected,
        services_affected=services_affected,
        skipped_pods=skipped_pods,
        skipped_namespaces=skipped_namespaces,
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_60(  # noqa: PLR0913
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
        services_affected=services_affected,
        skipped_pods=skipped_pods,
        skipped_namespaces=skipped_namespaces,
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_61(  # noqa: PLR0913
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
        skipped_pods=skipped_pods,
        skipped_namespaces=skipped_namespaces,
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_62(  # noqa: PLR0913
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
        skipped_namespaces=skipped_namespaces,
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_63(  # noqa: PLR0913
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
        scanned_namespaces=scanned_namespaces,
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_64(  # noqa: PLR0913
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
        no_matches=no_matches,
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_65(  # noqa: PLR0913
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
        summary=_build_summary(request, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_66(  # noqa: PLR0913
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
        )


def x_search_pod_logs__mutmut_67(  # noqa: PLR0913
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
        summary=_build_summary(None, no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_68(  # noqa: PLR0913
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
        summary=_build_summary(request, None, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_69(  # noqa: PLR0913
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
        summary=_build_summary(request, no_matches, None, services_affected),
    )


def x_search_pod_logs__mutmut_70(  # noqa: PLR0913
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
        summary=_build_summary(request, no_matches, pods_affected, None),
    )


def x_search_pod_logs__mutmut_71(  # noqa: PLR0913
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
        summary=_build_summary(no_matches, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_72(  # noqa: PLR0913
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
        summary=_build_summary(request, pods_affected, services_affected),
    )


def x_search_pod_logs__mutmut_73(  # noqa: PLR0913
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
        summary=_build_summary(request, no_matches, services_affected),
    )


def x_search_pod_logs__mutmut_74(  # noqa: PLR0913
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
        summary=_build_summary(request, no_matches, pods_affected, ),
    )

mutants_x_search_pod_logs__mutmut['_mutmut_orig'] = x_search_pod_logs__mutmut_orig # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_1'] = x_search_pod_logs__mutmut_1 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_2'] = x_search_pod_logs__mutmut_2 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_3'] = x_search_pod_logs__mutmut_3 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_4'] = x_search_pod_logs__mutmut_4 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_5'] = x_search_pod_logs__mutmut_5 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_6'] = x_search_pod_logs__mutmut_6 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_7'] = x_search_pod_logs__mutmut_7 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_8'] = x_search_pod_logs__mutmut_8 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_9'] = x_search_pod_logs__mutmut_9 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_10'] = x_search_pod_logs__mutmut_10 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_11'] = x_search_pod_logs__mutmut_11 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_12'] = x_search_pod_logs__mutmut_12 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_13'] = x_search_pod_logs__mutmut_13 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_14'] = x_search_pod_logs__mutmut_14 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_15'] = x_search_pod_logs__mutmut_15 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_16'] = x_search_pod_logs__mutmut_16 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_17'] = x_search_pod_logs__mutmut_17 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_18'] = x_search_pod_logs__mutmut_18 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_19'] = x_search_pod_logs__mutmut_19 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_20'] = x_search_pod_logs__mutmut_20 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_21'] = x_search_pod_logs__mutmut_21 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_22'] = x_search_pod_logs__mutmut_22 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_23'] = x_search_pod_logs__mutmut_23 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_24'] = x_search_pod_logs__mutmut_24 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_25'] = x_search_pod_logs__mutmut_25 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_26'] = x_search_pod_logs__mutmut_26 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_27'] = x_search_pod_logs__mutmut_27 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_28'] = x_search_pod_logs__mutmut_28 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_29'] = x_search_pod_logs__mutmut_29 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_30'] = x_search_pod_logs__mutmut_30 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_31'] = x_search_pod_logs__mutmut_31 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_32'] = x_search_pod_logs__mutmut_32 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_33'] = x_search_pod_logs__mutmut_33 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_34'] = x_search_pod_logs__mutmut_34 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_35'] = x_search_pod_logs__mutmut_35 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_36'] = x_search_pod_logs__mutmut_36 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_37'] = x_search_pod_logs__mutmut_37 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_38'] = x_search_pod_logs__mutmut_38 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_39'] = x_search_pod_logs__mutmut_39 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_40'] = x_search_pod_logs__mutmut_40 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_41'] = x_search_pod_logs__mutmut_41 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_42'] = x_search_pod_logs__mutmut_42 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_43'] = x_search_pod_logs__mutmut_43 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_44'] = x_search_pod_logs__mutmut_44 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_45'] = x_search_pod_logs__mutmut_45 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_46'] = x_search_pod_logs__mutmut_46 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_47'] = x_search_pod_logs__mutmut_47 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_48'] = x_search_pod_logs__mutmut_48 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_49'] = x_search_pod_logs__mutmut_49 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_50'] = x_search_pod_logs__mutmut_50 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_51'] = x_search_pod_logs__mutmut_51 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_52'] = x_search_pod_logs__mutmut_52 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_53'] = x_search_pod_logs__mutmut_53 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_54'] = x_search_pod_logs__mutmut_54 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_55'] = x_search_pod_logs__mutmut_55 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_56'] = x_search_pod_logs__mutmut_56 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_57'] = x_search_pod_logs__mutmut_57 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_58'] = x_search_pod_logs__mutmut_58 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_59'] = x_search_pod_logs__mutmut_59 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_60'] = x_search_pod_logs__mutmut_60 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_61'] = x_search_pod_logs__mutmut_61 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_62'] = x_search_pod_logs__mutmut_62 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_63'] = x_search_pod_logs__mutmut_63 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_64'] = x_search_pod_logs__mutmut_64 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_65'] = x_search_pod_logs__mutmut_65 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_66'] = x_search_pod_logs__mutmut_66 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_67'] = x_search_pod_logs__mutmut_67 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_68'] = x_search_pod_logs__mutmut_68 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_69'] = x_search_pod_logs__mutmut_69 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_70'] = x_search_pod_logs__mutmut_70 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_71'] = x_search_pod_logs__mutmut_71 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_72'] = x_search_pod_logs__mutmut_72 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_73'] = x_search_pod_logs__mutmut_73 # type: ignore # mutmut generated
mutants_x_search_pod_logs__mutmut['x_search_pod_logs__mutmut_74'] = x_search_pod_logs__mutmut_74 # type: ignore # mutmut generated


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
