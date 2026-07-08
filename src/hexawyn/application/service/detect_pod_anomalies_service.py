from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.pod_metrics_baseline_port import PodMetricsBaselinePort
from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_command import (
    DetectPodAnomaliesCommand,
)
from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_response import (
    DetectPodAnomaliesResponse,
    ExcludedPodDict,
    PodAnomalyDict,
)
from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_service_port import (
    DetectPodAnomaliesServicePort,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.pod_anomaly import ExcludedPod, PodAnomaly, PodAnomalyDetectionReport
from hexawyn.domain.services.pod_anomaly_detection.detector import detect_pod_anomalies


class DetectPodAnomaliesService(DetectPodAnomaliesServicePort):
    def __init__(self, port: PodMetricsBaselinePort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port

    def detect(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=command.namespace, window_days=command.baseline_window_days
        )
        report = detect_pod_anomalies(raw_data, baseline_window_days=command.baseline_window_days)
        return _to_response(report)

    def _validate_namespace_exists(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )


def _to_response(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        total_pods=report.total_pods,
        anomalies=[_to_anomaly_dict(anomaly) for anomaly in report.anomalies],
        excluded_pods=[_to_excluded_dict(excluded) for excluded in report.excluded_pods],
        summary=report.summary,
    )


def _to_anomaly_dict(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def _to_excluded_dict(excluded: ExcludedPod) -> ExcludedPodDict:
    return ExcludedPodDict(
        pod_name=excluded.pod_name, namespace=excluded.namespace, reason=excluded.reason
    )
