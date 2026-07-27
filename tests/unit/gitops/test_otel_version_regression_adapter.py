# Auto-generated test for otel_version_regression_adapter

from __future__ import annotations


class TestOtelVersionRegressionAdapterUnit:
    def test_returns_metrics(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_version_regression_adapter import (
            OTelVersionRegressionAdapter,
        )
        from hexawyn.domain.models.version_regression import VersionComparisonRequest

        adapter = OTelVersionRegressionAdapter()
        result = adapter.fetch_baseline_metrics(VersionComparisonRequest(service_name="test"))
        assert result.p50_ms >= 0.0
