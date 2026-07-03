"""Unit tests for detect_log_anomalies domain models (pure dataclasses)."""

from __future__ import annotations

from hexawyn.domain.models.log_anomaly import (
    DetectLogAnomaliesRequest,
    DetectLogAnomaliesResult,
    LogAnomaly,
)


class TestLogAnomaly:
    def test_fields(self) -> None:
        anomaly = LogAnomaly(
            timestamp="2024-01-01T15:00:00Z",
            log_line="500 lines/min (10x baseline)",
            anomaly_score=4.2,
            type="volume",
        )
        assert anomaly.timestamp == "2024-01-01T15:00:00Z"
        assert anomaly.log_line == "500 lines/min (10x baseline)"
        assert anomaly.anomaly_score == 4.2
        assert anomaly.type == "volume"
        assert anomaly.low_confidence is False

    def test_low_confidence_defaults_false_and_can_be_set(self) -> None:
        anomaly = LogAnomaly(
            timestamp="T1", log_line="l", anomaly_score=1.0, type="semantic", low_confidence=True
        )
        assert anomaly.low_confidence is True


class TestDetectLogAnomaliesRequest:
    def test_defaults(self) -> None:
        request = DetectLogAnomaliesRequest(pod_name="inventory-service", namespace="prod")
        assert request.pod_name == "inventory-service"
        assert request.namespace == "prod"
        assert request.time_window_minutes == 240
        assert request.zscore_threshold == 3.0

    def test_custom_values(self) -> None:
        request = DetectLogAnomaliesRequest(
            pod_name="p", namespace="n", time_window_minutes=60, zscore_threshold=2.0
        )
        assert request.time_window_minutes == 60
        assert request.zscore_threshold == 2.0


class TestDetectLogAnomaliesResult:
    def test_defaults(self) -> None:
        result = DetectLogAnomaliesResult(
            pod_name="inventory-service",
            namespace="prod",
            time_window_minutes=240,
            total_lines=500,
        )
        assert result.anomalies == []
        assert result.baseline_mean_lines_per_minute == 0.0
        assert result.baseline_std_dev == 0.0
        assert result.summary == ""
        assert result.insufficient_data is False
        assert result.formats_analyzed_separately == 1

    def test_with_anomalies(self) -> None:
        anomaly = LogAnomaly(timestamp="T1", log_line="l", anomaly_score=3.5, type="volume")
        result = DetectLogAnomaliesResult(
            pod_name="p",
            namespace="n",
            time_window_minutes=240,
            total_lines=100,
            anomalies=[anomaly],
            summary="1 anomaly detected",
        )
        assert len(result.anomalies) == 1
        assert result.summary == "1 anomaly detected"
