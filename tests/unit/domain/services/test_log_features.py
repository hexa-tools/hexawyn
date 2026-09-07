"""Tests for domain/services/anomaly_detection/log_features — feature extraction."""

from __future__ import annotations

from hexawyn.domain.services.anomaly_detection.log_features import (
    _extract_latency_ms,
    extract_log_features,
)


class TestExtractLogFeatures:
    def test_length_word_and_digit_features(self) -> None:
        features = extract_log_features("GET /api/v1/users 200")
        assert features == [21.0, 4.0, 0.0, 3.0]

    def test_empty_line(self) -> None:
        assert extract_log_features("") == [0.0, 0.0, 0.0, 0.0]

    def test_no_digits(self) -> None:
        features = extract_log_features("connection refused upstream")
        assert features[0] == float(len("connection refused upstream"))
        assert features[1] == 0.0
        assert features[3] == 3.0  # noqa: PLR2004

    def test_many_digits_counted(self) -> None:
        features = extract_log_features("retry 3 of 5 for pod 7")
        assert features[1] == 3.0  # noqa: PLR2004

    def test_ms_latency_included(self) -> None:
        features = extract_log_features("query took 250ms to run")
        assert features[2] == 250.0  # noqa: PLR2004

    def test_seconds_latency_normalized_to_ms(self) -> None:
        features = extract_log_features("query took 2s")
        assert features[2] == 2000.0  # noqa: PLR2004

    def test_decimal_seconds_normalized(self) -> None:
        features = extract_log_features("took 1.5s total")
        assert features[2] == 1500.0  # noqa: PLR2004

    def test_single_space_words(self) -> None:
        features = extract_log_features("a b c")
        assert features[0] == 5.0  # noqa: PLR2004
        assert features[3] == 3.0  # noqa: PLR2004


class TestExtractLatencyMsDirect:
    def test_no_match_returns_zero(self) -> None:
        assert _extract_latency_ms("no latency here") == 0.0

    def test_lowercase_ms(self) -> None:
        assert _extract_latency_ms("took 500ms") == 500.0  # noqa: PLR2004

    def test_uppercase_ms(self) -> None:
        assert _extract_latency_ms("took 500MS") == 500.0  # noqa: PLR2004

    def test_lowercase_s(self) -> None:
        assert _extract_latency_ms("took 3s") == 3000.0  # noqa: PLR2004

    def test_uppercase_s(self) -> None:
        assert _extract_latency_ms("took 3S") == 3000.0  # noqa: PLR2004

    def test_mixed_case_unit_ms(self) -> None:
        assert _extract_latency_ms("took 3Ms") == 3.0  # noqa: PLR2004

    def test_decimal_ms(self) -> None:
        assert _extract_latency_ms("took 0.5ms") == 0.5  # noqa: PLR2004

    def test_unit_word_boundary_not_matched(self) -> None:
        assert _extract_latency_ms("100 masses") == 0.0

    def test_first_match_wins(self) -> None:
        assert _extract_latency_ms("took 10ms then 2s") == 10.0  # noqa: PLR2004

    def test_number_without_unit_ignored(self) -> None:
        assert _extract_latency_ms("took 42") == 0.0
