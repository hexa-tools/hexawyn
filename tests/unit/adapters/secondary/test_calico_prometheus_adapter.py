"""Tests for CalicoPrometheusAdapter — felix metrics via Prometheus."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.calico.calico_prometheus_adapter import CalicoPrometheusAdapter
from hexawyn.domain.errors import HexawynError, PrometheusUnavailableError


class TestCalicoPrometheusAdapter:
    def test_felix_metrics_available(self) -> None:
        mq = MagicMock()
        mq.instant_query.return_value = [
            {"metric": {"instance": "node-1"}, "value": 12.0},
            {"metric": {"instance": "node-2"}, "value": 8.0},
        ]
        adapter = CalicoPrometheusAdapter(metrics_query_port=mq)

        result = adapter.felix_metrics()

        assert result["available"] is True
        metrics = result["metrics"]
        assert isinstance(metrics, dict)
        assert mq.instant_query.call_count >= 1

    def test_felix_metrics_handles_hexawyn_error(self) -> None:
        mq = MagicMock()
        mq.instant_query.side_effect = PrometheusUnavailableError("http://prom:9090")
        adapter = CalicoPrometheusAdapter(metrics_query_port=mq)

        result = adapter.felix_metrics()

        assert result["available"] is False
        assert "error" in result

    def test_felix_metrics_without_port(self) -> None:
        adapter = CalicoPrometheusAdapter(metrics_query_port=None)
        result = adapter.felix_metrics()
        assert result["available"] is False

    def test_connectivity_health_available(self) -> None:
        mq = MagicMock()
        mq.instant_query.return_value = [{"metric": {}, "value": 1.0}]
        adapter = CalicoPrometheusAdapter(metrics_query_port=mq)

        result = adapter.connectivity_health()

        assert result["available"] is True
        assert result["status"] in ("healthy", "degraded")

    def test_connectivity_health_degraded_on_error(self) -> None:
        mq = MagicMock()
        mq.instant_query.side_effect = HexawynError("boom")
        adapter = CalicoPrometheusAdapter(metrics_query_port=mq)

        result = adapter.connectivity_health()

        assert result["available"] is False
        assert result["status"] == "degraded"

    def test_connectivity_health_without_port(self) -> None:
        adapter = CalicoPrometheusAdapter(metrics_query_port=None)
        assert adapter.connectivity_health()["available"] is False

    def test_unknown_error_is_translated(self) -> None:
        mq = MagicMock()
        mq.instant_query.side_effect = RuntimeError("nope")
        adapter = CalicoPrometheusAdapter(metrics_query_port=mq)
        result = adapter.felix_metrics()
        assert result["available"] is False
        assert isinstance(result.get("error"), str)
