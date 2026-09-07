# Auto-generated test for otel_cost_profiling_adapter

from __future__ import annotations


class TestOtelCostProfilingAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.domain.models.cost_profiling import CostProfilingRequest
        from hexawyn.infrastructure.adapters.secondary.gitops.otel_cost_profiling_adapter import (
            OTelCostProfilingAdapter,
        )

        adapter = OTelCostProfilingAdapter()
        result = adapter.fetch_endpoint_cpu_metrics(CostProfilingRequest())
        assert isinstance(result, list)
