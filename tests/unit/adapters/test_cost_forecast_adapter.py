from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.vanilla.adapters.cost_forecast_adapter import (
    VanillaCostForecastAdapter,
)
from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort
from hexawyn.domain.errors import ClusterUnreachableError


class _FakeDeployment:
    def __init__(self, namespace: str, cpu: str, mem: str) -> None:
        container = MagicMock()
        container_resources = MagicMock()
        container_resources.requests = {"cpu": cpu, "memory": mem}
        container.resources = container_resources

        spec = MagicMock()
        spec.containers = [container]
        template = MagicMock()
        template.spec = spec
        dep_spec = MagicMock()
        dep_spec.template = template

        self.spec = dep_spec
        self.metadata = MagicMock()
        self.metadata.namespace = namespace


def _fake_items(api_response: object) -> list[object]:
    items = getattr(api_response, "items", [])
    if isinstance(items, list):
        return items
    return []


class TestVanillaCostForecastAdapter:
    def test_implements_cost_forecast_port(self) -> None:
        api = MagicMock()
        adapter = VanillaCostForecastAdapter(api=api)
        assert isinstance(adapter, CostForecastPort)

    def test_get_daily_costs_returns_expected_count(self) -> None:
        api = MagicMock()
        deploy = _FakeDeployment(namespace="default", cpu="500m", mem="512Mi")
        response = MagicMock()
        response.items = [deploy]
        api.list_deployment_for_all_namespaces.return_value = response

        adapter = VanillaCostForecastAdapter(api=api)
        result = adapter.get_daily_costs(days=7)

        assert len(result) == 7  # noqa: PLR2004
        for entry in result:
            assert isinstance(entry, dict)
            assert "date" in entry
            assert "total_usd" in entry
            assert "namespace_costs" in entry
        assert all(entry["total_usd"] > 0 for entry in result)

    def test_get_daily_costs_empty_deployments_returns_zero_costs(self) -> None:
        api = MagicMock()
        response = MagicMock()
        response.items = []
        api.list_deployment_for_all_namespaces.return_value = response

        adapter = VanillaCostForecastAdapter(api=api)
        result = adapter.get_daily_costs(days=3)

        assert len(result) == 3  # noqa: PLR2004
        for entry in result:
            assert entry["total_usd"] == 0.0
            assert entry["namespace_costs"] == []

    def test_get_daily_costs_api_error_raises_cluster_unreachable(self) -> None:
        api = MagicMock()
        api.list_deployment_for_all_namespaces.side_effect = OSError("Connection refused")

        adapter = VanillaCostForecastAdapter(api=api)
        with pytest.raises(ClusterUnreachableError):
            adapter.get_daily_costs(days=7)

    def test_prometheus_url_stored(self) -> None:
        api = MagicMock()
        adapter = VanillaCostForecastAdapter(api=api, prometheus_url="http://prom:9090")
        assert adapter._prometheus_url == "http://prom:9090"

    def test_prometheus_url_defaults_to_empty(self) -> None:
        api = MagicMock()
        adapter = VanillaCostForecastAdapter(api=api)
        assert adapter._prometheus_url == ""
