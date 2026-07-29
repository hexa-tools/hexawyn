from __future__ import annotations


class TestOtelCanaryComparisonAdapter:
    def test_fetch_canary_metrics_returns_version_metrics(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_canary_comparison_adapter import (
            OTelCanaryComparisonAdapter,
        )
        from hexawyn.domain.models.canary_comparison import CanaryComparisonRequest

        adapter = OTelCanaryComparisonAdapter()
        result = adapter.fetch_canary_metrics(CanaryComparisonRequest(service_name="test"))

        assert result.version in ("canary", "unknown")
        assert result.request_count >= 0

    def test_fetch_stable_metrics_returns_version_metrics(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_canary_comparison_adapter import (
            OTelCanaryComparisonAdapter,
        )
        from hexawyn.domain.models.canary_comparison import CanaryComparisonRequest

        adapter = OTelCanaryComparisonAdapter()
        result = adapter.fetch_stable_metrics(CanaryComparisonRequest(service_name="test"))

        assert result.version in ("stable", "unknown")
