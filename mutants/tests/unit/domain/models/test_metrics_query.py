"""Unit tests for Prometheus metrics-query domain models (pure dataclasses)."""

from __future__ import annotations

from hexawyn.domain.models.metrics_query import (
    PrometheusMetricResult,
    PrometheusQueryRequest,
    PrometheusQueryResult,
)


class TestPrometheusMetricResult:
    def test_instant_result_fields(self) -> None:
        result = PrometheusMetricResult(
            labels={"pod": "payment-pod-abc", "container": "app"},
            value=0.0032,
            formatted_value="3.2m cores",
        )
        assert result.labels == {"pod": "payment-pod-abc", "container": "app"}
        assert result.value == 0.0032  # noqa: PLR2004
        assert result.values == []
        assert result.formatted_value == "3.2m cores"

    def test_range_result_fields(self) -> None:
        result = PrometheusMetricResult(
            labels={"pod": "payment-pod-abc"},
            values=[("2024-06-01T14:00:00Z", 0.001), ("2024-06-01T14:01:00Z", 0.002)],
        )
        assert result.value is None
        assert len(result.values) == 2  # noqa: PLR2004


class TestPrometheusQueryRequest:
    def test_defaults(self) -> None:
        request = PrometheusQueryRequest(promql="up")
        assert request.query_type == "instant"
        assert request.start is None
        assert request.end is None
        assert request.step == "15s"
        assert request.unit_hint == "raw"

    def test_range_query_values(self) -> None:
        request = PrometheusQueryRequest(
            promql="rate(container_cpu_usage_seconds_total[5m])",
            query_type="range",
            start="2024-06-01T14:00:00Z",
            end="2024-06-01T14:05:00Z",
            step="30s",
            unit_hint="cores",
        )
        assert request.query_type == "range"
        assert request.start == "2024-06-01T14:00:00Z"
        assert request.unit_hint == "cores"


class TestPrometheusQueryResult:
    def test_defaults(self) -> None:
        result = PrometheusQueryResult(query="up", query_type="instant")
        assert result.results == []
        assert result.result_count == 0
        assert result.truncated is False
        assert result.no_data is False
        assert result.summary == ""

    def test_with_results(self) -> None:
        sample = PrometheusMetricResult(labels={"pod": "payment-pod-abc"}, value=0.0032)
        result = PrometheusQueryResult(
            query="rate(container_cpu_usage_seconds_total[5m])",
            query_type="instant",
            results=[sample],
            result_count=1,
        )
        assert len(result.results) == 1
        assert result.result_count == 1
