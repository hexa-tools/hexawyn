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


class TestCalicoPrometheusAdapterFelixCounters:
    def _sample(self, policy: str, kind: str, value: float) -> dict:
        return {"metric": {"policy": policy}, "value": value, "kind": kind}

    def test_felix_policy_counters_available(self) -> None:
        mq = MagicMock()
        mq.instant_query.side_effect = [
            [self._sample("a", "deny_packets", 10)],
            [self._sample("a", "allow_packets", 5)],
            [],
            [],
        ]
        adapter = CalicoPrometheusAdapter(metrics_query_port=mq)
        result = adapter.felix_policy_counters()
        assert result["available"] is True
        assert mq.instant_query.call_count >= 2  # noqa: PLR2004

    def test_felix_policy_counters_without_port(self) -> None:
        adapter = CalicoPrometheusAdapter(metrics_query_port=None)
        result = adapter.felix_policy_counters()
        assert result["available"] is False
        assert "message" in result

    def test_felix_policy_counters_on_error(self) -> None:
        mq = MagicMock()
        mq.instant_query.side_effect = RuntimeError("boom")
        adapter = CalicoPrometheusAdapter(metrics_query_port=mq)
        result = adapter.felix_policy_counters()
        assert result["available"] is False
        assert "boom" in str(result.get("message"))

    def test_felix_policy_counters_skips_non_numeric(self) -> None:
        mq = MagicMock()
        mq.instant_query.side_effect = [
            [{"metric": {"policy": "a"}, "value": "not-a-number"}],
            [],
            [],
            [],
        ]
        adapter = CalicoPrometheusAdapter(metrics_query_port=mq)
        result = adapter.felix_policy_counters()
        assert result["available"] is True
        assert result["samples"] == []

    def test_felix_policy_counters_unknown_policy_label(self) -> None:
        mq = MagicMock()
        mq.instant_query.side_effect = [
            [{"metric": {}, "value": 7}],
            [],
            [],
            [],
        ]
        adapter = CalicoPrometheusAdapter(metrics_query_port=mq)
        result = adapter.felix_policy_counters()
        assert result["samples"][0]["policy"] == "unknown"
        assert result["samples"][0]["kind"] == "deny_packets"
