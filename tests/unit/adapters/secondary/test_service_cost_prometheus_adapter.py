"""RED → GREEN — ServiceCostPrometheusAdapter unit tests."""

from hexawyn.adapters.secondary.gitops.service_cost_prometheus_adapter import (
    ServiceCostPrometheusAdapter,
)
from hexawyn.application.ports.driven.service_cost_port import ServiceCostPort


class TestServiceCostPrometheusAdapter:
    def test_implements_port(self) -> None:
        adapter = ServiceCostPrometheusAdapter()
        assert isinstance(adapter, ServiceCostPort)

    def test_fetch_pod_resources_returns_empty(self) -> None:
        adapter = ServiceCostPrometheusAdapter()
        result = adapter.fetch_pod_resources("test-svc", "2026-07")
        assert result == []
