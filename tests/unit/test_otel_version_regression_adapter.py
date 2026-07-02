from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_version_regression_adapter import (
    OTelVersionRegressionAdapter,
)
from hexawyn.application.ports.driven.version_regression_port import VersionRegressionPort
from hexawyn.domain.models.version_regression import VersionComparisonRequest


class TestOTelVersionRegressionAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelVersionRegressionAdapter(), VersionRegressionPort)

    def test_fetch_baseline_returns_default(self) -> None:
        r = OTelVersionRegressionAdapter().fetch_baseline_metrics(
            VersionComparisonRequest(service_name="x")
        )
        assert r.version == "unknown"
        assert r.request_count == 0

    def test_fetch_current_returns_default(self) -> None:
        r = OTelVersionRegressionAdapter().fetch_current_metrics(
            VersionComparisonRequest(service_name="x")
        )
        assert r.version == "unknown"
        assert r.request_count == 0
