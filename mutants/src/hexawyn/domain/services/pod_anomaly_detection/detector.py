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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_pod_anomalies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_pod_anomalies__mutmut)
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


def x_detect_pod_anomalies__mutmut_orig(
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


def x_detect_pod_anomalies__mutmut_1(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if raw_data:
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


def x_detect_pod_anomalies__mutmut_2(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace=None, total_pods=0, summary="No pods found.")

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


def x_detect_pod_anomalies__mutmut_3(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", total_pods=None, summary="No pods found.")

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


def x_detect_pod_anomalies__mutmut_4(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", total_pods=0, summary=None)

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


def x_detect_pod_anomalies__mutmut_5(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(total_pods=0, summary="No pods found.")

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


def x_detect_pod_anomalies__mutmut_6(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", summary="No pods found.")

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


def x_detect_pod_anomalies__mutmut_7(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", total_pods=0, )

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


def x_detect_pod_anomalies__mutmut_8(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="XXXX", total_pods=0, summary="No pods found.")

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


def x_detect_pod_anomalies__mutmut_9(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", total_pods=1, summary="No pods found.")

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


def x_detect_pod_anomalies__mutmut_10(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", total_pods=0, summary="XXNo pods found.XX")

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


def x_detect_pod_anomalies__mutmut_11(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", total_pods=0, summary="no pods found.")

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


def x_detect_pod_anomalies__mutmut_12(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", total_pods=0, summary="NO PODS FOUND.")

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


def x_detect_pod_anomalies__mutmut_13(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", total_pods=0, summary="No pods found.")

    namespace = None
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


def x_detect_pod_anomalies__mutmut_14(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", total_pods=0, summary="No pods found.")

    namespace = raw_data[1]["namespace"]
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


def x_detect_pod_anomalies__mutmut_15(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", total_pods=0, summary="No pods found.")

    namespace = raw_data[0]["XXnamespaceXX"]
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


def x_detect_pod_anomalies__mutmut_16(
    raw_data: list[PodMetricsRawData], baseline_window_days: int
) -> PodAnomalyDetectionReport:
    """Compares each pod's current CPU/memory/error-rate to its own baseline
    using Z-score (sharp deviation) + Isolation Forest (gradual drift) dual
    detection. Pure domain function — raw_data is already fetched through
    PodMetricsBaselinePort.
    """
    if not raw_data:
        return PodAnomalyDetectionReport(namespace="", total_pods=0, summary="No pods found.")

    namespace = raw_data[0]["NAMESPACE"]
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


def x_detect_pod_anomalies__mutmut_17(
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
    total_pods = None

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


def x_detect_pod_anomalies__mutmut_18(
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

    eligible, excluded = None

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


def x_detect_pod_anomalies__mutmut_19(
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

    eligible, excluded = _partition_by_age(None)

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


def x_detect_pod_anomalies__mutmut_20(
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

    anomalies: list[PodAnomaly] = None
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


def x_detect_pod_anomalies__mutmut_21(
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
            anomaly = None
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


def x_detect_pod_anomalies__mutmut_22(
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
            anomaly = _detect_metric_anomaly(None, metric)
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


def x_detect_pod_anomalies__mutmut_23(
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
            anomaly = _detect_metric_anomaly(pod, None)
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


def x_detect_pod_anomalies__mutmut_24(
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
            anomaly = _detect_metric_anomaly(metric)
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


def x_detect_pod_anomalies__mutmut_25(
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
            anomaly = _detect_metric_anomaly(pod, )
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


def x_detect_pod_anomalies__mutmut_26(
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
            if anomaly is None:
                anomalies.append(anomaly)

    anomalies.sort(key=lambda a: (_SEVERITY_RANK[a.severity], -a.deviation_pct))

    return PodAnomalyDetectionReport(
        namespace=namespace,
        total_pods=total_pods,
        anomalies=anomalies,
        excluded_pods=excluded,
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_27(
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
                anomalies.append(None)

    anomalies.sort(key=lambda a: (_SEVERITY_RANK[a.severity], -a.deviation_pct))

    return PodAnomalyDetectionReport(
        namespace=namespace,
        total_pods=total_pods,
        anomalies=anomalies,
        excluded_pods=excluded,
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_28(
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

    anomalies.sort(key=None)

    return PodAnomalyDetectionReport(
        namespace=namespace,
        total_pods=total_pods,
        anomalies=anomalies,
        excluded_pods=excluded,
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_29(
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

    anomalies.sort(key=lambda a: None)

    return PodAnomalyDetectionReport(
        namespace=namespace,
        total_pods=total_pods,
        anomalies=anomalies,
        excluded_pods=excluded,
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_30(
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

    anomalies.sort(key=lambda a: (_SEVERITY_RANK[a.severity], +a.deviation_pct))

    return PodAnomalyDetectionReport(
        namespace=namespace,
        total_pods=total_pods,
        anomalies=anomalies,
        excluded_pods=excluded,
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_31(
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
        namespace=None,
        total_pods=total_pods,
        anomalies=anomalies,
        excluded_pods=excluded,
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_32(
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
        total_pods=None,
        anomalies=anomalies,
        excluded_pods=excluded,
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_33(
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
        anomalies=None,
        excluded_pods=excluded,
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_34(
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
        excluded_pods=None,
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_35(
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
        summary=None,
    )


def x_detect_pod_anomalies__mutmut_36(
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
        total_pods=total_pods,
        anomalies=anomalies,
        excluded_pods=excluded,
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_37(
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
        anomalies=anomalies,
        excluded_pods=excluded,
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_38(
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
        excluded_pods=excluded,
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_39(
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
        summary=_summary(anomalies, excluded),
    )


def x_detect_pod_anomalies__mutmut_40(
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
        )


def x_detect_pod_anomalies__mutmut_41(
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
        summary=_summary(None, excluded),
    )


def x_detect_pod_anomalies__mutmut_42(
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
        summary=_summary(anomalies, None),
    )


def x_detect_pod_anomalies__mutmut_43(
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
        summary=_summary(excluded),
    )


def x_detect_pod_anomalies__mutmut_44(
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
        summary=_summary(anomalies, ),
    )

mutants_x_detect_pod_anomalies__mutmut['_mutmut_orig'] = x_detect_pod_anomalies__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_1'] = x_detect_pod_anomalies__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_2'] = x_detect_pod_anomalies__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_3'] = x_detect_pod_anomalies__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_4'] = x_detect_pod_anomalies__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_5'] = x_detect_pod_anomalies__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_6'] = x_detect_pod_anomalies__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_7'] = x_detect_pod_anomalies__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_8'] = x_detect_pod_anomalies__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_9'] = x_detect_pod_anomalies__mutmut_9 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_10'] = x_detect_pod_anomalies__mutmut_10 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_11'] = x_detect_pod_anomalies__mutmut_11 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_12'] = x_detect_pod_anomalies__mutmut_12 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_13'] = x_detect_pod_anomalies__mutmut_13 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_14'] = x_detect_pod_anomalies__mutmut_14 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_15'] = x_detect_pod_anomalies__mutmut_15 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_16'] = x_detect_pod_anomalies__mutmut_16 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_17'] = x_detect_pod_anomalies__mutmut_17 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_18'] = x_detect_pod_anomalies__mutmut_18 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_19'] = x_detect_pod_anomalies__mutmut_19 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_20'] = x_detect_pod_anomalies__mutmut_20 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_21'] = x_detect_pod_anomalies__mutmut_21 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_22'] = x_detect_pod_anomalies__mutmut_22 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_23'] = x_detect_pod_anomalies__mutmut_23 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_24'] = x_detect_pod_anomalies__mutmut_24 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_25'] = x_detect_pod_anomalies__mutmut_25 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_26'] = x_detect_pod_anomalies__mutmut_26 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_27'] = x_detect_pod_anomalies__mutmut_27 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_28'] = x_detect_pod_anomalies__mutmut_28 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_29'] = x_detect_pod_anomalies__mutmut_29 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_30'] = x_detect_pod_anomalies__mutmut_30 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_31'] = x_detect_pod_anomalies__mutmut_31 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_32'] = x_detect_pod_anomalies__mutmut_32 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_33'] = x_detect_pod_anomalies__mutmut_33 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_34'] = x_detect_pod_anomalies__mutmut_34 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_35'] = x_detect_pod_anomalies__mutmut_35 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_36'] = x_detect_pod_anomalies__mutmut_36 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_37'] = x_detect_pod_anomalies__mutmut_37 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_38'] = x_detect_pod_anomalies__mutmut_38 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_39'] = x_detect_pod_anomalies__mutmut_39 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_40'] = x_detect_pod_anomalies__mutmut_40 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_41'] = x_detect_pod_anomalies__mutmut_41 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_42'] = x_detect_pod_anomalies__mutmut_42 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_43'] = x_detect_pod_anomalies__mutmut_43 # type: ignore # mutmut generated
mutants_x_detect_pod_anomalies__mutmut['x_detect_pod_anomalies__mutmut_44'] = x_detect_pod_anomalies__mutmut_44 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__partition_by_age__mutmut)
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


def x__partition_by_age__mutmut_orig(
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


def x__partition_by_age__mutmut_1(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = None
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


def x__partition_by_age__mutmut_2(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = None
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


def x__partition_by_age__mutmut_3(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["XXpod_age_hoursXX"] < _cfg.min_pod_age_hours_for_baseline:
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


def x__partition_by_age__mutmut_4(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["POD_AGE_HOURS"] < _cfg.min_pod_age_hours_for_baseline:
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


def x__partition_by_age__mutmut_5(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["pod_age_hours"] <= _cfg.min_pod_age_hours_for_baseline:
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


def x__partition_by_age__mutmut_6(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["pod_age_hours"] < _cfg.min_pod_age_hours_for_baseline:
            excluded.append(
                None
            )
            continue
        eligible.append(pod)
    return eligible, excluded


def x__partition_by_age__mutmut_7(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["pod_age_hours"] < _cfg.min_pod_age_hours_for_baseline:
            excluded.append(
                ExcludedPod(
                    pod_name=None,
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


def x__partition_by_age__mutmut_8(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["pod_age_hours"] < _cfg.min_pod_age_hours_for_baseline:
            excluded.append(
                ExcludedPod(
                    pod_name=pod["pod_name"],
                    namespace=None,
                    reason=(
                        f"no baseline: pod age {pod['pod_age_hours']:.1f}h < "
                        f"required {_cfg.min_pod_age_hours_for_baseline:.0f}h"
                    ),
                )
            )
            continue
        eligible.append(pod)
    return eligible, excluded


def x__partition_by_age__mutmut_9(
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
                    reason=None,
                )
            )
            continue
        eligible.append(pod)
    return eligible, excluded


def x__partition_by_age__mutmut_10(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["pod_age_hours"] < _cfg.min_pod_age_hours_for_baseline:
            excluded.append(
                ExcludedPod(
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


def x__partition_by_age__mutmut_11(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["pod_age_hours"] < _cfg.min_pod_age_hours_for_baseline:
            excluded.append(
                ExcludedPod(
                    pod_name=pod["pod_name"],
                    reason=(
                        f"no baseline: pod age {pod['pod_age_hours']:.1f}h < "
                        f"required {_cfg.min_pod_age_hours_for_baseline:.0f}h"
                    ),
                )
            )
            continue
        eligible.append(pod)
    return eligible, excluded


def x__partition_by_age__mutmut_12(
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
                    )
            )
            continue
        eligible.append(pod)
    return eligible, excluded


def x__partition_by_age__mutmut_13(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["pod_age_hours"] < _cfg.min_pod_age_hours_for_baseline:
            excluded.append(
                ExcludedPod(
                    pod_name=pod["XXpod_nameXX"],
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


def x__partition_by_age__mutmut_14(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["pod_age_hours"] < _cfg.min_pod_age_hours_for_baseline:
            excluded.append(
                ExcludedPod(
                    pod_name=pod["POD_NAME"],
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


def x__partition_by_age__mutmut_15(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["pod_age_hours"] < _cfg.min_pod_age_hours_for_baseline:
            excluded.append(
                ExcludedPod(
                    pod_name=pod["pod_name"],
                    namespace=pod["XXnamespaceXX"],
                    reason=(
                        f"no baseline: pod age {pod['pod_age_hours']:.1f}h < "
                        f"required {_cfg.min_pod_age_hours_for_baseline:.0f}h"
                    ),
                )
            )
            continue
        eligible.append(pod)
    return eligible, excluded


def x__partition_by_age__mutmut_16(
    raw_data: list[PodMetricsRawData],
) -> tuple[list[PodMetricsRawData], list[ExcludedPod]]:
    eligible: list[PodMetricsRawData] = []
    excluded: list[ExcludedPod] = []
    for pod in raw_data:
        if pod["pod_age_hours"] < _cfg.min_pod_age_hours_for_baseline:
            excluded.append(
                ExcludedPod(
                    pod_name=pod["pod_name"],
                    namespace=pod["NAMESPACE"],
                    reason=(
                        f"no baseline: pod age {pod['pod_age_hours']:.1f}h < "
                        f"required {_cfg.min_pod_age_hours_for_baseline:.0f}h"
                    ),
                )
            )
            continue
        eligible.append(pod)
    return eligible, excluded


def x__partition_by_age__mutmut_17(
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
                        f"no baseline: pod age {pod['XXpod_age_hoursXX']:.1f}h < "
                        f"required {_cfg.min_pod_age_hours_for_baseline:.0f}h"
                    ),
                )
            )
            continue
        eligible.append(pod)
    return eligible, excluded


def x__partition_by_age__mutmut_18(
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
                        f"no baseline: pod age {pod['POD_AGE_HOURS']:.1f}h < "
                        f"required {_cfg.min_pod_age_hours_for_baseline:.0f}h"
                    ),
                )
            )
            continue
        eligible.append(pod)
    return eligible, excluded


def x__partition_by_age__mutmut_19(
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
            break
        eligible.append(pod)
    return eligible, excluded


def x__partition_by_age__mutmut_20(
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
        eligible.append(None)
    return eligible, excluded

mutants_x__partition_by_age__mutmut['_mutmut_orig'] = x__partition_by_age__mutmut_orig # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_1'] = x__partition_by_age__mutmut_1 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_2'] = x__partition_by_age__mutmut_2 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_3'] = x__partition_by_age__mutmut_3 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_4'] = x__partition_by_age__mutmut_4 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_5'] = x__partition_by_age__mutmut_5 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_6'] = x__partition_by_age__mutmut_6 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_7'] = x__partition_by_age__mutmut_7 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_8'] = x__partition_by_age__mutmut_8 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_9'] = x__partition_by_age__mutmut_9 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_10'] = x__partition_by_age__mutmut_10 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_11'] = x__partition_by_age__mutmut_11 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_12'] = x__partition_by_age__mutmut_12 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_13'] = x__partition_by_age__mutmut_13 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_14'] = x__partition_by_age__mutmut_14 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_15'] = x__partition_by_age__mutmut_15 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_16'] = x__partition_by_age__mutmut_16 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_17'] = x__partition_by_age__mutmut_17 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_18'] = x__partition_by_age__mutmut_18 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_19'] = x__partition_by_age__mutmut_19 # type: ignore # mutmut generated
mutants_x__partition_by_age__mutmut['x__partition_by_age__mutmut_20'] = x__partition_by_age__mutmut_20 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__baseline_and_current__mutmut)
def _baseline_and_current(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_orig(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_1(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric != "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_2(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "XXcpuXX":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_3(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "CPU":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_4(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["XXcpu_baseline_millicoresXX"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_5(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["CPU_BASELINE_MILLICORES"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_6(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["XXcpu_current_millicoresXX"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_7(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["CPU_CURRENT_MILLICORES"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_8(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric != "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_9(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "XXmemoryXX":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_10(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "MEMORY":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_11(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["XXmemory_baseline_bytesXX"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_12(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["MEMORY_BASELINE_BYTES"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_13(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["XXmemory_current_bytesXX"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_14(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["MEMORY_CURRENT_BYTES"]
    return pod["error_rate_baseline_pct"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_15(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["XXerror_rate_baseline_pctXX"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_16(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["ERROR_RATE_BASELINE_PCT"], pod["error_rate_current_pct"]


def x__baseline_and_current__mutmut_17(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["XXerror_rate_current_pctXX"]


def x__baseline_and_current__mutmut_18(pod: PodMetricsRawData, metric: PodMetric) -> tuple[list[float], float]:
    if metric == "cpu":
        return pod["cpu_baseline_millicores"], pod["cpu_current_millicores"]
    if metric == "memory":
        return pod["memory_baseline_bytes"], pod["memory_current_bytes"]
    return pod["error_rate_baseline_pct"], pod["ERROR_RATE_CURRENT_PCT"]

mutants_x__baseline_and_current__mutmut['_mutmut_orig'] = x__baseline_and_current__mutmut_orig # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_1'] = x__baseline_and_current__mutmut_1 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_2'] = x__baseline_and_current__mutmut_2 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_3'] = x__baseline_and_current__mutmut_3 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_4'] = x__baseline_and_current__mutmut_4 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_5'] = x__baseline_and_current__mutmut_5 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_6'] = x__baseline_and_current__mutmut_6 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_7'] = x__baseline_and_current__mutmut_7 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_8'] = x__baseline_and_current__mutmut_8 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_9'] = x__baseline_and_current__mutmut_9 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_10'] = x__baseline_and_current__mutmut_10 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_11'] = x__baseline_and_current__mutmut_11 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_12'] = x__baseline_and_current__mutmut_12 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_13'] = x__baseline_and_current__mutmut_13 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_14'] = x__baseline_and_current__mutmut_14 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_15'] = x__baseline_and_current__mutmut_15 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_16'] = x__baseline_and_current__mutmut_16 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_17'] = x__baseline_and_current__mutmut_17 # type: ignore # mutmut generated
mutants_x__baseline_and_current__mutmut['x__baseline_and_current__mutmut_18'] = x__baseline_and_current__mutmut_18 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_metric_anomaly__mutmut)
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


def x__detect_metric_anomaly__mutmut_orig(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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


def x__detect_metric_anomaly__mutmut_1(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = None
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


def x__detect_metric_anomaly__mutmut_2(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(None, metric)
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


def x__detect_metric_anomaly__mutmut_3(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, None)
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


def x__detect_metric_anomaly__mutmut_4(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(metric)
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


def x__detect_metric_anomaly__mutmut_5(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, )
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


def x__detect_metric_anomaly__mutmut_6(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = None
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


def x__detect_metric_anomaly__mutmut_7(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(None, raw_baseline)
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


def x__detect_metric_anomaly__mutmut_8(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, None)
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


def x__detect_metric_anomaly__mutmut_9(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(raw_baseline)
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


def x__detect_metric_anomaly__mutmut_10(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, )
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


def x__detect_metric_anomaly__mutmut_11(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = None

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


def x__detect_metric_anomaly__mutmut_12(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = None
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


def x__detect_metric_anomaly__mutmut_13(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(None)
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


def x__detect_metric_anomaly__mutmut_14(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=None).detect(series)
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


def x__detect_metric_anomaly__mutmut_15(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = None

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


def x__detect_metric_anomaly__mutmut_16(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(None, len(series) - 1)

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


def x__detect_metric_anomaly__mutmut_17(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, None)

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


def x__detect_metric_anomaly__mutmut_18(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(len(series) - 1)

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


def x__detect_metric_anomaly__mutmut_19(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, )

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


def x__detect_metric_anomaly__mutmut_20(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, len(series) + 1)

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


def x__detect_metric_anomaly__mutmut_21(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, len(series) - 2)

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


def x__detect_metric_anomaly__mutmut_22(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, len(series) - 1)

    iforest = None
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


def x__detect_metric_anomaly__mutmut_23(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, len(series) - 1)

    iforest = IsolationForestAnomalyDetector(
        contamination=None,
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


def x__detect_metric_anomaly__mutmut_24(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, len(series) - 1)

    iforest = IsolationForestAnomalyDetector(
        contamination=_cfg.isolation_forest_contamination,
        random_state=None,
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


def x__detect_metric_anomaly__mutmut_25(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, len(series) - 1)

    iforest = IsolationForestAnomalyDetector(
        contamination=_cfg.isolation_forest_contamination,
        random_state=_cfg.isolation_forest_random_state,
        min_samples=None,
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


def x__detect_metric_anomaly__mutmut_26(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, len(series) - 1)

    iforest = IsolationForestAnomalyDetector(
        contamination=_cfg.isolation_forest_contamination,
        random_state=_cfg.isolation_forest_random_state,
        min_samples=_cfg.isolation_forest_min_samples,
        min_score_deviation=None,
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


def x__detect_metric_anomaly__mutmut_27(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, len(series) - 1)

    iforest = IsolationForestAnomalyDetector(
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


def x__detect_metric_anomaly__mutmut_28(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, len(series) - 1)

    iforest = IsolationForestAnomalyDetector(
        contamination=_cfg.isolation_forest_contamination,
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


def x__detect_metric_anomaly__mutmut_29(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, len(series) - 1)

    iforest = IsolationForestAnomalyDetector(
        contamination=_cfg.isolation_forest_contamination,
        random_state=_cfg.isolation_forest_random_state,
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


def x__detect_metric_anomaly__mutmut_30(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
    raw_baseline, current = _baseline_and_current(pod, metric)
    baseline, restart_note = _effective_baseline(pod, raw_baseline)
    series = [*baseline, current]

    zscore_result = ZScoreAnomalyDetector(threshold=_cfg.zscore_threshold).detect(series)
    z_hit = _hit_at_index(zscore_result.anomalies, len(series) - 1)

    iforest = IsolationForestAnomalyDetector(
        contamination=_cfg.isolation_forest_contamination,
        random_state=_cfg.isolation_forest_random_state,
        min_samples=_cfg.isolation_forest_min_samples,
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


def x__detect_metric_anomaly__mutmut_31(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    iforest_result = None
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


def x__detect_metric_anomaly__mutmut_32(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    iforest_result = iforest.detect_series(None)
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


def x__detect_metric_anomaly__mutmut_33(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    recent_start = None
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


def x__detect_metric_anomaly__mutmut_34(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    recent_start = max(None, len(series) - int(_cfg.recent_window_hours) - 1)
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


def x__detect_metric_anomaly__mutmut_35(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    recent_start = max(0, None)
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


def x__detect_metric_anomaly__mutmut_36(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    recent_start = max(len(series) - int(_cfg.recent_window_hours) - 1)
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


def x__detect_metric_anomaly__mutmut_37(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    recent_start = max(0, )
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


def x__detect_metric_anomaly__mutmut_38(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    recent_start = max(1, len(series) - int(_cfg.recent_window_hours) - 1)
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


def x__detect_metric_anomaly__mutmut_39(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    recent_start = max(0, len(series) - int(_cfg.recent_window_hours) + 1)
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


def x__detect_metric_anomaly__mutmut_40(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    recent_start = max(0, len(series) + int(_cfg.recent_window_hours) - 1)
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


def x__detect_metric_anomaly__mutmut_41(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    recent_start = max(0, len(series) - int(None) - 1)
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


def x__detect_metric_anomaly__mutmut_42(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    recent_start = max(0, len(series) - int(_cfg.recent_window_hours) - 2)
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


def x__detect_metric_anomaly__mutmut_43(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    iforest_hit = None

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


def x__detect_metric_anomaly__mutmut_44(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    iforest_hit = _strongest_hit_from(None, recent_start)

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


def x__detect_metric_anomaly__mutmut_45(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    iforest_hit = _strongest_hit_from(iforest_result.anomalies, None)

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


def x__detect_metric_anomaly__mutmut_46(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    iforest_hit = _strongest_hit_from(recent_start)

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


def x__detect_metric_anomaly__mutmut_47(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    iforest_hit = _strongest_hit_from(iforest_result.anomalies, )

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


def x__detect_metric_anomaly__mutmut_48(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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

    if z_hit is None or iforest_hit is None:
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


def x__detect_metric_anomaly__mutmut_49(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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

    if z_hit is not None and iforest_hit is None:
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


def x__detect_metric_anomaly__mutmut_50(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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

    if z_hit is None and iforest_hit is not None:
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


def x__detect_metric_anomaly__mutmut_51(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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

    z_score_value = None
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


def x__detect_metric_anomaly__mutmut_52(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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

    z_score_value = float(None) if z_hit is not None else None
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


def x__detect_metric_anomaly__mutmut_53(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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

    z_score_value = float(z_hit["XXz_scoreXX"]) if z_hit is not None else None
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


def x__detect_metric_anomaly__mutmut_54(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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

    z_score_value = float(z_hit["Z_SCORE"]) if z_hit is not None else None
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


def x__detect_metric_anomaly__mutmut_55(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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

    z_score_value = float(z_hit["z_score"]) if z_hit is None else None
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


def x__detect_metric_anomaly__mutmut_56(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    iforest_score_value = None

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


def x__detect_metric_anomaly__mutmut_57(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    iforest_score_value = float(None) if iforest_hit is not None else None

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


def x__detect_metric_anomaly__mutmut_58(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    iforest_score_value = float(iforest_hit["XXanomaly_scoreXX"]) if iforest_hit is not None else None

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


def x__detect_metric_anomaly__mutmut_59(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    iforest_score_value = float(iforest_hit["ANOMALY_SCORE"]) if iforest_hit is not None else None

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


def x__detect_metric_anomaly__mutmut_60(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    iforest_score_value = float(iforest_hit["anomaly_score"]) if iforest_hit is None else None

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


def x__detect_metric_anomaly__mutmut_61(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    if z_hit is None:
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


def x__detect_metric_anomaly__mutmut_62(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        severity = None
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


def x__detect_metric_anomaly__mutmut_63(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        severity = _severity_from_zscore(None)
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


def x__detect_metric_anomaly__mutmut_64(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        severity = _severity_from_zscore(z_score_value and 0.0)
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


def x__detect_metric_anomaly__mutmut_65(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        severity = _severity_from_zscore(z_score_value or 1.0)
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


def x__detect_metric_anomaly__mutmut_66(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        detection_method = None
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


def x__detect_metric_anomaly__mutmut_67(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        detection_method = "XXbothXX" if iforest_hit is not None else "zscore"
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


def x__detect_metric_anomaly__mutmut_68(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        detection_method = "BOTH" if iforest_hit is not None else "zscore"
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


def x__detect_metric_anomaly__mutmut_69(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        detection_method = "both" if iforest_hit is None else "zscore"
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


def x__detect_metric_anomaly__mutmut_70(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        detection_method = "both" if iforest_hit is not None else "XXzscoreXX"
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


def x__detect_metric_anomaly__mutmut_71(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        detection_method = "both" if iforest_hit is not None else "ZSCORE"
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


def x__detect_metric_anomaly__mutmut_72(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        severity = None
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


def x__detect_metric_anomaly__mutmut_73(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        detection_method = None

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


def x__detect_metric_anomaly__mutmut_74(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        detection_method = "XXisolation_forestXX"

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


def x__detect_metric_anomaly__mutmut_75(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        detection_method = "ISOLATION_FOREST"

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


def x__detect_metric_anomaly__mutmut_76(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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

    baseline_mean = None
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


def x__detect_metric_anomaly__mutmut_77(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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

    baseline_mean = statistics.mean(None) if baseline else current
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


def x__detect_metric_anomaly__mutmut_78(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    deviation_pct = None

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


def x__detect_metric_anomaly__mutmut_79(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    deviation_pct = ((current - baseline_mean) / baseline_mean / 100) if baseline_mean else 0.0

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


def x__detect_metric_anomaly__mutmut_80(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    deviation_pct = ((current - baseline_mean) * baseline_mean * 100) if baseline_mean else 0.0

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


def x__detect_metric_anomaly__mutmut_81(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    deviation_pct = ((current + baseline_mean) / baseline_mean * 100) if baseline_mean else 0.0

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


def x__detect_metric_anomaly__mutmut_82(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    deviation_pct = ((current - baseline_mean) / baseline_mean * 101) if baseline_mean else 0.0

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


def x__detect_metric_anomaly__mutmut_83(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    deviation_pct = ((current - baseline_mean) / baseline_mean * 100) if baseline_mean else 1.0

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


def x__detect_metric_anomaly__mutmut_84(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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

    note = None
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


def x__detect_metric_anomaly__mutmut_85(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    if pod["XXis_scheduled_batch_jobXX"]:
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


def x__detect_metric_anomaly__mutmut_86(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
    if pod["IS_SCHEDULED_BATCH_JOB"]:
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


def x__detect_metric_anomaly__mutmut_87(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        severity = None
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


def x__detect_metric_anomaly__mutmut_88(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        note = None

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


def x__detect_metric_anomaly__mutmut_89(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        note = _append_note(None, "expected spike: scheduled batch/cron job — severity capped")

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


def x__detect_metric_anomaly__mutmut_90(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        note = _append_note(note, None)

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


def x__detect_metric_anomaly__mutmut_91(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        note = _append_note("expected spike: scheduled batch/cron job — severity capped")

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


def x__detect_metric_anomaly__mutmut_92(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        note = _append_note(note, )

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


def x__detect_metric_anomaly__mutmut_93(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        note = _append_note(note, "XXexpected spike: scheduled batch/cron job — severity cappedXX")

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


def x__detect_metric_anomaly__mutmut_94(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        note = _append_note(note, "EXPECTED SPIKE: SCHEDULED BATCH/CRON JOB — SEVERITY CAPPED")

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


def x__detect_metric_anomaly__mutmut_95(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        pod_name=None,
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


def x__detect_metric_anomaly__mutmut_96(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        namespace=None,
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


def x__detect_metric_anomaly__mutmut_97(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        metric=None,
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


def x__detect_metric_anomaly__mutmut_98(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        severity=None,
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


def x__detect_metric_anomaly__mutmut_99(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        deviation_pct=None,
        z_score=round(z_score_value, 4) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_100(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        z_score=None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_101(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        isolation_forest_score=None,
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_102(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        detection_method=None,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_103(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        current_value=None,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_104(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        baseline_mean=None,
        note=note,
    )


def x__detect_metric_anomaly__mutmut_105(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        note=None,
    )


def x__detect_metric_anomaly__mutmut_106(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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


def x__detect_metric_anomaly__mutmut_107(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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


def x__detect_metric_anomaly__mutmut_108(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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


def x__detect_metric_anomaly__mutmut_109(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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


def x__detect_metric_anomaly__mutmut_110(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        z_score=round(z_score_value, 4) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_111(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_112(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_113(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_114(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_115(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        note=note,
    )


def x__detect_metric_anomaly__mutmut_116(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        )


def x__detect_metric_anomaly__mutmut_117(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        pod_name=pod["XXpod_nameXX"],
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


def x__detect_metric_anomaly__mutmut_118(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        pod_name=pod["POD_NAME"],
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


def x__detect_metric_anomaly__mutmut_119(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        namespace=pod["XXnamespaceXX"],
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


def x__detect_metric_anomaly__mutmut_120(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        namespace=pod["NAMESPACE"],
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


def x__detect_metric_anomaly__mutmut_121(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        deviation_pct=round(None, 1),
        z_score=round(z_score_value, 4) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_122(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        deviation_pct=round(deviation_pct, None),
        z_score=round(z_score_value, 4) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_123(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        deviation_pct=round(1),
        z_score=round(z_score_value, 4) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_124(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        deviation_pct=round(deviation_pct, ),
        z_score=round(z_score_value, 4) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_125(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        deviation_pct=round(deviation_pct, 2),
        z_score=round(z_score_value, 4) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_126(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        z_score=round(None, 4) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_127(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        z_score=round(z_score_value, None) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_128(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        z_score=round(4) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_129(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        z_score=round(z_score_value, ) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_130(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        z_score=round(z_score_value, 5) if z_score_value is not None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_131(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        z_score=round(z_score_value, 4) if z_score_value is None else None,
        isolation_forest_score=(
            round(iforest_score_value, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_132(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
            round(None, 4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_133(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
            round(iforest_score_value, None) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_134(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
            round(4) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_135(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
            round(iforest_score_value, ) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_136(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
            round(iforest_score_value, 5) if iforest_score_value is not None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_137(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
            round(iforest_score_value, 4) if iforest_score_value is None else None
        ),
        detection_method=detection_method,
        current_value=current,
        baseline_mean=round(baseline_mean, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_138(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        baseline_mean=round(None, 4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_139(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        baseline_mean=round(baseline_mean, None),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_140(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        baseline_mean=round(4),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_141(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        baseline_mean=round(baseline_mean, ),
        note=note,
    )


def x__detect_metric_anomaly__mutmut_142(pod: PodMetricsRawData, metric: PodMetric) -> PodAnomaly | None:
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
        baseline_mean=round(baseline_mean, 5),
        note=note,
    )

mutants_x__detect_metric_anomaly__mutmut['_mutmut_orig'] = x__detect_metric_anomaly__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_1'] = x__detect_metric_anomaly__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_2'] = x__detect_metric_anomaly__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_3'] = x__detect_metric_anomaly__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_4'] = x__detect_metric_anomaly__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_5'] = x__detect_metric_anomaly__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_6'] = x__detect_metric_anomaly__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_7'] = x__detect_metric_anomaly__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_8'] = x__detect_metric_anomaly__mutmut_8 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_9'] = x__detect_metric_anomaly__mutmut_9 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_10'] = x__detect_metric_anomaly__mutmut_10 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_11'] = x__detect_metric_anomaly__mutmut_11 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_12'] = x__detect_metric_anomaly__mutmut_12 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_13'] = x__detect_metric_anomaly__mutmut_13 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_14'] = x__detect_metric_anomaly__mutmut_14 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_15'] = x__detect_metric_anomaly__mutmut_15 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_16'] = x__detect_metric_anomaly__mutmut_16 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_17'] = x__detect_metric_anomaly__mutmut_17 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_18'] = x__detect_metric_anomaly__mutmut_18 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_19'] = x__detect_metric_anomaly__mutmut_19 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_20'] = x__detect_metric_anomaly__mutmut_20 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_21'] = x__detect_metric_anomaly__mutmut_21 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_22'] = x__detect_metric_anomaly__mutmut_22 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_23'] = x__detect_metric_anomaly__mutmut_23 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_24'] = x__detect_metric_anomaly__mutmut_24 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_25'] = x__detect_metric_anomaly__mutmut_25 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_26'] = x__detect_metric_anomaly__mutmut_26 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_27'] = x__detect_metric_anomaly__mutmut_27 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_28'] = x__detect_metric_anomaly__mutmut_28 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_29'] = x__detect_metric_anomaly__mutmut_29 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_30'] = x__detect_metric_anomaly__mutmut_30 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_31'] = x__detect_metric_anomaly__mutmut_31 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_32'] = x__detect_metric_anomaly__mutmut_32 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_33'] = x__detect_metric_anomaly__mutmut_33 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_34'] = x__detect_metric_anomaly__mutmut_34 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_35'] = x__detect_metric_anomaly__mutmut_35 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_36'] = x__detect_metric_anomaly__mutmut_36 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_37'] = x__detect_metric_anomaly__mutmut_37 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_38'] = x__detect_metric_anomaly__mutmut_38 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_39'] = x__detect_metric_anomaly__mutmut_39 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_40'] = x__detect_metric_anomaly__mutmut_40 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_41'] = x__detect_metric_anomaly__mutmut_41 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_42'] = x__detect_metric_anomaly__mutmut_42 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_43'] = x__detect_metric_anomaly__mutmut_43 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_44'] = x__detect_metric_anomaly__mutmut_44 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_45'] = x__detect_metric_anomaly__mutmut_45 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_46'] = x__detect_metric_anomaly__mutmut_46 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_47'] = x__detect_metric_anomaly__mutmut_47 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_48'] = x__detect_metric_anomaly__mutmut_48 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_49'] = x__detect_metric_anomaly__mutmut_49 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_50'] = x__detect_metric_anomaly__mutmut_50 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_51'] = x__detect_metric_anomaly__mutmut_51 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_52'] = x__detect_metric_anomaly__mutmut_52 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_53'] = x__detect_metric_anomaly__mutmut_53 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_54'] = x__detect_metric_anomaly__mutmut_54 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_55'] = x__detect_metric_anomaly__mutmut_55 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_56'] = x__detect_metric_anomaly__mutmut_56 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_57'] = x__detect_metric_anomaly__mutmut_57 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_58'] = x__detect_metric_anomaly__mutmut_58 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_59'] = x__detect_metric_anomaly__mutmut_59 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_60'] = x__detect_metric_anomaly__mutmut_60 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_61'] = x__detect_metric_anomaly__mutmut_61 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_62'] = x__detect_metric_anomaly__mutmut_62 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_63'] = x__detect_metric_anomaly__mutmut_63 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_64'] = x__detect_metric_anomaly__mutmut_64 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_65'] = x__detect_metric_anomaly__mutmut_65 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_66'] = x__detect_metric_anomaly__mutmut_66 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_67'] = x__detect_metric_anomaly__mutmut_67 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_68'] = x__detect_metric_anomaly__mutmut_68 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_69'] = x__detect_metric_anomaly__mutmut_69 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_70'] = x__detect_metric_anomaly__mutmut_70 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_71'] = x__detect_metric_anomaly__mutmut_71 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_72'] = x__detect_metric_anomaly__mutmut_72 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_73'] = x__detect_metric_anomaly__mutmut_73 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_74'] = x__detect_metric_anomaly__mutmut_74 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_75'] = x__detect_metric_anomaly__mutmut_75 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_76'] = x__detect_metric_anomaly__mutmut_76 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_77'] = x__detect_metric_anomaly__mutmut_77 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_78'] = x__detect_metric_anomaly__mutmut_78 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_79'] = x__detect_metric_anomaly__mutmut_79 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_80'] = x__detect_metric_anomaly__mutmut_80 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_81'] = x__detect_metric_anomaly__mutmut_81 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_82'] = x__detect_metric_anomaly__mutmut_82 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_83'] = x__detect_metric_anomaly__mutmut_83 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_84'] = x__detect_metric_anomaly__mutmut_84 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_85'] = x__detect_metric_anomaly__mutmut_85 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_86'] = x__detect_metric_anomaly__mutmut_86 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_87'] = x__detect_metric_anomaly__mutmut_87 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_88'] = x__detect_metric_anomaly__mutmut_88 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_89'] = x__detect_metric_anomaly__mutmut_89 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_90'] = x__detect_metric_anomaly__mutmut_90 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_91'] = x__detect_metric_anomaly__mutmut_91 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_92'] = x__detect_metric_anomaly__mutmut_92 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_93'] = x__detect_metric_anomaly__mutmut_93 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_94'] = x__detect_metric_anomaly__mutmut_94 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_95'] = x__detect_metric_anomaly__mutmut_95 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_96'] = x__detect_metric_anomaly__mutmut_96 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_97'] = x__detect_metric_anomaly__mutmut_97 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_98'] = x__detect_metric_anomaly__mutmut_98 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_99'] = x__detect_metric_anomaly__mutmut_99 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_100'] = x__detect_metric_anomaly__mutmut_100 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_101'] = x__detect_metric_anomaly__mutmut_101 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_102'] = x__detect_metric_anomaly__mutmut_102 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_103'] = x__detect_metric_anomaly__mutmut_103 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_104'] = x__detect_metric_anomaly__mutmut_104 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_105'] = x__detect_metric_anomaly__mutmut_105 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_106'] = x__detect_metric_anomaly__mutmut_106 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_107'] = x__detect_metric_anomaly__mutmut_107 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_108'] = x__detect_metric_anomaly__mutmut_108 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_109'] = x__detect_metric_anomaly__mutmut_109 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_110'] = x__detect_metric_anomaly__mutmut_110 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_111'] = x__detect_metric_anomaly__mutmut_111 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_112'] = x__detect_metric_anomaly__mutmut_112 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_113'] = x__detect_metric_anomaly__mutmut_113 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_114'] = x__detect_metric_anomaly__mutmut_114 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_115'] = x__detect_metric_anomaly__mutmut_115 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_116'] = x__detect_metric_anomaly__mutmut_116 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_117'] = x__detect_metric_anomaly__mutmut_117 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_118'] = x__detect_metric_anomaly__mutmut_118 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_119'] = x__detect_metric_anomaly__mutmut_119 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_120'] = x__detect_metric_anomaly__mutmut_120 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_121'] = x__detect_metric_anomaly__mutmut_121 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_122'] = x__detect_metric_anomaly__mutmut_122 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_123'] = x__detect_metric_anomaly__mutmut_123 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_124'] = x__detect_metric_anomaly__mutmut_124 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_125'] = x__detect_metric_anomaly__mutmut_125 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_126'] = x__detect_metric_anomaly__mutmut_126 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_127'] = x__detect_metric_anomaly__mutmut_127 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_128'] = x__detect_metric_anomaly__mutmut_128 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_129'] = x__detect_metric_anomaly__mutmut_129 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_130'] = x__detect_metric_anomaly__mutmut_130 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_131'] = x__detect_metric_anomaly__mutmut_131 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_132'] = x__detect_metric_anomaly__mutmut_132 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_133'] = x__detect_metric_anomaly__mutmut_133 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_134'] = x__detect_metric_anomaly__mutmut_134 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_135'] = x__detect_metric_anomaly__mutmut_135 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_136'] = x__detect_metric_anomaly__mutmut_136 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_137'] = x__detect_metric_anomaly__mutmut_137 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_138'] = x__detect_metric_anomaly__mutmut_138 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_139'] = x__detect_metric_anomaly__mutmut_139 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_140'] = x__detect_metric_anomaly__mutmut_140 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_141'] = x__detect_metric_anomaly__mutmut_141 # type: ignore # mutmut generated
mutants_x__detect_metric_anomaly__mutmut['x__detect_metric_anomaly__mutmut_142'] = x__detect_metric_anomaly__mutmut_142 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__effective_baseline__mutmut)
def _effective_baseline(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_orig(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_1(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = None
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_2(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["XXhours_since_last_restartXX"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_3(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["HOURS_SINCE_LAST_RESTART"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_4(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = None
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_5(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["XXbaseline_window_hoursXX"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_6(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["BASELINE_WINDOW_HOURS"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_7(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours and not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_8(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None and hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_9(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is not None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_10(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart > window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_11(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_12(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, "XXXX"

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_13(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = None
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_14(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) * window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_15(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 2.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_16(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = None
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_17(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(None, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_18(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, None)
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_19(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_20(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, )
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_21(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(2, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_22(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(None))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_23(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart / points_per_hour))
    truncated = baseline[-usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_24(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = None
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_25(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[+usable_points:] if usable_points < len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"


def x__effective_baseline__mutmut_26(pod: PodMetricsRawData, baseline: list[float]) -> tuple[list[float], str]:
    hours_since_restart = pod["hours_since_last_restart"]
    window_hours = pod["baseline_window_hours"]
    if hours_since_restart is None or hours_since_restart >= window_hours or not baseline:
        return baseline, ""

    points_per_hour = len(baseline) / window_hours if window_hours else 1.0
    usable_points = max(1, int(hours_since_restart * points_per_hour))
    truncated = baseline[-usable_points:] if usable_points <= len(baseline) else baseline
    return truncated, f"baseline limited to {hours_since_restart:.1f}h since last restart"

mutants_x__effective_baseline__mutmut['_mutmut_orig'] = x__effective_baseline__mutmut_orig # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_1'] = x__effective_baseline__mutmut_1 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_2'] = x__effective_baseline__mutmut_2 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_3'] = x__effective_baseline__mutmut_3 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_4'] = x__effective_baseline__mutmut_4 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_5'] = x__effective_baseline__mutmut_5 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_6'] = x__effective_baseline__mutmut_6 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_7'] = x__effective_baseline__mutmut_7 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_8'] = x__effective_baseline__mutmut_8 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_9'] = x__effective_baseline__mutmut_9 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_10'] = x__effective_baseline__mutmut_10 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_11'] = x__effective_baseline__mutmut_11 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_12'] = x__effective_baseline__mutmut_12 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_13'] = x__effective_baseline__mutmut_13 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_14'] = x__effective_baseline__mutmut_14 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_15'] = x__effective_baseline__mutmut_15 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_16'] = x__effective_baseline__mutmut_16 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_17'] = x__effective_baseline__mutmut_17 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_18'] = x__effective_baseline__mutmut_18 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_19'] = x__effective_baseline__mutmut_19 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_20'] = x__effective_baseline__mutmut_20 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_21'] = x__effective_baseline__mutmut_21 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_22'] = x__effective_baseline__mutmut_22 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_23'] = x__effective_baseline__mutmut_23 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_24'] = x__effective_baseline__mutmut_24 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_25'] = x__effective_baseline__mutmut_25 # type: ignore # mutmut generated
mutants_x__effective_baseline__mutmut['x__effective_baseline__mutmut_26'] = x__effective_baseline__mutmut_26 # type: ignore # mutmut generated
mutants_x__hit_at_index__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__hit_at_index__mutmut)
def _hit_at_index(anomalies: list[AnomalyPoint], index: int) -> AnomalyPoint | None:
    return next((a for a in anomalies if int(a["index"]) == index), None)


def x__hit_at_index__mutmut_orig(anomalies: list[AnomalyPoint], index: int) -> AnomalyPoint | None:
    return next((a for a in anomalies if int(a["index"]) == index), None)


def x__hit_at_index__mutmut_1(anomalies: list[AnomalyPoint], index: int) -> AnomalyPoint | None:
    return next(None, None)


def x__hit_at_index__mutmut_2(anomalies: list[AnomalyPoint], index: int) -> AnomalyPoint | None:
    return next(None)


def x__hit_at_index__mutmut_3(anomalies: list[AnomalyPoint], index: int) -> AnomalyPoint | None:
    return next((a for a in anomalies if int(a["index"]) == index), )


def x__hit_at_index__mutmut_4(anomalies: list[AnomalyPoint], index: int) -> AnomalyPoint | None:
    return next((a for a in anomalies if int(None) == index), None)


def x__hit_at_index__mutmut_5(anomalies: list[AnomalyPoint], index: int) -> AnomalyPoint | None:
    return next((a for a in anomalies if int(a["XXindexXX"]) == index), None)


def x__hit_at_index__mutmut_6(anomalies: list[AnomalyPoint], index: int) -> AnomalyPoint | None:
    return next((a for a in anomalies if int(a["INDEX"]) == index), None)


def x__hit_at_index__mutmut_7(anomalies: list[AnomalyPoint], index: int) -> AnomalyPoint | None:
    return next((a for a in anomalies if int(a["index"]) != index), None)

mutants_x__hit_at_index__mutmut['_mutmut_orig'] = x__hit_at_index__mutmut_orig # type: ignore # mutmut generated
mutants_x__hit_at_index__mutmut['x__hit_at_index__mutmut_1'] = x__hit_at_index__mutmut_1 # type: ignore # mutmut generated
mutants_x__hit_at_index__mutmut['x__hit_at_index__mutmut_2'] = x__hit_at_index__mutmut_2 # type: ignore # mutmut generated
mutants_x__hit_at_index__mutmut['x__hit_at_index__mutmut_3'] = x__hit_at_index__mutmut_3 # type: ignore # mutmut generated
mutants_x__hit_at_index__mutmut['x__hit_at_index__mutmut_4'] = x__hit_at_index__mutmut_4 # type: ignore # mutmut generated
mutants_x__hit_at_index__mutmut['x__hit_at_index__mutmut_5'] = x__hit_at_index__mutmut_5 # type: ignore # mutmut generated
mutants_x__hit_at_index__mutmut['x__hit_at_index__mutmut_6'] = x__hit_at_index__mutmut_6 # type: ignore # mutmut generated
mutants_x__hit_at_index__mutmut['x__hit_at_index__mutmut_7'] = x__hit_at_index__mutmut_7 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__strongest_hit_from__mutmut)
def _strongest_hit_from(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) >= start_index]
    if not candidates:
        return None
    return max(candidates, key=lambda a: float(a["anomaly_score"]))


def x__strongest_hit_from__mutmut_orig(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) >= start_index]
    if not candidates:
        return None
    return max(candidates, key=lambda a: float(a["anomaly_score"]))


def x__strongest_hit_from__mutmut_1(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = None
    if not candidates:
        return None
    return max(candidates, key=lambda a: float(a["anomaly_score"]))


def x__strongest_hit_from__mutmut_2(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(None) >= start_index]
    if not candidates:
        return None
    return max(candidates, key=lambda a: float(a["anomaly_score"]))


def x__strongest_hit_from__mutmut_3(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["XXindexXX"]) >= start_index]
    if not candidates:
        return None
    return max(candidates, key=lambda a: float(a["anomaly_score"]))


def x__strongest_hit_from__mutmut_4(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["INDEX"]) >= start_index]
    if not candidates:
        return None
    return max(candidates, key=lambda a: float(a["anomaly_score"]))


def x__strongest_hit_from__mutmut_5(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) > start_index]
    if not candidates:
        return None
    return max(candidates, key=lambda a: float(a["anomaly_score"]))


def x__strongest_hit_from__mutmut_6(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) >= start_index]
    if candidates:
        return None
    return max(candidates, key=lambda a: float(a["anomaly_score"]))


def x__strongest_hit_from__mutmut_7(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) >= start_index]
    if not candidates:
        return None
    return max(None, key=lambda a: float(a["anomaly_score"]))


def x__strongest_hit_from__mutmut_8(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) >= start_index]
    if not candidates:
        return None
    return max(candidates, key=None)


def x__strongest_hit_from__mutmut_9(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) >= start_index]
    if not candidates:
        return None
    return max(key=lambda a: float(a["anomaly_score"]))


def x__strongest_hit_from__mutmut_10(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) >= start_index]
    if not candidates:
        return None
    return max(candidates, )


def x__strongest_hit_from__mutmut_11(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) >= start_index]
    if not candidates:
        return None
    return max(candidates, key=lambda a: None)


def x__strongest_hit_from__mutmut_12(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) >= start_index]
    if not candidates:
        return None
    return max(candidates, key=lambda a: float(None))


def x__strongest_hit_from__mutmut_13(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) >= start_index]
    if not candidates:
        return None
    return max(candidates, key=lambda a: float(a["XXanomaly_scoreXX"]))


def x__strongest_hit_from__mutmut_14(anomalies: list[AnomalyPoint], start_index: int) -> AnomalyPoint | None:
    candidates = [a for a in anomalies if int(a["index"]) >= start_index]
    if not candidates:
        return None
    return max(candidates, key=lambda a: float(a["ANOMALY_SCORE"]))

mutants_x__strongest_hit_from__mutmut['_mutmut_orig'] = x__strongest_hit_from__mutmut_orig # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_1'] = x__strongest_hit_from__mutmut_1 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_2'] = x__strongest_hit_from__mutmut_2 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_3'] = x__strongest_hit_from__mutmut_3 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_4'] = x__strongest_hit_from__mutmut_4 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_5'] = x__strongest_hit_from__mutmut_5 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_6'] = x__strongest_hit_from__mutmut_6 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_7'] = x__strongest_hit_from__mutmut_7 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_8'] = x__strongest_hit_from__mutmut_8 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_9'] = x__strongest_hit_from__mutmut_9 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_10'] = x__strongest_hit_from__mutmut_10 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_11'] = x__strongest_hit_from__mutmut_11 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_12'] = x__strongest_hit_from__mutmut_12 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_13'] = x__strongest_hit_from__mutmut_13 # type: ignore # mutmut generated
mutants_x__strongest_hit_from__mutmut['x__strongest_hit_from__mutmut_14'] = x__strongest_hit_from__mutmut_14 # type: ignore # mutmut generated
mutants_x__severity_from_zscore__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__severity_from_zscore__mutmut)
def _severity_from_zscore(z_score: float) -> EventSeverity:
    if z_score >= _cfg.zscore_critical_threshold:
        return EventSeverity.CRITICAL
    if z_score >= _cfg.zscore_high_threshold:
        return EventSeverity.HIGH
    return EventSeverity.MEDIUM


def x__severity_from_zscore__mutmut_orig(z_score: float) -> EventSeverity:
    if z_score >= _cfg.zscore_critical_threshold:
        return EventSeverity.CRITICAL
    if z_score >= _cfg.zscore_high_threshold:
        return EventSeverity.HIGH
    return EventSeverity.MEDIUM


def x__severity_from_zscore__mutmut_1(z_score: float) -> EventSeverity:
    if z_score > _cfg.zscore_critical_threshold:
        return EventSeverity.CRITICAL
    if z_score >= _cfg.zscore_high_threshold:
        return EventSeverity.HIGH
    return EventSeverity.MEDIUM


def x__severity_from_zscore__mutmut_2(z_score: float) -> EventSeverity:
    if z_score >= _cfg.zscore_critical_threshold:
        return EventSeverity.CRITICAL
    if z_score > _cfg.zscore_high_threshold:
        return EventSeverity.HIGH
    return EventSeverity.MEDIUM

mutants_x__severity_from_zscore__mutmut['_mutmut_orig'] = x__severity_from_zscore__mutmut_orig # type: ignore # mutmut generated
mutants_x__severity_from_zscore__mutmut['x__severity_from_zscore__mutmut_1'] = x__severity_from_zscore__mutmut_1 # type: ignore # mutmut generated
mutants_x__severity_from_zscore__mutmut['x__severity_from_zscore__mutmut_2'] = x__severity_from_zscore__mutmut_2 # type: ignore # mutmut generated


def _append_note(existing: str, addition: str) -> str:
    return f"{existing}; {addition}" if existing else addition
mutants_x__summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__summary__mutmut)
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


def x__summary__mutmut_orig(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
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


def x__summary__mutmut_1(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if anomalies:
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


def x__summary__mutmut_2(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "XXNo anomalies detected — all pods within baseline range.XX"
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


def x__summary__mutmut_3(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "no anomalies detected — all pods within baseline range."
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


def x__summary__mutmut_4(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "NO ANOMALIES DETECTED — ALL PODS WITHIN BASELINE RANGE."
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


def x__summary__mutmut_5(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = None
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


def x__summary__mutmut_6(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "XXyXX" if len(anomalies) == 1 else "ies"
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


def x__summary__mutmut_7(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "Y" if len(anomalies) == 1 else "ies"
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


def x__summary__mutmut_8(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) != 1 else "ies"
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


def x__summary__mutmut_9(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 2 else "ies"
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


def x__summary__mutmut_10(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "XXiesXX"
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


def x__summary__mutmut_11(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "IES"
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


def x__summary__mutmut_12(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = None
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


def x__summary__mutmut_13(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = {}
    for anomaly in anomalies:
        counts[anomaly.severity] = None
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


def x__summary__mutmut_14(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = {}
    for anomaly in anomalies:
        counts[anomaly.severity] = counts.get(anomaly.severity, 0) - 1
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


def x__summary__mutmut_15(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = {}
    for anomaly in anomalies:
        counts[anomaly.severity] = counts.get(None, 0) + 1
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


def x__summary__mutmut_16(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = {}
    for anomaly in anomalies:
        counts[anomaly.severity] = counts.get(anomaly.severity, None) + 1
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


def x__summary__mutmut_17(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = {}
    for anomaly in anomalies:
        counts[anomaly.severity] = counts.get(0) + 1
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


def x__summary__mutmut_18(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = {}
    for anomaly in anomalies:
        counts[anomaly.severity] = counts.get(anomaly.severity, ) + 1
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


def x__summary__mutmut_19(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = {}
    for anomaly in anomalies:
        counts[anomaly.severity] = counts.get(anomaly.severity, 1) + 1
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


def x__summary__mutmut_20(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = {}
    for anomaly in anomalies:
        counts[anomaly.severity] = counts.get(anomaly.severity, 0) + 2
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


def x__summary__mutmut_21(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = {}
    for anomaly in anomalies:
        counts[anomaly.severity] = counts.get(anomaly.severity, 0) + 1
    breakdown = None
    return f"{len(anomalies)} anomal{plural} detected ({breakdown})"


def x__summary__mutmut_22(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = {}
    for anomaly in anomalies:
        counts[anomaly.severity] = counts.get(anomaly.severity, 0) + 1
    breakdown = ", ".join(
        None
    )
    return f"{len(anomalies)} anomal{plural} detected ({breakdown})"


def x__summary__mutmut_23(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
    if not anomalies:
        return "No anomalies detected — all pods within baseline range."
    plural = "y" if len(anomalies) == 1 else "ies"
    counts: dict[EventSeverity, int] = {}
    for anomaly in anomalies:
        counts[anomaly.severity] = counts.get(anomaly.severity, 0) + 1
    breakdown = "XX, XX".join(
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


def x__summary__mutmut_24(anomalies: list[PodAnomaly], excluded: list[ExcludedPod]) -> str:
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
        if severity not in counts
    )
    return f"{len(anomalies)} anomal{plural} detected ({breakdown})"

mutants_x__summary__mutmut['_mutmut_orig'] = x__summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_1'] = x__summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_2'] = x__summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_3'] = x__summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_4'] = x__summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_5'] = x__summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_6'] = x__summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_7'] = x__summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_8'] = x__summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_9'] = x__summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_10'] = x__summary__mutmut_10 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_11'] = x__summary__mutmut_11 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_12'] = x__summary__mutmut_12 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_13'] = x__summary__mutmut_13 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_14'] = x__summary__mutmut_14 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_15'] = x__summary__mutmut_15 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_16'] = x__summary__mutmut_16 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_17'] = x__summary__mutmut_17 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_18'] = x__summary__mutmut_18 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_19'] = x__summary__mutmut_19 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_20'] = x__summary__mutmut_20 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_21'] = x__summary__mutmut_21 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_22'] = x__summary__mutmut_22 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_23'] = x__summary__mutmut_23 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_24'] = x__summary__mutmut_24 # type: ignore # mutmut generated
