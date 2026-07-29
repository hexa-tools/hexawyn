# Auto-generated test for otel_cost_profiling_adapter

from __future__ import annotations


class TestOtelCostProfilingAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_cost_profiling_adapter import (
            OTelCostProfilingAdapter,
        )
        from hexawyn.domain.models.cost_profiling import CostProfilingRequest

        adapter = OTelCostProfilingAdapter()
        result = adapter.fetch_endpoint_cpu_metrics(CostProfilingRequest())
        assert isinstance(result, list)
