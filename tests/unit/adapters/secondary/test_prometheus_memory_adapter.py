from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.adapters.secondary.gitops.prometheus_memory_adapter import (
    PrometheusMemoryAdapter,
)
from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort


class TestPrometheusMemoryAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(PrometheusMemoryAdapter(), MemorySaturationPort)

    def test_fetch_memory_metrics_with_data(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.gitops.prometheus_memory_adapter.query_prometheus_instant"
        ) as mock_query:
            mock_query.return_value = [
                {
                    "name": "memory",
                    "value": 500000000.0,
                    "labels": {"pod": "test-pod", "namespace": "default"},
                },  # noqa: E501
                {
                    "name": "memory",
                    "value": 200000000.0,
                    "labels": {"pod": "other-pod", "namespace": "default"},
                },  # noqa: E501
            ]
            adapter = PrometheusMemoryAdapter()
            request = MagicMock()
            request.namespace = "default"
            request.pod_name = "test-pod"

            result = adapter.fetch_memory_metrics(request)

            assert len(result) == 2  # noqa: PLR2004
            assert result[0]["pod"] == "test-pod"
            assert result[0]["memory_mib"] == round(500000000.0 / (1024 * 1024), 2)
            assert result[1]["memory_mib"] == round(200000000.0 / (1024 * 1024), 2)

    def test_fetch_memory_metrics_empty_on_error(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.gitops.prometheus_memory_adapter.query_prometheus_instant",
            side_effect=Exception("timeout"),
        ):
            adapter = PrometheusMemoryAdapter()
            request = MagicMock()
            request.namespace = "default"
            request.pod_name = ""

            result = adapter.fetch_memory_metrics(request)
            assert result == []

    def test_fetch_memory_metrics_empty_pod_name(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.gitops.prometheus_memory_adapter.query_prometheus_instant"
        ) as mock_query:
            mock_query.return_value = []
            adapter = PrometheusMemoryAdapter()
            request = MagicMock()
            request.namespace = "default"
            request.pod_name = ""

            result = adapter.fetch_memory_metrics(request)
            assert result == []

    def test_correlate_with_otel_returns_none(self) -> None:
        adapter = PrometheusMemoryAdapter()
        result = adapter.correlate_with_otel("test-pod", "default")
        assert result is None

    def test_correlate_with_otel_empty_params(self) -> None:
        adapter = PrometheusMemoryAdapter()
        result = adapter.correlate_with_otel("", "")
        assert result is None
