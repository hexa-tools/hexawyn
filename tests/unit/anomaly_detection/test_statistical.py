"""Unit tests for statistical anomaly detection (Z-score)."""

from hexawyn.domain.services.anomaly_detection.statistical import (
    AnomalyDetectionResult,
    ZScoreAnomalyDetector,
)


class TestAnomalyDetectionResult:
    def test_defaults(self) -> None:
        result = AnomalyDetectionResult()
        assert result.anomalies_detected is False
        assert result.anomaly_count == 0
        assert result.anomalies == []
        assert result.threshold == 2.5

    def test_with_anomalies(self) -> None:
        result = AnomalyDetectionResult(
            anomalies_detected=True,
            anomaly_count=2,
            anomalies=[{"index": 3, "value": 99.0, "z_score": 3.5}],
            threshold=2.5,
            mean=50.0,
            std_dev=14.0,
        )
        assert result.anomalies_detected is True
        assert len(result.anomalies) == 1
        assert result.anomalies[0]["z_score"] == 3.5


class TestZScoreAnomalyDetector:
    def test_insufficient_data_returns_no_anomalies(self) -> None:
        detector = ZScoreAnomalyDetector()
        result = detector.detect([10.0, 20.0])
        assert result.anomalies_detected is False

    def test_normal_distribution_no_anomalies(self) -> None:
        detector = ZScoreAnomalyDetector()
        data = [10.0, 11.0, 12.0, 11.0, 10.0, 12.0, 11.0, 10.0]
        result = detector.detect(data)
        assert result.anomalies_detected is False

    def test_clear_outlier_detected(self) -> None:
        detector = ZScoreAnomalyDetector()
        data = [10.0, 11.0, 10.0, 11.0, 10.0, 11.0, 10.0, 500.0, 11.0, 10.0]
        result = detector.detect(data)
        assert result.anomalies_detected is True
        assert result.anomaly_count == 1

    def test_custom_threshold(self) -> None:
        detector = ZScoreAnomalyDetector(threshold=1.0)
        data = [10.0, 11.0, 10.0, 14.0, 10.0]
        result = detector.detect(data)
        assert result.anomalies_detected is True

    def test_identical_values_no_anomalies(self) -> None:
        detector = ZScoreAnomalyDetector()
        data = [5.0, 5.0, 5.0, 5.0, 5.0]
        result = detector.detect(data)
        assert result.anomalies_detected is False

    def test_result_includes_statistics(self) -> None:
        detector = ZScoreAnomalyDetector()
        data = [10.0, 12.0, 11.0, 10.0, 11.0, 10.0, 50.0, 11.0]
        result = detector.detect(data)
        assert result.mean > 0
        assert result.std_dev > 0
        assert result.threshold == 2.5

    def test_anomaly_entry_has_required_fields(self) -> None:
        detector = ZScoreAnomalyDetector()
        data = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 500.0, 10.0, 10.0, 10.0]
        result = detector.detect(data)
        anomaly = result.anomalies[0]
        assert "index" in anomaly
        assert "value" in anomaly
        assert "z_score" in anomaly
        assert anomaly["z_score"] > result.threshold

    def test_detect_with_context_preserves_original_values(self) -> None:
        detector = ZScoreAnomalyDetector()
        data = [1.0, 2.0, 1.0, 2.0, 1000.0, 1.0, 2.0, 1.0, 2.0, 1.0, 2.0]
        context = ["a", "b", "c", "d", "OUTLIER", "e", "f", "g", "h", "i", "j"]
        result = detector.detect(data, context=context)
        assert result.anomalies[0]["context"] == "OUTLIER"

    def test_empty_list_returns_no_anomalies(self) -> None:
        detector = ZScoreAnomalyDetector()
        result = detector.detect([])
        assert result.anomalies_detected is False
