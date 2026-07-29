from __future__ import annotations

from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.command import (
    DetectLogAnomaliesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.response import (
    DetectLogAnomaliesResponse,
    LogAnomalyDict,
)
from hexawyn.domain.models.analyze_pod_logs import AnalyzePodLogsRequest
from hexawyn.domain.models.log_anomaly import DetectLogAnomaliesRequest, DetectLogAnomaliesResult
from hexawyn.domain.services.log_analysis.log_anomaly_detector import detect_log_anomalies


class DetectLogAnomaliesUseCase:
    def __init__(self, port: PodLogsPort) -> None:
        self._port = port

    def execute(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)


def _to_response(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )
