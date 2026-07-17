from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_cost_profiling_adapter import (
    OTelCostProfilingAdapter,
)
from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort
from hexawyn.domain.models.cost_profiling import CostProfilingRequest


class TestOTelCostProfilingAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelCostProfilingAdapter(), CostProfilingPort)

    def test_fetch_returns_empty(self) -> None:
        adapter = OTelCostProfilingAdapter()
        result = adapter.fetch_endpoint_cpu_metrics(
            CostProfilingRequest(time_window_minutes=60, top_n=5)
        )
        assert result == []
