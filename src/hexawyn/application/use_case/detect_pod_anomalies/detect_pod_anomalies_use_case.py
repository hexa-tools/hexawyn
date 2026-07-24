from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.pod_metrics_baseline_port import PodMetricsBaselinePort
from hexawyn.application.use_case.detect_pod_anomalies.command import DetectPodAnomaliesCommand
from hexawyn.application.use_case.detect_pod_anomalies.response import DetectPodAnomaliesResponse
from hexawyn.domain.services.pod_anomaly_detection.detector import detect_pod_anomalies


class DetectPodAnomaliesUseCase:
    def __init__(self, port: PodMetricsBaselinePort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port

    def execute(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        raw_data = self._port.get_all_pod_metrics_data(
            command.namespace, command.baseline_window_days
        )
        report = detect_pod_anomalies(raw_data, command.baseline_window_days)

        anomalies: list[dict[str, object]] = []
        for anomaly in report.anomalies:
            anomalies.append(
                {
                    "pod_name": anomaly.pod_name,
                    "namespace": anomaly.namespace,
                    "metric": anomaly.metric,
                    "severity": anomaly.severity.value,
                    "deviation_pct": anomaly.deviation_pct,
                    "z_score": anomaly.z_score,
                    "isolation_forest_score": anomaly.isolation_forest_score,
                    "detection_method": anomaly.detection_method,
                    "note": anomaly.note,
                }
            )

        excluded_names = [e.pod_name for e in report.excluded_pods]

        return DetectPodAnomaliesResponse(
            namespace=command.namespace,
            total_pods=report.total_pods,
            anomalies=anomalies,
            excluded_pods=excluded_names,
            summary=report.summary,
        )
