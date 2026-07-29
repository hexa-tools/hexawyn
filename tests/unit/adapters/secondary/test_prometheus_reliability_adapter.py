from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.prometheus_reliability_adapter import (
    PrometheusReliabilityAdapter,
    _build_uptime_query,
)
from hexawyn.application.ports.driven.weekly_reliability_report_port import (
    WeeklyReliabilityReportPort,
)


class TestPrometheusReliabilityAdapter:
    def test_implements_port(self) -> None:
        metrics_port = Mock()
        adapter = PrometheusReliabilityAdapter(metrics_query_port=metrics_port)
        assert isinstance(adapter, WeeklyReliabilityReportPort)

    def test_fetch_service_reliability(self) -> None:
        metrics_port = Mock()
        metrics_port.instant_query.return_value = [
            {"metric": {"service": "payments-api"}, "value": 0.995},
            {"metric": {"service": "user-svc"}, "value": 0.998},
        ]
        adapter = PrometheusReliabilityAdapter(metrics_query_port=metrics_port)
        result = adapter.fetch_service_reliability(window_days=7)
        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["service_name"] == "payments-api"
        assert result[0]["uptime_pct"] == 99.5  # noqa: PLR2004
        assert result[1]["service_name"] == "user-svc"
        assert result[1]["uptime_pct"] == 99.8  # noqa: PLR2004

    def test_fetch_service_reliability_exception_returns_empty(self) -> None:
        metrics_port = Mock()
        metrics_port.instant_query.side_effect = Exception("boom")
        adapter = PrometheusReliabilityAdapter(metrics_query_port=metrics_port)
        result = adapter.fetch_service_reliability(window_days=7)
        assert result == []

    def test_fetch_service_reliability_fallback_to_exported_service(self) -> None:
        metrics_port = Mock()
        metrics_port.instant_query.return_value = [
            {"metric": {"exported_service": "ext-svc"}, "value": 0.99},
        ]
        adapter = PrometheusReliabilityAdapter(metrics_query_port=metrics_port)
        result = adapter.fetch_service_reliability(window_days=7)
        assert len(result) == 1
        assert result[0]["service_name"] == "ext-svc"

    def test_fetch_incidents_returns_empty(self) -> None:
        metrics_port = Mock()
        adapter = PrometheusReliabilityAdapter(metrics_query_port=metrics_port)
        result = adapter.fetch_incidents(window_days=7)
        assert result == []


class TestBuildUptimeQuery:
    def test_builds_promql(self) -> None:
        query = _build_uptime_query(604800)
        assert 'code!~"5.."' in query
        assert "604800" in query
