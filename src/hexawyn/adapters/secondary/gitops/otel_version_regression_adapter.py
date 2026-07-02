from __future__ import annotations

from hexawyn.application.ports.driven.version_regression_port import VersionRegressionPort
from hexawyn.domain.models.version_regression import VersionComparisonRequest, VersionMetrics


class OTelVersionRegressionAdapter(VersionRegressionPort):
    def fetch_baseline_metrics(self, request: VersionComparisonRequest) -> VersionMetrics:
        return VersionMetrics(
            version="unknown",
            p50_ms=0.0,
            p95_ms=0.0,
            p99_ms=0.0,
            error_rate_pct=0.0,
            request_count=0,
        )

    def fetch_current_metrics(self, request: VersionComparisonRequest) -> VersionMetrics:
        return VersionMetrics(
            version="unknown",
            p50_ms=0.0,
            p95_ms=0.0,
            p99_ms=0.0,
            error_rate_pct=0.0,
            request_count=0,
        )
