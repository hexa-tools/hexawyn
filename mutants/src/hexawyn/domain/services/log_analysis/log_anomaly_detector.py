from __future__ import annotations

from collections import defaultdict
from dataclasses import replace

from hexawyn.domain.models.analyze_pod_logs import PodLogLine
from hexawyn.domain.models.constants import LogAnomalyDetectionConstants
from hexawyn.domain.models.log_anomaly import (
    DetectLogAnomaliesRequest,
    DetectLogAnomaliesResult,
    LogAnomaly,
)
from hexawyn.domain.services.anomaly_detection.ml import IsolationForestAnomalyDetector
from hexawyn.domain.services.anomaly_detection.statistical import ZScoreAnomalyDetector

_cfg = LogAnomalyDetectionConstants()
_INSUFFICIENT_DATA_SUMMARY = "insufficient data for statistical analysis"
_NO_ANOMALIES_SUMMARY = "no anomalies detected"

_IndexedLine = tuple[int, PodLogLine]
_IndexedAnomaly = tuple[int, LogAnomaly]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_log_anomalies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_log_anomalies__mutmut)
def detect_log_anomalies(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_orig(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_1(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = None
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_2(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines <= _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_3(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=None,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_4(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=None,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_5(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=None,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_6(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=None,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_7(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=None,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_8(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=None,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_9(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_10(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_11(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_12(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_13(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_14(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_15(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=False,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_16(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = None

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_17(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(None)

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_18(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(None))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_19(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = None
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_20(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        None, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_21(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, None
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_22(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_23(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_24(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = None
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_25(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(None)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_26(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = None

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_27(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(None)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_28(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = None

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_29(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(None)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_30(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies - semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_31(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_32(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=None,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_33(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=None,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_34(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=None,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_35(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=None,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_36(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=None,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_37(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=None,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_38(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=None,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_39(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=None,
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_40(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_41(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_42(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_43(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_44(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_45(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_46(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_47(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_48(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = None
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_49(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "XXyXX" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_50(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "Y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_51(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) != 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_52(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 2 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_53(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "XXiesXX"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_54(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "IES"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_55(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=None,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_56(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=None,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_57(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=None,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_58(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=None,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_59(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=None,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_60(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=None,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_61(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=None,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_62(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=None,
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_63(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=None,
    )


def x_detect_log_anomalies__mutmut_64(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_65(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_66(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_67(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_68(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_69(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_70(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        summary=f"{len(anomalies)} anomal{plural} detected",
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_71(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        formats_analyzed_separately=len(format_groups),
    )


def x_detect_log_anomalies__mutmut_72(
    request: DetectLogAnomaliesRequest, log_lines: list[PodLogLine]
) -> DetectLogAnomaliesResult:
    """Domain service — combines Z-score volume detection and Isolation Forest
    semantic outlier detection (ILogAnalysisStrategy port dependency, ECA-14).

    Zero K8s dependency: operates purely on PodLogLine values already fetched
    by an adapter through PodLogsPort.
    """
    total_lines = len(log_lines)
    if total_lines < _cfg.min_lines_for_analysis:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            insufficient_data=True,
            summary=_INSUFFICIENT_DATA_SUMMARY,
        )

    indexed_lines = list(enumerate(log_lines))

    volume_anomalies, baseline_mean, baseline_std = _detect_volume_anomalies(
        indexed_lines, request.zscore_threshold
    )
    format_groups = _group_by_format(indexed_lines)
    semantic_anomalies = _detect_semantic_anomalies(format_groups)

    anomalies = _finalize_anomalies(volume_anomalies + semantic_anomalies)

    if not anomalies:
        return DetectLogAnomaliesResult(
            pod_name=request.pod_name,
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            total_lines=total_lines,
            baseline_mean_lines_per_minute=baseline_mean,
            baseline_std_dev=baseline_std,
            summary=_NO_ANOMALIES_SUMMARY,
            formats_analyzed_separately=len(format_groups),
        )

    plural = "y" if len(anomalies) == 1 else "ies"
    return DetectLogAnomaliesResult(
        pod_name=request.pod_name,
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        total_lines=total_lines,
        anomalies=anomalies,
        baseline_mean_lines_per_minute=baseline_mean,
        baseline_std_dev=baseline_std,
        summary=f"{len(anomalies)} anomal{plural} detected",
        )

mutants_x_detect_log_anomalies__mutmut['_mutmut_orig'] = x_detect_log_anomalies__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_1'] = x_detect_log_anomalies__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_2'] = x_detect_log_anomalies__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_3'] = x_detect_log_anomalies__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_4'] = x_detect_log_anomalies__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_5'] = x_detect_log_anomalies__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_6'] = x_detect_log_anomalies__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_7'] = x_detect_log_anomalies__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_8'] = x_detect_log_anomalies__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_9'] = x_detect_log_anomalies__mutmut_9 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_10'] = x_detect_log_anomalies__mutmut_10 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_11'] = x_detect_log_anomalies__mutmut_11 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_12'] = x_detect_log_anomalies__mutmut_12 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_13'] = x_detect_log_anomalies__mutmut_13 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_14'] = x_detect_log_anomalies__mutmut_14 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_15'] = x_detect_log_anomalies__mutmut_15 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_16'] = x_detect_log_anomalies__mutmut_16 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_17'] = x_detect_log_anomalies__mutmut_17 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_18'] = x_detect_log_anomalies__mutmut_18 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_19'] = x_detect_log_anomalies__mutmut_19 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_20'] = x_detect_log_anomalies__mutmut_20 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_21'] = x_detect_log_anomalies__mutmut_21 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_22'] = x_detect_log_anomalies__mutmut_22 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_23'] = x_detect_log_anomalies__mutmut_23 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_24'] = x_detect_log_anomalies__mutmut_24 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_25'] = x_detect_log_anomalies__mutmut_25 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_26'] = x_detect_log_anomalies__mutmut_26 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_27'] = x_detect_log_anomalies__mutmut_27 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_28'] = x_detect_log_anomalies__mutmut_28 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_29'] = x_detect_log_anomalies__mutmut_29 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_30'] = x_detect_log_anomalies__mutmut_30 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_31'] = x_detect_log_anomalies__mutmut_31 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_32'] = x_detect_log_anomalies__mutmut_32 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_33'] = x_detect_log_anomalies__mutmut_33 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_34'] = x_detect_log_anomalies__mutmut_34 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_35'] = x_detect_log_anomalies__mutmut_35 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_36'] = x_detect_log_anomalies__mutmut_36 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_37'] = x_detect_log_anomalies__mutmut_37 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_38'] = x_detect_log_anomalies__mutmut_38 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_39'] = x_detect_log_anomalies__mutmut_39 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_40'] = x_detect_log_anomalies__mutmut_40 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_41'] = x_detect_log_anomalies__mutmut_41 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_42'] = x_detect_log_anomalies__mutmut_42 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_43'] = x_detect_log_anomalies__mutmut_43 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_44'] = x_detect_log_anomalies__mutmut_44 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_45'] = x_detect_log_anomalies__mutmut_45 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_46'] = x_detect_log_anomalies__mutmut_46 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_47'] = x_detect_log_anomalies__mutmut_47 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_48'] = x_detect_log_anomalies__mutmut_48 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_49'] = x_detect_log_anomalies__mutmut_49 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_50'] = x_detect_log_anomalies__mutmut_50 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_51'] = x_detect_log_anomalies__mutmut_51 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_52'] = x_detect_log_anomalies__mutmut_52 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_53'] = x_detect_log_anomalies__mutmut_53 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_54'] = x_detect_log_anomalies__mutmut_54 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_55'] = x_detect_log_anomalies__mutmut_55 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_56'] = x_detect_log_anomalies__mutmut_56 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_57'] = x_detect_log_anomalies__mutmut_57 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_58'] = x_detect_log_anomalies__mutmut_58 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_59'] = x_detect_log_anomalies__mutmut_59 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_60'] = x_detect_log_anomalies__mutmut_60 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_61'] = x_detect_log_anomalies__mutmut_61 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_62'] = x_detect_log_anomalies__mutmut_62 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_63'] = x_detect_log_anomalies__mutmut_63 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_64'] = x_detect_log_anomalies__mutmut_64 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_65'] = x_detect_log_anomalies__mutmut_65 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_66'] = x_detect_log_anomalies__mutmut_66 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_67'] = x_detect_log_anomalies__mutmut_67 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_68'] = x_detect_log_anomalies__mutmut_68 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_69'] = x_detect_log_anomalies__mutmut_69 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_70'] = x_detect_log_anomalies__mutmut_70 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_71'] = x_detect_log_anomalies__mutmut_71 # type: ignore # mutmut generated
mutants_x_detect_log_anomalies__mutmut['x_detect_log_anomalies__mutmut_72'] = x_detect_log_anomalies__mutmut_72 # type: ignore # mutmut generated
mutants_x__minute_bucket__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__minute_bucket__mutmut)
def _minute_bucket(timestamp: str) -> str:
    return timestamp[:16]


def x__minute_bucket__mutmut_orig(timestamp: str) -> str:
    return timestamp[:16]


def x__minute_bucket__mutmut_1(timestamp: str) -> str:
    return timestamp[:17]

mutants_x__minute_bucket__mutmut['_mutmut_orig'] = x__minute_bucket__mutmut_orig # type: ignore # mutmut generated
mutants_x__minute_bucket__mutmut['x__minute_bucket__mutmut_1'] = x__minute_bucket__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_volume_anomalies__mutmut)
def _detect_volume_anomalies(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_orig(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_1(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = None
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_2(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(None)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_3(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append(None)

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_4(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(None)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_5(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = None
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_6(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(None)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_7(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = None

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_8(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(None) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_9(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = None

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_10(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(None, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_11(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=None)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_12(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_13(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, )

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_14(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=None).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_15(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = None
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_16(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = None
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_17(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(None)]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_18(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["XXindexXX"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_19(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["INDEX"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_20(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = None
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_21(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][1]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_22(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            None
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_23(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=None,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_24(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=None,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_25(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=None,
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_26(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type=None,
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_27(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_28(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    anomaly_score=float(entry["z_score"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_29(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_30(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_31(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(None),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_32(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["XXz_scoreXX"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_33(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["Z_SCORE"]),
                    type="volume",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_34(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="XXvolumeXX",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev


def x__detect_volume_anomalies__mutmut_35(
    indexed_lines: list[_IndexedLine], zscore_threshold: float
) -> tuple[list[_IndexedAnomaly], float, float]:
    buckets: dict[str, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        buckets[_minute_bucket(line.timestamp)].append((index, line))

    bucket_keys = sorted(buckets)
    counts = [float(len(buckets[key])) for key in bucket_keys]

    result = ZScoreAnomalyDetector(threshold=zscore_threshold).detect(counts, context=bucket_keys)

    anomalies: list[_IndexedAnomaly] = []
    for entry in result.anomalies:
        bucket_key = bucket_keys[int(entry["index"])]
        first_index, first_line = buckets[bucket_key][0]
        anomalies.append(
            (
                first_index,
                LogAnomaly(
                    timestamp=bucket_key,
                    log_line=first_line.message,
                    anomaly_score=float(entry["z_score"]),
                    type="VOLUME",
                ),
            )
        )
    return anomalies, result.mean, result.std_dev

mutants_x__detect_volume_anomalies__mutmut['_mutmut_orig'] = x__detect_volume_anomalies__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_1'] = x__detect_volume_anomalies__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_2'] = x__detect_volume_anomalies__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_3'] = x__detect_volume_anomalies__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_4'] = x__detect_volume_anomalies__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_5'] = x__detect_volume_anomalies__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_6'] = x__detect_volume_anomalies__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_7'] = x__detect_volume_anomalies__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_8'] = x__detect_volume_anomalies__mutmut_8 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_9'] = x__detect_volume_anomalies__mutmut_9 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_10'] = x__detect_volume_anomalies__mutmut_10 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_11'] = x__detect_volume_anomalies__mutmut_11 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_12'] = x__detect_volume_anomalies__mutmut_12 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_13'] = x__detect_volume_anomalies__mutmut_13 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_14'] = x__detect_volume_anomalies__mutmut_14 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_15'] = x__detect_volume_anomalies__mutmut_15 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_16'] = x__detect_volume_anomalies__mutmut_16 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_17'] = x__detect_volume_anomalies__mutmut_17 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_18'] = x__detect_volume_anomalies__mutmut_18 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_19'] = x__detect_volume_anomalies__mutmut_19 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_20'] = x__detect_volume_anomalies__mutmut_20 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_21'] = x__detect_volume_anomalies__mutmut_21 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_22'] = x__detect_volume_anomalies__mutmut_22 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_23'] = x__detect_volume_anomalies__mutmut_23 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_24'] = x__detect_volume_anomalies__mutmut_24 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_25'] = x__detect_volume_anomalies__mutmut_25 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_26'] = x__detect_volume_anomalies__mutmut_26 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_27'] = x__detect_volume_anomalies__mutmut_27 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_28'] = x__detect_volume_anomalies__mutmut_28 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_29'] = x__detect_volume_anomalies__mutmut_29 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_30'] = x__detect_volume_anomalies__mutmut_30 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_31'] = x__detect_volume_anomalies__mutmut_31 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_32'] = x__detect_volume_anomalies__mutmut_32 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_33'] = x__detect_volume_anomalies__mutmut_33 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_34'] = x__detect_volume_anomalies__mutmut_34 # type: ignore # mutmut generated
mutants_x__detect_volume_anomalies__mutmut['x__detect_volume_anomalies__mutmut_35'] = x__detect_volume_anomalies__mutmut_35 # type: ignore # mutmut generated
mutants_x__group_by_format__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__group_by_format__mutmut)
def _group_by_format(indexed_lines: list[_IndexedLine]) -> list[list[_IndexedLine]]:
    """Edge case: log format changes mid-window → each format analyzed separately."""
    groups: dict[bool, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        groups[line.is_json].append((index, line))
    return [group for group in groups.values() if group]


def x__group_by_format__mutmut_orig(indexed_lines: list[_IndexedLine]) -> list[list[_IndexedLine]]:
    """Edge case: log format changes mid-window → each format analyzed separately."""
    groups: dict[bool, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        groups[line.is_json].append((index, line))
    return [group for group in groups.values() if group]


def x__group_by_format__mutmut_1(indexed_lines: list[_IndexedLine]) -> list[list[_IndexedLine]]:
    """Edge case: log format changes mid-window → each format analyzed separately."""
    groups: dict[bool, list[_IndexedLine]] = None
    for index, line in indexed_lines:
        groups[line.is_json].append((index, line))
    return [group for group in groups.values() if group]


def x__group_by_format__mutmut_2(indexed_lines: list[_IndexedLine]) -> list[list[_IndexedLine]]:
    """Edge case: log format changes mid-window → each format analyzed separately."""
    groups: dict[bool, list[_IndexedLine]] = defaultdict(None)
    for index, line in indexed_lines:
        groups[line.is_json].append((index, line))
    return [group for group in groups.values() if group]


def x__group_by_format__mutmut_3(indexed_lines: list[_IndexedLine]) -> list[list[_IndexedLine]]:
    """Edge case: log format changes mid-window → each format analyzed separately."""
    groups: dict[bool, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        groups[line.is_json].append(None)
    return [group for group in groups.values() if group]

mutants_x__group_by_format__mutmut['_mutmut_orig'] = x__group_by_format__mutmut_orig # type: ignore # mutmut generated
mutants_x__group_by_format__mutmut['x__group_by_format__mutmut_1'] = x__group_by_format__mutmut_1 # type: ignore # mutmut generated
mutants_x__group_by_format__mutmut['x__group_by_format__mutmut_2'] = x__group_by_format__mutmut_2 # type: ignore # mutmut generated
mutants_x__group_by_format__mutmut['x__group_by_format__mutmut_3'] = x__group_by_format__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_semantic_anomalies__mutmut)
def _detect_semantic_anomalies(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_orig(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_1(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = None
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_2(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = None
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_3(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = None
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_4(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = None
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_5(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(None)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_6(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = None
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_7(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(None)]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_8(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["XXindexXX"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_9(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["INDEX"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_10(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                None
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_11(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=None,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_12(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=None,
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_13(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=None,
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_14(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type=None,
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_15(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_16(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_17(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_18(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_19(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(None),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_20(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["XXlineXX"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_21(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["LINE"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_22(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(None),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_23(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["XXanomaly_scoreXX"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_24(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["ANOMALY_SCORE"]),
                        type="semantic",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_25(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="XXsemanticXX",
                    ),
                )
            )
    return anomalies


def x__detect_semantic_anomalies__mutmut_26(
    format_groups: list[list[_IndexedLine]],
) -> list[_IndexedAnomaly]:
    detector = IsolationForestAnomalyDetector()
    anomalies: list[_IndexedAnomaly] = []
    for group in format_groups:
        messages = [line.message for _, line in group]
        result = detector.detect(messages)
        for entry in result.anomalies:
            original_index, line = group[int(entry["index"])]
            anomalies.append(
                (
                    original_index,
                    LogAnomaly(
                        timestamp=line.timestamp,
                        log_line=str(entry["line"]),
                        anomaly_score=float(entry["anomaly_score"]),
                        type="SEMANTIC",
                    ),
                )
            )
    return anomalies

mutants_x__detect_semantic_anomalies__mutmut['_mutmut_orig'] = x__detect_semantic_anomalies__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_1'] = x__detect_semantic_anomalies__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_2'] = x__detect_semantic_anomalies__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_3'] = x__detect_semantic_anomalies__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_4'] = x__detect_semantic_anomalies__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_5'] = x__detect_semantic_anomalies__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_6'] = x__detect_semantic_anomalies__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_7'] = x__detect_semantic_anomalies__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_8'] = x__detect_semantic_anomalies__mutmut_8 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_9'] = x__detect_semantic_anomalies__mutmut_9 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_10'] = x__detect_semantic_anomalies__mutmut_10 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_11'] = x__detect_semantic_anomalies__mutmut_11 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_12'] = x__detect_semantic_anomalies__mutmut_12 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_13'] = x__detect_semantic_anomalies__mutmut_13 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_14'] = x__detect_semantic_anomalies__mutmut_14 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_15'] = x__detect_semantic_anomalies__mutmut_15 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_16'] = x__detect_semantic_anomalies__mutmut_16 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_17'] = x__detect_semantic_anomalies__mutmut_17 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_18'] = x__detect_semantic_anomalies__mutmut_18 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_19'] = x__detect_semantic_anomalies__mutmut_19 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_20'] = x__detect_semantic_anomalies__mutmut_20 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_21'] = x__detect_semantic_anomalies__mutmut_21 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_22'] = x__detect_semantic_anomalies__mutmut_22 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_23'] = x__detect_semantic_anomalies__mutmut_23 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_24'] = x__detect_semantic_anomalies__mutmut_24 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_25'] = x__detect_semantic_anomalies__mutmut_25 # type: ignore # mutmut generated
mutants_x__detect_semantic_anomalies__mutmut['x__detect_semantic_anomalies__mutmut_26'] = x__detect_semantic_anomalies__mutmut_26 # type: ignore # mutmut generated
mutants_x__finalize_anomalies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__finalize_anomalies__mutmut)
def _finalize_anomalies(anomalies: list[_IndexedAnomaly]) -> list[LogAnomaly]:
    """Sorts by original position and flags low-confidence anomalies (edge case:
    an anomaly found in the first N lines has too little surrounding context)."""
    anomalies.sort(key=lambda pair: pair[0])
    return [
        replace(anomaly, low_confidence=True)
        if index < _cfg.low_confidence_line_window
        else anomaly
        for index, anomaly in anomalies
    ]


def x__finalize_anomalies__mutmut_orig(anomalies: list[_IndexedAnomaly]) -> list[LogAnomaly]:
    """Sorts by original position and flags low-confidence anomalies (edge case:
    an anomaly found in the first N lines has too little surrounding context)."""
    anomalies.sort(key=lambda pair: pair[0])
    return [
        replace(anomaly, low_confidence=True)
        if index < _cfg.low_confidence_line_window
        else anomaly
        for index, anomaly in anomalies
    ]


def x__finalize_anomalies__mutmut_1(anomalies: list[_IndexedAnomaly]) -> list[LogAnomaly]:
    """Sorts by original position and flags low-confidence anomalies (edge case:
    an anomaly found in the first N lines has too little surrounding context)."""
    anomalies.sort(key=None)
    return [
        replace(anomaly, low_confidence=True)
        if index < _cfg.low_confidence_line_window
        else anomaly
        for index, anomaly in anomalies
    ]


def x__finalize_anomalies__mutmut_2(anomalies: list[_IndexedAnomaly]) -> list[LogAnomaly]:
    """Sorts by original position and flags low-confidence anomalies (edge case:
    an anomaly found in the first N lines has too little surrounding context)."""
    anomalies.sort(key=lambda pair: None)
    return [
        replace(anomaly, low_confidence=True)
        if index < _cfg.low_confidence_line_window
        else anomaly
        for index, anomaly in anomalies
    ]


def x__finalize_anomalies__mutmut_3(anomalies: list[_IndexedAnomaly]) -> list[LogAnomaly]:
    """Sorts by original position and flags low-confidence anomalies (edge case:
    an anomaly found in the first N lines has too little surrounding context)."""
    anomalies.sort(key=lambda pair: pair[1])
    return [
        replace(anomaly, low_confidence=True)
        if index < _cfg.low_confidence_line_window
        else anomaly
        for index, anomaly in anomalies
    ]


def x__finalize_anomalies__mutmut_4(anomalies: list[_IndexedAnomaly]) -> list[LogAnomaly]:
    """Sorts by original position and flags low-confidence anomalies (edge case:
    an anomaly found in the first N lines has too little surrounding context)."""
    anomalies.sort(key=lambda pair: pair[0])
    return [
        replace(None, low_confidence=True)
        if index < _cfg.low_confidence_line_window
        else anomaly
        for index, anomaly in anomalies
    ]


def x__finalize_anomalies__mutmut_5(anomalies: list[_IndexedAnomaly]) -> list[LogAnomaly]:
    """Sorts by original position and flags low-confidence anomalies (edge case:
    an anomaly found in the first N lines has too little surrounding context)."""
    anomalies.sort(key=lambda pair: pair[0])
    return [
        replace(anomaly, low_confidence=None)
        if index < _cfg.low_confidence_line_window
        else anomaly
        for index, anomaly in anomalies
    ]


def x__finalize_anomalies__mutmut_6(anomalies: list[_IndexedAnomaly]) -> list[LogAnomaly]:
    """Sorts by original position and flags low-confidence anomalies (edge case:
    an anomaly found in the first N lines has too little surrounding context)."""
    anomalies.sort(key=lambda pair: pair[0])
    return [
        replace(low_confidence=True)
        if index < _cfg.low_confidence_line_window
        else anomaly
        for index, anomaly in anomalies
    ]


def x__finalize_anomalies__mutmut_7(anomalies: list[_IndexedAnomaly]) -> list[LogAnomaly]:
    """Sorts by original position and flags low-confidence anomalies (edge case:
    an anomaly found in the first N lines has too little surrounding context)."""
    anomalies.sort(key=lambda pair: pair[0])
    return [
        replace(anomaly, )
        if index < _cfg.low_confidence_line_window
        else anomaly
        for index, anomaly in anomalies
    ]


def x__finalize_anomalies__mutmut_8(anomalies: list[_IndexedAnomaly]) -> list[LogAnomaly]:
    """Sorts by original position and flags low-confidence anomalies (edge case:
    an anomaly found in the first N lines has too little surrounding context)."""
    anomalies.sort(key=lambda pair: pair[0])
    return [
        replace(anomaly, low_confidence=False)
        if index < _cfg.low_confidence_line_window
        else anomaly
        for index, anomaly in anomalies
    ]


def x__finalize_anomalies__mutmut_9(anomalies: list[_IndexedAnomaly]) -> list[LogAnomaly]:
    """Sorts by original position and flags low-confidence anomalies (edge case:
    an anomaly found in the first N lines has too little surrounding context)."""
    anomalies.sort(key=lambda pair: pair[0])
    return [
        replace(anomaly, low_confidence=True)
        if index <= _cfg.low_confidence_line_window
        else anomaly
        for index, anomaly in anomalies
    ]

mutants_x__finalize_anomalies__mutmut['_mutmut_orig'] = x__finalize_anomalies__mutmut_orig # type: ignore # mutmut generated
mutants_x__finalize_anomalies__mutmut['x__finalize_anomalies__mutmut_1'] = x__finalize_anomalies__mutmut_1 # type: ignore # mutmut generated
mutants_x__finalize_anomalies__mutmut['x__finalize_anomalies__mutmut_2'] = x__finalize_anomalies__mutmut_2 # type: ignore # mutmut generated
mutants_x__finalize_anomalies__mutmut['x__finalize_anomalies__mutmut_3'] = x__finalize_anomalies__mutmut_3 # type: ignore # mutmut generated
mutants_x__finalize_anomalies__mutmut['x__finalize_anomalies__mutmut_4'] = x__finalize_anomalies__mutmut_4 # type: ignore # mutmut generated
mutants_x__finalize_anomalies__mutmut['x__finalize_anomalies__mutmut_5'] = x__finalize_anomalies__mutmut_5 # type: ignore # mutmut generated
mutants_x__finalize_anomalies__mutmut['x__finalize_anomalies__mutmut_6'] = x__finalize_anomalies__mutmut_6 # type: ignore # mutmut generated
mutants_x__finalize_anomalies__mutmut['x__finalize_anomalies__mutmut_7'] = x__finalize_anomalies__mutmut_7 # type: ignore # mutmut generated
mutants_x__finalize_anomalies__mutmut['x__finalize_anomalies__mutmut_8'] = x__finalize_anomalies__mutmut_8 # type: ignore # mutmut generated
mutants_x__finalize_anomalies__mutmut['x__finalize_anomalies__mutmut_9'] = x__finalize_anomalies__mutmut_9 # type: ignore # mutmut generated
