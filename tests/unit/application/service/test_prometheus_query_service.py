"""Unit tests for PrometheusQueryService (mocks MetricsQueryPort)."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.service.prometheus_query_service import PrometheusQueryService


class TestInstantQuery:
    def test_valid_query_returns_labeled_results(self) -> None:
        port = MagicMock()
        port.instant_query.return_value = [
            {"metric": {"pod": "payment-pod-abc", "container": "app"}, "value": 0.0032},
            {"metric": {"pod": "payment-pod-def", "container": "app"}, "value": 0.0015},
        ]
        service = PrometheusQueryService(port=port)

        response = service.execute(
            ExecutePrometheusQueryCommand(
                promql='rate(container_cpu_usage_seconds_total{namespace="payment"}[5m])',
                unit_hint="cores",
            )
        )

        assert response.error is None
        assert response.result_count == 2
        assert response.results[0]["labels"] == {"pod": "payment-pod-abc", "container": "app"}
        assert response.results[0]["formatted_value"] == "3.2m cores"
        port.instant_query.assert_called_once_with(
            'rate(container_cpu_usage_seconds_total{namespace="payment"}[5m])',
            timeout_seconds=15.0,
        )

    def test_empty_result_returns_no_data(self) -> None:
        port = MagicMock()
        port.instant_query.return_value = []
        service = PrometheusQueryService(port=port)

        response = service.execute(ExecutePrometheusQueryCommand(promql='up{job="ghost"}'))

        assert response.no_data is True
        assert response.result_count == 0
        assert "ghost" in response.summary


class TestRangeQuery:
    def test_range_query_returns_series_with_timestamps(self) -> None:
        port = MagicMock()
        port.range_query.return_value = [
            {
                "metric": {"pod": "payment-pod-abc"},
                "values": [("2024-06-01T14:00:00Z", 0.001), ("2024-06-01T14:01:00Z", 0.002)],
            }
        ]
        service = PrometheusQueryService(port=port)

        response = service.execute(
            ExecutePrometheusQueryCommand(
                promql="rate(container_cpu_usage_seconds_total[5m])",
                query_type="range",
                start="2024-06-01T14:00:00Z",
                end="2024-06-01T14:05:00Z",
                step="30s",
            )
        )

        assert response.query_type == "range"
        assert response.results[0]["values"] == [
            ("2024-06-01T14:00:00Z", 0.001),
            ("2024-06-01T14:01:00Z", 0.002),
        ]
        port.range_query.assert_called_once_with(
            "rate(container_cpu_usage_seconds_total[5m])",
            start="2024-06-01T14:00:00Z",
            end="2024-06-01T14:05:00Z",
            step="30s",
            timeout_seconds=15.0,
        )

    def test_port_failure_propagates(self) -> None:
        import pytest

        port = MagicMock()
        port.instant_query.side_effect = RuntimeError("Prometheus unreachable")
        service = PrometheusQueryService(port=port)

        with pytest.raises(RuntimeError, match="Prometheus unreachable"):
            service.execute(ExecutePrometheusQueryCommand(promql="up"))


class TestPrometheusQueryServiceEdgeCases:
    def test_empty_promql_query(self) -> None:
        port = MagicMock()
        port.instant_query.return_value = []
        service = PrometheusQueryService(port=port)

        response = service.execute(ExecutePrometheusQueryCommand(promql=""))

        assert response.result_count == 0
        assert response.query == ""

    def test_range_query_failure_propagates(self) -> None:
        import pytest

        port = MagicMock()
        port.range_query.side_effect = RuntimeError("Prometheus range query timeout")
        service = PrometheusQueryService(port=port)

        with pytest.raises(RuntimeError, match="Prometheus range query timeout"):
            service.execute(
                ExecutePrometheusQueryCommand(
                    promql="rate(cpu[5m])",
                    query_type="range",
                    start="2024-01-01T00:00:00Z",
                    end="2024-01-01T01:00:00Z",
                    step="60s",
                )
            )

    def test_custom_timeout_seconds_passed(self) -> None:
        port = MagicMock()
        port.instant_query.return_value = []
        service = PrometheusQueryService(port=port)

        service.execute(ExecutePrometheusQueryCommand(promql="up", timeout_seconds=30.0))

        port.instant_query.assert_called_once_with("up", timeout_seconds=30.0)
