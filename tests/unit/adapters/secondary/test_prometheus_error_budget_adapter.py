"""RED → GREEN — PrometheusErrorBudgetAdapter unit tests."""

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.gitops.prometheus_error_budget_adapter import (
    PrometheusErrorBudgetAdapter,
    _build_success_rate_query,
)
from hexawyn.application.ports.driven.error_budget_port import ErrorBudgetPort
from hexawyn.application.ports.driven.metrics_query_port import PrometheusInstantSample


def _instant_sample(value: float, total_requests: int = 0) -> PrometheusInstantSample:
    return PrometheusInstantSample(
        metric={"service": "test", "total_requests": str(total_requests)},
        value=value,
    )


class TestPrometheusErrorBudgetAdapter:
    def test_implements_error_budget_port(self) -> None:
        adapter = PrometheusErrorBudgetAdapter(metrics_query_port=MagicMock())
        assert isinstance(adapter, ErrorBudgetPort)

    def test_fetch_success_rate_returns_data(self) -> None:
        mock_metrics = MagicMock()
        mock_metrics.instant_query.return_value = [_instant_sample(0.995, 100000)]

        adapter = PrometheusErrorBudgetAdapter(metrics_query_port=mock_metrics)
        result = adapter.fetch_success_rate("payment-service", 30)

        assert result["service_name"] == "payment-service"
        assert result["has_data"] is True
        assert result["success_rate"] == 0.995  # noqa: PLR2004
        assert result["error_rate"] == 0.005  # noqa: PLR2004
        assert result["observation_days"] == 30  # noqa: PLR2004

    def test_fetch_success_rate_propagates_window(self) -> None:
        mock_metrics = MagicMock()
        mock_metrics.instant_query.return_value = [_instant_sample(1.0, 50000)]

        adapter = PrometheusErrorBudgetAdapter(metrics_query_port=mock_metrics)
        result = adapter.fetch_success_rate("auth-svc", 7)

        assert result["observation_days"] == 7  # noqa: PLR2004
        assert result["success_rate"] == 1.0
        assert result["error_rate"] == 0.0
        assert result["has_data"] is True

    def test_empty_prometheus_response_returns_no_data(self) -> None:
        mock_metrics = MagicMock()
        mock_metrics.instant_query.return_value = []

        adapter = PrometheusErrorBudgetAdapter(metrics_query_port=mock_metrics)
        result = adapter.fetch_success_rate("missing-svc", 30)

        assert result["has_data"] is False
        assert result["total_requests"] == 0
        assert result["success_rate"] == 0.0

    def test_prometheus_exception_returns_no_data(self) -> None:
        mock_metrics = MagicMock()
        mock_metrics.instant_query.side_effect = RuntimeError("connection refused")

        adapter = PrometheusErrorBudgetAdapter(metrics_query_port=mock_metrics)
        result = adapter.fetch_success_rate("broken-svc", 30)

        assert result["has_data"] is False
        assert result["total_requests"] == 0

    def test_computes_failed_requests_from_error_rate(self) -> None:
        mock_metrics = MagicMock()
        mock_metrics.instant_query.return_value = [
            _instant_sample(0.95, 10000)  # 95% success → 5% error
        ]

        adapter = PrometheusErrorBudgetAdapter(metrics_query_port=mock_metrics)
        result = adapter.fetch_success_rate("svc", 30)

        assert result["successful_requests"] == 9500  # noqa: PLR2004
        assert result["failed_requests"] == 500  # noqa: PLR2004
        assert result["total_requests"] == 10000  # noqa: PLR2004

    def test_zero_requests_avoids_division_by_zero(self) -> None:
        mock_metrics = MagicMock()
        mock_metrics.instant_query.return_value = [_instant_sample(0.0, 0)]

        adapter = PrometheusErrorBudgetAdapter(metrics_query_port=mock_metrics)
        result = adapter.fetch_success_rate("empty-svc", 30)

        assert result["has_data"] is True
        assert result["failed_requests"] == 0
        assert result["successful_requests"] == 0


class TestBuildSuccessRateQuery:
    def test_builds_promql_with_service_and_window(self) -> None:
        query = _build_success_rate_query("payment-service", 2592000)

        assert "payment-service" in query
        assert 'code!~"5.."' in query
        assert "2592000s" in query
        assert "http_requests_total" in query

    def test_uses_rate_function(self) -> None:
        query = _build_success_rate_query("auth", 86400)

        assert "rate(" in query
        assert "[86400s]" in query
        assert " / " in query
