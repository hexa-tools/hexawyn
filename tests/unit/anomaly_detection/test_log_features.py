"""Unit tests for log line feature extraction (semantic anomaly detection input)."""

from __future__ import annotations

from hexawyn.domain.services.anomaly_detection.log_features import extract_log_features


class TestExtractLogFeatures:
    def test_short_normal_line_has_low_latency_feature(self) -> None:
        features = extract_log_features("DB query completed in 5ms")
        assert features[2] == 5.0

    def test_slow_query_in_seconds_converted_to_milliseconds(self) -> None:
        features = extract_log_features("DB query completed in 8s")
        assert features[2] == 8000.0

    def test_line_with_no_latency_defaults_to_zero(self) -> None:
        features = extract_log_features("pod started successfully")
        assert features[2] == 0.0

    def test_feature_vector_length_is_stable(self) -> None:
        features = extract_log_features("some log line with words")
        assert len(features) == 4

    def test_line_length_and_word_count_reflect_content(self) -> None:
        line = "one two three four five"
        features = extract_log_features(line)
        assert features[0] == float(len(line))
        assert features[3] == 5.0

    def test_digit_count_reflects_numeric_characters(self) -> None:
        features = extract_log_features("status=200 retries=3")
        assert features[1] == 4.0
