from __future__ import annotations

import statistics

from hexawyn.application.ports.driven.pod_metrics_baseline_port import PodMetricsRawData
from hexawyn.domain.models.constants import PodAnomalyDetectionConstants
from hexawyn.domain.models.event import EventSeverity
from hexawyn.domain.models.pod_anomaly import (
    DetectionMethod,
    ExcludedPod,
    PodAnomaly,
    PodAnomalyDetectionReport,
    PodMetric,
)
from hexawyn.domain.services.anomaly_detection.ml import IsolationForestAnomalyDetector
from hexawyn.domain.services.anomaly_detection.statistical import ZScoreAnomalyDetector

_cfg = PodAnomalyDetectionConstants()

_METRICS: tuple[PodMetric, ...] = ("cpu", "memory", "error_rate")

_SEVERITY_RANK: dict[EventSeverity, int] = {
    EventSeverity.CRITICAL: 0,
    EventSeverity.HIGH: 1,
    EventSeverity.MEDIUM: 2,
    EventSeverity.LOW: 3,
}

AnomalyPoint = dict[str, float | int | str]


def detect_pod_anomalies(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", total_pods=0, summary="No pods found.")

    namespace = raw_data[0]["namespace"]
    total_pods = len(raw_data)

    eligible, excluded = _partition_by_age(raw_data)

    anomalies: list[PodAnomaly] = []
    for pod in eligible:
        for metric in _METRICS:
            anomaly = _detect_metric_anomaly(pod, metric)
            if anomaly is not None:
                anomalies.append(anomaly)

    anomalies.sort(key=lambda a: (_SEVERITY_RANK[a.severity], -a.deviation_pct))

    return PodAnomalyDetectionReport(
        namespace=namespace,
        total_pods=total_pods,
        anomalies=anomalies,
        excluded_pods=excluded,
        summary=_summary(anomalies, excluded),
    )


def _partition_by_age(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["pod_age_hours"] < _cfg.min_pod_age_hours_for_baseline:
            excluded.append(
                ExcludedPod(
                    pod_name=pod["pod_name"],
                    namespace=pod["namespace"],
                    reason=(
                        f"no baseline: pod age {pod['pod_age_hours']:.1f}h < "
                        f"required {_cfg.min_pod_age_hours_for_baseline:.0f}h"
                    ),
                )
            )
            continue
        eligible.append(pod)
    return eligible, excluded


def _baseline_and_current(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def _detect_metric_anomaly(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, len(series) - 1)

    iforest = IsolationForestAnomalyDetector(
        contamination=_cfg.isolation_forest_contamination,
        random_state=_cfg.isolation_forest_random_state,
        min_samples=_cfg.isolation_forest_min_samples,
        min_score_deviation=_cfg.isolation_forest_min_score_deviation,
    )
    iforest_result = iforest.detect_series(series)
    recent_start = max(0, len(series) - int(_cfg.recent_window_hours) - 1)
    iforest_hit = _strongest_hit_from(iforest_result.anomalies, recent_start)

    if z_hit is None and iforest_hit is None:
        return None

    z_score_value = float(z_hit["z_score"]) if z_hit is not None else None
    iforest_score_value = float(iforest_hit["anomaly_score"]) if iforest_hit is not None else None

    detection_method: DetectionMethod
    if z_hit is not None:
        severity = _severity_from_zscore(z_score_value or 0.0)
        detection_method = "both" if iforest_hit is not None else "zscore"
    else:
        severity = EventSeverity.MEDIUM
        detection_method = "isolation_forest"

    baseline_mean = statistics.mean(baseline) if baseline else current
    deviation_pct = ((current - baseline_mean) / baseline_mean * 100) if baseline_mean else 0.0

    note = restart_note
    if pod["is_scheduled_batch_job"]:
        severity = EventSeverity.LOW
        note = _append_note(note, "expected spike: scheduled batch/cron job — severity capped")

    return PodAnomaly(
        pod_name=pod["pod_name"],
        namespace=pod["namespace"],
        metric=metric,
        severity=severity,
        deviation_pct=round(deviation_pct, 1),
        z_score=round(z_score_value, 4) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def _effective_baseline(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def _hit_at_index(anomalies: list[AnomalyPoint], index: int) -> AnomalyPoint | None:
    return next((a for a in anomalies if int(a["index"]) == index), None)


def _strongest_hit_from(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) >= start_index]
    if not candidates:
        return None
    return max(candidates, key=lambda a: float(a["anomaly_score"]))


def _severity_from_zscore(z_score: float) -> EventSeverity:
    if z_score >= _cfg.zscore_critical_threshold:
        return EventSeverity.CRITICAL
    if z_score >= _cfg.zscore_high_threshold:
        return EventSeverity.HIGH
    return EventSeverity.MEDIUM


def _append_note(existing: str, addition: str) -> str:
    return f"{existing}; {addition}" if existing else addition


def _summary(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = {}
    for anomaly in anomalies:
        counts[anomaly.severity] = counts.get(anomaly.severity, 0) + 1
    breakdown = ", ".join(
        f"{counts[severity]} {severity.value}"
        for severity in (
            EventSeverity.CRITICAL,
            EventSeverity.HIGH,
            EventSeverity.MEDIUM,
            EventSeverity.LOW,
        )
        if severity in counts
    )
    return f"{len(anomalies)} anomal{plural} detected ({breakdown})"
