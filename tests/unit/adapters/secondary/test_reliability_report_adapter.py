"""RED → GREEN — PrometheusReliabilityAdapter unit tests."""

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.gitops.prometheus_reliability_adapter import (
    PrometheusReliabilityAdapter,
    _build_uptime_query,
)
from hexawyn.application.ports.driven.metrics_query_port import PrometheusInstantSample
from hexawyn.application.ports.driven.weekly_reliability_report_port import (
    WeeklyReliabilityReportPort,
)


def _sample(value: float, service: str = "payment-service") -> PrometheusInstantSample:
    return PrometheusInstantSample(
        metric={"service": service},
        value=value,
    )


class TestPrometheusReliabilityAdapter:
    def test_implements_weekly_reliability_report_port(self) -> None:
        adapter = PrometheusReliabilityAdapter(metrics_query_port=MagicMock())
        assert isinstance(adapter, WeeklyReliabilityReportPort)

    def test_fetch_service_reliability_returns_data(self) -> None:
        mock_metrics = MagicMock()
        mock_metrics.instant_query.return_value = [
            _sample(0.9992, "payment-service"),
            _sample(0.9972, "auth-service"),
        ]

        adapter = PrometheusReliabilityAdapter(metrics_query_port=mock_metrics)
        result = adapter.fetch_service_reliability(7)

        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["service_name"] == "payment-service"
        assert result[0]["uptime_pct"] == 99.92  # noqa: PLR2004
        assert result[1]["slo_target"] == 99.9  # noqa: PLR2004

    def test_fetch_service_reliability_empty_result(self) -> None:
        mock_metrics = MagicMock()
        mock_metrics.instant_query.return_value = []

        adapter = PrometheusReliabilityAdapter(metrics_query_port=mock_metrics)
        result = adapter.fetch_service_reliability(7)

        assert result == []

    def test_prometheus_exception_returns_empty(self) -> None:
        mock_metrics = MagicMock()
        mock_metrics.instant_query.side_effect = RuntimeError("timeout")

        adapter = PrometheusReliabilityAdapter(metrics_query_port=mock_metrics)
        result = adapter.fetch_service_reliability(7)

        assert result == []

    def test_fetch_incidents_returns_empty_list(self) -> None:
        adapter = PrometheusReliabilityAdapter(metrics_query_port=MagicMock())

        result = adapter.fetch_incidents(7)

        assert result == []

    def test_computes_error_rate_from_uptime(self) -> None:
        mock_metrics = MagicMock()
        mock_metrics.instant_query.return_value = [_sample(0.95, "degraded-svc")]

        adapter = PrometheusReliabilityAdapter(metrics_query_port=mock_metrics)
        result = adapter.fetch_service_reliability(7)

        assert result[0]["uptime_pct"] == 95.0  # noqa: PLR2004
        assert result[0]["error_rate"] == 5.0  # noqa: PLR2004

    def test_falls_back_to_exported_service_label(self) -> None:
        mock_metrics = MagicMock()
        mock_metrics.instant_query.return_value = [
            PrometheusInstantSample(
                metric={"exported_service": "exported-svc"},
                value=0.999,
            ),
        ]

        adapter = PrometheusReliabilityAdapter(metrics_query_port=mock_metrics)
        result = adapter.fetch_service_reliability(7)

        assert result[0]["service_name"] == "exported-svc"


class TestBuildUptimeQuery:
    def test_includes_window_in_seconds(self) -> None:
        query = _build_uptime_query(604800)
        assert "[604800s]" in query

    def test_excludes_5xx_codes(self) -> None:
        query = _build_uptime_query(86400)
        assert 'code!~"5.."' in query
