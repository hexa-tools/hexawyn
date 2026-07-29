from __future__ import annotations

from unittest.mock import patch

from hexawyn.adapters.secondary.gitops.service_cost_prometheus_adapter import (
    ServiceCostPrometheusAdapter,
)
from hexawyn.application.ports.driven.service_cost_port import ServiceCostPort


class TestServiceCostPrometheusAdapter:
    def test_implements_port(self) -> None:
        adapter = ServiceCostPrometheusAdapter()
        assert isinstance(adapter, ServiceCostPort)

    def test_fetch_pod_resources_with_data(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.gitops.service_cost_prometheus_adapter.query_prometheus_instant"
        ) as mock_query:
            mock_query.side_effect = [
                [
                    {
                        "name": "cpu",
                        "value": 0.5,
                        "labels": {"pod": "app-pod", "namespace": "default"},
                    }
                ],  # noqa: E501
                [
                    {
                        "name": "mem",
                        "value": 100000000.0,
                        "labels": {"pod": "app-pod", "namespace": "default"},
                    }
                ],  # noqa: E501
            ]

            adapter = ServiceCostPrometheusAdapter()
            result = adapter.fetch_pod_resources("test-svc", "2026-07")

            assert len(result) == 1
            assert result[0]["namespace"] == "default"
            assert result[0]["cpu_cores"] == 0.5  # noqa: PLR2004
            assert result[0]["memory_mib"] == round(100000000.0 / (1024 * 1024), 2)

    def test_fetch_pod_resources_empty_on_error(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.gitops.service_cost_prometheus_adapter.query_prometheus_instant",
            side_effect=Exception("timeout"),
        ):
            adapter = ServiceCostPrometheusAdapter()
            result = adapter.fetch_pod_resources("test-svc", "2026-07")
            assert result == []

    def test_fetch_pod_resources_empty_service_name(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.gitops.service_cost_prometheus_adapter.query_prometheus_instant"
        ) as mock_query:
            mock_query.return_value = []
            adapter = ServiceCostPrometheusAdapter()
            result = adapter.fetch_pod_resources("", "2026-07")
            assert result == []

    def test_fetch_pod_resources_no_pods(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.gitops.service_cost_prometheus_adapter.query_prometheus_instant"
        ) as mock_query:
            mock_query.return_value = []
            adapter = ServiceCostPrometheusAdapter()
            result = adapter.fetch_pod_resources("unknown-svc", "2026-07")
            assert result == []
