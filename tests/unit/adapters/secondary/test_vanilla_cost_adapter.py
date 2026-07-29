from __future__ import annotations

from hexawyn.adapters.secondary.vanilla.vanilla_cost_adapter import VanillaCostAdapter
from hexawyn.application.ports.driven.cost_estimation_port import CostEstimationPort


class TestVanillaCostAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(VanillaCostAdapter(), CostEstimationPort)

    def test_returns_zero_cost_report(self) -> None:
        adapter = VanillaCostAdapter()
        result = adapter.estimate_cluster_cost("test-cluster")

        assert result["cluster_name"] == "test-cluster"
        assert result["namespace_costs"] == []
        assert result["total_monthly_cost_usd"] == 0.0
        assert result["data_source"] == "vanilla"
        assert result["currency"] == "USD"
