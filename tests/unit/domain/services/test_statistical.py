"""Tests for domain/services/anomaly_detection/statistical — Z-score detector."""

from __future__ import annotations

from hexawyn.domain.models.constants import EventAnalysisConstants
from hexawyn.domain.services.anomaly_detection.statistical import (
    ZScoreAnomalyDetector,
)

_cfg = EventAnalysisConstants()


class TestZScoreDetector:
    def test_detect_spike_outlier(self) -> None:
        detector = ZScoreAnomalyDetector()
        series = [1.0] * 100 + [50.0]
        result = detector.detect(series)
        assert result.anomalies_detected is True
        assert result.anomaly_count == 1  # noqa: PLR2004
        assert result.anomalies == [{"index": 100, "value": 50.0, "z_score": 9.9504}]
        assert result.threshold == _cfg.temporal_anomaly_zscore_threshold
        assert result.mean == 1.4851  # noqa: PLR2004
        assert result.std_dev == 4.8757  # noqa: PLR2004

    def test_detect_includes_context_when_provided(self) -> None:
        detector = ZScoreAnomalyDetector()
        series = [1.0] * 100 + [50.0]
        context = ["ok"] * 100 + ["spike"]
        result = detector.detect(series, context=context)
        assert result.anomalies[0]["context"] == "spike"

    def test_context_longer_than_series_indexed(self) -> None:
        detector = ZScoreAnomalyDetector()
        series = [1.0] * 100 + [50.0]
        context = ["c%d" % i for i in range(200)]
        result = detector.detect(series, context=context)
        assert result.anomalies[0]["context"] == "c100"

    def test_too_few_points_returns_no_anomaly(self) -> None:
        detector = ZScoreAnomalyDetector(min_data_points=5)
        result = detector.detect([1.0, 2.0, 3.0])
        assert result.anomalies_detected is False
        assert result.anomaly_count == 0
        assert result.anomalies == []
        assert result.threshold == _cfg.temporal_anomaly_zscore_threshold

    def test_zero_std_dev_returns_no_anomaly(self) -> None:
        detector = ZScoreAnomalyDetector()
        result = detector.detect([5.0] * 10)
        assert result.anomalies_detected is False
        assert result.mean == 5.0  # noqa: PLR2004
        assert result.std_dev == 0.0

    def test_single_point_returns_no_anomaly(self) -> None:
        detector = ZScoreAnomalyDetector()
        result = detector.detect([7.0])
        assert result.anomalies_detected is False
        assert result.mean == 0.0
        assert result.std_dev == 0.0

    def test_two_points_differing_returns_no_anomaly(self) -> None:
        detector = ZScoreAnomalyDetector()
        result = detector.detect([1.0, 100.0])
        assert result.anomalies_detected is False

    def test_defaults_used_from_constants(self) -> None:
        detector = ZScoreAnomalyDetector()
        assert detector.threshold == _cfg.temporal_anomaly_zscore_threshold
        assert detector.min_data_points == _cfg.min_data_points_for_anomaly

    def test_custom_threshold_more_sensitive(self) -> None:
        detector = ZScoreAnomalyDetector(threshold=1.0)
        series = [10.0, 10.0, 10.0, 40.0, 10.0, 10.0]
        result = detector.detect(series)
        assert result.anomalies_detected is True
        assert result.anomalies[0]["index"] == 3  # noqa: PLR2004
        assert result.threshold == 1.0

    def test_single_point_with_minimum_one_reports_zero_std(self) -> None:
        detector = ZScoreAnomalyDetector(min_data_points=1)
        result = detector.detect([7.0])
        assert result.anomalies_detected is False
        assert result.mean == 7.0  # noqa: PLR2004
        assert result.std_dev == 0.0

    def test_context_length_equal_to_index_still_omitted(self) -> None:
        detector = ZScoreAnomalyDetector(threshold=1.0)
        series = [10.0, 10.0, 40.0, 10.0, 10.0, 10.0]
        context = ["a", "b"]
        result = detector.detect(series, context=context)
        assert len(result.anomalies) == 1  # noqa: PLR2004
        assert "context" not in result.anomalies[0]

    def test_custom_minimum_sample_count_accepted(self) -> None:
        detector = ZScoreAnomalyDetector(min_data_points=2)
        result = detector.detect([1.0, 100.0, 1.0, 1.0])
        assert result.threshold == _cfg.temporal_anomaly_zscore_threshold

    def test_zero_minimum_sample_count_falls_back_to_default(self) -> None:
        detector = ZScoreAnomalyDetector(min_data_points=0)
        assert detector.min_data_points == _cfg.min_data_points_for_anomaly

    def test_zero_threshold_falls_back_to_default(self) -> None:
        detector = ZScoreAnomalyDetector(threshold=0.0)
        assert detector.threshold == _cfg.temporal_anomaly_zscore_threshold

    def test_multiple_outliers_all_reported(self) -> None:
        detector = ZScoreAnomalyDetector()
        series = [1.0] * 50 + [80.0, 90.0] + [1.0] * 50
        result = detector.detect(series)
        assert result.anomaly_count == 2  # noqa: PLR2004
        assert [a["index"] for a in result.anomalies] == [50, 51]

    def test_two_point_series_std_used(self) -> None:
        detector = ZScoreAnomalyDetector(min_data_points=2)
        result = detector.detect([5.0, 9.0])
        assert result.mean == 7.0  # noqa: PLR2004
        assert result.std_dev == 2.8284  # noqa: PLR2004

    def test_high_threshold_no_anomaly_despite_std(self) -> None:
        detector = ZScoreAnomalyDetector(threshold=99.0)
        series = [1.0] * 10 + [50.0]
        result = detector.detect(series)
        assert result.anomalies_detected is False
        assert result.mean == 5.4545  # noqa: PLR2004
        assert result.std_dev == 14.7741  # noqa: PLR2004

    def test_exactly_minimum_sample_count_analysed(self) -> None:
        detector = ZScoreAnomalyDetector()
        result = detector.detect([5.0] * 5)
        assert result.anomalies_detected is False
        assert result.mean == 5.0  # noqa: PLR2004

    def test_custom_threshold_in_too_few_early_return(self) -> None:
        detector = ZScoreAnomalyDetector(threshold=1.5, min_data_points=5)
        result = detector.detect([1.0, 2.0])
        assert result.anomalies_detected is False
        assert result.threshold == 1.5  # noqa: PLR2004

    def test_custom_threshold_in_zero_std_early_return(self) -> None:
        detector = ZScoreAnomalyDetector(threshold=1.5)
        result = detector.detect([5.0] * 5)
        assert result.anomalies_detected is False
        assert result.threshold == 1.5  # noqa: PLR2004
        assert result.mean == 5.0  # noqa: PLR2004

    def test_context_shorter_than_index_omitted(self) -> None:
        detector = ZScoreAnomalyDetector(threshold=1.0)
        series = [10.0, 10.0, 40.0, 10.0, 10.0, 10.0]
        result = detector.detect(series, context=["x"])
        assert len(result.anomalies) == 1  # noqa: PLR2004
        assert "context" not in result.anomalies[0]
