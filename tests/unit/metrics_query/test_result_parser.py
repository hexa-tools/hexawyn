"""Unit tests for parse_instant_results / parse_range_results (pure — no HTTP)."""

from __future__ import annotations

from hexawyn.domain.services.metrics_query.result_parser import (
    parse_instant_results,
    parse_range_results,
)


class TestParseInstantResults:
    def test_valid_results_returned_with_labels_and_values(self) -> None:
        raw = [
            {"metric": {"pod": "payment-pod-abc", "container": "app"}, "value": 0.0032},
            {"metric": {"pod": "payment-pod-def", "container": "app"}, "value": 0.0015},
        ]

        result = parse_instant_results(raw, promql="rate(...)", unit_hint="cores")

        assert result.result_count == 2
        assert result.no_data is False
        assert result.results[0].labels == {"pod": "payment-pod-abc", "container": "app"}
        assert result.results[0].value == 0.0032
        assert result.results[0].formatted_value == "3.2m cores"

    def test_empty_result_returns_clear_no_data_message(self) -> None:
        result = parse_instant_results([], promql='up{job="ghost"}', unit_hint="raw")

        assert result.no_data is True
        assert result.result_count == 0
        assert "ghost" in result.summary
        assert "No data" in result.summary

    def test_more_than_max_results_is_truncated(self) -> None:
        raw = [{"metric": {"pod": f"pod-{i}"}, "value": 1.0} for i in range(10_001)]

        result = parse_instant_results(raw, promql="up", unit_hint="raw")

        assert result.truncated is True
        assert result.result_count == 10_000
        assert "truncated" in result.summary.lower()


class TestParseRangeResults:
    def test_range_series_includes_timestamps(self) -> None:
        raw = [
            {
                "metric": {"pod": "payment-pod-abc"},
                "values": [("2024-06-01T14:00:00Z", 0.001), ("2024-06-01T14:01:00Z", 0.002)],
            }
        ]

        result = parse_range_results(raw, promql="rate(...)[5m]", unit_hint="cores")

        assert result.query_type == "range"
        assert result.result_count == 1
        assert result.results[0].values == [
            ("2024-06-01T14:00:00Z", 0.001),
            ("2024-06-01T14:01:00Z", 0.002),
        ]

    def test_empty_range_result_returns_no_data(self) -> None:
        result = parse_range_results([], promql="up", unit_hint="raw")

        assert result.no_data is True
        assert result.result_count == 0
