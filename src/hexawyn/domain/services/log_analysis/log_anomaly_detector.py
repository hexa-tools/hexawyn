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


def _minute_bucket(timestamp: str) -> str:
    return timestamp[:16]


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


def _group_by_format(indexed_lines: list[_IndexedLine]) -> list[list[_IndexedLine]]:
    """Edge case: log format changes mid-window → each format analyzed separately."""
    groups: dict[bool, list[_IndexedLine]] = defaultdict(list)
    for index, line in indexed_lines:
        groups[line.is_json].append((index, line))
    return [group for group in groups.values() if group]


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
