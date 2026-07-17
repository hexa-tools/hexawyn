from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_canary_comparison_adapter import (
    OTelCanaryComparisonAdapter,
)
from hexawyn.application.ports.driven.canary_comparison_port import (
    CanaryComparisonPort,
)
from hexawyn.domain.models.canary_comparison import CanaryComparisonRequest


class TestOTelCanaryComparisonAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelCanaryComparisonAdapter(), CanaryComparisonPort)

    def test_fetch_stable_returns_default(self) -> None:
        adapter = OTelCanaryComparisonAdapter()
        req = CanaryComparisonRequest(service_name="test-svc")
        result = adapter.fetch_stable_metrics(req)
        assert result.version == "unknown"
        assert result.request_count == 0

    def test_fetch_canary_returns_default(self) -> None:
        adapter = OTelCanaryComparisonAdapter()
        req = CanaryComparisonRequest(service_name="test-svc")
        result = adapter.fetch_canary_metrics(req)
        assert result.version == "unknown"
        assert result.request_count == 0
