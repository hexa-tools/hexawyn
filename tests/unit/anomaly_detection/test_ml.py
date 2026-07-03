"""Unit tests for ML-based (Isolation Forest) semantic anomaly detection."""

from __future__ import annotations

from hexawyn.domain.services.anomaly_detection.ml import (
    IsolationForestAnomalyDetector,
    MLAnomalyDetectionResult,
)


class TestMLAnomalyDetectionResult:
    def test_defaults(self) -> None:
        result = MLAnomalyDetectionResult()
        assert result.anomalies_detected is False
        assert result.anomaly_count == 0
        assert result.anomalies == []


class TestIsolationForestAnomalyDetector:
    def test_insufficient_samples_returns_no_anomalies(self) -> None:
        detector = IsolationForestAnomalyDetector()
        result = detector.detect(["line one", "line two"])
        assert result.anomalies_detected is False

    def test_silent_slow_query_detected_without_error_keyword(self) -> None:
        """TC2: DB query jumps from 5ms to 8000ms, no 'ERROR' keyword anywhere."""
        detector = IsolationForestAnomalyDetector()
        normal_lines = [f"DB query completed in {5 + (i % 3)}ms" for i in range(97)]
        slow_lines = ["DB query completed in 8000ms" for _ in range(3)]
        lines = normal_lines + slow_lines

        result = detector.detect(lines)

        assert result.anomalies_detected is True
        detected_lines = {a["line"] for a in result.anomalies}
        assert "DB query completed in 8000ms" in detected_lines
        for anomaly in result.anomalies:
            assert "error" not in str(anomaly["line"]).lower()

    def test_completely_normal_logs_returns_no_anomalies(self) -> None:
        """TC3: uniform, unremarkable logs → no semantic outliers."""
        detector = IsolationForestAnomalyDetector()
        lines = [f"heartbeat ok seq={i}" for i in range(100)]

        result = detector.detect(lines)

        assert result.anomalies_detected is False
        assert result.anomaly_count == 0

    def test_anomaly_entry_has_required_fields(self) -> None:
        detector = IsolationForestAnomalyDetector()
        normal_lines = ["request handled in 10ms" for _ in range(97)]
        outliers = ["request handled in 9000ms" for _ in range(3)]
        result = detector.detect(normal_lines + outliers)

        assert result.anomalies_detected is True
        anomaly = result.anomalies[0]
        assert "index" in anomaly
        assert "line" in anomaly
        assert "anomaly_score" in anomaly

    def test_empty_list_returns_no_anomalies(self) -> None:
        detector = IsolationForestAnomalyDetector()
        result = detector.detect([])
        assert result.anomalies_detected is False

    def test_mild_score_deviation_below_threshold_is_not_flagged(self) -> None:
        """IsolationForest's fixed contamination flags borderline points too;
        only points deviating from the batch's own score spread by at least
        min_score_deviation are real anomalies (see _select_true_outliers)."""
        detector = IsolationForestAnomalyDetector(min_score_deviation=10.0)
        lines = [f"request handled in {5 + (i % 7)}ms extra={i % 13}" for i in range(100)]

        result = detector.detect(lines)

        assert result.anomalies_detected is False
