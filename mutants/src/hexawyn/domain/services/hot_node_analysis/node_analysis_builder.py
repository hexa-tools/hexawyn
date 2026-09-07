from __future__ import annotations

from hexawyn.domain.models.constants import HotNodeAnalysisConstants
from hexawyn.domain.models.hot_node_analysis import (
    ClusterNodeSnapshot,
    HotNodeAnalysisReport,
    HotNodeAnalysisRequest,
    HotNodeResult,
    Recommendation,
    TopConsumer,
)
from hexawyn.domain.services.hot_node_analysis.hot_node_detection import (
    HotStatus,
    compute_hot_status,
)
from hexawyn.domain.services.hot_node_analysis.redistribution import (
    RedistributionResult,
    find_redistribution_target,
)
from hexawyn.domain.services.hot_node_analysis.top_consumers import select_top_consumers

_cfg = HotNodeAnalysisConstants()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_analyze_hot_nodes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_analyze_hot_nodes__mutmut)
def analyze_hot_nodes(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_orig(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_1(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = None
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_2(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = None

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_3(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_4(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = None
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_5(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = None
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_6(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series or not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_7(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_8(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_9(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                None
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_10(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            break
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_11(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(None)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_12(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = None

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_13(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                None, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_14(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, None, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_15(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, None
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_16(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_17(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_18(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_19(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                None, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_20(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, None, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_21(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, None
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_22(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_23(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_24(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_25(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = None
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_26(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot and statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_27(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][1].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_28(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][2].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_29(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = None
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_30(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_31(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = None

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_32(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_33(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = None

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_34(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(None, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_35(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, None, non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_36(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], None)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_37(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_38(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_39(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], )
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_40(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=None,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_41(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=None,
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_42(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=None,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_43(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=None,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_44(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=None,
    )


def x_analyze_hot_nodes__mutmut_45(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_46(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_47(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_48(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_49(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        )


def x_analyze_hot_nodes__mutmut_50(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(None, len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_51(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, None, warnings),
    )


def x_analyze_hot_nodes__mutmut_52(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), None),
    )


def x_analyze_hot_nodes__mutmut_53(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(len(non_hot_snapshots), warnings),
    )


def x_analyze_hot_nodes__mutmut_54(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, warnings),
    )


def x_analyze_hot_nodes__mutmut_55(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), ),
    )

mutants_x_analyze_hot_nodes__mutmut['_mutmut_orig'] = x_analyze_hot_nodes__mutmut_orig # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_1'] = x_analyze_hot_nodes__mutmut_1 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_2'] = x_analyze_hot_nodes__mutmut_2 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_3'] = x_analyze_hot_nodes__mutmut_3 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_4'] = x_analyze_hot_nodes__mutmut_4 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_5'] = x_analyze_hot_nodes__mutmut_5 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_6'] = x_analyze_hot_nodes__mutmut_6 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_7'] = x_analyze_hot_nodes__mutmut_7 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_8'] = x_analyze_hot_nodes__mutmut_8 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_9'] = x_analyze_hot_nodes__mutmut_9 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_10'] = x_analyze_hot_nodes__mutmut_10 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_11'] = x_analyze_hot_nodes__mutmut_11 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_12'] = x_analyze_hot_nodes__mutmut_12 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_13'] = x_analyze_hot_nodes__mutmut_13 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_14'] = x_analyze_hot_nodes__mutmut_14 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_15'] = x_analyze_hot_nodes__mutmut_15 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_16'] = x_analyze_hot_nodes__mutmut_16 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_17'] = x_analyze_hot_nodes__mutmut_17 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_18'] = x_analyze_hot_nodes__mutmut_18 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_19'] = x_analyze_hot_nodes__mutmut_19 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_20'] = x_analyze_hot_nodes__mutmut_20 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_21'] = x_analyze_hot_nodes__mutmut_21 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_22'] = x_analyze_hot_nodes__mutmut_22 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_23'] = x_analyze_hot_nodes__mutmut_23 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_24'] = x_analyze_hot_nodes__mutmut_24 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_25'] = x_analyze_hot_nodes__mutmut_25 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_26'] = x_analyze_hot_nodes__mutmut_26 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_27'] = x_analyze_hot_nodes__mutmut_27 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_28'] = x_analyze_hot_nodes__mutmut_28 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_29'] = x_analyze_hot_nodes__mutmut_29 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_30'] = x_analyze_hot_nodes__mutmut_30 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_31'] = x_analyze_hot_nodes__mutmut_31 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_32'] = x_analyze_hot_nodes__mutmut_32 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_33'] = x_analyze_hot_nodes__mutmut_33 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_34'] = x_analyze_hot_nodes__mutmut_34 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_35'] = x_analyze_hot_nodes__mutmut_35 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_36'] = x_analyze_hot_nodes__mutmut_36 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_37'] = x_analyze_hot_nodes__mutmut_37 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_38'] = x_analyze_hot_nodes__mutmut_38 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_39'] = x_analyze_hot_nodes__mutmut_39 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_40'] = x_analyze_hot_nodes__mutmut_40 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_41'] = x_analyze_hot_nodes__mutmut_41 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_42'] = x_analyze_hot_nodes__mutmut_42 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_43'] = x_analyze_hot_nodes__mutmut_43 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_44'] = x_analyze_hot_nodes__mutmut_44 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_45'] = x_analyze_hot_nodes__mutmut_45 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_46'] = x_analyze_hot_nodes__mutmut_46 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_47'] = x_analyze_hot_nodes__mutmut_47 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_48'] = x_analyze_hot_nodes__mutmut_48 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_49'] = x_analyze_hot_nodes__mutmut_49 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_50'] = x_analyze_hot_nodes__mutmut_50 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_51'] = x_analyze_hot_nodes__mutmut_51 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_52'] = x_analyze_hot_nodes__mutmut_52 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_53'] = x_analyze_hot_nodes__mutmut_53 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_54'] = x_analyze_hot_nodes__mutmut_54 # type: ignore # mutmut generated
mutants_x_analyze_hot_nodes__mutmut['x_analyze_hot_nodes__mutmut_55'] = x_analyze_hot_nodes__mutmut_55 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_hot_node_result__mutmut)
def _build_hot_node_result(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_orig(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_1(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = None
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_2(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = None
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_3(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(None, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_4(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, None)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_5(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(_cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_6(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, )
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_7(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = None

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_8(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(None, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_9(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, None)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_10(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_11(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, )

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_12(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=None,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_13(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=None,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_14(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=None,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_15(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=None,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_16(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=None,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_17(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=None,
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_18(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=None,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_19(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=None,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_20(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=None,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_21(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=None,
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_22(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=None,
    )


def x__build_hot_node_result__mutmut_23(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_24(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_25(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_26(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_27(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_28(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_29(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_30(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_31(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_32(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_33(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        )


def x__build_hot_node_result__mutmut_34(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(None, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_35(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, None),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_36(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_37(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, ),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_38(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(None, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_39(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, None),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_40(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_41(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, ),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def x__build_hot_node_result__mutmut_42(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern and memory_status.business_hours_pattern,
    )

mutants_x__build_hot_node_result__mutmut['_mutmut_orig'] = x__build_hot_node_result__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_1'] = x__build_hot_node_result__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_2'] = x__build_hot_node_result__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_3'] = x__build_hot_node_result__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_4'] = x__build_hot_node_result__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_5'] = x__build_hot_node_result__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_6'] = x__build_hot_node_result__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_7'] = x__build_hot_node_result__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_8'] = x__build_hot_node_result__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_9'] = x__build_hot_node_result__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_10'] = x__build_hot_node_result__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_11'] = x__build_hot_node_result__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_12'] = x__build_hot_node_result__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_13'] = x__build_hot_node_result__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_14'] = x__build_hot_node_result__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_15'] = x__build_hot_node_result__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_16'] = x__build_hot_node_result__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_17'] = x__build_hot_node_result__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_18'] = x__build_hot_node_result__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_19'] = x__build_hot_node_result__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_20'] = x__build_hot_node_result__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_21'] = x__build_hot_node_result__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_22'] = x__build_hot_node_result__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_23'] = x__build_hot_node_result__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_24'] = x__build_hot_node_result__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_25'] = x__build_hot_node_result__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_26'] = x__build_hot_node_result__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_27'] = x__build_hot_node_result__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_28'] = x__build_hot_node_result__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_29'] = x__build_hot_node_result__mutmut_29 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_30'] = x__build_hot_node_result__mutmut_30 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_31'] = x__build_hot_node_result__mutmut_31 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_32'] = x__build_hot_node_result__mutmut_32 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_33'] = x__build_hot_node_result__mutmut_33 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_34'] = x__build_hot_node_result__mutmut_34 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_35'] = x__build_hot_node_result__mutmut_35 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_36'] = x__build_hot_node_result__mutmut_36 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_37'] = x__build_hot_node_result__mutmut_37 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_38'] = x__build_hot_node_result__mutmut_38 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_39'] = x__build_hot_node_result__mutmut_39 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_40'] = x__build_hot_node_result__mutmut_40 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_41'] = x__build_hot_node_result__mutmut_41 # type: ignore # mutmut generated
mutants_x__build_hot_node_result__mutmut['x__build_hot_node_result__mutmut_42'] = x__build_hot_node_result__mutmut_42 # type: ignore # mutmut generated
mutants_x__decide_recommendation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__decide_recommendation__mutmut)
def _decide_recommendation(
    redistribution: RedistributionResult, pods: list[TopConsumer]
) -> Recommendation:
    if redistribution.feasible:
        return "redistribute"
    if _has_single_dominant_pod(pods):
        return "scale_vertically"
    return "add_node"


def x__decide_recommendation__mutmut_orig(
    redistribution: RedistributionResult, pods: list[TopConsumer]
) -> Recommendation:
    if redistribution.feasible:
        return "redistribute"
    if _has_single_dominant_pod(pods):
        return "scale_vertically"
    return "add_node"


def x__decide_recommendation__mutmut_1(
    redistribution: RedistributionResult, pods: list[TopConsumer]
) -> Recommendation:
    if redistribution.feasible:
        return "XXredistributeXX"
    if _has_single_dominant_pod(pods):
        return "scale_vertically"
    return "add_node"


def x__decide_recommendation__mutmut_2(
    redistribution: RedistributionResult, pods: list[TopConsumer]
) -> Recommendation:
    if redistribution.feasible:
        return "REDISTRIBUTE"
    if _has_single_dominant_pod(pods):
        return "scale_vertically"
    return "add_node"


def x__decide_recommendation__mutmut_3(
    redistribution: RedistributionResult, pods: list[TopConsumer]
) -> Recommendation:
    if redistribution.feasible:
        return "redistribute"
    if _has_single_dominant_pod(None):
        return "scale_vertically"
    return "add_node"


def x__decide_recommendation__mutmut_4(
    redistribution: RedistributionResult, pods: list[TopConsumer]
) -> Recommendation:
    if redistribution.feasible:
        return "redistribute"
    if _has_single_dominant_pod(pods):
        return "XXscale_verticallyXX"
    return "add_node"


def x__decide_recommendation__mutmut_5(
    redistribution: RedistributionResult, pods: list[TopConsumer]
) -> Recommendation:
    if redistribution.feasible:
        return "redistribute"
    if _has_single_dominant_pod(pods):
        return "SCALE_VERTICALLY"
    return "add_node"


def x__decide_recommendation__mutmut_6(
    redistribution: RedistributionResult, pods: list[TopConsumer]
) -> Recommendation:
    if redistribution.feasible:
        return "redistribute"
    if _has_single_dominant_pod(pods):
        return "scale_vertically"
    return "XXadd_nodeXX"


def x__decide_recommendation__mutmut_7(
    redistribution: RedistributionResult, pods: list[TopConsumer]
) -> Recommendation:
    if redistribution.feasible:
        return "redistribute"
    if _has_single_dominant_pod(pods):
        return "scale_vertically"
    return "ADD_NODE"

mutants_x__decide_recommendation__mutmut['_mutmut_orig'] = x__decide_recommendation__mutmut_orig # type: ignore # mutmut generated
mutants_x__decide_recommendation__mutmut['x__decide_recommendation__mutmut_1'] = x__decide_recommendation__mutmut_1 # type: ignore # mutmut generated
mutants_x__decide_recommendation__mutmut['x__decide_recommendation__mutmut_2'] = x__decide_recommendation__mutmut_2 # type: ignore # mutmut generated
mutants_x__decide_recommendation__mutmut['x__decide_recommendation__mutmut_3'] = x__decide_recommendation__mutmut_3 # type: ignore # mutmut generated
mutants_x__decide_recommendation__mutmut['x__decide_recommendation__mutmut_4'] = x__decide_recommendation__mutmut_4 # type: ignore # mutmut generated
mutants_x__decide_recommendation__mutmut['x__decide_recommendation__mutmut_5'] = x__decide_recommendation__mutmut_5 # type: ignore # mutmut generated
mutants_x__decide_recommendation__mutmut['x__decide_recommendation__mutmut_6'] = x__decide_recommendation__mutmut_6 # type: ignore # mutmut generated
mutants_x__decide_recommendation__mutmut['x__decide_recommendation__mutmut_7'] = x__decide_recommendation__mutmut_7 # type: ignore # mutmut generated
mutants_x__has_single_dominant_pod__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__has_single_dominant_pod__mutmut)
def _has_single_dominant_pod(pods: list[TopConsumer]) -> bool:
    if not pods:
        return False
    total = sum(pod.cpu_usage_cores for pod in pods)
    if total <= 0:
        return False
    largest = max(pod.cpu_usage_cores for pod in pods)
    return (largest / total) >= _cfg.single_dominant_pod_ratio


def x__has_single_dominant_pod__mutmut_orig(pods: list[TopConsumer]) -> bool:
    if not pods:
        return False
    total = sum(pod.cpu_usage_cores for pod in pods)
    if total <= 0:
        return False
    largest = max(pod.cpu_usage_cores for pod in pods)
    return (largest / total) >= _cfg.single_dominant_pod_ratio


def x__has_single_dominant_pod__mutmut_1(pods: list[TopConsumer]) -> bool:
    if pods:
        return False
    total = sum(pod.cpu_usage_cores for pod in pods)
    if total <= 0:
        return False
    largest = max(pod.cpu_usage_cores for pod in pods)
    return (largest / total) >= _cfg.single_dominant_pod_ratio


def x__has_single_dominant_pod__mutmut_2(pods: list[TopConsumer]) -> bool:
    if not pods:
        return True
    total = sum(pod.cpu_usage_cores for pod in pods)
    if total <= 0:
        return False
    largest = max(pod.cpu_usage_cores for pod in pods)
    return (largest / total) >= _cfg.single_dominant_pod_ratio


def x__has_single_dominant_pod__mutmut_3(pods: list[TopConsumer]) -> bool:
    if not pods:
        return False
    total = None
    if total <= 0:
        return False
    largest = max(pod.cpu_usage_cores for pod in pods)
    return (largest / total) >= _cfg.single_dominant_pod_ratio


def x__has_single_dominant_pod__mutmut_4(pods: list[TopConsumer]) -> bool:
    if not pods:
        return False
    total = sum(None)
    if total <= 0:
        return False
    largest = max(pod.cpu_usage_cores for pod in pods)
    return (largest / total) >= _cfg.single_dominant_pod_ratio


def x__has_single_dominant_pod__mutmut_5(pods: list[TopConsumer]) -> bool:
    if not pods:
        return False
    total = sum(pod.cpu_usage_cores for pod in pods)
    if total < 0:
        return False
    largest = max(pod.cpu_usage_cores for pod in pods)
    return (largest / total) >= _cfg.single_dominant_pod_ratio


def x__has_single_dominant_pod__mutmut_6(pods: list[TopConsumer]) -> bool:
    if not pods:
        return False
    total = sum(pod.cpu_usage_cores for pod in pods)
    if total <= 1:
        return False
    largest = max(pod.cpu_usage_cores for pod in pods)
    return (largest / total) >= _cfg.single_dominant_pod_ratio


def x__has_single_dominant_pod__mutmut_7(pods: list[TopConsumer]) -> bool:
    if not pods:
        return False
    total = sum(pod.cpu_usage_cores for pod in pods)
    if total <= 0:
        return True
    largest = max(pod.cpu_usage_cores for pod in pods)
    return (largest / total) >= _cfg.single_dominant_pod_ratio


def x__has_single_dominant_pod__mutmut_8(pods: list[TopConsumer]) -> bool:
    if not pods:
        return False
    total = sum(pod.cpu_usage_cores for pod in pods)
    if total <= 0:
        return False
    largest = None
    return (largest / total) >= _cfg.single_dominant_pod_ratio


def x__has_single_dominant_pod__mutmut_9(pods: list[TopConsumer]) -> bool:
    if not pods:
        return False
    total = sum(pod.cpu_usage_cores for pod in pods)
    if total <= 0:
        return False
    largest = max(None)
    return (largest / total) >= _cfg.single_dominant_pod_ratio


def x__has_single_dominant_pod__mutmut_10(pods: list[TopConsumer]) -> bool:
    if not pods:
        return False
    total = sum(pod.cpu_usage_cores for pod in pods)
    if total <= 0:
        return False
    largest = max(pod.cpu_usage_cores for pod in pods)
    return (largest * total) >= _cfg.single_dominant_pod_ratio


def x__has_single_dominant_pod__mutmut_11(pods: list[TopConsumer]) -> bool:
    if not pods:
        return False
    total = sum(pod.cpu_usage_cores for pod in pods)
    if total <= 0:
        return False
    largest = max(pod.cpu_usage_cores for pod in pods)
    return (largest / total) > _cfg.single_dominant_pod_ratio

mutants_x__has_single_dominant_pod__mutmut['_mutmut_orig'] = x__has_single_dominant_pod__mutmut_orig # type: ignore # mutmut generated
mutants_x__has_single_dominant_pod__mutmut['x__has_single_dominant_pod__mutmut_1'] = x__has_single_dominant_pod__mutmut_1 # type: ignore # mutmut generated
mutants_x__has_single_dominant_pod__mutmut['x__has_single_dominant_pod__mutmut_2'] = x__has_single_dominant_pod__mutmut_2 # type: ignore # mutmut generated
mutants_x__has_single_dominant_pod__mutmut['x__has_single_dominant_pod__mutmut_3'] = x__has_single_dominant_pod__mutmut_3 # type: ignore # mutmut generated
mutants_x__has_single_dominant_pod__mutmut['x__has_single_dominant_pod__mutmut_4'] = x__has_single_dominant_pod__mutmut_4 # type: ignore # mutmut generated
mutants_x__has_single_dominant_pod__mutmut['x__has_single_dominant_pod__mutmut_5'] = x__has_single_dominant_pod__mutmut_5 # type: ignore # mutmut generated
mutants_x__has_single_dominant_pod__mutmut['x__has_single_dominant_pod__mutmut_6'] = x__has_single_dominant_pod__mutmut_6 # type: ignore # mutmut generated
mutants_x__has_single_dominant_pod__mutmut['x__has_single_dominant_pod__mutmut_7'] = x__has_single_dominant_pod__mutmut_7 # type: ignore # mutmut generated
mutants_x__has_single_dominant_pod__mutmut['x__has_single_dominant_pod__mutmut_8'] = x__has_single_dominant_pod__mutmut_8 # type: ignore # mutmut generated
mutants_x__has_single_dominant_pod__mutmut['x__has_single_dominant_pod__mutmut_9'] = x__has_single_dominant_pod__mutmut_9 # type: ignore # mutmut generated
mutants_x__has_single_dominant_pod__mutmut['x__has_single_dominant_pod__mutmut_10'] = x__has_single_dominant_pod__mutmut_10 # type: ignore # mutmut generated
mutants_x__has_single_dominant_pod__mutmut['x__has_single_dominant_pod__mutmut_11'] = x__has_single_dominant_pod__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_summary__mutmut)
def _build_summary(
    hot_results: list[HotNodeResult], healthy_node_count: int, warnings: list[str]
) -> str:
    if not hot_results:
        return (
            f"All {healthy_node_count} node(s) healthy — no nodes consistently "
            f"above {_cfg.hot_threshold_percent:.0f}%."
        )
    names = ", ".join(result.node_name for result in hot_results)
    summary = f"{len(hot_results)} hot node(s) detected: {names}."
    if warnings:
        summary += f" {len(warnings)} node(s) excluded due to missing metrics."
    return summary


def x__build_summary__mutmut_orig(
    hot_results: list[HotNodeResult], healthy_node_count: int, warnings: list[str]
) -> str:
    if not hot_results:
        return (
            f"All {healthy_node_count} node(s) healthy — no nodes consistently "
            f"above {_cfg.hot_threshold_percent:.0f}%."
        )
    names = ", ".join(result.node_name for result in hot_results)
    summary = f"{len(hot_results)} hot node(s) detected: {names}."
    if warnings:
        summary += f" {len(warnings)} node(s) excluded due to missing metrics."
    return summary


def x__build_summary__mutmut_1(
    hot_results: list[HotNodeResult], healthy_node_count: int, warnings: list[str]
) -> str:
    if hot_results:
        return (
            f"All {healthy_node_count} node(s) healthy — no nodes consistently "
            f"above {_cfg.hot_threshold_percent:.0f}%."
        )
    names = ", ".join(result.node_name for result in hot_results)
    summary = f"{len(hot_results)} hot node(s) detected: {names}."
    if warnings:
        summary += f" {len(warnings)} node(s) excluded due to missing metrics."
    return summary


def x__build_summary__mutmut_2(
    hot_results: list[HotNodeResult], healthy_node_count: int, warnings: list[str]
) -> str:
    if not hot_results:
        return (
            f"All {healthy_node_count} node(s) healthy — no nodes consistently "
            f"above {_cfg.hot_threshold_percent:.0f}%."
        )
    names = None
    summary = f"{len(hot_results)} hot node(s) detected: {names}."
    if warnings:
        summary += f" {len(warnings)} node(s) excluded due to missing metrics."
    return summary


def x__build_summary__mutmut_3(
    hot_results: list[HotNodeResult], healthy_node_count: int, warnings: list[str]
) -> str:
    if not hot_results:
        return (
            f"All {healthy_node_count} node(s) healthy — no nodes consistently "
            f"above {_cfg.hot_threshold_percent:.0f}%."
        )
    names = ", ".join(None)
    summary = f"{len(hot_results)} hot node(s) detected: {names}."
    if warnings:
        summary += f" {len(warnings)} node(s) excluded due to missing metrics."
    return summary


def x__build_summary__mutmut_4(
    hot_results: list[HotNodeResult], healthy_node_count: int, warnings: list[str]
) -> str:
    if not hot_results:
        return (
            f"All {healthy_node_count} node(s) healthy — no nodes consistently "
            f"above {_cfg.hot_threshold_percent:.0f}%."
        )
    names = "XX, XX".join(result.node_name for result in hot_results)
    summary = f"{len(hot_results)} hot node(s) detected: {names}."
    if warnings:
        summary += f" {len(warnings)} node(s) excluded due to missing metrics."
    return summary


def x__build_summary__mutmut_5(
    hot_results: list[HotNodeResult], healthy_node_count: int, warnings: list[str]
) -> str:
    if not hot_results:
        return (
            f"All {healthy_node_count} node(s) healthy — no nodes consistently "
            f"above {_cfg.hot_threshold_percent:.0f}%."
        )
    names = ", ".join(result.node_name for result in hot_results)
    summary = None
    if warnings:
        summary += f" {len(warnings)} node(s) excluded due to missing metrics."
    return summary


def x__build_summary__mutmut_6(
    hot_results: list[HotNodeResult], healthy_node_count: int, warnings: list[str]
) -> str:
    if not hot_results:
        return (
            f"All {healthy_node_count} node(s) healthy — no nodes consistently "
            f"above {_cfg.hot_threshold_percent:.0f}%."
        )
    names = ", ".join(result.node_name for result in hot_results)
    summary = f"{len(hot_results)} hot node(s) detected: {names}."
    if warnings:
        summary = f" {len(warnings)} node(s) excluded due to missing metrics."
    return summary


def x__build_summary__mutmut_7(
    hot_results: list[HotNodeResult], healthy_node_count: int, warnings: list[str]
) -> str:
    if not hot_results:
        return (
            f"All {healthy_node_count} node(s) healthy — no nodes consistently "
            f"above {_cfg.hot_threshold_percent:.0f}%."
        )
    names = ", ".join(result.node_name for result in hot_results)
    summary = f"{len(hot_results)} hot node(s) detected: {names}."
    if warnings:
        summary -= f" {len(warnings)} node(s) excluded due to missing metrics."
    return summary

mutants_x__build_summary__mutmut['_mutmut_orig'] = x__build_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_1'] = x__build_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_2'] = x__build_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_3'] = x__build_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_4'] = x__build_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_5'] = x__build_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_6'] = x__build_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_7'] = x__build_summary__mutmut_7 # type: ignore # mutmut generated
