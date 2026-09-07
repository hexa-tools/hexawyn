from __future__ import annotations

from datetime import datetime, timedelta

from hexawyn.application.ports.driven.cross_cluster_incident_port import (
    ClusterFailureSignature,
)
from hexawyn.domain.models.cross_cluster_correlation import (
    AffectedCluster,
    CrossClusterCorrelationReport,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_correlate__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_correlate__mutmut)
def correlate(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_orig(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_1(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_2(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope=None, has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_3(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=None, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_4(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning=None
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_5(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_6(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_7(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_8(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="XXnoneXX", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_9(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="NONE", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_10(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=True, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_11(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="XXAucune signature de panne remontee.XX"
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_12(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_13(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="AUCUNE SIGNATURE DE PANNE REMONTEE."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_14(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = None
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_15(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(None)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_16(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if grouped:  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_17(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope=None)

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_18(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="XXnoneXX")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_19(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="NONE")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_20(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = None

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_21(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(None, key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_22(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=None)

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_23(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_24(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), )

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_25(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: None)

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_26(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) <= 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_27(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 3:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_28(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope=None)

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_29(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="XXisolatedXX")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_30(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="ISOLATED")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_31(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = None
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_32(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(None, key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_33(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=None)
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_34(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_35(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], )
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_36(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[2], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_37(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: None)
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_38(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["XXonset_utcXX"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_39(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["ONSET_UTC"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_40(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = None
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_41(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(None, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_42(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, None)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_43(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_44(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, )
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_45(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = None  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_46(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 or _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_47(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) > 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_48(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 3 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_49(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(None) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_50(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) >= 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_51(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 1  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_52(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = None
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_53(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(None, len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_54(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), None)
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_55(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_56(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), )
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_57(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = None

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_58(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(None)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_59(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=None,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_60(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=None,
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_61(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=None,
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_62(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=None,
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_63(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=None,
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_64(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=None,
        has_data=True,
    )


def x_correlate__mutmut_65(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=None,
    )


def x_correlate__mutmut_66(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_67(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_68(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_69(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_70(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_71(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        has_data=True,
    )


def x_correlate__mutmut_72(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        )


def x_correlate__mutmut_73(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=None,
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_74(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=None,
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_75(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=None,
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_76(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=None,
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_77(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_78(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_79(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_80(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_81(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["XXcluster_nameXX"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_82(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["CLUSTER_NAME"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_83(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["XXonset_utcXX"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_84(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["ONSET_UTC"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_85(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["XXpod_countXX"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_86(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["POD_COUNT"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_87(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["XXfailure_typeXX"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_88(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["FAILURE_TYPE"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_89(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[1],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_90(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor and "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_91(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "XXXX",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_92(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(None, scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_93(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, None, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_94(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, None),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_95(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_96(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, common_factor),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_97(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, ),
        cascading=cascading,
        has_data=True,
    )


def x_correlate__mutmut_98(
    failures: list[ClusterFailureSignature], window_minutes: int
) -> CrossClusterCorrelationReport:
    if not failures:
        return CrossClusterCorrelationReport(
            scope="none", has_data=False, warning="Aucune signature de panne remontee."
        )

    grouped = _group_by_failure_type(failures)
    if (
        not grouped
    ):  # pragma: no cover — unreachable: non-empty failures always produce a grouped dict
        return CrossClusterCorrelationReport(scope="none")

    largest = max(grouped.items(), key=lambda item: len(item[1]))

    if len(largest[1]) < 2:  # noqa: PLR2004
        return CrossClusterCorrelationReport(scope="isolated")

    clusters = sorted(largest[1], key=lambda sig: sig["onset_utc"])
    in_window = _filter_within_window(clusters, window_minutes)
    cascading = len(in_window) >= 2 and _onset_gap_seconds(in_window) > 0  # noqa: PLR2004
    scope = _classify_scope(len(in_window), len(failures))
    common_factor = _extract_common_factor(in_window)

    return CrossClusterCorrelationReport(
        scope=scope,
        affected_clusters=[
            AffectedCluster(
                cluster_name=sig["cluster_name"],
                onset_utc=sig["onset_utc"],
                pod_count=sig["pod_count"],
                failure_type=sig["failure_type"],
            )
            for sig in in_window
        ],
        common_failure_type=largest[0],
        common_factor=common_factor or "",
        suggestion=_suggestion(scope, scope, common_factor),
        cascading=cascading,
        has_data=False,
    )

mutants_x_correlate__mutmut['_mutmut_orig'] = x_correlate__mutmut_orig # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_1'] = x_correlate__mutmut_1 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_2'] = x_correlate__mutmut_2 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_3'] = x_correlate__mutmut_3 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_4'] = x_correlate__mutmut_4 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_5'] = x_correlate__mutmut_5 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_6'] = x_correlate__mutmut_6 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_7'] = x_correlate__mutmut_7 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_8'] = x_correlate__mutmut_8 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_9'] = x_correlate__mutmut_9 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_10'] = x_correlate__mutmut_10 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_11'] = x_correlate__mutmut_11 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_12'] = x_correlate__mutmut_12 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_13'] = x_correlate__mutmut_13 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_14'] = x_correlate__mutmut_14 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_15'] = x_correlate__mutmut_15 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_16'] = x_correlate__mutmut_16 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_17'] = x_correlate__mutmut_17 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_18'] = x_correlate__mutmut_18 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_19'] = x_correlate__mutmut_19 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_20'] = x_correlate__mutmut_20 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_21'] = x_correlate__mutmut_21 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_22'] = x_correlate__mutmut_22 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_23'] = x_correlate__mutmut_23 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_24'] = x_correlate__mutmut_24 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_25'] = x_correlate__mutmut_25 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_26'] = x_correlate__mutmut_26 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_27'] = x_correlate__mutmut_27 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_28'] = x_correlate__mutmut_28 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_29'] = x_correlate__mutmut_29 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_30'] = x_correlate__mutmut_30 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_31'] = x_correlate__mutmut_31 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_32'] = x_correlate__mutmut_32 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_33'] = x_correlate__mutmut_33 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_34'] = x_correlate__mutmut_34 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_35'] = x_correlate__mutmut_35 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_36'] = x_correlate__mutmut_36 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_37'] = x_correlate__mutmut_37 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_38'] = x_correlate__mutmut_38 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_39'] = x_correlate__mutmut_39 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_40'] = x_correlate__mutmut_40 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_41'] = x_correlate__mutmut_41 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_42'] = x_correlate__mutmut_42 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_43'] = x_correlate__mutmut_43 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_44'] = x_correlate__mutmut_44 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_45'] = x_correlate__mutmut_45 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_46'] = x_correlate__mutmut_46 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_47'] = x_correlate__mutmut_47 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_48'] = x_correlate__mutmut_48 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_49'] = x_correlate__mutmut_49 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_50'] = x_correlate__mutmut_50 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_51'] = x_correlate__mutmut_51 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_52'] = x_correlate__mutmut_52 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_53'] = x_correlate__mutmut_53 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_54'] = x_correlate__mutmut_54 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_55'] = x_correlate__mutmut_55 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_56'] = x_correlate__mutmut_56 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_57'] = x_correlate__mutmut_57 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_58'] = x_correlate__mutmut_58 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_59'] = x_correlate__mutmut_59 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_60'] = x_correlate__mutmut_60 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_61'] = x_correlate__mutmut_61 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_62'] = x_correlate__mutmut_62 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_63'] = x_correlate__mutmut_63 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_64'] = x_correlate__mutmut_64 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_65'] = x_correlate__mutmut_65 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_66'] = x_correlate__mutmut_66 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_67'] = x_correlate__mutmut_67 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_68'] = x_correlate__mutmut_68 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_69'] = x_correlate__mutmut_69 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_70'] = x_correlate__mutmut_70 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_71'] = x_correlate__mutmut_71 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_72'] = x_correlate__mutmut_72 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_73'] = x_correlate__mutmut_73 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_74'] = x_correlate__mutmut_74 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_75'] = x_correlate__mutmut_75 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_76'] = x_correlate__mutmut_76 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_77'] = x_correlate__mutmut_77 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_78'] = x_correlate__mutmut_78 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_79'] = x_correlate__mutmut_79 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_80'] = x_correlate__mutmut_80 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_81'] = x_correlate__mutmut_81 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_82'] = x_correlate__mutmut_82 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_83'] = x_correlate__mutmut_83 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_84'] = x_correlate__mutmut_84 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_85'] = x_correlate__mutmut_85 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_86'] = x_correlate__mutmut_86 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_87'] = x_correlate__mutmut_87 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_88'] = x_correlate__mutmut_88 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_89'] = x_correlate__mutmut_89 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_90'] = x_correlate__mutmut_90 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_91'] = x_correlate__mutmut_91 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_92'] = x_correlate__mutmut_92 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_93'] = x_correlate__mutmut_93 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_94'] = x_correlate__mutmut_94 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_95'] = x_correlate__mutmut_95 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_96'] = x_correlate__mutmut_96 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_97'] = x_correlate__mutmut_97 # type: ignore # mutmut generated
mutants_x_correlate__mutmut['x_correlate__mutmut_98'] = x_correlate__mutmut_98 # type: ignore # mutmut generated
mutants_x__group_by_failure_type__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__group_by_failure_type__mutmut)
def _group_by_failure_type(
    failures: list[ClusterFailureSignature],
) -> dict[str, list[ClusterFailureSignature]]:
    grouped: dict[str, list[ClusterFailureSignature]] = {}
    for sig in failures:
        grouped.setdefault(sig["failure_type"], []).append(sig)
    return grouped


def x__group_by_failure_type__mutmut_orig(
    failures: list[ClusterFailureSignature],
) -> dict[str, list[ClusterFailureSignature]]:
    grouped: dict[str, list[ClusterFailureSignature]] = {}
    for sig in failures:
        grouped.setdefault(sig["failure_type"], []).append(sig)
    return grouped


def x__group_by_failure_type__mutmut_1(
    failures: list[ClusterFailureSignature],
) -> dict[str, list[ClusterFailureSignature]]:
    grouped: dict[str, list[ClusterFailureSignature]] = None
    for sig in failures:
        grouped.setdefault(sig["failure_type"], []).append(sig)
    return grouped


def x__group_by_failure_type__mutmut_2(
    failures: list[ClusterFailureSignature],
) -> dict[str, list[ClusterFailureSignature]]:
    grouped: dict[str, list[ClusterFailureSignature]] = {}
    for sig in failures:
        grouped.setdefault(sig["failure_type"], []).append(None)
    return grouped


def x__group_by_failure_type__mutmut_3(
    failures: list[ClusterFailureSignature],
) -> dict[str, list[ClusterFailureSignature]]:
    grouped: dict[str, list[ClusterFailureSignature]] = {}
    for sig in failures:
        grouped.setdefault(None, []).append(sig)
    return grouped


def x__group_by_failure_type__mutmut_4(
    failures: list[ClusterFailureSignature],
) -> dict[str, list[ClusterFailureSignature]]:
    grouped: dict[str, list[ClusterFailureSignature]] = {}
    for sig in failures:
        grouped.setdefault(sig["failure_type"], None).append(sig)
    return grouped


def x__group_by_failure_type__mutmut_5(
    failures: list[ClusterFailureSignature],
) -> dict[str, list[ClusterFailureSignature]]:
    grouped: dict[str, list[ClusterFailureSignature]] = {}
    for sig in failures:
        grouped.setdefault([]).append(sig)
    return grouped


def x__group_by_failure_type__mutmut_6(
    failures: list[ClusterFailureSignature],
) -> dict[str, list[ClusterFailureSignature]]:
    grouped: dict[str, list[ClusterFailureSignature]] = {}
    for sig in failures:
        grouped.setdefault(sig["failure_type"], ).append(sig)
    return grouped


def x__group_by_failure_type__mutmut_7(
    failures: list[ClusterFailureSignature],
) -> dict[str, list[ClusterFailureSignature]]:
    grouped: dict[str, list[ClusterFailureSignature]] = {}
    for sig in failures:
        grouped.setdefault(sig["XXfailure_typeXX"], []).append(sig)
    return grouped


def x__group_by_failure_type__mutmut_8(
    failures: list[ClusterFailureSignature],
) -> dict[str, list[ClusterFailureSignature]]:
    grouped: dict[str, list[ClusterFailureSignature]] = {}
    for sig in failures:
        grouped.setdefault(sig["FAILURE_TYPE"], []).append(sig)
    return grouped

mutants_x__group_by_failure_type__mutmut['_mutmut_orig'] = x__group_by_failure_type__mutmut_orig # type: ignore # mutmut generated
mutants_x__group_by_failure_type__mutmut['x__group_by_failure_type__mutmut_1'] = x__group_by_failure_type__mutmut_1 # type: ignore # mutmut generated
mutants_x__group_by_failure_type__mutmut['x__group_by_failure_type__mutmut_2'] = x__group_by_failure_type__mutmut_2 # type: ignore # mutmut generated
mutants_x__group_by_failure_type__mutmut['x__group_by_failure_type__mutmut_3'] = x__group_by_failure_type__mutmut_3 # type: ignore # mutmut generated
mutants_x__group_by_failure_type__mutmut['x__group_by_failure_type__mutmut_4'] = x__group_by_failure_type__mutmut_4 # type: ignore # mutmut generated
mutants_x__group_by_failure_type__mutmut['x__group_by_failure_type__mutmut_5'] = x__group_by_failure_type__mutmut_5 # type: ignore # mutmut generated
mutants_x__group_by_failure_type__mutmut['x__group_by_failure_type__mutmut_6'] = x__group_by_failure_type__mutmut_6 # type: ignore # mutmut generated
mutants_x__group_by_failure_type__mutmut['x__group_by_failure_type__mutmut_7'] = x__group_by_failure_type__mutmut_7 # type: ignore # mutmut generated
mutants_x__group_by_failure_type__mutmut['x__group_by_failure_type__mutmut_8'] = x__group_by_failure_type__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_utc__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_utc__mutmut)
def _parse_utc(onset: str) -> datetime:
    return datetime.fromisoformat(onset.replace("Z", "+00:00"))


def x__parse_utc__mutmut_orig(onset: str) -> datetime:
    return datetime.fromisoformat(onset.replace("Z", "+00:00"))


def x__parse_utc__mutmut_1(onset: str) -> datetime:
    return datetime.fromisoformat(None)


def x__parse_utc__mutmut_2(onset: str) -> datetime:
    return datetime.fromisoformat(onset.replace(None, "+00:00"))


def x__parse_utc__mutmut_3(onset: str) -> datetime:
    return datetime.fromisoformat(onset.replace("Z", None))


def x__parse_utc__mutmut_4(onset: str) -> datetime:
    return datetime.fromisoformat(onset.replace("+00:00"))


def x__parse_utc__mutmut_5(onset: str) -> datetime:
    return datetime.fromisoformat(onset.replace("Z", ))


def x__parse_utc__mutmut_6(onset: str) -> datetime:
    return datetime.fromisoformat(onset.replace("XXZXX", "+00:00"))


def x__parse_utc__mutmut_7(onset: str) -> datetime:
    return datetime.fromisoformat(onset.replace("z", "+00:00"))


def x__parse_utc__mutmut_8(onset: str) -> datetime:
    return datetime.fromisoformat(onset.replace("Z", "XX+00:00XX"))

mutants_x__parse_utc__mutmut['_mutmut_orig'] = x__parse_utc__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_utc__mutmut['x__parse_utc__mutmut_1'] = x__parse_utc__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_utc__mutmut['x__parse_utc__mutmut_2'] = x__parse_utc__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_utc__mutmut['x__parse_utc__mutmut_3'] = x__parse_utc__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_utc__mutmut['x__parse_utc__mutmut_4'] = x__parse_utc__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_utc__mutmut['x__parse_utc__mutmut_5'] = x__parse_utc__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_utc__mutmut['x__parse_utc__mutmut_6'] = x__parse_utc__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_utc__mutmut['x__parse_utc__mutmut_7'] = x__parse_utc__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_utc__mutmut['x__parse_utc__mutmut_8'] = x__parse_utc__mutmut_8 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__filter_within_window__mutmut)
def _filter_within_window(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["onset_utc"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_orig(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["onset_utc"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_1(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) <= 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["onset_utc"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_2(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 3  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["onset_utc"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_3(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = None
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_4(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(None)
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_5(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[1]["onset_utc"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_6(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["XXonset_utcXX"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_7(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["ONSET_UTC"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_8(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["onset_utc"])
    window = None
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_9(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["onset_utc"])
    window = _timedelta(minutes=None)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_10(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["onset_utc"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) + start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_11(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["onset_utc"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(None) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_12(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["onset_utc"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["XXonset_utcXX"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_13(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["onset_utc"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["ONSET_UTC"]) - start).total_seconds() <= window.total_seconds()
    ]


def x__filter_within_window__mutmut_14(
    clusters: list[ClusterFailureSignature], window_minutes: int
) -> list[ClusterFailureSignature]:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with ≥2 after line 28 check  # noqa: E501, PLR2004
        return clusters
    start = _parse_utc(clusters[0]["onset_utc"])
    window = _timedelta(minutes=window_minutes)
    return [
        sig
        for sig in clusters
        if (_parse_utc(sig["onset_utc"]) - start).total_seconds() < window.total_seconds()
    ]

mutants_x__filter_within_window__mutmut['_mutmut_orig'] = x__filter_within_window__mutmut_orig # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_1'] = x__filter_within_window__mutmut_1 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_2'] = x__filter_within_window__mutmut_2 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_3'] = x__filter_within_window__mutmut_3 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_4'] = x__filter_within_window__mutmut_4 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_5'] = x__filter_within_window__mutmut_5 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_6'] = x__filter_within_window__mutmut_6 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_7'] = x__filter_within_window__mutmut_7 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_8'] = x__filter_within_window__mutmut_8 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_9'] = x__filter_within_window__mutmut_9 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_10'] = x__filter_within_window__mutmut_10 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_11'] = x__filter_within_window__mutmut_11 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_12'] = x__filter_within_window__mutmut_12 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_13'] = x__filter_within_window__mutmut_13 # type: ignore # mutmut generated
mutants_x__filter_within_window__mutmut['x__filter_within_window__mutmut_14'] = x__filter_within_window__mutmut_14 # type: ignore # mutmut generated
mutants_x__timedelta__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__timedelta__mutmut)
def _timedelta(minutes: int):  # type: ignore[no-untyped-def]  # returns timedelta
    return timedelta(minutes=minutes)


def x__timedelta__mutmut_orig(minutes: int):  # type: ignore[no-untyped-def]  # returns timedelta
    return timedelta(minutes=minutes)


def x__timedelta__mutmut_1(minutes: int):  # type: ignore[no-untyped-def]  # returns timedelta
    return timedelta(minutes=None)

mutants_x__timedelta__mutmut['_mutmut_orig'] = x__timedelta__mutmut_orig # type: ignore # mutmut generated
mutants_x__timedelta__mutmut['x__timedelta__mutmut_1'] = x__timedelta__mutmut_1 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__onset_gap_seconds__mutmut)
def _onset_gap_seconds(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_orig(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_1(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) <= 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_2(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 3  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_3(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 1
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_4(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = None
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_5(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(None)
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_6(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[1]["onset_utc"])
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_7(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["XXonset_utcXX"])
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_8(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["ONSET_UTC"])
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_9(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = None
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_10(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(None)
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_11(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(clusters[+1]["onset_utc"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_12(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(clusters[-2]["onset_utc"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_13(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(clusters[-1]["XXonset_utcXX"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_14(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(clusters[-1]["ONSET_UTC"])
    return int((last - first).total_seconds())


def x__onset_gap_seconds__mutmut_15(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int(None)


def x__onset_gap_seconds__mutmut_16(clusters: list[ClusterFailureSignature]) -> int:
    if (
        len(clusters) < 2  # noqa: PLR2004
    ):  # pragma: no cover — always called with cascading=True precondition  # noqa: E501, PLR2004
        return 0
    first = _parse_utc(clusters[0]["onset_utc"])
    last = _parse_utc(clusters[-1]["onset_utc"])
    return int((last + first).total_seconds())

mutants_x__onset_gap_seconds__mutmut['_mutmut_orig'] = x__onset_gap_seconds__mutmut_orig # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_1'] = x__onset_gap_seconds__mutmut_1 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_2'] = x__onset_gap_seconds__mutmut_2 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_3'] = x__onset_gap_seconds__mutmut_3 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_4'] = x__onset_gap_seconds__mutmut_4 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_5'] = x__onset_gap_seconds__mutmut_5 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_6'] = x__onset_gap_seconds__mutmut_6 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_7'] = x__onset_gap_seconds__mutmut_7 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_8'] = x__onset_gap_seconds__mutmut_8 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_9'] = x__onset_gap_seconds__mutmut_9 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_10'] = x__onset_gap_seconds__mutmut_10 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_11'] = x__onset_gap_seconds__mutmut_11 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_12'] = x__onset_gap_seconds__mutmut_12 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_13'] = x__onset_gap_seconds__mutmut_13 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_14'] = x__onset_gap_seconds__mutmut_14 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_15'] = x__onset_gap_seconds__mutmut_15 # type: ignore # mutmut generated
mutants_x__onset_gap_seconds__mutmut['x__onset_gap_seconds__mutmut_16'] = x__onset_gap_seconds__mutmut_16 # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__classify_scope__mutmut)
def _classify_scope(in_window: int, total: int) -> str:
    if in_window >= total and in_window >= 3:  # noqa: PLR2004
        return "global"
    if in_window >= 2:  # noqa: PLR2004
        return "regional"
    return "isolated"


def x__classify_scope__mutmut_orig(in_window: int, total: int) -> str:
    if in_window >= total and in_window >= 3:  # noqa: PLR2004
        return "global"
    if in_window >= 2:  # noqa: PLR2004
        return "regional"
    return "isolated"


def x__classify_scope__mutmut_1(in_window: int, total: int) -> str:
    if in_window >= total or in_window >= 3:  # noqa: PLR2004
        return "global"
    if in_window >= 2:  # noqa: PLR2004
        return "regional"
    return "isolated"


def x__classify_scope__mutmut_2(in_window: int, total: int) -> str:
    if in_window > total and in_window >= 3:  # noqa: PLR2004
        return "global"
    if in_window >= 2:  # noqa: PLR2004
        return "regional"
    return "isolated"


def x__classify_scope__mutmut_3(in_window: int, total: int) -> str:
    if in_window >= total and in_window > 3:  # noqa: PLR2004
        return "global"
    if in_window >= 2:  # noqa: PLR2004
        return "regional"
    return "isolated"


def x__classify_scope__mutmut_4(in_window: int, total: int) -> str:
    if in_window >= total and in_window >= 4:  # noqa: PLR2004
        return "global"
    if in_window >= 2:  # noqa: PLR2004
        return "regional"
    return "isolated"


def x__classify_scope__mutmut_5(in_window: int, total: int) -> str:
    if in_window >= total and in_window >= 3:  # noqa: PLR2004
        return "XXglobalXX"
    if in_window >= 2:  # noqa: PLR2004
        return "regional"
    return "isolated"


def x__classify_scope__mutmut_6(in_window: int, total: int) -> str:
    if in_window >= total and in_window >= 3:  # noqa: PLR2004
        return "GLOBAL"
    if in_window >= 2:  # noqa: PLR2004
        return "regional"
    return "isolated"


def x__classify_scope__mutmut_7(in_window: int, total: int) -> str:
    if in_window >= total and in_window >= 3:  # noqa: PLR2004
        return "global"
    if in_window > 2:  # noqa: PLR2004
        return "regional"
    return "isolated"


def x__classify_scope__mutmut_8(in_window: int, total: int) -> str:
    if in_window >= total and in_window >= 3:  # noqa: PLR2004
        return "global"
    if in_window >= 3:  # noqa: PLR2004
        return "regional"
    return "isolated"


def x__classify_scope__mutmut_9(in_window: int, total: int) -> str:
    if in_window >= total and in_window >= 3:  # noqa: PLR2004
        return "global"
    if in_window >= 2:  # noqa: PLR2004
        return "XXregionalXX"
    return "isolated"


def x__classify_scope__mutmut_10(in_window: int, total: int) -> str:
    if in_window >= total and in_window >= 3:  # noqa: PLR2004
        return "global"
    if in_window >= 2:  # noqa: PLR2004
        return "REGIONAL"
    return "isolated"


def x__classify_scope__mutmut_11(in_window: int, total: int) -> str:
    if in_window >= total and in_window >= 3:  # noqa: PLR2004
        return "global"
    if in_window >= 2:  # noqa: PLR2004
        return "regional"
    return "XXisolatedXX"


def x__classify_scope__mutmut_12(in_window: int, total: int) -> str:
    if in_window >= total and in_window >= 3:  # noqa: PLR2004
        return "global"
    if in_window >= 2:  # noqa: PLR2004
        return "regional"
    return "ISOLATED"

mutants_x__classify_scope__mutmut['_mutmut_orig'] = x__classify_scope__mutmut_orig # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut['x__classify_scope__mutmut_1'] = x__classify_scope__mutmut_1 # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut['x__classify_scope__mutmut_2'] = x__classify_scope__mutmut_2 # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut['x__classify_scope__mutmut_3'] = x__classify_scope__mutmut_3 # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut['x__classify_scope__mutmut_4'] = x__classify_scope__mutmut_4 # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut['x__classify_scope__mutmut_5'] = x__classify_scope__mutmut_5 # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut['x__classify_scope__mutmut_6'] = x__classify_scope__mutmut_6 # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut['x__classify_scope__mutmut_7'] = x__classify_scope__mutmut_7 # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut['x__classify_scope__mutmut_8'] = x__classify_scope__mutmut_8 # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut['x__classify_scope__mutmut_9'] = x__classify_scope__mutmut_9 # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut['x__classify_scope__mutmut_10'] = x__classify_scope__mutmut_10 # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut['x__classify_scope__mutmut_11'] = x__classify_scope__mutmut_11 # type: ignore # mutmut generated
mutants_x__classify_scope__mutmut['x__classify_scope__mutmut_12'] = x__classify_scope__mutmut_12 # type: ignore # mutmut generated
mutants_x__extract_common_factor__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_common_factor__mutmut)
def _extract_common_factor(signatures: list[ClusterFailureSignature]) -> str | None:
    deps = {sig["shared_dependency"] for sig in signatures if sig["shared_dependency"]}
    return deps.pop() if len(deps) == 1 else None


def x__extract_common_factor__mutmut_orig(signatures: list[ClusterFailureSignature]) -> str | None:
    deps = {sig["shared_dependency"] for sig in signatures if sig["shared_dependency"]}
    return deps.pop() if len(deps) == 1 else None


def x__extract_common_factor__mutmut_1(signatures: list[ClusterFailureSignature]) -> str | None:
    deps = None
    return deps.pop() if len(deps) == 1 else None


def x__extract_common_factor__mutmut_2(signatures: list[ClusterFailureSignature]) -> str | None:
    deps = {sig["XXshared_dependencyXX"] for sig in signatures if sig["shared_dependency"]}
    return deps.pop() if len(deps) == 1 else None


def x__extract_common_factor__mutmut_3(signatures: list[ClusterFailureSignature]) -> str | None:
    deps = {sig["SHARED_DEPENDENCY"] for sig in signatures if sig["shared_dependency"]}
    return deps.pop() if len(deps) == 1 else None


def x__extract_common_factor__mutmut_4(signatures: list[ClusterFailureSignature]) -> str | None:
    deps = {sig["shared_dependency"] for sig in signatures if sig["XXshared_dependencyXX"]}
    return deps.pop() if len(deps) == 1 else None


def x__extract_common_factor__mutmut_5(signatures: list[ClusterFailureSignature]) -> str | None:
    deps = {sig["shared_dependency"] for sig in signatures if sig["SHARED_DEPENDENCY"]}
    return deps.pop() if len(deps) == 1 else None


def x__extract_common_factor__mutmut_6(signatures: list[ClusterFailureSignature]) -> str | None:
    deps = {sig["shared_dependency"] for sig in signatures if sig["shared_dependency"]}
    return deps.pop() if len(deps) != 1 else None


def x__extract_common_factor__mutmut_7(signatures: list[ClusterFailureSignature]) -> str | None:
    deps = {sig["shared_dependency"] for sig in signatures if sig["shared_dependency"]}
    return deps.pop() if len(deps) == 2 else None

mutants_x__extract_common_factor__mutmut['_mutmut_orig'] = x__extract_common_factor__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_common_factor__mutmut['x__extract_common_factor__mutmut_1'] = x__extract_common_factor__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_common_factor__mutmut['x__extract_common_factor__mutmut_2'] = x__extract_common_factor__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_common_factor__mutmut['x__extract_common_factor__mutmut_3'] = x__extract_common_factor__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_common_factor__mutmut['x__extract_common_factor__mutmut_4'] = x__extract_common_factor__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_common_factor__mutmut['x__extract_common_factor__mutmut_5'] = x__extract_common_factor__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_common_factor__mutmut['x__extract_common_factor__mutmut_6'] = x__extract_common_factor__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_common_factor__mutmut['x__extract_common_factor__mutmut_7'] = x__extract_common_factor__mutmut_7 # type: ignore # mutmut generated
mutants_x__suggestion__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__suggestion__mutmut)
def _suggestion(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "ghcr" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "global":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "regional":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case


def x__suggestion__mutmut_orig(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "ghcr" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "global":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "regional":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case


def x__suggestion__mutmut_1(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor or "ghcr" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "global":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "regional":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case


def x__suggestion__mutmut_2(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "XXghcrXX" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "global":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "regional":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case


def x__suggestion__mutmut_3(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "GHCR" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "global":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "regional":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case


def x__suggestion__mutmut_4(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "ghcr" not in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "global":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "regional":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case


def x__suggestion__mutmut_5(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "ghcr" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope != "global":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "regional":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case


def x__suggestion__mutmut_6(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "ghcr" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "XXglobalXX":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "regional":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case


def x__suggestion__mutmut_7(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "ghcr" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "GLOBAL":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "regional":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case


def x__suggestion__mutmut_8(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "ghcr" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "global":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope != "regional":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case


def x__suggestion__mutmut_9(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "ghcr" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "global":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "XXregionalXX":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case


def x__suggestion__mutmut_10(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "ghcr" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "global":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "REGIONAL":
        return f"Regional {failure_type} detected — investigate regional infra"
    return ""  # pragma: no cover — all branches above cover every reachable case


def x__suggestion__mutmut_11(scope: str, failure_type: str, common_factor: str | None) -> str:
    if common_factor and "ghcr" in common_factor:
        return f"Check {common_factor} registry availability and rate limits"
    if scope == "global":
        return f"Global {failure_type} detected — investigate shared infrastructure"
    if scope == "regional":
        return f"Regional {failure_type} detected — investigate regional infra"
    return "XXXX"  # pragma: no cover — all branches above cover every reachable case

mutants_x__suggestion__mutmut['_mutmut_orig'] = x__suggestion__mutmut_orig # type: ignore # mutmut generated
mutants_x__suggestion__mutmut['x__suggestion__mutmut_1'] = x__suggestion__mutmut_1 # type: ignore # mutmut generated
mutants_x__suggestion__mutmut['x__suggestion__mutmut_2'] = x__suggestion__mutmut_2 # type: ignore # mutmut generated
mutants_x__suggestion__mutmut['x__suggestion__mutmut_3'] = x__suggestion__mutmut_3 # type: ignore # mutmut generated
mutants_x__suggestion__mutmut['x__suggestion__mutmut_4'] = x__suggestion__mutmut_4 # type: ignore # mutmut generated
mutants_x__suggestion__mutmut['x__suggestion__mutmut_5'] = x__suggestion__mutmut_5 # type: ignore # mutmut generated
mutants_x__suggestion__mutmut['x__suggestion__mutmut_6'] = x__suggestion__mutmut_6 # type: ignore # mutmut generated
mutants_x__suggestion__mutmut['x__suggestion__mutmut_7'] = x__suggestion__mutmut_7 # type: ignore # mutmut generated
mutants_x__suggestion__mutmut['x__suggestion__mutmut_8'] = x__suggestion__mutmut_8 # type: ignore # mutmut generated
mutants_x__suggestion__mutmut['x__suggestion__mutmut_9'] = x__suggestion__mutmut_9 # type: ignore # mutmut generated
mutants_x__suggestion__mutmut['x__suggestion__mutmut_10'] = x__suggestion__mutmut_10 # type: ignore # mutmut generated
mutants_x__suggestion__mutmut['x__suggestion__mutmut_11'] = x__suggestion__mutmut_11 # type: ignore # mutmut generated
