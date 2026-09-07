"""Tests for domain/services/anomaly_detection/ml — Isolation Forest detector."""

from __future__ import annotations

import numpy as np
import pytest
from hexawyn.domain.models.constants import LogAnomalyDetectionConstants
from hexawyn.domain.services.anomaly_detection import ml as ml_module
from hexawyn.domain.services.anomaly_detection.ml import IsolationForestAnomalyDetector

_cfg = LogAnomalyDetectionConstants()


class TestDetectorDefaults:
    def test_defaults_loaded_from_constants(self) -> None:
        detector = IsolationForestAnomalyDetector()
        assert detector.contamination == _cfg.isolation_forest_contamination
        assert detector.random_state == _cfg.isolation_forest_random_state
        assert detector.min_samples == _cfg.isolation_forest_min_samples
        assert detector.min_score_deviation == _cfg.isolation_forest_min_score_deviation

    def test_zero_contamination_falls_back_to_default(self) -> None:
        detector = IsolationForestAnomalyDetector(contamination=0.0)
        assert detector.contamination == _cfg.isolation_forest_contamination

    def test_zero_min_samples_falls_back_to_default(self) -> None:
        detector = IsolationForestAnomalyDetector(min_samples=0)
        assert detector.min_samples == _cfg.isolation_forest_min_samples

    def test_zero_deviation_falls_back_to_default(self) -> None:
        detector = IsolationForestAnomalyDetector(min_score_deviation=0.0)
        assert detector.min_score_deviation == _cfg.isolation_forest_min_score_deviation

    def test_custom_values_accepted(self) -> None:
        detector = IsolationForestAnomalyDetector(
            contamination=0.2,
            random_state=7,
            min_samples=3,
            min_score_deviation=0.5,
        )
        assert detector.contamination == 0.2  # noqa: PLR2004
        assert detector.random_state == 7  # noqa: PLR2004
        assert detector.min_samples == 3  # noqa: PLR2004
        assert detector.min_score_deviation == 0.5  # noqa: PLR2004


class TestDetectText:
    def _spike_batch(self) -> list[str]:
        base = "GET /api/resource ok"
        return [base] * 40 + [base + " with very long anomalous tail " * 30] + [base] * 40

    def test_spike_line_detected(self) -> None:
        detector = IsolationForestAnomalyDetector()
        result = detector.detect(self._spike_batch())
        assert result.anomalies_detected is True
        assert result.anomaly_count == 1  # noqa: PLR2004
        assert result.anomalies[0]["index"] == 40  # noqa: PLR2004
        assert result.anomalies[0]["line"] == self._spike_batch()[40]
        assert isinstance(result.anomalies[0]["anomaly_score"], float)

    def test_uniform_lines_no_anomaly(self) -> None:
        detector = IsolationForestAnomalyDetector()
        result = detector.detect(["uniform line ok"] * 30)
        assert result.anomalies_detected is False
        assert result.anomaly_count == 0
        assert result.anomalies == []

    def test_too_few_lines_returns_empty(self) -> None:
        detector = IsolationForestAnomalyDetector()
        result = detector.detect(["a", "b", "c", "d"])
        assert result.anomalies_detected is False
        assert result.anomaly_count == 0
        assert result.anomalies == []

    def test_exactly_minimum_lines_still_analysed(self) -> None:
        detector = IsolationForestAnomalyDetector(min_samples=10)
        base = "normal line"
        lines = [base] * 9 + [base + " very long " * 40]
        result = detector.detect(lines)
        assert result.anomalies_detected is True
        assert result.anomaly_count == 1  # noqa: PLR2004

    def test_deterministic_given_random_state(self) -> None:
        detector = IsolationForestAnomalyDetector()
        first = detector.detect(self._spike_batch())
        second = detector.detect(self._spike_batch())
        assert first.anomalies == second.anomalies

    def test_two_detectors_same_seed_agree(self) -> None:
        left = IsolationForestAnomalyDetector(random_state=42).detect(self._spike_batch())
        right = IsolationForestAnomalyDetector(random_state=42).detect(self._spike_batch())
        assert left.anomalies == right.anomalies

    def test_configured_hyperparameters_forwarded_to_model(self, mocker: object) -> None:
        detector = IsolationForestAnomalyDetector(
            contamination=0.1,
            random_state=7,
            min_score_deviation=0.5,
        )
        mock_model = mocker.Mock()
        mock_model.fit_predict.return_value = np.array([1, 1])
        mock_model.decision_function.return_value = np.array([0.3, 0.4])
        mocker.patch(
            "hexawyn.domain.services.anomaly_detection.ml.IsolationForest",
            return_value=mock_model,
        )
        detector._run(["a", "b"], np.array([[0.1], [0.2]]), "line")
        constructor = ml_module.IsolationForest
        assert constructor.call_args.kwargs == {"contamination": 0.1, "random_state": 7}
        np.testing.assert_array_equal(
            mock_model.fit_predict.call_args.args[0], np.array([[0.1], [0.2]])
        )

    def test_empty_lines_returns_empty(self) -> None:
        detector = IsolationForestAnomalyDetector()
        result = detector.detect([])
        assert result.anomalies_detected is False


class TestDetectSeries:
    def _spike_series(self) -> list[float]:
        return [1.0] * 90 + [500.0] + [1.0] * 90

    def test_sharp_spike_detected(self) -> None:
        detector = IsolationForestAnomalyDetector()
        result = detector.detect_series(self._spike_series())
        assert result.anomalies_detected is True
        assert result.anomaly_count == 1  # noqa: PLR2004
        assert result.anomalies[0]["index"] == 90  # noqa: PLR2004
        assert result.anomalies[0]["value"] == 500.0  # noqa: PLR2004

    def test_uniform_series_no_anomaly(self) -> None:
        detector = IsolationForestAnomalyDetector()
        result = detector.detect_series([5.0] * 40)
        assert result.anomalies_detected is False

    def test_too_few_values_returns_empty(self) -> None:
        detector = IsolationForestAnomalyDetector()
        result = detector.detect_series([1.0, 2.0, 3.0])
        assert result.anomalies_detected is False
        assert result.anomaly_count == 0

    def test_exactly_minimum_values_still_analysed(self) -> None:
        detector = IsolationForestAnomalyDetector(min_samples=10)
        result = detector.detect_series([1.0] * 9 + [500.0])
        assert result.anomalies_detected is True
        assert result.anomalies[0]["value"] == 500.0  # noqa: PLR2004

    def test_detect_and_detect_series_result_shape(self) -> None:
        detector = IsolationForestAnomalyDetector()
        text = detector.detect(self._spike_batch_text())
        series = detector.detect_series(self._spike_series())
        assert set(text.anomalies[0].keys()) == {"index", "line", "anomaly_score"}
        assert set(series.anomalies[0].keys()) == {"index", "value", "anomaly_score"}

    def _spike_batch_text(self) -> list[str]:
        base = "normal line"
        return [base] * 40 + [base + " very long " * 40] + [base] * 40


class TestSelectTrueOutliersDirect:
    """Direct coverage of the deviation-filter that removes forced outliers."""

    def test_no_negative_predictions_returns_empty(self) -> None:
        detector = IsolationForestAnomalyDetector()
        scores = np.array([0.3, 0.2, 0.4])
        result = detector._select_true_outliers(
            ["a", "b", "c"], np.array([1, 1, 1]), scores, "line"
        )
        assert result == []

    def test_zero_score_std_returns_empty(self) -> None:
        detector = IsolationForestAnomalyDetector()
        scores = np.array([0.5, 0.5, 0.5])
        result = detector._select_true_outliers(
            ["a", "b", "c"], np.array([-1, 1, -1]), scores, "line"
        )
        assert result == []

    def test_positive_prediction_skipped_despite_low_score(self) -> None:
        detector = IsolationForestAnomalyDetector()
        scores = np.array([0.3, -5.0, 0.4])
        result = detector._select_true_outliers(
            ["a", "boom", "c"], np.array([1, 1, 1]), scores, "line"
        )
        assert result == []

    def test_low_deviation_outlier_skipped(self) -> None:
        detector = IsolationForestAnomalyDetector()
        scores = np.array([0.3, -0.5, 0.4])
        result = detector._select_true_outliers(
            ["a", "slightly-off", "c"], np.array([1, -1, 1]), scores, "line"
        )
        assert result == []

    def test_true_outlier_reported_with_line(self) -> None:
        detector = IsolationForestAnomalyDetector()
        items = ["bulk%d" % i for i in range(9)] + ["boom"]
        scores = np.array([0.3] * 9 + [-5.0])
        predictions = np.array([1] * 9 + [-1])
        result = detector._select_true_outliers(items, predictions, scores, "line")
        assert result == [{"index": 9, "line": "boom", "anomaly_score": 5.0}]

    def test_true_outlier_reported_with_value_key(self) -> None:
        detector = IsolationForestAnomalyDetector()
        items = [1.0] * 9 + [500.0]
        scores = np.array([0.3] * 9 + [-5.0])
        predictions = np.array([1] * 9 + [-1])
        result = detector._select_true_outliers(items, predictions, scores, "value")
        assert result == [{"index": 9, "value": 500.0, "anomaly_score": 5.0}]

    def test_multiple_true_outliers_reported_in_order(self) -> None:
        detector = IsolationForestAnomalyDetector()
        items = ["bulk%d" % i for i in range(8)] + ["boom1", "boom2"]
        scores = np.array([0.3] * 8 + [-5.0, -4.0])
        predictions = np.array([1] * 8 + [-1, -1])
        result = detector._select_true_outliers(items, predictions, scores, "line")
        assert [entry["index"] for entry in result] == [8, 9]
        assert [entry["line"] for entry in result] == ["boom1", "boom2"]

    def test_positive_prediction_before_outlier_does_not_break(self) -> None:
        detector = IsolationForestAnomalyDetector()
        items = ["bulk%d" % i for i in range(9)] + ["normal", "boom"]
        scores = np.array([0.3] * 9 + [0.25, -5.0])
        predictions = np.array([1] * 9 + [1, -1])
        result = detector._select_true_outliers(items, predictions, scores, "line")
        assert result == [{"index": 10, "line": "boom", "anomaly_score": 5.0}]

    def test_low_deviation_before_true_outlier_keeps_scanning(self) -> None:
        detector = IsolationForestAnomalyDetector()
        items = ["bulk%d" % i for i in range(8)] + ["lowdev", "boom"]
        scores = np.array([0.5] * 8 + [0.3, -8.0])
        predictions = np.array([1] * 8 + [-1, -1])
        result = detector._select_true_outliers(items, predictions, scores, "line")
        assert result == [{"index": 9, "line": "boom", "anomaly_score": 8.0}]

    def test_score_rounded_to_four_decimals(self) -> None:
        detector = IsolationForestAnomalyDetector()
        items = ["bulk%d" % i for i in range(9)] + ["boom"]
        scores = np.array([0.3] * 9 + [-1.23456])
        predictions = np.array([1] * 9 + [-1])
        result = detector._select_true_outliers(items, predictions, scores, "line")
        assert result == [{"index": 9, "line": "boom", "anomaly_score": 1.2346}]

    def test_mismatched_lengths_raise_value_error(self) -> None:
        detector = IsolationForestAnomalyDetector()
        with pytest.raises(ValueError):
            detector._select_true_outliers(["a", "b"], np.array([1]), np.array([0.1, 0.2]), "line")
